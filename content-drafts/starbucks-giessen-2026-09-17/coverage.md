# Coverage QA — starbucks-giessen

## Entity coverage
- Tier 1 (Starbucks, Gießen, Seltersweg 39, JLU): 4/4 covered, all with a stated attribute/relationship — 100%.
- Tier 2 (Goethestraße, White Stuff, Parkhaus Karstadt, Hauptbahnhof Gießen, Lieferando, Mobile Order & Pay, Starbucks Rewards, Drive-Thru): 8/8 covered — 100%.
- Tier 3 (Parkhaus GALERIA, Contipark Selters Tor, Mathematikum): all used naturally in the parking/transit sections.

## Heading architecture check
- One H1, no skipped levels (H1 → H2 → H3 in section 1 only, valid nesting).
- Every H2 owns a distinct focus/LSI phrase — no cannibalising duplicate headings.
- Heading list alone conveys the logic: location → hours → parking → transit → amenities → delivery gap → why-Gießen → FAQ.
- H2 count (7 body + FAQ) matches the fan-out/question set gathered in research.

## Answer-block check
- Direct-answer block: 3 sentences, ~55 words, standalone claim (location + hours + drive-thru fact), does not restate the H1, matches a "location + hours" local-business snippet format.
- Each H2 answers its implicit question in the first sentence (QUORA order held).

## Competitor-heading matrix
No directly comparable competitor article exists for "starbucks giessen" (searches surfaced only local-news pieces and the official store locator, not a blog-style competitor). Heading structure instead benchmarked against the site's own Kassel/Trier pages, which cover the same location-page intent successfully.

## Question coverage
- All 6 fan-out queries from Step 1 answered: opening hours, location/Seltersweg, "does Starbucks exist in Gießen", opening date, parking, delivery.
- No PAA box was present for this query; FAQ questions instead drawn from entity research gaps (size, transit, why-Gießen, price-list link).

## Fact cross-check
- Address, hours, amenities → official Starbucks store locator (research-notes.md source 1).
- Opening date, size, former tenant, site-selection quote → giessener-anzeiger.de (source 2).
- Parking facilities/hours → giessen.de / mein-contipark.de / parkinglist.de / q-park.de (source 4).
- Transit route/bus lines/train lines → giessen-entdecken.de, Wikipedia "Nahverkehr in Gießen", Moovit (source 5).
- Student count / Studentenstadt claim → giessen.de, Wikipedia JLU (source 6).
- Lieferando city list (delivery gap) → lieferando.de city pages (source 7).
- No unsourced numbers, dates, or names in the draft.

## Intent check
Delivers what a "starbucks giessen" searcher wants: confirms the store exists, gives exact address/hours, and adds practical visit info (parking, transit, delivery) plus a genuine information-gain angle (delivery gap, site-selection reasoning). Visit-in-person intent satisfied.

## Readability
Estimated grade ~8-9 (German Realschule-level prose, short-to-medium sentences, no jargon beyond named entities). No overly dense passages.

## E-E-A-T flags (for user, before publishing)
- **Author byline**: page uses the generic "StarbucksPreise Redaktion" organization author, same as existing Kassel/Trier pages — no individual byline/credentials, consistent with site convention, not a regression.
- **Hero image**: reused the generic `kaffee-hero.webp` (no dedicated Gießen photo exists in `img/blog/`) — same shortcut the Kassel/Trier pages take by reusing Braunschweig/Heilbronn heroes. Consider a real Seltersweg/Gießen photo if available.
- **Opening-hours drift**: hours sourced from the store locator on 2026-09-17; like all location pages on this site, flag for periodic re-verification since Starbucks can adjust hours without notice.
- **"Studentenstadt Nr. 1" claim**: framed as a commonly cited characterization (per search aggregation), not an official ranking body's certified title — phrased with "gilt als" in the draft to avoid overclaiming.
- No invented statistics, quotes, or credentials were used.
