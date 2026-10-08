# Research notes – starbucks koffeinfrei (2026-10-09)

## 1. Keyword, intent, SERP
- Primary: **starbucks koffeinfrei** · under the Trends threshold (Research_Oct2026, "New post (Oct 2026)", 6 autocomplete variants). The sheet's target cell says /blog/starbucks-fuer-kinder (copy error); written as its own page /blog/starbucks-koffeinfrei.
- Intent: know (which drinks have no caffeine, how much is left in decaf) + do (how to order). SERP via WebSearch is US-proxied: coffeeatthree.com, purewow.com, lifeboostcoffee.com, cookwithrome.com, tastingtable.com, cafe-merlin.de, Nespresso-capsule shops. No German page answers the query with German data. PAA not captured (no rendered SERP).
- Fan-out, Google Autocomplete hl=de gl=de, live 9 Oct 2026: starbucks koffeinfreier kaffee · koffeinfrei bestellen · koffeinfreie getränke · koffeinfrei kapseln · koffeinfrei espresso roast · hat starbucks koffeinfreien kaffee · nespresso koffeinfrei · kaffeebohnen koffeinfrei · frappuccino koffeinfrei · entkoffeinierter kaffee verfahren · entkoffeinierter espresso · getränke ohne koffein · eiskaffee ohne koffein · starbucks decaf drinks / menu / bohnen · starbucks schwangerschaft · chai latte starbucks schwangerschaft.

## 2. Head entities
| Entity | Type | sameAs | Facts |
|---|---|---|---|
| Entkoffeinierter Kaffee (Decaf) | Concept | de.wikipedia.org/wiki/Entkoffeinierung | KaffeeV: max 1 g caffeine per kg dry matter |
| Koffein | Concept | de.wikipedia.org/wiki/Coffein | EFSA 2015: 400 mg/day, 200 mg single dose, 200 mg/day pregnant |
| Starbucks | Organization | wikidata Q37158 | DE menu and nutrition list on starbucks.de |
| Decaf Espresso Roast | Product | – (unlinked) | bean on starbucks.de/de/menu-kaffeebohnen, pack says Dark Roast, 100 % Arabica |

## 3. Sources (fetched 9 Oct 2026)
| # | Source | Facts used |
|---|---|---|
| S1 | Nährwert-PDF „Autumn – 10.09.2026 (Getränke Nährwerte)“, relative link on starbucks.de/de/nutrition, 21 pages, pypdf → 2,204 rows parsed (name, size, kcal, sugar, caffeine) | 33 drink names with "Decaf". Decaf Espresso 1,8 mg (regular 44,5), Doppio 3,6 (89,1). Decaf Caffè Latte Short/Tall/Grande/Venti 1,8 / 3,6 / 3,6 / 5,4 (regular 44,5 / 89,1 / 89,1 / 133,6; same for every milk). Decaf Americano 1,8 / 3,6 / 5,4 / 7,2 (regular Grande 133,6). Decaf Cappuccino, Latte Macchiato, Caramel Macchiato, White Mocha, PSL Grande 3,6 (regular 89,1). Decaf Flat White Short 3,6 (89,1). Decaf Mocha Grande 27,9 (113,4). Decaf Coffee Frappuccino Grande 2,8 (31,4), Decaf Mocha Frappuccino 10,4 (37,9), Decaf Java Chip 12,0 (39,9). Decaf Iced Latte Grande 3,6, Decaf Iced Americano Grande 5,4. 0 mg in every size: Vanilla Cream, Caramel Cream, Strawberries & Cream, Cookies & Cream, Pumpkin Spice Cream Frappuccino, Mint Herbal Blend, Spiced Apple Tea. Classic Hot Chocolate 13,4 / 20,0 / 26,1 / 32,2; Signature Hot Chocolate Grande 28,6; Iced Chocolate Grande 26,0; Chocolate Cream Frappuccino Grande 10,3; Matcha Green Tea Latte Grande 83,0; Matcha Cream Frappuccino Grande 74,3; Chai Tea Latte Grande 52,4; Strawberry Acai / Mango Dragonfruit Refresha 3,7 / 4,9 / 6,2; Peach Iced Tea Grande 1,0; English Breakfast 102 (Venti 204); Earl Grey 1,1 and Emperor's Clouds & Mist 0,9 (implausibly low, not relied on, same call as /blog/starbucks-tee); Filterkaffee Grande 254,6; Cold Brew Grande 255,8. |
| S2 | Order menu starbucks.de/de/menu/drinks/hot-drinks (full menu JSON: 135 products) + 42 product pages /de/menu/product/<id> | bean options per drink ("beans": Signature Espresso / Blonde / Decaf, no price suffix; Frappuccinos: Decaf / Frappuccino Roast). Decaf selectable on 25 of 31 coffee drinks checked; none on Filterkaffee, Café Crème, Caffè Misto, Cold Brew, Cold Brew Latte; Java Chip only Frappuccino Roast. Soy Protein Drink +1,50 €, milks +0,00. Footnote "Der Koffeingehalt ist ungefährer Wert". Caffeine shown: Heiße Milch 0,0, Mint Blend Tea 0,0, Hibiscus Tea 0,0, White Hot Chocolate 0,0, but also Classic Hot Chocolate 0,0, Classic Iced Chocolate 0,0, Chocolate Cream Frappuccino 0,0 and English Breakfast 1,3 → the menu JSON is not reliable for caffeine (known: it still carries the Spring recipe). |
| S3 | starbucks.de/de/menu-kaffeebohnen | Decaf Espresso Roast description ("Entkoffeinierten Espresso Roast … samtig-weichen Geschmack … geröstetem Karamell und Kakao"); Espresso Roast = "Das Herzstück unserer Espresso-Getränke" |
| S4 | starbucks.de/de/menu-drinks-hot-teas | Hibiscus = "natürliche koffeinfreie Mischung" (Papaya, Mango, Zitronengras, Hibiskusblüten); Mint Blend = grüne Minze, Pfefferminze, Zitronenverbene; Youthberry contains white tea |
| S5 | starbucksfreiburg.de (Freiburg Hbf ordering page, no sizes) | Americano 3,50 · Iced Americano 3,50 · Caffè Latte 4,90 · Iced Caffè Latte 4,90 · Caffè Mocha 5,90 · Caramel Frappuccino 6,40 · teas 3,90 · Vanilla Cream 6,40 · Caramel Cream / Strawberries and Cream / Cookies and Cream 6,90 · Pumpkin Spice Cream 7,40 · Filterkaffee 3,00 · Cold Brew 4,40 · Classic Hot Chocolate 5,90. Heiße Milch not listed. |
| S6 | gesetze-im-internet.de KaffeeV 2001 | "entkoffeiniert": Röstkaffee with at most 1 g caffeine per kg Kaffeetrockenmasse |
| S7 | efsa.europa.eu/de/topics/topic/caffeine (opinion of 27 May 2015) | 200 mg single dose, 400 mg/day adults, 200 mg/day pregnant and breastfeeding, 3 mg/kg children and adolescents |
| S8 | bfr.bund.de FAQ on caffeine (Stand 05.01.2026) | same amounts; cocoa drink 8–35 mg per 200 ml |
| S9 | starbucksathome.com/de/produkte/blonde-espresso-decaf-roast-nespresso | Blonde Espresso Roast Decaf by Nespresso: 10 capsules, 100 % Arabica, intensity 6, "koffeinfrei", espresso 40 ml / lungo 110 ml |
| S10 | tastingtable.com/1821200 (Luna Regina, 4 Apr 2025) | second-hand: Starbucks does not name its process publicly; nutritionist Monica Reinagel reports the Direct Contact Method for most decaf, Swiss Water for two US products. US only. |

