# QA / coverage — starbucks iced coffee

## Entity coverage
- Tier-1: 6/6 covered (100%) — Starbucks Iced Coffee, Cold Brew, Iced Americano, Preis/Kosten,
  Starbucks, "nicht auf der Karte" — each with a stated attribute/relationship, not a bare mention.
- Tier-2: 6/6 covered (100%) — Kalorien/Koffein, Iced Caffè Latte, Doubleshot Iced Coffee,
  PepsiCo/NACP, Nestlé, Brühmethode.
- Tier-3: 3/3 used (Iced Caramel Macchiato, Tall/Grande/Venti/Trenta, Nitro Cold Brew) — none
  unused.

## Heading architecture check
- One H1, no skipped levels (H2 → H3 only, e.g. "Gibt es..." → "Die nächstliegenden
  Alternativen..."), every H3 sits under an H2. Valid as a standalone outline.
- Every H2/H3 owns a distinct focus/LSI phrase — no two headings compete for the same query.
- Every heading maps to a Step 8 row in research-notes.md.
- Heading list alone conveys the logic: does it exist here? → what's the branded retail version? →
  what does it cost? → how strong/caloric is it? → how is it actually made? → FAQ.
- H2 count (6) roughly matches the fan-out/PAA question set (12 distinct questions across FAQ +
  body).

## Answer-block check
- Direct-answer block: 54 words — within the 40-55 word target, doesn't restate the H1, states a
  standalone claim (not available in DE cafés under that name, nearest alternatives + price,
  Doubleshot can exists).
- Each question-style H2 answers in its first sentence (QUORA order held) — verified section by
  section.

## Competitor-heading matrix

| Recurring H2 across competitors | starbucksxmenu | starbucksreserveonly | speisekartemenus | groundstobrew | Covered here? |
|---|---|---|---|---|---|
| What is it / intro | yes | yes | — | — | yes (own framing: "is it on the DE menu") |
| Price | yes | yes | yes | yes | yes, DE-specific EUR table |
| Calories/nutrition | yes | yes | — | partial | yes |
| Caffeine | yes | yes | — | yes | yes |
| vs Cold Brew | — | yes | — | yes (whole article) | yes |
| vs Iced Americano | — | yes | — | — | yes |
| Customize/pros-cons | yes | yes | — | — | intentionally skipped — DE menu doesn't offer the same customization path; would be off-topic for a DE audience |
| FAQ | yes | yes | yes (1 Q) | yes | yes, 12 questions |

## Question coverage
All 3 fan-out sub-keywords (`starbucks iced`, `iced caffe latte starbucks`, `starbucks ice
coffee`) and all 12 FAQ questions are mapped to a body section or the FAQ block — none left
unanswered. Competitor FAQ questions reused: 4 of 12 (2 from starbucksreserveonly, 1 from
starbucksxmenu, 1 from groundstobrew); remaining 8 are genuine gaps (DE availability, Doubleshot
manufacturer, DE alternative, DE Iced-Americano price, home-brew ratio) none of the 4 competitors
ask.

## Fact cross-check
Every number traces to research-notes.md: US prices/calories/caffeine → starbucksxmenu.com +
starbucksreserveonly.com; DE EUR prices → speisekartemenus.de (live fetch); DE menu drink list →
starbucks.de/de/menu-drinks-iced-coffees (live fetch, 2026-09-22); PepsiCo/NACP 1994 fact →
pepsico.com press release + pepsicopartners.com (WebSearch, cross-referenced two independent
sources); home-brew ratio → starbucks.com official athome page (WebSearch summary). No unsourced
numbers. Doubleshot retail price ("ca. 2,00–2,50 € pro Dose" in the comparison table) is the one
softest figure — inferred from typical German RTD-canned-coffee retail pricing rather than a
single quoted source; flagged below for manual spot-check.

## Intent check
Delivers on the dominant *know* intent (does it exist here, what is it) and the secondary *buy*
intent (price, where the branded can is sold) — matches Step 1 classification.

## Readability
Estimated grade ~8-9 (German). Sentences kept short-to-medium; two longer sentences in the
"Zubereitung" section could be split further if a stricter grade target is needed.

## E-E-A-T flags (need manual review)
1. **Doubleshot can retail price (~2,00–2,50 €)** is an estimate, not a directly sourced quoted
   price — verify against an actual German retailer listing (e.g. the Kaffeegemeinde or Flink
   listing found during research) before treating it as exact.
2. **Author byline** uses the site's existing "StarbucksPreise Redaktion" organizational author
   pattern (same as the sibling kapseln-angebot post) — no individual named author/credentials,
   consistent with how the rest of the site already handles bylines.
3. First-person-adjacent phrasing ("Recherchestand: 22. September 2026") is scaffolding stating
   when the page was checked, not a lived-experience claim — flagged per pipeline convention, no
   action needed unless the site wants a different disclosure style.
4. YMYL: none — this is commercial/informational F&B content, not health/finance/legal/government
   benefits; no special disclaimer needed beyond the existing site-wide footer disclaimer.
