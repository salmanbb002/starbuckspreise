# Research notes – starbucks laktosefrei / milchalternativen (run 2026-10-03, planned publish 2026-10-21)

## Intent / SERP (google.de, 3 Oct 2026, via browser)
- Primary "starbucks laktosefrei" ~40/mo; secondary hafermilch, milch (Research_Oct2026 estimates). Intent: know-simple ("gibt es…?") + know (which milk / costs / kcal). YMYL-light (allergies).
- Organic: 1 rewe.de Starbucks No Added Sugar Latte laktosefrei 220 ml · 2 starbuckschilledcoffee.com Caffè Latte No Added Sugar · 3 starbucks.de/personalisierung · 4 reddit r/starbucks "Laktosefreie Milch wird eingestellt" (~1 yr, market unclear) · 5 knuspr.de · 6 gutefrage.net (2016) · 7 selgros.de · 8 starbucks.de/nutrition.
- SERP features: PAA, Google Shopping (chilled coffee 2,07–2,99 €), images, related searches. No snippet.
- PAA: Gibt es bei Starbucks glutenfreie Produkte? · Welche Milchalternativen bietet Starbucks an? · Was ist das gesündeste Getränk bei Starbucks? · Was gibt es bei Starbucks ohne Kaffee?
- Related searches are off-topic (sirup, rewe) → SERP is mixed retail/in-store intent; this page serves in-store intent and covers the supermarket product in §7.

## Head entities
- Lactose-free milk – https://en.wikipedia.org/wiki/Lactose-free_milk · Plant milk – https://en.wikipedia.org/wiki/Plant_milk · Starbucks Q37158.

## Fact ledger
| Fact | Source |
|---|---|
| 9 milk options incl. Laktosefreie Milch +0,00; Soy Protein Drink +1,50 € | starbucks.de product 104683 JSON (fetched 3 Oct) |
| Schuss: kalt/warm, all +0,00 incl. laktosefrei | product 106865 JSON |
| "fettarmer oder laktosefreier Milch oder … Sojadrink, Haferdrink, Mandeldrink oder Kokosnussdrink"; vegane Schlagsahne; zuckerfrei Vanille/Karamell/Haselnuss | starbucks.de/de/personalisierung (fetched) |
| Default milk: Halbfett (Latte, Cappuccino, Caramel Macchiato, Matcha, Chai); Vollmilch (Flat White, Coffee Frapp, Vanilla Cream Frapp) | product JSONs (fetched) |
| Caffè Latte Grande per milk (kcal/Fett/Zucker/Eiweiß) | Nährwert-PDF Getränke 10.09.2026 |
| Soy Protein Vanilla Latte Grande 194 kcal | product 397105 JSON |
| Vegan status with Hafer per drink; *** footnote (vegane Schlagcreme, ohne Topping); Hafer = d (glutenhaltige Getreide); Mandel = g (Schalenfrüchte); Kreuzkontamination note; allergen header "Milch (Laktose)" | Allergen-PDF Getränke 10.09.2026 |
| No lactose-free row in either PDF | both PDFs |
| Surcharge dropped, 155 outlets, after UK & France | worldcoffeeportal.com 13 Mar 2023 |
| Porridges with hot Haferdrink | content-drafts/starbucks-fruehstueck research (site) |
| No Added Sugar Latte 220 ml, laktosefreie Milch, ohne Zuckerzusatz; Knuspr 2,07–2,59 €; Oat Caramel Macchiato "vegan" | rewe.de / knuspr.de / Google Shopping snippets 3 Oct |
| Protein Drink milk-based | /blog/starbucks-protein (site) |
| "laktosefrei" < 0,1 g/100 g in DE; oat sugar from starch hydrolysis; lactose ≈ sugar in milk latte | general food-science knowledge – FLAG light |

