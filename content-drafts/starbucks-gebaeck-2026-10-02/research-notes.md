# Research notes: starbucks gebäck

Run date: 2 Oct 2026. Target: starbuckspreise.com `/blog/starbucks-gebaeck`, voice: du. Queue item #9 (~100/mo). Supporting keywords (Autocomplete_Oct2026): kuchen (bestellen, kalorien, karotte, nährwerte, preise, rezepte, thermomix), muffin (cheesecake, kalorien, preis, muffins blueberry, rezept), cookie (kalorien, cookies), zimtschnecke (+ pistazien zimtschnecke).

## Step 1: Intent + SERP

- **Dominant intent:** know-simple (Preise, Kalorien of individual items). **Secondary:** know (what's in the range), do (bestellen).
- **SERP (WebSearch):** price-list aggregators (starbuckspreise.de, meinespeisekarten.de, fastfood-preischeck.de, speisekartemenus.de, burgerspreises.de, schmackhafte-speisen.de), fatsecret.de / fddb.info item pages (Zimtschnecke Klassik 355 kcal, Lebkuchen Zimtschnecke 394), starbucks.de/menu/food/desserts.
- **SERP features (inferred):** tables in snippets (price lists), nutrition rich results from fddb/fatsecret, PAA around kcal.
- **Fan-out:** see supporting keywords.

## Step 2: Sources

| # | Source | Used for |
|---|---|---|
| S1 | Starbucks DE "Allergen- und Nährwertinformationen Autumn – 10.09.2026 (Food)" PDF (starbucks.de/nutrition, pypdf, 71 rows mapped to names in order; check: Carrot Cake 181 g/817, Zimtschnecke 355 match fddb/competitors) → `_food-autumn-2026.json` | every weight / kcal / sugar / protein; vegan + vegetarisch flags (only Croissant + Pain au chocolat vegan; NY Cheesecake + Pistachio Raspberry Lover Cake not vegetarian); Chocolate Brownie row without wheat letter; cross-contamination note "Eine Kreuzkontamination … in unserer Pastry kann nicht ausgeschlossen werden" |
| S2 | starbucksfreiburg.de (Freiburg Hbf ordering page, Lieferando-run), curl 1 Oct 2026 | every price; DE product descriptions (Carrot Cake, Zimtschnecke, Blaubeer Muffin, Apple Crumble, Signature Cones, Pastel de Nata); categories "Autumn Specials – Food"; Bundles: Kuchenträume 6 Kuchen 22,70 €, Muffins zum Teilen 5 for 15,90 €, Cozy Cinnamon Collection 3 for 11,40 €, Homeoffice Favourites 14,40 € |
| S3 | Starbucks DE Winter 12.12.2025 Food PDF (via archived starbucks.de/nutrition, 15 Jan 2026) | Lebkuchen Zimtschnecke 394 kcal; Cherry Cream Muffin vegan "ja"; Zitronenkuchen/Marmorkuchen/Carrot Cake/NY Cheesecake/Chocolate Lover Cake also in winter |
| S4 | Same Autumn 2026 drinks PDF | Caffè Latte Grande Halbfettmilch 151 kcal |
| S5 | blog/starbucks-app.html (own site) | 3 Sterne pro Euro; Freigetränk = 150 Sterne |

## Step 3: Metadata

- **Title:** Starbucks Gebäck 2026: Kuchen, Muffins & Zimtschnecken (54 chars)
- **H1:** Starbucks Gebäck 2026: Kuchen, Muffins, Cookies und Zimtschnecken mit Preisen und Kalorien
- **Meta:** see meta.json (145 chars)
- **Slug:** /blog/starbucks-gebaeck
- Alt title: "Starbucks Kuchen & Muffins: alle Preise und Kalorien 2026"

## Step 4: Competitors

| C | URL | Date | Notes |
|---|---|---|---|
| C1 | starbuckspreise.de (bakery section) | "Dezember 2025" | Breakfast Bakery / Muffins / Cookies / Cakes / Brownies / Cake Pop; price + kJ/kcal. Winter 2025 range, now stale (Lebkuchen, Red Velvet). |
| C2 | meinespeisekarten.de/starbucks-menu | 24 Jul 2026 | Breakfast Bakery / Muffins / Cookies / Kuchen & Cheesecakes / Cake Pops; prices ~0,40–0,60 € higher than S2 (probably delivery prices); no kcal; 10 generic FAQs. |
| C3 | fastfood-preischeck.de/starbucks-preise | "2026" (title) | "American Bakery" table with clearly old prices (Muffins 2,79 €, Zimtschnecke 2,59 €), brownie "glutenfrei". 5 generic FAQs. |
| C4 | fatsecret.de / fddb.info item pages | — | per-item kcal (Zimtschnecke Klassik 355 kcal / 120 g, 15,2 g Fett, 47,8 g KH). |

## Step 5: Extraction (condensed)

- **C1:** Lebkuchen Zimtschnecke 4,80 €, Signature Cone Pistachio/Hazelnut 2,10 €, Croissant vegan 2,40 €, Zimtschnecke 3,60 €, Blaubeer Muffin 3,80 €, Chocolate Cheesecake Muffin, Triple Chocolate Muffin, Choc Chunk Cookie 2,90 €, Double Choc Cookie, Red Velvet Cookie, Red Velvet Cake, Carrot Cake 3,99 €/817 kcal, NY Cheesecake 4,80 €, Mini Pastel de Nata 1,80 €, Banana Bread, Zitronenkuchen, Marmorkuchen, Chocolate Brownie, Cake Pop Polar, kJ/kcal. (20)
- **C2:** Strawberry Lemon Swirl, Carrot Cake Zimtschnecke, UBErry Zimtschnecke, Signature Cones, Banana-Caramel Cheesecake Muffin, Matcha Cherry Blob Muffin, Pistachio Ricotta Muffin, Cherry Cream Muffin, Ruby Chocolate-Macadamia Cookie, Bunny Cup Cookie, Grande Pistachio Cookie, Calamansi-Mango Lover Cake, Pink Velvet Cake, Caramelised Banana Loaf Cake, Pistachio Velvet Latte Cake, Strawberry Matcha Lover Cake, Passion Dream Cheesecake, UBE Cake, Strawberry Heart, Dorayaki-Style Pancake, Cake Pops (Flamingo, Little Chick, Love Bear, Brown Bear, Pistachio Dream), vegan, glutenfrei FAQ. (26)
- **C3:** American Bakery, Lemon Muffin, Triple Chocolate Muffin, Schoko Torte, Himbeer Stracciatella Kuchen, Veganer Apfelkuchen, Saftiger Zitronenkuchen, Double Chocolate Cookie, Veganer Sweetheart Donut, Zimtschnecke 2,59 €, Brownie glutenfrei. (11)
- **C4:** Zimtschnecke Klassik, 355 kcal, 120 g, Fett 15,2 g, Kohlenhydrate 47,8 g, Eiweiß 6,7 g, Lebkuchen Zimtschnecke 394 kcal, Pflaumen-Zimt Muffin 478 kcal, Himbeer-Cheesecake Muffin. (9)

## Step 6: Entity ledger

See entities.json (25 rows: 8 tier-1, 12 tier-2, 5 tier-3).

**Relationships**
- Starbucks Gebäck —ranges→ 1,70 € (Pastel de Nata) … 5,40 € (Lover Cakes); 86 … 817 kcal
- Carrot Cake —has→ 817 kcal / 181 g / 58 g Zucker / 8,5 g Eiweiß; —is→ Karottentorte mit Cheesecake-Crème und Rosinen
- Zimtschnecke Klassik —costs→ 3,80 €; —has→ 355 kcal; —filled with→ Butter + Zimt-Zucker
- Muffins —cost→ 3,80–4,10 €; —have→ 408–473 kcal; 5er-Bundle 15,90 € (−3,10 €)
- Passion Dream Cheesecake —is→ lowest-kcal cake slice (339)
- NY Cheesecake, Pistachio Raspberry Lover Cake —are not→ vegetarisch
- Only Croissant + Pain au Chocolat —are→ vegan (Autumn 2026)
- Chocolate Brownie —listed without→ glutenhaltiges Getreide; cross-contamination possible
- "Ofenfrisch" —marks→ Pastel de Nata, Signature Cones, Croissant, Pain au Chocolat
- Cake Pops —cost→ 2,80 €; —have→ 101–168 kcal

**Dedupe/parked:** Lemon Loaf = Zitronenkuchen, Marble Loaf = Marmorkuchen (merged names). Items in S1 without a Freiburg price and out of season (Calamansi-Mango, Pink Velvet, Strawberry Lemon Swirl, Easter cake pops) parked. Recipes/Thermomix (copycat intent) parked → separate article. C3's old prices parked as stale. Croissants/bagels parked → /blog/starbucks-fruehstueck.

## Step 7: Information gain

- C1 is the winter 2025 range; C3 has prices ~1 € too low (old); C2 has no kcal. **None has current official kcal + current price side by side.**
- No competitor gives **sugar** values, the **lowest/highest kcal ranking**, the **bundle savings maths**, or the **vegetarian warning** (NY Cheesecake).
- "Pistazien Zimtschnecke" (fan-out) is answered (not on the current list + where pistachio is instead).
- **Original element:** kcal ranking table (top 5 lowest vs highest) + per-category price/kcal/sugar tables from the official PDF.

## Step 8: Heading map

| Lvl | Heading | Owns phrase | Question |
|---|---|---|---|
| H1 | Starbucks Gebäck 2026: Kuchen, Muffins, Cookies und Zimtschnecken mit Preisen und Kalorien | starbucks gebäck | — |
| H2 | 1. Welches Gebäck gibt es bei Starbucks? | gebäck sortiment | range |
| H2 | 2. Was kostet ein Kuchen bei Starbucks? | kuchen preise / kalorien | price |
| H3 | Carrot Cake: der Kuchen mit den meisten Kalorien | kuchen karotte | — |
| H3 | Cheesecake bei Starbucks | cheesecake | — |
| H3 | Kuchen bestellen und teilen | kuchen bestellen | — |
| H2 | 3. Was kostet ein Muffin bei Starbucks? | muffin preis / kalorien | — |
| H2 | 4. Welche Cookies und Brownies gibt es bei Starbucks? | cookies | — |
| H2 | 5. Welche Zimtschnecken gibt es bei Starbucks? | zimtschnecke | — |
| H3 | Gibt es eine Pistazien-Zimtschnecke bei Starbucks? | pistazien zimtschnecke | — |
| H2 | 6. Cake Pops und kleines Gebäck | cake pop | — |
| H2 | 7. Welches Starbucks Gebäck hat die wenigsten Kalorien? | kuchen nährwerte | info gain |
| H2 | 8. Gibt es veganes Gebäck bei Starbucks? | vegan | — |
| H2 | Häufig gestellte Fragen | — | 10 Q |

**Internal links (out):** fruehstueck, weihnachten (new, same batch), kalorien-guide, vegane-optionen, app, preise.
**Inbound candidates:** starbucks-fruehstueck (Zimtschnecke mention), starbucks-menu (Essen section), starbucks-preise (food rows), starbucks-kalorien-guide, starbucks-vegane-optionen, blog/index.
**Cannibalisation:** low. fruehstueck mentions Zimtschnecke as a breakfast option; this page owns the sweet bakery/kcal intent. Consider linking fruehstueck's Zimtschnecke mention here.

## FAQ source map

Zimtschnecke Preis (fan-out), Muffin Kalorien (fan-out), Carrot Cake Kalorien (fan-out "karotte"), frisch (S2 "Ofenfrisch"), bestellen (fan-out), glutenfrei (C2/C3 FAQ), Cake Pop (follow-up), beliebteste (follow-up), App (internal), nur im Herbst (S2 category).
