# Research notes — "starbucks bamberg"

## Step 1 — Intent + SERP
- Dominant intent: **visit-in-person / know-simple** ("is there a Starbucks in Bamberg, where, when open"). Secondary: **navigational confusion** (Bamberg, SC, USA also returns in generic search tools).
- SERP for the exact phrase is thin: no dedicated "Starbucks Bamberg" article exists on any competitor domain. Results are dominated by kleinanzeigen.de merchandise classifieds ("Starbucks Tasse in Bamberg"), a Yellow Pages page for **Bamberg, South Carolina, USA**, generic Germany-wide store-finder directories (meinprospekt.de, kaufda.de, cylex), and unrelated job listings. No JS-rendered official store locator result surfaced in search snapshots.
- SERP features: none of note (no featured snippet, no local pack — Google has nothing to pack because no store exists).
- Query fan-out / related: "starbucks bamberg öffnungszeiten", "starbucks tasse bamberg" (merch/collectible angle, real search demand per kleinanzeigen results), "starbucks in der nähe bamberg", "starbucks bamberg south carolina" (cross-contamination from the US town).
- **No 4 distinct competitor articles exist for this query** — genuinely thin/uncontested SERP. Per pipeline Step 4 fallback rule: substituted the site's own prior "no-store" city page (`/blog/starbucks-trier`, live, fetched in full) as the structural model, since it is the closest matching content type on the same domain, plus the general directory pages to extract what a Germany-wide Starbucks-locations list does/doesn't include for Bamberg.

## Step 2 — Head-entity research
- **Bamberg** (city, Bavaria, Germany) — Wikidata Q2749; ~77,000 residents (2024); UNESCO World Heritage "Altstadt von Bamberg" since 11 Dec 1993 (Berg-, Insel- und Gärtnerstadt districts, 1,000+ listed buildings). Source: bamberg.info / unesco.de.
- **Starbucks Corporation** — Wikidata Q37158; US coffeehouse chain; German operations via Starbucks Deutschland (starbucks.de), official store locator at starbucks.de/de/store-locator.
- **Hallstadt** — small town directly adjoining Bamberg, in the Bamberg district; site of the nearest café-chain alternative.

## Step 4/5 — "Competitor" extraction (adapted — thin SERP)
No independently-ranking dedicated Starbucks-Bamberg article exists. Extraction instead drawn from:
1. Own site's `starbucks-trier` page (live) — heading pattern for "no store in this city" pages: existence question → naming-confusion section(s) → nearest real locations w/ distance+access → why-no-store speculation → local alternative → "watch for opening" → FAQ.
2. Germany-wide directory pages (cylex Filialfinder brand list, meinprospekt.de) — list of German cities Starbucks names as having locations; **Bamberg is absent** from every list checked.
3. Own site's `merged_stores.json` (140-row scraped store dataset, official store-locator + OSM/Overpass sourced) — zero rows match "Bamberg". Confirms no listed store.

Entities/terms found across these sources (single pooled list, since no per-competitor heading breakdown exists for a query with no competing articles):
Starbucks, Bamberg, Hallstadt, Coffee Fellows, market Einkaufszentrum, UNESCO-Welterbe, Altstadt, A70, A3, Nürnberg, Hauptmarkt, Hefnersplatz, Häusling (A3 Autobahn), Bamberg South Carolina, Store Locator, Öffnungszeiten, Filiale — 15 terms.

## Step 6 — Entity map + tiers
See `entities.json`. Tier 1: Bamberg, Starbucks (Corporation), "no store in Bamberg" fact. Tier 2: Hallstadt/Coffee Fellows alternative, nearest real Starbucks (Nürnberg + A3 Häusling rest stop), Bamberg-South-Carolina naming confusion, UNESCO Altstadt context. Tier 3: specific Nürnberg branch addresses, A70 corridor detail.

