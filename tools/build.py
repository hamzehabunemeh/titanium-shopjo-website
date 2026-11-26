"""Builds every page of the site from tools/content.py.

    python3 tools/build.py

English pages are written to the repository root, Arabic pages to /ar/.
All links are relative, so the site works on GitHub Pages (sub-path) and
on Netlify (domain root) without changes.
"""
import html
import json
import urllib.parse
from pathlib import Path

import content as C

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / "assets" / "img" / "manifest.json").read_text())
LANGS = ("en", "ar")
SERVICE_BY_SLUG = {s["slug"]: s for s in C.SERVICES}


def _ver(path):
    """Short content hash, so browsers fetch the new file after every change."""
    import hashlib
    return hashlib.md5((ROOT / path).read_bytes()).hexdigest()[:8]


CSS_V = _ver("assets/css/style.css")
JS_V = _ver("assets/js/main.js")
INTRO_V = _ver("assets/js/intro.js")


def esc(s):
    return html.escape(str(s), quote=True)


class Page:
    """Context for one page in one language."""

    def __init__(self, lang, filename):
        self.lang = lang
        self.filename = filename
        self.prefix = "" if lang == "en" else "../"  # path back to repo root
        self.service = None  # set on service pages: WhatsApp messages mention it

    def t(self, value):
        return value[self.lang] if isinstance(value, dict) else value

    def asset(self, path):
        return self.prefix + path

    def other_lang_href(self):
        return ("ar/" + self.filename) if self.lang == "en" else ("../" + self.filename)

    def url(self, lang=None):
        lang = lang or self.lang
        path = ("" if lang == "en" else "ar/") + ("" if self.filename == "index.html" else self.filename)
        return f"{C.SITE_URL}/{path}"


# ---------------------------------------------------------------- helpers ---

def img(p, name, alt, sizes="100vw", cls="", eager=False):
    sizes_list = MANIFEST[name]
    w, h = sizes_list[-1]
    srcset = ", ".join(f"{p.asset(f'assets/img/{name}-{sw}.webp')} {sw}w" for sw, _ in sizes_list)
    mid = sizes_list[min(1, len(sizes_list) - 1)][0]
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img src="{p.asset(f"assets/img/{name}-{mid}.webp")}" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{esc(alt)}" {loading} decoding="async"'
            + (f' class="{cls}"' if cls else "") + ">")


def ratio(name):
    w, h = MANIFEST[name][-1]
    return w / h


def wa_link(p, text=None):
    if not text and p.service:
        name = p.t(p.service["title"])
        text = {"en": f"Hello Titanium Shop, I'm interested in {name}.",
                "ar": f"مرحباً Titanium Shop، أنا مهتم بخدمة {name}."}[p.lang]
    text = text or {"en": "Hello Titanium Shop, I'd like to make a request.",
                    "ar": "مرحباً Titanium Shop، أود تقديم طلب."}[p.lang]
    return f"https://wa.me/{C.CONTACT['whatsapp']}?text={urllib.parse.quote(text)}"


ICONS = {
    "whatsapp": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z" fill="currentColor" stroke="none"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.3-7-12a7 7 0 0 1 14 0c0 5.7-7 12-7 12Z"/><circle cx="12" cy="9" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "menu": '<path d="M4 8h16M4 16h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>',
    "facebook": '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v7h4v-7h3l1-4h-4V8.5a.5.5 0 0 1 .5-.5Z"/>',
    "diamond": '<path d="M12 3 21 12 12 21 3 12Z"/>',
}


def icon(name, cls="icon"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# ------------------------------------------------------------ page shell ---

PRELOAD = {
    "en": ["cormorant-garamond-latin-500-normal.woff2", "jost-latin-300-normal.woff2"],
    "ar": ["noto-naskh-arabic-arabic-600-normal.woff2", "ibm-plex-sans-arabic-arabic-300-normal.woff2"],
}


def jsonld(p):
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": C.BRAND,
        "slogan": p.t(C.L("فخامة بلا حد", "Unlimited Luxury")),
        "url": C.SITE_URL + "/",
        "logo": C.SITE_URL + "/assets/brand/logo.png",
        "image": C.SITE_URL + "/assets/brand/og-image.jpg?v=2",
        "telephone": C.CONTACT["phone_tel"],
        "email": C.CONTACT["email"],
        "foundingDate": "2018",
        "address": {"@type": "PostalAddress", "streetAddress": "Al-Karadsheh Tower, 1st Floor",
                    "addressLocality": "Amman", "addressCountry": "JO"},
        "areaServed": ["JO", "AE", "SA", "EG", "LB"],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
                                      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                      "opens": "00:00", "closes": "23:59"},
        "sameAs": [C.CONTACT["instagram"], C.CONTACT["instagram_events"], C.CONTACT["facebook"]],
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def head(p, title, description, noindex=False, schema=False):
    dir_ = "rtl" if p.lang == "ar" else "ltr"
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    return f"""<!doctype html>
<html lang="{p.lang}" dir="{dir_}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{robots}
<link rel="canonical" href="{p.url()}">
<link rel="alternate" hreflang="en" href="{p.url('en')}">
<link rel="alternate" hreflang="ar" href="{p.url('ar')}">
<link rel="alternate" hreflang="x-default" href="{p.url('en')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{C.BRAND}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{p.url()}">
<meta property="og:image" content="{C.SITE_URL}/assets/brand/og-image.jpg?v=2">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(C.BRAND)}: {esc(p.t(C.L('فخامة بلا حد', 'Unlimited Luxury')))}">
<meta name="twitter:image" content="{C.SITE_URL}/assets/brand/og-image.jpg?v=2">
<meta property="og:locale" content="{'ar_JO' if p.lang == 'ar' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a0a0b">
<link rel="icon" href="{p.asset('favicon.ico')}" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{p.asset('assets/brand/favicon-32.png')}">
<link rel="apple-touch-icon" href="{p.asset('assets/brand/apple-touch-icon.png')}">
<link rel="manifest" href="{p.asset('site.webmanifest')}">
{''.join(f'<link rel="preload" href="{p.asset("assets/fonts/" + f)}" as="font" type="font/woff2" crossorigin>' for f in PRELOAD[p.lang])}
<link rel="stylesheet" href="{p.asset('assets/css/style.css')}?v={CSS_V}">
<script src="{p.asset('assets/js/intro.js')}?v={INTRO_V}"></script>
<script src="{p.asset('assets/js/main.js')}?v={JS_V}" defer></script>
{jsonld(p) if schema else ''}
</head>
<body>
<div class="logo-intro" aria-hidden="true" data-intro>
  <svg class="intro-lines" viewBox="0 0 200 200" width="200" height="200">
    <path class="intro-path" pathLength="1" d="M100 6 194 100 100 194 6 100Z"/>
    <path class="intro-path p2" pathLength="1" d="M100 30 170 100 100 170 30 100Z"/>
  </svg>
  <img class="intro-emblem" src="{p.asset('assets/brand/emblem.webp')}" width="158" height="160" alt="">
</div>
<a class="skip-link" href="#main">{p.t(C.UI['skip'])}</a>
"""


