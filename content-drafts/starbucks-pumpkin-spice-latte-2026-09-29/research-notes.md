# Research notes: starbucks pumpkin spice latte (+ Herbst 2026)

Run date: 29 Sep 2026 · Site: starbuckspreise.com (DE, du-voice) · Page type: blog post · Slug: `/blog/starbucks-pumpkin-spice-latte`

## Step 1: Intent + SERP
- **Demand:** Google Trends DE (12 months) gives about 500/mo for "starbucks pumpkin spice latte" and about 110/mo for "starbucks herbst" (anchored on "starbucks kalorien" = 480). Searches peaked 23–29 Aug 2026 and are **seasonal (Aug–Nov)**.
- **Intent:** mainly *know* (price, kcal, availability), with *buy/visit* as a secondary intent.
- **SERP (German DuckDuckGo scrape, 29 Sep, before the rate limit):** starbucks.de, about.starbucks.com, starbucks.de, starbucks.com, starbucksathome.com, ad-hoc-news.de, starbucks.ch. Google SERP not captured: captcha in the automation browser.
- **Expected features:** PAA ("wie viel kostet…", "wie viele kalorien…", "ab wann…"), image pack, news box in season.
- **Fan-out (Google Autocomplete DE, 29 Sep):** starbucks pumpkin spice latte 2026 / 2026 deutschland / ab wann / instant / pulver; starbucks preise pumpkin spice latte; was kostet starbucks pumpkin spice latte; starbucks pumpkin spice frappuccino; starbucks sirup pumpkin spice; starbucks nespresso (kapseln) pumpkin spice; starbucks dolce gusto pumpkin spice latte; starbucks herbst 2026 / herbst getränke 2026 / herbst menü / herbst merch; starbucks deutschland pumpkin spice latte.

## Step 2: Head-entity sources
| # | Source | Used for |
|---|---|---|
| S1 | starbucks.de/menu/drinks/hot-drinks, /iced-drinks, /matcha (WebFetch, 29 Sep) | DE seasonal lineup: PSL, Pumpkin Spice Caramel Macchiato, Pecan Maple Flavour Macchiato (+ iced), Iced Apple Crumble Cream Matcha, Pumpkin Spice Matcha Latte, Pumpkin Cream Iced Matcha Latte |
| S2 | Starbucks DE "Allergen- und Nährwertinformationen Autumn – 10.09.2026 (Getränke Nährwerte)" PDF, pypdf | every kcal/sugar/protein/caffeine value (PSL by size and milk, Blonde, Decaf, Iced, Macchiatos, Matcha, Frappuccinos) |
| S3 | starbucksfreiburg.de: online ordering page of STARBUCKS FREIBURG HAUPTBAHNHOF (curl, 29 Sep) | prices (PSL 6,20; Iced PSL 6,20; PSCM 6,40; Pecan 6,40; PS Matcha 7,20; Apple Crumble 7,20; Frapps 7,40; Caffè Latte 4,90; food 2,80–5,20), DE product descriptions ("Haube aus Milchschaum und einer feinen Pumpkin-Spice-Gewürzmischung") |
| S4 | Starbucks DE Allergen PDF (Getränke), Autumn 10.09.2026 | vegan flags: Iced PSL + plant milk = vegan; hot PSL + plant milk = "nein***" → "mit Soja-/Kokos-/Hafer-/Mandeldrink, veganer Schlagcreme und ohne Topping vegan"; PSCM with plant milk = nein |
| S5 | en.wikipedia.org/wiki/Pumpkin_spice_latte | 2003 test (Vancouver, Washington D.C.), 2004 national, pumpkin purée 2015, ~424 million sold by 2019, "PSL" trademark 2015 |
| S6 | about.starbucks.com (Aug 2026 US fall menu), it-boltwise.de 25 Aug 2026 | US lineup, used ONLY for the DE-vs-US table: US start 25 Aug 2026, Pumpkin Cream Cold Brew, Iced Pumpkin Cream Shaken Espresso, Pumpkin Spice Chai, Iced Pumpkin Cream Chai, Pecan Cortado, Pecan Crunch Latte, Chaider |
| S7 | menu.js (site) | PSL 6,20 € and 259 kcal (consistent with S2/S3) |

