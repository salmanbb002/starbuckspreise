# Coverage QA — starbucks greding

- **Entity coverage**: Tier-1 6/6 (100%), each with a stated attribute (Greding: pop+district; Starbucks: 2 locations; A9: direction context; Greding-Ost: hours+co-tenant+parking; Greding-West: seats+opening+design; Tank & Rast: operator+12th-location fact). Tier-2 7/7 (100%). Tier-3: 3/3 used (EnBW, E.ON, SANIFAIR all placed naturally in the amenities section).
- **Heading architecture**: 1 H1, 6 H2s + FAQ, no skipped levels, no sub-H3s needed (sections are short/flat, appropriate for a 110 vol/mo page). No two headings compete for the same phrase.
- **Answer-block check**: Direct-answer block is 46 words, states the core fact (no store in town, two rest-stop locations, hours) without restating the H1 or using "In diesem Artikel."
- **Question coverage**: No PAA/fan-out existed (thin SERP) — FAQ built from the confirmed facts plus the two questions a reader would predictably still have (car-only access, why two stores). All 10 questions map to facts stated in the body.
- **Fact cross-check**: every number (population, seat counts, parking counts, hours, discount amount, distances) traced to a specific source in research-notes.md. The one single-sourced claim (Greding-Ost serves the Nürnberg direction) is flagged below, not hidden.
- **Intent check**: query intent is "does Greding have a Starbucks / where / when" — delivered directly in the first 46 words, then expanded.
- **Readability**: short sentences, concrete numbers throughout: approx. grade 7-8, appropriate for a local-info page.
- **E-E-A-T flags**:
  1. **Single-sourced fact**: "Greding-Ost serves traffic toward Nürnberg" comes from one WebSearch result snippet, not independently cross-verified against a second source — worth a quick manual check before publishing if precision matters.
  2. **Data discrepancy surfaced, not resolved**: this site's own merged_stores.json says "24/7" for Greding-Ost; two independent external sources say 6:00–22:00. The draft states both and defers to the official/independent sources — flagging in case the OSM data reflects something the other sources missed (e.g. a since-changed schedule).
  3. **No phone number found** for either location in any source checked (store locator, Gelbe Seiten) — omitted rather than invented.
  4. **schema.jsonld** has `TODO:` placeholders for hero image path and publish/modified dates — fill in at publish time.
  5. **No exact opening date** for Greding-West found (source only says "recently" as of the 11 Dec 2025 article) — stated as "Ende 2025" rather than a fabricated specific date.
