# Research notes – starbucks vanilla latte (2026-10-07)

## 1. Keyword, intent, SERP
- Primary: **starbucks vanilla latte** · ~60/mo (Research_Oct2026, evergreen). Sheet decision was "Merge into starbucks-latte §3"; that page had no vanilla mention. Owner asked for a standalone post.
- Intent: know (what is it, calories) + do (how to order). SERP (WebSearch, US-proxied): yazio.com (3 entries), fatsecret, kuechenfibel.de, fastfoodsmenu.com, supermarktcheck. PAA not captured.
- Fan-out (Autocomplete_Oct2026): starbucks vanilla latte; starbucks iced protein sugar free vanilla latte; starbucks vanilla; vanilla iced latte; vanilla kapseln; vanilla macchiato; vanilla syrup.

## 2. Head entities
| Entity | Type | sameAs | Facts |
|---|---|---|---|
| Vanilla Latte | Product | – (unlinked) | Caffè Latte + Vanillesirup |
| Caffè Latte | Product | de.wikipedia.org/wiki/Milchkaffee | Espresso, steamed milk, thin foam |
| Starbucks | Organization | wikidata Q37158 | DE menu on starbucks.de |

## 3. Sources (fetched 7 Oct 2026)
| # | Source | Facts used |
|---|---|---|
| S1 | starbucks.de/de/menu-drinks-hot-coffees | "Vanilla Latte" listed with description (Espresso, gedämpfte Milch, leichte Schaumschicht, Vanillesirup) |
| S2 | starbucks.de/de/menu/drinks/hot-drinks | 28 hot drinks; no "Vanilla Latte"; has "Soy Protein Vanilla Latte mit Sugar-Free Vanilla Sirup" |
| S3 | starbucks.de product JSON 106955 / 106985 / 107535 (Caffè Latte Tall/Grande/Venti) | volumes 284,1 / 345,5 / 455,6 ml; 129 / 151 / 204 kcal; sugar 12,3 / 14,2 / 19,4 g; caffeine 44,5 / 89,1 / 89,1 mg; shots 1 / 2 / 2; Vanilla Sirup firstAdd 3 / 4 / 5, max 12; default milk Halbfett; 12 syrups incl. 3 sugar-free; milks +0,00 (incl. Soja, Kokos, Mandel, Hafer), Soy Protein Drink +1,50 €; Einwegbecher +0,05, Mehrwegbecher +2,50 Pfand; beans Signature / Blonde / Decaf |
| S4 | product JSON 107073 (Iced Caffè Latte) | sizes 350,8 / 467,2 / 558,6 ml; Vanilla Sirup firstAdd 4 (Grande) |
| S5 | product JSON 397153 / 397105 / 397038 / 397167 (Soy Protein Vanilla Latte) | 155 / 194 / 256 kcal; protein 13,3 / 16,6 / 22,0 g; sugar 7 / 8 / 11 g; iced Grande 135 kcal, 11,3 g protein, 5 g sugar; labels vegan, gluten-free |
| S6 | product JSON 107625 (Caramel Macchiato Grande) | 214 kcal, 27,6 g sugar, "Vanilla Sirup und Karamellsauce" |
| S7 | Allergen-PDF "Autumn – 10.09.2026 (Getränke)", starbucks.de/de/nutrition | Vanilla Latte listed with 7 milks; vegan with Soja/Kokosnuss/Mandel/Hafer; Syrups Vanilla + Vanilla (Sugarfree)** vegan; ** = "Kann bei übermäßigem Verzehr abführend wirken". PDF has no kcal. |
| S8 | starbucksfreiburg.de | Caffè Latte 4,90 €, Iced Caffè Latte 4,90 €, Soy Protein Vanilla Latte 5,90 € (hot/iced), Iced Caramel Macchiato 5,90 €, Vanilla Cream Frappuccino 6,40 € |
| S9 | starbucks.de/de/rewards | 3 Sterne pro Euro; Gold ab 450 Sternen; Gold: Sirups und Espresso-Shots kostenlos |
| S10 | starbucksathome.com/de | Creamy Vanilla by Nespresso (10 Kapseln, Blonde Roast); Madagascar Vanilla Macchiato by Nescafé Dolce Gusto |
| S11 | own /blog/starbucks-sirup research (tastingtable.com, US) | ~20 kcal and 5 g sugar per pump – US value, not DE |
| S12 | Nährwert-PDF „Autumn – 10.09.2026 (Getränke Nährwerte)“, relative link on starbucks.de/de/nutrition (found 8 Oct 2026) | Caffè Latte Halbfettmilch: Short 74 kcal / 44,5 mg, Tall 124 / 89,1, Grande 151 / 89,1, Venti 204 / 133,6; sugar 6,9 / 11,5 / 14,2 / 19,1 g. Caramel Macchiato 167 / 214 / 272 kcal. Soy Protein Latte 155 / 194 / 256 kcal, 44,5 / 89,1 / 89,1 mg. No Vanilla Latte row, no syrup rows. |