def header(p, current=""):
    def nav_item(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'

    service_links = "".join(
        f'<li><a href="{s["slug"]}.html"{" aria-current=\"page\"" if s["slug"] == current else ""}>{p.t(s["title"])}</a></li>'
        for s in C.SERVICES)
    return f"""<header class="site-header" data-header>
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="{C.BRAND}, {p.t(C.UI['home'])}">
      <img class="brand-emblem" src="{p.asset('assets/brand/emblem.webp')}" width="158" height="160" alt="">
      <img class="brand-wordmark" src="{p.asset('assets/brand/wordmark.webp')}" width="443" height="120" alt="{C.BRAND}">
    </a>
    <nav class="main-nav" aria-label="{p.t(C.UI['menu'])}">
      <ul>
        {nav_item('index.html', p.t(C.UI['home']), 'home')}
        <li class="has-sub">
          <a href="index.html#services"{' aria-current="page"' if current in SERVICE_BY_SLUG else ''}>{p.t(C.UI['services'])}</a>
          <ul class="sub">{service_links}</ul>
        </li>
        {nav_item('about.html', p.t(C.UI['about']), 'about')}
        {nav_item('contact.html', p.t(C.UI['contact']), 'contact')}
      </ul>
    </nav>
    <div class="header-actions">
      <a class="lang-switch" href="{p.other_lang_href()}" hreflang="{'ar' if p.lang == 'en' else 'en'}" lang="{'ar' if p.lang == 'en' else 'en'}" aria-label="{p.t(C.UI['lang_switch_label'])}">{p.t(C.UI['lang_switch'])}</a>
      <a class="btn btn-silver btn-sm header-cta" href="contact.html">{p.t(C.UI['request'])}</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" data-menu-toggle>
        <span class="visually-hidden">{p.t(C.UI['menu'])}</span>{icon('menu', 'icon icon-open')}{icon('close', 'icon icon-close')}
      </button>
    </div>
  </div>
  <div class="mobile-menu" id="mobile-menu" data-mobile-menu hidden>
    <div class="container">
      <ul class="mobile-links">
        <li><a href="index.html">{p.t(C.UI['home'])}</a></li>
        {service_links}
        <li><a href="about.html">{p.t(C.UI['about'])}</a></li>
        <li><a href="contact.html">{p.t(C.UI['contact'])}</a></li>
      </ul>
      <div class="mobile-actions">
        <a class="btn btn-silver" href="{wa_link(p)}" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}{p.t(C.UI['whatsapp'])}</a>
        <a class="btn btn-ghost" href="tel:{C.CONTACT['phone_tel']}">{icon('phone')}{p.t(C.UI['call'])}</a>
      </div>
    </div>
  </div>
</header>
"""


def cta_band(p):
    return f"""<section class="section cta-band reveal">
  <div class="container narrow center">
    <span class="ornament" aria-hidden="true"></span>
    <h2 class="h2">{p.t(C.UI['cta_title'])}</h2>
    <p class="lead">{p.t(C.UI['cta_text'])}</p>
    <p class="amman-clock" data-amman-clock hidden></p>
    <div class="btn-row center">
      <a class="btn btn-silver" href="{wa_link(p)}" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}{p.t(C.UI['whatsapp'])}</a>
      <a class="btn btn-ghost" href="tel:{C.CONTACT['phone_tel']}">{icon('phone')}<span dir="ltr">{C.CONTACT['phone_display']}</span></a>
    </div>
  </div>
</section>
"""


def footer(p):
    services = "".join(f'<li><a href="{s["slug"]}.html">{p.t(s["title"])}</a></li>' for s in C.SERVICES)
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="{p.asset('assets/brand/logo.webp')}" width="531" height="480" alt="{C.BRAND}, unlimited luxury" loading="lazy">
      <p>{p.t(C.UI['footer_line'])}</p>
    </div>
    <div>
      <h2 class="footer-title">{p.t(C.UI['services'])}</h2>
      <ul class="footer-links">{services}</ul>
    </div>
    <div>
      <h2 class="footer-title">{p.t(C.UI['reach'])}</h2>
      <ul class="footer-links contact-list">
        <li><a href="tel:{C.CONTACT['phone_tel']}">{icon('phone')}<span dir="ltr">{C.CONTACT['phone_display']}</span></a></li>
        <li><a href="{wa_link(p)}" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}<span dir="ltr">{C.CONTACT['whatsapp_display']}</span></a></li>
        <li><a href="mailto:{C.CONTACT['email']}">{icon('mail')}<span>{C.CONTACT['email']}</span></a></li>
        <li><a href="{C.CONTACT['map_url']}" target="_blank" rel="noopener noreferrer">{icon('pin')}<span>{p.t(C.CONTACT['address'])}</span></a></li>
        <li><span class="plain">{icon('clock')}<span>{p.t(C.UI['cs_247'])}</span></span></li>
      </ul>
    </div>
    <div>
      <h2 class="footer-title">{p.t(C.UI['follow'])}</h2>
      <ul class="social">
        <li><a href="{C.CONTACT['instagram']}" target="_blank" rel="noopener noreferrer" aria-label="Instagram @titaniumshopjo">{icon('instagram')}</a></li>
        <li><a href="{C.CONTACT['instagram_events']}" target="_blank" rel="noopener noreferrer" aria-label="Instagram @titanium_event.jo">{icon('instagram')}</a></li>
        <li><a href="{C.CONTACT['facebook']}" target="_blank" rel="noopener noreferrer" aria-label="Facebook">{icon('facebook')}</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>© <span data-year>2026</span> {C.BRAND}. {p.t(C.UI['rights'])}.</p>
    <a href="privacy.html">{p.t(C.UI['privacy'])}</a>
  </div>
