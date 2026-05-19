/* ── Mobile nav toggle ───────────────────────────────────────────── */
const navToggle = document.getElementById('nav-toggle');
const mainNav   = document.getElementById('main-nav');
if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => mainNav.classList.toggle('open'));
}

/* ── Category filter (region page) ──────────────────────────────── */
const filterBar = document.getElementById('filter-bar');
if (filterBar) {
  filterBar.addEventListener('click', (e) => {
    const btn = e.target.closest('.filter-btn');
    if (!btn) return;

    filterBar.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const cat = btn.dataset.cat;
    document.querySelectorAll('#stories-grid .story-card').forEach(card => {
      if (cat === 'all' || card.dataset.cat === cat) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  });
}

/* ── Breaking page sidebar filter ───────────────────────────────── */
const catNav = document.querySelector('.cat-nav');
if (catNav) {
  catNav.addEventListener('click', (e) => {
    const link = e.target.closest('.cat-nav-link');
    if (!link) return;
    e.preventDefault();

    catNav.querySelectorAll('.cat-nav-link').forEach(l => l.classList.remove('active'));
    link.classList.add('active');

    const cat = link.dataset.cat;
    document.querySelectorAll('#breaking-feed .cat-section').forEach(section => {
      if (cat === 'all' || section.dataset.cat === cat) {
        section.style.display = '';
      } else {
        section.style.display = 'none';
      }
    });

    // Smooth scroll to section
    if (cat !== 'all') {
      const target = document.getElementById(cat);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
}

/* ── Date picker ─────────────────────────────────────────────────── */
const dateSelect = document.getElementById('date-select');
if (dateSelect) {
  fetch('data/available_dates.json')
    .then(r => r.json())
    .then(dates => {
      const current = dateSelect.dataset.current;
      dateSelect.innerHTML = '';
      dates.forEach(({ date, path }, i) => {
        const opt = document.createElement('option');
        opt.value = path;
        opt.textContent = i === 0 ? `${date} — latest` : date;
        if (date === current) opt.selected = true;
        dateSelect.appendChild(opt);
      });
      dateSelect.addEventListener('change', () => {
        if (dateSelect.value) window.location.href = dateSelect.value;
      });
    })
    .catch(() => {
      const wrap = dateSelect.closest('.date-selector');
      if (wrap) wrap.style.display = 'none';
    });
}

/* ── Breaking page sidebar drawer (mobile) ───────────────────────── */
const sidebarTab     = document.getElementById('sidebar-tab');
const sidebarOverlay = document.getElementById('sidebar-overlay');
const breakingSidebar = document.getElementById('breaking-sidebar');

function openSidebar() {
  if (!breakingSidebar) return;
  breakingSidebar.classList.add('open');
  if (sidebarOverlay) sidebarOverlay.classList.add('visible');
  if (sidebarTab) sidebarTab.setAttribute('aria-expanded', 'true');
}
function closeSidebar() {
  if (!breakingSidebar) return;
  breakingSidebar.classList.remove('open');
  if (sidebarOverlay) sidebarOverlay.classList.remove('visible');
  if (sidebarTab) sidebarTab.setAttribute('aria-expanded', 'false');
}

if (sidebarTab) sidebarTab.addEventListener('click', () => {
  breakingSidebar.classList.contains('open') ? closeSidebar() : openSidebar();
});
if (sidebarOverlay) sidebarOverlay.addEventListener('click', closeSidebar);

// Auto-close drawer after picking a category on mobile
if (catNav && breakingSidebar) {
  catNav.addEventListener('click', (e) => {
    if (window.innerWidth <= 768 && e.target.closest('.cat-nav-link')) {
      setTimeout(closeSidebar, 250);
    }
  });
}

/* ── Duplicate ticker content to make loop seamless ─────────────── */
const ticker = document.querySelector('.ticker');
if (ticker) {
  ticker.innerHTML += ticker.innerHTML;
}

/* ── Tab switching ───────────────────────────────────────────────── */
const tabBtns = document.querySelectorAll('.tab-btn');
tabBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    tabBtns.forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
  });
});
