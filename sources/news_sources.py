# RSS feed definitions — exactly 3 verified working sources per country.
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
        {"name": "The Tico Times",        "rss": "https://ticotimes.net/feed",                                                             "home": "https://ticotimes.net",                    "country": "Costa Rica"},
        {"name": "CRHoy",                 "rss": "https://www.crhoy.com/feed/",                                                            "home": "https://www.crhoy.com",                    "country": "Costa Rica"},
        {"name": "La Nación CR",          "rss": "https://www.nacion.com/arc/outboundfeeds/rss/",                                          "home": "https://www.nacion.com",                   "country": "Costa Rica"},
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
}
