# Research notes — "starbucks tasse münchen"

## Step 1 — Intent + SERP

SERP is dominated by **marketplace listings**, not content pages: kleinanzeigen.de,
ebay.de, amazon.de, picclick.de all rank for the bare keyword. Only 3 substantive
content/product pages exist:

1. thecoffeemugshop.de/products/munchen-city-kaffee-tasse-you-are-here-series-kaufen — reseller product page, specs + price
2. starbucks-mugs.com/mug/you-are-here-munchen/ — English-language collector catalog entry, 2016, thin
3. starbuckspreise.de/starbucks-tasse/ — general "Starbucks Tasse Deutschland" guide (competitor .de domain, NOT this site), mentions München only as one of several store locations

A 4th candidate (coffeegeek.co article on collector-mug resale value) 404'd — dropped per
fetch-failure rule, not substituted (SERP has no further distinct-domain content page beyond
marketplace listings).

**Dominant intent:** *buy* (where to get one, what it costs) with secondary *know-simple*
(what it is / specs). NOT navigational/local — this is Starbucks-branded **merchandise**, a
collector mug themed on Munich, not a store-locator query. Deliberately not templated as a
`/standorte/` location page.

**SERP features:** No featured snippet observed for this long-tail. No PAA block surfaced in
search tool results (thin SERP, low volume). No local pack (not a "near me" query).

**Query fan-out (from related searches / follow-up queries):**
- starbucks tasse münchen kaufen wo
- starbucks tasse münchen echt fälschung erkennen
- starbucks sammler-tassen wert
- starbucks you are here collection
- starbucks city mug münchen gebraucht

## Step 2 — Head entities (non-competitor sources)

| Entity | Type | sameAs | Notes |
|---|---|---|---|
| Starbucks Corporation | Organization | https://www.wikidata.org/wiki/Q37158 | US coffeehouse chain, operates in Germany since 2002 |
| München (Munich) | Place | https://www.wikidata.org/wiki/Q1726 | Bavarian capital; mug's theme city |
| "You Are Here" Collection | Product series | — (unlinked entity, no Wikidata match) | Starbucks global city-mug merchandise line, launched ~2011; German city mugs (incl. München) first issued June 2016 per reseller data |

## Step 3 — Title/metadata

- **Title (primary):** Starbucks Tasse München: Preis, Kaufen & Echtheit prüfen (2026)
- **Title (alt):** Starbucks Tasse München (You Are Here): Wo kaufen & was kostet sie?
- **H1:** Starbucks Tasse München: Die You-Are-Here-Sammlertasse im Überblick
- **Meta description:** Die Starbucks Tasse München aus der You Are Here Collection: Maße, Preis, wo Sie sie neu oder gebraucht kaufen – und wie Sie Fälschungen erkennen.
- **Slug:** starbucks-tasse-muenchen
- **OG title/description:** mirror title + meta

## Step 4/5 — Competitor extraction

### thecoffeemugshop.de (product page)
| term/entity | type | canonical | kind |
|---|---|---|---|
| You Are Here Series | Product | You Are Here Collection | entity |
| 414ml / 14 fl.oz. | Metric | Fassungsvermögen 414ml | term |
| dickwandiger Keramikbecher | Concept | Keramik | term |
| 8,5cm Höhe / 9,5cm Durchmesser | Metric | Maße | term |
| 0,5kg | Metric | Gewicht | term |
| €25,99 (reduziert von €37,99) | Money | Preis | term |
| Juni 2016 | Date | Erstausgabe | term |
| Geschenkbox | Concept | Geschenkverpackung | term |
| Versand/Rückgabe (2-4 Tage, 14 Tage Rückgabe) | Process | Versandbedingungen | term |
Count: 9

### starbucks-mugs.com (catalog entry)
| term/entity | type | canonical | kind |
|---|---|---|---|
| You Are Here – Munchen | Product | You Are Here Collection | entity |
| Posted August 25, 2016 | Date | Katalogdatum | term |
| Germany / Munich tag | Place | München | entity |
| eBay / Amazon Wiederverkäufer | Org | Marktplätze | entity |
| Preisspanne $20–$109 | Money | Zweitmarktpreis | term |
Count: 5

