# Research notes – starbucks cold brew (run 2026-10-03, planned publish 2026-10-20)

## Intent / SERP (google.de, hl=de, gl=de, 3 Oct 2026, via browser)
- ~50/mo (Research_Oct2026, Trends estimate ±50 %). Intent: know (what/price/caffeine) + secondary do (recipe) + buy (concentrate/beans).
- Organic: 1 starbucks.de Iced-Coffees page · 2 starbucks.com Cold Brew (EN) · 3 amazon.de search · 4 starbucksathome.com Cold-Brew French-Press guide · 5 nutriscan.app (calories) · 6 starbucks.de product 106865 · 7 reddit r/Coffee · 8 YouTube.
- SERP features: image pack, Google Shopping (concentrates, 26,97 € PSL concentrate import), PAA, related searches. No featured snippet.
- PAA: Was ist der Unterschied zwischen Iced Coffee und Cold Brew? · Gibt es bei Starbucks kalten Kaffee? · Was ist das Besondere an Cold Brew? · Hat Cold Brew mehr Koffein?
- Related: cold brew deutschland, kaufen, preis, concentrate, rezept, drinks, bohnen, cold brew latte kcal.
- Competitor note: no German editorial article in the top 8 – SERP is official pages + shops + UGC. "Competitors" for extraction = starbucks.de (iced coffees + product page), starbucksathome.com recipe, nutriscan.app (thin, US values: "5 Kalorien, 205mg").

## Head entities (Step 2)
- Cold brew coffee – https://en.wikipedia.org/wiki/Cold_brew_coffee (coarse grounds steeped in cold water, long extraction, lower acidity).
- Starbucks – Wikidata Q37158. DE stores operated by AmRest (site research).

## Fact ledger
| Fact | Source |
|---|---|
| "Ein über 20 Stunden kalt gebrühter Kaffee für ein extra sanftes Kaffeeerlebnis, ungesüßt" | starbucks.de/de/menu/product/106865 (fetched 3 Oct) |
| Täglich in kleinen Mengen von Hand, 20 h, ohne Hitze, spezielle Bohnenmischung | starbucks.de/de/menu-drinks-iced-coffees (fetched) |
| Cold Brew Latte "mit Milch, ungesüßt"; sizes Tall/Grande/Venti | product 104683 (fetched) |
| Cold Brew labels GLUTEN_FREE, VEGAN, VEGETARIAN; Latte GLUTEN_FREE, VEGETARIAN | product JSON (fetched) |
| Milk splash options all +0,00 incl. laktosefreie Milch; Soy Protein Drink +1,50 € (Latte) | product JSON (fetched) |
| kcal/caffeine: CB 16/22/28 kcal, 188,6/255,8/322,9 mg; CBL by milk; Filterkaffee Grande 254,6 mg 31 kcal; Iced Americano Grande 133,6 mg 11 kcal; Caffè Latte Grande 89,1 mg 151 kcal | Nährwert-PDF Getränke 10.09.2026 (starbucks.de/de/nutrition, downloaded) |
| Cold Brew Latte with Hafer = vegan; Hafer = glutenhaltiges Getreide (d), Mandel = Schalenfrüchte (g) | Allergen-PDF Getränke 10.09.2026 |
| Nitro Cold Brew = store feature "NB" in store locator | starbucks.de page payload (STORE_FEATURE_NB) |
| Salted Caramel Cold Brew not on menu/PDF | /blog/starbucks-getraenke + menu check 3 Oct |
| Prices 4,25/4,75/5,15 € | /blog/starbucks-getraenke (site, 28 Sep) |
| Freiburg Hbf order page 4,40 € (28 Sep) | /blog/starbucks-preise (site) |
| Cold Brew Latte ~5,90 € | /blog/starbucks-kaffee (site; size not stated) – FLAG |
| Cold Foam +1,00 € | /blog/starbucks-getraenke (site) |
| Plant-milk surcharge dropped March 2023, 155 stores | worldcoffeeportal.com, 13 Mar 2023 |
| Cold Brew on Starbucks DE menu since 2016 | hogapage.de, 23 May 2018 |
| Home recipe: 22 g / 180 ml, grob, 12 h, Mulltuch, 1:1 Wasser, Eiswürfel einfrieren; page shows Veranda Blend | starbucksathome.com/de/brewing-guides/brewing-at-home/cold-brew-mit-mason-jar (fetched) |
| Starbucks at Home DE online range = Nespresso + Dolce Gusto capsules | starbucksathome.com/de/produkte (fetched) |
| Pike Place Roast 450 g 14,89 € | Google Shopping on google.de SERP, 3 Oct |
| PSL cold brew concentrate 26,97 € | Google Shopping, 3 Oct |
| EFSA 400 mg/day safe for healthy adults | EFSA 2015 opinion (general knowledge, not fetched this run) – FLAG light |
| US Grande cold brew ~205 mg | nutriscan.app snippet / US data |

