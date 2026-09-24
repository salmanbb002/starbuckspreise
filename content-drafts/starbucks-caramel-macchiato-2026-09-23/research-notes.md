# Research notes: „starbucks caramel macchiato“ (merge → /iced-caramel-macchiato)

Run date: 2026-09-23. Mode: merge-ready insert. The workbook says "Merge-Recommended (fold into existing iced-caramel-macchiato)". 720 searches/month.

## Step 1: Intent + SERP
Query: "starbucks caramel macchiato preis kalorien" (US tool, so treat it as a proxy).
1. yazio.com/de: Caramel Macchiato, Starbucks nutrition
2. fddb.info: Starbucks Caramel Macchiato
3. starbucks.com/menu/product/413/hot: official (JS-rendered, **fetch returned empty**)
4. starbucks.com …/413/iced/nutrition
5. fatsecret.de Starbucks
6. starbucksmenususa.com/caramel-macchiato (US prices)
7. snapcalorie.com, starbucks-menus.com, nutriscan.app

**Intent:** know-simple (Kalorien, Preis, what is it) + a little do (recipe). Nutrition databases dominate the SERP, so **calories are the core sub-intent**. That's why Block B is a full H2 with a table.
SERP features: no snippet seen; the result pattern suggests a table-style answer (per-size calories).
Fan-out / FAQs seen: "Is Starbucks Caramel Macchiato strong coffee?", "difference between Caramel Macchiato and Latte", "Is it healthy?", "Can I get it for my birthday?", "deals".

## Step 2: Head entities
| Entity | Type | sameAs |
|---|---|---|
| Caramel Macchiato | Thing (drink) | https://en.wikipedia.org/wiki/Latte_macchiato (closest; no dedicated article), so it's left **unlinked** in schema |
| Starbucks | Organization | https://de.wikipedia.org/wiki/Starbucks |
| Espresso | Thing | https://de.wikipedia.org/wiki/Espresso |
| Latte macchiato | Thing | https://de.wikipedia.org/wiki/Latte_macchiato |

## Step 4: Sources
- **starbucks.com hot product + nutrition:** fetch returned empty (JS app). The official description comes from the search-result snippet: "freshly steamed milk with vanilla-flavored syrup marked with espresso and topped with a caramel drizzle". Ingredients (milk, brewed espresso, vanilla syrup, caramel sauce) are from the snippet too.
- **starbucksmenususa.com** (third-party, US): Short 120 / Tall 190 / Grande 250 / Venti 310 kcal; caffeine Short+Tall 75 mg, Grande+Venti 150 mg; US prices $6.37–$7.57 (not used, since this is a DE site). FAQs verbatim above.
- **fddb.info:** per 100 ml 60 kcal, 2.5 g fat, 7.3 g carbs, 7 g sugar, 2.2 g protein; Tall 355 ml = 213 kcal, 8.9 g fat, 25.9 g carbs, 7.8 g protein.
- **yazio.com:** 591 ml = 312 kcal, 41.2 g sugar, 8.7 g fat, 12.5 g protein; ≈53 kcal/100 ml.
- **Site's own menu.js:** Caramel Macchiato 4,99 € 901 kJ/214 kcal; Iced 5,79 € 847 kJ/201 kcal; Caffè Latte 4,59 € 151 kcal; Latte Macchiato 4,70 € 147 kcal.
- **Site's own pages:** menu page says Venti Iced = 709 ml and hot Venti = 591 ml; becher page gives Tall 355 / Grande 473 / Venti 590 ml; kapseln-angebot lists the Dolce Gusto Caramel Macchiato (Medium Roast) with milk powder.

**Conflicts noted:**
- US Tall 190 kcal vs DE/fddb Tall 213–214 kcal. The draft uses the DE figure for Tall and labels the US Grande figure as US.
- fddb 60 kcal/100 ml vs yazio 53 kcal/100 ml. The draft rounds to "rund 7 g Zucker/100 ml", which both agree on.
- **Live page errors:** Grande caffeine 75 mg (should be 150 mg per US data); Iced Venti 591 ml (should be 709 ml per our own menu page); "Grande … 201 kcal" (size label probably wrong, see instructions).

## Step 5/6: Entity ledger
| canonical | type | comp. | tier |
|---|---|---|---|
| Caramel Macchiato | Thing | 4 | 1 |
| Iced Caramel Macchiato | Thing | 3 | 1 |
| Kalorien (per size) | Metric | 4 | 1 |
| Preis | Money | 2 | 1 |
| Espresso | Thing | 4 | 1 |
| Vanillesirup | Thing | 3 | 1 |
| Karamellsauce / Drizzle | Thing | 3 | 1 |
| Koffein (75/150 mg) | Metric | 2 | 2 |
| Zucker | Metric | 3 | 2 |
| Größen Tall/Grande/Venti | Concept | 3 | 2 |
| Caffè Latte | Thing | 2 | 2 |
| Latte Macchiato | Thing | 1 | 2 |
| „Macchiato“ = gefleckt | Concept | 1 | 2 |
| Fett / Eiweiß / Kohlenhydrate | Metric | 3 | 3 |
| Dolce-Gusto-Kapsel | Product | 0 | 3 (site's own data) |

Relationships: Caramel Macchiato —contains→ Vanillesirup, Milch, Espresso, Karamellsauce · Espresso —added last, marks→ Milch · Tall —has→ 214 kcal, 75 mg · Grande —has→ 150 mg · Iced —costs→ 5,79 €, hot —costs→ 4,99 € · Latte Macchiato —lacks→ Sirup, so 147 kcal · Caffè Latte —espresso first→.

## Step 7: Information gain
1. A **hot vs iced comparison table**. No competitor compares both, and the host page ignores the hot drink entirely.
2. A **per-size table combining DE + US data** with the source of every cell labelled, so readers can see where DE figures and US figures differ.
3. **Corrections** to 3 errors on the live page.

## Step 8: Heading map
| Level | Heading | Owns |
|---|---|---|
| H2 | Caramel Macchiato heiß: Was unterscheidet ihn vom Iced Caramel Macchiato? | starbucks caramel macchiato (focus) |
| H2 | Wie viele Kalorien, wie viel Zucker und Koffein hat ein Caramel Macchiato? | caramel macchiato kalorien (LSI) |
The existing H2s (Preis, Kalorien & Nährwerte [iced], Kalorien sparen, Rezept, FAQ) are unchanged. The new calorie H2 targets the *hot/all-size* query, and the existing one keeps the iced figure. ⚠️ Two calorie H2s on one page is mild heading overlap. If you'd rather avoid it, merge Block B into the existing "Kalorien & Nährwerte" H2 as a sub-table.

## Step 8e: Links / cannibalisation
Out: /blog/starbucks-latte-macchiato (already compares CM, so we link rather than duplicate), /blog/starbucks-kapseln-angebot.
In (recommend): starbucks-latte-macchiato already links here ✅. Consider linking from /blog/starbucks-menu "Heiße Kaffeegetränke" with the anchor "Caramel Macchiato".
Note: **0 internal links in the blog/ folder use href containing "caramel-macchiato" except via the latte page**, so this page is under-linked.

## Step 10: FAQ source map
10 new + 1 replacement. Q1, Q5 → starbucks.com snippet. Q2, Q6, Q7 → menu.js. Q3, Q4 → fddb/yazio/menu.js. Q8 → US caffeine data. Q9 → site's size data. Q10 → site's kapseln-angebot page. Replacement (Koffein) → US caffeine data.
