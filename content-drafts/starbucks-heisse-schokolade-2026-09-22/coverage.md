# Coverage / QA — starbucks heiße schokolade

- **Entity coverage:** Tier-1 4/4 (Starbucks, Signature/Classic/White Hot Chocolate) each with a stated attribute or relationship. Tier-2 4/4 (Signature Chocolate 42%, 70%, Java Chip disambiguation, fddb metric) covered. Tier-3: none defined (short post, no long-tail padding needed).
- **Heading architecture:** One H1, no skipped levels (one H3 nested correctly under the Sorten H2), every H2 owns a distinct question/topic, heading list alone conveys the page logic (varieties → price → calories → at-home powder → Java Chip disambiguation → vegan → FAQ).
- **Answer-block check:** Direct-answer block is 48 words, doesn't restate the H1, states the concrete price range up front.
- **Competitor-heading matrix:**
  | Recurring section | starbuckspreise.de | speisekartemenus.de | fddb.info | starbucks.de official |
  |---|---|---|---|---|
  | Varieties/menu | Yes | Yes (wrong names) | — | Yes (authoritative) |
  | Price | Yes (self-contradictory) | Yes | — | No prices shown |
  | Calories | Yes | No | Yes (authoritative) | No |
  | At-home powder | No | No | No | Covered via starbucksathome.com — genuine gap all 3 direct competitors missed |
- **Question coverage:** All Step 1 fan-out questions answered in-body or FAQ. No PAA block was available from the search tool for this run (no browser SERP capture) — noted as a scope limit, not silently skipped.
- **Fact cross-check:**
  - starbuckspreise.de prices (6,40 €/4,99 €/ab 4,80 €) — sourced, flagged as internally inconsistent in the draft itself.
  - speisekartemenus.de Tall/Grande/Venti prices — NOT used in the final draft (product names don't match the real German menu); explicitly noted as a mismatch instead.
  - fddb.info kcal figures (56 kcal/100g, 140/112/236 kcal by size) — sourced.
  - starbuckspreise.de kcal figures (351/357/311 kcal) — sourced, presented as a second, higher data point rather than merged into one number.
  - Signature Chocolate 42% ~185 kcal/cup, 70% prep ratio (5 tsp/200ml), 70% price 7,79€/330g — sourced from starbucksathome.com and sweet-universe.de.
  - Nestlé/2018 Global Coffee Alliance licensing fact — reused verbatim from the already-sourced `starbucks-kapseln-angebot` post, not re-derived.
  - Java Chip = Frappuccino, not hot chocolate — sourced from Starbucks' own product categorization (general knowledge cross-checked against starbucks-menu.html's existing category list, which separates Frappuccino from Hot Chocolates).
- **Intent check:** Delivers on know-simple intent (what exists, what it costs, calories) plus the commercial at-home-powder sub-intent. Meets the keyword's stated "FAQ / short answer post" content type — body kept short, FAQ carries most of the query surface.
- **Readability:** Estimated grade ~8 (German). Sentences are longer in the price/calorie sections due to necessary hedging over conflicting source numbers — acceptable given the topic requires that honesty, flagged rather than smoothed over.
- **E-E-A-T flags for manual review:**
  1. **No single authoritative German price list exists for Hot Chocolates** — draft states a range and names the source conflict rather than picking one number. If StarbucksPreise later gets a verified in-store price, replace the range with an exact figure.
  2. **Calorie figures conflict by more than 2x between two third-party sources** (fddb.info vs. starbuckspreise.de) — both are cited as distinct data points; neither is Starbucks' own published nutrition data (starbucks.de shows none). Recommend replacing with Starbucks' official nutrition calculator figures if/when found for the German menu.
  3. **White Hot Chocolate caffeine claim ("nahe null") is a reasoned inference** (no espresso in the recipe), not a cited figure — flagged in the FAQ answer itself and here; do not present as an exact number without a source.
  4. No author byline/credentials on the page beyond the site's standing "StarbucksPreise Redaktion" — consistent with every other post on this site, not a new gap.
