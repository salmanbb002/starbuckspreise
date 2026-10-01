# Research notes: starbucks reserve

Run date: 2 Oct 2026. Target: starbuckspreise.com `/blog/starbucks-reserve`, voice: du. Queue item #8 (~200/mo). Supporting keywords (Autocomplete_Oct2026): starbucks reserve, reserve roastery, reserve bedeutung, reserve unterschied.

## Step 1: Intent + SERP

- **Dominant intent:** know (what is it / what does it mean / how is it different). **Secondary:** visit (is there one in Germany / nearest roastery).
- **SERP (WebSearch, de + en queries):** en.wikipedia Starbucks Reserve + Roastery (Seattle, Chicago) articles, starbucksreserve.com, nrn.com explainer, yourdreamcoffee.com, foodrepublic.com, yahoo "Roastery, Reserve Bar, Regular", danielfiene.com (Düsseldorf 2018), food-service.de (München 2016), kaffee-netz.de thread, wiwo.de.
- **SERP features (inferred):** knowledge panel (Starbucks Reserve Roastery places), image pack, PAA ("What is the difference…", "Is Starbucks Reserve more expensive?").
- **Fan-out:** bedeutung, unterschied, roastery, deutschland (implied), mailand.

## Step 2: Sources

| # | Source | Used for |
|---|---|---|
| S1 | en.wikipedia.org/wiki/Starbucks_Reserve (fetched 2 Oct 2026) | launch 2010; definition (rarest, single-origin); roasteries + dates: Seattle Dec 2014 (closed Sep 2025), Shanghai Dec 2017, Milan 7 Sep 2018, NYC 13 Dec 2018, Tokyo 28 Feb 2019, Chicago 15 Nov 2019; 5 operating, 43 Reserve Bars, ~7 Reserve Stores, ~1,500 stores with Reserve coffee; Princi |
| S2 | komonews / geekwire / capitolhillseattle (search snippets) | Seattle Roastery closed 25 Sep 2025, ~180 store closures, ~900 non-retail roles cut |
| S3 | nrn.com explainer, 10 Jan 2019 | three formats; Reserve Bar = premium coffee in classic Starbucks environment; 1,000-store vision (Schultz 2016) → "aspirational" (Johnson 2019) |
| S4 | yourdreamcoffee.com (upd. 23 Jun 2026) | small-lot, single-farm; 7 brewing methods (pour over, Chemex, cold brew, French press, siphon, espresso, Clover) |
| S5 | foodrepublic.com, 1 Sep 2023 | US prices: cold brew flight 13 $ (Chicago), PSL ~8 $ vs 5,50 $, Roastery Old Fashioned 18 $ (Seattle) / 23 $ (NYC); Princi menu (focaccia, pizza, desserts) |
| S6 | food-service.de, 29 Aug 2016 | München Sendlinger Straße = first DE Reserve + Clover; vacuum press; Cape Verde Fogo Island, Colombia Los Rosales; ~2,000 Reserve stores then |
| S7 | danielfiene.com, 10 Jun 2018 | Düsseldorf Kö/Steinstraße Reserve "Clover-Bar"; Nicaragua + Rwanda, roasted in Seattle; rotating every 2 months; only Munich besides |
| S8 | WebSearch snippet (wiwo.de 2018 context) | "Reserve-Filialen gibt es bereits in Düsseldorf, Frankfurt und Berlin" |
| S9 | Milan sources (mindtrip/yelp/opentable/eatbuytravel via search) | Piazza Cordusio 3; Palazzo Broggi (former stock exchange + post office); 2,300 m²; Scolari roaster with copper pipes; Princi wood-fired oven; Arriviamo cocktail bar; opened 7 Sep 2018; first Starbucks in Italy, largest in Europe; daily 7:30–22:00; OpenTable listing |

## Step 3: Metadata

- **Title:** Starbucks Reserve: Bedeutung, Roastery & Unterschied erklärt (59 chars)
- **H1:** Starbucks Reserve: Bedeutung, Roasteries und der Unterschied zum normalen Starbucks
- **Meta:** see meta.json (147 chars)
- **Slug:** /blog/starbucks-reserve
- Alt title: "Starbucks Reserve in Deutschland: Gibt es das noch?"

## Step 4: Competitors

| C | URL | Date | Notes |
|---|---|---|---|
| C1 | en.wikipedia.org/wiki/Starbucks_Reserve | live | History / Types / Roasteries / Reception. No FAQ. |
| C2 | nrn.com explainer | Jan 2019 | What is / strategy shift / roastery timeline. Stale counts. |
| C3 | yourdreamcoffee.com/what-is-starbucks-reserve | upd. Jun 2026 | differences, formats table, 7 brewing methods, drinks. Still lists Seattle as open. |
| C4 | foodrepublic.com/1380096 | Sep 2023 | What can you drink / eat / worth a trip? Prices. |
| — | kaffee-netz.de thread | — | 403 → substituted by S6/S7 |

## Step 5: Extraction (condensed)

