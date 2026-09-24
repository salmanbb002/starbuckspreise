# Research notes: „starbucks latte“ (new post)

Run date: 2026-09-24. Keywords "starbucks latte" 320 (KD 30) + "latte starbucks drinks" 320 (KD 21). The workbook said "merge into starbucks-kaffee". I went with a new post because there's no Caffè Latte page and the query wants the latte family (a hub for every "… Latte" drink).

## Step 1: SERP + intent
Query "starbucks caffè latte preis kalorien deutschland": germanmenus.de, speisekartemenus.de, starbuckspreise.de (+ its Iced Caffè Latte post), burgerspreises.de, fastfood-preisecheck.de, fastfoodleaks.com; Wikipedia Milk coffee / Café au lait. Query "starbucks latte sorten deutschland": dolce-gusto.de Caffè Latte capsules, starbucks.de iced coffees, starbuckschilledcoffee.com Caffè Latte.
Intent: know (price, calories, which lattes) + comparison. Price-list sites dominate. Fan-out: "starbucks latte preis", "latte vs cappuccino", "starbucks latte kalorien", "chai latte starbucks".

## Step 2: Head entities
Caffè Latte (Thing) https://de.wikipedia.org/wiki/Caff%C3%A8_Latte · Starbucks (Org) · Latte macchiato https://de.wikipedia.org/wiki/Latte_macchiato · Cappuccino https://de.wikipedia.org/wiki/Cappuccino · Flat White https://de.wikipedia.org/wiki/Flat_White · Chai https://de.wikipedia.org/wiki/Chai · Matcha https://de.wikipedia.org/wiki/Matcha.

## Step 4: Sources
- **Site menu.js** (all prices/kcal in the draft): 21 latte items + Latte Macchiato 4,70/147, Flat White 4,71/76, Cappuccino 3,90/130, Protein Drink Caffe Latte 2,94/168.
- **starbucksmenususa.com/caffe-latte** (third-party, US): Short 100/Tall 150/Grande 190/Venti 250 kcal; caffeine 75/75/150/150 mg; prep "espresso into steamed milk, topped with foam". FAQs used for fan-out.
- **fatsecret/fddb search snippets**: Tall 124–150 kcal (varies by milk). We keep our own 151.
- **dolce-gusto.de**: "Starbucks® Caffè Latte – 12 Kapseln". **starbuckschilledcoffee.com/de**: Chilled Classics Caffè Latte exists. **discounto**: chilled Caffè Latte 2,99 € in offers.
- Search summary: plant milk surcharge ~0,50 € (third-party). The draft only says "kleiner Aufpreis".

## Step 6: Entity ledger
T1: Caffè Latte, Preis 4,59, Kalorien 151, Latte-Sorten (hot/iced/tea), Espresso, Milch/Milchschaum, Koffein. T2: Iced Caffè Latte, Cold Brew Latte, Toffee Nut, Tiramisu Velvet, PSL, Lebkuchen, Mocha Mousse, Chai Tea Latte, Matcha variants, Latte Macchiato, Flat White, Cappuccino, sizes, Dolce Gusto, Chilled, Protein Drink. T3: Hafermilch/Pflanzendrink, 2 %-Milch, Italian etymology.
Relationships: Caffè Latte = espresso first + steamed milk + thin foam · flavoured lattes = Caffè Latte + syrup/topping · tea lattes —no espresso, caffeine from→ chai/matcha · Tall 75 / Grande 150 mg · cheapest milk drink = Cappuccino 3,90; lowest kcal latte = Iced Matcha 122 / coffee latte = Cold Brew Latte 123; most expensive = Iced PSL Matcha 8,90.

## Step 7: Information gain
1. **Complete latte price+kcal ladder (21 drinks)** in 3 tables. Competitors give 1–5 lattes.
2. **4-way comparison** Latte / Latte Macchiato / Flat White / Cappuccino with our prices.
3. Decision table + "latte at home" (3 retail formats).

## Step 8e: Links / cannibalisation
Out: /blog/starbucks-preise, /blog/starbucks-iced-coffee, /blog/starbucks-kalorien-guide, /blog/starbucks-latte-macchiato, /blog/starbucks-flat-white, /blog/starbucks-angebote (new, publish together). **Cannibalisation:** latte-macchiato owns "latte macchiato", flat-white owns "flat white", and iced-coffee holds the "iced caffe latte starbucks" merge row. This post targets the head term "starbucks latte" and keeps those as links + one comparison row each. **In-links to add when publishing:** starbucks-latte-macchiato, starbucks-flat-white, starbucks-kaffee.
