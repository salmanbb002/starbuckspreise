# Merge batch 2026-09-28: 43 "Merge-Recommended" keywords folded into 7 existing pages

Decision: the user chose "merge rest + 3 new posts" (tee/teesorten, matcha preis ×2 and frühstück ×2 became new posts; see their own folders).

## Sources (all fetched 2026-09-28)
- S1 starbucks.de drink category pages (curl): 61 drinks, 8 categories, 36 cold drinks.
- S2 starbucks.de nutrition PDFs "Autumn - 10.09.2026" (drinks + food), extracted with pypdf. Drinks rows are reliable. In the food PDF only the vegan/vegetarian flags and gluten letters are reliable (empty cells collapse).
- S3 starbucksfreiburg.de: ordering site of Starbucks Freiburg Hauptbahnhof, 156 items with prices incl. merchandise (sizes of drinks not stated).
- S4 menupricetoday.com: delivery-platform prices, Sept 2026 (matches S3).
- S5 aktionspreis.de + prospektangebote.de: REWE Starbucks-by-Nespresso 10er regular 4,49–4,69 €, offer 3,69 € (−18/−21 %) until ~02.10.2026, regional.

## Per page
| Page | Keywords merged | What changed |
|---|---|---|
| starbucks-preise | was kostet ein kaffee, starbucks kaffee preise, was kostet ein cappuccino, kaffeepreise starbucks, frappuccino starbucks preis, starbucks getränke liste preise, price of starbucks coffee, starbucks getränke preise, starbucks speisekarte preise, starbucks cost, starbucks prices, starbucks preis, preise bei starbucks | dated S3 price check in §5; **food table replaced**: the old rows (Buttercroissant 2,10 €, Panini that are not in the official food PDF) became 11 current items with S3 prices; links to tee, matcha and frühstück; +5 FAQs (1 in English) |
| starbucks-menu | starbuck getränkekarte, starbucks deutschland menü, getränk starbucks, starbucks sortiment, starbucks mnu, starbucks kalte getränke, starbucks menu of drinks, starbucks sorten, starbucks drink menu, starbucks beverage, menukaart starbucks, getränke bei starbucks | croissant/muffin prices updated to the current values; links to frühstück, tee and matcha; +4 FAQs (36 cold drinks, 61 drinks, range = 61 drinks + 66 foods, English drink menu); meta keywords. "menukaart" (Dutch) is keyword-meta only |
| starbucks-kaffee | starbucks coffeee, starbucks espresso, kaffee starbucks kaufen, starbucks kaffee sorten, starbucks coffee drinks menu, starbucks oats | +5 FAQs (espresso caffeine 44,5/89,1 mg from S2, roast types, where to buy, oat drink, English coffee menu) |
| starbucks-becher | starbucks shop becher, starbucks becher groß, starbucks deutschland mug, starbucks cups kaufen, starbucks cup kaufen, starbuck cup | **price table replaced with S3 store prices** (2,50 € reusable to 26,90 € SS cold cup; mugs 8,90–17,90 €); answer box + 1 FAQ updated; +4 FAQs |
| starbucks-kapseln-angebot | starbucks kaffee rewe, starbucks nespresso kapseln angebot, starbucks kaffee kapseln angebot, starbucks kapseln angebot rewe | REWE check paragraph (S5); +3 FAQs |
| starbucks-groessen-tall-grande-venti | starbucks tall ml | **first JSON-LD on the page** (Article/FAQPage/Breadcrumb); fixed the wrong "Caffè Latte Venti = 2 Shots" (the PDF says 3; Tall = 2 since the Autumn PDF); +7 FAQs (3 → 10) |
| starbucks-tasse-berlin | starbucks tassen berlin | +1 FAQ listing all 4 Berlin series; meta keywords |
| starbucks-getraenke (cleanup, no keywords) | — | caffeine/kcal columns of the 25-row table replaced with S2 Grande values; **fixed Pink Drink "ca. 45 mg" (base is 4,9 mg) and Filterkaffee "ca. 310 mg" (254,6 mg)**; corrected the note: Brown Sugar Oat + Cool Lime are in the Autumn PDF; tea/matcha links |

## Open flags
- starbucks-tassen says "In Deutschland wird nur die You Are Here Series verkauft", but starbucks-tasse-berlin says Been There has replaced all earlier series since 2018. The two pages contradict each other and this needs research.
- Price columns in the getraenke and preise drink tables are older research. S3 (a station store) agrees roughly (Latte 4,90 € = Venti level), but they have not been re-verified per size.
- The own-cup discount (0,30 vs 0,50 €) is still inconsistent sitewide.
- REWE offers are regional and time-limited (until ~02.10.2026), so this needs a refresh.
