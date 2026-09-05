# starbuckspreise.com

Static site: Starbucks Preise 2026 - komplette Speisekarte mit Preisen & Kalorien (Deutschland).

- `index.html` + `menu.js` + `styles.css` - home (menu is rendered from `DATA` in `menu.js`)
- `img/` - product images (local copies)
- `*.html` - info pages (contact, about, legal, topic pages)
- `vercel.json` - clean URLs + cache headers

No build step. Deployed on Vercel, auto-deploys from `main`.

## Local preview
    python3 -m http.server 8000
