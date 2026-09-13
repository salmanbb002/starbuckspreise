# Research notes — "starbucks braunschweig"

Date researched: 2026-09-13. Language: de-DE. Page type: City/Location blog post (Content_Calendar Day 8, cluster "City / Location Pages", intent Navigational+Transactional, SV 720 / KD 30).

## Step 1 — Intent + SERP

Dominant intent: **visit-in-person / navigational** ("where is the Braunschweig Starbucks and is it open"), with a secondary **know** intent around the 2024 reopening story. No classic featured snippet/PAA block observed for this long-tail city query; results are dominated by local-directory aggregators (Öffnungszeitenbuch, Offen.net, Ortsdienst, Das Örtliche, Kaufda-style sites) plus the official Starbucks store locator and one local-news piece.

SERP features: local-pack-style directory listings, no PAA box surfaced, no table/list snippet.

Query fan-out: "starbucks braunschweig öffnungszeiten", "starbucks braunschweig kohlmarkt", "starbucks braunschweig schloss arkaden", "starbucks braunschweig damm", "gibt es noch starbucks in braunschweig".

## Step 2 — Head-entity research

- **Starbucks** — Organization. `sameAs`: https://de.wikipedia.org/wiki/Starbucks. Global coffeehouse chain; operates a German subsidiary (Starbucks Coffee Deutschland GmbH).
- **Braunschweig** — City, Lower Saxony. `sameAs`: https://de.wikipedia.org/wiki/Braunschweig. Per the reopening announcement, described by Starbucks as Lower Saxony's second-largest city.

## Step 3 — Title/metadata

- Title: "Starbucks Braunschweig: Filiale, Adresse & Öffnungszeiten am Damm" (61 chars)
- H1: "Starbucks Braunschweig: Filiale, Adresse und Öffnungszeiten am Damm"
- Meta description: "Starbucks Braunschweig: Die einzige aktuelle Filiale liegt am Damm 22. Adresse, Öffnungszeiten, Lieferung und warum ältere Standorte nicht mehr gelten." (153 chars)
- Slug: starbucks-braunschweig

## Step 4 — Competitor fetch (4 distinct domains)

| id | URL | Notes |
|---|---|---|
| oezb | https://www.oeffnungszeitenbuch.de/filiale/Braunschweig-Starbucks%2520Coffee-133825P.html | H1 "Starbucks Coffee in Braunschweig"; lists **Bohlweg 74-75 (Schloss Arkaden)** as the address, Mo–Fr 08:00–20:00, Sa 08:30–20:00, Su closed; also references "Starbucks Coffee House, Kohlmarkt 18" as a second nearby entry. No FAQ. |
| offennet | https://www.offen.net/braunschweig/filialen/starbucks-1HVM0.html | H1 "Starbucks in Braunschweig"; lists 2 Innenstadt locations: Kohlmarkt 18 and Bohlweg 74. No hours shown, no FAQ. |
| tonline | https://braunschweig.t-online.de/region/braunschweig/id_100517224/braunschweig-starbucks-eroeffnet-anfang-dezember-filiale-in-der-innenstadt.html | Local news (pre-opening announcement). States Starbucks fully left Braunschweig ~5 years earlier; prior locations were Kohlmarkt (ran ~10 years, closed) and Schloss-Arkaden (closed 2016); new ~200 m² store opens early December 2024 on Damm in the pedestrian zone; Starbucks reasoning paraphrased: the two former coffee houses showed the site's potential, and Braunschweig is Lower Saxony's second-largest city. |
| yelp | https://www.yelp.com/biz/starbucks-braunschweig-3 | Lists Kohlmarkt 18 with status **"CLOSED"** (updated March 2026) — third-party confirmation the Kohlmarkt address is no longer trading. |

**Fetch note:** none of the four fetches failed; no substitution needed.

## Step 5/6 — Entity ledger (consolidated, tiered)

| canonical | type | tier | competitor_count | in_title_or_h2 | relationship |
|---|---|---|---|---|---|
| Starbucks | Organization | 1 | 4 | yes | Betreibt die einzige aktuelle Filiale in Braunschweig am Damm 22. |
| Braunschweig | Place | 1 | 4 | yes | Ort der Filialsuche; laut Starbucks zweitgrößte Stadt Niedersachsens. |
| Damm 22 | Place (store address) | 1 | 3 | yes | Aktuelle, einzige aktive Adresse laut offiziellem Store Locator und Lieferplattformen. |
| Kohlmarkt 18 | Place (former store) | 2 | 3 | no | Frühere Filiale, ca. 10 Jahre betrieben, laut Yelp seit März 2026 als "CLOSED" geführt; laut t-online bereits ~2019 aufgegeben. |
| Schloss-Arkaden / Bohlweg 74-75 | Place (former store) | 2 | 3 | no | Frühere Filiale im Einkaufszentrum Schloss-Arkaden, laut t-online 2016 geschlossen; taucht in zwei Verzeichnissen weiterhin als aktueller Standort auf. |
| Öffnungszeiten | Concept/term | 1 | 3 | yes | Damm 22: Mo–Fr 08–20 Uhr, Sa 09–20 Uhr, So 11–18 Uhr laut offiziellem Store Locator. |
| Mobile Order & Pay | Concept/term | 2 | 0 (official locator only) | no | Store Locator listet Vorbestellfunktion für Damm 22. |
| Starbucks Rewards | Product | 2 | 0 | no | Store Locator listet Rewards-Einlösung für Damm 22. |
| WLAN | Concept/term | 2 | 0 | no | Store Locator listet "drahtloser Hotspot" für Damm 22. |
| Lieferung (Uber Eats/Wolt/Lieferando) | Concept/term | 2 | 0 | yes | Alle drei Plattformen listen Starbucks Damm 22; Abholung (Pick-up) ebenfalls über die Apps wählbar; Lieferkarte ist eingeschränkt. |
| Fußgängerzone Damm | Place | 2 | 1 | no | t-online verortet die neue Filiale in der Fußgängerzone am Damm. |
| Niedersachsen | Place | 3 | 1 | no | Braunschweig als zweitgrößte Stadt des Bundeslandes genannt. |
| Drive-Thru | Concept/term | 3 | 0 | no | Nicht als Ausstattung von Damm 22 gelistet — bewusst nicht behauptet. |

