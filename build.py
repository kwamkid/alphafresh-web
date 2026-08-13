# Alpha Fresh — static site generator.
# Keeps the nav, footer and <head> identical across every page.
# Run:  python3 build.py
import hashlib
import os
from translations import TR, MONTHS, META, GLOSSARY

FONT_CSS = ("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600"
            "&family=Inter:wght@400;500;600;700&family=Caveat:wght@500;600;700&display=swap")

MEDIA_HOST = "https://d2ol7oe51mr4n9.cloudfront.net"
MEDIA = f"{MEDIA_HOST}/user_3FvAUpXpCnZUma0p4ZCgNFe1CGD"
# Every image is now served from our own domain — nothing is fetched
# from a third-party CDN any more.
IMG = {
    "orchard":    "images/thai-longan-orchard-lamphun.webp",
    "hands":  "images/longan-hand-picking.webp",
    "shedfront":  "images/longan-packing-house-lamphun.webp",
    "sorting":  "images/longan-hand-sorting.webp",
    "qc":  "images/longan-quality-inspection.webp",
    "cold":  "images/longan-cold-room.webp",
    "loading":  "images/refrigerated-container-loading.webp",
    "longanpack":  "images/longan-export-carton.webp",
    "durian":  "images/thai-durian-monthong.webp",
    "mangosteen":  "images/thai-mangosteen.webp",
    "lychee":  "images/thai-lychee.webp",
}
# Hero clips, re-encoded to 1280px H.264 without audio: 59.9 MB became 3.6 MB.
# "mobile" is a 720px cut for phones.
VID = {
    "orchard": "videos/thai-longan-orchard.mp4",
    "shed":    "videos/longan-packing-house.mp4",
    "line":    "videos/longan-grading-line.mp4",
    "mobile":  "videos/thai-longan-orchard-mobile.mp4",
}

NAV = [
    ("index.html",    "หน้าแรก",   "Home"),
    ("about.html",    "เกี่ยวกับเรา", "About"),
    ("products.html", "สินค้า",     "Products"),
    ("quality.html",  "คุณภาพและการส่งออก", "Quality &amp; Export"),
    ("contact.html",  "ติดต่อ",     "Contact"),
]


def G(term, label=None):
    """A trade term with a plain-language tooltip in all four languages."""
    en, th, zh, ar = GLOSSARY[term]
    return (f'<span class="term" tabindex="0" role="button" aria-label="{term}">{label or term}'
            f'<span class="tip"><b>{term}</b>'
            f'<span class="i18n"><span data-en>{en}</span><span data-th>{th}</span>'
            f'<span data-zh>{zh}</span><span data-ar dir="rtl">{ar}</span></span></span></span>')


FLAG_SVG = {
"cn": '<rect width="60" height="60" fill="#DE2910"/><g fill="#FFDE00"><circle cx="16" cy="18" r="7"/><circle cx="29" cy="9" r="2.6"/><circle cx="35" cy="16" r="2.6"/><circle cx="34" cy="26" r="2.6"/><circle cx="27" cy="32" r="2.6"/></g>',
"hk": '<rect width="60" height="60" fill="#DE2910"/><g fill="#fff"><circle cx="30" cy="18" r="5"/><circle cx="42" cy="27" r="5"/><circle cx="37" cy="41" r="5"/><circle cx="23" cy="41" r="5"/><circle cx="18" cy="27" r="5"/></g>',
"sg": '<rect width="60" height="30" fill="#EF3340"/><rect y="30" width="60" height="30" fill="#fff"/><circle cx="16" cy="15" r="9" fill="#fff"/><circle cx="21" cy="15" r="9" fill="#EF3340"/><g fill="#fff"><circle cx="24" cy="9" r="1.8"/><circle cx="28" cy="14" r="1.8"/><circle cx="26" cy="20" r="1.8"/><circle cx="20" cy="20" r="1.8"/><circle cx="18" cy="14" r="1.8"/></g>',
"nl": '<rect width="60" height="20" fill="#AE1C28"/><rect y="20" width="60" height="20" fill="#fff"/><rect y="40" width="60" height="20" fill="#21468B"/>',
"fr": '<rect width="20" height="60" fill="#0055A4"/><rect x="20" width="20" height="60" fill="#fff"/><rect x="40" width="20" height="60" fill="#EF4135"/>',
"ae": '<rect width="60" height="20" fill="#00732F"/><rect y="20" width="60" height="20" fill="#fff"/><rect y="40" width="60" height="20" fill="#000"/><rect width="18" height="60" fill="#C8102E"/>',
"gb": '<rect width="60" height="60" fill="#012169"/><path d="M0 0l60 60M60 0L0 60" stroke="#fff" stroke-width="12"/><path d="M0 0l60 60M60 0L0 60" stroke="#C8102E" stroke-width="7"/><path d="M30 0v60M0 30h60" stroke="#fff" stroke-width="20"/><path d="M30 0v60M0 30h60" stroke="#C8102E" stroke-width="12"/>',
"th": '<rect width="60" height="60" fill="#fff"/><rect width="60" height="10" fill="#A51931"/><rect y="50" width="60" height="10" fill="#A51931"/><rect y="20" width="60" height="20" fill="#2D2A4A"/>',
"jp": '<rect width="60" height="60" fill="#fff"/><circle cx="30" cy="30" r="13" fill="#BC002D"/>',
}


def flags(*codes):
    out = ""
    for i, c in enumerate(codes):
        out += (f'<span class="mflag"><svg viewBox="0 0 60 60" aria-hidden="true">'
                f'<g clip-path="url(#f{c})"><clipPath id="f{c}"><circle cx="30" cy="30" r="30"/></clipPath>'
                f'{FLAG_SVG[c]}</g></svg></span>')
    return f'<span class="mflags">{out}</span>'

TICK = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>')
ARROW = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')


LANGS = ("en", "th", "zh", "ar")


def L(th, en):
    """One phrase in every language the site speaks.

    English and Thai are written inline at the call site; Chinese and Arabic
    come from translations.py. The wrapper lets the stylesheet fall back to
    English for any phrase that has not been translated yet, instead of
    showing nothing at all.
    """
    out = f'<span class="i18n"><span data-en>{en}</span><span data-th>{th}</span>'
    pair = TR.get(en)
    if pair:
        zh, ar = pair
        out += f'<span data-zh>{zh}</span><span data-ar dir="rtl">{ar}</span>'
    return out + "</span>"


def nav(current):
    items = ""
    for href, th, en in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items += f'      <li><a href="{href}"{cur}>{L(th, en)}</a></li>\n'
    return f"""<nav class="nav">
  <div class="nav-in">
    <a class="logo" href="index.html" aria-label="Alpha Fresh — home">
      <span class="logo-mark">
        <img class="l-white" src="images/logo-icon-white.webp" alt="" aria-hidden="true">
        <img class="l-dark" src="images/logo-icon.webp" alt="" aria-hidden="true">
      </span>
      <span class="logo-text">Alpha<small>Fresh</small></span>
    </a>
    <ul class="menu" id="menu">
{items}    </ul>
    <div class="lang" id="langpick">
      <button class="lang-btn" type="button" aria-haspopup="listbox" aria-expanded="false" aria-label="Language">
        <span class="mflag fl fl-en"><svg viewBox="0 0 60 60" aria-hidden="true"><g clip-path="url(#ben)"><clipPath id="ben"><circle cx="30" cy="30" r="30"/></clipPath>{FLAG_SVG["gb"]}</g></svg></span>
        <span class="mflag fl fl-th"><svg viewBox="0 0 60 60" aria-hidden="true"><g clip-path="url(#bth)"><clipPath id="bth"><circle cx="30" cy="30" r="30"/></clipPath>{FLAG_SVG["th"]}</g></svg></span>
        <span class="mflag fl fl-zh"><svg viewBox="0 0 60 60" aria-hidden="true"><g clip-path="url(#bzh)"><clipPath id="bzh"><circle cx="30" cy="30" r="30"/></clipPath>{FLAG_SVG["cn"]}</g></svg></span>
        <span class="mflag fl fl-ar"><svg viewBox="0 0 60 60" aria-hidden="true"><g clip-path="url(#bar)"><clipPath id="bar"><circle cx="30" cy="30" r="30"/></clipPath>{FLAG_SVG["ae"]}</g></svg></span>
        <span class="lang-now"><span class="fl fl-en">English</span><span class="fl fl-th">ไทย</span><span class="fl fl-zh">中文</span><span class="fl fl-ar">العربية</span></span>
        <svg class="chev" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <div class="lang-list" role="listbox">
        <button class="lang-opt" type="button" data-set-lang="en" role="option"><span class="mflag"><svg viewBox="0 0 60 60" aria-hidden="true"><g clip-path="url(#len)"><clipPath id="len"><circle cx="30" cy="30" r="30"/></clipPath>{FLAG_SVG["gb"]}</g></svg></span>English</button>
        <button class="lang-opt" type="button" data-set-lang="th" role="option"><span class="mflag"><svg viewBox="0 0 60 60" aria-hidden="true"><g clip-path="url(#lth)"><clipPath id="lth"><circle cx="30" cy="30" r="30"/></clipPath>{FLAG_SVG["th"]}</g></svg></span>ไทย</button>
        <button class="lang-opt" type="button" data-set-lang="zh" role="option"><span class="mflag"><svg viewBox="0 0 60 60" aria-hidden="true"><g clip-path="url(#lzh)"><clipPath id="lzh"><circle cx="30" cy="30" r="30"/></clipPath>{FLAG_SVG["cn"]}</g></svg></span>中文</button>
        <button class="lang-opt" type="button" data-set-lang="ar" role="option"><span class="mflag"><svg viewBox="0 0 60 60" aria-hidden="true"><g clip-path="url(#lar)"><clipPath id="lar"><circle cx="30" cy="30" r="30"/></clipPath>{FLAG_SVG["ae"]}</g></svg></span>العربية</button>
      </div>
    </div>
    <button class="burger" aria-label="Menu">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</nav>"""


