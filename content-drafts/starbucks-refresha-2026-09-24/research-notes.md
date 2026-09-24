# Research notes: „starbucks refresha“ (new post)

Run date: 2026-09-24. Volume 480/mo, KD 22. The workbook said "merge into starbucks-menu", but I went with a new post because Refresha is a distinct product line and the menu page gives it one line (user approved the new-post list 24 Sep). Also covers "starbucks teesorten/tee" only via a link (not targeted).

## Step 1: SERP + intent
Query "starbucks refresha sorten preis deutschland" (US tool, so treat it as a proxy): despeisekartes.org/refresha (prices "2025"), fastfood-preisecheck.de, fastfoodpreise.de (Cool Lime price page from **Jan 2016**, stale), preiseinfo.de, starbuckspreise.de (competitor), fastfoodleaks.com, starbucks.de/de/menu-drinks-refresha, starbucks.de refresha product page.
Intent: know (which flavours, price, caffeine?) + a light buy signal. No snippet seen. Fan-out: "refresha koffein", "pink drink deutschland", "refresha kalorien", "cool lime starbucks".

## Step 2: Head entities
- Starbucks Refresha® (Thing, product line). International name "Starbucks Refreshers", no DE Wikipedia article, so it's **unlinked**
- Starbucks (Org) https://de.wikipedia.org/wiki/Starbucks
- Grünkaffee-Extrakt / Green coffee extract https://en.wikipedia.org/wiki/Green_coffee_extract

## Step 4: Sources
- **starbucks.de/de/menu-drinks-refresha** (official): 4 drinks + verbatim descriptions (Mango Dragonfruit, Dragon Coconut, Strawberry Acai, Pink Coconut). No prices, kcal or caffeine.
- **starbucks.de/de/menu/iced-drinks/starbucks-refresha-drink** (official): 6 drinks incl. Frozen Strawberry Acai + Frozen Mango Dragonfruit.
- **Search snippet of starbucks.de/de/menu/product/401801**: Frozen = Refresha base + freeze-dried dragonfruit + Frozen Refresha powder + ice. (The product page fetch returned only nav, so the facts come from the snippet.)
- **food-service.de, 4 Jul 2012**: DE launch 10 Jul 2012, Cool Lime + Very Berry Hibiscus, fruit-juice concentrate + fruit + green coffee extract + ice, Arabica, "low-calorie".
- **starbucks.com MD Refresher nutrition via search snippet**: Grande 90 kcal, 20 g sugar, ~45–50 mg caffeine (US). Third-party dmcoffee: Grande Cool Lime 45 mg.
- **Site menu.js**: Strawberry Acai 6,40 € 87 kcal; Mango Dragonfruit 6,90 € 101; Dragon Coconut 7,40 € 158; Pink Coconut 7,90 € 144. Also Iced Caffè Latte 5,40/128, Caramel Frappuccino 6,90/362, Caramel Cream 358, Matcha Cream 325, Chai Cream 319.
- **despeisekartes**: Strawberry Acai 6,40 € (matches), Pink Coconut 6,90 € (**conflicts** with our 7,90 €). We use our own list.

## Step 6: Entity ledger (tiers)
T1: Refresha, 4 flavours, Frozen variants, Preis, Kalorien, Koffein/Grünkaffee-Extrakt. T2: Kokosdrink, Fruchtsaftkonzentrat, Drachenfrucht/Acai/Erdbeere/Mango, Einführung 2012, Cool Lime/Very Berry Hibiscus, Pink Drink, Refreshers (US), Iced Tea, Frappuccino. T3: Zucker 20 g, App/Stars.
Relationships: Refresha —contains→ Grünkaffee-Extrakt → Koffein · Coconut variant = base + Kokosdrink (+0,50/+1,50 €) · Frozen = base + powder, blended · launched —10 Jul 2012→ with Cool Lime, VBH · Pink Coconut ≈ Pink Drink (US).

## Step 7: Information gain
1. Full flavour/price/kcal table incl. Frozen (competitors list 2–4 items, some stale from 2016/2025).
2. Clear caffeine answer + source (green coffee extract, US 45–50 mg), which none of the DE competitors state.
3. "Which one suits you" decision table + Refresha vs Iced Tea vs Frappuccino comparison.
4. Launch history (2012) and the discontinued Cool Lime, which answers the "cool lime" fan-out.

## Step 8: Heading map
H1 focus "Starbucks Refresha". H2: Was ist (know-simple) → Sorten (H3 classic / H3 frozen) → Preis (table) → Koffein → Kalorien → Entscheidungshilfe → Vergleich → FAQ.

## Step 8e: Links / cannibalisation
Out: /blog/starbucks-preise, /blog/starbucks-kalorien-guide, /blog/starbucks-heisse-schokolade, /blog/starbucks-frappuccino-sorten, /blog/starbucks-getraenke. **In (to add when publishing):** starbucks-menu (Kalte Getränke paragraph mentions Refresha®), starbucks-getraenke. Cannibalisation: none. The menu page only mentions Refresha in passing.
