# QA / coverage — starbucks bamberg

## Entity coverage
- Tier 1: 3/3 covered, all with a stated attribute (Bamberg = no store, 77k pop, UNESCO Altstadt; Starbucks = has locator, no Bamberg listing; "no store" fact stated directly in H1's direct-answer block).
- Tier 2: 5/5 covered (Nürnberg locations, A3 Häusling, Bamberg-SC confusion, Coffee Fellows Hallstadt, UNESCO Altstadt).
- Tier 3: 2/2 used naturally (A70 in alternatives section, Store Locator as link).

## Heading architecture
Valid: one H1, no skipped levels (H2→H3 only), every H3 sits under its H2. No two headings target the same query. Table used for the distance comparison, matching the "closest options" info-gain element. 6 H2s (incl. FAQ) — reasonable for a thin-SERP, single-intent page.

## Answer-block check
Direct-answer block: 52 words, doesn't restate H1, leads with the direct no/yes answer per the *visit-in-person* intent. Question-style H2/H3s answer in their first sentence (QUORA order held throughout).

## Competitor-heading matrix
No independently-ranking competitor article exists for this exact query (see research-notes Step 1/4) — matrix not applicable in the normal sense. Structural model was the site's own live `starbucks-trier` page (same "no store in this city" content type); its heading pattern was followed and adapted, not copied verbatim.

## Question coverage
All fan-out questions identified in Step 1 (existence, öffnungszeiten curiosity, nearest alternative, US-namesake confusion) are answered in body or FAQ. No PAA box was present on the live SERP to check against (thin SERP, no PAA rendered).

## Fact cross-check
- Zero-Bamberg-rows-in-dataset claim → traced to direct `merged_stores.json` file check (own site data).
- Nürnberg/A3 store addresses + coordinates → traced to `merged_stores.json`.
- Population, UNESCO date → traced to bamberg.info / unesco.de search snippets.
- Coffee Fellows Hallstadt detail → traced to franchise.coffee-fellows.de press page.
- Bamberg-SC confusion → traced to yellowpages.com appearing in live search results for the query.
- **FLAG**: driving distances (40-45 km, 55-60 km) are haversine estimates from stored coordinates with a rough ×1.3 road-factor, not a routed Google/OSM Maps query — replace with exact routed distances before publishing if precision matters.
- No invented statistics, prices, or quotes.

## Intent check
Delivers what a "does Bamberg have a Starbucks" searcher wants: a direct yes/no, the real nearest options with distance/access tradeoffs, and the local alternative. Matches the successful pattern of the site's own already-ranking Trier page.

## Readability
Estimated grade 8-9 (German). Sentences are mostly single-clause with one embedded fact; no passage exceeds ~90 words without a break.

## E-E-A-T flags (needs human input before publishing)
- **Author byline**: `schema.jsonld` has a `TODO:` placeholder — no author name/credentials invented.
- **Distances**: flagged above — verify with a real routed-maps query, don't publish the estimate as if it were exact.
- **"Recherchestand" date line**: set to today (2026-09-19); update if publish date differs.
- No first-person "lived experience" claims were added (this is a fact-lookup page, not an experience piece) — nothing to flag there.
- Not YMYL (health/finance/legal) — no medical/financial disclaimer needed.