**Relationships:**
- Bamberg —has no— Starbucks Coffee House (as of Sept 2026)
- Nürnberg (Hauptmarkt 1 / Hefnersplatz 10) —nearest full-service Starbucks to→ Bamberg, ~55–60 km by road
- Häusling / A3 Autobahn service area (Aurach-Süd, near Herzogenaurach) —nearest Starbucks of any kind to→ Bamberg, ~40–45 km, 24/7, highway-access only, not a walk-in-city store
- Bamberg —confused in search with→ Bamberg, South Carolina, USA (unrelated town, own separate Starbucks-adjacent search results)
- Coffee Fellows —operates a shop in→ "market" Einkaufszentrum, Hallstadt (Bamberg's direct neighbouring town, on the Bamberg–Nürnberg axis, A70 exit)
- Bamberg Altstadt —UNESCO World Heritage since→ 1993

## Step 7 — Information gain
All the generic directory sites just fail to answer the question at all (they list Germany-wide Starbucks cities and simply omit Bamberg without saying so explicitly, forcing the reader to infer it). None mention the Bamberg/South-Carolina name collision, none mention the A3 Häusling highway Starbucks as the literal-nearest option, and none give real driving distances. **Information-gain element**: a distance-ranked "nearest options" table (Autobahn rest-stop vs. Nürnberg city center) plus an explicit callout resolving the Bamberg (Germany) vs. Bamberg (SC, USA) search confusion.

## Step 8 — Heading + keyword + question map
| Level | Heading | Focus/LSI phrase | Question answered | Tier-1/2 carried |
|---|---|---|---|---|
| H1 | Starbucks Bamberg: Gibt es eine Filiale in der Stadt? | starbucks bamberg | primary query | Bamberg, Starbucks, no-store fact |
| Direct answer | (block, not heading) | — | is there a Starbucks in Bamberg | no-store fact |
| H2 | Gibt es einen Starbucks in Bamberg? | starbucks bamberg filiale | confirms absence, since when checked | Bamberg, Starbucks |
| H3 | Warum taucht bei der Suche manchmal ein Ergebnis aus den USA auf? | starbucks bamberg south carolina | naming confusion | Bamberg-SC confusion |
| H2 | Wo liegt der nächstgelegene Starbucks? | nächster starbucks bamberg | nearest option incl. distance | Nürnberg, Häusling/A3 |
| H3 | Starbucks an der A3 bei Häusling/Herzogenaurach | starbucks a3 | closest of all, highway-only | Häusling |
| H3 | Starbucks in der Nürnberger Innenstadt | starbucks nürnberg | closest full city store | Nürnberg |
| H2 | Warum hat Bamberg noch keinen Starbucks? | starbucks bamberg öffnung | speculation given UNESCO Altstadt size limits | UNESCO Altstadt |
| H2 | Welche Alternative gibt es direkt in Bamberg? | coffee fellows bamberg | local alternative | Hallstadt/Coffee Fellows |
| H2 | Eine Neueröffnung im Blick behalten | starbucks bamberg neueröffnung | how to monitor | Store Locator |
| H2 | Frequently Asked Questions | — | fan-out | all |

## Step 8e — Internal links
- `/blog/starbucks-trier` — sibling "no store in this city" page, same pattern, direct cross-link both directions.
- `/blog/starbucks-in-der-naehe` — general nearest-store finder, link from "nächstgelegener Starbucks" section.
- `/blog/starbucks-geoeffnet` — general opening-hours rules, link from FAQ.
- `/blog/starbucks-wuerzburg` (calendar-published) — another Franconia city page, worth a "nearby cities" cross-link once confirmed live.
- No cannibalisation risk found — no existing page on this site or elsewhere targets "starbucks bamberg".

## Fact sourcing
- Bamberg population (~77,000) & UNESCO Altstadt (1993, Berg-/Insel-/Gärtnerstadt, 1,000+ listed buildings): bamberg.info, unesco.de (Step 1/2 search).
- Nürnberg Starbucks addresses (Hauptmarkt 1, Hefnersplatz 10) + coordinates: site's own `merged_stores.json` dataset.
- A3 Häusling/Aurach-Süd 24/7 Starbucks: site's own `merged_stores.json` dataset (id 399216246).
- Zero Bamberg rows in `merged_stores.json` (140-store dataset): direct file check, confirms no listed store.
- Coffee Fellows Hallstadt "market" shopping centre, opened as their 17th shop, at the A70 exit on the Bamberg–Nürnberg axis: franchise.coffee-fellows.de press page.
- Bamberg, South Carolina naming confusion: yellowpages.com "Starbucks Locations & Hours Near Bamberg, SC" appearing in searches for the German city.
- Driving distances (Nürnberg ~55–60 km, A3 Häusling ~40–45 km) are straight-line-derived estimates from the dataset's lat/lon (haversine ×~1.3 road-factor approximation), **not** a routed Google Maps figure — flagged in coverage.md for the user to verify with a live maps query before publishing exact numbers.
