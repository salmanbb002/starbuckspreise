# Research notes – starbucks halloween (2026-10-07)

## 1. Keyword, intent, SERP
- Primary: **starbucks halloween** · ~200/mo (Research_Oct2026, Trends-based ±50 %, seasonal, peak 30 Aug–5 Sep 2026). Sheet decision was "Merge into becher-aktuell"; owner asked for a standalone post on 7 Oct 2026.
- Intent: know + buy (cups). Secondary: visit-in-person (opening on 31 Oct).
- SERP (WebSearch, US-proxied; no rendered DE SERP because the Chrome extension was not connected): eBay.de, Kleinanzeigen, Disney Store, Yahoo/Woman's World, about.starbucks.com, sheknows, passionatepennypincher. No German editorial page ranks → gap.
- Fan-out (Autocomplete_Oct2026, hl=de, 29 Sep 2026): starbucks halloween 2026 / 2026 cups / 2026 deutschland / 2026 tasse / becher / becher 2026 / merch / merch 2026 / tasse / tumbler halloween.
- PAA: not captured.

## 2. Head entities
| Entity | Type | sameAs | Facts |
|---|---|---|---|
| Halloween | Event | de.wikipedia.org/wiki/Halloween | 31 Oct; 2026 = Saturday |
| Starbucks (DE, operated by AmRest) | Organization | wikidata Q37158 | seasonal menu at starbucks.de/de/menu/featured |
| Reformationstag | Event | de.wikipedia.org/wiki/Reformationstag | public holiday 31 Oct in BB, HB, HH, MV, NI, SN, ST, SH, TH |

## 3. Sources (fetched 7 Oct 2026)
| # | Source | How | Facts used |
|---|---|---|---|
| S1 | starbucks.de/de/menu/featured | curl | 20 featured products incl. Mystery Black Cat Swirl, Cake Pop - Mystery Black Cat, 8 pumpkin drinks, Pecan Maple, Apple Crumble |
| S2 | starbucks.de/de/menu/product/417669 | curl, RSC JSON | Swirl: description, 140 g, 473 kcal, fat 20,2 g, carbs 62,4 g, sugar 21,8 g, protein 7,8 g; no dietary labels |
| S3 | starbucks.de/de/menu/product/417609 | curl, RSC JSON | Cake Pop: description, 35 g, 154 kcal, fat 8,1 g, carbs 19,0 g, sugar 15,0 g; no dietary labels |
| S4 | starbucksfreiburg.de | curl | Prices: Swirl 4,20 €, Cake Pop Black Cat 2,80 €, Cake Pop Pumpkin 2,80 €, PSL 6,20 €, PS Caramel Macchiato 6,40 €, Pecan Maple Macchiato 6,40 €, PS Matcha Latte 7,20 €, Iced Apple Crumble Cream Matcha 7,20 €, PS Frappuccino 7,40 €, Chocolate Cream Frappuccino 6,40 €, Apple Crumble Cinnamon Roll 4,20 € |
| S5 | starbucks.co.uk/merchandise/autumn-2026 | curl | Halloween pieces + sizes; "For a limited time only, while stocks last. Range availability may vary by store." |
| S6 | about.starbucks.com/stories/2026/black-cat-frappuccino-… (14 Sep 2026) | headless Chrome (curl/WebFetch 403) | Black Cat Frappuccino + Venti Black Night Cookie from 22 Oct, select U.S. coffeehouses; merch from 15 Sep: mug $19.95, cauldron mug 14 oz $16.95, glow cold cup $29.95, Bearista charm $14.95 |
| S7 | about.starbucks.com/stories/2026/starbucks-holiday-menu-is-coming-to-town-nov-5 (5 Oct 2026) | headless Chrome | US holiday start 5 Nov 2026 |
| S8 | /blog/starbucks-weihnachten, /blog/starbucks-becher-aktuell (own) | repo | DE holiday start 4 Nov 2024 / 6 Nov 2025; Peanuts from 15 Sep 2026 |
| S9 | starbucks.de/de/menu-merchandise-core | curl | core range only; /de/merchandise/autumn-2026 → 404 |

## 4. Competitors (all US)
| # | URL | Date | Headings |
|---|---|---|---|
| C1 | about.starbucks.com (S6) | 14 Sep 2026 | item list, no H2s |
| C2 | sheknows.com/…/starbucks-black-cat-cup-release-date | 15 Sep 2026 | When does it drop · How to get it · How much · What else is in the collection · Black Cat Frappuccino |
| C3 | passionatepennypincher.com/starbucks-fall-halloween-cups | 15 Sep 2026 | 2026 Fall Cups · 2026 Halloween Cups · Peanuts line |
| C4 | shopping.yahoo.com (Woman's World) | 15 Sep 2026 | What's included · Release dates · Dupes (Dollar Tree, Kohl's, Amazon) |
- thestreet.com → 403, then empty body in headless Chrome; not used.
- Extraction (shuffled): glow-in-the-dark, cauldron, Bearista, plush bag charm, select coffeehouses, while supplies last, pumpkin-shaped, Snoopy, Peanuts, PSL, dupes, $29.95, $19.95, $16.95, $14.95, Sept. 15, Oct. 22.

## 5. Entity ledger → entities.json
T1: Starbucks Halloween, Starbucks Deutschland, Halloween-Becher, Black Cat Frappuccino, Mystery Black Cat Swirl, Cake Pop Mystery Black Cat. T2: Herbstkollektion, Venti Black Night Cookie, Black-Cat-Kollektion, Pumpkin Spice Latte, Peanuts, Bearista, Reformationstag, Weihnachtskarte, Preis, Kalorien. T3: Wiederverkauf, Allerheiligen, Dupes (parked: US retailers).
Relations: Starbucks DE —sells→ Swirl (4,20 €, 473 kcal) · Starbucks DE —sells→ Cake Pop (2,80 €, 154 kcal) · Black Cat Frappuccino —available→ USA only, 22 Oct · Halloween cups EU —part of→ Autumn 2026 · US collection —starts→ 15 Sep · 31 Oct 2026 —is→ Saturday + Reformationstag in 9 Länder · Halloween range —ends→ holiday menu (DE early Nov; US 5 Nov).

## 6. Information gain
All four competitors are US-only. This piece adds the German menu items with nutrition and price, the DE vs. USA table, and the holiday/opening question.

## 7. Outline → see draft H2 1–9. Internal links
becher-aktuell, gebaeck, pumpkin-spice-latte, frappuccino-sorten, weihnachten, geoeffnet, becher, groessen, fuer-kinder, vegane-optionen, angebote. Inbound added from gebaeck + becher-aktuell. Cannibalisation: becher-aktuell §2 covers the autumn cups; this page owns "halloween" and links back for the full cup calendar.