</footer>
<a class="float-wa" href="{wa_link(p)}" target="_blank" rel="noopener noreferrer" aria-label="{p.t(C.UI['whatsapp'])}">{icon('whatsapp')}</a>
</body>
</html>
"""


def page_head(p, kicker, title, lead, actions=True, service=None):
    btns = ""
    if actions:
        req_href = f"contact.html?services={service}" if service else "contact.html"
        label = C.UI['request_this'] if service else C.UI['request']
        btns = f"""<div class="btn-row">
        <a class="btn btn-silver" href="{req_href}">{p.t(label)}</a>
        <a class="btn btn-ghost" href="{wa_link(p)}" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}{p.t(C.UI['whatsapp'])}</a>
      </div>"""
    return f"""<p class="kicker">{kicker}</p>
      <h1 class="h1">{title}</h1>
      <p class="lead">{lead}</p>
      {btns}"""


# ---------------------------------------------------------- page bodies ---

def services_grid(p, exclude=None):
    cards = []
    services = C.SERVICES
    if exclude:  # "more services": the next four after the current one
        i = [s["slug"] for s in services].index(exclude)
        services = [services[(i + k) % len(services)] for k in range(1, 5)]
    for s in services:
        cards.append(f"""<li class="service-card reveal">
        <a href="{s['slug']}.html">
          <span class="frame">{img(p, s['card_img'], p.t(s['title']), '(min-width: 1100px) 25vw, (min-width: 640px) 50vw, 100vw')}</span>
          <span class="card-body">
            <span class="card-kicker">{p.t(s['kicker'])}</span>
            <span class="card-title">{p.t(s['title'])}</span>
            <span class="card-text">{p.t(s['short'])}</span>
            <span class="card-more">{p.t(C.UI['discover'])}{icon('arrow', 'icon arrow')}</span>
          </span>
        </a>
      </li>""")
    return f'<ul class="service-grid">{"".join(cards)}</ul>'


def celebs_marquee(p):
    def items(hidden):
        extra = ' aria-hidden="true"' if hidden else ""
        return "".join(
            f"""<li class="celeb"{extra}><figure><span class="frame">{img(p, name, "" if hidden else p.t(label) + (' with Hamza Khashman' if p.lang == 'en' else ' مع حمزة خشمان'), '240px')}</span>
        <figcaption>{p.t(label)}</figcaption></figure></li>"""
            for name, label in C.CELEBRITIES)
    return f'<div class="marquee" data-marquee><ul class="marquee-track">{items(False)}{items(True)}</ul></div>'


def celebs_grid(p):
    items = "".join(
        f"""<li class="celeb reveal"><figure><span class="frame">{img(p, name, p.t(label) + (' with Hamza Khashman' if p.lang == 'en' else ' مع حمزة خشمان'), '(min-width: 1100px) 16vw, (min-width: 640px) 33vw, 60vw')}</span>
        <figcaption>{p.t(label)}</figcaption></figure></li>"""
        for name, label in C.CELEBRITIES)
    return f'<ul class="celeb-grid">{items}</ul>'


def service_choices(p, name, prefix):
    """Checkbox 'chips' for the services, used on the home planner and the form."""
    out = []
    for s in C.SERVICES:
        cid = f"{prefix}-{s['slug']}"
        out.append(f'<li><input class="choice-input" type="checkbox" id="{cid}" '
                   f'{f"name={chr(34)}{name}{chr(34)} " if name else ""}value="{s["slug"]}" data-label="{esc(p.t(s["title"]))}">'
                   f'<label class="choice" for="{cid}">{icon("diamond", "icon choice-icon")}<span>{p.t(s["title"])}</span></label></li>')
    return f'<ul class="choices">{"".join(out)}</ul>'


def planner_block(p):
    P = C.PLANNER
    return f"""<section class="section section-alt planner" id="plan">
  <div class="container narrow-wide">
    <div class="section-head center reveal">
      <span class="ornament" aria-hidden="true"></span>
      <h2 class="h2">{p.t(P['title'])}</h2>
      <p class="lead">{p.t(P['text'])}</p>
    </div>
    <form class="planner-form" action="contact.html#request" method="get" data-planner>
      <fieldset>
        <legend class="visually-hidden">{p.t(P['legend'])}</legend>
        {service_choices(p, 'services', 'plan')}
      </fieldset>
      <p class="planner-count" data-planner-count aria-live="polite"></p>
      <div class="center"><button class="btn btn-silver" type="submit">{p.t(P['cta'])}</button></div>
    </form>
  </div>
