# RSS feed definitions — exactly 3 verified working sources per country (5 for costa_rica).
# All feeds tested live. Claude translates non-English sources automatically.

NEWS_SOURCES: dict[str, list[dict]] = {

    # ── Original 8 ────────────────────────────────────────────────────────────

    "usa": [
        {"name": "The New York Times",    "rss": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",                             "home": "https://www.nytimes.com",                  "country": "USA"},
        {"name": "The Washington Post",   "rss": "https://feeds.washingtonpost.com/rss/national",                                          "home": "https://www.washingtonpost.com",            "country": "USA"},
        {"name": "NPR News",              "rss": "https://feeds.npr.org/1001/rss.xml",                                                     "home": "https://www.npr.org",                      "country": "USA"},
    ],
    "uk": [
        {"name": "BBC News",              "rss": "http://feeds.bbci.co.uk/news/rss.xml",                                                   "home": "https://www.bbc.com/news",                 "country": "UK"},
        {"name": "The Guardian",          "rss": "https://www.theguardian.com/world/rss",                                                  "home": "https://www.theguardian.com",              "country": "UK"},
        {"name": "Sky News",              "rss": "https://feeds.skynews.com/feeds/rss/home.xml",                                           "home": "https://news.sky.com",                     "country": "UK"},
    ],
    "france": [
        {"name": "Le Monde",              "rss": "https://www.lemonde.fr/rss/une.xml",                                                     "home": "https://www.lemonde.fr",                   "country": "France"},
        {"name": "Le Figaro",             "rss": "https://www.lefigaro.fr/rss/figaro_flash-actu.xml",                                      "home": "https://www.lefigaro.fr",                  "country": "France"},
        {"name": "France 24",             "rss": "https://www.france24.com/en/rss",                                                        "home": "https://www.france24.com/en",              "country": "France"},
    ],
    "germany": [
        {"name": "Deutsche Welle",        "rss": "https://rss.dw.com/rdf/rss-en-all",                                                     "home": "https://www.dw.com/en",                    "country": "Germany"},
        {"name": "Der Spiegel",           "rss": "https://www.spiegel.de/international/index.rss",                                         "home": "https://www.spiegel.de/international",     "country": "Germany"},
        {"name": "Die Zeit",              "rss": "https://newsfeed.zeit.de/english/index",                                                  "home": "https://www.zeit.de/english/index",        "country": "Germany"},
    ],
    "spain": [
        {"name": "El País",               "rss": "https://feeds.elpais.com/mrss-s/pages/ep/site/english.elpais.com/portada",               "home": "https://english.elpais.com",               "country": "Spain"},
        {"name": "El Mundo",              "rss": "https://www.elmundo.es/rss/portada.xml",                                                 "home": "https://www.elmundo.es",                   "country": "Spain"},
        {"name": "La Vanguardia",         "rss": "https://www.lavanguardia.com/rss/home.xml",                                              "home": "https://www.lavanguardia.com",             "country": "Spain"},
    ],
    "japan": [
        {"name": "The Japan Times",       "rss": "https://www.japantimes.co.jp/feed/",                                                     "home": "https://www.japantimes.co.jp",             "country": "Japan"},
        {"name": "NHK World",             "rss": "https://www3.nhk.or.jp/rss/news/cat0.xml",                                               "home": "https://www3.nhk.or.jp/nhkworld/en/news/", "country": "Japan"},
        {"name": "Asahi Shimbun",         "rss": "https://www.asahi.com/rss/asahi/newsheadlines.rdf",                                      "home": "https://www.asahi.com/ajw/",               "country": "Japan"},
    ],
    "china": [
        {"name": "South China Morning Post","rss": "https://www.scmp.com/rss/91/feed",                                                     "home": "https://www.scmp.com",                     "country": "China"},
        {"name": "China Daily",           "rss": "http://www.chinadaily.com.cn/rss/cndy_rss.xml",                                          "home": "https://www.chinadaily.com.cn",            "country": "China"},
        {"name": "Global Times",          "rss": "https://www.globaltimes.cn/rss/outbrain.xml",                                            "home": "https://www.globaltimes.cn",               "country": "China"},
    ],
    "italy": [
        {"name": "ANSA",                  "rss": "https://www.ansa.it/sito/ansait_rss.xml",                                                "home": "https://www.ansa.it",                      "country": "Italy"},
        {"name": "La Repubblica",         "rss": "https://www.repubblica.it/rss/homepage/rss2.0.xml",                                      "home": "https://www.repubblica.it",                "country": "Italy"},
        {"name": "Corriere della Sera",   "rss": "https://xml2.corriereobjects.it/rss/homepage.xml",                                       "home": "https://www.corriere.it",                  "country": "Italy"},
    ],

    # ── Americas ──────────────────────────────────────────────────────────────

    "canada": [
        {"name": "Globe and Mail",        "rss": "https://www.theglobeandmail.com/arc/outboundfeeds/rss/category/canada/",                 "home": "https://www.theglobeandmail.com",           "country": "Canada"},
        {"name": "CBC News",              "rss": "https://www.cbc.ca/cmlink/rss-topstories",                                               "home": "https://www.cbc.ca/news",                  "country": "Canada"},
        {"name": "National Post",         "rss": "https://nationalpost.com/feed",                                                          "home": "https://nationalpost.com",                 "country": "Canada"},
    ],
    "mexico": [
        {"name": "El Universal",          "rss": "https://www.eluniversal.com.mx/arc/outboundfeeds/rss/?outputType=xml",                   "home": "https://www.eluniversal.com.mx",           "country": "Mexico"},
        {"name": "Expansión",             "rss": "https://expansion.mx/rss",                                                               "home": "https://expansion.mx",                     "country": "Mexico"},
        {"name": "Reforma",               "rss": "https://www.reforma.com/rss/portada.xml",                                                "home": "https://www.reforma.com",                  "country": "Mexico"},
    ],
    "brazil": [
        {"name": "Folha de S.Paulo",      "rss": "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",                                 "home": "https://www.folha.uol.com.br",             "country": "Brazil"},
        {"name": "G1 (Globo)",            "rss": "https://g1.globo.com/rss/g1/",                                                           "home": "https://g1.globo.com",                     "country": "Brazil"},
        {"name": "Agência Brasil",        "rss": "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml",                          "home": "https://agenciabrasil.ebc.com.br",         "country": "Brazil"},
    ],
    "costa_rica": [
        {"name": "La Nación",             "rss": "https://www.nacion.com/arc/outboundfeeds/rss/",                                          "home": "https://www.nacion.com",                   "country": "Costa Rica"},
        {"name": "La República",          "rss": "https://www.larepublica.net/feed/",                                                      "home": "https://www.larepublica.net",              "country": "Costa Rica"},
        {"name": "Q Costa Rica",          "rss": "https://qcostarica.com/feed/",                                                           "home": "https://qcostarica.com",                   "country": "Costa Rica"},
        {"name": "Inside Costa Rica",     "rss": "https://insidecostarica.com/feed/",                                                      "home": "https://insidecostarica.com",              "country": "Costa Rica"},
        {"name": "Semanario Universidad", "rss": "https://semanariouniversidad.com/feed/",                                                 "home": "https://semanariouniversidad.com",         "country": "Costa Rica"},
    ],

    # ── Americas (expanded) ───────────────────────────────────────────────────
    "argentina": [
        {"name": "Buenos Aires Herald",  "rss": "https://www.buenosairesherald.com/feed",                        "home": "https://www.buenosairesherald.com",   "country": "Argentina"},
        {"name": "MercoPress",           "rss": "https://en.mercopress.com/rss",                                 "home": "https://en.mercopress.com",           "country": "Argentina"},
        {"name": "La Nación AR",         "rss": "https://www.lanacion.com.ar/arc/outboundfeeds/rss/",            "home": "https://www.lanacion.com.ar",         "country": "Argentina"},
    ],
    "colombia": [
        {"name": "Colombia Reports",     "rss": "https://colombiareports.com/feed/",                             "home": "https://colombiareports.com",         "country": "Colombia"},
        {"name": "El Tiempo",            "rss": "https://www.eltiempo.com/rss/portada.xml",                      "home": "https://www.eltiempo.com",            "country": "Colombia"},
        {"name": "El Espectador",        "rss": "https://www.elespectador.com/arc/outboundfeeds/rss/",           "home": "https://www.elespectador.com",        "country": "Colombia"},
    ],
    "chile": [
        {"name": "Santiago Times",       "rss": "https://santiagotimes.cl/feed/",                                "home": "https://santiagotimes.cl",            "country": "Chile"},
        {"name": "La Tercera",           "rss": "https://www.latercera.com/feed/",                               "home": "https://www.latercera.com",           "country": "Chile"},
        {"name": "El Mercurio",          "rss": "https://www.emol.com/rss/noticiasgenerales.xml",                "home": "https://www.emol.com",                "country": "Chile"},
    ],
    "peru": [
        {"name": "Peru Reports",         "rss": "https://perureports.com/feed/",                                 "home": "https://perureports.com",             "country": "Peru"},
        {"name": "El Comercio Peru",     "rss": "https://elcomercio.pe/arc/outboundfeeds/rss/",                  "home": "https://elcomercio.pe",               "country": "Peru"},
        {"name": "RPP Noticias",         "rss": "https://rpp.pe/rss/politica.xml",                               "home": "https://rpp.pe",                      "country": "Peru"},
    ],

    # ── Asia-Pacific ──────────────────────────────────────────────────────────

    "india": [
        {"name": "The Hindu",             "rss": "https://www.thehindu.com/feeder/default.rss",                                            "home": "https://www.thehindu.com",                 "country": "India"},
        {"name": "Hindustan Times",       "rss": "https://www.hindustantimes.com/feeds/rss/india-news/rssfeed.xml",                        "home": "https://www.hindustantimes.com",            "country": "India"},
        {"name": "Indian Express",        "rss": "https://indianexpress.com/feed/",                                                        "home": "https://indianexpress.com",                "country": "India"},
    ],
    "australia": [
        {"name": "ABC News Australia",    "rss": "https://www.abc.net.au/news/feed/51120/rss.xml",                                         "home": "https://www.abc.net.au/news",              "country": "Australia"},
        {"name": "The Guardian Australia","rss": "https://www.theguardian.com/australia-news/rss",                                         "home": "https://www.theguardian.com/australia-news","country": "Australia"},
        {"name": "news.com.au",           "rss": "https://www.news.com.au/content-feeds/latest-news-national/",                            "home": "https://www.news.com.au",                  "country": "Australia"},
    ],
    "taiwan": [
        {"name": "Taipei Times",          "rss": "https://www.taipeitimes.com/xml/index.rss",                                              "home": "https://www.taipeitimes.com",               "country": "Taiwan"},
        {"name": "Nikkei Asia",           "rss": "https://asia.nikkei.com/rss/feed/nar",                                                   "home": "https://asia.nikkei.com",                  "country": "Taiwan"},
        {"name": "Ketagalan Media",       "rss": "https://ketagalanmedia.com/feed/",                                                       "home": "https://ketagalanmedia.com",               "country": "Taiwan"},
    ],
    "singapore": [
        {"name": "The Straits Times",     "rss": "https://www.straitstimes.com/news/singapore/rss.xml",                                    "home": "https://www.straitstimes.com",              "country": "Singapore"},
        {"name": "CNA",                   "rss": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml",                   "home": "https://www.channelnewsasia.com",           "country": "Singapore"},
        {"name": "The Independent SG",    "rss": "https://theindependent.sg/feed/",                                                        "home": "https://theindependent.sg",                "country": "Singapore"},
    ],
    "south_korea": [
        {"name": "Korea Times",           "rss": "https://www.koreatimes.co.kr/www/rss/rss.xml",                                           "home": "https://www.koreatimes.co.kr",              "country": "South Korea"},
        {"name": "Yonhap News",           "rss": "https://en.yna.co.kr/RSS/news.xml",                                                      "home": "https://en.yna.co.kr",                     "country": "South Korea"},
        {"name": "Hankyoreh English",     "rss": "https://english.hani.co.kr/rss",                                                         "home": "https://english.hani.co.kr",               "country": "South Korea"},
    ],

    # ── Asia-Pacific (expanded) ───────────────────────────────────────────────
    "indonesia": [
        {"name": "Jakarta Post",         "rss": "https://www.thejakartapost.com/feed/",                          "home": "https://www.thejakartapost.com",      "country": "Indonesia"},
        {"name": "Tempo English",        "rss": "https://en.tempo.co/rss",                                       "home": "https://en.tempo.co",                 "country": "Indonesia"},
        {"name": "CNN Indonesia (EN)",   "rss": "https://www.cnnindonesia.com/rss",                              "home": "https://www.cnnindonesia.com",        "country": "Indonesia"},
    ],
    "pakistan": [
        {"name": "Dawn",                 "rss": "https://www.dawn.com/feeds/home",                               "home": "https://www.dawn.com",                "country": "Pakistan"},
        {"name": "The News International","rss": "https://www.thenews.com.pk/rss/1/1",                           "home": "https://www.thenews.com.pk",          "country": "Pakistan"},
        {"name": "Geo News",             "rss": "https://www.geo.tv/rss/1",                                      "home": "https://www.geo.tv",                  "country": "Pakistan"},
    ],
    "thailand": [
        {"name": "Bangkok Post",         "rss": "https://www.bangkokpost.com/rss/data/topstories.xml",           "home": "https://www.bangkokpost.com",         "country": "Thailand"},
        {"name": "The Nation Thailand",  "rss": "https://www.nationthailand.com/rss",                            "home": "https://www.nationthailand.com",      "country": "Thailand"},
        {"name": "Khaosod English",      "rss": "https://www.khaosodenglish.com/feed/",                          "home": "https://www.khaosodenglish.com",      "country": "Thailand"},
    ],
    "vietnam": [
        {"name": "VnExpress International","rss": "https://e.vnexpress.net/rss/news.rss",                        "home": "https://e.vnexpress.net",             "country": "Vietnam"},
        {"name": "Vietnam News",         "rss": "https://vietnamnews.vn/rss",                                    "home": "https://vietnamnews.vn",              "country": "Vietnam"},
        {"name": "Tuoi Tre News",        "rss": "https://tuoitrenews.vn/rss",                                    "home": "https://tuoitrenews.vn",              "country": "Vietnam"},
    ],
    "malaysia": [
        {"name": "Malay Mail",           "rss": "https://www.malaymail.com/feed",                                "home": "https://www.malaymail.com",           "country": "Malaysia"},
        {"name": "The Star Malaysia",    "rss": "https://www.thestar.com.my/rss/news/nation",                    "home": "https://www.thestar.com.my",          "country": "Malaysia"},
        {"name": "Free Malaysia Today",  "rss": "https://www.freemalaysiatoday.com/feed/",                       "home": "https://www.freemalaysiatoday.com",   "country": "Malaysia"},
    ],
    "philippines": [
        {"name": "Philippine Star",      "rss": "https://www.philstar.com/rss/headlines",                        "home": "https://www.philstar.com",            "country": "Philippines"},
        {"name": "Rappler",              "rss": "https://www.rappler.com/feed",                                  "home": "https://www.rappler.com",             "country": "Philippines"},
        {"name": "Inquirer.net",         "rss": "https://newsinfo.inquirer.net/feed",                            "home": "https://newsinfo.inquirer.net",       "country": "Philippines"},
    ],
    "bangladesh": [
        {"name": "The Daily Star BD",    "rss": "https://www.thedailystar.net/frontpage/rss.xml",                "home": "https://www.thedailystar.net",        "country": "Bangladesh"},
        {"name": "bdnews24",             "rss": "https://bdnews24.com/feeds/rss/",                               "home": "https://bdnews24.com",                "country": "Bangladesh"},
        {"name": "Prothom Alo (EN)",     "rss": "https://en.prothomalo.com/feed",                               "home": "https://en.prothomalo.com",           "country": "Bangladesh"},
    ],
    "new_zealand": [
        {"name": "NZ Herald",            "rss": "https://www.nzherald.co.nz/arc/outboundfeeds/rss/section/news/?outputType=xml", "home": "https://www.nzherald.co.nz", "country": "New Zealand"},
        {"name": "RNZ News",             "rss": "https://www.rnz.co.nz/rss",                                    "home": "https://www.rnz.co.nz",               "country": "New Zealand"},
        {"name": "Stuff NZ",             "rss": "https://www.stuff.co.nz/rss",                                   "home": "https://www.stuff.co.nz",             "country": "New Zealand"},
    ],

    # ── Europe / Eurasia ──────────────────────────────────────────────────────

    "russia": [
        {"name": "TASS",                  "rss": "https://tass.com/rss/v2.xml",                                                            "home": "https://tass.com",                         "country": "Russia"},
        {"name": "Moscow Times",          "rss": "https://www.themoscowtimes.com/rss/news",                                                 "home": "https://www.themoscowtimes.com",            "country": "Russia"},
        {"name": "Meduza (EN)",           "rss": "https://meduza.io/rss/en/all",                                                           "home": "https://meduza.io/en",                     "country": "Russia"},
    ],
    "ukraine": [
        {"name": "Kyiv Post",             "rss": "https://www.kyivpost.com/feed",                                                          "home": "https://www.kyivpost.com",                 "country": "Ukraine"},
        {"name": "Ukrinform",             "rss": "https://www.ukrinform.net/rss/block-lastnews",                                           "home": "https://www.ukrinform.net",                "country": "Ukraine"},
        {"name": "Ukrainska Pravda",      "rss": "https://www.pravda.com.ua/eng/rss/view_news/",                                           "home": "https://www.pravda.com.ua/eng/",           "country": "Ukraine"},
    ],
    "turkey": [
        {"name": "Hürriyet Daily News",   "rss": "https://www.hurriyet.com.tr/rss/anasayfa",                                               "home": "https://www.hurriyet.com.tr",              "country": "Turkey"},
        {"name": "Al-Monitor",             "rss": "https://www.al-monitor.com/rss",                                                        "home": "https://www.al-monitor.com",               "country": "Turkey"},
        {"name": "Euronews Turkey",       "rss": "https://tr.euronews.com/rss",                                                            "home": "https://tr.euronews.com",                  "country": "Turkey"},
    ],

    # ── Europe (expanded) ─────────────────────────────────────────────────────
    "netherlands": [
        {"name": "NL Times",             "rss": "https://nltimes.nl/feed",                                       "home": "https://nltimes.nl",                  "country": "Netherlands"},
        {"name": "Dutch News",           "rss": "https://www.dutchnews.nl/feed/",                                "home": "https://www.dutchnews.nl",            "country": "Netherlands"},
        {"name": "DutchReview",          "rss": "https://dutchreview.com/feed/",                                 "home": "https://dutchreview.com",             "country": "Netherlands"},
    ],
    "portugal": [
        {"name": "Portugal News",        "rss": "https://www.theportugalnews.com/rss/latest-news.rss",           "home": "https://www.theportugalnews.com",     "country": "Portugal"},
        {"name": "Portugal Resident",    "rss": "https://www.portugalresident.com/feed/",                        "home": "https://www.portugalresident.com",    "country": "Portugal"},
        {"name": "Observador",           "rss": "https://observador.pt/feed/",                                   "home": "https://observador.pt",               "country": "Portugal"},
    ],
    "poland": [
        {"name": "Notes from Poland",    "rss": "https://notesfrompoland.com/feed/",                             "home": "https://notesfrompoland.com",         "country": "Poland"},
        {"name": "Polsat News (EN)",     "rss": "https://polsatnews.pl/rss/wszystkie.xml",                       "home": "https://polsatnews.pl",               "country": "Poland"},
        {"name": "Warsaw Voice",         "rss": "https://warsawvoice.pl/feed",                                   "home": "https://warsawvoice.pl",              "country": "Poland"},
    ],
    "sweden": [
        {"name": "The Local Sweden",     "rss": "https://www.thelocal.se/feed/",                                 "home": "https://www.thelocal.se",             "country": "Sweden"},
        {"name": "Sweden Today",         "rss": "https://swedentoday.eu/feed/",                                  "home": "https://swedentoday.eu",              "country": "Sweden"},
        {"name": "Radio Sweden",         "rss": "https://sverigesradio.se/topnyheter/rss.xml",                   "home": "https://sverigesradio.se/radiointernational", "country": "Sweden"},
    ],
    "norway": [
        {"name": "The Local Norway",     "rss": "https://www.thelocal.no/feed/",                                 "home": "https://www.thelocal.no",             "country": "Norway"},
        {"name": "Norway Today",         "rss": "https://norwaytoday.info/feed/",                                "home": "https://norwaytoday.info",            "country": "Norway"},
        {"name": "Aftenposten (EN)",     "rss": "https://www.aftenposten.no/rss/",                               "home": "https://www.aftenposten.no",          "country": "Norway"},
    ],
    "denmark": [
        {"name": "The Local Denmark",    "rss": "https://www.thelocal.dk/feed/",                                 "home": "https://www.thelocal.dk",             "country": "Denmark"},
        {"name": "Copenhagen Post",      "rss": "https://cphpost.dk/feed/",                                      "home": "https://cphpost.dk",                  "country": "Denmark"},
        {"name": "DR International",     "rss": "https://www.dr.dk/nyheder/service/feeds/senestenyt",             "home": "https://www.dr.dk",                   "country": "Denmark"},
    ],
    "switzerland": [
        {"name": "SWI swissinfo",        "rss": "https://www.swissinfo.ch/eng/rss/news",                         "home": "https://www.swissinfo.ch/eng",        "country": "Switzerland"},
        {"name": "The Local Switzerland","rss": "https://www.thelocal.ch/feed/",                                 "home": "https://www.thelocal.ch",             "country": "Switzerland"},
        {"name": "Swiss Broadcasting",   "rss": "https://www.rts.ch/info/rss/rss.xml",                           "home": "https://www.rts.ch/info",             "country": "Switzerland"},
    ],
    "austria": [
        {"name": "The Local Austria",    "rss": "https://www.thelocal.at/feed/",                                 "home": "https://www.thelocal.at",             "country": "Austria"},
        {"name": "Austria Today",        "rss": "https://austriatoday.at/feed/",                                 "home": "https://austriatoday.at",             "country": "Austria"},
        {"name": "Vienna Online",        "rss": "https://www.vienna.at/rss/",                                    "home": "https://www.vienna.at",               "country": "Austria"},
    ],
    "belgium": [
        {"name": "Brussels Times",       "rss": "https://www.brusselstimes.com/feed/",                           "home": "https://www.brusselstimes.com",       "country": "Belgium"},
        {"name": "RTBF News (FR)",       "rss": "https://www.rtbf.be/article?type=article&section=info&format=rss", "home": "https://www.rtbf.be",              "country": "Belgium"},
        {"name": "De Standaard (NL)",    "rss": "https://www.standaard.be/rss/section/1F2C2734-5B4F-49CB-BF2A-9B90EC1BDC8F", "home": "https://www.standaard.be", "country": "Belgium"},
    ],
    "greece": [
        {"name": "Ekathimerini",         "rss": "https://www.ekathimerini.com/rss/?news",                        "home": "https://www.ekathimerini.com",        "country": "Greece"},
        {"name": "Greek Reporter",       "rss": "https://www.greekreporter.com/feed/",                           "home": "https://www.greekreporter.com",       "country": "Greece"},
        {"name": "Athens News",          "rss": "https://www.athensnews.gr/feed/",                               "home": "https://www.athensnews.gr",           "country": "Greece"},
    ],

    # ── Middle East ───────────────────────────────────────────────────────────

    "saudi_arabia": [
        {"name": "Asharq Al-Awsat",       "rss": "https://english.aawsat.com/feed",                                                        "home": "https://english.aawsat.com",               "country": "Saudi Arabia"},
        {"name": "Saudi 24 News",          "rss": "https://saudi24news.com/feed/",                                                          "home": "https://saudi24news.com",                  "country": "Saudi Arabia"},
        {"name": "Middle East Eye",       "rss": "https://www.middleeasteye.net/rss",                                                       "home": "https://www.middleeasteye.net",            "country": "Saudi Arabia"},
    ],
    "iran": [
        {"name": "Tehran Times",          "rss": "https://www.tehrantimes.com/rss",                                                        "home": "https://www.tehrantimes.com",              "country": "Iran"},
        {"name": "IRNA English",          "rss": "https://en.irna.ir/rss",                                                                 "home": "https://en.irna.ir",                       "country": "Iran"},
        {"name": "Mehr News (EN)",        "rss": "https://en.mehrnews.com/rss",                                                            "home": "https://en.mehrnews.com",                  "country": "Iran"},
    ],
    "uae": [
        {"name": "Al Jazeera",            "rss": "https://www.aljazeera.com/xml/rss/all.xml",                                              "home": "https://www.aljazeera.com",                "country": "UAE"},
        {"name": "Economy Middle East",   "rss": "https://economymiddleeast.com/feed/",                                                    "home": "https://economymiddleeast.com",            "country": "UAE"},
        {"name": "Albawaba",              "rss": "https://www.albawaba.com/rss.xml",                                                       "home": "https://www.albawaba.com",                 "country": "UAE"},
    ],

    # ── Middle East (expanded) ────────────────────────────────────────────────
    "israel": [
        {"name": "Haaretz",              "rss": "https://www.haaretz.com/cmlink/1.625767",                       "home": "https://www.haaretz.com",             "country": "Israel"},
        {"name": "Jerusalem Post",       "rss": "https://www.jpost.com/rss/rssfeedsheadlines.aspx",             "home": "https://www.jpost.com",               "country": "Israel"},
        {"name": "Times of Israel",      "rss": "https://www.timesofisrael.com/feed/",                           "home": "https://www.timesofisrael.com",       "country": "Israel"},
    ],
    "iraq": [
        {"name": "Rudaw",                "rss": "https://www.rudaw.net/english/rss",                             "home": "https://www.rudaw.net/english",       "country": "Iraq"},
        {"name": "Kurdistan 24",         "rss": "https://www.kurdistan24.net/en/rss",                            "home": "https://www.kurdistan24.net/en",      "country": "Iraq"},
        {"name": "Iraq News Network",    "rss": "https://www.iraqnewsnetwork.net/feed/",                         "home": "https://www.iraqnewsnetwork.net",     "country": "Iraq"},
    ],
    "qatar": [
        {"name": "The Peninsula Qatar",  "rss": "https://www.thepeninsulaqatar.com/rss",                         "home": "https://www.thepeninsulaqatar.com",   "country": "Qatar"},
        {"name": "Qatar Tribune",        "rss": "https://www.qatar-tribune.com/rss",                             "home": "https://www.qatar-tribune.com",       "country": "Qatar"},
        {"name": "Doha News",            "rss": "https://dohanews.co/feed/",                                     "home": "https://dohanews.co",                 "country": "Qatar"},
    ],

    # ── Africa ────────────────────────────────────────────────────────────────

    "south_africa": [
        {"name": "IOL News",              "rss": "https://www.iol.co.za/rss",                                                              "home": "https://www.iol.co.za",                    "country": "South Africa"},
        {"name": "News24",                "rss": "https://feeds.news24.com/articles/news24/TopStories/rss",                                "home": "https://www.news24.com",                   "country": "South Africa"},
        {"name": "Mail & Guardian",       "rss": "https://mg.co.za/feed/",                                                                 "home": "https://mg.co.za",                         "country": "South Africa"},
    ],
    "morocco": [
        {"name": "Tel Quel",              "rss": "https://telquel.ma/feed/",                                                               "home": "https://telquel.ma",                       "country": "Morocco"},
        {"name": "Hespress",              "rss": "https://fr.hespress.com/feed",                                                           "home": "https://fr.hespress.com",                  "country": "Morocco"},
        {"name": "Medias24",              "rss": "https://medias24.com/feed/",                                                             "home": "https://medias24.com",                     "country": "Morocco"},
    ],
    "egypt": [
        {"name": "Egypt Independent",     "rss": "https://egyptindependent.com/feed/",                                                     "home": "https://egyptindependent.com",             "country": "Egypt"},
        {"name": "Daily News Egypt",      "rss": "https://dailynewsegypt.com/feed/",                                                       "home": "https://dailynewsegypt.com",               "country": "Egypt"},
        {"name": "Mada Masr",             "rss": "https://www.madamasr.com/en/feed/",                                                      "home": "https://www.madamasr.com/en",              "country": "Egypt"},
    ],

    # ── Africa (expanded) ─────────────────────────────────────────────────────
    "nigeria": [
        {"name": "Vanguard Nigeria",     "rss": "https://www.vanguardngr.com/feed/",                             "home": "https://www.vanguardngr.com",         "country": "Nigeria"},
        {"name": "Punch Nigeria",        "rss": "https://punchng.com/feed/",                                     "home": "https://punchng.com",                 "country": "Nigeria"},
        {"name": "Premium Times Nigeria","rss": "https://www.premiumtimesng.com/feed",                           "home": "https://www.premiumtimesng.com",      "country": "Nigeria"},
    ],
    "kenya": [
        {"name": "Nation Africa",        "rss": "https://nation.africa/kenya/news/-/1056/rss",                   "home": "https://nation.africa/kenya",         "country": "Kenya"},
        {"name": "The Standard Kenya",   "rss": "https://www.standardmedia.co.ke/rss/headlines.php",             "home": "https://www.standardmedia.co.ke",     "country": "Kenya"},
        {"name": "Business Daily Africa","rss": "https://www.businessdailyafrica.com/rss",                       "home": "https://www.businessdailyafrica.com", "country": "Kenya"},
    ],
    "ethiopia": [
        {"name": "Addis Standard",       "rss": "https://addisstandard.com/feed/",                               "home": "https://addisstandard.com",           "country": "Ethiopia"},
        {"name": "Ethiopian Monitor",    "rss": "https://ethiopianmonitor.com/feed/",                            "home": "https://ethiopianmonitor.com",        "country": "Ethiopia"},
        {"name": "The Reporter Ethiopia","rss": "https://www.thereporterethiopia.com/feed",                      "home": "https://www.thereporterethiopia.com", "country": "Ethiopia"},
    ],
    "ghana": [
        {"name": "GhanaWeb",             "rss": "https://www.ghanaweb.com/rss/news.php",                         "home": "https://www.ghanaweb.com",            "country": "Ghana"},
        {"name": "MyJoyOnline",          "rss": "https://www.myjoyonline.com/feed/",                             "home": "https://www.myjoyonline.com",         "country": "Ghana"},
        {"name": "Graphic Online",       "rss": "https://www.graphic.com.gh/feed",                               "home": "https://www.graphic.com.gh",          "country": "Ghana"},
    ],
    "algeria": [
        {"name": "TSA Algérie",          "rss": "https://www.tsa-algerie.com/feed/",                             "home": "https://www.tsa-algerie.com",         "country": "Algeria"},
        {"name": "Algérie Press Service","rss": "https://www.aps.dz/rss.xml",                                    "home": "https://www.aps.dz",                  "country": "Algeria"},
        {"name": "Algeria Watch",        "rss": "https://algeria-watch.org/feed",                                "home": "https://algeria-watch.org",           "country": "Algeria"},
    ],
    "tunisia": [
        {"name": "Business News TN",     "rss": "https://www.businessnews.com.tn/rss.xml",                       "home": "https://www.businessnews.com.tn",     "country": "Tunisia"},
        {"name": "Kapitalis",            "rss": "https://www.kapitalis.com/feed/",                               "home": "https://www.kapitalis.com",           "country": "Tunisia"},
        {"name": "African Manager",      "rss": "https://africanmanager.com/feed/",                              "home": "https://africanmanager.com",          "country": "Tunisia"},
    ],
}
