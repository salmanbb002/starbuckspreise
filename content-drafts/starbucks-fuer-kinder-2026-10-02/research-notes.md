# Research notes – starbucks kinder (run 2026-10-02, planned publish 2026-10-14)

## Intent / SERP
- ~70/mo (Research_Oct2026; evergreen, Trends peak 13–19 Sep 2026). Mixed intent: kids' drinks (know/do), plus viral "kinder bueno" and noise ("kinderarbeit" – parked, different intent/YMYL-reputation topic, not covered).
- Autocomplete (9): kinder bueno, kinder bueno drink/frappe/latte, kinder drink, kinderarbeit, kinderbecher, kindergetränke.
- SERP is dominated by US/UK pages: tastingtable.com, homegrounds.co, roastycoffee.com, coffeenearyou.com, chicagoparent.com, lonaslileats.com, danielle-moss.com (titles via WebSearch; not fetched). German SERP: babyccino recipe pages (utopia.de, cafedujour.de, greenplantation.de, cafe-merlin.de). **No German Starbucks-kids page found → real information gap for DE.**

## Head entities / sources
- starbucks.de Frappuccino page (fetched 2 Oct 2026): Cream Frappuccino descriptions; page has no kids menu/hot chocolate/juice.
- starbucks.de hot-coffees page (fetched 2 Oct): no kids section.
- Kinder Bueno viral recipe: tastingtable.com, marieclaire.co.uk, twistedfood.co.uk (search snippets: Grande iced latte, 2 pumps white mocha, 2 hazelnut, chocolate cream cold foam) – UK/US, not DE.
- Babyccino: US pages (steamed milk + extra foam, kids size) + DE pages (utopia, cafedujour) – DE Starbucks availability NOT verified.

## Fact ledger
| Fact | Source |
|---|---|
| Cream Frappuccino prices/kcal (Strawberries 4,79/310; Vanilla 5,35/290; Chocolate 4,85/322; Java Chip 5,35/403) | menu.js lines 92–104 |
| Classic Hot Chocolate 4,99/309; Signature 6,40/350; White 6,40/357; Hot Milk 8,50/203 | menu.js lines 107–119 |
| Apfelschorle 0,5 l 1,60/115; Volvic 0,25; Adelholzener Sprudel 0,15; Cake Pop Polar 2,80/164; Blaubeer Muffin 3,80/415 | menu.js |
| Chai Tea Latte 52 mg; Iced Matcha 85 mg; Teavana up to 102 mg; Coffee Frappuccino 31,4 mg | /blog/starbucks-getraenke, -kaffee (Nährwert-PDF 10 Sep 2026) |
| Refresha: green coffee extract caffeine, no DE value | /blog/starbucks-refresha |
| Hot chocolate caffeine ≈ 0, no exact value | /blog/starbucks-heisse-schokolade |
| sizes Tall 354 ml, Short 237 ml (some hot espresso drinks only) | /blog/starbucks-groessen-tall-grande-venti |
| Sirup-Shot +0,60–0,80 € | /blog/starbucks-getraenke |

## Tiers / relationships
T1: Kinder, Starbucks, Koffein, Cream Frappuccino, Hot Chocolate, Kalorien, Preis. T2: Babyccino, Kinder Bueno, Refresha, Chai, Matcha, Apfelschorle, Hot Milk, Cake Pop, Kinderarzt, Allergene, Zucker.
Relations: Cream Frappuccino —has→ no coffee · Chocolate Cream —made with→ Mocha-Sauce —contains→ trace caffeine from cocoa · Refresha —contains→ green-coffee caffeine · Chai/Matcha —contain→ tea caffeine · Kinder Bueno drink —needs→ espresso (original) · Hot Chocolate —≈0→ caffeine.

## Information gain
1. Caffeine-trap table (drinks that don't taste like coffee but contain caffeine).  2. Worked cost example for a visit with two children (9,39 € / 588 kcal).  3. Decision table with caffeine column. DE-specific, which US/UK pages can't give.

## Internal links
frappuccino-sorten, heisse-schokolade, refresha, cappuccino (new), vegane-optionen, gebaeck, fruehstueck, app, angebote, kalorien-guide, becher. Cannibalisation: none direct; /blog/starbucks-refresha and /blog/starbucks-heisse-schokolade stay owners of their topics.

## FLAGS (need human)
- YMYL (children): no medical statement is made; the draft defers to the Kinderarzt. Have a human review the wording around caffeine and kids before publishing.
- Babyccino availability in DE filialen unverified; Kinder Bueno recipe is third-party/UK/US and contains espresso.
- Hot Milk 8,50 € in menu.js looks like a data error – flagged in the draft ("vor Ort prüfen"); please check and fix menu.js.
- "Kinderbecher": no evidence of a kids' cup range was checked; draft says so.
- Chai/Matcha Cream Frappuccino caffeine: inferred from tea, no official value.
- Sugar (g) values not available from the sources used → only kcal given.
- "Keine Kinderkarte" rests on two starbucks.de pages (Frappuccino, hot coffees); a menu-wide check is worth doing.
- Hero image TODO.