## 4. Competitors
| # | URL | What it has |
|---|---|---|
| C1 | yazio.com/de/kalorientabelle/vanilla-latte-starbucks.html | 220 kcal, 28 g carbs, 9 g protein, 9 g fat; no size |
| C2 | fastfoodsmenu.com/starbucks-menu-preise-deutschland (9 May 2026) | price list: Caffè Latte 4,90 €, Protein Sugar Free Vanilla Latte 5,90 €, Vanilla Cream Frappuccino 6,40 €; H2s: Bundles, Espresso Beverages, Frappuccino, Öffnungszeiten, Alternativen, FAQ |
| C3 | kuechenfibel.de/faq/wie-viel-zucker-ist-in-starbucks (1 Sep 2023) | sugar angle, no DE vanilla latte data |
| C4 | starbucksathome.com/de/produkte | at-home vanilla capsules |
- None explains how to order it in Germany or how many pumps it gets.

## 5. Entity ledger → entities.json
T1: Vanilla Latte, Caffè Latte, Vanillesirup, Preis, Kalorien, Starbucks Deutschland. T2: Pumpen, Soy Protein Vanilla Latte, Sugar Free Vanilla Sirup, Iced Vanilla Latte, Zucker, Koffein, Caramel Macchiato, Starbucks Rewards, Pflanzendrink, Größen. T3: Blonde, Vanilla Cream Frappuccino, Creamy Vanilla, Madagascar Vanilla Macchiato.
Relations: Vanilla Latte = Caffè Latte + Vanilla Sirup · size —sets→ 3/4/5 pumps · Gold —waives→ syrup fee · 450 Sterne = 150 € · Soy Protein Vanilla Latte —uses→ sugar-free syrup (194 kcal, 16,6 g protein) · Caramel Macchiato = Vanilla Sirup + Karamellsauce (214 kcal) · plant milk —costs→ +0,00 €.

## 6. Information gain
Pump presets per size from the official order menu, the "where is it listed" table, the worked calorie estimate and the comparison table.

## 7. Calorie estimate (worked) – corrected 8 Oct 2026
**Correction:** the first version used the order-menu product JSON for the latte base (Tall 129 kcal, 44,5 mg, 1 shot; Venti 89,1 mg, 2 shots). Those are the Spring 2026 values. The Autumn nutrition list (S12) is newer: Tall 2 shots / 124 kcal / 89,1 mg, Venti 3 shots / 133,6 mg, as /blog/starbucks-kalorien-guide and /blog/starbucks-protein already said. The draft now uses S12 and mentions the order-menu discrepancy.
Tall 124 + 3×20 = 184 ≈ 185 kcal (first version: 129 + 60 = 189) · Grande 151 + 4×20 = 231 ≈ 230 kcal · Venti 204 + 5×20 = 304 ≈ 300 kcal. Sugar Grande 14,2 + 4×5 = 34,2 g. Yazio (220 kcal, no size) is in the same range. Official Caramel Macchiato Grande (214 kcal) is lower → estimate may be high; said so in the draft.

## 8. Internal links
latte, sirup, protein, kalorien-guide, groessen, app, preise, iced-coffee, milchalternativen, kapseln-angebot, /iced-caramel-macchiato. Inbound added from latte, sirup, getraenke. Cannibalisation: /blog/starbucks-latte owns "latte" (family overview); this page owns the vanilla variant.
