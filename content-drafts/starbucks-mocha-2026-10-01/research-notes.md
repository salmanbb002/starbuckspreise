# Research notes: starbucks mocha

Run date: 1 Oct 2026. Target: starbuckspreise.com `/blog/starbucks-mocha`, voice: du. Queue item #6 (~410/mo, peaks Nov).

## Step 1: Intent + SERP

- **Dominant intent:** know (what it is + price/kcal/caffeine). **Secondary:** know-simple (Preis, Kalorien), do (Rezept / selber machen).
- **SERP (WebSearch, US-proxied, de queries):** starbuckspreise.de (home + "Caffè Mocha: Die perfekte Verbindung…" + white-mocha post), starbucks.de/de/menu/product/107197 (JS shell, no content fetched), fddb.info, en.wikipedia Caffè mocha, starbucksathome.com/de/rezepte/caffe-mocha, US menu clones (starbucks-menus.com, starbucksreserveonly.com, bucksmenu.store), supermarktcheck.de (Frappuccino Mocha bottle 263 g).
- **SERP features (inferred):** paragraph snippet for definition/price; image pack; PAA around Koffein, Kalorien, Unterschied White Mocha. Rendered SERP not checked (Google blocks scraping, see project memory).
- **Fan-out (Autocomplete_Oct2026):** starbucks mocha, mocha coffee, mocha frappuccino, mocha frappuccino kalorien, mocha frappuccino rezept, mocha latte, mocha pulver, mocha sauce, mocha cookie crumble, dolce gusto white mocha.

## Step 2: Head-entity sources

| # | Source | Used for |
|---|---|---|
| S1 | en.wikipedia.org/wiki/Caffè_mocha | definition (chocolate variant of latte), aliases mocaccino/mochaccino, name from port of Mokha, Yemen, coffee trade 15th–17th c. |
| S2 | Starbucks DE "Allergen- und Nährwertinformationen Autumn – 10.09.2026 (Getränke Nährwerte)" PDF, pypdf | every kcal/Zucker/Fett/Eiweiß/Koffein value: Mocha by size × milk; White Mocha; Iced Mocha; Iced White Mocha; Mocha Frappuccino × milk; Decaf Mocha Frapp; Blonde Mocha; Decaf Mocha; Classic Hot Chocolate; Caffe Latte; Caramel Macchiato |
| S3 | Starbucks DE Allergen PDF (Getränke), same release | "Caffé Mocha mit Sahne", plant milk = `nein***`; footnote *** "mit Soja-/Kokos-/Hafer-/Mandeldrink, veganer Schlagcreme und ohne Topping vegan"; White Chocolate Mocha with plant milk = `ja` (vegan); Ristretto Mocha present; components "Bar Mocha Syrup" (17 g/pump), "Bar Mocha Powder" |
| S4 | starbucksfreiburg.de (online ordering page, Freiburg Hbf), curl 1 Oct | prices: Caffè Mocha 5,90; Iced Caffè Mocha 5,90; White Chocolate Mocha 6,40; Iced WCM 6,40; Mocha Frapp 6,40; WCM Frapp 6,90; WCM Cream Frapp 6,90; Java Chip 6,90; Classic Hot Chocolate 5,90; DE descriptions quoted |
| S5 | starbucksathome.com/de/rezepte/caffe-mocha | home recipe: 1 shot, 1 Tasse Milch, 2 EL Schokoladensoße, Sahne, Schokoraspel |
| S6 | starbucksathome.com/de/produkte/starbucks-white-mocha + dolce-gusto.de + Kaufland/frogcoffee listings | Dolce Gusto White Mocha: 6 portions / 12 capsules, 170 ml milk + 30 ml coffee = 200 ml, from ~5,99 € |
| S7 | lifestyleofafoodie.com / coffeecopycat.com (copycat sauce) | sauce ratio ½ cup water, ½ cup sugar, ⅓ cup cocoa, ⅛ tsp salt, ½ tsp vanilla, simmer 2 min |
| S8 | maxicoffee.de listing | "Starbucks löslicher Kaffee White Mocha 115 g" |
| S9 | Caffè Latte 4,90 € (Freiburg Hbf) | from PSL run S3 (29 Sep), not re-checked |

## Step 3: Metadata

- **Title:** Starbucks Mocha 2026: Preis, Kalorien, Koffein & Sorten (55 chars)
- **H1:** Starbucks Mocha 2026: Preis, Kalorien, Koffein und alle Sorten
- **Meta:** Starbucks Caffè Mocha 2026: 5,90 €, 281 kcal und 113 mg Koffein im Grande. Plus White Chocolate Mocha, Iced Mocha, Mocha Frappuccino und Rezept. (148)
- **Slug:** /blog/starbucks-mocha
- Alt title: "Starbucks Caffè Mocha: Was steckt drin und was kostet er?"