</section>"""


def build_home(p):
    H = C.HOME
    stats = "".join(f'<li><span class="stat-num">{p.t(n)}</span><span class="stat-label">{p.t(l)}</span></li>' for n, l in H["stats"])
    fleet_preview = "".join(
        f'<li class="fleet-card reveal"><span class="frame">{img(p, n, name, "(min-width: 900px) 25vw, 50vw")}</span><span class="fleet-name">{name}</span></li>'
        for n, name, _ in C.FLEET[:4])
    body = f"""{head(p, p.t(H['title']), p.t(H['meta']), schema=True)}{header(p, 'home')}
<main id="main">
<section class="hero">
  <div class="hero-media" data-parallax>{img(p, 'escort-tarmac-sunset', p.t(C.L('رجل أعمال مع فريق الحراسة وسيارة فاخرة وطائرة خاصة عند الغروب', 'An executive with his protection team, a luxury car and a private jet at sunset')), '100vw', eager=True)}</div>
  <div class="container hero-content">
    <p class="kicker">{p.t(H['hero_kicker'])}</p>
    <h1 class="display">{p.t(H['hero_title'])}</h1>
    <p class="lead">{p.t(H['hero_text'])}</p>
    <div class="btn-row">
      <a class="btn btn-silver" href="contact.html">{p.t(C.UI['request'])}</a>
      <a class="btn btn-ghost" href="#services">{p.t(H['hero_cta2'])}</a>
    </div>
    <p class="amman-clock" data-amman-clock hidden></p>
  </div>
</section>

<section class="section intro">
  <div class="container narrow center reveal">
    <span class="ornament" aria-hidden="true"></span>
    <h2 class="h2">{p.t(H['intro_title'])}</h2>
    <p class="lead">{p.t(H['intro_text'])}</p>
  </div>
  <div class="container">
    <ul class="stats reveal">{stats}</ul>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">{p.t(H['services_title'])}</h2>
      <p class="lead">{p.t(H['services_text'])}</p>
    </div>
    {services_grid(p)}
  </div>
</section>

{planner_block(p)}

<section class="section">
  <div class="container split">
    <div class="split-media reveal"><span class="frame frame-square">{img(p, 'tarmac-meet', p.t(C.L('سيارتا فان فاخرتان وفريق استقبال بجانب طائرة خاصة', 'Two luxury vans and a reception team beside a private jet')), '(min-width: 900px) 50vw, 100vw')}</span></div>
    <div class="split-text reveal">
      <p class="kicker">{p.t(H['feature_kicker'])}</p>
      <h2 class="h2">{p.t(H['feature_title'])}</h2>
      <p class="lead">{p.t(H['feature_text'])}</p>
      <a class="text-link" href="airport.html">{p.t(C.UI['discover'])}{icon('arrow', 'icon arrow')}</a>
    </div>
  </div>
</section>

<section class="section section-alt spotlight" data-spotlight>
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">{p.t(H['fleet_title'])}</h2>
      <p class="lead">{p.t(H['fleet_text'])}</p>
    </div>
    <ul class="fleet-grid">{fleet_preview}</ul>
    <div class="center reveal"><a class="btn btn-ghost" href="cars.html">{p.t(H['fleet_cta'])}</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">{p.t(H['celebs_title'])}</h2>
      <p class="lead">{p.t(H['celebs_text'])}</p>
    </div>
    </div>
    {celebs_marquee(p)}
</section>

<section class="section section-alt">
  <div class="container split founder-teaser">
    <div class="split-media reveal"><span class="frame frame-portrait frame-founder" data-founder>{img(p, 'founder-portrait', p.t(C.ABOUT['founder_name']), '(min-width: 900px) 40vw, 100vw')}</span></div>
    <div class="split-text reveal">
      <p class="kicker">{p.t(H['founder_kicker'])}</p>
      <blockquote class="quote">“{p.t(H['founder_quote'])}”</blockquote>
      <p class="signature">{p.t(C.ABOUT['founder_name'])}<span>{p.t(C.ABOUT['founder_role'])}</span></p>
      <a class="text-link" href="about.html">{p.t(H['founder_cta'])}{icon('arrow', 'icon arrow')}</a>
    </div>
  </div>
</section>

{cta_band(p)}
</main>
{footer(p)}"""
    return body


FOCUS = {"chauffeur-service": "focus-right"}


def includes_block(p, s):
    items = "".join(f'<li>{icon("diamond", "icon bullet")}<span>{p.t(i)}</span></li>' for i in s["includes"])
    side = ""
    if s["gallery"]:
        g = s["gallery"][0]
        side = f'<div class="split-media reveal"><span class="frame frame-portrait {FOCUS.get(g, "")}">{img(p, g, p.t(s["title"]), "(min-width: 900px) 45vw, 100vw")}</span></div>'
    cls = "split" if side else "narrow"
    return f"""<section class="section section-alt">
  <div class="container {cls}">
    <div class="split-text reveal">
      <h2 class="h2">{p.t(C.UI['included'])}</h2>
      <ul class="check-list">{items}</ul>
    </div>
    {side}
  </div>