## Entity tiers / relationships
T1: Cold Brew, Starbucks, 20-h-Kaltextraktion, Koffein, Preis, Kalorien, Cold Brew Latte, Rezept. T2: Iced Coffee, Iced Americano, Filterkaffee, Nitro Cold Brew, Säure, Bohnenmischung, Konzentrat, Milchoptionen, Sirup, Cold Foam, Größen, vegan/glutenfrei, Starbucks at Home. T3: Nestlé, EFSA, Salted Caramel CB, Kenya, Veranda, Pike Place.
Relations: Cold Brew —steeped→ 20 h cold water · Grande CB —contains→ 255,8 mg caffeine ≈ Filterkaffee 254,6 mg · CB Latte —has less caffeine because→ milk replaces coffee · milk choice —determines→ CBL kcal (69–161) · plant milk —costs→ 0 € since 03/2023 · Hafer —contains→ gluten · home recipe —ratio→ 22 g/180 ml, 12 h, 1:1 · Kenya —"unverzichtbar in"→ Eiskaffee-Mischungen · Starbucks at Home —is→ Nestlé brand.

## Information gain
1. Official per-size caffeine/kcal table + caffeine comparison vs Filterkaffee/Americano/Latte (no SERP page has DE values; nutriscan uses US 205 mg).
2. Cold Brew Latte kcal/sugar/protein by all 7 milks (official PDF).
3. DIY cost worked example (0,96 € per Grande-Menge vs 4,75 €).
4. Correction: plant milk is free since 03/2023 (several site pages still say 0,50–0,80 €).

## Heading + keyword + question map
| Level | Heading | Phrase owned | Question |
|---|---|---|---|
| H1 | Starbucks Cold Brew: Preis, Koffein, Kalorien und Rezept … | starbucks cold brew | – |
| H2 | 1. Was ist Starbucks Cold Brew? | was ist cold brew | PAA "Was ist das Besondere an Cold Brew?" |
| H3 | Wie stellt Starbucks den Cold Brew her? | zubereitung | – |
| H3 | Welche Bohnen nutzt Starbucks für Cold Brew? | cold brew bohnen | related |
| H2 | 2. Welche Cold-Brew-Getränke gibt es …? | cold brew drinks / deutschland | related; PAA "kalten Kaffee?" |
| H3 | Wie kann ich meinen Cold Brew anpassen? | cold brew milch/sirup | – |
| H2 | 3. Was kostet ein Cold Brew …? | cold brew preis | related |
| H3 | Lohnt sich der Cold Brew preislich? | – | – |
| H2 | 4. Wie viel Koffein …? | cold brew koffein | – |
| H3 | Hat Cold Brew mehr Koffein als normaler Kaffee? | – | PAA |
| H2 | 5. Wie viele Kalorien …? | cold brew latte kcal | related |
| H2 | 6. Unterschied Cold Brew, Iced Coffee, Iced Americano | iced coffee vs cold brew | PAA |
| H2 | 7. Wie mache ich Starbucks Cold Brew zu Hause? | cold brew rezept | related (HowTo) |
| H3 | Was kostet selbst gemachter Cold Brew? | – | info gain |
| H3 | Welche Bohnen eignen sich für Cold Brew? | – | – |
| H3 | Gibt es Starbucks Cold Brew zu kaufen? | cold brew kaufen / concentrate | related |
| H2 | 8. Vegan, glutenfrei, laktosefrei? | – | – |
| H2 | FAQ (12) | – | – |

## Internal links / cannibalisation
Out: iced-coffee, kaffee, getraenke, preise, kalorien-guide, sirup, milchalternativen (new), kaffeebohnen (new), angebote.
Cannibalisation: /blog/starbucks-iced-coffee §5 (Iced Coffee vs Cold Brew vs Americano) and /blog/starbucks-kaffee (Cold Brew FAQ). This page must own "starbucks cold brew"; add a link "Starbucks Cold Brew" from iced-coffee §5 and kaffee's brewed-coffee section after publish.

## FLAGS (need human)
- Price inconsistency across own site: Cold Brew 3,99–4,99 (iced-coffee), 4,25/4,75/5,15 (getraenke), 4,60 (menu/kaffee), 4,40 Freiburg. Draft uses getraenke + Freiburg. Cold Brew Latte 5,90 € has no size. Verify in the app before publish.
- Site-wide correction needed: plant-milk surcharge 0,50–0,80 € is outdated (free since 03/2023; MOP shows +0,00 on 3 Oct 2026). Affects vegane-optionen, preise, cappuccino, getraenke, sirup and others.
- Concentrate shelf life ("einige Tage") is general guidance, no Starbucks source.
- Hero image TODO.
