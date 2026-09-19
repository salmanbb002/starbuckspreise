# QA scorecard — "starbucks tasse münchen"

## Entity coverage
- **Tier 1 (6 items):** 6/6 covered (100%). All 6 carry a stated attribute/relationship,
  not a bare mention — Starbucks (brand/org), München (theme city + store location),
  You Are Here Collection (series + release year), 414ml (capacity), Juni 2016 (release
  date), Preis/Kaufort (price bands + channels).
- **Tier 2 (5 items):** 5/5 covered (100%) — Keramik/Maße, Starbucks Store München
  (Rosental 7), Echtheit/Fälschung, Sammlermarkt/Zweitmarktwert, Bring-Your-Own-Mug-Rabatt.
- **Tier 3 (2 items):** Geschenkbox/Versandbedingungen used (reseller section);
  "weitere Tassentypen Deutschland" deliberately parked (out of scope, logged in
  research-notes.md).

## Heading architecture check
- One H1, no skipped levels, all H3s sit under an H2 (H3s only under "Wo können Sie
  kaufen?"). Every H2/H3 targets a distinct phrase — no heading-level cannibalisation.
- Heading list read alone conveys the page logic: what it is → specs → price → where to
  buy → authenticity → discount question → collector value → FAQ.
- H2 count (7) matches the fan-out/question set found (no PAA block surfaced for this
  low-volume query — fan-out came from related-search phrasing instead).

## Answer-block check
- Direct-answer block: 46 words, states what the mug is, capacity, and buying reality
  without restating the H1. Matches "no strong snippet format" from Step 1 (no snippet to
  mirror on this thin SERP).
- Question-style H2s (kaufen, echt, Rabatt, Sammlerstück) each answer in their first
  sentence.

## Competitor-heading matrix
| Recurring element | thecoffeemugshop.de | starbucks-mugs.com | starbuckspreise.de | Covered? |
|---|---|---|---|---|
| Specs (capacity/material/dimensions) | yes | partial | no | yes |
| Release date | yes | yes | no | yes |
| Price | yes | yes (resale) | general range only | yes |
| Where to buy (multi-channel) | one channel only | one channel only | store list only | yes — improved (this is the info-gain table) |
| Authenticity guidance | no | no | yes (general) | yes — made München-specific |
| Collector value / resale | no | yes (brief) | yes (general tips) | yes |

## Question coverage
All Step 1 fan-out queries and Step 10 FAQ-source questions are mapped to a section or FAQ
answer (see research-notes.md Step 10 table). None left unanswered.

## Fact cross-check
- 414ml/14fl.oz, dimensions, weight, release date, reseller price (€25,99/€37,99) →
  thecoffeemugshop.de.
- Resale price range ($20–$109) → starbucks-mugs.com.
- Rosental 7 / Marienplatz store address, 0,30€ discount → starbuckspreise.de (competitor
  source — **flag: this address was not independently verified against Starbucks' own
  store locator; confirm before publishing**).
- Munich landmark motifs (Neues Rathaus, Weißwurst, Oktoberfest) → Amazon listing title
  captured in Step 1 search, not a full fetch — **flag: secondary-source only, worth a
  quick visual confirmation from a product photo before publishing**.
- Authenticity marks (Sirenen-Logo, Bodenprägung) → general knowledge stated cautiously,
  not tied to a specific cited source — **flag: generic anti-counterfeit guidance, not
  München-mug-specific verified fact**.

## Intent check
Delivers on *buy* intent (price bands, channels, new-vs-used table) and secondary
*know-simple* (specs, release date) — correctly avoided forcing this into a
store-locator template.

## Readability
Estimated grade 8-9 (German). Sentences are moderate length; a few longer compound
sentences in the pricing section could be split further on a copy-edit pass.

## E-E-A-T — flags needing manual input
1. **No first-hand ownership claim was made** — good, but if the site owner actually owns
   or has seen this mug, adding one genuine specific detail (a photo, a real observed
   defect/quality note) would meaningfully strengthen trust on what is otherwise a
   reseller-sourced spec sheet.
2. **Author byline/credentials** — `schema.jsonld` has a `TODO:` placeholder, not filled.
3. **dishwasher/microwave-safe FAQ answer** — deliberately hedged (no official care spec
   found for this specific mug); do not tighten this into a firm claim without a real
   source.
4. **Rosental 7 store address and 0,30€ discount amount** — sourced from a competitor
   article (starbuckspreise.de), not Starbucks' own site — verify both against the
   official store locator before publishing, especially the discount amount which can
   change.
5. **`datePublished`/`dateModified` and author fields** in `schema.jsonld` are placeholders
   — fill before deploying, and run the file through the Rich Results Test.
6. **BreadcrumbList schema omitted** — this site's URL structure for this page
   (`/blog/...` vs `/standorte/...` vs a possible `/tassen/` path) wasn't confirmed from
   existing files; add breadcrumb schema once the final URL/nav placement is decided.
