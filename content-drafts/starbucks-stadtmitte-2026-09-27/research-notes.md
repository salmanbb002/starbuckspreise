# Research notes: "starbucks stadtmitte" (27 Sep 2026)

Calendar row: Day 39, vol 90, KD 30, Intent Informational/Navigational, workbook label "Merge-Recommended → starbucks-in-der-naehe". **User asked for a standalone blog post**, so this is written as one. See the cannibalisation note in §8.

## 1. SERP + intent

WebSearch "starbucks stadtmitte" (US-proxy index, 27 Sep):
1. gastroguide.de, Starbucks Königstraße 44, Stuttgart (Stadtmitte): directory, updated 24.02.2023
2. ubereats.com, Starbucks Düsseldorf Hauptbahnhof: delivery listing
3. gastroguide.de, Starbucks Königsbau Passagen EG, Stuttgart: directory
4. gelbeseiten.de, Starbucks Coffee Deutschland GmbH, 40210 Düsseldorf-Stadtmitte: directory (**410 Gone** on fetch)
5. foursquare, Starbucks Gendarmenmarkt, Friedrichstraße 61: login wall on fetch
6. dastelefonbuch.de, Starbucks Düsseldorf-Stadtmitte Schadowstraße (**410 Gone**)
7. stadtbranchenbuch.com, Starbucks Esslingen Stadtmitte, Pliensaustr. 8 (**closed store**, see §6)
8. gocafes.de, Starbucks (Stadtmitte) ("Country error" on fetch)
9. nochoffen.de, Starbucks Coffee House Stadtmitte, Düsseldorf

- **Intent:** visit-in-person (local), secondary know-simple (hours/address). The query is ambiguous across cities: "Stadtmitte" is a Düsseldorf district, a Berlin U-Bahn station and a Stuttgart S-Bahn station.
- **SERP features:** directory/local-pack style, no article competitor, no featured snippet observed. A table answer plus a clear direct answer is the best fit.
- **Fan-out (inferred from the result mix):** starbucks stadtmitte düsseldorf / berlin / stuttgart, öffnungszeiten, königsallee, sonntag geöffnet, esslingen. Autocomplete/PAA were not captured (no rendered SERP), which is a limitation.

## 2. Head entities (non-competitor)

| Entity | Type | sameAs | Key attributes |
|---|---|---|---|
| Starbucks | Organization | https://www.wikidata.org/wiki/Q37158 | Store locator at starbucks.de/de/store-locator |
| Düsseldorf-Stadtmitte | Place | https://en.wikipedia.org/wiki/D%C3%BCsseldorf-Stadtmitte | District in Stadtbezirk 1; Schadowstraße runs Königsallee → Pempelfort (en.wikipedia Schadowstraße) |
| Stadtmitte (Berlin U-Bahn) | Place | https://en.wikipedia.org/wiki/Stadtmitte_(Berlin_U-Bahn) | U2 + U6, Friedrichstraße, Mitte |
| Stuttgart Stadtmitte station | Place | https://en.wikipedia.org/wiki/Stuttgart_Stadtmitte_station | S-Bahn, Theodor-Heuss-Str./Rotebühlplatz, 70173 |
| Starbucks Reserve | Brand | https://en.wikipedia.org/wiki/Starbucks_Reserve | Rare single-origin coffees |
| Königsallee | Place | https://en.wikipedia.org/wiki/K%C3%B6nigsallee_(D%C3%BCsseldorf) | |
| Friedrichstraße | Place | https://en.wikipedia.org/wiki/Friedrichstra%C3%9Fe | |

## 3. Store facts + sources (fact ledger)