### starbuckspreise.de/starbucks-tasse/ (general German guide, competitor domain)
| term/entity | type | canonical | kind |
|---|---|---|---|
| Starbucks Deutschland seit 2002 | Date | Marktstart Deutschland | entity |
| 170+ Filialen | Metric | Filialanzahl | term |
| Reusable Tumbler / Keramiktasse / Saisonedition / Kaltgetränkebecher | Product | Tassentypen | term |
| €10–€30 Preisspanne | Money | Preisspanne | term |
| Starbucks Store München, Rosental 7, nahe Marienplatz | Place | Starbucks Filiale München | entity |
| 0,30€ Rabatt eigener Becher | Money | Bring-Your-Own-Mug-Rabatt | term |
| Fälschungen vermeiden | Concept | Echtheit | term |
| Zweitmarkt / Sammler-Tipps | Concept | Sammlermarkt | term |
Count: 8

## Step 6 — Entity ledger + tiers

See `entities.json` for the structured version.

**Tier 1 (core, ≥3 sources or in title/keyword — attribute stated):**
- Starbucks (org, all sources)
- München (place, all sources + keyword)
- You Are Here Collection (product series, keyword-implied + 2/3 sources)
- Fassungsvermögen 414ml (2/3 sources)
- Erstausgabe Juni 2016 (2/3 sources)
- Preis / Kaufort (all sources, central to *buy* intent)

