# Coverage / QA: starbucks-gebaeck-2026-10-02

- **Words:** 1,850 (finalize.py). **Direct answer:** 49 words, paragraph. **FAQ:** 10.
- **Tier-1 coverage:** 8/8 (100%), all with values (prices, kcal per item).
- **Tier-2 coverage:** 12/12 (100%).
- **Tier-3 used:** Lebkuchen Zimtschnecke, Pistazien-Zimtschnecke, Ofenfrisch, App (4/5). Unused: Rezepte/Thermomix (different intent).
- **Heading architecture:** one H1, 8 numbered H2 + FAQ, 4 body H3 + 10 FAQ H3, 0 hierarchy errors; distinct phrase per heading.
- **QUORA check:** every H2/H3 opens with a direct answer.
- **Competitor-heading matrix:** Breakfast Bakery (C1/C2) → §1 (sweet) + link to Frühstück ✔; Muffins → §3 ✔; Cookies → §4 ✔; Kuchen & Cheesecakes → §2 ✔; Brownies → §4 ✔; Cake Pops → §6 ✔; generic FAQs (Öffnungszeiten, Influencer…) → skipped (off-topic).
- **Question coverage:** kuchen preise/kalorien/nährwerte → §2 + §7; karotte → §2.1; kuchen bestellen → §2.3 + FAQ; muffin preis/kalorien/blueberry/cheesecake → §3; cookies → §4; zimtschnecke + pistazien → §5/§5.1; kuchen rezepte/thermomix, muffins rezept → not covered (parked).
- **Fact cross-check:** all kcal/g/sugar/protein → S1 (S3 for winter items, S4 for latte); all prices/descriptions/bundles → S2; Sterne → S5. Bundle maths checked: 5 × 3,80 = 19,00 − 15,90 = 3,10 €.
- **Soft claims (flag):** "Sie werden in der Filiale gebacken" for Ofenfrisch items is an inference from the label. Brownie gluten statement relies on an empty cell in the PDF row (pypdf collapses blank cells; worth a visual check of the PDF).
- **Intent check:** yes: prices + kcal up front, by category, with ranking.
- **Readability:** ~grade 7; 7 tables.
- **E-E-A-T:** no first-person claims. Schema publisher logo TODO.

## Flags (need user)
1. **Prices are one store (Freiburg Hbf, Lieferando-run ordering page).** C2 shows prices ~0,40–0,60 € higher; in-store prices may differ.
2. Brownie, Ruby Cookie and Banana-Caramel Muffin have kcal but no Freiburg price ("nicht in Freiburg gelistet").
3. Seasonal items (Herbst/Halloween) will go stale in early Nov. Refresh with the Weihnachten launch.
4. /blog/starbucks-preise and menu.js food prices were not checked against S2. Likely stale, same pattern as earlier runs.
5. Hero image needed (cake/muffin/cinnamon roll, no logo).