## Step 4: Competitors (top 4 distinct, fetched)

| C | URL | Type | Date | Notes |
|---|---|---|---|---|
| C1 | starbuckspreise.de/caffe-mocha-die-perfekte-verbindung-von-kaffee-und-schokolade/ | blog | none shown | H2: Was macht den Caffè Mocha besonders? / Preis und Nährwerte im Überblick / Für wen eignet sich der Caffè Mocha? / Fazit. 5,90 €, 283 kcal. No FAQ. |
| C2 | starbucksathome.com/de/rezepte/caffe-mocha | recipe | none | Ein STARBUCKS®-Klassiker / Was du benötigst / So wird's gemacht (5 steps). No FAQ. |
| C3 | en.wikipedia.org/wiki/Caffè_mocha | encyclopedia | live | definition, etymology (Mokha), bicerin/bavareisa, variants (white, tuxedo, mochaccino, frappuccino), ~152 mg/350 ml |
| C4 | fddb.info Starbucks Café Mocha | nutrition DB | upd. 3 Feb 2026 | 70 kcal/100 ml, Grande "453 ml" 316 kcal, caffeine 0 mg, "Angaben noch nicht bestätigt" |
| — | starbucks.de/de/menu/product/107197 | official | — | WebFetch returned nav shell only (JS) → substituted by S2/S4 |

## Step 5: Extraction (condensed)

- **C1:** Espresso, Schokoladensirup, aufgeschäumte Milch, Sahne, Kakaopulver, Preis 5,90 €, 1187 kJ / 283 kcal, Schokoladenliebhaber, kalte Tage, Lebkuchen Latte, Pumpkin Spice Latte, Genuss. (12)
- **C2:** Espresso-Shot, Milch deiner Wahl, 2 EL Schokoladensoße, Schlagsahne, Schokoladenraspeln, Tasse, aufschäumen, Starbucks-Klassiker, Espresso Roast. (9)
- **C3:** caffè mocha, mocaccino, mochaccino, caffè latte, Mokha, Yemen, coffee trade 15th–17th c., bavareisa, bicerin, Turin, cocoa powder, sugar, whipped cream, milk froth, white caffè mocha, tuxedo/marble mocha, Frappuccino, 152 mg/350 ml. (18)
- **C4:** Kalorien 70 kcal/100 ml, Eiweiß 2,8 g, Kohlenhydrate 9,1 g, Zucker 6 g, Fett 3,2 g, Grande 453 ml 316 kcal, Koffein 0 mg, vegetarisch. (8)

## Step 6: Entity ledger

See entities.json (29 rows: 9 tier-1, 12 tier-2, 8 tier-3).

**Relationships**
- Caffè Mocha —is→ Caffè Latte + Mocha-Sauce + Sahne
- Caffè Mocha —named after→ Mokka (Jemen)
- Mocha-Sauce —adds→ ~24 mg Koffein (Grande; 113,4 − 89,1)
- Espresso shot —has→ 44,5 mg (DE); Tall/Grande 2 shots, Venti 3
- Caffè Mocha Grande Halbfett —has→ 281 kcal / 30,1 g Zucker / 113,4 mg
- White Chocolate Mocha —uses→ weiße Schokoladensauce; —has→ 345 kcal / 45,4 g / 89,1 mg
- Classic Hot Chocolate —= Mocha-Sauce without espresso→ 309 kcal / 26,1 mg
- Mocha Frappuccino —uses→ coffee base, not shots → 37,9 mg
- Milchsorte —changes→ Grande by up to 86 kcal (Mandel 230 … Vollmilch 316)
- Caffè Mocha + Pflanzendrink —vegan only with→ veganer Schlagcreme (S3 ***)
- White Chocolate Mocha + Pflanzendrink —is→ vegan (S3)
- Mocha Cookie Crumble Frappuccino —not on→ DE menu 2026 (absent S2 + S4)
- Dolce Gusto White Mocha —is→ 12 capsules = 6 drinks à 200 ml

**Dedupe/parked:** "Café Mocha"/"Caffè Mocha"/"Mocha" merged. fddb values parked (unconfirmed, conflict with official). Iced Mocha Mousse Latte (in site menu.js, not in Autumn PDF or Freiburg menu) parked. Lebkuchen Latte / PSL (C1 cross-promo) parked as off-topic.

