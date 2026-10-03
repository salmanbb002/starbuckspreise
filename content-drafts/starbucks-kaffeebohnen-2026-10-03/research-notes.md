# Research notes – starbucks kaffeebohnen (run 2026-10-03, planned publish 2026-10-22)

## Intent / SERP (google.de, 3 Oct 2026, via browser)
- ~40/mo (+ "bohnen" ~20). Intent: buy-informational (which beans, where, price) + know (best bean).
- Organic: 1 starbucksathome.com/de-ch/produkte (404 when fetched) · 2 starbucks.de/de/menu-kaffeebohnen · 3 maxicoffee.de (450 g range) · 4 kaffek.de Blonde Espresso Roast 450 g · 5 amazon.de · 6 vergleich.org "Starbucks-Kaffee Vergleich 2026" (mostly capsules) · 7 reddit r/espresso · 8 YouTube ZDF besseresser quality test (~3 yrs, ~378k views; NOT watched – not used in draft).
- SERP features: Google Shopping (Espresso Dark Roast 12,90 €, Blonde 30,50 € (multi?), Pike Place 15,64 €, Pike Place 450 g 14,89 €), PAA, images, related.
- PAA: Welcher Starbucks-Kaffee ist der beste? · Welche Kaffee gibt es bei Starbucks? · Wie viel kostet Kaffee bei Starbucks? · Wo kommt Starbucks Kaffee her?
- Related: 1kg, für vollautomaten, wo kaufen, preis, edeka, rewe, vanille, crema.