FOOTER = f"""<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <div class="flogo"><img src="images/logo-stack-white.webp" alt="Alpha Fresh" width="146" height="128"></div>
        <p style="color:rgba(255,255,255,.55);margin:0;max-width:34ch">
          {L("บริษัท อัลฟ่า เฟรช จำกัด — นำเข้าและส่งออกผลไม้สด ลำพูน ประเทศไทย",
             "Alpha Fresh Co., Ltd. — fresh fruit import &amp; export. Lamphun, Thailand.")}</p>
      </div>
      <div><h4>{L("สินค้า", "Products")}</h4>
        <ul>
          <li><a href="products.html#longan">{L("ลำไยสด", "Fresh longan")}</a></li>
          <li><a href="products.html#durian">{L("ทุเรียนหมอนทอง", "Monthong durian")}</a></li>
          <li><a href="products.html#mangosteen">{L("มังคุด", "Mangosteen")}</a></li>
          <li><a href="products.html#lychee">{L("ลิ้นจี่", "Lychee")}</a></li>
        </ul></div>
      <div><h4>{L("บริษัท", "Company")}</h4>
        <ul>
          <li><a href="about.html">{L("เกี่ยวกับเรา", "About us")}</a></li>
          <li><a href="quality.html#process">{L("ขั้นตอนการทำงาน", "How we work")}</a></li>
          <li><a href="quality.html#standards">{L("มาตรฐานคุณภาพ", "Quality standards")}</a></li>
          <li><a href="quality.html#markets">{L("ตลาดเป้าหมาย", "Target markets")}</a></li>
        </ul></div>
      <div><h4>{L("ติดต่อ", "Contact")}</h4>
        <ul>
          <li><a href="mailto:alphafreshthailand@gmail.com">alphafreshthailand@gmail.com</a></li>
          <li><a href="tel:+66898949491">+66 89 894 9491</a></li>
          <li><a href="contact.html">{L("ขอใบเสนอราคา", "Request a quote")}</a></li>
          <li><a href="sitemap.xml">Sitemap</a></li>
        </ul></div>
    </div>
    <div class="fbot">
      <span>© 2026 Alpha Fresh Co., Ltd.</span>
      {L("ข้อมูลบนเว็บนี้เป็นตัวอย่างสำหรับฉบับร่าง", "Figures on this draft site are illustrative placeholders.")}
    </div>
  </div>
</footer>"""

BAND = f"""<div class="band">
  <div class="wrap rv">
    <h2>{L("สนใจสั่งซื้อ หรืออยากได้ราคาก่อน?", "Ready to order — or just want a price first?")}</h2>
    <p>{L("บอกเราสั้น ๆ ว่าต้องการผลไม้อะไร ปริมาณเท่าไร ส่งไปที่ไหน แล้วเราจะตอบกลับพร้อมราคาและกำหนดตัดภายใน 2 วันทำการ",
          "Tell us the fruit, the volume and the destination. You will get a price and a picking schedule back within two working days.")}</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="contact.html">{L("ขอใบเสนอราคา", "Request a quotation")} {ARROW}</a>
      <a class="btn btn-ghost" href="products.html">{L("ดูสินค้าทั้งหมด", "See all products")}</a>
    </div>
  </div>
</div>"""

SCHEMA = """{"@context":"https://schema.org","@type":"Organization","name":"Alpha Fresh Co., Ltd.","alternateName":"บริษัท อัลฟ่า เฟรช จำกัด","url":"https://alphafreshthailand.com/","description":"Thai fruit importer turned exporter. Fresh longan, durian, mangosteen and lychee from GAP-certified orchards in Northern Thailand.","address":{"@type":"PostalAddress","addressRegion":"Lamphun","addressCountry":"TH"},"email":"alphafreshthailand@gmail.com","telephone":"+66-89-894-9491","contactPoint":{"@type":"ContactPoint","telephone":"+66-89-894-9491","email":"alphafreshthailand@gmail.com","contactType":"sales","availableLanguage":["th","en"],"areaServed":"Worldwide"}}"""


def stamp(path):
    """Short content hash, appended to asset URLs.

    _headers tells browsers to keep /assets/* for a week, which is what we want
    — but only as long as a changed file arrives under a new URL. Without this
    a visitor who has been to the site keeps the old stylesheet until the cache
    expires, and sees a half-broken page.
    """
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


CSS_V = stamp("assets/style.css")
JS_V = stamp("assets/main.js")

_ASSET_V = {}


def stamp_assets(html):
    """Images and videos are cached for 30 days. A file whose bytes change but
    whose name does not would keep serving the stale copy from the edge for a
    month, so every local media URL gets a content hash appended — a changed
    file is then simply a different URL."""
    import re

    def sub(m):
        path = m.group(1)
        if path not in _ASSET_V:
            try:
                _ASSET_V[path] = stamp(path)
            except FileNotFoundError:
                _ASSET_V[path] = None
        v = _ASSET_V[path]
        return path if v is None else f"{path}?v={v}"

    return re.sub(r"((?:images|videos)/[A-Za-z0-9._-]+\.(?:webp|png|ico|jpg|mp4))", sub, html)

SITE = "https://alphafreshthailand.com"
OG_IMAGE = f"{SITE}/{IMG['orchard']}"   # social cards need an absolute URL


def page(filename, title, desc, body, solid_nav=True, title_th="", desc_th="", preload=""):
    """Titles and descriptions are English by default (the site's default language);
    main.js swaps them to the Thai versions when the visitor picks TH."""
    body_class = ' class="solid-nav"' if solid_nav else ""
    url = SITE + ("" if filename == "index.html" else "/" + filename)
    html = f"""<!DOCTYPE html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="title-th" content="{title_th}">
<meta name="description-th" content="{desc_th}">
<meta name="title-zh" content="{META.get(filename, {}).get('zh', ('',''))[0]}">
<meta name="description-zh" content="{META.get(filename, {}).get('zh', ('',''))[1]}">
<meta name="title-ar" content="{META.get(filename, {}).get('ar', ('',''))[0]}">
<meta name="description-ar" content="{META.get(filename, {}).get('ar', ('',''))[1]}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="th" href="{url}">
<link rel="alternate" hreflang="zh" href="{url}">
<link rel="alternate" hreflang="ar" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Alpha Fresh">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="th_TH">
<meta property="og:locale:alternate" content="zh_CN">
<meta property="og:locale:alternate" content="ar_AE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMAGE}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!-- The font sheet lives on another origin, so fetching it normally costs a DNS
     lookup and a TLS handshake before anything can paint. Loading it as a
     preload and promoting it to a stylesheet once it arrives keeps it off the
     critical path; font-display:swap paints the text in a system face first. -->
<link rel="preload" as="style" href="{FONT_CSS}" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="{FONT_CSS}"></noscript>
<link rel="icon" href="images/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="images/apple-touch-icon.png">
<link rel="stylesheet" href="assets/style.css?v={CSS_V}">
{preload}<script type="application/ld+json">{SCHEMA}</script>
</head>
<body{body_class}>

{nav(filename)}

{body}

{FOOTER}
<script src="assets/main.js?v={JS_V}"></script>
</body>
</html>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(stamp_assets(html))
    print("wrote", filename, len(html), "bytes")


def phead(crumb_th, crumb_en, h1_th, h1_en, p_th, p_en, img):
    return f"""<header class="phead">
  <img class="phead-img" src="{img}" alt="" aria-hidden="true">
  <div class="wrap phead-in">
    <div class="crumb"><a href="index.html">{L("หน้าแรก", "Home")}</a> / {L(crumb_th, crumb_en)}</div>
    <h1>{L(h1_th, h1_en)}</h1>
    <p class="lead">{L(p_th, p_en)}</p>
  </div>
