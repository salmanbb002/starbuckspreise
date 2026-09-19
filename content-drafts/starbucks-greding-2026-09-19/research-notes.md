# Research notes — starbucks greding

## Step 1 — Intent + SERP
- Query volume: 110/mo, KD 24 (per calendar). Dominant intent: **visit-in-person / know-simple** ("is there a Starbucks in Greding, where, what hours").
- SERP for `"starbucks greding"` (exact-match search): no article-format competitors at all. Results were: Apple Maps place page, 2 official Starbucks store-locator pages (Ost + West), a Tank & Rast trade-press note (mobilityplaza.org), a local newspaper article (nn.de, Landkreis Roth edition), a Gelbe Seiten directory listing, 2 Serways rest-stop pages, and unrelated Starbucks Wikipedia pages (Café Grumpy, Starbucks Reserve — noise, discarded).
- No SERP features (no snippet/PAA box observed for this low-volume query) — outline follows the site's own established "city page" pattern instead (see Step 8).
- Fan-out: none meaningful surfaced (query too low-volume for autocomplete/PAA expansion).

## Step 2 — Head-entity research
- **Greding**: de.wikipedia.org/wiki/Greding — pop. 7,070 (31 Dec 2025), Landkreis Roth, Bavaria; ~50 km S of Nürnberg, ~32 km N of Ingolstadt.
- **Starbucks**: de.wikipedia.org/wiki/Starbucks.
- **A9 (Autobahn)**: de.wikipedia.org/wiki/Bundesautobahn_9.
- **Tank & Rast**: de.wikipedia.org/wiki/Autobahn_Tank_%26_Rast — operator of both rest stops.

## Step 3 — Title/metadata
- Title: "Starbucks Greding: Zwei Coffee Houses direkt an der A9"
- Meta: "Starbucks Greding liegt nicht in der Stadt, sondern an der Autobahn A9: Zwei Coffee Houses in den Raststätten Greding-Ost und Greding-West, täglich 6–22 Uhr geöffnet."
- Slug: starbucks-greding

## Step 4 — Competitor fetch (substituted — no article competitors exist)
No competitor *articles* exist for this query (confirmed thin SERP). Per pipeline fallback rule, substituted 4 primary sources instead of competitor articles:
1. starbucks.de store locator — Greding Ost (85062-314859): address, hours 6–22 daily.
2. starbucks.de store locator — Greding West (85881-314444): same rest-stop pair, confirmed via search snippet.
3. koesching-aktuell.de (15 Dec 2025): Greding-West opening detail — 24 indoor + 32 terrace seats, ~150 total facility seats, design details, Tank & Rast's 12th Starbucks, €0.50 reusable-cup discount.
4. nn.de (11 Dec 2025, Landkreis Roth local paper): confirms Greding-West is "directly across" from the pre-existing Greding-Ost store, and is described as the *second* Coffee House in Landkreis Roth.
Supporting: gelbeseiten.de (independently confirms 6–22 hours), serways.de Greding-West and Greding-Ost pages (amenities, parking counts, fuel brand, EV charging brand — used to build the comparison table), and this site's own merged_stores.json.

## Step 5/6 — Entity ledger + tiers
See entities.json. Tier-1: Greding, Starbucks, A9, Raststätte Greding-Ost, Raststätte Greding-West, Tank & Rast. Tier-2: Landkreis Roth, Nürnberg, Ingolstadt, Shell, McDonald's, Dallmayr, reusable-cup discount. Tier-3: EnBW, E.ON, SANIFAIR.
Relationships: Greding —has no Starbucks in→ town center; Starbucks —operates at→ Raststätte Greding-Ost / Greding-West; Tank & Rast —operates→ both rest stops; Greding-West —opened Dec 2025 as→ Tank & Rast's 12th Starbucks; Greding-Ost —serves traffic toward→ Nürnberg.
Dedupe: no exact duplicates found. Parked: general Autobahn-rest-stop history (out of scope — not specific to Greding).

## Step 7 — Information-gain pass
What none of the raw sources combine: a **side-by-side Ost vs. West comparison table** (fuel brand is the same Shell at both, but co-tenant restaurant, parking capacity, and EV charging brand all differ) plus the discrepancy catch between this site's own OSM-derived dataset (claims "24/7" for Greding-Ost) and the two independently-confirmed sources (6:00–22:00). Also the explanation of *why* a single town shows two separate Starbucks entries (one rest stop per driving direction) — no source states this explicitly; it's a reasoned synthesis from the confirmed facts, flagged as such rather than presented as a quoted fact.

## Step 8 — Heading map
1. H1 – Starbucks Greding: Zwei Coffee Houses direkt an der A9 (focus kw)
2. H2 Gibt es einen Starbucks in Greding? — know-simple, tier-1 Greding+Starbucks
3. H2 Die beiden Standorte: Greding-Ost und Greding-West im Vergleich — core section, tier-1 both rest stops + Tank & Rast, comparison table
4. H2 Öffnungszeiten und Erreichbarkeit — tier-2 hours, discrepancy note (info-gain)
5. H2 Warum zwei Starbucks an einer Raststätte? — synthesis/explainer
6. H2 Was bieten die Raststätten sonst noch? — tier-2/3 amenities
7. H2 Weitere Filialen in der Region — internal links (Nürnberg, Ingolstadt, Bamberg, near-me, deutschland-filialen)
8. FAQ (10 questions, last)

## Step 8e — Internal links / cannibalisation
Outbound: /blog/starbucks-bamberg (sibling "no town-center store" page), /blog/starbucks-in-der-naehe, /blog/starbucks-deutschland-filialen. No existing page on this site currently covers Greding — confirmed via `grep -ri greding` against the blog folder (no hits) and a live-site 404 check on /blog/starbucks-greding before writing. No cannibalisation risk identified.

## Fact-check trace
- Population 7,070 (31 Dec 2025), Landkreis Roth, Bavaria, distances to Nürnberg/Ingolstadt — de.wikipedia.org/wiki/Greding.
- Two-rest-stop-pair, "directly across," Greding-West = second in Landkreis Roth — nn.de article.
- Greding-West: 24+32 seats, ~150 total, Tank & Rast's 12th Starbucks, design details, €0.50 cup discount — koesching-aktuell.de.
- Hours 6:00–22:00 daily — starbucks.de store locator + gelbeseiten.de (two independent sources, cross-checked).
- Parking/fuel/EV-charging/co-tenant counts per side — serways.de Greding-West and Greding-Ost pages.
- "24/7" discrepancy for Greding-Ost — this site's own merged_stores.json (flagged as unresolved conflict, not silently dropped).
- Direction "Richtung Nürnberg" for Greding-Ost — WebSearch result snippet (single source; flagged in coverage.md as not independently cross-verified).
