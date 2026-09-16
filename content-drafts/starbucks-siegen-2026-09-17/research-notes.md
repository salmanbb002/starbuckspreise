# Research notes — "starbucks siegen"

Date researched: 2026-09-17. Language: de-DE. Page type: City/Location blog post (Content_Calendar keyword "starbucks siegen", SV 260 / KD 24, Priority Medium).

## Step 1 — Intent + SERP

Dominant intent: **visit-in-person / navigational** (where is the Siegen Starbucks, is it open now). No classic featured snippet observed; results dominated by local-directory aggregators (Öffnungszeitenbuch, Kaufda, meinprospekt, Das Telefonbuch/Gelbe Seiten) plus the official Starbucks store locator and the City Galerie Siegen mall's own page.

SERP features: local-directory listings, no PAA box surfaced, no table/list snippet. Note: "Siegen" also collides internationally with **Siegen Lane, Baton Rouge (Louisiana, USA)**, a street that hosts an unrelated Starbucks — aggregated search results mix German and US results for the bare query "starbucks siegen".

Query fan-out: "starbucks siegen öffnungszeiten", "starbucks siegen city galerie", "starbucks siegen am bahnhof", "starbucks siegen lieferservice".

## Step 2 — Head-entity research

- **Starbucks** — Organization. `sameAs`: https://de.wikipedia.org/wiki/Starbucks.
- **Siegen** — Place (Nordrhein-Westfalen). `sameAs`: https://de.wikipedia.org/wiki/Siegen. Population 102,685 (Stand 31.12.2024, Land NRW / IT.NRW; Smart City Index 2025 cites 102,560).
- **Universität Siegen** — Organization. `sameAs`: https://de.wikipedia.org/wiki/Universit%C3%A4t_Siegen. 13,755 Studierende im Wintersemester 2025/2026 (offizielle Studierendendaten der Universität), davon 3,265 Studienanfänger*innen.

## Step 3 — Title/metadata

- Title: "Starbucks Siegen: Filiale, Adresse & Öffnungszeiten in der City Galerie" (68 chars incl. brand suffix trimmed in H1)
- H1: "Starbucks Siegen: Filiale, Adresse und Öffnungszeiten in der City Galerie"
- Meta description: "Starbucks Siegen liegt in der City Galerie am Bahnhof 40. Adresse, Öffnungszeiten, Parken, Lieferung per Lieferando/Uber Eats und weitere Infos." (149 chars)
- Slug: starbucks-siegen

## Step 4 — Competitor fetch / sources (4 distinct domains + official)

| id | URL | Notes |
|---|---|---|
| official | https://www.starbucks.de/de/store-locator/55528-288975/siegen-city-galerie | Official store name "Siegen, City Galerie", Am Bahnhof 40, 57072 Siegen. Tel. +49 271 30336040. Hours Mo–Fr 08:30–20:00, Sa 09:00–20:00, So geschlossen. Amenities: Rewards-Einlösung, drahtloser Hotspot, Mobiles Bestellen und Bezahlen. |
| citygalerie | https://www.city-galerie-siegen.de/gastronomie/starbucks/ | Mall's own page. Address matches (Am Bahnhof 40). Hours shown as Mo–Sa 10:00–20:00, So geschlossen — differs from the official locator on weekday opening time, agrees on Sunday closure. |
| lieferando | https://www.lieferando.de/speisekarte/starbucks-siegen | Confirms delivery: 4.1★ (19 Bewertungen), Lieferzeit 35–50 Min., Liefergebühr 6,79 €, Mindestbestellwert 20,00 €. |
| ubereats | https://www.ubereats.com/de/store/starbucks-city-galerie/A4sNlqhSV1WBKijdy6fCKQ | Second delivery platform listing the same City-Galerie store — confirms multi-platform delivery coverage. |
| directories | kaufda.de, meinprospekt.de, oeffnungszeitenbuch.de | All list Am Bahnhof 40, 57072 Siegen; one third-party snippet claims Sunday 13:00–18:00 open, contradicted by both the official locator and the mall's own page (both say Sunday closed) — treated as the less reliable outlier. |
| parking | siegen.de, parkinglist.de, city-galerie-siegen.de/service/anfahrt-parken/parken | Parkhaus City-Galerie: 1,200 Stellplätze (davon 40 Frauenparkplätze, 20 Behindertenparkplätze), Öffnungszeiten 08:00–20:30, direkt am Hauptbahnhof Siegen. |

**Fetch note:** no fetch failed; the third-party "Sunday 13–18" claim was cross-checked against two independent sources (official locator + mall page) and rejected as the minority/stale figure.

## Step 5/6 — Entity ledger (consolidated, tiered)