## Fact ledger
| Fact | Source |
|---|---|
| 9 beans + descriptions (Spring Season Blend 2025, Kenya, Guatemala Antigua, Pike Place 2008, Sumatra, Caffè Verona/Jake's Blend 1975 80/20, Espresso Roast seit 1975, Blonde, Decaf) | starbucks.de/de/menu-kaffeebohnen (fetched 3 Oct) |
| Roast levels per bean | Starbucks Roast Spectrum (global classification; not on DE page) – FLAG light |
| Drink bean options: Signature Espresso/Blonde/Decaf; Frappuccino Roast/Decaf; Filterkaffee = Pike Place | starbucks.de product JSON (fetched) |
| SAH: only 100 % Arabica; 1971 only whole beans; Signature Espresso Roast since 1984 base; 150+ yrs roasting experience; 98 % water; 4 fundamentals; regions' flavour profiles; flavoured Nespresso capsules (Creamy Vanilla, Smooth Caramel, Chocolate Hazelnut); DE online range = capsules | starbucksathome.com/de/produkte (fetched) |
| 10 g / 180 ml | starbucksathome.com brewing guide (via search result) |
| 22 g / 180 ml cold brew | SAH Mason-Jar recipe (fetched) |
| MaxiCoffee: 450 g and 4×450 g (Blonde, Colombia, Espresso Roast), Starter-Set 3×450 g | maxicoffee.com/de-de (curl) |
| KaffeK Blonde Espresso Roast 450 g 14,79 € (32,87 €/kg), "Mindestens haltbar bis" | kaffek.de (curl) |
| Pike Place 450 g 14,89 € | Google Shopping 3 Oct |
| Kaufland marketplace 4×450 g Pike Place 97,99 € | WebSearch snippet (kaufland.de/product/566114282) |
| Store 250 g 6,99–7,99 €, Reserve bis 12,99 €, free grinding | /blog/starbucks-preise (site, unverified by Starbucks) – FLAG |
| Filterkaffee Tall 3,10 € | /blog/starbucks-preise (site) |
| Nestlé Global Coffee Alliance 2018, 7,15 Mrd USD | /blog/starbucks-kapseln-angebot (site) |
| AmRest operates DE stores | /blog/starbucks-menu, -protein (site) |
| Capsules at REWE/Edeka/dm; 0,30–0,50 €/Kapsel | /blog/starbucks-kapseln-angebot (site) |
| Reserve: "R" mit Stern; single farms; small lots | /blog/starbucks-reserve (site) |

## Tiers / relationships
T1: Kaffeebohnen, Starbucks, Sorten, Preis, kaufen, Arabica, Pike Place Roast, Espresso Roast. T2: Blonde, Roast Spectrum, Single Origin, Verona, Sumatra, Decaf, Vollautomat, 450/250 g, Mahlgrad, Nestlé, Starbucks at Home, Lagerung, REWE/Edeka, Kapseln. T3: Reserve, Guatemala, Kenya, Global Coffee Alliance, AmRest, Pike Place Market, Robusta.
Relations: Espresso Roast —is base of→ espresso drinks · Pike Place —is→ Filterkaffee · Nestlé —sells retail under→ Starbucks at Home (since 2018) · AmRest —operates→ DE stores · 450 g —costs→ ~14,8 € (~33 €/kg) · 10 g —makes→ 180 ml (0,33 €) · dark oily beans —may leave residue in→ Vollautomat grinder · Kenya —ideal for→ Eiskaffee.

## Information gain
1. Bean → roast → flavour table with the official DE list (competitors list shop stock only).
2. Price-per-kg comparison store vs online vs marketplace + cost-per-cup worked example.
3. Machine-matching table (Vollautomat/Siebträger/Filter/French Press/Cold Brew/Decaf).
4. Which bean is in which café drink (official order-page data).

## Heading map
| Level | Heading | Phrase | Source |
|---|---|---|---|
| H1 | Starbucks Kaffeebohnen kaufen: Sorten, Preise … | starbucks kaffeebohnen | – |
| H2 | 1. Welche Kaffeebohnen gibt es bei Starbucks? | sorten | PAA "Welche Kaffee gibt es" |
| H3 | Was steckt hinter den bekanntesten Sorten? | – | – |
| H3 | Welche Bohne steckt in welchem Starbucks Getränk? | – | info gain |
| H2 | 2. Wo kann ich Starbucks Kaffeebohnen kaufen? | wo kaufen | related |
| H3 | Gibt es Starbucks Bohnen bei REWE und Edeka? | rewe / edeka | related |
| H3 | Kann ich die Bohnen in der Filiale mahlen lassen? | – | – |
| H2 | 3. Was kosten Starbucks Kaffeebohnen? | preis | related + PAA |
| H3 | Was kostet eine Tasse … zu Hause? | – | info gain |
| H2 | 4. … Vollautomat, Siebträger und Filter? | für vollautomaten / crema | related |
| H3 | Welche Bohne kommt dem Starbucks Latte am nächsten? | – | – |
| H2 | 5. Wie gut sind Starbucks Kaffeebohnen? | – | PAA "beste" |
| H3 | Was ist der Unterschied zu Starbucks Reserve? | – | – |
| H2 | 6. Wie lagere ich … richtig? | – | HowTo |
| H3 | Gibt es Starbucks Bohnen mit Vanille-Geschmack? | vanille | related |
| H2 | FAQ (12) | 1kg, herkunft (PAA "Wo kommt…") | |

## Internal links / cannibalisation
Out: kaffee, kapseln-angebot, preise, cold-brew (new), latte, reserve, sirup. In (after publish): kaffee ("Bohnenwahl" section), menu ("Kaffeebohnen" FAQ), preise §2.6.
Cannibalisation: /blog/starbucks-kaffee covers roast spectrum + origins + home brewing; /blog/starbucks-menu & -preise have "Kann ich Kaffeebohnen kaufen?" FAQs. This page owns kaufen/sorten/preis; kept roast science short and linked out.

## FLAGS (need human)
- Store prices (250 g 6,99–7,99 €), Reserve 12,99 € and free in-store grinding come only from our own older page – verify in a store or the app.
- "Spring Season Blend 2025" still on starbucks.de – draft points out the stale year.
- Roast level per bean uses Starbucks' global spectrum; DE page does not state roast levels.
- Did not confirm whole beans at REWE/Edeka (related searches suggest demand); draft says "vor allem online" – re-check before publish.
- ZDF besseresser test not used (video not reviewed).
- Hero image TODO.