## 4. Competitors
| # | URL | Headings / what it has |
|---|---|---|
| C1 | coffeeatthree.com/starbucks-caffeine-free-drinks (Jee Choe, 2021/2022) | Caffeine-Free at Starbucks · Tips for Ordering · Drinks without Caffeine · Secret Menu · Questions: hot chocolate caffeine? mocha caffeine? decaf coffee caffeine? US menu; decaf shot "about 12 mg" |
| C2 | purewow.com/food/caffeine-free-starbucks-drinks (Taryn Pire, 2 Sep 2024) | list of 15 drinks incl. "Any Decaf Espresso Drink"; FAQ: Do Refreshers have caffeine? Pink Drink without caffeine? Best caffeine-free drink? No mg values |
| C3 | cafe-merlin.de/?p=6329 | 403 on fetch. Search snippet only: lists Matcha Latte and Chai Latte as "ohne Kaffee" (both contain caffeine) |
| C4 | cookwithrome.com (3 posts, search summary only) | decaf shot estimates 3–25 mg, half-caf, ask the barista |
| C5 | tastingtable.com (see S10) | decaf process |
- Per-heading extraction: C1/C2 are short list posts, terms recorded in the ledger below. None has German data, German prices, the order-menu bean option or the legal definition.

## 5. Entity ledger → entities.json
T1: Starbucks koffeinfrei, Decaf, entkoffeinierter Kaffee, Koffein, Decaf Espresso Roast, Getränke ohne Koffein, Bestellkarte, Starbucks Deutschland. T2: Caffè Latte, Caffè Americano, Cappuccino, Frappuccino / Cream Frappuccino, Kräutertee (Mint Blend, Hibiscus), Heiße Schokolade / Kakao, Refresha, Filterkaffee, Cold Brew, Eiskaffee, Preis, Kaffeeverordnung, Schwangerschaft, EFSA, Kapseln / Nespresso, Kaffeebohnen, Heiße Milch, Chai, Matcha. T3: Blonde, Direct Contact Method, Swiss Water, Spiced Apple Tea, Aerocano, Ristretto Mocha, Café Crème, Caffè Misto, White Hot Chocolate, BfR.
Relations: Decaf —is bean option of→ espresso drinks (25 of 31) · Decaf shot —has→ 1,8 mg (regular 44,5) · KaffeeV —caps→ 0,1 % caffeine · Decaf Mocha —keeps→ 27,9 mg from cocoa · Cream Frappuccino (5 flavours) —has→ 0 mg · Mint Blend / Hibiscus —are→ herbal, 0 mg · Filterkaffee / Cold Brew —have no→ decaf option · Decaf Americano —costs→ 3,50 € (Freiburg) · EFSA —sets→ 200 mg/day in pregnancy · Filterkaffee Grande —exceeds→ that amount (254,6 mg) · Blonde Espresso Roast Decaf by Nespresso —contains→ 10 capsules.
Dedupe / parked: half-caf (not verifiable for DE), Passion Tango / Mint Majesty / Peach Tranquility (US teas), Pink Drink (no DE value), Iced Brown Sugar Oat Shaken Espresso (in the nutrition list, not on the order menu; open "shaken espresso" merge), secret-menu drinks.

