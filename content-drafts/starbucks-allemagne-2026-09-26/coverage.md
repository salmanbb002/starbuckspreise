# Coverage + QA: starbucks allemagne

- **Tier 1:** 4/4 (100 %) with values (179 cafés, 3,90 € cappuccino, etc.). **Tier 2:** 4/4 (100 %). Tier 3 „You Are Here“ mug not used (see annotated notes).
- **Headings:** one FR H2 inside the existing German page (host H1 unchanged). Lead-ins are bold questions, not headings, to avoid adding 4 FR H3s to a German outline. ✔
- **Answer block:** 45 words, standalone, FR. ✔
- **Fact check:** every figure traced to the host page (ScrapeHero 1 Jul 2026, AmRest 2016, Berlin May 2002) or `menu.js`. ✔ Prices are from the site's own list, not verified in store (same caveat as the rest of the site).
- **Intent:** covers know intent; mug intent left to /blog/starbucks-tassen.
- **Flags for the user:**
  1. ⚠ A native-French proofread is recommended before publishing (written by the pipeline, not a native speaker).
  2. ⚠ `lang="fr"` must be set on the section and the FAQ H3/P elements, or Google will treat the text as German.
  3. The FR FAQs are appended to a German `FAQPage`. That's valid schema, but if you want to keep the FAQ schema German-only, skip the schema append and keep the FR Q&A as HTML only.
  4. Watch GSC country data (FR/BE/CH) for 8 weeks. If impressions appear, a dedicated FR page is worth it.