</section>"""


def steps_block(p, s):
    steps = s.get("steps", C.STEPS_DEFAULT)
    items = "".join(f'<li class="step reveal"><span class="step-num">0{i}</span><h3 class="h3">{p.t(t)}</h3><p>{p.t(d)}</p></li>'
                    for i, (t, d) in enumerate(steps, 1))
    return f"""<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2 class="h2">{p.t(C.UI['how'])}</h2></div>
    <ol class="steps">{items}</ol>
  </div>
</section>"""


def facts_block(p, s):
    rows = list(s["facts"])
    rows.append((C.UI["price"], s.get("price", C.PRICE_ON_REQUEST)))
    rows.append((C.UI["payment"], C.UI["payment_value"]))
    items = "".join(f'<div class="fact"><dt>{p.t(k)}</dt><dd>{p.t(v)}</dd></div>' for k, v in rows)
    return f"""<section class="section section-alt">
  <div class="container narrow">
    <h2 class="h2 reveal">{p.t(C.UI['details'])}</h2>
    <dl class="facts reveal">{items}</dl>
  </div>
</section>"""


def gallery_block(p, s, names):
    if not names:
        return ""
    portrait = all(ratio(n) < 1.2 for n in names)
    items = "".join(f'<li class="reveal"><span class="frame {"frame-portrait" if portrait else "frame-wide"}">{img(p, n, p.t(s["title"]), "(min-width: 900px) 33vw, 100vw")}</span></li>' for n in names)
    return f"""<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2 class="h2">{p.t(C.UI['gallery'])}</h2></div>
    <ul class="gallery cols-{len(names)}">{items}</ul>
  </div>
</section>"""


def faq_block(p, s):
    items = "".join(f'<details class="faq-item"><summary>{p.t(q)}<span class="faq-icon" aria-hidden="true"></span></summary><p>{p.t(a)}</p></details>' for q, a in s["faqs"])
    return f"""<section class="section">
  <div class="container narrow">
    <h2 class="h2 reveal">{p.t(C.UI['faq'])}</h2>
    <div class="faq reveal">{items}</div>
  </div>
</section>"""


def fleet_block(p):
    filters = [("all", C.L("الكل", "All"))] + [(k, v) for k, v in C.CAR_CATEGORIES.items()]
    btns = "".join(f'<button type="button" class="chip" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{p.t(v)}</button>' for k, v in filters)
    def card(n, name, cat):
        featured = cat == "van"
        sizes = "(min-width: 1280px) 1200px, 100vw" if featured else "(min-width: 1100px) 33vw, (min-width: 640px) 50vw, 100vw"
        return (f'<li class="fleet-card{" featured" if featured else ""}" data-cat="{cat}">'
                f'<button type="button" class="car-open" data-car="{esc(name)}" data-car-cat="{esc(p.t(C.CAR_CATEGORIES[cat]))}" aria-haspopup="dialog">'
                f'<span class="frame">{img(p, n, name, sizes)}</span>'
                f'<span class="fleet-name">{name}</span><span class="fleet-cat">{p.t(C.CAR_CATEGORIES[cat])}</span>'
                f'<span class="fleet-more">{p.t(C.CAR_DIALOG["view"])}{icon("arrow", "icon arrow")}</span></button></li>')
    ordered = [c for c in C.FLEET if c[2] != "van"] + [c for c in C.FLEET if c[2] == "van"]
    cards = "".join(card(*c) for c in ordered)
    return f"""<section class="section spotlight" id="fleet" data-spotlight>
  <div class="container">
    <div class="section-head reveal"><h2 class="h2">{p.t(C.HOME['fleet_title'])}</h2></div>
    <div class="chips reveal" role="group" aria-label="{p.t(C.L('تصفية الأسطول', 'Filter the fleet'))}">{btns}</div>
    <ul class="fleet-grid fleet-full" data-fleet>{cards}</ul>
  </div>
</section>
{car_dialog(p)}"""


def car_dialog(p):
    D = C.CAR_DIALOG
    facts = "".join(f'<div class="fact"><dt>{p.t(k)}</dt><dd{" data-car-cat-out" if i == 0 else ""}>{p.t(v)}</dd></div>' for i, (k, v) in enumerate(D["facts"]))
    return f"""<dialog class="car-dialog" data-car-dialog aria-labelledby="car-dialog-title">
  <div class="car-dialog-inner">
    <button type="button" class="dialog-close" data-car-close aria-label="{p.t(C.UI['close'])}">{icon('close')}</button>
    <div class="car-dialog-media"><img data-car-img src="" alt="" width="1600" height="900"></div>
    <div class="car-dialog-body">
      <p class="kicker">{p.t(C.SERVICE_BY_SLUG_TITLE)}</p>
      <h2 class="h2" id="car-dialog-title" data-car-title></h2>
      <dl class="facts">{facts}</dl>
      <div class="btn-row">
        <a class="btn btn-silver" href="contact.html?services=cars#request" data-car-request>{p.t(D['request'])}</a>
        <a class="btn btn-ghost" href="{wa_link(p)}" target="_blank" rel="noopener noreferrer" data-car-wa>{icon('whatsapp')}{p.t(C.UI['whatsapp'])}</a>
      </div>
    </div>
  </div>
