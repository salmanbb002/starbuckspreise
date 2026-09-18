# Research notes — starbucks-tasse-hamburg

## Step 1 — Intent + SERP

Query: "starbucks tasse hamburg" (Vol 260, KD 14, cluster: Tassen & Merch / City sub-angle).

Top results are a mix of marketplace listings (eBay.de, kleinanzeigen.de) and small
retailer/collector pages — no strong editorial competitor, same pattern as the sibling
Berlin page.

- **Dominant intent:** buy / know-simple (which motif does the mug have, where to get it).
- **Secondary intent:** know (is there a current in-store edition, or only secondhand).
- **SERP features:** no featured snippet, no PAA box observed, no knowledge panel, shopping
  carousel dominates (eBay/kleinanzeigen/thecoffeemugshop.de/queenshop.ch/Amazon).
- **Query fan-out (autocomplete/related, inferred from search results + adjacent queries):**
  "starbucks tasse hamburg kaufen", "starbucks hamburg tasse preis", "starbucks you are here
  hamburg", "starbucks städtetasse hamburg", "starbucks tasse hamburg ebay", "gibt es noch die
  starbucks hamburg tasse".

## Step 2 — Head-entity research

- **Starbucks Corporation** — global coffeehouse chain, HQ Seattle. `sameAs`:
  https://de.wikipedia.org/wiki/Starbucks
- **Hamburg** — German city, Hansestadt. `sameAs`: https://de.wikipedia.org/wiki/Hamburg
- **Hamburger Rathaus** — Hamburg city hall, the mug's front motif. `sameAs`:
  https://de.wikipedia.org/wiki/Hamburger_Rathaus
- **HafenCity** — Hamburg harbour district, the mug's back-motif skyline. `sameAs`:
  https://de.wikipedia.org/wiki/HafenCity
- **You Are Here Series** — Starbucks' first city-mug collectible line, launched 2008,
  discontinued/replaced 2018. No stable Wikipedia/Wikidata match → unlinked entity (term).
- **Been There Series** — current (since 2018) city/region mug line. Unlinked entity (term).

## Step 3 — Title + metadata

- **Title:** "Starbucks Tasse Hamburg: Motiv, Preis und aktuelle Verfügbarkeit 2026" (60
  chars)
- **Alternate:** "Starbucks Tasse Hamburg 2026: Rathaus-Motiv, Preise, Kaufquellen"
- **H1:** same as title, phrased naturally.
- **Meta description:** "Die Starbucks Tasse Hamburg zeigt Rathaus und HafenCity-Skyline.
  Was die You-Are-Here-Ausgabe kostet, ob es 2026 eine aktuelle Filialtasse gibt und wo Sie
  kaufen." (~152 chars)
- **URL:** `starbucks-tasse-hamburg` (site convention: `/blog/starbucks-tasse-hamburg.html`;
  the content-calendar's `/standorte/...` slug does not match this cluster's real URL
  pattern — flagging for the user, see report).
- **OG title/description:** mirror title + meta description.

## Step 4 — Competitor fetch (top 4 distinct domains)

1. **starbucks-mugs.com** — `/mug/you-are-here-hamburg/` — collector blog post (25 Aug
   2016). H1 "You Are Here – Hamburg"; only other heading is "Leave a Reply" (comment
   form). Body: affiliate marketplace roundup, eBay price range $15.00–$95.38, most listings
   $19.99–$29.99, ~25 active listings referenced. Tags: City, Europe, Germany, Hamburg.
2. **thecoffeemugshop.de** — `/products/hamburg-city-kaffee-tasse-kaufen` — active retailer
   product page. Specs: 414ml/14 fl oz, 8.5cm height, 9.5cm diameter, 0.5kg, thick-walled
   ceramic, new stock with SKU sticker + gift box, "You Are Here Series", first released
   June 2016. Price €29.99 (was €32.99). Shipping/returns FAQ block (not product FAQ).
