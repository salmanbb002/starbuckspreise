# Research notes — "starbucks tasse berlin"

## Step 1 — Intent + SERP
- Intent: mixed *buy* (transactional — where/how much) + *know-simple* (which motif/series).
- Query is a spoke of the site's own pillar `blog/starbucks-tassen.html`, which already has a
  Berlin bullet in its "Beliebte deutsche Städtemotive" section and an FAQ entry
  ("Kann man Berliner Tassen auch in München kaufen?"). **Cannibalisation check (Step 8e):**
  the pillar treats Berlin as one bullet among four cities; this page goes deep on Berlin only
  (all historical mug generations, exact current resale price, specific buy-now links) — a
  distinct, narrower intent, not a duplicate. Internal-link both directions instead of merging.
- SERP (live search, Sept 2026): dominated by mug-catalogue/reseller sites, not classic blogs —
  starbucks-mugs.com (mug database/catalogue), thecoffeemugshop.de (German reseller, exact
  product page), kleinanzeigen.de and ebay.de (marketplace listings), lekomka.com (relief mug
  reseller). No strong "blog guide" competitor exists yet — an information gap this page fills.
- No classic featured snippet / PAA box observed for this exact long-tail; treat as a
  know+buy hybrid, direct-answer block leads with price + where-to-buy.

## Step 2 — Head entities
- **Starbucks Corporation** — sameAs https://de.wikipedia.org/wiki/Starbucks
- **Berlin** — sameAs https://de.wikipedia.org/wiki/Berlin
- **Been There Series / You Are Here Series** — Starbucks city-mug product lines, no standalone
  Wikipedia article → recorded as unlinked entities (consistent with the pillar page's own
  treatment).

## Step 4 — Competitors fetched
1. starbucks-mugs.com (tag: Berlin) — catalogue of every historical Berlin mug: You Are Here
   Berlin + Christmas + Ornament variants (2016), Icon Berlin 1/2 + Mini (2016 listing, mug
   itself ~2012-era), Relief Berlin (production date 2012). All flagged "collector item."
   Secondary-market range cited: ~$13.99–$117.80.
2. thecoffeemugshop.de — product page "Berlin City Kaffee Tasse": You Are Here series, 414 ml,
   thick-wall ceramic, dishwasher/microwave-safe, gift box included, released May 2016, still
   in their current catalogue, price **€19.99 (reduced from €34.99)**. States stock is sourced
   from Starbucks directly, operates independently of Starbucks Corp.
3. kleinanzeigen.de (search: "starbucks tasse berlin") — active private-seller marketplace
   listings, prices vary by seller/condition (not a fixed catalogue price — do not quote a
   single number as official).
4. ebay.de — individual listing(s) for Starbucks Berlin mugs, marketplace pricing, same caveat.
   (lekomka.com also surfaced — Relief/3D Berlin mug reseller; used as a secondary source for
   the Relief-series existence, not quoted for price.)

Fetch note: all 4 targets were reachable directly (no 403/JS-wall substitutions needed).

## Step 5/6 — Entity ledger (condensed)

| canonical | type | kind | competitor_count | tier |
|---|---|---|---|---|
| Starbucks Corporation | Organization | entity | 4 | 1 |
| Berlin | Place | entity | 4 | 1 |
| You Are Here Series | Product line | term | 3 | 1 |
| Been There Series | Product line | term | 1 (site pillar) | 1 |
| Icon Series | Product line | term | 2 | 2 |
| Relief Series | Product line | term | 2 | 2 |
| Ornament / Mini mug | Product | term | 2 | 2 |
| Brandenburger Tor | Landmark | entity | 0 (pillar-sourced) | 2 |
| Berliner Fernsehturm | Landmark | entity | 0 (pillar-sourced) | 3 |
| Kleinanzeigen / eBay | Marketplace | entity | 2 | 2 |
| Keramik (ceramic) | Material | term | 3 | 2 |
| SKU-Aufkleber / Bodenstempel | Concept | term | 1 | 2 |

Relationships: `You Are Here Berlin —released→ May 2016`; `You Are Here Berlin —capacity→ 414 ml`;
`thecoffeemugshop.de —currently sells→ You Are Here Berlin (€19.99)`; `Berlin mug —regionally
exclusive to→ Berlin Starbucks stores (per site pillar)`; `Icon/Relief Berlin —production
era→ 2012`; `resale value —driven by→ scarcity + condition + original box/SKU sticker`.

Dedupe: dropped "Berlin Wall fragment" as a standalone entity — folded into "Brandenburger Tor
/ Mauer-Motive" design description per the pillar's own phrasing, not a separate sourced fact.

## Step 7 — Information gain
All 4 competitors are catalogue/marketplace pages with no single up-to-date table spanning
every Berlin mug generation + era + real current price anchor. **Original element added:** a
dated "Berlin-Tasse Generationen im Überblick" table (Icon 2012 → Relief 2012 → You Are Here
2016 → current Been There) with production era, size, and a real, sourced current-price anchor
(thecoffeemugshop.de €19.99) instead of vague "varies by seller" language.

## Step 8 — Heading map
1. H1: Starbucks Tasse Berlin: Motive, Preise und wo Sie sie 2026 kaufen (focus keyword)
2. Direct-answer block (45 words)
3. H2 Welches Berlin-Motiv zeigt die Starbucks Tasse? — design/landmarks (tier 1/2)
4. H2 Welche Serien der Berlin-Tasse gibt es? — Icon/Relief/YAH/Been There (tier 1/2)
5. H2 Was kostet die Starbucks Tasse Berlin? — price ranges, official vs. resale (tier 1)
6. H2 Wo kann man die Starbucks Tasse Berlin kaufen? — Berlin filialen, thecoffeemugshop.de, eBay/Kleinanzeigen (tier 1)
7. H2 Ist die Berlin-Tasse auch außerhalb Berlins erhältlich? — regional exclusivity (tier 2, mirrors pillar FAQ but answered here first-hand)
8. H2 Woran erkennt man eine echte Starbucks Tasse Berlin? — authenticity (tier 2)
9. H2 Berlin-Tasse Generationen im Überblick (info-gain table)
10. H2 FAQ (10 questions)

Internal links: → `/blog/starbucks-tassen` (pillar, anchor "Starbucks Tassen Serien &
Sammlermodellen"), → `/starbucks-in-meiner-naehe` (find a Berlin store), → `/blog/starbucks-tasse`
(classic logo mug guide), → `/` (Starbucks Preise).

## Fact-check trace
- €19.99 / was €34.99, 414 ml, May 2016, gift box, dishwasher/microwave-safe →
  thecoffeemugshop.de product page (fetched live).
- Historical Berlin generations (Icon 2012, Relief 2012, You Are Here 2016 + Christmas/Ornament
  variants) → starbucks-mugs.com Berlin tag page (fetched live).
- Resale range ~$14–$118 → starbucks-mugs.com (converted/rounded to € ranges in copy, flagged
  as approximate/fluctuating, not quoted as a fixed price).
- Regional-exclusivity claim + current Been There Berlin motif details (Brandenburger Tor,
  Fernsehturm, Berliner Bär, Currywurst, Mauer-Motive) + official filiale price band
  (14,95–19,95 €) → reused verbatim-consistent with the site's own published pillar
  `blog/starbucks-tassen.html`, not re-fabricated.
- **Not independently verifiable and flagged in coverage.md:** whether the current Been There
  Berlin mug is in physical stock at a specific Berlin store today (stock fluctuates store by
  store; no live inventory API available).