</dialog>"""


def jets_block(p):
    cards = "".join(f'<li class="jet-class reveal"><span class="jet-num">{n}</span><span class="jet-unit">{p.t(C.L("راكباً", "passengers"))}</span><p>{p.t(d)}</p></li>'
                    for n, d in C.JET_CLASSES)
    return f"""<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2 class="h2">{p.t(C.L('اختر حجم طائرتك', 'Choose your aircraft size'))}</h2></div>
    <ul class="jet-classes">{cards}</ul>
  </div>
</section>"""


def events_extra(p):
    return f"""<section class="section">
  <div class="container split">
    <div class="split-text reveal">
      <p class="kicker">{p.t(C.L('الفنانون', 'Artists'))}</p>
      <h2 class="h2">{p.t(C.L('أي فنان عربي، في ليلتكم', 'Any Arab artist, on your night'))}</h2>
      <p class="lead">{p.t(C.L('نحجز لكم الفنان الذي تحلمون به، حسب جدول مواعيده. ومن الفنانين الذين أحيوا أعراساً نظّمناها:', 'We book the artist you dream of, subject to their schedule. Among those who have performed at weddings we organized:'))}</p>
      <ul class="artist-names">{"".join(f"<li>{p.t(a)}</li>" for a in C.WEDDING_ARTISTS)}</ul>
    </div>
    <div class="split-media reveal"><span class="frame frame-portrait">{img(p, 'wedding-heart-arch', p.t(C.L('ديكور عرس بقوس على شكل قلب وطاولات مزينة بالورد', 'Wedding decor with a heart-shaped arch and flower-dressed tables')), '(min-width: 900px) 45vw, 100vw')}</span></div>
  </div>
</section>
<section class="section section-alt">
  <div class="container split reverse">
    <div class="split-text reveal">
      <p class="kicker">{p.t(C.L('المؤتمرات', 'Conferences'))}</p>
      <h2 class="h2">{p.t(C.L('مؤتمرات بمعايير عالمية', 'Conferences to world-class standards'))}</h2>
      <p class="lead">{p.t(C.L('نوفّر كل ما يلزم: الصوت، والشاشات، والتسجيل، واستقبال الضيوف، لتبدأ فعاليتك بثقة وتنتهي بنجاح.', 'We provide everything you need: sound, screens, recording and guest reception, so your event starts with confidence and ends in success.'))}</p>
    </div>
    <div class="split-media reveal"><span class="frame frame-wide">{img(p, 'conference-hall', p.t(C.L('قاعة مؤتمرات فاخرة جاهزة بمنصة وشاشة', 'A luxury conference hall set with a stage and screen')), '(min-width: 900px) 50vw, 100vw')}</span></div>
  </div>
</section>"""


def build_service(p, s):
    p.service = s
    hero_name = s["img"]
    portrait_hero = ratio(hero_name) < 1.2
    title_tag = f"{p.t(s['title'])} | {C.BRAND}"
    ph = page_head(p, p.t(s["kicker"]), p.t(s["title"]), p.t(s["lead"]), service=s["slug"])
    if portrait_hero:
        hero = f"""<section class="page-hero split-hero">
  <div class="container split">
    <div class="split-text">{ph}</div>
    <div class="split-media"><span class="frame frame-portrait">{img(p, hero_name, p.t(s['title']), '(min-width: 900px) 45vw, 100vw', eager=True)}</span></div>
  </div>
</section>"""
    else:
        hero = f"""<section class="page-hero">
  <div class="container narrow-wide">{ph}</div>
  <div class="container"><figure class="wide-figure" data-parallax>{img(p, hero_name, p.t(s['title']), '(min-width: 1280px) 1200px, 100vw', eager=True)}</figure></div>
</section>"""

    extra_top = {"cars": fleet_block(p), "jets": jets_block(p)}.get(s["slug"], "")
    if s["slug"] == "cars":
        # chauffeur image beside the includes list
        s = dict(s, gallery=["chauffeur-service"])
    events = events_extra(p) if s["slug"] == "events" else ""
    gallery = gallery_block(p, s, s["gallery"][1:])
    others = f"""<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><h2 class="h2">{p.t(C.L('خدمات أخرى', 'More services'))}</h2></div>
    {services_grid(p, exclude=s['slug'])}
  </div>
</section>"""
    return f"""{head(p, title_tag, p.t(s['meta']))}{header(p, s['slug'])}
<main id="main">
{hero}
{extra_top}
{includes_block(p, s)}
{events}
{gallery}
{steps_block(p, s)}
{facts_block(p, s)}
{faq_block(p, s)}
{cta_band(p)}
{others}
</main>
{footer(p)}"""


def build_about(p):
    A = C.ABOUT
    values = "".join(f'<li class="value reveal">{icon("diamond", "icon value-icon")}<h3 class="h3">{p.t(t)}</h3><p>{p.t(d)}</p></li>' for t, d in A["values"])
    paras = "".join(f"<p>{p.t(x)}</p>" for x in A["founder_paragraphs"])
    return f"""{head(p, f"{p.t(A['title'])} | {C.BRAND}", p.t(A['meta']))}{header(p, 'about')}
<main id="main">
<section class="page-hero">
  <div class="container narrow-wide">
    <p class="kicker">{p.t(C.HOME['hero_kicker'])}</p>
    <h1 class="h1">{p.t(A['title'])}</h1>
    <p class="lead">{p.t(A['lead'])}</p>
  </div>