**Tier 2 (supporting, 2 sources or clear sub-topic):**
- Keramik/Material + Maße/Gewicht (thecoffeemugshop)
- Starbucks Store München, Rosental 7 (starbuckspreise.de — real local detail, internal-link value)
- Echtheit/Fälschung erkennen (starbuckspreise.de + fan-out query)
- Sammlermarkt/Zweitmarktwert (starbucks-mugs.com + starbuckspreise.de)
- Bring-Your-Own-Mug 0,30€-Rabatt (starbuckspreise.de + this site's own pillar page)

**Tier 3 (optional, single-source):**
- Geschenkbox/Versandbedingungen (thecoffeemugshop only — used briefly, mostly parked, not core to a buying guide)
- Weitere Tassentypen Deutschland (starbuckspreise.de only — out of scope, this article is München-specific; parked)

**Relationships:**
- You Are Here Collection —beinhaltet→ Starbucks Tasse München
- Starbucks Tasse München —Fassungsvermögen→ 414ml / 14 fl.oz.
- Starbucks Tasse München —Erstausgabe→ Juni 2016
- Starbucks Tasse München —Material→ dickwandiger Keramikbecher
- Starbucks Tasse München —Maße→ 8,5cm Höhe, 9,5cm Durchmesser, 0,5kg
- Starbucks Store München —liegt an→ Rosental 7, nahe Marienplatz
- Originale Starbucks Tasse —erkennbar an→ Sirenen-Logo + Bodenprägung
- Sammlerwert —steigt mit→ Seltenheit/limitierte Auflage

**Dedupe log:** "Been There Series" (mentioned in earlier SERP snippet) is a *related but
distinct* Starbucks line, not identical to "You Are Here" — kept separate, not merged, to
avoid a factual error. General Starbucks-Deutschland history (2002 market entry, 170+
Filialen) parked as out-of-scope for a single-mug buying guide — belongs on the site's
broader `starbucks-tasse.html` pillar, which already covers it.

## Step 7 — Information-gain pass

All 3 competitors omit: a **side-by-side view of where to actually buy the mug now** (new
via reseller vs. secondhand via marketplace, with realistic price bands for each) — each
source only covers one channel. None address whether this souvenir/collector mug is a
normal in-store cup eligible for the 0,30€ reusable-cup discount — a natural reader question
this site's own audience (which already reads the general Starbucks-Tasse pillar) would ask.
None give concrete counterfeit-detection guidance specific to *this* mug rather than generic
advice.

**Committed info-gain element:** a "Neu vs. gebraucht kaufen" comparison table (channel,
typical price band, condition, pros/cons) — no competitor presents this.

## Step 8 — Heading + keyword + question map

| Level | Heading | Focus/LSI phrase | Question answered | Tier-1/2 carried |
|---|---|---|---|---|
| H1 | Starbucks Tasse München: Die You-Are-Here-Sammlertasse im Überblick | starbucks tasse münchen | What is this page about | Starbucks, München, You Are Here |
| — | Direct-answer block | — | What is the Starbucks Tasse München | You Are Here, München, 414ml |
| H2 | Was ist die Starbucks Tasse München? | starbucks tasse münchen you are here | What is it / which series | You Are Here Collection, Starbucks |
| H2 | Maße, Material und Fassungsvermögen im Detail | starbucks tasse münchen maße | How big is it / what's it made of | 414ml, Keramik, Maße |
| H2 | Wie viel kostet die Starbucks Tasse München? | starbucks tasse münchen preis | What does it cost (new vs. used) | Preis, Zweitmarkt |
| H2 | Wo können Sie die Starbucks Tasse München kaufen? | starbucks tasse münchen kaufen | Where to buy | Marktplätze, Reseller, Store München |
| H3 | Online-Marktplätze (eBay, Amazon, Kleinanzeigen) | — | Which marketplaces | Zweitmarkt |
| H3 | Spezialisierte Reseller | — | Where to buy new | Reseller |
| H3 | Im Starbucks Store München | starbucks store münchen | Can I get it in-store | Starbucks Store München, Rosental 7 |
| H2 | Original oder Fälschung? So erkennen Sie eine echte Tasse | starbucks tasse münchen echt | How to spot a fake | Echtheit/Fälschung |
| H2 | Zählt die Sammlertasse für den 30-Cent-Rabatt? | starbucks tasse münchen rabatt | Does it work for the reusable-cup discount | Bring-Your-Own-Mug-Rabatt |
| H2 | Ist die Starbucks Tasse München ein gutes Sammlerstück? | starbucks sammlertasse wert | Is it worth collecting | Sammlermarkt, Erstausgabe |
| H2 | Häufig gestellte Fragen | — | FAQ | — |

## Step 8e — Internal-link plan

- Anchor "Starbucks Tasse" (general) → `/starbucks-tasse.html` (this site's existing pillar
  page — no cannibalisation found; that page never mentions München, this new page is a
  city-specific spin-off and should link up to the pillar, and the pillar should eventually
  link down to this page).
- Anchor "Starbucks Filialen in München" → this site's München store-locator content if it
  exists under `/standorte/` (not yet found in this project's file list — flag for the user
  to add once a München location page exists; do not fabricate a URL).
- Anchor "0,30€ Rabatt für den eigenen Becher" → the Bring Your Own Mug section of
  `/starbucks-tasse.html` (section id `#rabatt`).

## Step 10 — FAQ source map

1. Was ist die "You Are Here Collection"? — from Step 2/5 entity research
2. Wie groß ist die Starbucks Tasse München? — thecoffeemugshop.de specs
3. Wann kam die Starbucks Tasse München raus? — thecoffeemugshop.de / starbucks-mugs.com
4. Was kostet eine originale Starbucks Tasse München? — thecoffeemugshop.de + starbucks-mugs.com price range
5. Wo bekomme ich die Tasse gebraucht? — fan-out "gebraucht"
6. Ist die Tasse noch neu erhältlich? — thecoffeemugshop.de (reseller stock)
7. Woran erkenne ich eine gefälschte Starbucks Tasse? — fan-out + starbuckspreise.de
8. Kann ich mit der Sammlertasse den Rabatt fürs eigene Getränk bekommen? — this site's pillar + starbuckspreise.de
9. Ist die Starbucks Tasse München spülmaschinenfest? — genuine reader follow-up (ceramic mug care), not directly sourced — flagged in coverage.md as unsourced, phrased generically without inventing a specific certification claim
10. Lohnt sich die Tasse als Wertanlage? — fan-out "wert" + starbucks-mugs.com resale range
11. Welche Motive zeigt die Starbucks Tasse München? — Amazon listing title (Neues Rathaus, Weißwurst, Maß Bier / Oktoberfest theme)
