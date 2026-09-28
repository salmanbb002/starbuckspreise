# Research notes: starbucks-matcha-latte

Keywords: starbucks matcha preis (90) + starbucks matcha latte preis (90) = 180/mo. The calendar marked both rows "Merge-Recommended". On 2026-09-28 the user chose "merge rest + 3 new posts", so this is a standalone post; no existing page covers the topic beyond one short section.

## 1. Intent + SERP (WebSearch 2026-09-28)
Intent: know (+ buy/visit for prices). The SERP is dominated by US starbucks.com product pages, US "matcha menu" price farms (USD) and DE price aggregators that list only seasonal matcha prices. No DE page gives the classic Matcha Latte price with nutrition per size/milk.

## Sources (fetched 2026-09-28)
| # | Source | Used for |
|---|---|---|
| S1 | starbucks.de/de/menu-drinks-hot-teas, -iced-teas (curl) | official tea/matcha names and counts (8 hot, 6 iced) |
| S2 | starbucks.de/de/nutrition → "Allergen- und Nährwertinformationen Autumn - 10.09.2026" (Getränke Nährwerte PDF, Food PDF), text-extracted with pypdf | all kcal / Zucker / Eiweiß / Koffein values, vegan/vegetarian flags, gluten letters |
| S3 | starbucksfreiburg.de (ordering site "STARBUCKS FREIBURG HAUPTBAHNHOF", curl, 156 items) | prices + product descriptions; drink sizes not stated |
| S4 | menupricetoday.com/de/brands/starbucks/menu ("Die Preise stammen von Lieferplattformen", Sept 2026) | price cross-check (matches S3), Protein Joghurt 3,20 €, Cream Cheese Bagel 4,90 €, Hibiscus 4,05 €, Ube/Banana matcha 7,40 €, "Frühstück à la française" 8,50 € |
| S5 | en.wikipedia.org API (Teavana, Matcha, Matcha latte, Masala chai, Earl Grey, English breakfast tea, Porridge, Bagel, Croissant, Pain au chocolat) | entity facts + Wikidata sameAs |

## 7. Information gain
(1) price 6,00 € with 2 agreeing sources; (2) a full kcal/Zucker/Koffein table per size and per milk from the official PDF; (3) hot vs iced vs Frappuccino comparison; (4) Matcha vs Caffè Latte vs Chai matrix; (5) "ungesüßt in DE" noted explicitly.

## 8e. Internal links
out: preise, kalorien-guide, tee, frappuccino-sorten, becher-aktuell, groessen, vegane-optionen, becher, latte. in (to add): getraenke §6 matcha line, frappuccino-sorten, kalorien-guide.

## Open flags
- Prices: starbucks.de publishes none; S3 is one station store (Freiburg Hbf) and S4 is delivery-platform data. They agree with each other but **conflict with our own starbucks-preise/getraenke tables** (e.g. Caffè Latte 4,90 € here vs 3,90–4,45 € there). This needs a sitewide price reconciliation (planned in the preise merge).
- The drinks PDF extraction is row-reliable (one product/size per line). In the **food PDF, only the vegan/vegetarian ja/nein and the gluten letters are reliable**: empty cells collapse, so the ✓/S allergen marks cannot be mapped to columns and were not used.
- The Ube Vanilla Velvet and Caramelised Banana matcha (7,40 €) appear only in S4 and may be past-season.
- Our homepage says "Iced Matcha Latte: 6,90 € bis 7,90 €" and getraenke says 5,15–6,15 €. Both conflict with S3/S4 (6,00 €).
- The only Starbucks-named matcha photo on Commons looks like a re-uploaded web banner, so a generic matcha photo is used instead (credited).