</section>
<section class="section section-alt" id="founder">
  <div class="container split founder">
    <div class="split-media reveal"><span class="frame frame-portrait frame-founder" data-founder>{img(p, 'founder-portrait', p.t(A['founder_name']), '(min-width: 900px) 40vw, 100vw')}</span></div>
    <div class="split-text reveal">
      <p class="kicker">{p.t(A['founder_title'])}</p>
      <div class="prose">{paras}</div>
      <p class="signature">{p.t(A['founder_name'])}<span>{p.t(A['founder_role'])}</span></p>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2 class="h2">{p.t(A['values_title'])}</h2></div>
    <ul class="values">{values}</ul>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><h2 class="h2">{p.t(C.HOME['celebs_title'])}</h2><p class="lead">{p.t(C.HOME['celebs_text'])}</p></div>
    {celebs_grid(p)}
  </div>
</section>
<section class="section">
  <div class="container narrow center reveal">
    <span class="ornament" aria-hidden="true"></span>
    <h2 class="h2">{p.t(A['network_title'])}</h2>
    <p class="lead">{p.t(A['network_text'])}</p>
  </div>
</section>
{cta_band(p)}
</main>
{footer(p)}"""


def field(id_, label, control):
    return f'<div class="field"><label for="{id_}">{label}</label>{control}</div>'


def build_contact(p):
    F = C.CONTACT_PAGE
    t = p.t
    opts = "".join(f'<option value="{s["slug"]}">{t(s["title"])}</option>' for s in C.SERVICES)
    car_opts = "".join(f'<option>{name}</option>' for _, name, _ in C.FLEET)
    groups = {
        "cars": field("f-driver", t(F["driver"]), f'<select id="f-driver" name="chauffeur"><option>{t(F["with_driver"])}</option><option>{t(F["self_drive"])}</option></select>')
        + field("f-days", t(F["days"]), '<input id="f-days" name="days" type="number" min="2" max="365" inputmode="numeric">')
        + field("f-car", t(F["car"]), f'<select id="f-car" name="car"><option value="">—</option>{car_opts}</select>'),
        "jets": field("f-pax", t(F["passengers"]), '<select id="f-pax" name="passengers"><option>6</option><option>8</option><option>12</option><option>16</option></select>')
        + field("f-route", t(F["route"]), '<input id="f-route" name="route" type="text" maxlength="120">'),
        "yachts": field("f-guests", t(F["guests"]), '<input id="f-guests" name="guests" type="number" min="1" max="200" inputmode="numeric">')
        + field("f-city", t(F["city"]), '<input id="f-city" name="city" type="text" maxlength="80">'),
        "airport": field("f-airport", t(F["airport"]), f'<select id="f-airport" name="airport"><option>{t(C.L("مطار الملكة علياء الدولي", "Queen Alia International"))}</option><option>{t(C.L("مطار عمّان المدني (ماركا)", "Amman Civil (Marka)"))}</option></select>')
        + field("f-flight", t(F["flight"]), '<input id="f-flight" name="flight" type="text" maxlength="80">'),
        "events": field("f-etype", t(F["event_type"]), f'<select id="f-etype" name="occasion"><option>{t(F["wedding"])}</option><option>{t(F["conference"])}</option></select>')
        + field("f-eguests", t(F["guests"]), '<input id="f-eguests" name="event_guests" type="number" min="1" max="5000" inputmode="numeric">'),
    }
    titles = {s["slug"]: t(s["title"]) for s in C.SERVICES}
    group_html = "".join(f'<fieldset class="field-group" data-service-fields="{k}" hidden><legend>{titles[k]}</legend>{v}</fieldset>' for k, v in groups.items())
    subject_prefix = t(C.L("طلب جديد من الموقع", "New website request"))
    return f"""{head(p, f"{t(F['title'])} | {C.BRAND}", t(F['meta']), schema=True)}{header(p, 'contact')}
<main id="main">
<section class="page-hero">
  <div class="container narrow-wide">
    <p class="kicker">{t(C.UI['cs_247'])}</p>
    <h1 class="h1">{t(F['title'])}</h1>
    <p class="lead">{t(F['lead'])}</p>
    <p class="amman-clock" data-amman-clock hidden></p>
  </div>