## Tiers / relationships
T1: laktosefreie Milch, Starbucks, Haferdrink, Sojadrink, Mandeldrink, Kokosdrink, Aufpreis, Laktose. T2: Kalorien je Milch, Halbfett/Voll/Mager, Soy Protein Drink, vegan, Laktoseintoleranz, Milcheiweißallergie, Allergenliste, Sauce/Sahne/Topping, Gluten, Eiweiß, Zucker, Caffè Latte. T3: Flat White, Frappuccino, Caramel Macchiato, Laktase, Zöliakie, No Added Sugar Latte (Oatly parked: unverified brand).
Relations: plant milk —costs→ 0 € since 03/2023 · Soy Protein —costs→ +1,50 € · laktosefreie Milch —still contains→ Milcheiweiß · Hafer —contains→ Gluten · Mandel —is→ Schalenfrucht · Haferdrink —has more kcal than→ Halbfettmilch (178 vs 151) · Mandeldrink —lowest→ 82 kcal · Caramel Macchiato/White Mocha —not vegan even with→ Haferdrink · Sahne/Topping —removal makes vegan→ Mocha, Frappuccinos.

## Information gain
1. Official 7-milk nutrition table (no SERP page has it).
2. "Laktose-Fallen" table from the allergen PDF (which drinks stay non-vegan with oat).
3. Need-based decision table (intolerance vs. allergy vs. coeliac vs. nut allergy).
4. Correction: no surcharge since 03/2023 (contradicts our own older pages).

## Heading map
| Level | Heading | Phrase | Question source |
|---|---|---|---|
| H1 | Starbucks laktosefrei: alle Milchsorten, Hafermilch … | starbucks laktosefrei | – |
| H2 | 1. Welche Milchsorten gibt es bei Starbucks? | starbucks milch | PAA "Welche Milchalternativen…" |
| H3 | Welche Milch nimmt Starbucks standardmäßig? | – | – |
| H2 | 2. Kann ich bei Starbucks laktosefrei bestellen? | laktosefrei bestellen | primary |
| H3 | Laktosefrei oder pflanzlich: Was passt zu mir? | – | info gain |
| H2 | 3. Kostet Hafermilch bei Starbucks extra? | starbucks hafermilch aufpreis | fan-out |
| H2 | 4. Welche Milch hat … die wenigsten Kalorien? | – | PAA "gesündestes Getränk" |
| H3 | Wie viel Zucker steckt in der Milch? | – | – |
| H2 | 5. Welche Getränke enthalten trotz Hafermilch noch Milch? | – | info gain |
| H3 | Wie bestelle ich ein Getränk komplett laktosefrei? | – | HowTo |
| H2 | 6. Welche Hafermilch nutzt Starbucks …? | starbucks hafermilch | secondary kw |
| H3 | Ist der Haferdrink bei Starbucks glutenfrei? | – | PAA "glutenfreie Produkte" |
| H2 | 7. Gibt es Starbucks laktosefrei im Supermarkt? | – | SERP (REWE, Knuspr) |
| H2 | FAQ (12) | | |

## Internal links / cannibalisation
Out: preise, protein, kalorien-guide, pumpkin-spice-latte, vegane-optionen, angebote. In (after publish): cold-brew (done), vegane-optionen "Pflanzliche Milchalternativen", cappuccino §6, preise FAQ "Hafermilch Aufpreis", getraenke §9.
Cannibalisation: /blog/starbucks-vegane-optionen has an H2 "Pflanzliche Milchalternativen" → keep it short there and link here; this page owns laktosefrei / hafermilch / milch.

## FLAGS (need human)
- SITE ERRORS to fix: "Aufpreis 0,50–0,80 € für Pflanzenmilch" on vegane-optionen, preise (FAQ "Wie viel kostet Hafermilch…" + table), cappuccino, getraenke, sirup (table), menu.js FAQ. Also preise names "Oatly Barista" and cappuccino says laktosefreie Milch "nicht belegt" – both now wrong/unverified.
- Sirup post says sugar-free hazelnut unverified – starbucks.de/personalisierung lists Vanille, Karamell, Haselnuss zuckerfrei.
- Reddit thread (~2025) claims lactose-free milk being discontinued; DE order page still lists it on 3 Oct 2026. Draft says availability can vary by store.
- Health/allergy content: reviewed for caution, but not checked by a nutrition professional.
- Hero image TODO.
