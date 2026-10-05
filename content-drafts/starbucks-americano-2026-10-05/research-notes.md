# Research notes – starbucks americano (run 2026-10-05, calendar slot 2026-10-27)

## Intent / SERP (WebSearch, US-proxied, German queries, 5 Oct 2026)
- ~30/mo (Trends estimate ±50 %), evergreen. Intent: know (what is it, caffeine, calories) + know-simple (price). Calendar type "FAQ / short answer post"; written to the network standard (1.500+ words) instead.
- Organic: starbuckspreise.de Caffè-Americano page (thin, 3,10 €, 11 kcal), fddb (404 on fetch), koffeinhaltig.com, Wikipedia; generic explainers: nescafe.com, top-kaffee.de, k-fee.com, goodbean.coffee, hannoversche-kaffeemanufaktur.
- No rendered SERP (Chrome extension not connected) → PAA not captured.

## Head entities (Step 2)
- Caffè americano – Wikidata Q1152551; en.wikipedia (espresso + hot water, 1:3–1:4; naming: WWII G.I. story is popular belief, OED traces it to Central American Spanish "café americano", 1950s; long black = water first; iced americano).
- Starbucks – Wikidata Q37158.

## Competitors (Step 4)
| # | URL | Result |
|---|---|---|
| C1 | starbuckspreise.de/caffe-americano-kraftvoller-kaffee-ohne-schnickschnack | fetched – H: Was macht ihn besonders / Preis und Nährwerte / Für wen / Fazit; 3,10 €, 44 kJ / 11 kcal; no sizes, no caffeine, no FAQ |
| C2 | nescafe.com/de … was-ist-ein-americano | fetched – ratio 1/2:1/2 or 1/3:2/3, WWII origin, vs Filterkaffee, vs Long Black |
| C3 | top-kaffee.de/kaffee-americano | fetched – ratio 1:2–4, double espresso 45–60 ml + 60–120 ml, FAQ (Lungo? Wasser? stärker als Filter? Long Black? kalt?) |
| C4 | k-fee.com blog (Schümli, Café Crema, Americano, Lungo) | fetched – Americano 100–180 ml, wenig Crema; Lungo doppelte Wassermenge, Überextraktion; Long Black Crema bleibt |
| – | speisekartemenus.de/starbucks-preise | fetched (curl) – Americano 3,39/3,89/4,39 €; Iced 3,39/3,79/4,39 € |
| – | fddb.info | 404 – skipped |

## Fact ledger
| Fact | Source |
|---|---|
| Americano Short/Tall/Grande/Venti: 4/7/11/14 kcal; 44,5/89,1/133,6/178,2 mg; Grande 0,2 g Fett, 0,1 g Zucker | Nährwert-PDF Getränke, Starbucks DE, 10.09.2026 (downloaded 5 Oct, pypdf) |
| Iced Americano Tall/Grande/Venti same values, no Short | PDF |
| Blonde Americano Grande 128,2 mg / 9 kcal; Decaf 5,4 mg / 11 kcal; Blonde Caramel Protein Americano Grande 100 kcal, 16,4 g protein | PDF |
| Espresso single 44,5 mg; Filterkaffee Grande 254,6 mg / 31 kcal; Cold Brew 255,8 / 22; Cappuccino Grande 89,1 / 130, 9,4 g protein; Caffè Latte 89,1 / 151 | PDF (+ cold-brew notes) |
| Shots per size 1/2/3/4 | derived from caffeine ÷ 44,5 mg – FLAG derived (site already states 3 shots Grande) |
| "Die mit heißem Wasser übergossenen Espresso-Shots bilden eine leichte Crema-Schicht …" | starbucks.de/de/menu-drinks-hot-coffees (fetched 5 Oct) |
| Iced: "Kräftiger Espresso mit gefiltertem Wasser und Eiswürfeln" | starbucks.de/de/menu-drinks-iced-coffees |
| Freiburg Hbf: Caffè Americano 3,50 €, Iced 3,50 €, Caffè Latte 4,90 €, Filterkaffee 3,00 € (size not stated) | starbucksfreiburg.de (fetched 5 Oct) |
| Price spans Tall 3,10–3,85 / Grande 3,60–4,35 / Venti 4,10–4,75 | /blog/starbucks-preise (3,10/3,60/4,10), /blog/starbucks-getraenke (3,85/4,35/4,75), speisekartemenus – own pages contradict each other – FLAG |
| Extra-Shot +0,80 € | /blog/starbucks-preise |
| Sizes 237/354/473/591 ml | /blog/starbucks-preise |
| EFSA 400 mg/day | not fetched this run (same flag as cold-brew) – FLAG light |
| Café Crème on DE menu | coffee-drinks notes 26 Sep |

## Tiers / relationships
T1: Starbucks Americano / Caffè Americano, Espresso, heißes Wasser, Koffein, Preis, Kalorien, Shots. T2: Iced Americano, Filterkaffee, Long Black, Lungo, Blonde, Decaf, Größen, Crema, Verhältnis, Rezept, Extra-Shot. T3: Café Crème, Caramel Protein Americano, EFSA, OED/WWII.
- Americano = Espresso + heißes Wasser · Grande —enthält→ 3 Shots → 133,6 mg · Filterkaffee Grande —hat→ 254,6 mg (fast doppelt) · Iced Americano —gleiche Werte wie→ heiß · Long Black —Wasser zuerst→ Crema bleibt.

## Information gain
No competitor gives German per-size caffeine/shots, variants (Blonde/Decaf) or a price span. Original: (1) shots/caffeine/kcal table per size from the official DE PDF, (2) caffeine ranking table that corrects "Americano = strongest", (3) preparation comparison table.

## Heading map
H1 Starbucks Americano: Preis, Koffein, Kalorien und Shots pro Größe (2026) · H2 1 Was ist ein Starbucks Americano? (H3 Name / Shots) · 2 Was kostet ein Americano? (H3 günstigstes Getränk?) · 3 Wie viel Koffein? (H3 stärker als Filterkaffee?) · 4 Wie viele Kalorien? · 5 Americano vs Iced Americano · 6 Welche Varianten? (H3 anpassen) · 7 Americano, Lungo oder Long Black · 8 Zu Hause (HowTo)

## Internal links / cannibalisation
Out: groessen, preise, cold-brew, sirup, kalorien-guide, iced-coffee, protein, milchalternativen, kaffee, kapseln-angebot. In: getraenke, kaffee, preise, iced-coffee, cold-brew, kalorien-guide, menu. Cannibalisation: /blog/starbucks-iced-coffee treats Iced Americano as the DE substitute for Iced Coffee; this page owns "americano" and links back.

## FAQ source map
verdünnter Espresso (C2/C3) · mehr Koffein als Latte (PDF) · vegan (fan-out) · Zucker (PDF) · entkoffeiniert (C4 heading "entkoffeiniert?") · Blonde (PDF) · Venti Iced (PDF) · Short (PDF) · gesünder als Cappuccino (fan-out) · Sterne (AGB) · Café Crème (C4).
