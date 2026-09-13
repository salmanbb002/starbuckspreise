# Publication handoff

This folder contains drafts, not published pages.

1. TODO: insert the real author/byline and author entity, if applicable.
2. TODO: set datePublished to the actual publication date; use dateModified for subsequent changes.
3. Recheck the Damm 22 hours and "only current location" status immediately before publication — this page's whole angle is calling out stale competitor data, so it must not itself go stale.
4. Insert article.fragment.html into the existing StarbucksPreise blog template (see blog/starbucks-in-der-naehe.html for the shell). Keep `#direct-answer` for the supplied speakable selector.
5. Use metadata.json and schema.jsonld with the intended `/blog/starbucks-braunschweig` slug. Update `blog/index.html`, `sitemap.xml`, `vercel.json` rewrites, and the keyword workbook (Day 8, Content_Calendar) only when publication actually happens — `engine/master_publisher.py:build_starbucks_article()` in the SEO Content creator repo does all four of those plus git push + `vercel --prod` deploy in one call; do not run it until the draft is approved.
6. A hero image is still needed — no existing `img/blog/` asset fits a Braunschweig storefront; source one manually (`?license=free` Unsplash filter per project convention) rather than reusing another city's photo.
7. Validate the assembled page with Schema.org Validator / Rich Results Test. No rich-result appearance is promised.

Draft sources and QA limits are documented in research-notes.md and coverage.md.