</header>"""


STATS = f"""<div class="stats">
  <div class="stats-in">
    <div class="stat"><b>4</b><span>{L("สินค้าหลักส่งออก", "core export products")}</span></div>
    <div class="stat"><b>20+</b><span>{L("สวนพันธมิตรมาตรฐาน GAP", "GAP-certified partner orchards")}</span></div>
    <div class="stat"><b>48 <small style="font-size:.55em;font-weight:500">hrs</small></b><span>{L("จากสวนถึงสนามบิน", "orchard to airport")}</span></div>
    <div class="stat"><b>{G("FOB")} / {G("CIF")}</b><span>{L("เงื่อนไขการส่งมอบ", "delivery terms available")}</span></div>
  </div>
</div>"""


# ---------- Thai fruit seasonality calendar ----------
# '#' peak · '-' in season · '.' out of season.  Twelve characters, Jan → Dec.
# Approximate national averages: the North and the East run a few weeks apart,
# and induced ("off-season") orchards shift longan and mango outside these bands.
SEASON = [
    ("ลำไย", "Longan", "--....-#-.--", True),
    ("ทุเรียน", "Durian", "...-##--....", True),
    ("มังคุด", "Mangosteen", "....-##--...", True),
    ("ลิ้นจี่", "Lychee", "...-#-......", True),
    ("เงาะ", "Rambutan", "....-##--...", False),
    ("ลองกอง", "Longkong", "......-##-..", False),
    ("มะม่วงน้ำดอกไม้", "Mango (Nam Dok Mai)", "--##--.....-", False),
    ("ส้มโอ", "Pomelo", ".--....-##-.", False),
    ("แก้วมังกร", "Dragon fruit", "....-##---..", False),
    ("ขนุน", "Jackfruit", "-##--.......", False),
    ("สับปะรด", "Pineapple", "##-###----##", False),
    ("มะพร้าวน้ำหอม", "Young coconut", "--###-------", False),
    ("มะขามหวาน", "Sweet tamarind", "##.........#", False),
]
# Square catalogue shots, one per fruit, keyed to the SEASON rows below.
FRUIT_PIC = {
    "Longan":  "images/fruit-longan.webp",
    "Durian":  "images/fruit-durian.webp",
    "Mangosteen":  "images/fruit-mangosteen.webp",
    "Lychee":  "images/fruit-lychee.webp",
    "Rambutan":  "images/fruit-rambutan.webp",
    "Longkong":  "images/fruit-longkong.webp",
    "Mango (Nam Dok Mai)":  "images/fruit-mango-nam-dok-mai.webp",
    "Pomelo":  "images/fruit-pomelo.webp",
    "Dragon fruit":  "images/fruit-dragon-fruit.webp",
    "Jackfruit":  "images/fruit-jackfruit.webp",
    "Pineapple":  "images/fruit-pineapple.webp",
    "Young coconut":  "images/fruit-young-coconut.webp",
    "Sweet tamarind":  "images/fruit-sweet-tamarind.webp",
}

MONTHS_EN = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
MONTHS_TH = ["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."]


def runs(band, chars):
    """Contiguous month spans, as (start, end) inclusive 0-based indices."""
    out, i = [], 0
    while i < 12:
        if band[i] in chars:
            j = i
            while j + 1 < 12 and band[j + 1] in chars:
                j += 1
            out.append((i, j))
            i = j + 1
        else:
            i += 1
    return out


def season_table():
    def month(i):
        return ('<span class="i18n">'
                f'<span data-en>{MONTHS_EN[i]}</span><span data-th>{MONTHS_TH[i]}</span>'
                f'<span data-zh>{MONTHS["zh"][i]}</span><span data-ar>{MONTHS["ar"][i]}</span>'
                '</span>')
    head = "".join(f'<th scope="col" class="m">{month(i)}</th>' for i in range(12))
    rows = ""
    prev_ours = None
    for th_name, en_name, band, ours in SEASON:
        # a label row each time the table crosses from our products to the rest
        if ours != prev_ours:
            first = " first" if prev_ours is None else ""
            label = (L("สินค้าที่เราส่งออก", "What we export")
                     if ours else L("ผลไม้ไทยอื่น ๆ", "Other Thai fruit"))
            rows += (f'      <tr class="grp{first}"><th scope="row">{label}</th>'
                     f'<td class="track" colspan="12"></td></tr>\n')
            prev_ours = ours
        bars, read = "", []
        for a, b in runs(band, "-#"):
            bars += f'<span class="bar" style="grid-column:{a + 1}/{b + 2}"></span>'
            read.append(f"{MONTHS_EN[a]}–{MONTHS_EN[b]}")
        for a, b in runs(band, "#"):
            bars += f'<span class="bar peak" style="grid-column:{a + 1}/{b + 2}"></span>'
            read.append(f"peak {MONTHS_EN[a]}–{MONTHS_EN[b]}")
        cells = (f'<td class="track" colspan="12"><span class="sr">{"; ".join(read)}</span>'
                 f'<span class="lane">{bars}</span></td>')
        tag = ' <b class="ours">{}</b>'.format(L("สินค้าเรา", "ours")) if ours else ""
        pic = (f'<img class="fpic" src="{FRUIT_PIC[en_name]}" alt="" aria-hidden="true" '
               f'loading="lazy" width="34" height="34">')
        cls = ' class="mine"' if ours else ""
        rows += (f'      <tr{cls}><th scope="row"><span class="fname">{pic}'
                 f'<span>{L(th_name, en_name)}</span>{tag}</span></th>{cells}</tr>\n')
    return f"""<div class="cal-wrap">
  <table class="cal">
    <thead><tr><th scope="col">{L("ผลไม้", "Fruit")}</th>{head}</tr></thead>
    <tbody>
{rows}    </tbody>
  </table>
</div>"""


SEASON_SECTION = f"""<section class="soft" id="season">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("ปฏิทินผลผลิต", "Harvest calendar")}</div>
      <h2>{L("ฤดูกาลผลไม้ไทย", "When Thai fruit is in season")}</h2>
      <p class="lead">{L("ใช้วางแผนล่วงหน้าว่าควรจองล็อตช่วงไหน ช่วงพีคคือช่วงที่ผลผลิตมากที่สุดและราคาดีที่สุด — สี่ชนิดแรกคือสินค้าที่เราส่งออกเอง ที่เหลือใส่ไว้ให้เห็นภาพรวมของปฏิทินผลไม้ไทย",
                        "Use it to plan when to book. The peak band is when volume is highest and the price is best — the first four are what we export ourselves; the rest are here to show the shape of the Thai fruit year.")}</p>
    </div>
    <div class="rv">
      <p class="cal-hint">{L("เลื่อนตารางไปทางขวาเพื่อดูเดือนถัดไป", "Swipe the table sideways for the later months")} →</p>
      {season_table()}
      <div class="cal-legend">
        <span><i class="k-peak"></i>{L("ช่วงพีค ผลผลิตมากที่สุด", "Peak — highest volume")}</span>
        <span><i class="k-on"></i>{L("มีผลผลิต", "In season")}</span>
        <span class="k-now-wrap"><i class="k-now"></i>{L("เดือนปัจจุบัน", "This month")}</span>
        <span class="cal-note">{L("ตัวเลขเป็นค่าเฉลี่ยทั้งประเทศ ภาคเหนือกับภาคตะวันออกคลาดกันราวสองถึงสามสัปดาห์ · ลำไยและมะม่วงมีผลผลิตนอกฤดูจากสวนราดสารด้วย",
                                  "National averages. The North and the East run two to three weeks apart, and longan and mango also crop off-season from induced orchards.")}</span>
      </div>
    </div>
  </div>
</section>