3. **queenshop.ch** — `/produkt/porzellan-starbucks-staedte-mug-hamburg/` — Swiss retailer,
   "vintage" framing, grey-blue/white Hamburg image, 16 fl oz (differs from
   thecoffeemugshop.de's 14 fl oz — flagged, see coverage.md), 35.00 CHF, made in England,
   dishwasher/microwave safe.
4. **one-million-places.com** — `/blog/starbucks-tassensammlung-weltweit` (15 May 2019,
   updated context to Apr 2018 "Been There" launch) — editorial travel-blog roundup of the
   *Global Icon* series (2008-era predecessor line), **does not mention Hamburg** at all.
   Used for series-history/pricing context only (current mugs €12-17 in filialen, rare
   vintage Global Icon €50+, one extreme outlier €500+; ~420 Global Icon mugs exist
   worldwide, Germany has 38 designs).

**Fetch failures (substituted per pipeline rule):**
- `amazon.de/dp/B01MDKTRDG` — JS-rendered, only meta/head returned, no price/spec body →
  substituted with queenshop.ch.
- `ebay.de/b/Starbucks-Tasse-in-Hamburg/...` — HTTP 403 (bot-blocked) → substituted with
  one-million-places.com.
- Also checked `starbuckspreise.de/starbucks-tasse/` (direct .de niche competitor) and
  `starbucks-city-mugs.com/germany-3/hamburg/` (collector directory) — neither had
  extractable Hamburg-specific product detail (the .de competitor's article never names a
  Hamburg mug; the collector directory page is a nav shell that didn't render product
  content through fetch) — not counted as one of the 4, used only to corroborate the motif
  (Rathaus front / HafenCity skyline / dark blue) found via search synthesis.

## Step 5 — Entity/term extraction by heading

**starbucks-mugs.com — "You Are Here – Hamburg" (1 heading, comment form excluded):**
Starbucks, You Are Here, Hamburg, Germany, Europe, eBay, affiliate link, $15.00, $95.38,
$19.99, $29.99, 25 listings, August 2016, collector, secondhand. — 14 items.

**thecoffeemugshop.de — "Hamburg City Kaffee Tasse" (product page, no internal H2s, treated
as one block):**
414ml, 14 fl oz, 8.5cm, 9.5cm, 0.5kg, dickwandige Keramik, SKU-Aufkleber, Geschenkbox, You
Are Here Series, Juni 2016, €29.99, €32.99, DHL, 2-4 Werktage, 14-tägiges Rückgaberecht,
Käuferschutz. — 15 items.

**queenshop.ch — product block:**
Porzellan, Starbucks Städte Mug, Hamburg, grau-bläulich, weiss, 16 fl oz, 35.00 CHF, Made in
England, spülmaschinenfest, mikrowellengeeignet, Neuware. — 11 items.

**one-million-places.com — heading list (Hamburg absent, series-level terms only):**
Global Icon Serie, Been There Serie, 2008, April 2018, 65 Städtetassen, 420 Global-Icon-
Modelle weltweit, Deutschland 38 Designs, USA 49, China 59, Mexiko 26, €12-17, €50+, Tokio-
Basistasse €500+. — 15 items.

## Step 6 — Entity ledger + tiers

See `entities.json`. Relationships:
- `You Are Here Series —discontinued→ 2018 (replaced by Been There Series)`
- `Starbucks Tasse Hamburg (YAH) —zeigt→ Hamburger Rathaus (Vorderseite)`
- `Starbucks Tasse Hamburg (YAH) —zeigt→ HafenCity-Skyline (Rückseite)`
- `Starbucks Tasse Hamburg —Fassungsvermögen→ 414-415 ml / 14 fl oz (thecoffeemugshop.de,
  starbucks-mugs.com specs) vs 16 fl oz (queenshop.ch listing — discrepancy noted)`
- `thecoffeemugshop.de —verkauft→ Hamburg-Tasse für €29.99 (reduziert von €32.99)`
- `Global Icon Serie —Vorgänger von→ You Are Here Serie —Vorgänger von→ Been There Serie`

**Dedupe log:** "eBay" and "Kleinanzeigen" merged into one "Zweitmarkt" term (same role as
Berlin piece); "Amazon.de" parked — fetch returned no usable Hamburg-specific data, not
asserted. "Global Icon Series" kept as tier-2 (series-history context) even though it
predates and isn't the Hamburg mug's own series, because it's needed to explain the
succession chain in the info-gain section.

## Step 7 — Information-gain pass

All four competitors either (a) only document the *2016 You Are Here* Hamburg mug via
resale/collector framing, or (b) don't mention Hamburg specifically at all. **None state
whether a current *Been There* Hamburg city mug exists in filialen in 2026** — this is the
genuine gap. A live search for "Been There Hamburg 2026" turned up no confirmed listing.
**Information-gain element:** a dated "Stand September 2026" status callout + a data table,
stating plainly that the confirmed Hamburg city mug is the discontinued 2016 You Are Here
edition (now secondhand/reseller-only), and that no current in-store Been-There Hamburg
edition could be confirmed — rather than guessing either way.

## Step 8 — Heading + keyword + question map

| # | Level | Heading | Focus/LSI phrase | Question answered | Tier-1/2 carried |
|---|---|---|---|---|---|
| 1 | H1 | Starbucks Tasse Hamburg: Motiv, Preis und aktuelle Verfügbarkeit 2026 | starbucks tasse hamburg | — | Starbucks, Hamburg |
| — | answer block | (direct answer, 40-55 words) | — | what is it / how much / is it current | Rathaler, HafenCity, You Are Here |
| 2 | H2 | Welches Motiv zeigt die Starbucks Tasse Hamburg? | Motiv/Rathaus | what does it look like | Hamburger Rathaus, HafenCity |
| 3 | H2 | Aus welcher Serie stammt die Tasse — und gibt es 2026 noch eine aktuelle Ausgabe? | You Are Here / Been There | is it still sold new | You Are Here Series, Been There Series |
| 4 | H2 | Was kostet die Starbucks Tasse Hamburg? | Preis | how much | thecoffeemugshop.de, Zweitmarkt |
| 5 | H2 | Wo kann man die Starbucks Tasse Hamburg kaufen? | kaufen | where to buy | thecoffeemugshop.de, queenshop.ch, Zweitmarkt |
| 6 | H2 | Ist die Hamburg-Tasse auch außerhalb Hamburgs erhältlich? | außerhalb Hamburgs | regional exclusivity | Been There Series |
| 7 | H2 | Woran erkennt man eine echte Starbucks Tasse Hamburg? | echte / Fälschung | authenticity | SKU-Aufkleber, Keramik |
| 8 | H2 + table | Hamburg-Tasse: Daten & Maße im Überblick | Maße/Fassungsvermögen | specs table | all tier-1/2 specs |
| 9 | H2 | Frequently Asked Questions | — | leftover fan-out | all |

## Internal-link plan

- Anchor "Starbucks Tassen Serien und Sammlermodellen" → `/blog/starbucks-tassen` (existing
  pillar, same as Berlin piece).
- Anchor "Starbucks Tasse Berlin" → `/blog/starbucks-tasse-berlin` (sibling city page,
  cross-link between city mugs).
- Anchor "Kaufratgeber zur Starbucks Tasse" → `/blog/starbucks-tasse` (existing pillar).
- Anchor "Starbucks Filialen in der Nähe" → `/starbucks-in-meiner-naehe` (existing root
  page).
- No cannibalisation found — no existing page targets "starbucks tasse hamburg" or the
  Hamburg-specific mug.

## FAQ source map

Questions sourced from: fan-out ("gibt es noch die tasse", "was kostet", "ebay-Preis"),
genuine follow-ups implied by the info-gain finding (is it discontinued, is there a current
edition), and the same authenticity/care/regional-exclusivity questions the Berlin sibling
FAQ answered (reused because the underlying product line and site policy are identical,
not because they were copied without checking they apply to Hamburg's own facts).
