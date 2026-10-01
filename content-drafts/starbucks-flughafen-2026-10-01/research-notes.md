# Research notes: starbucks flughafen (+ bahnhof, autobahn)

Run date: 1 Oct 2026. Target: `/blog/starbucks-flughafen`, voice: du. Queue item #5 (~540/mo).

## Step 1: Intent + SERP

- **Dominant intent:** visit-in-person (is there a Starbucks at airport X / where / when open). **Secondary:** know-simple (vor/nach Sicherheitskontrolle, Card).
- **SERP (WebSearch):** frankfurt-airport.com location pages (DE/EN), munich-airport.com, Tripadvisor/Yelp (Düsseldorf Flughafenstr. 120, Frankfurt), inmapz FRA map, Wikipedia (airports). Results are directory/airport pages. No editorial competitor covers all of Germany.
- **SERP features (inferred):** local pack / Maps, sitelinks of airport sites, PAA ("Gibt es Starbucks am Flughafen X?").
- **Fan-out (Autocomplete_Oct2026):** 22× flughafen (berlin, düsseldorf, frankfurt, frankfurt terminal 1, hamburg, köln, münchen …), 32× bahnhof (augsburg, berlin, bremen, frankfurt, hamburg, hannover, leipzig, münster, stuttgart …), 11× autobahn (a1, a2, a3, a5, a7, a9, deutschland, raststätte, richtung münchen).

## Step 2: Head-entity + fact sources

| # | Source | Used for |
|---|---|---|
| S1 | **starbucks.de store-locator pages**, curl 1 Oct 2026 (embedded `storeDetails` JSON: name, address, isOpen, openHours for 1–7 Oct, features) | every hours row in the station and A9 tables; FRA Halle B L2 + Mezzanine; MUC T2; BER "Berlin Flughafen" + "BBI Airport E2 L01"; feature flags (Redeem Rewards, Mobile Order and Pay). Store numbers: 71641-305599, 29638-254609, 63382-284093, 78307-307453, 53226-281957, 57165-291185, 53185-282056, 53214-282066, 59910-294154, 68434-303199, 53114-282034, 53206-282040, 81097-310136, 83407-313030, 80818-309376, 52070-280686, 53168-281925, 53131-281948, 54990-288766, 85062-314859, 85881-314444, 84431-311014 |
| S2 | Same locator: **no data** for 27798-248728 (Hamburg Airport), 53186-282061 (DUS Terminal B), 53207-282047 (Dresden Hbf); Mainz Hbf 53118-282017 listed with `openHours: null` | Hamburg/Mainz "no hours shown"; Dresden omitted |
| S3 | starbucks.de/de/faq-starbucks-card | licence stores where the Card is NOT accepted: Berlin Zoo, Berlin BBI (T1 airside), Erfurt Hbf, FRA T1 Halle B, T1 Halle C, T2 airside, The Squaire, Hamburg Hbf Südsteg und West, Hamburg Airport, Hamburg Dammtor, Stuttgart Hbf, Bremen Hbf, Mainz Hbf, Raststätten Fernthal, Brohltal West, Ellwanger Berge, Holledau, Bruchsal, Holmmoor, Feuchtwangen, Medenbach. Card only in AmRest-operated stores ("bankaufsichtsrechtliche Regelungen") |
| S4 | frankfurt-airport.com/de/lokationen/s/starbucks.html (+ starbucks3 page) | T1 C L2 5:30–21:00; T1 B L2 6:00–21:30; T1 B L3 6:00–22:00; Squaire Mo–Fr 5:30–20:30, Sa/So 6–21; T2 E airside gates E1–9 6–22 |
| S5 | munich-airport.com/starbucks-1601601 | T2 Level 03, public area, gates G/H, daily 6–21 |
| S6 | dus.com/de-de/news-de/ausblick-shops (curl) + 404 on dus.com Starbucks page + gastro list has no Starbucks | "Coffee Fellows im Flugsteig B sowie in der Check-in-Halle … übernimmt zwei bisher von Starbucks betriebene Standorte" (April 2026) |
| S7 | koeln-bonn-airport.de Starbucks detail page (search snippet) | T1 / B Abflug, public, daily 6–21 |
| S8 | hamburg-airport.de/en/shop-dine/eat-drink/all/starbucks (search snippet) | T2 Arrivals Level 0, public, Mo–Fr+So 7:30–18:30, Sa 7:30–16:00 |
| S9 | corporate.berlin-airport.de press release 26 Mar 2024 + ber.berlin-airport.de news 15 Mar 2024 | BER: Starbucks behind security in T1 food court, >100 m², 28 seats; one on upper level of main hall |
| S10 | curl of stuttgart-airport.com/shopping-gastronomie, hannover-airport.de, airport-nuernberg.de, leipzig-halle-airport.de | 0 "starbucks" mentions (pages may be JS-rendered → phrased as "haben wir … nicht gefunden") |
| S11 | repo merged_stores.json (OSM) | München-Pasing Bahnhofsplatz, Siegen Am Bahnhof, Lörrach Bahnhofsplatz; A3 Häusling/Neschen, A61 Niederzissen (OSM only, parked) |