"""

# ============================================================ HOME
home = f"""<header class="hero">
  <div class="hero-media" id="heroMedia">
    <img class="hero-slide on" src="{IMG['orchard']}" alt="Longan orchard in Northern Thailand at sunrise" fetchpriority="high">
    <img class="hero-slide" data-src="images/fresh-longan-on-the-branch.webp" alt="Fresh Thai longan hanging on the branch" decoding="async">
    <img class="hero-slide" data-src="images/longan-export-crates.webp" alt="Hand-graded longan in export crates" decoding="async">
    <video class="hero-vid" muted playsinline preload="none" poster="{IMG['orchard']}" data-src="{VID['orchard']}" data-src-small="{VID['mobile']}"></video>
    <video class="hero-vid" muted playsinline preload="none" data-src="{VID['shed']}"></video>
    <video class="hero-vid" muted playsinline preload="none" data-src="{VID['line']}"></video>
  </div>
  <div class="hero-in">
    <div class="eyebrow">Alpha Fresh Co., Ltd. — Lamphun, Thailand</div>
    <h1>{L("ลำไยไทยคัดคุณภาพ<span class='accent'>จากสวนถึงตลาดของคุณ</span>",
           "Premium Thai Longan<span class='accent script'>from the orchard to your market</span>")}</h1>
    <p>{L("โรงคัดลำไยขนาดเล็กที่ดูแลเองทุกขั้นตอน คัดด้วยมือ เก็บความเย็นทันที และส่งออกพร้อมเอกสารครบ — ทุเรียน มังคุด ลิ้นจี่ ตามฤดูกาล",
          "A small, hands-on packing house in Northern Thailand. Hand-graded, chilled within hours, and shipped with complete export paperwork — plus durian, mangosteen and lychee in season.")}</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="contact.html"><span class="lbl-lg">{L("ขอใบเสนอราคา", "Request a quotation")}</span><span class="lbl-sm">{L("ขอราคา", "Get a quote")}</span> {ARROW}</a>
      <a class="btn btn-ghost" href="products.html"><span class="lbl-lg">{L("ดูสินค้าและสเปก", "Products &amp; specifications")}</span><span class="lbl-sm">{L("ดูสินค้า", "Products")}</span></a>
    </div>
  </div>
  <div class="hero-dots" id="dots"></div>
</header>

{STATS}

<section>
  <div class="wrap split rv">
    <div>
      <div class="tag">{L("เกี่ยวกับเรา", "About us")}</div>
      <h2>{L("เราทำ “นำเข้า” มาก่อน จึงรู้ว่าปลายทางต้องการอะไร", "We started as importers — so we know what the buyer's end needs")}</h2>
      <p>{L("บริษัท อัลฟ่า เฟรช จำกัด เริ่มจากธุรกิจนำเข้าผลไม้ เรามีห้องเย็น รถห้องเย็น และทีมที่คุ้นเคยกับพิธีการศุลกากรอยู่แล้ว วันนี้เราทำย้อนทาง — ใช้ระบบเดิมทั้งชุดในการส่งออกผลไม้ไทย โดยเริ่มจากสิ่งที่เราถนัดที่สุดคือลำไย",
            "Alpha Fresh began as a fruit importer. We already run the cold room, the refrigerated truck and a team fluent in customs clearance. Today we run it in reverse — the same chain, pointed outward — starting with what we know best: longan.")}</p>
      <div class="cta-row" style="margin-top:22px">
        <a class="btn btn-outline" href="about.html">{L("อ่านเรื่องของเรา", "Read our story")} {ARROW}</a>
      </div>
    </div>
    <div class="split-media">
      <img src="{IMG['shedfront']}" alt="Alpha Fresh longan packing house in Lamphun, Thailand" loading="lazy">
      <div class="cap">{L("โรงคัดลำไยของเรา จ.ลำพูน", "Our longan collection &amp; packing shed, Lamphun")}</div>
    </div>
  </div>
</section>

<section class="soft">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("สินค้า", "What we ship")}</div>
      <h2>{L("ลำไยเป็นตัวหลัก และผลไม้ไทยอีก 3 ชนิดตามฤดู", "Longan first, and three more Thai fruits in season")}</h2>
    </div>
    <div class="grid-4 rv g2m">
      <a class="card" href="products.html#longan"><img src="images/graded-longan-in-crates.webp" alt="Fresh Thai longan for export" loading="lazy">
        <div class="card-b"><h3>{L("ลำไยสด", "Fresh longan")}</h3>
          <p>{L("อีดอ · ดอ · เบี้ยวเขียว · เกรด AA–C · ก.ค.–ก.ย. และนอกฤดู", "E-Daw · Daw · Biew Kiew · grades AA–C · Jul–Sep plus off-season")}</p>
          <span class="more">{L("ดูสเปกเต็ม", "Full specification")} {ARROW}</span></div></a>
      <a class="card" href="products.html#durian"><img src="{IMG['durian']}" alt="Fresh Thai durian for export" loading="lazy">
        <div class="card-b"><h3>{L("ทุเรียนหมอนทอง", "Monthong durian")}</h3>
          <p>{L("ตัดแก่ 80–85% · เม.ย.–ส.ค.", "80–85% maturity · Apr–Aug")}</p>
          <span class="more">{L("ดูรายละเอียด", "See details")} {ARROW}</span></div></a>
      <a class="card" href="products.html#mangosteen"><img src="{IMG['mangosteen']}" alt="Fresh Thai mangosteen for export" loading="lazy">
        <div class="card-b"><h3>{L("มังคุด", "Mangosteen")}</h3>
          <p>{L("ผิวมัน ขั้วเขียวสด · พ.ค.–ก.ย.", "Glossy rind, fresh calyx · May–Sep")}</p>
          <span class="more">{L("ดูรายละเอียด", "See details")} {ARROW}</span></div></a>
      <a class="card" href="products.html#lychee"><img src="{IMG['lychee']}" alt="Fresh Thai lychee for export" loading="lazy">
        <div class="card-b"><h3>{L("ลิ้นจี่", "Lychee")}</h3>
          <p>{L("ฮงฮวย · จักรพรรดิ · เม.ย.–มิ.ย.", "Hong Huay · Chakrapad · Apr–Jun")}</p>
          <span class="more">{L("ดูรายละเอียด", "See details")} {ARROW}</span></div></a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("วิธีทำงาน", "How we work")}</div>
      <h2>{L("5 ขั้นตอน จากคำถามแรกถึงตู้ออกจากท่า", "Five steps, from first enquiry to departure")}</h2>
    </div>
    <div class="steps rv">
      <div class="step"><div class="n">1</div><h3>{L("สอบถาม", "Enquiry")}</h3>
        <p>{L("แจ้งชนิด เกรด ปริมาณ ปลายทางและ Incoterm", "Fruit, grade, volume, destination and Incoterm.")}</p></div>
      <div class="step"><div class="n">2</div><h3>{L("จัดหา", "Sourcing")}</h3>
        <p>{L("จองผลผลิตกับสวน GAP ล่วงหน้า ล็อกราคาและวันตัด", "Harvest booked with GAP orchards, price and date fixed.")}</p></div>
      <div class="step"><div class="n">3</div><h3>{L("คัดและแพ็ค", "Grading")}</h3>
        <p>{L("คัดด้วยมือ ชั่ง ปิดกล่อง ถ่ายรูปล็อตให้ดูก่อนโหลด", "Hand-graded, weighed, sealed and photographed for approval.")}</p></div>
      <div class="step"><div class="n">4</div><h3>{L("เอกสาร", "Documents")}</h3>
        <p>{L("Phyto, C/O, Invoice, Packing List, B/L หรือ AWB", "Phyto, C/O, invoice, packing list, B/L or AWB.")}</p></div>
      <div class="step"><div class="n">5</div><h3>{L("ส่งออก", "Shipping")}</h3>
        <p>{L("โหลดตู้ Reefer หรือส่งทางอากาศ พร้อมข้อมูลติดตาม", "Reefer container or air freight, with tracking sent.")}</p></div>
    </div>
    <div class="cta-row rv" style="margin-top:36px">
      <a class="btn btn-outline" href="quality.html">{L("ดูมาตรฐานคุณภาพและเงื่อนไขการส่งออก", "Quality standards and export terms")} {ARROW}</a>
    </div>
  </div>
</section>

{BAND}"""

# ============================================================ ABOUT
about = f"""{phead("เกี่ยวกับเรา", "About", "จากผู้นำเข้า สู่ผู้ส่งออก", "From importer to exporter",
        "เราไม่ได้เริ่มจากศูนย์ — ห้องเย็น รถห้องเย็น และความรู้เรื่องเอกสารพิธีการ เรามีอยู่แล้วจากฝั่งนำเข้า สิ่งที่เพิ่มเข้ามาคือโรงคัดของเราเองที่ลำพูน",
        "We did not start from nothing. The cold room, the refrigerated truck and the customs paperwork were already ours from the import side. What we added is our own packing shed in Lamphun.",
        IMG['orchard'])}

