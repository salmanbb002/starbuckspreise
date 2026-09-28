# Research notes: starbucks-tee

Keywords: starbucks teesorten (140) + starbucks tee (110) = 250/mo. The calendar marked both rows "Merge-Recommended". On 2026-09-28 the user chose "merge rest + 3 new posts", so this is a standalone post; no existing page covers the topic beyond one short section.

## 1. Intent + SERP (WebSearch 2026-09-28)
Intent: know (+ buy/visit for prices). "starbucks tee sorten" returns T-shirt shops, eBay listings and one 2016 Swiss Teavana launch article (proudmag.com: 10 loose-leaf teas incl. Jasmine Pearls, Mint Citrus, Kamille; no prices). "starbucks tee" price queries return generic price-list aggregators (fastfood-preisecheck, germanmenus 403, speisekartemenus). There is no dedicated, current DE tea guide, which is a clear gap.

## Sources (fetched 2026-09-28)
| # | Source | Used for |
|---|---|---|
| S1 | starbucks.de/de/menu-drinks-hot-teas, -iced-teas (curl) | official tea/matcha names and counts (8 hot, 6 iced) |
| S2 | starbucks.de/de/nutrition → "Allergen- und Nährwertinformationen Autumn - 10.09.2026" (Getränke Nährwerte PDF, Food PDF), text-extracted with pypdf | all kcal / Zucker / Eiweiß / Koffein values, vegan/vegetarian flags, gluten letters |
| S3 | starbucksfreiburg.de (ordering site "STARBUCKS FREIBURG HAUPTBAHNHOF", curl, 156 items) | prices + product descriptions; drink sizes not stated |
| S4 | menupricetoday.com/de/brands/starbucks/menu ("Die Preise stammen von Lieferplattformen", Sept 2026) | price cross-check (matches S3), Protein Joghurt 3,20 €, Cream Cheese Bagel 4,90 €, Hibiscus 4,05 €, Ube/Banana matcha 7,40 €, "Frühstück à la française" 8,50 € |
| S5 | en.wikipedia.org API (Teavana, Matcha, Matcha latte, Masala chai, Earl Grey, English breakfast tea, Porridge, Bagel, Croissant, Pain au chocolat) | entity facts + Wikidata sameAs |

## 7. Information gain
(1) the official 2026 DE tea list vs the outdated 2016 lineup competitors copy; (2) a caffeine table from the official PDF showing English Breakfast at 102 mg > Grande Caffè Latte at 89 mg; (3) a Tee-vs-Kaffee price/caffeine/kcal matrix; (4) koffeinfreie Optionen.

## 8e. Internal links
out: getraenke#getraenke-liste, preise, matcha-latte, refresha, vegane-optionen, becher, kaffee. in (to add): getraenke §6, menu §2.

## Open flags
- Prices: starbucks.de publishes none; S3 is one station store (Freiburg Hbf) and S4 is delivery-platform data. They agree with each other but **conflict with our own starbucks-preise/getraenke tables** (e.g. Caffè Latte 4,90 € here vs 3,90–4,45 € there). This needs a sitewide price reconciliation (planned in the preise merge).
- The drinks PDF extraction is row-reliable (one product/size per line). In the **food PDF, only the vegan/vegetarian ja/nein and the gluten letters are reliable**: empty cells collapse, so the ✓/S allergen marks cannot be mapped to columns and were not used.
- The PDF gives Earl Grey 1,1 mg and Emperor's Clouds 0,9 mg caffeine, which is implausible for black/green tea. The page says so and does not rely on them.
- Youthberry is on starbucks.de but not on the Freiburg ordering site. Its white-tea base is from the 2016 CH article, so the draft does not state it.
- Our getraenke table says "Teavana Blatt-Tee ca. 40 mg", Chai 240 kcal/95 mg and Iced Matcha 200 kcal. All conflict with the PDF (fix in the getraenke merge).