| canonical | type | tier | competitor_count | in_title_or_h2 | relationship |
|---|---|---|---|---|---|
| Starbucks | Organization | 1 | 5 | yes | Betreibt die Filiale in der City Galerie Siegen, Am Bahnhof 40. |
| Siegen | Place | 1 | 5 | yes | Stadt in NRW mit rund 102.685 Einwohnern (Stand 31.12.2024). |
| City Galerie / Am Bahnhof 40 | Place (store address) | 1 | 5 | yes | Adresse der einzigen Filiale, direkt am Hauptbahnhof Siegen. |
| Öffnungszeiten | Concept/term | 1 | 3 | yes | Mo–Fr 08:30–20:00, Sa 09:00–20:00, So geschlossen (offizieller Store Locator). |
| Parkhaus City-Galerie | Place | 2 | 2 | no | 1.200 Stellplätze, direkt am Einkaufszentrum, Öffnungszeiten 08:00–20:30 Uhr. |
| Siegen Hauptbahnhof | Place | 2 | 1 | no | Rund 40 Buslinien am Bahnhofsvorplatz, zahlreiche Zuganbindungen in die Region. |
| Lieferando | Product/term | 2 | 1 | yes | Liefert Starbucks Siegen, 4,1★ (19 Bewertungen), 35–50 Min., 6,79 € Gebühr, 20 € Mindestbestellwert. |
| Uber Eats | Product/term | 2 | 1 | yes | Zweite Lieferplattform, listet dieselbe City-Galerie-Filiale. |
| Mobile Order & Pay | Concept/term | 2 | 1 | no | Laut Store Locator für diesen Standort verfügbar. |
| Starbucks Rewards | Product | 2 | 1 | no | Rewards-Einlösung laut Store Locator möglich. |
| WLAN | Concept/term | 2 | 1 | no | Drahtloser Hotspot laut Store Locator vorhanden. |
| Universität Siegen | Organization | 2 | 1 | no | 13.755 Studierende im WiSe 2025/2026, rund 1,5 km von der City Galerie entfernt. |
| Siegen Lane (Baton Rouge, USA) | Place | 3 | 2 | no | Unabhängige Straße/Starbucks in Louisiana, USA — Namensverwechslung bei internationalen Suchergebnissen, bewusst als Klarstellung behandelt statt ignoriert. |
| Drive-Thru | Concept/term | 3 | 0 | no | Nicht als Ausstattung gelistet — Center-Lage ohne Durchfahrt, bewusst nicht behauptet. |

**Dedupe log:** "Starbucks City Galerie" (Uber Eats) and "Siegen, City Galerie" (offizieller Locator) als ein Store zusammengeführt. Kein Tier-1/2-Begriff verworfen; "Siegen Lane" bewusst als Tier-3-Disambiguierung aufgenommen statt gestrichen.

## Step 7 — Information-gain pass

All local-directory competitors state only "delivery available" without numbers, and none disambiguate the international "Siegen" name collision. **Committed information-gain elements:**
1. A delivery-platform comparison with real, dated numbers (rating, delivery window, fee, minimum order) from Lieferando, plus the Uber Eats listing — none of the aggregators go this granular.
2. A short disambiguation note about "Siegen Lane" in Baton Rouge, Louisiana (an unrelated US Starbucks that pollutes international search results for the bare query) — mirrors the disambiguation approach already used on the Trier page for this site, but for a genuinely different confusion (name collision, not address confusion).

## Step 8 — Heading map

| # | Level | Heading | Phrase owned | Question answered | Tier-1/2 carried |
|---|---|---|---|---|---|
| — | H1 | Starbucks Siegen: Filiale, Adresse und Öffnungszeiten in der City Galerie | focus keyword | Where is Starbucks in Siegen | Starbucks, Siegen, City Galerie |
| 1 | H2 | Wo liegt der Starbucks in Siegen? | starbucks siegen city galerie | location | City Galerie/Am Bahnhof 40, Siegen Hauptbahnhof |
| — | H3 | Warum taucht bei "Starbucks Siegen" manchmal ein Ergebnis aus den USA auf? | siegen lane | disambiguation | Siegen Lane (Baton Rouge) |
| 2 | H2 | Welche Öffnungszeiten gelten in der City Galerie? | starbucks siegen öffnungszeiten | hours | Öffnungszeiten |
| 3 | H2 | Wie und wo parken Sie am besten? | parken city galerie | parking | Parkhaus City-Galerie |
| 4 | H2 | Mit Bus und Bahn zum Hauptbahnhof Siegen | starbucks siegen am bahnhof | transit | Siegen Hauptbahnhof |
| 5 | H2 | Was bietet die Filiale in der City Galerie? | mobile order rewards wlan | amenities | Mobile Order & Pay, Starbucks Rewards, WLAN, Drive-Thru (Verneinung) |
| 6 | H2 | Können Sie sich Starbucks aus Siegen liefern lassen? | starbucks siegen lieferservice | delivery | Lieferando, Uber Eats |
| 7 | H2 | Wer sind die Gäste rund um die City Galerie? | universität siegen | audience context | Universität Siegen |
| — | H2 | FAQ | — | — | all tier-1/2 recap |

## Step 8e — Internal links / cannibalisation

- Link to `/blog/starbucks-preise` (Preisliste, same as Kassel pattern) and `/blog/starbucks-groessen-tall-grande-venti` (Größen) from the amenities section.
- Link to `/blog/starbucks-in-der-naehe` and `/blog/starbucks-geoeffnet` from a closing regional-context line (matches Kassel/Trier pattern).
- **Cannibalisation check:** no existing page on starbuckspreise.com targets "starbucks siegen" — no merge needed. "starbucks açık" (separate keyword flagged by the user in the same batch) targets the same core intent as the existing `/blog/starbucks-geoeffnet` page — flagged separately, not written as its own page.

## FAQ source map

Sourced from: official store locator amenities list, the mall's own hours page, Lieferando's listed metrics, and genuine fan-out questions (Sunday hours, Siegen Lane confusion, drive-thru, delivery). No competitor FAQ block existed to reuse verbatim (none of the sources publish an FAQ section for this store) — all 12 questions are fan-out/aggregator-gap-derived, each answer traceable to a row in the entity ledger above.