## 6. Information gain
(1) Regular-vs-decaf caffeine table from the official German list. (2) Which 25 of 31 order-menu drinks offer the Decaf bean. (3) The "hidden caffeine" table, including the order menu's 0,0 mg for hot chocolate against 26,1 mg in the nutrition list. (4) Share-of-200-mg table for pregnancy. (5) Decision table. (6) Inline chart.

## 7. Heading + keyword + question map
| Lvl | Heading | Phrase | Carries |
|---|---|---|---|
| H1 | Starbucks koffeinfrei: Decaf-Kaffee und alle Getränke ohne Koffein | starbucks koffeinfrei | focus |
| H2 | 1. Hat Starbucks koffeinfreien Kaffee? | hat starbucks koffeinfreien kaffee | Decaf Espresso Roast, Filterkaffee, Cold Brew |
| H2 | 2. Wie bestellst du koffeinfrei bei Starbucks? | koffeinfrei bestellen | Bestellkarte, bean option (HowTo) |
| H3 | Bei welchen Getränken kannst du Decaf wählen? | decaf drinks / menu | 25 of 31 |
| H2 | 3. Wie viel Koffein steckt in Decaf? | decaf koffeingehalt | 1,8 mg per shot, KaffeeV |
| H3 | Warum hat ein Decaf Mocha noch 27,9 mg Koffein? | – | Kakao |
| H2 | 4. Welche Starbucks Getränke sind ganz ohne Koffein? | getränke ohne koffein | teas, Heiße Milch, Cream Frappuccinos |
| H2 | 5. Welche Getränke enthalten Koffein, obwohl kein Kaffee drin ist? | – | hot chocolate, chai, matcha, Refresha |
| H2 | 6. Gibt es Frappuccino und Eiskaffee ohne Koffein? | frappuccino koffeinfrei, eiskaffee ohne koffein | |
| H2 | 7. Was kostet Decaf bei Starbucks? | preis | Freiburg prices |
| H2 | 8. Wie wird der Kaffee bei Starbucks entkoffeiniert? | entkoffeinierter kaffee verfahren | KaffeeV, Tasting Table |
| H2 | 9. Wie viel Koffein ist in der Schwangerschaft unbedenklich? | starbucks schwangerschaft | EFSA, BfR |
| H2 | 10. Gibt es Starbucks koffeinfrei als Kapseln und Bohnen? | koffeinfrei kapseln, kaffeebohnen koffeinfrei | Nespresso |
| H2 | 11. Welche koffeinfreie Bestellung passt zu dir? | – | decision table |

## 8. Internal links
Out: kaffeebohnen, groessen, americano, kalorien-guide, mocha, tee, fuer-kinder, heisse-schokolade, refresha, matcha-latte, frappuccino-sorten, cold-brew, iced-coffee, preise, app, kapseln-angebot, milchalternativen, getraenke. In (22): americano, kaffeebohnen, kapseln-angebot, tee, mocha, pumpkin-spice-latte, vanilla-latte, kaffee, matcha-latte, protein, kalorien-guide, fuer-kinder, cappuccino, cold-brew, iced-coffee, latte, groessen, preise, getraenke, menu, /iced-caramel-macchiato, hund. Published 9 Oct 2026, commit e513174. Cannibalisation: /blog/starbucks-fuer-kinder covers caffeine-free drinks for children (different intent); /blog/starbucks-tee owns tea; no page owned decaf.

## 9. Own-site contradictions found (NOT changed, for the owner)
- /blog/starbucks-heisse-schokolade and /blog/starbucks-fuer-kinder say Starbucks gives no caffeine value for hot chocolate ("nahe null"). The nutrition list gives 26,1 mg (Grande).
- /blog/starbucks-refresha says Starbucks Deutschland publishes no caffeine values for Refresha and compares with a "Grande Caffè Latte mit 150 mg". The list gives 4,9 mg for the Refresha and 89,1 mg for the latte.
- /blog/starbucks-frappuccino-sorten calls the Matcha Cream Frappuccino "die koffeinfreie, grüne Alternative". The list gives 74,3 mg (Grande).
- /blog/starbucks-in-der-naehe says the official site can filter for outdoor seating and accessibility; the store-feature API has four features only (WLAN, Drive-Through, mobile order, Rewards).