## Step 3: Metadata

- **Title:** Starbucks Flughafen, Bahnhof & Autobahn: alle Standorte 2026 (59)
- **H1:** Starbucks am Flughafen, Bahnhof und an der Autobahn: alle Standorte 2026
- **Meta:** see meta.json (151)
- **Slug:** /blog/starbucks-flughafen

## Step 4: Competitors

| C | URL | Notes |
|---|---|---|
| C1 | frankfurt-airport.com Starbucks location page | 4 locations + hours, phone, no landside/airside flag |
| C2 | munich-airport.com Starbucks | 1 location, T2 L03, public, 6–21 |
| C3 | Tripadvisor/Yelp "Starbucks Düsseldorf Flughafenstr. 120" | still lists DUS as open ("Updated Aug 2026"), Terminal B L3 4:30–21:00 → **stale** |
| C4 | starbuckspreise.de "Starbucks in meiner Nähe" | generic locator advice, no airport list |
No competitor has headings comparable to an editorial article; structure is built from fan-out instead.

## Step 5: Extraction (condensed)

C1: Terminal 1, Halle B, Halle C, Ebene 2, Ebene 3, The Squaire, Öffnungszeiten, Telefon, Kaffee & Snacks. C2: Terminal 2, Level 03, public area, Gates G/H, Iced Cappuccino, Kuchen, Tee, Zahlungsarten. C3: Flughafenstraße 120, Terminal B, Bewertungen, Fotos. C4: Store Locator, App, Öffnungszeiten, Filialen.

## Step 6: Entity ledger

See entities.json (31 rows: 8 tier-1, 13 tier-2, 10 tier-3).

**Relationships**
- Starbucks Card —only valid in→ AmRest-operated stores (S3)
- Lizenzstore —does not accept→ Starbucks Card (S3)
- FRA —has→ 5 Starbucks (T1 B L2, T1 B L3, T1 C L2, T2 E, Squaire)
- DUS —Starbucks replaced by→ Coffee Fellows (Apr 2026)
- BER food court Starbucks —opened→ March 2024, >100 m², 28 seats
- MUC T2 L03 —offers→ Rewards + Mobile Order
- A9 —hosts→ Fläming Ost, Greding Ost/West, Holledau
- A7 —hosts→ Ellwanger Berge, Holmmoor; A3 → Fernthal, Medenbach; A61 → Brohltal West; A5 → Bruchsal
- Store Locator feature flags —show→ Redeem Rewards / Mobile Order and Pay

**Parked:** Dresden Hbf (no locator data), OSM-only Raststätten, Dunkin'/Coffee Fellows details, SSP as operator (only partial evidence).

## Step 7: Information gain