<section>
  <div class="wrap split rv">
    <div>
      <div class="tag">{L("จุดเริ่มต้น", "Where we come from")}</div>
      <h2>{L("ธุรกิจเล็ก ที่ทำเองเห็นเองทุกขั้น", "A small business that still touches every crate")}</h2>
      <p>{L("อัลฟ่า เฟรช เริ่มจากการนำเข้าผลไม้เข้ามาขายในประเทศ งานนั้นสอนเราสองเรื่อง — ผลไม้เสียตรงไหนของห่วงโซ่ และผู้ซื้อปลายทางหงุดหงิดกับอะไร เราเลยรู้ว่าเวลาส่งออก อะไรคือสิ่งที่ต้องไม่พลาด",
            "Alpha Fresh began by importing fruit for the domestic market. That work taught us two things — where in the chain fruit actually spoils, and what buyers get frustrated about. So we know what must not slip when the fruit goes the other way.")}</p>
      <p>{L("ทุกวันนี้เราเป็นโรงคัดขนาดเล็ก ไม่ใช่โรงงานใหญ่ ล็อตของเราไม่มหาศาล แต่นั่นแหละคือเหตุผลที่เรายังตรวจได้ทีละตะกร้า ไม่ใช่สุ่มตรวจ",
            "Today we are a small sorting shed, not a large factory. Our lots are modest — which is exactly why we can still check crate by crate instead of sampling.")}</p>
      <ul class="ticks">
        <li>{TICK}<span>{L("<b>Cold chain พร้อมใช้</b> — ห้องเย็นและรถห้องเย็นของเราเอง ไม่ต้องรอคิวใคร", "<b>Cold chain already in place</b> — our own cold room and refrigerated truck, no queueing for third parties.")}</span></li>
        <li>{TICK}<span>{L("<b>เอกสารเราทำเอง</b> — Phyto, C/O, Packing List, Invoice จบในทีมเดียว", "<b>Paperwork in-house</b> — phytosanitary certificate, C/O, packing list and invoice handled by one team.")}</span></li>
        <li>{TICK}<span>{L("<b>เล็กแต่ตรวจได้ทุกลูก</b> — เราคัดด้วยมือ ล็อตไม่ใหญ่ จึงคุมคุณภาพได้จริง", "<b>Small enough to check every crate</b> — hand-graded in modest lots, so quality control is real, not a claim.")}</span></li>
        <li>{TICK}<span>{L("<b>คุยกับสวนโดยตรง</b> — ไม่ผ่านคนกลางหลายชั้น ราคาและวันตัดจึงตกลงล่วงหน้าได้", "<b>Direct with the orchards</b> — no chain of middlemen, so price and picking date can be agreed in advance.")}</span></li>
      </ul>
    </div>
    <div class="split-media">
      <img src="{IMG['shedfront']}" alt="Alpha Fresh longan packing house in Lamphun, Thailand" loading="lazy">
      <div class="cap">{L("โรงคัดลำไยของเรา จ.ลำพูน", "Our longan collection &amp; packing shed, Lamphun")}</div>
    </div>
  </div>
</section>

<section class="soft">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("สิ่งที่เราดูแลเอง", "What we handle ourselves")}</div>
      <h2>{L("สามอย่างที่เราไม่ยกให้ใครทำแทน", "Three things we do not hand to anyone else")}</h2>
    </div>
    <div class="grid-3 rv">
      <div class="card"><img src="{IMG['sorting']}" alt="Hand-grading longan at the packing house" loading="lazy">
        <div class="card-b"><h3>{L("การคัดเกรด", "Grading")}</h3>
          <p>{L("คัดด้วยมือทุกล็อต แยกช่อที่ผลร่วงหรือผิวช้ำออกก่อนลงกล่อง ไม่ใช้สายพานคัดอัตโนมัติ เพราะล็อตเราไม่ใหญ่พอที่จะคุ้ม และมือคนแม่นกว่าในงานขนาดนี้",
                "Every lot is graded by hand — loose or bruised clusters pulled before boxing. No automated grading line: our lots are not large enough to justify one, and at this scale hands are more accurate.")}</p></div></div>
      <div class="card"><img src="{IMG['cold']}" alt="Cold room holding fresh longan before shipment" loading="lazy">
        <div class="card-b"><h3>{L("ห้องเย็น", "The cold room")}</h3>
          <p>{L("ผลไม้เข้าห้องเย็นในวันที่ตัด ไม่ค้างคืนกลางแจ้ง อุณหภูมิถูกบันทึกไว้ และถ้าผู้ซื้อขอ เราใส่ data logger ไปในตู้ให้ดูย้อนหลังได้",
                "Fruit goes into the cold room on picking day — never left outside overnight. Temperatures are logged, and if the buyer asks we put a data logger in the container.")}</p></div></div>
      <div class="card"><img src="{IMG['loading']}" alt="Loading a refrigerated container for export" loading="lazy">
        <div class="card-b"><h3>{L("เอกสารและการโหลด", "Documents and loading")}</h3>
          <p>{L("ทีมเดิมที่เคยเคลียร์ของขาเข้าเป็นคนทำเอกสารขาออก เราอยู่ตอนโหลดตู้ทุกครั้ง และส่งรูปล็อตให้ผู้ซื้อดูก่อนปิดตู้",
                "The same team that used to clear inbound shipments prepares the outbound papers. We are present at every loading, and send lot photos to the buyer before the container is sealed.")}</p></div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split flip rv">
    <div class="split-media">
      <img src="images/longan-orchard-northern-thailand.webp" alt="GAP-certified longan orchard in Lamphun" loading="lazy">
      <div class="cap">{L("สวนพันธมิตรในลำพูน", "A partner orchard in Lamphun")}</div>
    </div>
    <div>
      <div class="tag">{L("เครือข่ายสวน", "Our orchards")}</div>
      <h2>{L("20 กว่าสวน ที่เรารู้จักเจ้าของทุกคน", "Twenty-odd orchards, and we know every owner")}</h2>
      <p>{L("เราไม่ได้ซื้อผ่านตลาดกลาง แต่จองผลผลิตกับสวนที่ผ่านมาตรฐาน GAP ล่วงหน้าเป็นฤดู ทำให้ตกลงราคาและวันตัดได้ก่อน และรู้ว่าลำไยแต่ละล็อตมาจากแปลงไหน",
            "We do not buy through the central market. We book the harvest a season ahead with GAP-certified orchards, which lets us fix price and picking date in advance — and know which plot each lot came from.")}</p>
      <p>{L("ในฤดูเราใช้สวนในลำพูน เชียงใหม่ และเชียงราย ส่วนนอกฤดูรับจากสวนราดสารในจันทบุรี",
            "In season we draw from Lamphun, Chiang Mai and Chiang Rai; off-season fruit comes from induced orchards in Chanthaburi.")}</p>
      <div class="cta-row" style="margin-top:22px">
        <a class="btn btn-outline" href="quality.html#standards">{L("ดูมาตรฐานที่เราใช้", "The standards we work to")} {ARROW}</a>
      </div>
    </div>
  </div>
</section>

{BAND}"""

# ============================================================ PRODUCTS
products = f"""{phead("สินค้า", "Products", "ลำไย และผลไม้ไทยตามฤดูกาล", "Longan, and Thai fruit in season",
        "ลำไยคือสินค้าหลักของเรา — มีสเปกเต็มด้านล่าง ส่วนทุเรียน มังคุด และลิ้นจี่ รับออเดอร์ตามฤดู ผ่านเครือข่ายล้งที่ทำงานด้วยกันมานาน",
        "Longan is our flagship — the full specification is below. Durian, mangosteen and lychee are taken to order in season, through packing houses we have worked with for years.",
        IMG['longanpack'])}

