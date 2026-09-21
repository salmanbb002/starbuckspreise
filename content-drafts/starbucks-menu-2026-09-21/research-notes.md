# Research notes — "starbucks menu" (StarbucksPreise, de-DE) — 2026-09-21

Source of the keyword: `Starbucks Keyword Strategy - Clusters, Topical Map, Content Calendar.xlsx` — `starbucks menu`, 4,400/mo, KD 30, Navigational+Transactional, Priority High, cluster *Menu & Product Range* / pillar *Speisekarte & Menü*, "Dedicated page (pillar/hub-level)", calendar slot 2026-09-22, planned URL `/menu/starbucks-menu` (published as `/blog/starbucks-menu`, matching how `starbucks-getraenke` was shipped). Merged variants: starbuck.menu, starbucks menü, starbuck menu, starbuks menu, menu starbucks, starbukes menu, starbcuks menu. Cluster hub also absorbs (Merge-Recommended): starbucks menue, starbucks speisekarte, starbuck karte, starbucks sortiment, starbucks frühstück, starbucks kalte getränke, starbucks menu of drinks, starbucks sorten, starbucks produkte, starbucks deutschland menü, starbucks germany menu.

## 1. Intent + SERP
- **Dominant intent:** *know* (broad research) with navigational/transactional colour — searcher wants "what is on the Starbucks menu in Germany, roughly what does it cost". Secondary: *website* (find the official menu).
- **Top organic results (WebSearch, US-side proxy, 3 queries):** starbuckspreise.de (competitor, different domain from ours), fastfoodpreis-info.de, germanmenus.de (403), burgerspreises.de, speisekartemenus.de, allmenupreis.de, fastfoodpreiseinfo.de, fastfoodsmenu.com, menupricetoday.com, despeisekartes.org, starbucks.de (official menu pages), Uber Eats store pages (403).
- **Page types:** almost all are *price-list pages* (table of every product + price). None is a true navigational hub explaining the menu structure.
- **SERP features:** could not observe a rendered German SERP (WebSearch is text-only, US-side). PAA / autocomplete **not directly captured** — fan-out was built from the keyword sheet's cluster keywords + competitor FAQ blocks. **Needs a manual check in a real German browser.**
- **Query fan-out (from keyword sheet):** getränke, karte, drinks, speisekarte, produkte, germany menu, getränkeliste, getränkekarte, deutschland menü, sortiment, frühstück, kalte getränke, sorten.

## 2. Head-entity research
| entity | source | facts used |
|---|---|---|
| Starbucks (Q37158) | de.wikipedia.org/wiki/Starbucks | first store April 1971 Pike Place, Seattle (Baldwin/Bowker/Siegl); Germany: first stores May 2002 in Berlin; operator AmRest Coffee Deutschland (formerly Starbucks Coffee Deutschland GmbH until April 2016) |
| AmRest | food-service.de (2024-07-05) | "seit 2016 mit der Marke in Deutschland vertreten", "auf Lizenzbasis", "Master-Franchiser für Starbucks in Deutschland" |
| Starbucks menu (official structure) | starbucks.de `/de/menu`, `/en/menu-drinks-categories`, `/de/menu-drinks-hot-coffees` | Getränke: Highlights, Hot Coffees, Hot Chocolates, Hot Teas, Iced Coffees, Iced Chocolates, Refresha®, Iced Teas, Frappuccinos, Bottled Drinks. Essen: Frühstück & Gebäck, Bakery, Sandwiches, Snacks & Leckereien. To Go: Verpackung. Hot Coffees = 14 items (list in draft). **No prices on any of the 3 pages fetched.** |
| Starbucks Rewards / App | starbucks.de/en/app | 3 stars per €, 150 stars = free drink, 450 = Gold (extra shots/syrup/whipped cream, free brewed coffee/tea refill, birthday drink). Order-ahead **not** mentioned on that page. |
| Reusable cup | starbucks.de/de/article/491 | green reusable cup, 2,50 € Pfand; own white reusable cup or personal tumbler accepted. No discount amount stated there. |
| Uber Eats | uber.com/de/newsroom (2021-12-07) | launch Frankfurt, Hamburg, München, 14 stores |
| Stores | own page `starbucks-deutschland-filialen` | 179 (1 July 2026, ScrapeHero), 77 cities |

