# starbuckspreise.com

Static site: Starbucks Preise 2026 - komplette Speisekarte mit Preisen & Kalorien (Deutschland).

- `index.html` + `menu.js` + `styles.css` - home (menu is rendered from `DATA` in `menu.js`)
- `img/` - product images (local copies)
- `*.html` - info pages (contact, about, legal, topic pages)
- `vercel.json` - clean URLs + cache headers

No build step. Deployed on Vercel, auto-deploys from `main`.

## Local preview
    python3 -m http.server 8000

## Blog layout

All 14 articles use the same static layout in `blog/*.html`. `blog.css` contains
the scoped blog styles; `blog.js` progressively collapses the native contents
list on smaller screens. Navigation and FAQs work without JavaScript.

When publishing an article, copy an existing article's structure, including
the shared header, stylesheet/script links, `.article-header`, `.article-layout`,
and footer. Keep each `h2` and its content in an `.article-section` with
`aria-labelledby` pointing to that heading's unique ID. Link the contents list
to those IDs and wrap tables in `.table-wrap`. Retain the article's metadata,
structured data, image descriptions, and text when changing its presentation.

Run the layout check before publishing; GitHub also runs it for blog changes:

    python3 scripts/check-blog-layout.py
