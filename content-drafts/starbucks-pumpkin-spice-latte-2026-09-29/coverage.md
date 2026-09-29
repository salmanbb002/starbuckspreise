# Coverage / QA: starbucks-pumpkin-spice-latte-2026-09-29

- **Entity coverage:** tier 1 is 9/9 (100%), and every tier-1 entity is stated with a value (price, kcal, mg or definition). Tier 2 is 15/15 (100%). Tier 3 is 6/8 used; Peter Dukes and the Nespresso/Dolce Gusto PSL were parked (reasons in research-notes).
- **Headings:** one H1, eight numbered H2s plus the FAQ H2, and 18 H3s, all nested under H2s. The finalize.py check found no hierarchy errors. Each H2 owns a distinct phrase: preis, kalorien/koffein, herbst getränke 2026, USA-vergleich, ab/bis wann, vegan, bestellen.
- **Answer block:** 50 words; it does not restate the H1 and leads with the price. Every H2 and H3 answers in its first sentence (verified in the finalize output).
- **Questions:** 12 FAQs. Autocomplete intents (preis, 2026, ab wann, frappuccino, herbst getränke) are answered in the body or FAQ. "Instant/Pulver/Nespresso" is intentionally not answered.
- **Fact check:**
  - All kcal, sugar, protein and caffeine values were re-checked row by row against S2 (DE Autumn PDF, 10.09.2026).
  - All prices come from S3 (Freiburg Hbf).
  - US items come from S6.
  - The vegan rules come from S4.
  - History comes from S5.
  - Two errors were caught and fixed: "lightest herbstgetränk mit Halbfettmilch" (was PSCM 209, now Iced PSL 192), and "jeweils heiß oder iced".
  - The PSL is topped with **Milchschaum + Gewürzmischung** (S3 DE description), not whipped cream. This was corrected from the first draft.
- **Intent:** delivers price, kcal and caffeine in the direct answer, which is the know intent.
- **Readability:** short sentences with tables for numbers, about grade 8.
- **Schema:** BlogPosting + FAQPage (generated from draft.md, so it matches verbatim) + BreadcrumbList. about/mentions use Thing/Organization only. Wikidata PSL Q18345746 and Starbucks Q37158 were verified via the API. **TODO:** publisher logo URL, and run the Rich Results Test.
- **E-E-A-T:** no first-person claims. The author is set to "StarbucksPreise Redaktion" (Organization); replace it if the site has a real author page.

## Flags
See research-notes.md "Open flags" (price conflict with /blog/starbucks-preise, the unknown DE 2026 start date, the iced PS matcha name mapping, the missing Apple Crumble nutrition, and the hero image).