<section id="longan">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("สินค้าหลัก", "Flagship product")}</div>
      <h2>{L("ลำไยสด — Fresh Longan", "Fresh Longan (Dimocarpus longan)")}</h2>
      <p class="lead">{L("ลำไยจากสวนในลำพูน เชียงใหม่ และจันทบุรี คัดด้วยมือ ตัดขั้ว ล้าง รมซัลเฟอร์ตามข้อกำหนดปลายทาง แล้วเข้าห้องเย็นภายในวันเดียวกัน",
                        "Longan from partner orchards in Lamphun, Chiang Mai and Chanthaburi. Hand-picked, de-stemmed, washed, SO₂-treated to destination requirement, and into the cold room the same day.")}</p>
    </div>
    <div class="figs rv" style="margin-bottom:36px">
      <figure><img src="images/fresh-longan-on-the-branch.webp" alt="A cluster of fresh Thai longan on the tree" loading="lazy"></figure>
      <figure><img src="images/graded-longan-in-crates.webp" alt="Graded longan packed into export crates" loading="lazy"></figure>
    </div>
    <div class="rv">
    <table class="spec">
      <tr><th>{L("สายพันธุ์", "Varieties")}</th>
        <td>{L("อีดอ (E-Daw) — พันธุ์หลักเพื่อการส่งออก · ดอ (Daw) · เบี้ยวเขียว (Biew Kiew) — เนื้อหนา หวานน้อย เหมาะตลาดพรีเมียม",
               "E-Daw (main export variety) · Daw · Biew Kiew — thicker flesh, less sugary, suited to premium markets")}</td></tr>
      <tr><th>{L("แหล่งปลูก", "Growing areas")}</th>
        <td>{L("ลำพูน · เชียงใหม่ · เชียงราย (ในฤดู) และจันทบุรี (นอกฤดู)", "Lamphun · Chiang Mai · Chiang Rai (in season); Chanthaburi (off-season)")}</td></tr>
      <tr><th>{L("ฤดูกาล", "Season")}</th>
        <td>{L("ในฤดู ก.ค.–ก.ย. (พีค ส.ค.) · นอกฤดู พ.ย.–ก.พ. จากสวนราดสาร", "In season Jul–Sep (peak August) · off-season Nov–Feb from induced orchards")}</td></tr>
      <tr><th>{L("เกรด", "Grades")}</th>
        <td>{L("AA · A · B · C คัดตามขนาดผลและความสมบูรณ์ของช่อ", "AA · A · B · C, graded by fruit diameter and cluster condition")}</td></tr>
      <tr><th>{L("รูปแบบบรรจุ", "Packing")}</th>
        <td>{L("ตะกร้าพลาสติก / กล่องกระดาษ 5 กก. และ 10 กก. บุกระดาษซับ + แผ่นดูดความชื้น · พิมพ์แบรนด์ผู้ซื้อได้",
               "Plastic crates or cartons of 5 kg and 10 kg, lined with absorbent paper and a moisture pad · buyer's own branding available")}</td></tr>
      <tr><th>{L("อุณหภูมิเก็บรักษา", "Storage temperature")}</th>
        <td>{L("2–5 °C ความชื้นสัมพัทธ์ 90–95%", "2–5 °C at 90–95% relative humidity")}</td></tr>
      <tr><th>{L("อายุการเก็บ", "Shelf life")}</th>
        <td>{L("21–30 วัน เมื่อรักษา cold chain ต่อเนื่อง", "21–30 days with an unbroken cold chain")}</td></tr>
      <tr><th>{L("ปริมาณต่อตู้", "Container load")}</th>
        <td>{L("ประมาณ 2,000 กล่อง (10 กก.) ต่อตู้ 40 ฟุต Reefer ≈ 20 ตัน", "Approx. 2,000 cartons (10 kg) per 40 ft reefer ≈ 20 tonnes")}</td></tr>
      <tr><th>MOQ</th>
        <td>{L("ทางเรือ 1 ตู้ 40 ฟุต · ทางอากาศ 500 กก. (ล็อตทดลองคุยได้)", "Sea: one 40 ft container · Air: 500 kg (trial lots negotiable)")}</td></tr>
    </table>
    </div>
    <h3 class="rv" style="margin:34px 0 16px">{L("เกรดลำไย", "Longan grades")}</h3>
    <div class="grid-4 rv g2m">
      <div class="grade"><b>AA</b><small>{L("ผล 26 มม.ขึ้นไป", "26 mm and above")}</small>
        <p>{L("ช่อสมบูรณ์ ผิวสม่ำเสมอ สำหรับตลาดพรีเมียมและของฝาก", "Full clusters, even skin. Premium retail and gift markets.")}</p></div>
      <div class="grade"><b>A</b><small>{L("ผล 24–26 มม.", "24–26 mm")}</small>
        <p>{L("เกรดขายดีที่สุด สมดุลระหว่างขนาดและราคา", "Our best-selling grade — balance of size and price.")}</p></div>
      <div class="grade"><b>B</b><small>{L("ผล 22–24 มม.", "22–24 mm")}</small>
        <p>{L("สำหรับค้าส่งและตลาดสด ปริมาณมาก", "Wholesale and wet-market volume.")}</p></div>
      <div class="grade"><b>C</b><small>{L("ต่ำกว่า 22 มม.", "Below 22 mm")}</small>
        <p>{L("สำหรับแปรรูป อบแห้ง และบรรจุกระป๋อง", "Processing, drying and canning.")}</p></div>
    </div>
  </div>
</section>

<section class="soft">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("สินค้าอื่น", "Other fruits")}</div>
      <h2>{L("ผลไม้ไทยตามฤดูกาล", "Seasonal Thai fruits")}</h2>
    </div>
    <div class="grid-3 rv">
      <div class="card" id="durian"><img src="{IMG['durian']}" alt="Monthong durian for export from Thailand" loading="lazy">
        <div class="card-b"><h3>{L("ทุเรียนหมอนทอง", "Monthong Durian")}</h3>
          <p>{L("ตัดแก่ 80–85% วัดเปอร์เซ็นต์น้ำหนักแห้งทุกล็อต ก่อนบรรจุห่อตาข่ายโฟมกันกระแทก", "Harvested at 80–85% maturity with dry-matter testing on every lot, then foam-netted against knocks.")}</p>
          <div class="meta">
            <div><span>{L("ฤดูกาล", "Season")}</span><span>{L("เม.ย.–ส.ค.", "Apr–Aug")}</span></div>
            <div><span>{L("แพ็ค", "Packing")}</span><span>{L("กล่อง 15–18 กก.", "15–18 kg carton")}</span></div>
            <div><span>{L("อุณหภูมิ", "Temp")}</span><span>13–15 °C</span></div>
          </div></div></div>
      <div class="card" id="mangosteen"><img src="{IMG['mangosteen']}" alt="Fresh Thai mangosteen for export" loading="lazy">
        <div class="card-b"><h3>{L("มังคุด", "Mangosteen")}</h3>
          <p>{L("คัดผิวมัน ขั้วเขียวสด ไม่มียางไหล และไม่มีอาการเนื้อแก้วจากการกระแทก", "Selected for glossy rind and a fresh green calyx, with no gamboge staining or impact damage.")}</p>
          <div class="meta">
            <div><span>{L("ฤดูกาล", "Season")}</span><span>{L("พ.ค.–ก.ย.", "May–Sep")}</span></div>
            <div><span>{L("แพ็ค", "Packing")}</span><span>{L("กล่อง 5 / 10 กก.", "5 / 10 kg carton")}</span></div>
            <div><span>{L("อุณหภูมิ", "Temp")}</span><span>8–12 °C</span></div>
          </div></div></div>
      <div class="card" id="lychee"><img src="{IMG['lychee']}" alt="Fresh Thai lychee for export" loading="lazy">
        <div class="card-b"><h3>{L("ลิ้นจี่", "Lychee")}</h3>
          <p>{L("พันธุ์ฮงฮวยและจักรพรรดิ ตัดเช้า แช่เย็นทันที เพราะลิ้นจี่เปลี่ยนสีเร็วที่สุดในบรรดาผลไม้ที่เราส่ง", "Hong Huay and Chakrapad, picked at dawn and chilled immediately — lychee browns faster than anything else we ship.")}</p>
          <div class="meta">
            <div><span>{L("ฤดูกาล", "Season")}</span><span>{L("เม.ย.–มิ.ย.", "Apr–Jun")}</span></div>
            <div><span>{L("แพ็ค", "Packing")}</span><span>{L("กล่อง 2 / 5 กก. + เจลเย็น", "2 / 5 kg carton, gel ice")}</span></div>
            <div><span>{L("อุณหภูมิ", "Temp")}</span><span>2–4 °C</span></div>
          </div></div></div>
    </div>
  </div>
</section>

{SEASON_SECTION}{BAND}"""

# ============================================================ QUALITY
quality = f"""{phead("คุณภาพและการส่งออก", "Quality &amp; Export", "ตรวจได้ ตามได้ ส่งถึงในสภาพเดิม", "Checked, traceable, and delivered in the condition it left",
        "หน้านี้รวมทุกอย่างที่ผู้ซื้อมักถามก่อนสั่งครั้งแรก — ขั้นตอนการทำงาน มาตรฐานที่เราใช้ การตรวจสารตกค้าง ห่วงโซ่ความเย็น เงื่อนไขการส่งมอบและการชำระเงิน",
        "Everything a buyer usually asks before a first order — how an order runs, the standards we work to, residue testing, the cold chain, and our delivery and payment terms.",
        IMG['qc'])}

