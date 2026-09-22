# Coverage / QA — "starbucks kapseln angebot"

## Entity coverage
- **Tier 1 (7 rows):** Starbucks, Starbucks Kapseln, Angebot/Rabatt/Preis, Nespresso, Dolce Gusto, Sorten/Röstungen, Preis pro Kapsel, Global Coffee Alliance — **100% covered**, each with a stated attribute/relationship (not bare mentions): Starbucks↔Nestlé license relationship, Nespresso↔Vertuo incompatibility, Dolce Gusto↔specific varieties, price-per-capsule↔pack-size math.
- **Tier 2 (7 rows):** Nestlé, Intensität, Multipack, Händler, Preisverlauf, Vertuo, Rabattzeiträume — **100% covered**.
- **Tier 3 (3 rows):** Decaf (used), Aluminium/Recycling (used), Kompatible Maschinen (used briefly, flagged as not deepened — logged in draft.annotated.md).

## Heading architecture check
- One H1, no skipped levels (H1→H2→H3 only where Nespresso/Dolce Gusto split needs it). Valid as a standalone outline.
- Every H2/H3 owns a distinct focus/LSI phrase — no two headings target the same query.
- Every heading maps to a Step 8 map row (research-notes.md).
- Heading list alone conveys the logic: what/who-makes-it → machine-fit → varieties → price → deal-timing → sustainability → FAQ.

## Answer-block check
- Direct-answer block: 52 words — within the 40–55 word target, doesn't restate the H1, states the core fact (price range + who makes it + where to buy) matching the informational+commercial SERP.
- Question-style sections (Nespresso/Dolce Gusto, price, deal-timing) answer in their first sentence — QUORA order held throughout.

## Competitor-heading matrix

| Recurring heading concept | aktionspreis.de | starbuckspreise.de | tuttocialde.de | Covered here? |
|---|---|---|---|---|
| Price / price history | ✅ | ✅ | ✅ | ✅ (price table + info-gain price-history box) |
| Where to buy / retailers | — | ✅ | — | ✅ |
| Varieties | ✅ (brief) | ✅ | ✅ | ✅ |
| Compatibility (Nespresso vs. other machines) | — | ✅ (partial) | ✅ | ✅ — extended to include Dolce Gusto side, which none of the 3 covered in full |
| FAQ | — | ✅ | — | ✅ (12 vs. their ~3) |
| Nestlé/manufacturer explainer | — | — | — (mentioned only in passing) | ✅ — information-gain element, not covered by any competitor |

## Question coverage
All fan-out questions (research-notes.md Step 1) and all 3 starbuckspreise.de FAQ topics are mapped to either a body section or the FAQ block. None left unanswered.

## Fact cross-check
Every number, date, and named entity traces to `research-notes.md`:
- 0,30–0,50 €/Kapsel, price table figures → aktionspreis.de + starbuckspreise.de + tuttocialde.de (Step 4/5).
- 7,15 Mrd. USD / 28.8.2018 Global Coffee Alliance → verified via WebSearch (SEC 8-K filing + Food Business News + Nestlé/Starbucks press releases), cross-checked across 3 independent sources.
- Dolce Gusto varieties (Madagascar Vanilla Macchiato etc.) → starbucksathome.com (official, fetched).
- Intensity numbers (5–11) → tuttocialde.de.
- Price-history table (3,65€ Q3 2024 → 3,95€ Q2 2026) → aktionspreis.de.
- Nespresso Vertuo incompatibility → tuttocialde.de ("nur Original Line") + general product-line knowledge.
- Nespresso aluminum recycling program → stated generally (no invented statistic), consistent with tuttocialde.de's "Aluminiumkapsel" mention and well-documented public Nespresso program.

**No unsourced numbers remain.**

## Intent check
Keyword intent (commercial/buy + know-simple) is served: reader learns what fits their machine, what it costs, and — the actual "angebot" ask — when/where to catch a real discount, backed by real tracked pricing data rather than a generic "check the shop" answer.

## Readability
Estimated grade ~8–9 (German B2-equivalent) — short paragraphs, concrete numbers, no jargon beyond what's defined inline (Original Line vs. Vertuo). Consistent with the rest of the site.

## E-E-A-T flags (need human review before/after publishing)
1. **Hero image is not Starbucks-branded.** Wikimedia Commons (the site's usual image source) returned connection errors for every attempt in this run (host-level, not per-file) and no browser-tool fallback was available. Substituted a generic, on-topic, no-attribution-required Pexels photo ("Coffee Capsules in Metal Rack" by Carlos Zael) instead. **Recommend swapping for an actual Starbucks-branded capsule box/product photo** when Commons access is available again — logged in `img/blog/ATTRIBUTION.md`.
2. **Only 3 of 4 target competitors fetched** (8 substitution attempts, all blocked/403/JS-wall/error — see research-notes.md Step 4 table) — the piece is still fully sourced, but a 4th independent competitor pass (e.g. via browser tools once connected) could surface additional angles.
3. **Author byline is the site's standing "StarbucksPreise Redaktion" Organization credit** (same convention as every other post on this site, e.g. `blog/starbucks-becher.html`) — not a fabricated person, no action needed, flagged only for completeness per Step 12 rules.
4. **Pricing is a snapshot** (22 September 2026) from third-party trackers/retailers, not Starbucks' own price list — inherently time-sensitive, same caveat as every price-comparison page on this site.
