# Research notes: starbucks-fruehstueck

Keywords: preisliste frühstück (210) + starbucks frühstück (110) = 320/mo. The calendar marked both rows "Merge-Recommended". On 2026-09-28 the user chose "merge rest + 3 new posts", so this is a standalone post; no existing page covers the topic beyond one short section.

## 1. Intent + SERP (WebSearch 2026-09-28)
Intent: know (+ buy/visit for prices). "starbucks frühstück" returns Uber Eats store pages (Hamburg Rathausmarkt, München Odeonsplatz), starbucks.de, starbucksathome, Shutterstock and Wikipedia. There is no editorial DE breakfast guide, so the intent (what is there / what does it cost) is unserved.

## Sources (fetched 2026-09-28)
| # | Source | Used for |
|---|---|---|
| S1 | starbucks.de/de/menu-drinks-hot-teas, -iced-teas (curl) | official tea/matcha names and counts (8 hot, 6 iced) |
| S2 | starbucks.de/de/nutrition → "Allergen- und Nährwertinformationen Autumn - 10.09.2026" (Getränke Nährwerte PDF, Food PDF), text-extracted with pypdf | all kcal / Zucker / Eiweiß / Koffein values, vegan/vegetarian flags, gluten letters |
| S3 | starbucksfreiburg.de (ordering site "STARBUCKS FREIBURG HAUPTBAHNHOF", curl, 156 items) | prices + product descriptions; drink sizes not stated |
| S4 | menupricetoday.com/de/brands/starbucks/menu ("Die Preise stammen von Lieferplattformen", Sept 2026) | price cross-check (matches S3), Protein Joghurt 3,20 €, Cream Cheese Bagel 4,90 €, Hibiscus 4,05 €, Ube/Banana matcha 7,40 €, "Frühstück à la française" 8,50 € |
| S5 | en.wikipedia.org API (Teavana, Matcha, Matcha latte, Masala chai, Earl Grey, English breakfast tea, Porridge, Bagel, Croissant, Pain au chocolat) | entity facts + Wikidata sameAs |

## 7. Information gain
(1) the official breakfast product list from the food PDF (10.09.2026) with kcal + protein; (2) a price list from 2 sources; (3) a worked example of 4 breakfast combos (5,40–10,00 €) + the Sip & Sandwich saving of 0,80 €; (4) vegan list from the PDF; (5) a gluten table.

## 8e. Internal links
out: getraenke#getraenke-liste, menu, preise, becher, angebote, vegane-optionen, kalorien-guide, geoeffnet, in-meiner-naehe. in (to add): menu §3 Essen, preise food table, vegane-optionen.

## Open flags
- Prices: starbucks.de publishes none; S3 is one station store (Freiburg Hbf) and S4 is delivery-platform data. They agree with each other but **conflict with our own starbucks-preise/getraenke tables** (e.g. Caffè Latte 4,90 € here vs 3,90–4,45 € there). This needs a sitewide price reconciliation (planned in the preise merge).
- The drinks PDF extraction is row-reliable (one product/size per line). In the **food PDF, only the vegan/vegetarian ja/nein and the gluten letters are reliable**: empty cells collapse, so the ✓/S allergen marks cannot be mapped to columns and were not used.
- "Frühstück à la française" contents are unconfirmed (they come only from a search summary), so the page says so.
- The Avocado & Egg Bagel is in the PDF but has no price in S3/S4.
- Our starbucks-preise food table (Croissant 2,10 €, Bagel 3,60 €, Panini) is outdated vs S3/S4.
- The "ab Öffnung / keine festen Frühstückszeiten" claim is inferred from the menu structure (no breakfast category in S3/PDF).