Head entities: **Pumpkin Spice Latte** (Thing; sameAs https://en.wikipedia.org/wiki/Pumpkin_spice_latte, https://www.wikidata.org/wiki/Q18345746). **Starbucks** (Organization; https://www.wikidata.org/wiki/Q37158). Unlinked: Pecan Maple Flavour Macchiato, Pumpkin Spice Matcha Latte, Iced Apple Crumble Cream Matcha.
> Wikidata IDs verified via wbsearchentities API on 29 Sep 2026: PSL = Q18345746, Starbucks = Q37158. Espresso/Matcha searches returned wrong top hits, so those use Wikipedia URLs only.

## Step 3: Metadata
- **Title tag:** Starbucks Pumpkin Spice Latte 2026: Preis, Kalorien & Koffein (61 chars)
- Alt title: Pumpkin Spice Latte bei Starbucks: Preis, Kalorien & Herbstkarte 2026
- **H1:** Starbucks Pumpkin Spice Latte 2026: Preis, Kalorien und alle Herbstgetränke
- **Meta description:** Starbucks Pumpkin Spice Latte 2026: 6,20 €, 259 kcal im Grande, 89 mg Koffein. Alle Herbstgetränke in Deutschland mit Preisen, Kalorien & veganen Tipps. (156 chars)
- **Slug:** /blog/starbucks-pumpkin-spice-latte

## Step 4: Competitors (top 4 distinct, fetched)
| # | URL | Date | Notes |
|---|---|---|---|
| C1 | ad-hoc-news.de/wirtschaft/produkte/starbucks-pumpkin-spice-latte-in-deutschland-saisonklassiker-mit/69940110 | 12.08.2026 | H3s: Rezeptur und Aromaprofil / Größen, Kalorien und Zucker / Saisonale Verfügbarkeit und Preisrahmen / Vergleich mit alternativen Herbstdrinks / Einordnung für den Alltag. **Wrong numbers:** Grande "~380 kcal", "~50 g Zucker" (official: 259 kcal and 31,4 g with Halbfettmilch; 297 kcal with Vollmilch). Venti "591 ml" (DE hot Venti; OK). Claims "2025 Germany: 26 Aug with early app access" (unverified). |
| C2 | it-boltwise.de/starbucks-bringt-pumpkin-spice-latte-und-neue-herbstdrinks-zurueck.html | 25.08.2026 | German-language article that lists the **US** menu (Pumpkin Spice Chai, Chaider, Pecan Crunch) without saying it is US-only. This is the misinformation our §5 corrects. |
| C3 | fastfood-preisecheck.de/starbucks-preise-deutschland/ | 12.02.2026 | PSL 6,20 € and "Eiskaffee Pumpkin Spice Latte" 6,20 €. H2 "Holiday Specials – Drinks". FAQ: "Gibt es saisonale Angebote?" |
| C4 | starbucks.de hot-drinks (official) | live | product listing only, no prices or kcal on the page |
Substitution note: starbucks.com / about.starbucks.com are US pages, used only as US reference (S6).

## Step 5: Extraction (condensed)
- **C1 Rezeptur und Aromaprofil:** Espresso (Product), Milch, Pumpkin-Spice-Sauce, Sahne, Zimt, Muskatnuss, Nelke, Iced Pumpkin Spice Latte, Pumpkin Spice Frappuccino, vegan, pflanzliche Milch. 11
- **C1 Größen, Kalorien und Zucker:** Tall 355 ml, Grande 473 ml, Venti 591 ml, kcal, Fett, Zucker, Magermilch. 7
- **C1 Saisonale Verfügbarkeit und Preisrahmen:** USA Ende August, Deutschland Mitte/Ende September, 12.09.2023, 26.08.2025, App-Nutzer, November, Dezember. 7
- **C1 Vergleich mit alternativen Herbstdrinks:** Pumpkin Cream Cold Brew, Pumpkin Spice Frappuccino, Chai Tea (Oat) Latte, Filterkaffee. 4
- **C2:** 25. August 2026, Iced Pumpkin Cream Shaken Espresso, Pumpkin Spice Chai, Iced Pumpkin Cream Matcha, Pumpkin Cream Cold Brew, Iced Pumpkin Cream Chai, Pecan Cortado, Pecan Crunch Latte, Iced Banana Bread Latte, Chaider, Pumpkin Cream Cheese Muffin, Cake Pop. 12
- **C3:** Pumpkin Spice Latte 6,20 €, Eiskaffee Pumpkin Spice Latte 6,20 €, saisonale Getränke, Winter-Specials. 4
Numbers seen: 6,20 €; 380 kcal (wrong); 50 g (wrong); 355/473/591 ml; 2003; 25.08.2026; 26.08.2025.

## Step 6: Entity ledger (see entities.json)
- **Tier 1:** Pumpkin Spice Latte, Starbucks Deutschland, Preis, Kalorien, Koffein, Grande, Herbstkarte/Herbstgetränke, Iced Pumpkin Spice Latte, Kürbis-Gewürzsauce.
- **Tier 2:** Tall, Venti, Halbfettmilch, Milchsorte (Hafer/Soja/Mandel/Kokos/Vollmilch/Magermilch), Zucker, Pumpkin Spice Caramel Macchiato, Pecan Maple Flavour Macchiato, Pumpkin Spice Matcha Latte, Pumpkin Spice Frappuccino, vegan, Blonde Espresso, Decaf, Starbucks Rewards, Zimt/Muskat/Nelke, Espresso.
- **Tier 3:** Pumpkin Spice Loaf Cake, Cake Pop, Pecan Maple Cake, Apple Crumble Cinnamon Roll, Iced Apple Crumble Cream Matcha, Pumpkin Spice Cream Cold Foam, Starbucks Blonde, Peter Dukes (unused), Nespresso/Dolce Gusto PSL (parked).
- **Relationships:**
  - PSL —costs→ 6,20 € (S3).
  - PSL Grande Halbfett —has→ 259 kcal / 31,4 g Zucker / 89,1 mg Koffein (S2).
  - Tall = Grande —same caffeine→ 2 shots.
  - Venti —3 shots→ 133,6 mg.
  - Iced PSL Grande —has→ 192 kcal.
  - Mandeldrink —lowest→ 205 kcal; Vollmilch —highest→ 297.
  - Decaf PSL —has→ 3,6 mg.
  - Blonde PSL Grande —has→ 239 kcal / 85,5 mg.
  - Iced PSL + Pflanzendrink —is→ vegan; hot PSL —vegan only→ ohne Topping (S4).
  - PSCM —costs→ 6,40, 234 kcal.
  - Pecan Maple Macchiato —uses→ Blonde Espresso, 215 kcal / 85,5 mg.
  - PS Matcha Latte —has→ 296 kcal / 80,8 mg.
  - PS Coffee Frapp —has→ 351 kcal / 33,4 mg; PS Cream Frapp —has→ 0 mg.
  - PSL —introduced→ 2003 USA.
  - Rewards 150 Sterne —redeem→ free drink; 3 Sterne/€ → 50 €.
- **Heading keyword set:**
  - (a) Focus: starbucks pumpkin spice latte, pumpkin spice latte starbucks, starbucks psl, starbucks deutschland pumpkin spice latte.
  - (b) Secondary: was kostet… / preis, kalorien, koffein, herbst getränke 2026, ab wann / bis wann, vegan, iced pumpkin spice latte, pumpkin spice frappuccino, pecan maple macchiato.
- **Dedupe/parked:** "PSL Pulver/Instant", "Nespresso/Dolce Gusto pumpkin spice" are parked (at-home products; DE 2026 availability unverified; better suited to the kapseln-angebot page). "Halloween/Herbst merch" is parked (covered by /blog/starbucks-becher-aktuell). The "Pumpkin Cream Iced Matcha Latte" (PDF name) and "Iced Pumpkin Spice Matcha Latte" (S3 name) are treated as the same drink. That mapping is inferred (both are iced matcha with Pumpkin Spice Cream Cold Foam) and flagged below.

## Step 7: Information gain
- C1 has wrong kcal/sugar (380 kcal, 50 g) and gives no per-milk data.
- C2 presents the US menu as if it applied in Germany.
- No competitor has **official DE nutrition by size and by milk**, **DE prices for the whole Herbstkarte**, or **the vegan rule from the DE allergen list**.
- **Original elements:** (1) the **Deutschland-vs-USA table** (§5), (2) the kcal-by-milk table, (3) the "clever bestellen" checklist with real numbers.

## Step 8: Heading map
| Level | Heading | Owns phrase | Question | Carries |
|---|---|---|---|---|
| H1 | Starbucks Pumpkin Spice Latte 2026: Preis, Kalorien und alle Herbstgetränke | starbucks pumpkin spice latte | — | PSL, Starbucks |
| H2 | 1. Was ist der Pumpkin Spice Latte bei Starbucks? | was ist pumpkin spice latte | definition | Espresso, Sauce, Milchschaum, Gewürze, 2003 |
| H2 | 2. Was kostet der Pumpkin Spice Latte 2026? | preis | price | 6,20; table |
| H2 | 3. Wie viele Kalorien und wie viel Koffein…? | kalorien / koffein | nutrition | S2 |
| H3 | Kalorien und Koffein nach Größe | tall grande venti | — | shots |
| H3 | Kalorien nach Milchsorte | hafer/mandel… | — | per-milk |
| H2 | 4. Welche Herbstgetränke gibt es 2026…? | herbst getränke 2026 | lineup | 8 drinks |
| H3 | Pumpkin Spice Caramel Macchiato und Pecan Maple Macchiato | pecan maple macchiato | — | |
| H3 | Pumpkin Spice Matcha und Apple Crumble Matcha | pumpkin spice matcha | — | |
| H3 | Pumpkin Spice Frappuccino | pumpkin spice frappuccino | — | |
| H3 | Herbstliches Gebäck | herbst gebäck | — | food prices |
| H2 | 5. Deutschland oder USA…? | (info-gain) | US vs DE | S6 |
| H2 | 6. Wann gibt es den Pumpkin Spice Latte? | ab wann / bis wann | availability | 10.09.2026 list |
| H2 | 7. Ist der Pumpkin Spice Latte vegan? | vegan | diet | S4 |
| H2 | 8. So bestellst du deinen PSL clever | bestellen tipps | action | checklist |
| H2 | Häufig gestellte Fragen | — | 12 Q | |

**Internal links used:**
- [Starbucks Preisliste] → /blog/starbucks-preise
- [Kalorien-Guide] → /blog/starbucks-kalorien-guide
- [Matcha Latte Guide] → /blog/starbucks-matcha-latte
- [Frappuccino-Übersicht] → /blog/starbucks-frappuccino-sorten
- [Starbucks vegan] → /blog/starbucks-vegane-optionen
- [Größen] → /blog/starbucks-groessen-tall-grande-venti
- [Becher aktuell] → /blog/starbucks-becher-aktuell

**Links to add after publishing:**
- Link to this page from /blog/starbucks-latte (the PSL row), /blog/starbucks-getraenke and /blog/starbucks-kalorien-guide.
- Add a link from the upcoming /blog/starbucks-weihnachten (the winter successor).

**Cannibalisation:** no page targets PSL. /blog/starbucks-latte mentions it as one row, which is fine.

## FAQ source map
| FAQ question | Source |
|---|---|
| Preis | PAA/autocomplete ("was kostet starbucks pumpkin spice latte") |
| kcal Grande | C1 topic |
| Koffein | fan-out |
| echter Kürbis | S5 + common PAA |
| bis wann | autocomplete "ab wann" |
| kalt | fan-out iced |
| laktosefrei | vegan cluster |
| Unterschied Macchiato | S1 lineup |
| Rewards | cross-sell / S-app |
| wenigste Kalorien | derived S2 |
| USA-only | info gain |
| weniger Zucker | S2 |

## Open flags (need user)
1. **Price conflict on our own site:** /blog/starbucks-preise says PSL is Tall 5,40 / Grande 5,90 / Venti 6,50 €, but S3, menu.js and C3 all say 6,20 €. Not changed (out of scope). Reconcile it in the planned price pass.
2. **Start date 2026 DE** is unknown. The draft only says "Ende August oder September" plus the date of the 10.09.2026 nutrition list. C1's claim of "26 Aug 2025 with app early access" is not used.
3. The **Iced Pumpkin Spice Matcha Latte = Pumpkin Cream Iced Matcha Latte** mapping is inferred. The draft avoids giving kcal for the iced PS matcha.
4. **Iced Apple Crumble Cream Matcha** has no nutrition row yet (newer than the 10.09 list).
5. In the FAQ about the macchiato, "Espresso zuletzt dazugegeben" is inferred from the S3 description wording ("mit Espresso veredelt"). It is a standard macchiato build, but not stated explicitly for DE.
6. Hero image needed: 1600×1000 WebP, Unsplash `license=free`, no Starbucks logo (e.g. a pumpkin-spice latte in an orange mug).
