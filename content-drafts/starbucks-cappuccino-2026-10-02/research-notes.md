# Research notes – starbucks cappuccino (run 2026-10-02, planned publish 2026-10-09)

## Intent / SERP
- Keyword: starbucks cappuccino, DE, ~60/mo (Research_Oct2026, evergreen, Trends peak 7–13 Jun 2026). Intent: know-simple + price/kcal lookup (price-list sites dominate: fatsecret, wikifit, yazio, starbuckspreise.de, speisekartemenus.de, fastfoodpreis-info.de).
- Fan-out (autocomplete, 29 Sep 2026): angebot, chilled coffee, edeka, eiskaffee, hafermilch, hafermilch kalorien, kalorien, koffein, laktosefrei, preis, pulver, rewe → sections 2,3,4,6,7.
- SERP competitor pages seen (titles only, via WebSearch; **full 4-competitor fetch NOT done**): fatsecret.de (Grande 140 kcal), wikifit.de, yazio.com, starbuckspreise.de (3,90 € / 546 kJ 130 kcal), speisekartemenus.de, fastfoodpreis-info.de.

## Head entities / sources
- Cappuccino — https://de.wikipedia.org/wiki/Cappuccino (fetched 2 Oct 2026): name from Kapuziner, 20–30 ml espresso + 120 ml milk, ~16 % of Germans weekly (2006/07).
- Starbucks — wikidata Q37158.
- starbucks.de/de/menu-drinks-hot-coffees (fetched 2 Oct 2026): 14 hot coffees; Cappuccino description (quoted in draft).
- starbucksathome.com/de/rezepte/cappuccino (fetched): 1 shot, 150 ml milk, 50/50 milk/foam, 3 min, Single-Origin Colombia.
- dolce-gusto.de/starbucks-cappuccino (search hit only, not fetched) → capsule exists.

## Fact ledger (every number → source)
| Fact | Source |
|---|---|
| 3,90 € / 546 kJ / 130 kcal; Iced 4,65 € / 106 kcal | `/July Projects/starbuckspreise/menu.js` lines 14–15 |
| Grande ~4,40 €, Venti ~4,90 € | /blog/starbucks-groessen-tall-grande-venti |
| 3rd-party 5,20–6,20 € Tall–Venti | /blog/starbucks-menu (own earlier research) |
| Latte 4,59/151, Latte Macchiato 4,70/147, Flat White 4,71/76 | menu.js |
| 44,5 mg/shot; Tall/Grande 89,1; Venti 133,6; Pike Place Grande 254,6 | Starbucks DE Nährwert-PDF 10 Sep 2026 as cited in /blog/starbucks-latte, -kaffee, -groessen |
| Cappuccino = same espresso as Latte/Caramel Macchiato | /blog/starbucks-kaffee |
| plant milk +0,50–0,80 €, extra shot ≈0,80 €, syrup +0,60–0,80 € | menu.js FAQ, /blog/starbucks-menu, /blog/starbucks-getraenke |
| sizes 354/473/591 ml, Short 237 ml | /blog/starbucks-groessen-tall-grande-venti |

## Entity tiers + relationships
T1: Cappuccino, Starbucks, Espresso, Milchschaum, Preis, Kalorien, Koffein, Espresso-Shot. T2: Latte, Latte Macchiato, Flat White, Iced Cappuccino, Hafermilch/Pflanzendrink, laktosefrei, sizes, Kapseln, Filterkaffee.
Relationships: Cappuccino —made from→ Signature Espresso + Milchschaum · Tall/Grande —contain→ 2 shots = 89,1 mg · Cappuccino —cheaper than→ Latte (3,90 vs 4,59) · Filterkaffee Grande —has more caffeine than→ Cappuccino · Pflanzendrink —adds→ 0,50–0,80 €.
Dedupe/parked: "starbucks cappuccino pulver/chilled coffee/edeka/rewe" → only capsule facts used (no verified product page); "angebot" → link to /blog/starbucks-kapseln-angebot.

## Information gain
1. 4-way table Cappuccino/Latte/Latte Macchiato/Flat White with price + kcal + build (competitors list only kcal).  2. Caffeine by size tied to Filterkaffee comparison.  3. Home recipe (HowTo).

## Internal links / cannibalisation
Links used: latte, flat-white, latte-macchiato, kaffee, preise, menu?(not used), groessen, kalorien-guide, iced-coffee, vegane-optionen, kapseln-angebot, app. Risk: /blog/starbucks-latte already has a Latte-vs-Cappuccino section → this page owns "cappuccino" head term; add inbound link from latte, kaffee, menu, preise, getraenke when publishing.

## FLAGS (need human)
- Competitor fetch: only SERP titles/snippets + 3 primary sources fetched; 4 full competitor extractions not done.
- Our own site prices disagree: menu.js 3,90 €; /blog/starbucks-getraenke says Cappuccino "ab 4,45 €"; third-party 5,20–6,20 €. Draft says "ab 3,90 €" and explains the spread. Please verify against the live app.
- Third-party nutrition: starbuckspreise.de shows Iced Cappuccino 72 kcal vs menu.js 106 kcal. Draft uses menu.js.
- No official Hafermilch kcal and no confirmation of laktosefreie Milch → not stated.
- Cappuccino caffeine is inferred (same shots as Latte), not read from a cappuccino row of the PDF.
- Hero image: TODO (Unsplash, no Starbucks branding), credit in post.json.