</section>
<section class="section section-tight">
  <div class="container contact-grid">
    <form class="request-form" id="request" novalidate action="{C.FORM_ACTION}" method="POST" data-request-form
          data-subject-prefix="{esc(subject_prefix)}" data-wa-number="{C.CONTACT['whatsapp']}"
          data-wa-intro="{esc(t(C.L('مرحباً Titanium Shop، أرسلت طلباً عبر الموقع:', 'Hello Titanium Shop, I just sent a request on your website:')))}">
      <h2 class="h3">{t(F['form_title'])}</h2>
      <input type="hidden" name="_subject" value="{esc(subject_prefix)}">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_next" value="{C.SITE_URL}/{'' if p.lang == 'en' else 'ar/'}thanks.html">
      <input type="hidden" name="service" value="">
      <input type="hidden" name="language" value="{'English' if p.lang == 'en' else 'العربية'}">
      <div class="hp" aria-hidden="true"><label for="f-honey">Leave empty</label><input id="f-honey" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
      {field('f-name', t(F['name']), '<input id="f-name" name="name" type="text" required maxlength="80" autocomplete="name">')}
      {field('f-phone', t(F['phone']), '<input id="f-phone" name="phone" type="tel" required maxlength="20" pattern="[+0-9 ()-]{7,20}" autocomplete="tel" dir="ltr" placeholder="+962 7…">')}
      {field('f-email', t(F['email']), '<input id="f-email" name="email" type="email" maxlength="120" autocomplete="email" dir="ltr">')}
      <fieldset class="field" data-service-picker>
        <legend>{t(F['services_pick'])}</legend>
        {service_choices(p, '', 'f')}
        <p class="field-error" data-service-error hidden>{t(F['services_error'])}</p>
      </fieldset>
      {group_html}
      {field('f-date', t(F['date']), '<input id="f-date" name="date" type="date">')}
      {field('f-details', t(F['details']), '<textarea id="f-details" name="details" rows="4" maxlength="1000"></textarea>')}
      <button class="btn btn-silver btn-block" type="submit">{t(F['send'])}</button>
      <p class="form-note">{t(F['note'])} <a href="privacy.html">{t(C.UI['privacy'])}</a></p>
    </form>
    <aside class="contact-card">
      <h2 class="h3">{t(F['direct_title'])}</h2>
      <ul class="contact-lines">
        <li><a href="{wa_link(p)}" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}<span><strong>{t(C.UI['whatsapp'])}</strong><span dir="ltr">{C.CONTACT['whatsapp_display']}</span></span></a></li>
        <li><a href="tel:{C.CONTACT['phone_tel']}">{icon('phone')}<span><strong>{t(C.UI['call'])}</strong><span dir="ltr">{C.CONTACT['phone_display']}</span></span></a></li>
        <li><a href="tel:{C.CONTACT['mgmt_tel']}">{icon('phone')}<span><strong>{t(F['mgmt'])}</strong><span dir="ltr">{C.CONTACT['mgmt_display']}</span></span></a></li>
        <li><a href="mailto:{C.CONTACT['email']}">{icon('mail')}<span><strong>Email</strong><span>{C.CONTACT['email']}</span></span></a></li>
        <li><a href="{C.CONTACT['map_url']}" target="_blank" rel="noopener noreferrer">{icon('pin')}<span><strong>{t(F['address_title'])}</strong><span>{t(C.CONTACT['address'])}</span><span class="small-link">{t(F['open_map'])}</span></span></a></li>
        <li><span class="plain">{icon('clock')}<span><strong>{t(F['hours_title'])}</strong><span>{t(C.UI['cs_247'])}</span></span></span></li>
      </ul>
    </aside>
  </div>
</section>
</main>
{footer(p)}"""


def build_simple(p, title, inner, noindex=False, description=""):
    return f"""{head(p, f"{title} | {C.BRAND}", description or title, noindex=noindex)}{header(p)}
<main id="main">
{inner}
</main>
{footer(p)}"""


def build_thanks(p):
    T = C.THANKS
    inner = f"""<section class="page-hero center-page">
  <div class="container narrow center">
    <span class="ornament" aria-hidden="true"></span>
    <h1 class="h1">{p.t(T['title'])}</h1>
    <p class="lead">{p.t(T['text'])}</p>
    <p>{p.t(T['wa_text'])}</p>
    <div class="btn-row center">
      <a class="btn btn-silver" href="{wa_link(p)}" target="_blank" rel="noopener noreferrer" data-wa-continue>{icon('whatsapp')}{p.t(T['wa_btn'])}</a>
      <a class="btn btn-ghost" href="index.html">{p.t(C.UI['back_home'])}</a>
    </div>
  </div>
</section>"""
    return build_simple(p, p.t(T["title"]), inner, noindex=True)


def build_404(p):
    N = C.NOT_FOUND
    inner = f"""<section class="page-hero center-page">
  <div class="container narrow center">
    <span class="ornament" aria-hidden="true"></span>
    <h1 class="h1">{p.t(N['title'])}</h1>
    <p class="lead">{p.t(N['text'])}</p>
    <div class="btn-row center">
      <a class="btn btn-silver" href="{C.SITE_URL}/{'ar/' if p.lang == 'ar' else ''}">{p.t(C.UI['back_home'])}</a>
      <a class="btn btn-ghost" href="{wa_link(p)}" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}{p.t(C.UI['whatsapp'])}</a>
    </div>
  </div>
</section>"""
    return build_simple(p, p.t(N["title"]), inner, noindex=True)


def build_privacy(p):
    P = C.PRIVACY
    secs = "".join(f'<h2 class="h3">{p.t(h)}</h2><p>{p.t(b)}</p>' for h, b in P["sections"])
    inner = f"""<section class="page-hero">
  <div class="container narrow">
    <h1 class="h1">{p.t(P['title'])}</h1>
    <div class="prose">{secs}</div>
  </div>
</section>"""
    return build_simple(p, p.t(P["title"]), inner, description=p.t(P["title"]))


# ------------------------------------------------------------------ main ---

def write(lang, filename, text):
    out = ROOT / ("" if lang == "en" else "ar") / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


def main():
    pages = []
    for lang in LANGS:
        write(lang, "index.html", build_home(Page(lang, "index.html")))
        for s in C.SERVICES:
            fn = f"{s['slug']}.html"
            write(lang, fn, build_service(Page(lang, fn), s))
        write(lang, "about.html", build_about(Page(lang, "about.html")))
        write(lang, "contact.html", build_contact(Page(lang, "contact.html")))
        write(lang, "privacy.html", build_privacy(Page(lang, "privacy.html")))
        write(lang, "thanks.html", build_thanks(Page(lang, "thanks.html")))
        write(lang, "404.html", build_404(Page(lang, "404.html")))
    # sitemap (thanks/404 excluded)
    files = ["index.html"] + [f"{s['slug']}.html" for s in C.SERVICES] + ["about.html", "contact.html", "privacy.html"]
    urls = []
    for f in files:
        for lang in LANGS:
            p = Page(lang, f)
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{p.url(l)}"/>' for l in LANGS)
            urls.append(f"<url><loc>{p.url()}</loc>{alts}</url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    print("built", len(files) * 2 + 4, "pages")


if __name__ == "__main__":
    main()