| Store | Fact | Source |
|---|---|---|
| Berlin, Friedrichstraße 61, 10117 | Official store-locator entries exist (starbucks.de 53222-282090; starbucks.com store 1018901) | WebSearch site:starbucks.de |
| | Mo–Sa 7:30–20:00, So 9:00–19:00 "according to the official Starbucks website"; WLAN, Mobile Order, mobile pay, stools, WC in basement; near Checkpoint Charlie + U Stadtmitte; tel +49 30 20628799; Quartier 206 | WebSearch snippet (Tripadvisor / starbucks.com / starbucksberlin.de). starbucks.com page fetched empty (JS) |
| Berlin, Friedrichstraße 96 | Different store (IHZ, Bahnhof Friedrichstraße) | kaufda / nochoffen snippets. "~1 km north" is an **estimate**, verify on a map |
| Düsseldorf, Schadowstraße 11, 40212 | Mo–Fr 7–20, Sa 8–20, So 12–18; tel (0211) 136 54 28 | dasoertliche / kaufda / meinprospekt snippets. golocal lists "Schadowstraße 84", a **conflict**; 3 sources say 11 |
| | Friendly staff, WLAN, few seats, pricey | golocal reviews (4.2/5, 17) |
| Düsseldorf, Steinstraße 1-3 (Kö) | Official locator entry (53638-285886; starbucks.com 1020786) | WebSearch |
| | Reserve coffee house, opening announced for summer 2018 | danielfiene.com 08.05.2018, WebSearch summary. **The exact opening date is not verified** |
| Düsseldorf, Königsallee 40 | Permanently closed | Yelp "CLOSED" (Sep 2026), Foursquare "Jetzt geschlossen" |
| Düsseldorf Hbf, Konrad-Adenauer-Platz 14, 40210 | Mo–Fr 6–22, Sa 7–22, So 8–22 | nochoffen.de (fetched). Uber Eats listing exists |
| Stuttgart, Königstraße 44, 70173 | Mo–Sa 7:00–22:00, So 10:00–21:00 (2026 snippet); gastroguide 2023 says 7:30–22 / So 10–22; tel 0711 1204301; WLAN, outdoor seats | WebSearch + gastroguide fetch |
| Stuttgart, Königsbau Passagen | Königstraße 26 per the centre operator (gastroguide says 28); Mo–Do 8–22, Fr 8–23, Sa 8:30–23, So 10–21; tel 0711/22 02 070 | koenigsbau-passagen.de (fetched) |
| | Long queues, WiFi, S-Bahn nearby | gastroguide reviews |
| Stuttgart HB Kiosk | Official locator entry 59910-294154 | WebSearch |
| Esslingen, Pliensaustraße 8 | Closed Feb 2020 (lease ended); Villa Berg café opened March 2020 | Esslinger Zeitung (3 articles), WebSearch summary |

## 4. Competitor extraction (the 4 fetchable pages)

Competitors are directories with no editorial headings, so the extraction is thin.

**C1 gastroguide Königstraße 44.** Headings: Info, Öffnungszeiten, Empfehlungen, Alben.
| term | type | canonical | kind |
|---|---|---|---|
| Königstraße 44 | Place | Königstraße 44 Stuttgart | entity |
| Öffnungszeiten | Concept | Öffnungszeiten | term |
| WLAN | Concept | WLAN | term |
| Terrasse | Concept | Außenplätze | term |
| Shopping-Lage | Concept | Einkaufsstraße | term |
Numbers: 07:30, 22:00, 10:00, 4/5, 3 Bewertungen, 0711 1204301, 2023. Total: 5

**C2 gastroguide Königsbau.** Headings: same template.
| Königsbau Passagen | Place | Königsbau Passagen | entity |
| S-Bahn | Place | S-Bahn Stadtmitte | entity |
| Warteschlange | Concept | Wartezeit | term |
| Kuchen, Muffins | Product | Snacks | term |
Numbers: 4.5/5, 5 Bewertungen, 0711 2202070, 08:00–20:00. Total: 4

**C3 nochoffen Düsseldorf.** Headings: Öffnungszeiten … in Stadtmitte, Adresse, Geschäftszeiten, Haltestellen in der Nähe.
| Konrad-Adenauer-Platz 14 | Place | Düsseldorf Hauptbahnhof | entity |
| Wallstraße 12 (Altstadt) | Place | – | entity (status unknown, parked) |
| Haltestelle | Concept | ÖPNV | term |
Numbers: 6:00, 7:00, 8:00, 22:00. Total: 3

**C4 (substitute) koenigsbau-passagen.de.** Description only: "seit 1971", Arabica, "third place". Total: 3

Substituted or failed: gelbeseiten (410), dastelefonbuch (410), gocafes (error), foursquare (login).

## 5. Entity ledger (tiered). See entities.json

- **Tier 1:** Starbucks; Düsseldorf-Stadtmitte; U-Bahnhof Stadtmitte Berlin; Friedrichstraße 61; Schadowstraße 11; Königstraße 44 Stuttgart; Öffnungszeiten; Store-Locator.
- **Tier 2:** Steinstraße 1-3 / Königsallee; Düsseldorf Hauptbahnhof; Königsbau Passagen; S-Bahn Stadtmitte Stuttgart; Starbucks Reserve; Esslingen closure; WLAN; Sonntag.
- **Tier 3:** Checkpoint Charlie; Quartier 206; Uber Eats; Mobile Order; Stuttgart Hbf Kiosk; Rotebühlplatz; Pei Cobb Freed (unused).