- C3 (Tripadvisor/Yelp) and several directories still list **Düsseldorf**. The airport itself says Coffee Fellows took over both spots in April 2026 → we're the only page saying so.
- No page lists **all German travel locations (airports + stations + Autobahn) in one place** with **hours pulled from the official locator on a stated date**.
- No page explains the **Starbucks Card / licence-store limitation** at travel locations (S3) or the Rewards/Mobile-Order feature flags.
- Original element: the **station table with a Mobile Order column** and the **5-step travel checklist** (HowTo).

## Step 8: Heading map

| Lvl | Heading | Owns phrase | Question |
|---|---|---|---|
| H1 | Starbucks am Flughafen, Bahnhof und an der Autobahn … | starbucks flughafen | — |
| H2 | 1. An welchen Flughäfen gibt es Starbucks? | starbucks flughafen | which airports |
| H3 | Starbucks am Flughafen Frankfurt | flughafen frankfurt (terminal 1) | — |
| H3 | Starbucks am Flughafen München | flughafen münchen | — |
| H3 | Starbucks am Flughafen BER und in Köln/Bonn | flughafen berlin / köln | — |
| H3 | Starbucks am Flughafen Hamburg und Düsseldorf | flughafen hamburg / düsseldorf | — |
| H2 | 2. Gibt es Starbucks am Bahnhof? | starbucks bahnhof | — |
| H3 | Weitere Bahnhöfe mit Starbucks | bahnhof [city] long tail | — |
| H2 | 3. Gibt es Starbucks an der Autobahn? | starbucks autobahn | — |
| H3 | Weitere Raststätten mit Starbucks | autobahn raststätte / a3 / a5 / a7 | — |
| H2 | 4. Was ist an Starbucks-Reisestandorten anders? | (licence stores) | — |
| H3 | Starbucks Card, Rewards und App | starbucks card flughafen | — |
| H3 | Preise am Flughafen und Bahnhof | preise flughafen | — |
| H2 | 5. Checkliste: Starbucks auf Reisen finden | (HowTo) | do |
| H2 | Häufig gestellte Fragen | 11 Q | — |

Fan-out gaps: "autobahn a1 / a2" → **no Starbucks found on A1/A2** in official sources. Not mentioned in body (no fact to state). Could become an FAQ once verified.

**Internal links:** /blog/starbucks-app, /blog/starbucks-deutschland-filialen, /blog/starbucks-greding, /blog/starbucks-preise, /blog/starbucks-geoeffnet. **Inbound candidates:** starbucks-deutschland-filialen (Flughafen mention in FAQ), starbucks-geoeffnet, starbucks-in-der-naehe, starbucks-near-me, starbucks-preise §5 (Bahnhof/Flughafen prices), starbucks-greding.
**Cannibalisation:** starbucks-preise §5 "Warum sind Preise am Bahnhof und Flughafen höher?" is a subsection, not the same intent. starbucks-greding is one A9 site, and we link to it.

## FAQ source map

DUS (fan-out + info gain), FRA T1 (fan-out "terminal 1"), Stuttgart (fan-out bahnhof stuttgart / airport gap), vor/nach Kontrolle (PAA-style), earliest opening (follow-up), Card (S3), Hamburg Hbf (fan-out), Frankfurt Hbf (fan-out), A7 (fan-out), Raststätten 24/7 (follow-up), Preise (C4/internal).

## Open flags (need user)

1. **Hamburg Airport:** the airport site lists it, Starbucks' own locator shows no data. Worth a quick check in the app.
2. **BER:** we can't tell which locator entry is the airside food-court store (the draft says so openly).
3. **Frankfurt Hbf / München Hbf:** not confirmed either way. The draft only says "haben wir im Store Locator nicht gefunden" for Frankfurt.
4. **/blog/starbucks-preise §5** claims "40 bis 80 Cent mehr" at stations/airports with no source. This draft doesn't repeat the figure.
5. Hours were snapshotted on 1 Oct 2026 (week incl. 3 Oct holiday). Weekday/Sunday columns use 1 Oct (Thu) / 4 Oct (Sun); Köln Friday = 2 Oct.
