# Coverage + QA: menu keyword batch

- **Tier 1:** 4/4 (100 %). **Tier 2:** 7/7 (100 %).
- **Headings:** Block A = one EN H2 (host already has FAQ H2 last, so place it before §1). Block B = one H3 under existing H2 §4. No skipped levels. The five keywords map to five distinct placements, so no heading-level cannibalisation. ✔
- **Answer block (EN):** 44 words. ✔
- **Fact check:** prices from `menu.js`; English categories fetched from starbucks.de/en/menu on 26 Sep; Nestlé/Global Coffee Alliance/Chilled Classics from the site's own researched pages. ✔
  - „Halbfettmilch = standard milk in most drinks“ is an **inference** (PDF lists it first; site kcal match it). ⚠ Same flag as the Nährwerte draft.
  - The table's „Merchandise: nur in der Filiale“ is consistent with the site's becher page (starbucks.de merch is catalogue-only, no shop). ✔
- **Flags for the user:**
  1. ⚠ Existing page H3 says Rubrik „Hot Coffees“. starbucks.de/en/menu now shows „Hot Drinks“ / „Iced Drinks“. Worth re-checking §2 headings against the live German menu.
  2. The EN box adds English text to a German page. Set `lang="en"` on the section, or it dilutes the page's language signal.
  3. A native-English proofread is optional; the text is short and plain.
