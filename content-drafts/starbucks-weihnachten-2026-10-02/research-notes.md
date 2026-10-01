# Research notes: starbucks weihnachten 2026

Run date: 2 Oct 2026. Target: starbuckspreise.com `/blog/starbucks-weihnachten`, voice: du. Queue item #7 (~370/mo, must be live by ~19 Oct). Supporting keywords (Autocomplete_Oct2026): starbucks weihnachten 2025 / 2025 deutschland / 2026, weihnachtsbecher (+2025), weihnachtsgetränke, weihnachtskaffee, winter / winter edition, toffee nut (latte, sirup, kapseln, dolce gusto, nespresso), gingerbread (latte, chai, chai latte), adventskalender (+ app, heute, 2025, kaufen).

## Step 1: Intent + SERP

- **Dominant intent:** know (what's on the holiday menu, when does it start). **Secondary:** know-simple (Starttermin, Preis), buy-adjacent (Becher, Christmas Blend, Adventskalender).
- **SERP (WebSearch, US-proxied, de queries):** food-service.de (2018 red cups), ganz-muenchen.de (2005 Christmas article), leadersnet.at (AT Holiday 2025), gutefrage ("Bis wann gibt es Weihnachtsstarbucks?"), starbucksathome.com/de/rezepte, eBay/Kleinanzeigen/Amazon cup listings, stories.starbucks.com/emea (Holiday 2025).
- **SERP features (inferred):** shopping/image pack for Becher, forum result (gutefrage), PAA around "wann", "bis wann". Rendered SERP not checked (Google blocks scraping).
- **Fan-out:** see supporting keywords above + gutefrage question "bis wann".

## Step 2: Sources

| # | Source | Used for |
|---|---|---|
| S1 | web.archive.org snapshot 18 Nov 2025 of starbucks.de/de/menu/featured | DE 2025 lineup: Toffee Nut Latte (+Iced), Lebkuchen Latte (+Iced), Mocha Mousse Latte (+Iced), Winter Spiced Apple Tea, Toffee Nut Matcha Latte, Toffee Nut Cream Iced Matcha Latte, Lebkuchen Matcha Latte, Lebkuchen Cream Iced Matcha Latte, Toffee Nut Coffee/Cream Frappuccino, Lebkuchen Coffee/Cream Frappuccino; food: Apple Caramel Cake, Red Velvet Cookie & Cream Cake, Blueberry-Lemon Curd Cheesecake, Lebkuchen Zimtschnecke, Red Velvet Cake, Cake Pop Polar Bear, Red Velvet Cookie, Sauerteig Cranberry & Brie Sandwich; Christmas Blend 2025 250g, Christmas Blonde 2025 250g |
| S2 | web.archive.org 18 Nov 2025 of starbucks.de/de/article/706/jetzt-wird-es-festlich | descriptions: Mocha Mousse Latte (Signature Espresso, Pralinensauce, Milch, Pralinen-Sahne-Topping, Kakaopulver), Lebkuchen Latte (Espresso, Lebkuchen Sirup, Milch, Zimt), Toffee Nut Latte (Espresso, Toffee Nut Sirup, Milch, Toffee Nut Streusel) |
| S3 | web.archive.org 18 Nov 2025 of starbucks.de/de/article/716/matcha-x-holiday-flavours | 100 % japanischer Matcha; Toffee Nut Cream Iced Matcha (Milch, Eis, TN Flavour Sirup, TN Cream Cold Foam, Sprinkles; also hot with Sahne); Lebkuchen Matcha Latte (Milch, Matcha, Lebkuchen Flavour Sauce, Sahne, Zimt; also iced with Lebkuchen Cream Cold Foam) |
| S4 | starbucks.de/en/article/576 (live, curl 2 Oct) | dated "Nov 04, 2024" (slug your-holiday-faves-are-back) → 2024 start |
| S5 | stories.starbucks.com/emea 2025 "Feeling festive?" (via search snippet; page Cloudflare-blocked) | Holiday menu from 6 Nov 2025 in EMEA, hot drinks in new Red Cup design |
| S6 | leadersnet.at 9 Nov 2025 (AT) | cups with logo + red ribbons; Christmas Blend = Latin America + Indonesia + Aged Sumatra; Blonde + Espresso Roast; whole bean or capsules; tumblers, cold cups, mugs |
| S7 | Starbucks DE "Allergen- und Nährwertinformationen Winter – 12.12.2025 (Food)" PDF, via archived starbucks.de/nutrition 15 Jan 2026 | Lebkuchen Zimtschnecke 120 g/394 kcal/23,8 g; Red Velvet Cake 90/377/25,2; Red Velvet Cookie 72/346/26,6; RV Cookie & Cream Cake 141/533/39,5; Apple Caramel Cake 175/499/47,0; Cake Pop Polar Bär 34/164/14,0 |
| S8 | same release (Nährwerte Getränke) | no Toffee Nut / Lebkuchen rows; Pistachio Velvet Latte, Pistachio Hot Chocolate → Winter = pistachio menu |
| S9 | food-service.de 9 Nov 2018 | first reusable red cup in DE, 2,50 €, up to 30 uses, 0,30 € own-cup discount |
| S10 | ganz-muenchen.de (Christmas 2005) | 2005 Adventskalender: 24 chocolates + 3 coffees, 19,95 €, Coppeneur |
| S11 | kaffeenavigator.de 10 Nov 2008 "endlich Lebkuchen Latte bei Starbucks" (search result title) | Lebkuchen Latte in DE by 2008 |
| S12 | statesman.com / today.com (search snippets) | US Red Cup Day 13 Nov 2025, free reusable cup with holiday drink |
| S13 | starbuckspreise.de (competitor price list, "Dezember 2025") | 2025 prices: Toffee Nut Latte 6,20; Lebkuchen Latte 6,70; Matcha variants 7,40; Winter Spiced Apple Tea 4,20 / 9 kcal. **Third-party, unofficial.** |
| S14 | starbucksfreiburg.de (Freiburg Hbf ordering page), curl 1 Oct 2026 | Herbst comparison prices: PSL 6,20, PSCM 6,40, PS Matcha 7,20, PS Coffee Frapp 7,40, Caffè Latte 4,90 |
| S15 | eBay/Walmart listings via search | Starbucks advent calendar 2025 = 24 K-Cups for Keurig (US) |
| S16 | starbucksathome.com/de/rezepte | Toffee Nut Latte recipe ("Rezept des Monats") |

## Step 3: Metadata

- **Title:** Starbucks Weihnachten 2026: Start, Getränke & Becher (52 chars)
- **H1:** Starbucks Weihnachten 2026: Start, Getränke, Gebäck und Weihnachtsbecher
- **Meta:** see meta.json (150 chars)
- **Slug:** /blog/starbucks-weihnachten
- Alt title: "Starbucks Weihnachtsgetränke 2026: Toffee Nut, Lebkuchen & Co."

## Step 4: Competitors (top 4 distinct, fetched)

| C | URL | Date | Notes |
|---|---|---|---|
| C1 | leadersnet.at/news/94649 | 9 Nov 2025 | AT lineup (Toffee Nut, Gingerbread, Fudge Brownie Hot Choc, Red Velvet Cake Latte, TN/Gingerbread Matcha, RV Iced Matcha), Christmas Blends, drinkware. No FAQ. |
| C2 | food-service.de (rote Becher) | 9 Nov 2018 | 2,50 €, 30 uses, 0,30 € discount. Stale. |
| C3 | ganz-muenchen.de Christmas at Starbucks | 2005 | Toffee Nut, Crème Brûlée Latte, Gingerbread Muffins, Cranberry Bliss Bars, Adventskalender 19,95 €. Very stale. |
| C4 | starbucksathome.com/de/rezepte | live | Toffee Nut Latte recipe only. |
| — | cafefrida.de/winter-starbucks-getraenke, gutefrage.net | — | 403 → substituted |

## Step 5: Extraction (condensed)

- **C1:** Holiday Season 2025, Toffee Nut Latte, Gingerbread Latte, Fudge Brownie Hot Chocolate, Red Velvet Cake Latte, Toffee Nut Matcha Latte, Gingerbread Matcha Latte, Red Velvet Cake Iced Matcha Latte, hot/iced/blended, Classic Christmas Blend, Aged Sumatra, Blonde Roast, Espresso Roast, Bohnen, Kapseln, Tumbler, Cold Cups, Mehrwegbecher, Tassen, Brown Bear. (21)
- **C2:** rote Becher, 2,50 €, 30-mal, 0,30 € Rabatt, Bring Your Own Tumbler, Weihnachtszeit, solange Vorrat, Strohhalme 2020. (8)
- **C3:** Toffee Nut Latte, Crème Brûlée Latte, Gingerbread Muffins, Cranberry Bliss Bars, Christmas Blend 250 g 6,90 €, Adventskalender 24 Schokoladen, Coppeneur, Colombia Nariño, Espresso Roast, Ethiopia Sidamo, 19,95 €, Cheer Party, Bücher spenden. (13)
- **C4:** Toffee Nut Latte, Rezept des Monats, 5 Minuten, aromatisch & nussig. (4)

## Step 6: Entity ledger

See entities.json (30 rows: 7 tier-1, 14 tier-2, 9 tier-3).

**Relationships**
- Weihnachtskarte DE —starts→ 4 Nov 2024 / 6 Nov 2025 → expected early Nov 2026
- Weihnachtskarte —replaces→ Herbstkarte (PSL); —replaced by→ Winterkarte (Pistachio, Jan 2026)
- Toffee Nut Latte —is→ Signature Espresso + Toffee Nut Sirup + Milch + Streusel
- Lebkuchen Latte —is DE name of→ Gingerbread Latte; —in DE since ≤→ 2008
- Mocha Mousse Latte —new in→ 2025; —uses→ Pralinensauce
- Holiday-Matcha —contains no→ Espresso; —uses→ 100 % japanischer Matcha
- "Cream" Frappuccino —has no→ Kaffee; "Coffee" Frappuccino —has→ Kaffee
- Lebkuchen Zimtschnecke —has→ 394 kcal / 120 g
- Red Cup Day —exists only in→ USA (13 Nov 2025, free cup)
- Roter Mehrwegbecher DE —since→ 2018, 2,50 €, 30 uses
- Christmas Blend —is blend of→ Lateinamerika + Indonesien + Aged Sumatra
- Starbucks Adventskalender 2025 —is→ US K-Cup product for Keurig

**Dedupe/parked:** Gingerbread/Lebkuchen merged. Red Velvet Cake Latte + Fudge Brownie Hot Chocolate parked: on AT/EMEA lists, NOT on the DE featured page (S1). Bearista (US craze) parked. Crème Brûlée Latte / Cranberry Bliss (2005) parked as stale.

## Step 7: Information gain

- Competitors are stale (2005, 2018) or Austrian; none has the **German 2025 lineup** (S1–S3: Lebkuchen naming, Mocha Mousse Latte, 4 Holiday-Matcha, Winter Spiced Apple Tea).
- Nobody gives **start dates by year** or the **end (Winterkarte Jan 2026)** → answers gutefrage's "bis wann".
- Nobody explains that the "Starbucks Adventskalender" sold online is a **US Keurig product**.
- **Original element:** "Was hat sich verändert" timeline table (2005–2026) + official kcal table for the holiday bakery.

## Step 8: Heading map

| Lvl | Heading | Owns phrase | Question |
|---|---|---|---|
| H1 | Starbucks Weihnachten 2026: Start, Getränke, Gebäck und Weihnachtsbecher | starbucks weihnachten 2026 | — |
| H2 | 1. Wann startet Starbucks Weihnachten 2026? | ab wann / start | when |
| H3 | Wie lange gibt es die Weihnachtsgetränke? | bis wann / winter edition | until when |
| H2 | 2. Welche Weihnachtsgetränke gibt es bei Starbucks? | weihnachtsgetränke | lineup |
| H3 | Toffee Nut Latte | toffee nut latte | — |
| H3 | Lebkuchen Latte | gingerbread / lebkuchen latte | — |
| H3 | Mocha Mousse Latte | mocha mousse | — |
| H3 | Holiday-Matcha: Toffee Nut und Lebkuchen | toffee nut matcha | — |
| H3 | Frappuccinos und Winter Spiced Apple Tea | weihnachts frappuccino | — |
| H2 | 3. Was kosten die Weihnachtsgetränke bei Starbucks? | preis | price |
| H2 | 4. Welches Weihnachtsgebäck gibt es bei Starbucks? | weihnachtsgebäck | food |
| H2 | 5. Gibt es bei Starbucks Weihnachtsbecher? | weihnachtsbecher | cups |
| H2 | 6. Christmas Blend und Weihnachtskaffee für zu Hause | weihnachtskaffee | at home |
| H3 | Gibt es einen Starbucks Adventskalender? | adventskalender | — |
| H2 | 7. Was hat sich bei Starbucks Weihnachten verändert? | weihnachten 2025 vs 2026 | info gain |
| H2 | Häufig gestellte Fragen | — | 10 Q |

**Internal links (out):** pumpkin-spice-latte, app, latte, mocha, matcha-latte, frappuccino-sorten, preise, gebaeck (new, same batch), becher-aktuell, kapseln-angebot, angebote.
**Inbound candidates:** starbucks-latte ("Toffee Nut Latte"), starbucks-pumpkin-spice-latte ("Weihnachtskarte"), starbucks-becher-aktuell, starbucks-menu, starbucks-getraenke, blog/index.
**Cannibalisation:** none. becher-aktuell covers cup drops generally; this page owns the seasonal-menu intent and links there for cups.

## FAQ source map

2026 Start (fan-out "2026"), ganzjährig (gutefrage-style), Gingerbread vs Lebkuchen (fan-out), vegan (follow-up), wenigste Kalorien (PAA-style), App (internal), Mocha Mousse (S2), Peppermint Mocha (US-searcher follow-up), Christmas Blend (C1/C3), Rabatte (follow-up).