**Relationships:**
- Friedrichstraße 61 —near→ U-Bahnhof Stadtmitte (U2, U6)
- Friedrichstraße 61 —is not→ Friedrichstraße 96 (Bahnhof Friedrichstraße)
- Düsseldorf-Stadtmitte —contains→ Schadowstraße 11, Steinstraße 1-3, Hbf
- Schadowstraße —starts at→ Königsallee
- Steinstraße 1-3 —offers→ Starbucks Reserve (since 2018)
- Königsallee 40 —status→ permanently closed
- Königstraße —hosts→ Königstraße 44 + Königsbau Passagen
- Königsbau Passagen —open until→ 23:00 Fri/Sat
- Esslingen Pliensaustraße 8 —closed→ Feb 2020
- Hbf Düsseldorf —longest hours→ 6:00–22:00
- Store-Locator —is the authoritative source for→ opening hours
- Bahnhof stores —may have→ different prices

**Heading keyword set:** (a) starbucks stadtmitte, starbucks in der stadtmitte, starbucks innenstadt. (b) starbucks stadtmitte berlin, starbucks düsseldorf stadtmitte, starbucks stuttgart königstraße, öffnungszeiten, geschlossen esslingen, kaffee innenstadt preise.

**Dedupe/parked:** Wallstraße 12 Düsseldorf Altstadt (status unknown, not Stadtmitte); Stadtbranchenbuch Esslingen (duplicate of closure); Uber Eats reviews (off-intent).

## 6. Information gain

- Every competitor is a single-store directory entry. **None** puts the cities side by side or explains why "Stadtmitte" is ambiguous.
- Stale data: Esslingen is still listed with hours six years after it closed; Königsallee 40 is still listed on nochoffen; gastroguide hours date from 2023.
- **Original elements:** (1) a cross-city comparison table with sourced hours; (2) a "closed but still listed" section; (3) a 5-step verification HowTo; (4) a Friedrichstraße 61 vs 96 disambiguation.

## 7. Heading + keyword + question map

| Lvl | Heading | Owns | Question | Carries |
|---|---|---|---|---|
| H1 | Starbucks Stadtmitte: Alle Innenstadt-Filialen … | starbucks stadtmitte | Where is Starbucks Stadtmitte? | T1 all |
| H2 | 1. Alle … auf einen Blick | starbucks stadtmitte filialen | Which stores? | table, hours |
| H2 | 2. Warum zeigt die Suche … so viele Städte? | stadtmitte bedeutung | Why several cities? | district/station entities |
| H2 | 3. Starbucks Berlin Stadtmitte | starbucks stadtmitte berlin | Berlin store? | Friedrichstr 61, U2/U6 |
| H2 | 4. Düsseldorf-Stadtmitte | starbucks düsseldorf stadtmitte | Düsseldorf stores? | 3 stores |
| H3 | Schadowstraße 11 / Steinstraße 1-3 / Hbf | street variants | | Reserve, hours |
| H2 | 5. Stuttgart-Mitte | starbucks stuttgart königstraße | Stuttgart stores? | 2 stores + kiosk |
| H3 | Königstraße 44 / Königsbau Passagen | | | |
| H2 | 6. Geschlossen, aber noch gelistet | starbucks esslingen geschlossen | Is it still open? | closures |
| H2 | 7. So prüfst du … | öffnungszeiten prüfen | How do I check? | HowTo |
| H2 | 8. Kostet Kaffee in der Innenstadt mehr? | preise innenstadt | Is it pricier? | Bahnhof pricing |
| H2 | Häufig gestellte Fragen | | | 11 Qs |

## 8. Internal links + cannibalisation

- **Cannibalisation:** `blog/starbucks-in-der-naehe` was the workbook's merge target, but it has 0 mentions of "Stadtmitte" and is generic (app/maps/drive-thru). A multi-city Stadtmitte page is a distinct local angle, so the risk is low. **Add a link from in-der-naehe §7 and deutschland-filialen §6 to this page.** There is no existing Berlin, Düsseldorf or Stuttgart city page, so this post is also the first content for those cities.
- Out-links used: /blog/starbucks-deutschland-filialen, /blog/starbucks-in-der-naehe, /blog/starbucks-geoeffnet, /blog/starbucks-preise, /blog/starbucks-becher.
- Future articles: standalone city guides "Starbucks Düsseldorf", "Starbucks Stuttgart", "Starbucks Berlin Mitte" should link back here.

## 9. FAQ source map

All 11 FAQ answers use only §3 facts. The questions are derived from the result mix and the store facts (Reserve, Esslingen, Königsallee, Sunday, WLAN, Mobile Order, Friedrichstr 96). No PAA box was captured.
