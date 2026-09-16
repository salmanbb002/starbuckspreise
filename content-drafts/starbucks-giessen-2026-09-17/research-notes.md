# Research notes — "starbucks giessen"

## Step 1 — Intent + SERP
- Dominant intent: **visit-in-person** (local) — "does Starbucks have a branch in Giessen, where, when open".
- Secondary intent: know-simple (opening date / backstory).
- SERP: local news outlets (hi-heute.de, giessener-anzeiger.de, giessen-aktuell.de) covering the August 2025 opening; official Starbucks store locator; Gelbe Seiten business listing; UberEats listing (unverifiable — 403, see Dedupe log).
- No featured snippet/PAA observed directly; treated as a local-business "know where/when" query, direct-answer block formatted as a standalone location + hours statement (matches site's existing Kassel/Trier convention).
- Fan-out: "starbucks gießen öffnungszeiten", "starbucks gießen seltersweg", "gibt es starbucks in gießen", "wann eröffnet starbucks gießen".

## Step 2 — Head-entity research
- **Starbucks Corporation** — sameAs https://de.wikipedia.org/wiki/Starbucks
- **Gießen** (city, ~90,000 residents, Hesse) — sameAs https://de.wikipedia.org/wiki/Gie%C3%9Fen
- **Justus-Liebig-Universität Gießen (JLU)** — ~25,000+ students, sameAs https://de.wikipedia.org/wiki/Justus-Liebig-Universit%C3%A4t_Gie%C3%9Fen — unlinked-entity risk avoided, has a real Wikipedia page.

## Step 4 — Sources fetched (competitor-equivalent: local news + official listings, no direct blog competitors exist for this exact query)
1. https://www.starbucks.de/de/store-locator/86162-315307/giessen-seltersweg-39 — official store locator: address, hours, amenities.
2. https://www.giessener-anzeiger.de/stadt-giessen/ab-mitte-august-gibt-kaffee-bei-starbucks-in-giessen-93860148.html — opening date, ~170 sqm, former tenant White Stuff, site-selection quote.
3. WebSearch aggregate (hi-heute.de, giessen-aktuell.de, gelbeseiten.de headlines) — corroborated address/opening, not fetched in full (headline-level confirmation only, no unique facts beyond #1/#2).
4. WebSearch: parking — giessen.de, mein-contipark.de, parkinglist.de, q-park.de — Parkhaus Karstadt (Seltersweg 64, 741 spaces, hours), Parkhaus GALERIA (Reichensand), Contipark Selters Tor (Südanlage).
5. WebSearch: transit — giessen-entdecken.de walking-route description (Hauptbahnhof → Bahnhofstraße → Mathematikum → Liebigstraße → Frankfurter Straße → Selterstor → Seltersweg), Wikipedia "Nahverkehr in Gießen", Moovit — bus lines 372/375, train lines ICE/RB41/RE98 near Seltersweg.
6. WebSearch: JLU student count — giessen.de, Wikipedia JLU — ~25,000+ students, "Studentenstadt Nr. 1" framing (student-to-resident ratio).
7. WebSearch: Lieferando delivery cities — lieferando.de city-specific Starbucks pages (Frankfurt, Stuttgart, Köln, Hamburg, München, Hannover, Dresden, Bonn, Düsseldorf, Mannheim) — Gießen absent from the list → used as the information-gain element.

**Fetch failure:** UberEats listing "starbucks-kilianstrasse" returned HTTP 403; likely unrelated (Kilianstraße/Kilianskirche is associated with Heilbronn, not Gießen) — excluded from the draft rather than guessed at.

## Step 5/6 — Entity ledger (condensed; single-source topic, no multi-competitor heading matrix applies)

| canonical | type | aliases | sameAs | kind | tier |
|---|---|---|---|---|---|
| Starbucks | Organization | Starbucks Corporation | de.wikipedia/Starbucks | entity | 1 |
| Gießen | Place | Giessen | de.wikipedia/Gießen | entity | 1 |
| Seltersweg 39 | Place/address | — | — (unlinked) | entity | 1 |
| Goethestraße | Place | — | — (unlinked) | entity | 2 |
| White Stuff | Organization | — | — (unlinked) | entity | 2 |
| Justus-Liebig-Universität Gießen | CollegeOrUniversity | JLU | de.wikipedia/JLU_Gießen | entity | 1 |
| Parkhaus Karstadt | Place | — | — (unlinked) | entity | 2 |
| Hauptbahnhof Gießen | Place | — | — (unlinked) | entity | 2 |
| Lieferando | Organization | — | — (unlinked) | entity | 2 |
| Mobile Order & Pay | Process | — | — | term | 2 |
| Starbucks Rewards | Product/Process | — | — | term | 2 |
| Drive-Thru | Concept | — | — | term | 2 |

**Relationships:**
- Starbucks —opened branch in→ Gießen (August 2025, first in the city)
- Filiale —located at→ Seltersweg 39, corner Goethestraße
- Filiale —replaced→ White Stuff (former tenant)
- Filiale —size→ ~170 m²
- Gießen —home to→ Justus-Liebig-Universität (~25,000 students)
- Filiale —lacks→ Drive-Thru, listed outdoor seating
- Filiale —offers→ WLAN, Mobile Order & Pay, Rewards redemption
- Lieferando —does not yet serve→ Gießen (as of research date)

## Step 7 — Information-gain element
No existing article (site or competitor) explicitly states Gießen's **delivery-service gap** (Lieferando serves 10 major German cities with Starbucks but not Gießen) or connects the site-selection to Gießen's "Studentenstadt Nr. 1" status with a hard student count. Both used as the original angle (sections 6 and 7).

## Step 8 — Heading map
1. H2 Wo liegt der Starbucks in Gießen? — location/address, tier-1 Seltersweg/Gießen, former-tenant relationship
2. H2 Öffnungszeiten im Seltersweg 39 — hours table
3. H2 Wie und wo parken Sie am besten? — Parkhaus Karstadt/GALERIA/Selters Tor
4. H2 Mit Bus und Bahn zum Seltersweg — walking route, bus 372/375, train lines
5. H2 Was bietet die Filiale? — amenities, no drive-thru, price-list internal links
6. H2 Können Sie sich Starbucks aus Gießen liefern lassen? — Lieferando gap (info-gain)
7. H2 Warum hat Starbucks ausgerechnet Gießen als Standort gewählt? — JLU/Studentenstadt angle (info-gain), internal links
8. H2 FAQ (12 questions)

## Step 8e — Internal links / cannibalisation check
- Links out to: /blog/starbucks-preise, /blog/starbucks-groessen-tall-grande-venti, /blog/starbucks-in-der-naehe, /blog/starbucks-geoeffnet.
- No existing starbuckspreise.com article targets "starbucks giessen" — no cannibalisation found.
- Sibling location pages (Kassel, Trier, Würzburg, etc.) not linked directly from this page since they're not geographically adjacent to Gießen; the general "Starbucks in der Nähe" hub covers that role.

## Dedupe log
- Removed: UberEats "starbucks-kilianstrasse" listing — likely a different city (Heilbronn), fetch blocked (403), not used per no-fabrication rule.
- Parked: exact tram history trivia (1941 streetcar line discontinued) — out of scope for a location/hours page, not tier-1/2.

## FAQ source map
All 12 FAQs sourced from: official store locator (address, hours, amenities), giessener-anzeiger.de (opening date, size, former tenant), lieferando.de city list (delivery gap), giessen.de/Wikipedia (student count/Studentenstadt claim), transit research (walking route, bus lines). No PAA/competitor-FAQ block existed to source from (no comparable competitor article found) — all questions are genuine reader follow-ups derived from the entity research and fan-out.
