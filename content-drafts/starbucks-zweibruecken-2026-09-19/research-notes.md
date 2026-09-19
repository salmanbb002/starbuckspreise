# Research notes — starbucks zweibrücken

## Step 1 — Intent + SERP
Dominant intent: **visit-in-person** (local/navigational — address, hours). Secondary: know-simple (since store).
SERP features: local pack style results (directory listings), no featured snippet observed, no PAA expansion needed for a single-fact query this small.
Query fan-out: "starbucks zweibrücken öffnungszeiten", "starbucks zweibrücken outlet", "starbucks zweibrücken adresse".

## Step 2 — Head entity
- Starbucks Corporation — https://de.wikipedia.org/wiki/Starbucks
- Zweibrücken (city) — https://de.wikipedia.org/wiki/Zweibr%C3%BCcken
- Zweibrücken Fashion Outlet — unlinked entity (no clear standalone Wikipedia article found; part of the former Flugplatz Zweibrücken site)

## Step 3 — Title/metadata
Title: "Starbucks Zweibrücken: Filiale im Fashion Outlet, Adresse & Öffnungszeiten"
Meta: leads with address + hours, ~150 chars.
Slug: starbucks-zweibruecken

## Step 4 — Competitor sources (site's own store data + 3 external)
1. **Site's own dataset**: /Users/mac/July Projects/starbuckspreise/merged_stores.json — confirms a real store exists at "Allee der Rosse, Gewerbegebiet Flugplatz Zweibrücken" (OSM coordinate data, no hours/phone).
2. **zweibrueckenfashionoutlet.com/en/restaurants/starbucks** (official outlet site) — address Londoner Bogen 10-90, hours Mon-Sat 10:00-19:00, Sun closed, phone +49 6332 9935320, product description.
3. **rheinpfalz.de** (local news article on the 2019 opening) — opening date 31 Oct 2019, crowd on opening day, former Center-Information space, outdoor seating under construction at launch.
4. **oeffnungszeitenbuch.de** directory — address confirmed, hours listed as Mon-Sat 09:30-19:30 (differs from official site by 30 min each side — flagged, not resolved, both cited), phone + AmRest guest-service email confirmed.
- meinprospekt.de fetched but had no usable data (empty "no brochure this week" page) — dropped, not substituted with a 5th source since 3 usable competitor/directory sources plus the site's own dataset were sufficient for this small single-fact local page.
- gelbeseiten.de listing returned HTTP 410 Gone — dropped.

## Step 5/6 — Entity ledger (condensed; small page)
| canonical | type | tier | note |
|---|---|---|---|
| Starbucks | Organization | 1 | brand |
| Zweibrücken | Place | 1 | city |
| Zweibrücken Fashion Outlet | Place/Organization | 1 | unlinked, exact venue |
| Londoner Bogen 10-90 | Place (address) | 1 | exact address |
| 31. Oktober 2019 | Date | 2 | opening date |
| Center-Information (former space) | Concept | 2 | location context |
| Öffnungszeiten Mo-Sa 10-19 | Fact | 1 | core fact, with directory discrepancy noted |
| +49 6332 9935320 | Contact | 2 | phone |
| Rheinland-Pfalz | Place | 3 | region context |

Relationships: Starbucks —operates location in→ Zweibrücken Fashion Outlet; Filiale —eröffnete am→ 31. Oktober 2019; Filiale —occupies former space of→ Center-Information.

## Step 7 — Information gain
None of the 3 external sources combine the opening date + former-space context + the hours discrepancy in one place. Added: opening-date/crowd context, "why outlet not city center" framing, and an explicit flag on the two conflicting published hour ranges (info-gain element).

## Step 8 — Heading map
H1 → focus keyword. Direct-answer block → address/hours/opening date. H2s: location, hours (table), opening history, product offering, contact + internal links, FAQ.

## Step 8e — Internal links / cannibalisation
No existing Zweibrücken page on the site (confirmed 404 pre-write). Links out to starbucks-mainz, starbucks-trier, starbucks-deutschland-filialen, starbucks-preise. No cannibalisation risk identified.

## Step 10 — FAQ source map
10 questions: address/hours (site facts), Sunday hours (derived), opening date (rheinpfalz), city-center coverage (derived/negative), phone (outlet site), offerings (outlet site), outdoor seating (rheinpfalz, dated caveat), location rationale (analysis), pricing (site convention, cross-linked to starbucks-preise).
