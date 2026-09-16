# Research notes — "starbucks chemnitz"

Recherchestand: 17. September 2026.

## Step 1 — Intent + SERP

- **Dominant intent:** visit-in-person / know ("gibt es einen Starbucks in Chemnitz?"), same shape as the existing `starbucks-trier.html` page.
- **SERP composition observed:** aggregator/directory pages (fastfoodpreise.de, meinprospekt.de, Cylex Filialfinder), the official Starbucks store locator, a paywalled local-news article (Freie Presse) whose headline names Starbucks among "Läden, die doch nicht kommen" (stores that in the end didn't come) — a strong signal of a real, unresolved local rumor. No dedicated, well-written city-guide page exists yet for this query — same gap as Trier.
- **No featured snippet format identified** (aggregator noise, no clean extractable answer on page 1) — direct-answer block modelled as a paragraph, matching Trier.
- **Query fan-out:** "starbucks chemnitz altmarkt" (false-positive — resolves to Dresden Altmarkt on delivery aggregators), "starbucks chemnitz eröffnung", "nächster starbucks chemnitz", "coffee fellows chemnitz".

## Step 2 — Head entities

- **Chemnitz** (Place) — sameAs `https://de.wikipedia.org/wiki/Chemnitz`. Pop. 250,497 (30 June 2026, main residence; chemnitz.de press release), 3rd-largest city in Saxony, European Capital of Culture 2025.
- **Starbucks** (Organization) — sameAs `https://de.wikipedia.org/wiki/Starbucks`.
- **Coffee Fellows** (Organization, unlinked-quality but has a German Wikipedia page) — nearest real alternative chain with two Chemnitz locations.

## Step 4 — Competitor fetch results

- `freiepresse.de` article (13805456): fetch returned only the free preview (paywalled) — headline names Starbucks among openings "die doch nicht kommen" but full paragraph is not accessible. **Flagged, not fabricated** — reported as an unresolved local-press mention, not a confirmed fact either way.
- `ubereats.com/de/store/starbucks-altmarkt/...`: fetch blocked (403). Cross-checked via search instead — this listing resolves to **Dresden** Altmarkt 7 (confirmed against `starbucks.de` store locator), not a Chemnitz store; a classic aggregator mismatch, same failure mode as the Trier "Trierer Straße" confusion.
- Official `starbucks.de` store-locator detail pages returned 403 to direct fetch; used WebSearch result snippets (titles + indexed addresses) to confirm real Dresden Altmarkt 7 and Leipzig (Grimmaische Straße 1, Hauptbahnhof, Petersstraße 22, Hainstraße 16-18) locations instead of fabricating.
- No standalone, well-optimized competitor article on "starbucks chemnitz" found — nearest peers are generic directory-listing pages, not full articles. Entity extraction table skipped as not meaningful (no real per-heading competitor structure to extract); the page is built from verified facts instead, per Trier precedent.

## Entity ledger (tier)

| canonical | type | tier | note |
|---|---|---|---|
| Chemnitz | Place | 1 | city the query is about; population, Capital of Culture 2025 |
| Starbucks | Organization | 1 | brand; no store confirmed in Chemnitz |
| Dresden Altmarkt (Starbucks) | Place/Organization | 1 | nearest confirmed real store, ~77 km |
| Leipzig (Starbucks, multiple) | Place/Organization | 1 | 2nd nearest cluster, ~85 km, most store choice |
| Coffee Fellows | Organization | 2 | real local alternative, 2 Chemnitz branches |
| Freie Presse Starbucks rumor | Event/Claim | 2 | local press mention, unresolved — info-gain angle |
| Starbucks Store Locator | Product/Tool | 2 | how to check for a future opening |

## Relationships

- Starbucks —has no branch in→ Chemnitz (as of Recherchestand)
- Freie Presse (May 2025) —named Starbucks among→ Innenstadt-Neuansiedlungen, die "doch nicht kommen"
- Nächstgelegene Filiale —Dresden Altmarkt 7→ rund 77 km / 54 Min. über A4
- Zweitnächste Auswahl —Leipzig Innenstadt (mehrere Filialen)→ rund 85 km / 61 Min. über A72
- Coffee Fellows —betreibt 2 Filialen in→ Chemnitz (Neumarkt 2; Thomas-Mann-Platz 1)
- "Starbucks Altmarkt" (Aggregator-Treffer) —ist tatsächlich→ Dresden Altmarkt 7, nicht Chemnitz

## Step 7 — Information gain

All competitor-adjacent results are directory noise; none address the specific "did Starbucks almost open in Chemnitz" rumor or the Dresden-Altmarkt aggregator mismatch. **Original element:** a dedicated section unpacking the Freie Presse "Läden, die doch nicht kommen" mention plus the Altmarkt mismatch — the same "resolve the confusing search results" structure that worked for Trier — plus a comparison table of the two real nearest cities.

## Step 8 — Heading map

| Level | Heading | Question it answers | Tier-1/2 carried |
|---|---|---|---|
| H1 | Starbucks Chemnitz: Gibt es eine Filiale? Standorte und Alternativen | — | Chemnitz, Starbucks |
| H2 | 1. Gibt es einen Starbucks in Chemnitz? | direct fact | Chemnitz, Starbucks |
| H2 | 2. Was ist mit der angekündigten Eröffnung in der Innenstadt? | rumor resolution | Freie Presse rumor |
| H2 | 3. Die Verwechslung mit "Starbucks Altmarkt" | why search shows a hit | Dresden Altmarkt |
| H2 | 4. Die nächstgelegenen Filialen | where to actually go | Dresden, Leipzig |
| H2 | 5. Warum hat eine Großstadt wie Chemnitz noch keinen Starbucks? | why gap exists | Chemnitz population/Kulturhauptstadt |
| H2 | 6. Gute Alternativen direkt in Chemnitz | what to drink locally | Coffee Fellows |
| H2 | 7. Kann ich trotzdem Starbucks-Produkte kaufen? | packaged goods | Starbucks retail |
| H2 | FAQ | fan-out | all |

## Internal-link plan / cannibalisation check

- No existing page targets "starbucks chemnitz" → no cannibalisation.
- Link to `/blog/starbucks-preise` (pricing), `/blog/starbucks-in-der-naehe` (other locations), `/blog/starbucks-geoeffnet` (hours rules) — same cross-links used on Kassel/Trier.
- Link back from this page is not yet added to sibling pages — out of scope for this run (would touch shared files); noted for the coordinator.

## FAQ source map

10 FAQs sourced from: the core intent question, the two aggregator-confusion questions (Altmarkt, Freie Presse rumor), the nearest-store question set (mirrors Trier's proven FAQ shape), Coffee Fellows alternative, packaged-goods question, and a "how do I find out if one opens" question.

## Fact cross-check (Step 12 pre-check)

Every number in the draft traces to a source above: Chemnitz population (chemnitz.de press release), Chemnitz–Dresden distance (groute.ch / ADAC, ~77 km / 54 min via A4), Chemnitz–Leipzig distance (luftlinie.org driving figure, ~85 km / 61 min via A72), Coffee Fellows addresses (coffee-fellows.com location page + Yelp). The Freie Presse claim is reported as an unresolved press mention, explicitly not stated as fact either way.
