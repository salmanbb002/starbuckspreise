# Coverage and editorial QA — starbucks-siegen

Visible-text words (draft.md, excl. FAQ): ~640. FAQs: 12. Direct-answer block: 48 whitespace-delimited words.

| Check | Result |
|---|---|
| Tier 1 concepts | 4/4 (100%) — Starbucks, Siegen, City Galerie/Am Bahnhof 40, Öffnungszeiten all carry an address, hour, or population fact |
| Tier 2 concepts | 8/8 (100%) — Parkhaus, Hauptbahnhof, Lieferando, Uber Eats, Mobile Order & Pay, Rewards, WLAN, Universität Siegen |
| Tier 1 attribute/relationship | All four core entities carry an explicit attribute (address, hours, population, or store-name fact), not a bare mention |
| Heading hierarchy | One H1; one H3 nested correctly under its H2 (disambiguation aside); no skipped levels |
| Heading query ownership | Each H2/H3 owns a distinct phrase; no cannibalising duplicate headings |
| Answer-first (QUORA order) | Every question-style heading answers in its opening sentence |
| FAQ parity | All 12 FAQ answers match the FAQPage schema text verbatim |
| Schema | JSON valid (checked with `python3 -m json.tool`); author field uses existing site convention (Organization, no invented person); not run through an external Rich Results validator — user should do so before deploy |
| Internal links | `/blog/starbucks-preise`, `/blog/starbucks-groessen-tall-grande-venti`, `/blog/starbucks-in-der-naehe`, `/blog/starbucks-geoeffnet` — all four already exist on the site |
| Information gain | (1) dated delivery-platform comparison with real numbers (rating/fee/time/minimum) neither aggregator publishes; (2) "Siegen Lane, Baton Rouge" disambiguation note, absent from every competitor source |

## Fact cross-check (every number/date/name traced to a source)

| Fact | Source |
|---|---|
| Am Bahnhof 40, 57072 Siegen; Tel. +49 271 30336040 | Official Starbucks store locator |
| Mo–Fr 08:30–20:00, Sa 09:00–20:00, So geschlossen | Official Starbucks store locator |
| Mo–Sa 10:00–20:00, So geschlossen (mall's own, noted as a minor discrepancy) | city-galerie-siegen.de |
| WLAN, Mobile Order & Pay, Rewards-Einlösung listed | Official Starbucks store locator |
| Kein Drive-Thru | Absence in official store locator amenity list (not directly stated — inferred from omission + center location; flagged below) |
| Parkhaus City-Galerie: 1.200 Stellplätze, 40 Frauen-/20 Behindertenparkplätze, 08:00–20:30 | siegen.de / city-galerie-siegen.de parking page (via search snippet) |
| ~40 Buslinien am Bahnhofsvorplatz | siegen.de / city-galerie-siegen.de parking page (via search snippet) |
| Lieferando: 4,1★, 19 Bewertungen, 35–50 Min., 6,79 € Gebühr, 20 € Mindestbestellwert | lieferando.de/speisekarte/starbucks-siegen (via search snippet) |
| Uber Eats lists the same store | ubereats.com store page (via search snippet) |
| Siegen: 102.685 Einwohner (Stand 31.12.2024) | IT.NRW / Land NRW official figure (via search snippet); Smart City Index 2025 cites 102.560 as a close alternate figure — both noted |
| Universität Siegen: 13.755 Studierende, 3.265 Studienanfänger*innen, WiSe 2025/2026 | uni-siegen.de official Studierendendaten page (via search snippet) |
| Siegen Lane, Baton Rouge, Louisiana — unrelated US Starbucks | Confirmed via search results (Tripadvisor, Yelp, starbucks.com listings for "Siegen Lane") |

## Intent check

Delivers on the dominant **visit-in-person/navigational** intent (address, hours, how to get there) plus the secondary informational hook (name-collision disambiguation) a plain directory listing doesn't answer.

## Readability

Estimated grade ~8-9 (German Realschule-level prose, short paragraphs, one idea per sentence) — in line with the Kassel/Trier sibling pages.

## E-E-A-T flags (need user's manual input before publishing)

- **Drive-Thru claim is an inference, not a direct statement** — the official store locator simply doesn't list a drive-thru amenity for this address; the copy says "nicht gelistet" (matches the Kassel/Trier phrasing convention) rather than asserting its absence as fact. Acceptable under that established site convention, but flagged per the fact-check rule.
- Author is listed as "StarbucksPreise Redaktion" (Organization), matching every sibling page — no individual byline/credentials exist to add.
- `datePublished`/`dateModified` set to 2026-09-17; update `dateModified` if this page is edited later.
- Run `schema.jsonld` through the Rich Results Test / schema.org validator before deploy (not done in this pass).
- Weekday-hours discrepancy between the official locator (8:30) and the mall's own page (10:00) is disclosed in-copy rather than silently resolved — confirm with a phone call or a site visit if precision matters for a paid campaign.