<section id="process">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("ขั้นตอนการทำงาน", "How an order runs")}</div>
      <h2>{L("5 ขั้นตอน จากคำถามแรกถึงตู้ออกจากท่า", "Five steps, from first enquiry to departure")}</h2>
    </div>
    <div class="steps rv">
      <div class="step"><div class="n">1</div><h3>{L("สอบถาม", "Enquiry")}</h3>
        <p>{L("แจ้งชนิดผลไม้ เกรด ปริมาณ ปลายทางและ Incoterm เราตอบใบเสนอราคาภายใน 2 วันทำการ", "Tell us the fruit, grade, volume, destination and Incoterm. Quotation within two working days.")}</p></div>
      <div class="step"><div class="n">2</div><h3>{L("จัดหา", "Sourcing")}</h3>
        <p>{L("จองผลผลิตกับสวน GAP ล่วงหน้า ล็อกราคาและวันตัด", "We book the harvest with GAP orchards ahead of time, locking price and picking date.")}</p></div>
      <div class="step"><div class="n">3</div><h3>{L("คัดและแพ็ค", "Grading &amp; packing")}</h3>
        <p>{L("คัดด้วยมือตามเกรดที่ตกลง ชั่งน้ำหนัก ปิดกล่อง ถ่ายรูปล็อตส่งให้ดูก่อนโหลด", "Hand-graded to the agreed spec, weighed, sealed — and photographed for your approval before loading.")}</p></div>
      <div class="step"><div class="n">4</div><h3>{L("เอกสาร", "Documentation")}</h3>
        <p>{L("ใบรับรองสุขอนามัยพืช (Phyto), C/O, Invoice, Packing List และ B/L หรือ AWB", "Phytosanitary certificate, C/O, invoice, packing list and B/L or AWB.")}</p></div>
      <div class="step"><div class="n">5</div><h3>{L("ส่งออก", "Shipping")}</h3>
        <p>{L("โหลดตู้ Reefer หรือส่งทางอากาศ พร้อมส่งข้อมูลติดตามให้ทุกครั้ง", "Reefer container or air freight, with tracking details sent every time.")}</p></div>
    </div>
  </div>
</section>

<section class="soft" id="standards">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("มาตรฐานและการตรวจสอบ", "Standards &amp; testing")}</div>
      <h2>{L("สิ่งที่เราการันตีได้ และสิ่งที่เรายังไม่การันตี", "What we can guarantee — and what we do not claim")}</h2>
    </div>
    <div class="grid-3 rv">
      <div class="card"><img src="{IMG['sorting']}" alt="Hand-grading longan at the packing house" loading="lazy">
        <div class="card-b"><h3>{L("มาตรฐานการผลิต", "Production standards")}</h3>
          <p>{L("สวนพันธมิตรผ่าน GAP โรงคัดทำตามแนวทาง GMP และ HACCP มีบันทึกล็อตย้อนกลับถึงสวนได้", "Partner orchards are GAP-certified; the packing shed follows GMP and HACCP practice, with lot records traceable back to the orchard.")}</p>
          <div class="chips"><span class="chip">{G("GAP")}</span><span class="chip">{G("GMP")}</span><span class="chip">{G("HACCP")}</span><span class="chip gold">Traceable lot code</span></div></div></div>
      <div class="card"><img src="{IMG['qc']}" alt="Quality inspection of export fruit" loading="lazy">
        <div class="card-b"><h3>{L("สารตกค้างและเอกสาร", "Residues &amp; certificates")}</h3>
          <p>{L("ส่งตรวจสารตกค้างตาม MRL ของปลายทาง — EU, จีน (GACC), ญี่ปุ่น — พร้อมใบรับรองสุขอนามัยพืชทุกชิปเมนต์", "Residue testing against destination MRLs — EU, China (GACC) and Japan — with a phytosanitary certificate on every shipment.")}</p>
          <div class="chips"><span class="chip">EU {G("MRL")}</span><span class="chip">{G("GACC")}</span><span class="chip">Japan MHLW</span><span class="chip gold">{G("Phytosanitary")}</span></div></div></div>
      <div class="card"><img src="{IMG['cold']}" alt="Cold room holding fresh longan before shipment" loading="lazy">
        <div class="card-b"><h3>{L("ห่วงโซ่ความเย็น", "Cold chain")}</h3>
          <p>{L("เข้าห้องเย็นภายในวันที่ตัด บันทึกอุณหภูมิตลอดทาง ใส่ data logger ในตู้ตามคำขอ", "Into the cold room on picking day, temperature logged throughout, with a data logger placed in the container on request.")}</p>
          <div class="chips"><span class="chip">2–5 °C</span><span class="chip">RH 90–95%</span><span class="chip gold">Data logger</span></div></div></div>
    </div>
    <div class="tbox rv" style="margin-top:26px;border-left:3px solid var(--gold)">
      <h3>{L("พูดกันตรง ๆ", "Plainly stated")}</h3>
      <p style="margin:6px 0 0;font-size:14.5px">{L("เราเป็นธุรกิจเล็ก ไม่ได้มีไลน์ผลิตอัตโนมัติหรือห้องแล็บของตัวเอง การตรวจสารตกค้างส่งแล็บภายนอก และปริมาณที่รับได้ต่อสัปดาห์มีเพดาน ถ้าออเดอร์ใหญ่เกินกำลัง เราจะบอกตรง ๆ ตั้งแต่ต้นแทนที่จะรับไว้ก่อน",
            "We are a small business. There is no automated line and no in-house laboratory here — residue testing goes to an external lab, and there is a ceiling on what we can handle per week. If an order is beyond us, we will say so up front rather than take it and hope.")}</p>
    </div>
  </div>
</section>

<section id="terms">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("เงื่อนไข", "Terms")}</div>
      <h2>{L("การส่งมอบและการชำระเงิน", "Delivery and payment")}</h2>
    </div>
    <div class="grid-2 rv">
      <div class="tbox">
        <h3>{L("เงื่อนไขการส่งมอบ", "Delivery terms")} ({G("Incoterms 2020")})</h3>
        <ul>
          <li><b>{G("EXW")}</b> — {L("รับที่โรงคัด จ.ลำพูน", "collect at our shed in Lamphun")}</li>
          <li><b>{G("FOB")}</b> — {L("ท่าเรือแหลมฉบัง หรือ สนามบินสุวรรณภูมิ / เชียงใหม่", "Laem Chabang port, or Suvarnabhumi / Chiang Mai airport")}</li>
          <li><b>{G("CFR")} / {G("CIF")}</b> — {L("ถึงท่าปลายทางที่ตกลง", "to the agreed destination port")}</li>
          <li>{L("ขนส่ง: ตู้ Reefer 40 ฟุต หรือ air freight สำหรับล็อตเล็กและลิ้นจี่", "Transport: 40 ft reefer container, or air freight for small lots and lychee")}</li>
        </ul>
      </div>
      <div class="tbox">
        <h3>{L("เงื่อนไขการชำระเงิน", "Payment terms")}</h3>
        <ul>
          <li>{L("<b>ออเดอร์แรก</b> — T/T มัดจำ 30% ส่วนที่เหลือก่อนออกเอกสาร B/L", "<b>First order</b> — 30% T/T deposit, balance before B/L release")}</li>
          <li>{L("<b>ลูกค้าประจำ</b> — L/C at sight หรือ T/T 30 วัน พิจารณาเป็นรายกรณี", "<b>Repeat buyers</b> — L/C at sight or 30-day T/T, case by case")}</li>
          <li>{L("สกุลเงิน USD หรือ THB · ใบเสนอราคายืน 7 วัน (ราคาลำไยขึ้นลงตามหน้าสวน)", "Quoted in USD or THB · quotations valid 7 days (longan farm-gate prices move weekly)")}</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="soft" id="markets">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="tag">{L("ตลาดเป้าหมาย", "Target markets")}</div>
      <h2>{L("ปลายทางที่เราเตรียมพร้อมแล้ว", "Where we are ready to ship")}</h2>
    </div>
    <div class="grid-4 rv g2m">
      <div class="mkc">{flags("cn")}<b>{L("จีน", "China")}</b><span>{L("ลำไย ทุเรียน มังคุด · ผ่านด่านโหย่วอี้กวน / ท่าเรือ · ต้องมีทะเบียน GACC", "Longan, durian, mangosteen · via Youyiguan or sea port · GACC registration required")}</span></div>
      <div class="mkc">{flags("hk","sg")}<b>{L("ฮ่องกง / สิงคโปร์", "Hong Kong / Singapore")}</b><span>{L("ล็อตเล็ก ส่งบ่อย เหมาะกับ air freight", "Small, frequent lots — well suited to air freight")}</span></div>
      <div class="mkc">{flags("nl","fr")}<b>{L("ยุโรป", "Europe")}</b><span>{L("เนเธอร์แลนด์ ฝรั่งเศส · เข้มเรื่อง MRL และ SO₂", "Netherlands, France · strict on MRL and SO₂ limits")}</span></div>
      <div class="mkc">{flags("ae")}<b>{L("ตะวันออกกลาง", "Middle East")}</b><span>{L("ดูไบ · ตลาดของฝากและซูเปอร์พรีเมียม", "Dubai · gifting and premium supermarket channels")}</span></div>
    </div>
  </div>
</section>