## 3. Titles (competitors)
- starbuckspreise.de: "Starbucks Preise 2026 - Starbucks Menu & speisekarte Preis" (no date shown)
- fastfoodpreis-info.de: "Starbucks Preise Deutschland 2026: Aktuelle Menü-Preisliste"
- speisekartemenus.de: "Starbucks Preise in Deutschland – 2026 Aktuelle Preisliste" (published 2026-03-04)
- fastfoodsmenu.com: "Preise auf der Speisekarte von Starbucks in Deutschland" (published 2026-05-09)
- burgerspreises.de, germanmenus.de (403), Uber Eats (403): not fetched. Substituted: 4 distinct domains fetched successfully (starbuckspreise.de, fastfoodpreis-info.de, speisekartemenus.de, fastfoodsmenu.com).

**Chosen:** Title tag "Starbucks Menu 2026: Die komplette Karte für Deutschland" (55 chars). H1 "Starbucks Menu Deutschland: Die komplette Karte mit Getränken, Food & Preisspannen". Slug `starbucks-menu`. Alternates: "Starbucks Menü Deutschland 2026: Karte, Getränke & Essen"; "Starbucks Speisekarte 2026: Alle Kategorien im Überblick". (The fetched competitors don't lead with "Menu" before "Preise" — the hub angle is "Karte/Aufbau", not "Preisliste".)

## 4/5. Competitor structure + extraction (headings kept as written)
**A. starbuckspreise.de** — H2: Starbucks Preise Deutschland 2026 · Starbucks Getränke liste Preise (Hot Espresso Drinks, Iced Espresso Drinks, Filterkaffee, Hot Teavana Tea, Iced Teavana Tea, Starbucks Refresha®, Frappuccino® Blended Beverages, Schokolade & Milch) · Essen Starbucks Menü Preis 2026 (Desserts, Sandwiches, Snacks & Süße) · Flaschengetränke · To Go – Verpackung · Kaffee zu Hause – Kaffeebohnen · Merchandise (Mehrwegbecher, Tassen, Becher, Stabfilterkanne, Sonstiges) · Starbucks Menü Deutschland: Preise, Highlights & Tipps · FAQ (29 Q, verbatim in source). Sample items: Caffè Latte 4,59 €, Cappuccino 3,90 € (later Tall–Venti 5,20–6,20 €), Espresso 2,75 €, Tiramisu Frappuccino 8,50 €, Hot Milk 8,50 €(!), Breakfast Combo 6,50 €. Price data internally inconsistent → **not used for numbers**.
**B. speisekartemenus.de** — H2: Starbucks Preise Deutschland · Was gibt's Neues · Starbucks Angebote Speisekarte · Die Geschichte von Starbucks in Deutschland · Alternativen. H3: Menü – Beliebte Gerichte, getränke & kaffee, Hot Chocolate, Teavana Hot Tea, Chai/Matcha, Frappuccino, Iced Tea, American Bakery, Sandwiches, Sirup, Whole Bean, Kapseln, Packaged Food, Nährwerte, öffnungszeiten, In Der Nähe. FAQ 5 Q (Espresso 2,50 €, Preisliste, beliebteste, günstig, essen).
**C. fastfoodpreis-info.de** — H2: Menü Preise · Heiße Espresso-Getränke · Iced Coffee und Cold Drinks · Frappuccino · Heiße Schokolade & Tee · Snacks & Desserts · Sandwiches & Frühstück · Flaschengetränke & Kaffee für Zuhause · Nährwerte · Allergene · Standorte · Öffnungszeiten · Video · Häufige Fragen · Fazit. FAQ (verbatim): Eggnog Latte; Wie viele Starbucks gibt es in Deutschland? (>160); Gibt es Starbucks in Deutschland?; (2 off-language Qs); Wie bekomme ich kostenlose Nachfüllungen bei Starbucks? Published 2026-03-04.
**D. fastfoodsmenu.com** — H2: Bundles · Summer Specials Drinks/Food · Espresso Beverages · Hot Chocolate · Chai/Matcha · Hot Teavana Tea · Frappuccino · Iced Teavana Tea · Refresha · Desserts · Sandwiches · Ofenfrische Backwaren · Snacks & Süßes · Merchandise · beliebteste Produkte · Öffnungszeiten · Alternativen · FAQ (9 Q: Filialen 181, Zahlungsmöglichkeiten, Lieferservice, vegan, App, Drive-Thru, Preise gleich?, Frühstück, reservieren). Published 2026-05-09.

Entity/term extraction per heading is folded into `entities.json` (competitor_count = number of the 4 fetched pages using the concept in a heading). Full per-heading term dumps were not written out: competitor pages are product-price lists (hundreds of product names) — the ledger keeps the concept level and lists product examples per section instead.

## 6. Entity ledger — see `entities.json` (33 rows; T1 16 / T2 10 / T3 7)
**Relationships (10-20 triples), stated in the draft:**
- Starbucks —opened first German stores in→ Berlin, May 2002
- AmRest Coffee Deutschland —operates (licence, master franchiser)→ Starbucks Germany since April 2016
- Starbucks Germany —has→ ~179 Filialen / 77 Städte (1 July 2026)
- Starbucks Menü —splits into→ Getränke / Essen / To Go / Highlights
- Getränke —contain→ Hot Coffees (14), Iced Coffees, Hot/Iced Teas, Hot/Iced Chocolates, Refresha®, Frappuccinos, Bottled Drinks
- Frappuccino® —is→ blended ice drink (Coffee vs Cream base); Frappuccino —is priciest→ Dauerkarte drink group (5,40–7,20 €)
- Cold Brew —is extracted→ ~20 h cold, säurearm
- Refresha® —contains→ fruit juice + green-coffee extract
- Größe (Tall/Grande/Venti) —adds→ ~0,50 € per step (own price page); Venti = 591 ml hot / 709 ml iced
- Pflanzliche Milch —costs→ +0,50–0,80 €
- Bahnhof/Flughafen —adds→ ~10–15 % (own price page)
- starbucks.de —publishes→ no prices on menu pages
- Uber Eats —delivers Starbucks since→ Dec 2021 (Frankfurt, Hamburg, München)
- Starbucks App —awards→ 3 stars/€; 150 stars → free drink
- Saisonale Highlights —rotate→ PSL / Toffee Nut / Lebkuchen (autumn-winter)

**Section pools** (→ H2): Menü-Struktur (Starbucks, Menü, Highlights, Filialen, AmRest) · Getränke (heiße Kaffees, Iced/Cold Brew, Refresha, Frappuccino, Tee/Chai/Matcha/Schokolade, saisonal) · Essen (Frühstück, Bakery/Kuchen, Sandwiches, Snacks) · Mehr als Getränke (Bottled, Bohnen, Merch/Becher) · Preise (Preisspannen, Größen, Extras, Standort) · Entscheidungshilfe (Kalorien, vegan) · Bestellen (App/Rewards, Uber Eats, Drive-Thru, Öffnungszeiten).

**Heading keyword set** — (a) focus + close variants: starbucks menu / menü / karte / speisekarte (H1, direct answer, first H2). (b) LSI per H2: getränke, essen/frühstück, sortiment/flaschengetränke/bohnen, preise, entscheidung, bestellen. Sub-phrase for `starbucks getränkekarte`, `starbucks kalte getränke` handled as H3s; `starbucks getränke` itself deliberately **not** an H2 (owned by `/blog/starbucks-getraenke`).

**Dedupe / parked log**
- Duplicates merged: starbucks menu = menü = menue = karte = speisekarte = sortiment = produkte (one hub).
- Parked (with reason): *Eggnog Latte, Snack Mints, Gold Coin, Kapseln, Sirup-Preise, Allergene, Gründer/Geschichte (1971)* — single-source, no menu-hub value or own topic; *Öffnungszeiten* and *Standorte* are T1 by count but sister intents (`/blog/starbucks-geoeffnet`, `/blog/starbucks-deutschland-filialen`) → one-sentence attribute + link only; *Merchandise price list (27 items)* → `/blog/starbucks-tassen`, `/blog/starbucks-becher`; *Nährwerte table* → `/blog/starbucks-kalorien-guide` (decision-table row + 2 values only); *Bundles, Breakfast Combo 6,50 €, Starbucks Card 5 €* → single third-party claims, unverified; *Kostenlose Nachfüllungen FAQ* → US-centric, only Gold-tier refill statement kept (starbucks.de).

## 7. Information gain
All 4 competitors: are flat price lists; none explains **how the menu is structured** (official categories), none has a decision aid, and all present unsourced, mutually contradicting prices (e.g. Cappuccino 3,90 € vs 5,20–6,20 € **on the same page**; Hot Milk 8,50 €; PSL 6,20 € vs 6,40–7,50 €), none states that starbucks.de publishes no prices. Stale/undated: A (no date), B (2026-03-04 — pre-autumn), D (2026-05-09 — summer specials).
**Elements added:** (1) *Menü-Landkarte* (official category → examples → price band → detail article), (2) *Entscheidungshilfe* table ("Ich möchte … → Kategorie → Beispiel"), (3) transparent note on why lists disagree + "starbucks.de shows no prices".

## 8. Heading + keyword + question map
| H | heading | owns | question | entities / relationships |
|---|---|---|---|---|
| H1 | Starbucks Menu Deutschland: Die komplette Karte … | starbucks menu (+menü/karte) | Was steht auf der Karte? | Starbucks, Menü |
| H2-1 | Was steht auf dem Starbucks Menu in Deutschland? | menü aufbau / karte | Wie ist die Karte aufgebaut? | official categories |
| H3 | Die Menü-Landkarte … | speisekarte kategorien | Welche Kategorien gibt es? | all T1 categories + price bands |
| H3 | Wie unterscheidet sich die Karte je nach Filiale? | — | Ist überall dasselbe? | Standortpreise |
| H2-2 | Welche Getränke gibt es bei Starbucks? | getränke, drinks | Welche Getränke? | Getränke → categories |
| H3 ×5 | Hot Coffees (14) · Kalte Getränke · Frappuccino® · Tee/Chai/Matcha/Schokolade · Saisonale Highlights | kalte getränke, getränkekarte | … | per category |
| H2-3 | Was gibt es bei Starbucks zu essen? | frühstück, essen | Was gibt's zu essen? | Bakery, Sandwiches, Snacks |
| H3 ×3 | Frühstück & Gebäck · Sandwiches · Kuchen, Desserts, Snacks | | | |
| H2-4 | Gibt es bei Starbucks noch mehr als Getränke und Essen? | sortiment, produkte | Was gibt's noch? | Bottled, Bohnen, Merch |
| H3 ×2 | Flaschengetränke & Bohnen · Becher/Tassen | | | |
| H2-5 | Was kostet das Starbucks Menu? | preise (links to /starbucks-preise) | Wie teuer? | Preisspannen |
| H3 ×2 | Warum widersprechen sich Preislisten? · Größen und Extras | | | Größen, Pflanzenmilch |
| H2-6 | Was passt zu mir? Entscheidungshilfe | sorten | Was bestelle ich? | info-gain table |
| H2-7 | Wie bestelle ich vom Starbucks Menu? | bestellen | Filiale/App/Lieferdienst? | Rewards, Uber Eats, Drive-Thru |
| H3 ×2 | In der Filiale und per App · Per Lieferdienst | | | |
| H2-8 | FAQ (13) | | | |

## 8e. Internal links / cannibalisation
- **Cannibalisation:** `/blog/starbucks-getraenke` (target: starbucks getränke, getränkekarte, drinks) and `/blog/starbucks-preise` (Starbucks Preise) already exist. The hub deliberately **does not** reproduce their price tables — it shows one 7-row category band table and links out. `starbucks-essen.html` is a Essen (city) page, not food — do not link it for food. → Recommendation: keep the hub as the "Speisekarte & Menü" pillar, the two siblings as spokes (matches the Topical_Map: "Central menu hub … Links out to Preise and Getränke im Detail pillars").
- **Links used (from the draft):** getraenke, preise, frappuccino-sorten, kaffee, latte-macchiato, vegane-optionen, groessen-tall-grande-venti, tassen, becher, in-der-naehe, geoeffnet, kalorien-guide.
- **Inbound links added:** `starbucks-getraenke.html` ("Starbucks Menü" now → hub, was `/#menu`) and `starbucks-preise.html` (new sentence). `starbucks-getraenke.html` already had a BreadcrumbList item pointing at `/starbucks-menu/` — that URL now resolves.
- **Candidate follow-up spokes** (not written): `starbucks essen` / Frühstück page, `starbucks kalte getränke`, `starbucks sortiment`.

## FAQ source map
Filialen (fastfoodpreis-info + fastfoodsmenu FAQ, answer from own page) · Wer betreibt (Wikipedia + food-service) · Offizielle Preisliste? (gap: no competitor states this) · Preise überall gleich? (fastfoodsmenu FAQ) · Frappuccino vs Iced Coffee (gap) · vegan (fastfoodsmenu FAQ) · Frühstück (fastfoodsmenu FAQ) · Uber Eats (fastfoodsmenu FAQ, dated via uber.com) · Drive-Thru (fastfoodsmenu FAQ, own page) · Rewards (starbucks.de/app) · Pumpkin Spice Latte (fastfoodpreis-info FAQ "ab September" + news) · eigener Becher (starbucks.de) · Kaffeebohnen (own page + 2 competitors).
