# Research notes: starbucks coffee choices / starbucks coffee drinks

**Run:** 26 Sep 2026 · merge into `blog/starbucks-kaffee.html` · Calendar Days #85 (390, KD 34) + #87 (320, KD 30)

## Intent + SERP
- English query, *know* intent: „which coffee drinks does Starbucks have and how do they differ“.
- **Results (WebSearch, 26 Sep):** chowhound (iced coffee types), athome.starbucks.com (roast finder, product overview), tastingtable (47 drinks ranked), coffeeteaculture.com („The Starbucks Drinks Menu, Explained“), starbucksmenu1.com (calories, caffeine, sizes), starbucks.com/menu, amazingfoodanddrink.com, scribd drink list, parade (espresso types), moonandspoonandyum (23 espresso drinks).
- **Recurring competitor framing:** three bases (espresso / brewed / none), three roasts (Blonde/Medium/Dark), espresso + milk ratios (latte vs cappuccino vs flat white vs macchiato), four iced coffee types (iced coffee, iced espresso, cold brew, nitro), calories/caffeine by size.
- All are **US-menu** based (US caffeine values, US sizes). None reflects German caffeine values.
- **starbucks.de/menu/drinks/hot-drinks (fetched 26 Sep):** Espresso, Espresso Macchiato, Espresso Con Panna, Café Crème, Caffè Misto, Caffè Americano, Flat White, Caffè Latte, Latte Macchiato, Cappuccino, Caramel Macchiato, Caffè Mocha, White Chocolate Mocha, Soy Protein Vanilla Latte, Ristretto Mocha (+ seasonal). Iced: … Aerocano™ … The nutrition PDF is **not** a complete menu list.

## Sources
Starbucks DE Nährwerte Getränke Autumn 10.09.2026 (caffeine, kcal, which drinks exist on the DE menu); `menu.js` (prices); `/blog/starbucks-menu` (extra shot ≈ 0,80 €).

## Entity ledger (summary)
Tier 1: Starbucks coffee drinks, Espresso, brewed coffee, caffeine. Tier 2: Americano, Cappuccino, Latte, Latte Macchiato, Flat White, Caramel Macchiato, Mocha, Cold Brew, Frappuccino, Blonde, Decaf, kcal, price. Tier 3: Espresso Con Panna, Caffè Misto, Café Crème, Ristretto Mocha, Aerocano™ (on starbucks.de/menu, but no DE nutrition data, so named only), Nitro Cold Brew (per-store feature).
**Relationships:** base —determines→ strength · milk/syrup —determine→ kcal · Grande Latte = Cappuccino = Caramel Macchiato → 2 shots · Americano Grande → 3 shots · Frappuccino —uses→ coffee base (31,4 mg) · Filterkaffee → strongest (254,6 mg).

## Heading map
H3 „Starbucks Coffee Drinks im Vergleich …“ → *starbucks coffee drinks*; H3 „Welcher Starbucks Kaffee passt zu Ihnen?“ → *starbucks coffee choices*; 4 FAQ.

## Info gain
First comparison of base × shots × caffeine × kcal × price using **German** official values; a choice matrix .

## Cannibalisation
`/blog/starbucks-kalorien-guide` (after its rewrite) owns kcal/nutrition, so this block shows kcal as one column and links there. `/blog/starbucks-latte` owns the latte family. No conflict.