{BAND}"""

# ============================================================ CONTACT
contact = f"""{phead("ติดต่อ", "Contact", "ขอใบเสนอราคา", "Request a quotation",
        "บอกเราสั้น ๆ ว่าต้องการผลไม้อะไร ปริมาณเท่าไร ส่งไปที่ไหน แล้วเราจะตอบกลับพร้อมราคาและกำหนดตัดภายใน 2 วันทำการ",
        "Tell us the fruit, the volume and the destination. You will get a price and a picking schedule back within two working days.",
        IMG['hands'])}

<section>
  <div class="wrap contact rv">
    <div>
      <div class="tag">{L("ช่องทางติดต่อ", "Reach us")}</div>
      <h2>{L("คุยกับคนที่ทำงานจริง", "You will be talking to the people who do the work")}</h2>
      <p>{L("เราตอบเองไม่ผ่านคอลเซ็นเตอร์ ถ้ามีคำถามเรื่องเกรด ฤดูกาล หรือข้อกำหนดปลายทาง ถามมาได้เลยแม้ยังไม่พร้อมสั่ง",
            "There is no call centre here. If you have questions about grades, seasons or destination requirements, ask — even if you are not ready to order.")}</p>
      <div class="ci">
        <div><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#3f6b3a" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>
          <span><b><a href="mailto:alphafreshthailand@gmail.com" style="text-decoration:none">alphafreshthailand@gmail.com</a></b></span></div>
        <div><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#3f6b3a" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>
          <span><b><a href="tel:+66898949491" style="text-decoration:none">+66 89 894 9491</a></b> · {L("LINE และ WeChat เบอร์เดียวกัน", "LINE and WeChat on the same number")}</span></div>
        <div><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#3f6b3a" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <span>{L("โรงคัดลำไย อ.เมือง จ.ลำพูน · สำนักงาน กรุงเทพฯ", "Packing shed: Mueang District, Lamphun · Office: Bangkok")}</span></div>
        <div><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#3f6b3a" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
          <span>{L("จันทร์–เสาร์ 08:00–17:00 (เวลาไทย) · ช่วงฤดูลำไยเราอยู่ที่โรงคัดทั้งวัน", "Mon–Sat 08:00–17:00 Thailand time · during longan season we are at the shed all day")}</span></div>
      </div>
    </div>
    <form onsubmit="event.preventDefault();this.querySelector('.note').innerHTML='<b style=color:#3f6b3a>'+(document.documentElement.dataset.lang==='th'?'ขอบคุณครับ — เราจะติดต่อกลับภายใน 2 วันทำการ':'Thank you — we will reply within two working days.')+'</b>';">
      <div class="f2">
        <div class="field"><label>{L("ชื่อ-นามสกุล", "Full name")}</label><input required></div>
        <div class="field"><label>{L("บริษัท", "Company")}</label><input></div>
      </div>
      <div class="f2">
        <div class="field"><label>{L("อีเมล", "Email")}</label><input type="email" required></div>
        <div class="field"><label>{L("ประเทศปลายทาง", "Destination country")}</label><input required></div>
      </div>
      <div class="f2">
        <div class="field"><label>{L("สินค้าที่สนใจ", "Product")}</label>
          <select>
            <option data-en>Fresh longan</option><option data-th>ลำไยสด</option><option data-zh>新鲜龙眼</option><option data-ar>لونجان طازج</option>
            <option data-en>Monthong durian</option><option data-th>ทุเรียนหมอนทอง</option><option data-zh>金枕榴莲</option><option data-ar>دوريان مونثونغ</option>
            <option data-en>Mangosteen</option><option data-th>มังคุด</option><option data-zh>山竹</option><option data-ar>مانجوستين</option>
            <option data-en>Lychee</option><option data-th>ลิ้นจี่</option><option data-zh>荔枝</option><option data-ar>ليتشي</option>
            <option data-en>Mixed / several</option><option data-th>หลายรายการ</option><option data-zh>多种混装</option><option data-ar>متنوّع / أكثر من صنف</option>
          </select></div>
        <div class="field"><label>{L("เงื่อนไขการส่งมอบ", "Incoterm")}</label>
          <select><option>FOB</option><option>CIF</option><option>CFR</option><option>EXW</option>
            <option data-en>Not sure yet</option><option data-th>ยังไม่แน่ใจ</option><option data-zh>尚未确定</option><option data-ar>غير محدد بعد</option></select></div>
      </div>
      <div class="field"><label>{L("ปริมาณโดยประมาณ และช่วงเวลาที่ต้องการ", "Approximate volume and timing")}</label>
        <textarea placeholder="เช่น ลำไยเกรด A 1 ตู้ 40 ฟุต ส่งเดือนสิงหาคม / e.g. one 40 ft container of Grade A longan, August"></textarea></div>
      <button class="btn btn-green" style="width:100%;justify-content:center" type="submit">{L("ส่งคำขอใบเสนอราคา", "Send quotation request")}</button>
      <p class="note">{L("เป็นฟอร์มตัวอย่างสำหรับเว็บฉบับร่าง ยังไม่ได้เชื่อมระบบส่งอีเมลจริง", "Demo form for this draft site — not yet connected to a mail service.")}</p>
    </form>
  </div>
</section>"""


page("index.html",
     "Thai Longan Exporter | Alpha Fresh, Lamphun Thailand",
     "Alpha Fresh exports hand-graded fresh longan from Lamphun, Thailand, plus durian, mangosteen and lychee in season. GAP orchards, cold chain, FOB and CIF.",
     home, solid_nav=False,
     preload=f'<link rel="preload" as="image" href="{IMG["orchard"]}" fetchpriority="high">\n',
     title_th="ผู้ส่งออกลำไยและผลไม้ไทย | บริษัท อัลฟ่า เฟรช จำกัด",
     desc_th="อัลฟ่า เฟรช ส่งออกลำไยสดคัดมือจากลำพูน พร้อมทุเรียน มังคุด ลิ้นจี่ตามฤดูกาล สวน GAP ห่วงโซ่ความเย็นครบ ส่งได้ทั้ง FOB และ CIF")
page("about.html",
     "About Alpha Fresh — Thai Fruit Importer Turned Exporter",
     "From fruit importer to exporter: our own cold room, refrigerated truck and packing shed in Lamphun, with 20+ GAP-certified longan orchards behind every lot.",
     about,
     title_th="เกี่ยวกับเรา — จากผู้นำเข้าสู่ผู้ส่งออก | อัลฟ่า เฟรช",
     desc_th="จากธุรกิจนำเข้าผลไม้ สู่การส่งออกลำไยไทย เรามีโรงคัดของตัวเองที่ลำพูน ห้องเย็น รถห้องเย็น และเครือข่ายสวน GAP กว่า 20 สวน")
page("products.html",
     "Fresh Longan Specs, Grades &amp; Thai Fruit Seasons",
     "Full longan export specification — E-Daw, Daw and Biew Kiew, grades AA to C, 5 and 10 kg packing, 21–30 day shelf life — plus a Thai fruit harvest calendar.",
     products,
     title_th="สเปกลำไยส่งออก เกรด AA–C และปฏิทินผลไม้ไทย | อัลฟ่า เฟรช",
     desc_th="สเปกลำไยส่งออกเต็มรูปแบบ สายพันธุ์อีดอ ดอ เบี้ยวเขียว เกรด AA–C บรรจุ 5 และ 10 กก. อายุเก็บ 21–30 วัน พร้อมตารางฤดูกาลผลไม้ไทย 13 ชนิด")
page("quality.html",
     "Quality, Cold Chain &amp; Export Terms | Alpha Fresh",
     "How an order runs, GAP GMP and HACCP practice, EU China and Japan residue testing, an unbroken cold chain, Incoterms 2020 and payment terms for first orders.",
     quality,
     title_th="คุณภาพ ห่วงโซ่ความเย็น และเงื่อนไขส่งออก | อัลฟ่า เฟรช",
     desc_th="ขั้นตอนการทำงาน 5 ขั้น มาตรฐาน GAP GMP HACCP ตรวจสารตกค้างตาม MRL ของ EU จีน ญี่ปุ่น ห่วงโซ่ความเย็น Incoterms 2020 และเงื่อนไขการชำระเงิน")
page("contact.html",
     "Request a Longan Export Quotation | Alpha Fresh",
     "Request a quotation for fresh Thai longan, durian, mangosteen or lychee. Price and picking schedule back within two working days. LINE and WeChat available.",
     contact,
     title_th="ขอใบเสนอราคาลำไยส่งออก | อัลฟ่า เฟรช",
     desc_th="ขอใบเสนอราคาลำไยและผลไม้ไทยส่งออก ตอบกลับพร้อมราคาและกำหนดตัดภายใน 2 วันทำการ ติดต่อได้ทาง LINE และ WeChat")
