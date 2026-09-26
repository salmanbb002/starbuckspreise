# Coverage + QA: starbucks nährwerte → kalorien-guide

## Entity coverage
- **Tier 1:** 5/5 covered (100 %), all with attribute/value (e.g. Koffein → 44,5 mg pro Shot; Zucker → schließt Laktose ein).
- **Tier 2:** 11/11 covered (100 %).
- **Tier 3:** ESHA and Allergene used; Ballaststoffe/Salz/kJ only named (see annotated notes).

## Heading architecture
- One H1, 8 numbered H2 + FAQ H2, every H3 nested under an H2, no skipped levels. ✔
- Each H2 owns a distinct phrase (quelle / tabelle / kalorien / milch / zucker / koffein / snacks / sparen). No overlap. ✔
- Headings read alone give the page's logic (source → table → kcal → levers → action). ✔

## Answer block
- Direct answer: 47 words, doesn't restate the H1, paragraph format (no snippet on SERP to match). ✔
- Every question-style H2 answers in its first sentence. ✔

## Competitor matrix
Competitors are databases without editorial H2s. Covered: product list ✔, kcal ✔, portions/sizes ✔, categories (drinks/food) ✔.

## Question coverage
All fan-out phrases mapped: tabelle → §2, kalorien latte → FAQ, zucker → §5, koffein → §6, pdf → §1, allergene → FAQ, frappuccino kalorien → §3 + FAQ.

## Fact cross-check
- Every drink/food number is transcribed from the Autumn 10.09.2026 PDFs (rows quoted in research-notes). Derived numbers are arithmetic on those rows: 390 kcal gap, 47 kcal / 6,6 g Tall saving, 69/36 kcal milk saving, 649 kcal combo, ~13 g added sugar. ✔
- **WHO** (<10 % / <5 % free sugar) and **EFSA** (400 mg/day, 200 mg single dose, 200 mg pregnancy) are well-established public guidance, but **no link was fetched this run**. ⚠ Add source links before publishing: WHO 2015 sugars guideline, EFSA Journal 2015;13(5):4102.
- „Halbfettmilch ist die Standardmilch“ is an **inference**: the PDF lists Halbfettmilch first for every milk drink, and `menu.js` kcal match the Halbfettmilch Grande rows. Starbucks doesn't state it in words. ⚠ Verify in store or soften to „in der Regel“.
- „Sugar-Free Vanilla Sirup“ exists as a PDF row (Soy Protein Latte). Whether it can be added to any drink is not confirmed. The draft only says the syrup exists. ✔

## Intent
Delivers a lookup table (know-simple) plus the levers for choosing (know). ✔

## Readability
~Grade 8. Short sentences; the tables carry the density.

## E-E-A-T / flags for the user
1. ⚠ **Site-wide data drift:** `menu.js` kcal come from an older release. ~20 drinks differ from Autumn 2026, e.g. Strawberry Acai 87→80, Mango Dragonfruit 101→90, Coffee Frappuccino 299→283, Caramel Frappuccino 362→346, PSL 266→259, Matcha Latte 166→161. The homepage then disagrees with this article. Recommend a `menu.js` kcal refresh from the PDF.
2. ⚠ **`iced-caramel-macchiato.html` caffeine:** on 24 Sep (e7a9e68) Grande was changed 75→150 mg. The official DE PDF says **89,1 mg** for Grande Iced Caramel Macchiato (150 mg is the US figure). Should be corrected.
3. Health/YMYL-adjacent: add a one-line note that values are guidance, not dietary advice (the FAQ „verbindlich“ partly covers this).
4. No first-person claims were written, so none need replacing.
5. `schema.jsonld`: author is the site's existing „StarbucksPreise Redaktion“ Organization (matches the other posts). Validate in the Rich Results Test.
