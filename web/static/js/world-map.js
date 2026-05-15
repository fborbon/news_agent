/* world-map.js — D3 v7 interactive world map for Global News Intelligence */
(function () {
  'use strict';

  /* ── ISO numeric → region key for all 57 covered countries ───────────── */
  const REGION_BY_ISO = {
    840: 'usa',
    826: 'uk',
    250: 'france',
    276: 'germany',
    724: 'spain',
    392: 'japan',
    156: 'china',
    380: 'italy',
    124: 'canada',
    484: 'mexico',
     76: 'brazil',
    188: 'costa_rica',
    356: 'india',
     36: 'australia',
    158: 'taiwan',
    702: 'singapore',
    410: 'south_korea',
    643: 'russia',
    804: 'ukraine',
    792: 'turkey',
    682: 'saudi_arabia',
    364: 'iran',
    784: 'uae',
    710: 'south_africa',
    504: 'morocco',
    818: 'egypt',
     32: 'argentina',
    170: 'colombia',
    152: 'chile',
    604: 'peru',
    360: 'indonesia',
    586: 'pakistan',
    764: 'thailand',
    704: 'vietnam',
    458: 'malaysia',
    608: 'philippines',
     50: 'bangladesh',
    554: 'new_zealand',
    528: 'netherlands',
    620: 'portugal',
    616: 'poland',
    752: 'sweden',
    578: 'norway',
    208: 'denmark',
    756: 'switzerland',
     40: 'austria',
     56: 'belgium',
    300: 'greece',
    376: 'israel',
    368: 'iraq',
    634: 'qatar',
    566: 'nigeria',
    404: 'kenya',
    231: 'ethiopia',
    288: 'ghana',
     12: 'algeria',
    788: 'tunisia',
  };

  /* ── Names for uncovered countries (ISO numeric key) ─────────────────── */
  const COUNTRY_NAMES = {
      4: 'Afghanistan',
      8: 'Albania',
     12: 'Algeria',         // covered — fallback label
     20: 'Andorra',
     24: 'Angola',
     32: 'Argentina',       // covered — fallback label
     36: 'Australia',       // covered
     40: 'Austria',         // covered
     50: 'Bangladesh',      // covered
     56: 'Belgium',         // covered
     64: 'Bhutan',
     68: 'Bolivia',
     76: 'Brazil',          // covered
     84: 'Belize',
    100: 'Bulgaria',
    104: 'Myanmar',
    116: 'Cambodia',
    120: 'Cameroon',
    124: 'Canada',          // covered
    140: 'Central African Rep.',
    144: 'Sri Lanka',
    148: 'Chad',
    152: 'Chile',           // covered
    156: 'China',           // covered
    170: 'Colombia',        // covered
    178: 'Congo',
    180: 'DR Congo',
    188: 'Costa Rica',      // covered
    191: 'Croatia',
    192: 'Cuba',
    203: 'Czech Republic',
    204: 'Benin',
    208: 'Denmark',         // covered
    214: 'Dominican Republic',
    218: 'Ecuador',
    222: 'El Salvador',
    231: 'Ethiopia',        // covered
    232: 'Eritrea',
    233: 'Estonia',
    246: 'Finland',
    250: 'France',          // covered
    262: 'Djibouti',
    266: 'Gabon',
    270: 'Gambia',
    276: 'Germany',         // covered
    288: 'Ghana',           // covered
    300: 'Greece',          // covered
    320: 'Guatemala',
    324: 'Guinea',
    328: 'Guyana',
    332: 'Haiti',
    340: 'Honduras',
    344: 'Hong Kong',
    348: 'Hungary',
    352: 'Iceland',
    356: 'India',           // covered
    360: 'Indonesia',       // covered
    364: 'Iran',            // covered
    368: 'Iraq',            // covered
    372: 'Ireland',
    376: 'Israel',          // covered
    380: 'Italy',           // covered
    388: 'Jamaica',
    392: 'Japan',           // covered
    398: 'Kazakhstan',
    404: 'Kenya',           // covered
    408: 'North Korea',
    410: 'South Korea',     // covered
    414: 'Kuwait',
    418: 'Laos',
    422: 'Lebanon',
    426: 'Lesotho',
    428: 'Latvia',
    430: 'Liberia',
    434: 'Libya',
    440: 'Lithuania',
    442: 'Luxembourg',
    450: 'Madagascar',
    454: 'Malawi',
    458: 'Malaysia',        // covered
    466: 'Mali',
    478: 'Mauritania',
    484: 'Mexico',          // covered
    496: 'Mongolia',
    504: 'Morocco',         // covered
    508: 'Mozambique',
    516: 'Namibia',
    524: 'Nepal',
    528: 'Netherlands',     // covered
    540: 'New Caledonia',
    554: 'New Zealand',     // covered
    558: 'Nicaragua',
    562: 'Niger',
    566: 'Nigeria',         // covered
    578: 'Norway',          // covered
    586: 'Pakistan',        // covered
    591: 'Panama',
    598: 'Papua New Guinea',
    600: 'Paraguay',
    604: 'Peru',            // covered
    608: 'Philippines',     // covered
    616: 'Poland',          // covered
    620: 'Portugal',        // covered
    630: 'Puerto Rico',
    634: 'Qatar',           // covered
    642: 'Romania',
    643: 'Russia',          // covered
    646: 'Rwanda',
    682: 'Saudi Arabia',    // covered
    686: 'Senegal',
    694: 'Sierra Leone',
    703: 'Slovakia',
    705: 'Slovenia',
    706: 'Somalia',
    710: 'South Africa',    // covered
    716: 'Zimbabwe',
    724: 'Spain',           // covered
    729: 'Sudan',
    740: 'Suriname',
    752: 'Sweden',          // covered
    756: 'Switzerland',     // covered
    760: 'Syria',
    762: 'Tajikistan',
    764: 'Thailand',        // covered
    788: 'Tunisia',         // covered
    792: 'Turkey',          // covered
    800: 'Uganda',
    804: 'Ukraine',         // covered
    818: 'Egypt',           // covered
    826: 'United Kingdom',  // covered
    834: 'Tanzania',
    840: 'United States',   // covered
    858: 'Uruguay',
    860: 'Uzbekistan',
    862: 'Venezuela',
    887: 'Yemen',
    894: 'Zambia',
  };

  /* ── Async init ──────────────────────────────────────────────────────── */
  async function init() {
    const container = document.getElementById('world-map-container');
    const popup     = document.getElementById('map-popup');
    if (!container || !popup) return;

    let topoData, newsData;
    try {
      [topoData, newsData] = await Promise.all([
        d3.json('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json'),
        d3.json('data/world_news.json').catch(() => ({})),
      ]);
    } catch (err) {
      console.warn('world-map: failed to load data', err);
      container.innerHTML = '<p style="color:var(--text-muted);padding:2rem;text-align:center">Map unavailable</p>';
      return;
    }

    const width  = 960;
    const height = 500;

    const projection = d3.geoNaturalEarth1()
      .scale(153)
      .translate([width / 2, height / 2]);

    const path = d3.geoPath().projection(projection);

    const svg = d3.select(container)
      .append('svg')
      .attr('viewBox', `0 0 ${width} ${height}`)
      .attr('preserveAspectRatio', 'xMidYMid meet')
      .style('width', '100%')
      .style('height', 'auto')
      .style('display', 'block');

    const countries = topojson.feature(topoData, topoData.objects.countries);
    const borders   = topojson.mesh(topoData, topoData.objects.countries, (a, b) => a !== b);

    /* Ocean background */
    svg.append('rect')
      .attr('class', 'map-ocean')
      .attr('width', width)
      .attr('height', height);

    svg.selectAll('.map-country')
      .data(countries.features)
      .join('path')
        .attr('class', d => {
          const iso = +d.id;
          const key = REGION_BY_ISO[iso];
          return 'map-country' + (key ? ' map-country--covered' : '');
        })
        .attr('d', path)
        .on('mouseenter', function (event, d) {
          const iso   = +d.id;
          const key   = REGION_BY_ISO[iso];
          const info  = key ? newsData[key] : null;

          d3.select(this).classed('map-country--hovered', true);

          /* Build popup HTML */
          let html = '';
          if (info) {
            const flag  = info.flag  || '';
            const label = info.label || key;
            html += `<div class="mp-header">${flag} ${label}</div>`;
            if (info.stories && info.stories.length) {
              html += '<ul class="mp-stories">';
              info.stories.slice(0, 3).forEach(s => {
                const link = s.url
                  ? `<a href="${s.url}" target="_blank" rel="noopener">${s.headline}</a>`
                  : `<span>${s.headline}</span>`;
                html += `<li>${link}<span class="mp-source">${s.source || ''}</span></li>`;
              });
              html += '</ul>';
            } else {
              html += '<p class="mp-empty">No stories today.</p>';
            }
            html += `<a class="mp-link" href="regions/${key}.html">Full digest →</a>`;
          } else {
            const name = COUNTRY_NAMES[iso] || `Country #${iso}`;
            html += `<div class="mp-header">${name}</div>`;
            html += '<p class="mp-empty">No coverage yet.</p>';
          }

          popup.innerHTML = html;
          popup.classList.add('mp--visible');
        })
        .on('mousemove', function (event) {
          /* Popup is position:fixed — use viewport coords directly */
          const popW = 295;
          const popH = popup.offsetHeight || 180;
          const pad  = 16;
          const vw   = window.innerWidth;
          const vh   = window.innerHeight;

          let left = event.clientX + pad;
          let top  = event.clientY - popH / 2;

          if (left + popW > vw - 8) left = event.clientX - popW - pad;
          if (top  < 8)             top  = 8;
          if (top  + popH > vh - 8) top  = vh - popH - 8;

          popup.style.left = left + 'px';
          popup.style.top  = top  + 'px';
        })
        .on('mouseleave', function () {
          d3.select(this).classed('map-country--hovered', false);
          popup.classList.remove('mp--visible');
        })
        .on('click', function (event, d) {
          const iso = +d.id;
          const key = REGION_BY_ISO[iso];
          if (key) window.location.href = `regions/${key}.html`;
        });

    /* Border mesh */
    svg.append('path')
      .datum(borders)
      .attr('class', 'map-borders')
      .attr('d', path);
  }

  /* ── Bootstrap ───────────────────────────────────────────────────────── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