- **C1:** Starbucks Reserve, 2010, rarest, single-origin, Roastery, Reserve Bar, Reserve Store, Seattle, Shanghai, Milan, New York, Tokyo, Chicago, closed September 2025, 43, ~7, ~1,500, Princi, cocktail bar. (18)
- **C2:** premium line, third-wave, 2014, Roastery, Reserve Store, Reserve Bar, Princi, 1,000 stores, 20–30 Roasteries, Howard Schultz, Kevin Johnson, aspirational, 15,000/30,000/25,000 sq ft. (13)
- **C3:** rare beans, small-lot, single-origin, single farm, stronger, Nitro Cascara Cloud 6 $, pour over, Chemex, cold brew, French press, siphon, espresso, Clover, affogato, Emerald City Mule, Old Fashioned. (17)
- **C4:** Seattle 2014, espresso martini, coffee cocktails, cold brew flight 13 $, Princi breakfast/lunch/desserts, siphon, Chemex, pour-over, PSL 8 $ vs 5,50 $, Old Fashioned 18/23 $. (12)

## Step 6: Entity ledger

See entities.json (22 rows: 6 tier-1, 11 tier-2, 5 tier-3).

**Relationships**
- Starbucks Reserve —launched→ 2010; —sells→ rare single-origin small-lot coffee
- Reserve —has formats→ Roastery (5) / Reserve Bar (43) / Reserve Store (~7); ~1,500 stores carry Reserve coffee
- Seattle Roastery —opened→ Dec 2014; —closed→ 25 Sep 2025 (restructuring, ~180 stores)
- Mailand Roastery —is→ only roastery in Europe; —located in→ Palazzo Broggi, Piazza Cordusio 3; —opened→ 7 Sep 2018
- Roastery —includes→ Princi bakery, cocktail bar (Arriviamo in Milan), on-site roasting (Scolari)
- Clover —brews by→ vacuum press, per cup
- München Sendlinger Straße —was→ first DE Reserve + Clover (2016)
- Düsseldorf Kö/Steinstraße —opened→ Reserve Clover-Bar June 2018; beans —roasted in→ Seattle; rotate every 2 months
- Reserve —costs more than→ regular (US: PSL ~8 $ vs 5,50 $)

**Dedupe/parked:** Arrival Bar (S1 fetch summary) vs Arriviamo (S9) → used "Arriviamo" for Milan only. Schultz/Johnson strategy parked (off-intent). "Reserve coffee is stronger" (C3) parked: unsupported. Nitro Cascara Cloud / Emerald City Mule parked (US/Seattle-only).

## Step 7: Information gain

- C3 still lists Seattle as open; C2 counts are from 2019. Ours has the **Seattle closure (25 Sep 2025)** and current counts.
- No competitor covers **Germany** (München 2016, Düsseldorf 2018, status today) or the **nearest roastery for Germans** (Mailand) with practical facts.
- No competitor explains "Reserve" ≠ reservation (German searchers' "bedeutung").
- **Original element:** "Lohnt sich Reserve?" decision checklist + roastery status table.

## Step 8: Heading map

| Lvl | Heading | Owns phrase | Question |
|---|---|---|---|
| H1 | Starbucks Reserve: Bedeutung, Roasteries und der Unterschied zum normalen Starbucks | starbucks reserve | — |
| H2 | 1. Was bedeutet Starbucks Reserve? | reserve bedeutung | meaning |
| H3 | Woran erkennt man Starbucks Reserve? | reserve logo | — |
| H2 | 2. Welche Arten von Starbucks Reserve gibt es? | reserve bar / store | formats |
| H3 | Starbucks Reserve Roastery: alle Standorte | reserve roastery | locations |
| H2 | 3. Was ist der Unterschied …? | reserve unterschied | comparison |
| H3 | Die Brühmethoden bei Starbucks Reserve | clover / siphon | — |
| H3 | Was kostet Kaffee bei Starbucks Reserve? | reserve preis | — |
| H2 | 4. Gibt es Starbucks Reserve in Deutschland? | reserve deutschland | — |
| H3 | Wie findest du eine Reserve-Filiale in Deutschland? | reserve filiale | — |
| H2 | 5. Starbucks Reserve Roastery Mailand | roastery mailand | visit |
| H2 | 6. Lohnt sich Starbucks Reserve? | lohnt sich | info gain |
| H2 | Häufig gestellte Fragen | — | 10 Q |

**Internal links (out):** kaffee, preise, app, deutschland-filialen, stadtmitte.
**Inbound candidates:** starbucks-kaffee (röstungen), starbucks-logo-name-bedeutung (logo/brand), starbucks-deutschland-filialen, starbucks-stadtmitte (Düsseldorf Steinstraße), blog/index.
**Cannibalisation:** none. logo-name-bedeutung covers the siren logo, not Reserve.

## FAQ source map

Seit wann (C1), Seattle geschlossen (S2), nächste Roastery (S1/S9), teurer (C4), Clover (S6/C3), normale Getränke (C2), Princi (C1/C4), Bohnen kaufen (C1/S7), reservieren (S9 OpenTable + "bedeutung" angle), vor Ort geröstet (S7/S9).
