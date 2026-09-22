# QA / coverage — starbucks-flat-white

## Entity coverage
- Tier-1: 2/2 covered (Flat White, Starbucks), both with attributes/relationships stated, not bare mentions. **100%**
- Tier-2: 7/7 covered (Café Latte, Cappuccino, origin dispute, Iced Flat White, Starbucks Flat White Eiskaffee, Arla Foods — Hafermilch-Variante also covered in §4). **100%**
- Tier-3: 1/2 used (Ristretto, used in §1 subsection). "Vanilla-Flavor-Variante (fddb)" deliberately unused — flagged in research-notes.md and draft.annotated.md, not silently dropped.

## Heading architecture check
- One H1, no skipped levels (H1 → H2 → one H3 under §1). Valid as a standalone outline.
- Every H2 owns a distinct focus/LSI phrase: definition / origin / comparison / price / retail-iced — no two H2s target the same query.
- Every heading maps to a Step 8 row (research-notes.md).
- H2 count (5 body + FAQ) matches the short-answer post format used by the sibling `starbucks-heisse-schokolade` post, scaled to this keyword's lower search volume/KD.

## Answer-block check
- Direct-answer block: 46 words (within the 40-55 word target), doesn't restate the H1, matches a paragraph-snippet format.
- Each H2 answers its own question in the opening sentence (QUORA answer-first order held) — verified section by section.

## Competitor-heading matrix

| Recurring block | starbuckspreise.de | speisekartemenus.de | supermarktcheck.de | fddb.mobi |
|---|---|---|---|---|
| Definition/composition | yes (thin) | no | no | no | covered, expanded (industry-standard ml/mm figures + ristretto note)
| Price | yes | **no (gap)** | n/a (different product) | n/a | covered, gap named explicitly
| Calories | yes | no | yes (RTD can, different product) | yes (flagged unconfirmed variant, unused) | covered
| Origin story | no | no | no | no | net-new (Wikipedia), not on any competitor
| Latte/Cappuccino comparison | no (adjectives only) | no | no | no | net-new comparison table (info-gain element)
| Retail can / manufacturer | no | no | yes (product data) | no | expanded with Arla Foods licensing fact (not on the product page itself)

## Question coverage
All 3 fan-out/merged-keyword questions ("flat white starbucks drink", "starbucks flat white", implicit
"what's the difference vs latte/cappuccino") are mapped to a section or FAQ; none left unanswered.

## Fact cross-check
- 4,71 € price, 318 kJ/76 kcal (Vollmilch) → starbuckspreise.de (fetched in full).
- 70 kcal (Hafermilch) → WebSearch AI-summary of fatsecret.de/fddb.de, **not a directly fetched page** —
  flagged here as a secondary-source figure, consistent with (not contradicted by) the fetched
  starbuckspreise.de Vollmilch number.
- 220 ml / €2.29 / Nutri-Score B / 66 kcal per 100 ml / ingredient list → supermarktcheck.de (fetched in full).
- Composition (50 ml espresso + ~130 ml milk + ~5 mm microfoam, 175-200 ml cup), origin claims + dates,
  6 January 2015 US launch date → en.wikipedia.org/wiki/Flat_white (fetched in full).
- Arla Foods 21-year EMEA license, Esbjerg production, Arla Foods Deutschland distribution →
  cross-referenced trade-press WebSearch results (lebensmittelpraxis.de, rundschau.de, arlafoods.de,
  lebensmittelzeitung.net) — not a single fetched page, but four independent trade sources converging on
  the same facts; flagged as secondary/aggregated sourcing, not an invented figure.
- speisekartemenus.de omission → confirmed directly via WebFetch of that exact page (fetched in full,
  Flat White absent from its price table).
- No number in the draft is unsourced or invented. The fddb.mobi "Vanilla Flavor" figures are the one
  data point deliberately excluded rather than used.

## Intent check
Satisfies know-simple (what it is), know (origin, vs. latte/cappuccino), and transactional (price, where
to buy the can) intent in one short piece, matching the calendar's Informational+Low-priority/
FAQ-short-answer classification.

## Readability
Estimated grade ~8-9 (German public-info register, short sentences, one comparison table). No
excessively dense passage over ~120 words without a break.

## E-E-A-T flags (need manual/human input before treating as final)
1. **Author byline is a placeholder organizational name** ("StarbucksPreise Redaktion"), matching the
   sitewide pattern already used on every prior post — no invented personal credential, but still not a
   named human author with credentials.
2. **Price and calorie figures are third-party, not Starbucks-official** — Starbucks Germany publishes no
   public price list; stated plainly in the draft (§4) rather than presented as an official figure.
3. **Hafermilch (70 kcal) figure traces to an AI-summarized search result, not a page this run fetched
   directly** — worth a spot-check against fatsecret.de or fddb.de directly before treating as exact.
4. **Arla Foods manufacturing facts come from converged trade-press reporting, not an Arla/Starbucks
   primary source page fetched in this run** — high-confidence (four independent outlets agree) but still
   secondary sourcing; verify against arlafoods.de's press release directly if this fact is challenged.
5. No health/YMYL disclaimer added — content is informational/commercial (pricing, product description),
   not medical, so this follows the same standard as the sibling drink posts on this site.