## Step 7: Information gain

- All competitors use stale or wrong values: C1 283 kcal (official Grande now 281), C4 claims 0 mg caffeine and 453 ml Grande; SERP summaries quote 89,1 mg caffeine. None mention that **Mocha-Sauce adds caffeine** (official 113,4 mg Grande).
- No competitor has **official DE nutrition by size and by milk**, the **vegan rule from the DE allergen list**, or a **Mocha vs White Mocha vs Hot Chocolate comparison table** (our original element).
- Nobody answers "Mocha Cookie Crumble in Deutschland?" → answered (not on DE menu).

## Step 8: Heading map

| Lvl | Heading | Owns phrase | Question | Entities |
|---|---|---|---|---|
| H1 | Starbucks Mocha 2026: Preis, Kalorien, Koffein und alle Sorten | starbucks mocha | — | Caffè Mocha, Starbucks |
| H2 | 1. Was ist ein Starbucks Mocha? | mocha coffee / was ist | definition | Espresso, Mocha-Sauce, Sahne, Mokka |
| H3 | Mocha, Latte oder heiße Schokolade? | mocha latte | difference | Caffè Latte, Classic Hot Chocolate |
| H2 | 2. Was kostet ein Mocha bei Starbucks? | preis | price | S4 table |
| H2 | 3. Wie viele Kalorien und wie viel Koffein…? | kalorien / koffein | nutrition | S2 |
| H3 | Kalorien und Koffein nach Größe | größen | by size | Short–Venti |
| H3 | Kalorien nach Milchsorte | milch | by milk | 7 milks, Decaf, Blonde |
| H2 | 4. Unterschied zum White Chocolate Mocha? | white chocolate mocha | comparison | info-gain table |
| H3 | Vegan und laktosefrei | vegan | allergen | S3 |
| H2 | 5. Welche Mocha-Sorten gibt es kalt? | iced | cold variants | — |
| H3 | Iced Caffè Mocha | iced mocha | — | S2 |
| H3 | Mocha Frappuccino und Kalorien | mocha frappuccino kalorien | — | S2 |
| H3 | Mocha Cookie Crumble Frappuccino | mocha cookie crumble | availability | S2/S4 |
| H2 | 6. Wie macht man einen Starbucks Mocha selber? | rezept | do | HowTo |
| H3 | Rezept für die Mocha-Sauce | mocha sauce | steps | S7 |
| H3 | Caffè Mocha zusammenbauen | (assembly) | steps | S5 |
| H3 | Starbucks White Mocha für Dolce Gusto | dolce gusto white mocha | at home | S6 |
| H2 | Häufig gestellte Fragen | — | 10 Q | — |

**Internal links:** /blog/starbucks-heisse-schokolade, /blog/starbucks-preise, /blog/starbucks-kalorien-guide, /blog/starbucks-vegane-optionen, /blog/starbucks-frappuccino-sorten, /blog/starbucks-kapseln-angebot, /blog/starbucks-app. **Inbound candidates** (for add_inbound_links.py): starbucks-getraenke, starbucks-kaffee (lists "Mocha"), starbucks-latte, starbucks-heisse-schokolade, starbucks-menu, starbucks-frappuccino-sorten.
**Cannibalisation:** none. No page targets "mocha"; heisse-schokolade covers Hot Chocolate only.

## FAQ source map

Koffein (fan-out + info gain), süßer als Caramel Macchiato (follow-up), Sahne (C1/C2), Mochaccino (C3 alias), Decaf / Blonde / Ristretto (S2/S3 variants), wenigste Kalorien (PAA-style), App (internal), Supermarkt (supermarktcheck + S6/S8).

## Open flags (need user)

1. **Price conflict on /blog/starbucks-preise:** its size table lists Caffè Mocha and White Chocolate Mocha at 4,90/5,50/6,20 €, but the Freiburg ordering page has 5,90 / 6,40 € (one price, no size). The same type of conflict was already flagged for PSL.
2. **menu.js is stale for mochas:** White Chocolate Mocha 5,99 €, Iced Caffè Mocha 5,79 € / 340 kcal, WCM Frappuccino 5,79 €, WCM Cream Frapp 5,29 €, Mocha Frapp 6,90 €. Freiburg prices are 6,40 / 5,90 / 6,90 / 6,90 / 6,40 €.
3. **White Chocolate Mocha Frappuccino** has no row in the Autumn nutrition PDF, so the draft gives no kcal for it.
4. Dolce Gusto price "ab 5,99 €" comes from retailer listings and changes often.