**Dedupe log:** "Starbucks Coffee House" (offen.net) and "Starbucks Coffee" (oezb) merged into the single Kohlmarkt/Schloss-Arkaden former-location entries — same two addresses, different aggregator labels. No tier-1/2 term parked/dropped.

## Step 7 — Information gain

All four competitor/aggregator pages either omit the 2024 reopening story entirely or actively show stale addresses (Kohlmarkt 18, Schloss-Arkaden/Bohlweg 74-75) as if still trading, when the only address confirmed live by the official Starbucks locator and all three delivery platforms is **Damm 22**. **Committed information-gain element:** a short "aktuell vs. veraltet" timeline/comparison explicitly naming which addresses are historical and why directories still show them, sourced to the Yelp "CLOSED" flag and the t-online closure dates — none of the four competitors state this.

## Step 8 — Heading map

| level | heading | focus/LSI phrase | question answered | entities carried |
|---|---|---|---|---|
| H1 | Starbucks Braunschweig: Filiale, Adresse und Öffnungszeiten am Damm | starbucks braunschweig | — | Starbucks, Braunschweig |
| — | (direct-answer block) | — | Wo und wann ist der aktuelle Starbucks in Braunschweig? | Starbucks, Damm 22, Öffnungszeiten |
| H2 | Wo ist der aktuelle Starbucks in Braunschweig? | starbucks braunschweig adresse | Wo genau liegt die Filiale? | Damm 22, Fußgängerzone Damm |
| H3 | Warum listen manche Verzeichnisse noch den Kohlmarkt oder die Schloss-Arkaden? | starbucks braunschweig kohlmarkt / schloss arkaden | Sind diese alten Adressen noch aktuell? | Kohlmarkt 18, Schloss-Arkaden |
| H2 | Welche Öffnungszeiten gelten am Damm 22? | starbucks braunschweig öffnungszeiten | Wann ist geöffnet? | Öffnungszeiten |
| H2 | Warum kehrte Starbucks erst Ende 2024 nach Braunschweig zurück? | starbucks braunschweig eröffnung | Warum gab es Jahre keinen Starbucks? | Braunschweig, Kohlmarkt 18, Schloss-Arkaden |
| H2 | Was bietet die Filiale am Damm? | starbucks braunschweig ausstattung | WLAN, Vorbestellen, Rewards? | Mobile Order & Pay, Starbucks Rewards, WLAN |
| H2 | Können Sie sich Starbucks aus Braunschweig liefern lassen? | starbucks braunschweig lieferung | Liefert Uber Eats/Wolt/Lieferando? | Lieferung |
| H2 | Wie kommen Sie am besten zum Damm 22? | starbucks braunschweig anfahrt | Anfahrt/Parken? | Fußgängerzone Damm |
| H2 | Häufig gestellte Fragen | starbucks braunschweig faq | — | — |

## Internal-link plan

- Anchor "Starbucks in der Nähe" → `/blog/starbucks-in-der-naehe` (sibling near-me pillar; no cannibalisation — that page is national/generic, this one is Braunschweig-specific).
- Anchor "Starbucks geöffnet" → `/blog/starbucks-geoeffnet` (opening-hours pillar).
- No existing page targets "starbucks braunschweig" specifically — no cannibalisation risk.

## FAQ source map

Sourced from: fan-out queries, the comeback narrative, and genuine follow-ups not covered in the body (delivery menu limits, drive-thru absence, past closures, parking, second location).

## Fact cross-check

Every address, date, and hour below traces to the source table above (starbucks.de store locator ID 81776-311207, t-online article, Yelp listing, delivery platform pages). No price, phone number, or job-count claim is made — the t-online source did not state them, so none are invented.

## E-E-A-T / YMYL flags

- Not YMYL. Low risk.
- Hours and "only current location" claim are time-sensitive — flagged in coverage.md for a manual recheck before publishing.
- No first-person "I visited" claim written — none of the sources support genuine first-hand experience.
