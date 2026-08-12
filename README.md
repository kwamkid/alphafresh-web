# alphafreshthailand.com

Static marketing site for **Alpha Fresh Co., Ltd.** (บริษัท อัลฟ่า เฟรช จำกัด) —
a small longan packing shed in Lamphun exporting Thai fruit.

Plain HTML, CSS and JavaScript. No build step, no framework, no dependencies.
Open `index.html` in a browser and it works.

## Layout

```
index.html      Home — video hero, headline figures, product cards, 5-step summary
about.html      Importer-to-exporter story, what we handle ourselves, orchards
products.html   Longan specification + grades, other fruits, harvest calendar
quality.html    How an order runs, standards, residues, cold chain, terms, markets
contact.html    Quotation request form and contact details

assets/style.css   All styling for every page
assets/main.js     Language toggle, sticky nav, scroll reveal, hero slider, calendar
images/            Logo files, favicons, and real photographs from the shed

sitemap.xml     Search engines
robots.txt      Crawler rules, points at the sitemap
llms.txt        Plain-text summary of the business for AI search engines
_headers        Cloudflare Pages cache rules
_redirects      Pretty URLs (/about → /about.html)
```

## Editing

Both languages live in the same markup. Each phrase is a pair:

```html
<span data-th>ลำไยสด</span><span data-en>Fresh longan</span>
```

CSS hides whichever language is not active, so **edit both halves** or one
language will silently fall out of date. English is the default on first visit;
the visitor's choice is then remembered in `localStorage`.

The harvest calendar is generated from twelve-character bands, one per fruit —
`#` peak, `-` in season, `.` out of season, January to December.

## Deploying

Connected to Cloudflare Pages. Every push to `main` publishes automatically;
no build command, output directory is the repository root.

## Still to do

- The quotation form is a demo — it validates and thanks the visitor but sends
  nothing. Needs a form service (Formspree, Cloudflare Workers, or similar).
- Photographs and the hero videos are still served from an external CDN. Move
  them into `images/` so the site is self-contained.
- The office address on the contact page is a placeholder.
