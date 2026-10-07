# Research notes – starbucks outlet (2026-10-07)

## 1. Keyword, intent, SERP
- Primary: **starbucks outlet** · ~40/mo (Research_Oct2026). Sheet decision was "Merge into deutschland-filialen (Outlet-Center list)"; that page had no outlet mention. Owner asked for a standalone post.
- Intent: visit-in-person + know. Ambiguity: "outlet" as factory outlet vs. store inside an outlet centre → both answered in §1.
- SERP (WebSearch, US-proxied): centre press release (Halle Leipzig), mcarthurglen.com (Neumünster), trade press on Starbucks expansion, outlet round-ups. No page lists all outlet-centre branches. PAA not captured.
- Fan-out (Autocomplete_Oct2026): outlet ingolstadt starbucks; starbucks halle leipzig outlet; outlet berlin / bremen / landquart / metzingen / montabaur / neumünster / soltau / wolfsburg / zweibrücken; plus unmapped: starbucks ingolstadt village, metzingen, ochtrup, wolfsburg, westpark ingolstadt starbucks.

## 2. Head entities
| Entity | Type | sameAs |
|---|---|---|
| Factory-Outlet-Center | Concept | de.wikipedia.org/wiki/Factory-Outlet-Center |
| Starbucks (DE, AmRest) | Organization | wikidata Q37158 |
| Outletcity Metzingen | Place | de.wikipedia.org/wiki/Outletcity_Metzingen |

## 3. Primary data: starbucks.de/api/v2/stores (7 Oct 2026)
24 coordinate queries, 1 thread, 2,5 s apart, no 429. Raw result: `store-locator-outlet-2026-10-07.json`.
| Centre | Store name in locator | Address | Mo–Fr | Sa | Features |
|---|---|---|---|---|---|
| Outletcity Metzingen | Metzingen Outlet City | Hugo Boss Platz 6, 72555 | 9–20 (Fr –20:30) | 8–20:30 | WF DR XO |
| Montabaur The Style Outlets | Montabaur Fashion Outlet | Am Fashion Outlet 72, 56410 | 8:30–20 | 9–20 | WF DR XO |
| Designer Outlet Neumünster | Neumuenster, FOC Hamburg | Oderstrasse 11, 24539 | 9:30–20 | 9:30–20 | DR WF XO |
| Halle Leipzig The Style Outlets | Halle Leipzig The Style Outlet | Berliner Strasse 1, 06796 Sandersdorf-Brehna | 10–20 | 10–20 | WF DR XO |
| Ochtum Park | Stuhr, FOC Ochtum Park | Bremer Str 107, 28816 Stuhr | 9–19 | 9–18:30 | WF DR XO |
| designer outlets Wolfsburg | Wolfsburg FOC | An der Vorburg, 38440 | 9–19 (Fr –20) | 9–20 | DR WF XO |
| Zweibrücken Fashion Outlet | Zweibruecken, Londoner Bogen 1 | Londoner Bogen 10 90, 66482 | 10–19 | 10–19 | WF DR XO |
| Designer Outlet Soltau | Soltau FOC | Factory Outlet Center, 29614 | 10–20 | 10–20 | DR WF XO |
| Designer Outlet Berlin | Berlin, Designer Outlet | Alter Spandauer Weg 1, 14641 Wustermark | 9:30–20 | 9:30–20 | WF DR XO |
| Designer Outlet Ochtrup | Designer Outlet Ochtrup | Laurenzstrasse 51 55, 48607 | 9:30–20 | 9:30–20 | WF DR XO |
All ten closed on Sunday 11 Oct 2026. None has DT.
- No store returned for: Ingolstadt Village (2 queries), Ingolstadt Westpark, Ingolstadt centre, Wertheim Village (2), Bad Münstereifel (2), Roppenheim (FR), Geislingen, Radolfzell, Selb.
- Abroad: Roermond (NL) 3 stores "Outlet SC Zuid / Oost / Noord", Stadsweide, daily 10–18 / 10–21 / 10–18; Landquart Fashion Outlet (CH), Tardisstrasse 20a, Mo–Sa 8–20, So 8:30–20.
- Bremen (not outlets): Marktstrasse 3, Main Station, Waterfront Kiosk, Waterfront C02.

## 4. Other sources
| # | Source | Facts used |
|---|---|---|
| S2 | Pressemitteilung "Starbucks eröffnet im Halle Leipzig The Style Outlets" (26 Sep 2024, prezly PDF) | opening 1 Oct 2024; happy hour 1–8 Oct, 2 Grande Frappuccino for 1; ~70 stores, 1.800 free parking spaces; AmRest "über 140 Coffee Houses in mehr als 40 Städten" |
| S3 | outletcity.com/de/metzingen/gastronomie | Starbucks listed: "Kaffeehaus und amerikanische Bäckerei", Sonnenterrasse |
| S4 | mcarthurglen.com/…/designer-outlet-neumuenster/offers/nov-starbucks | Starbucks listed at the centre (Oderstraße 10) |
| S5 | thebicestercollection.com/ingolstadt-village/de/gastronomie · /wertheim-village/de/gastronomie (headless Chrome) | no Starbucks in either directory; Wertheim lists "The Coffee Corner" |
| S6 | /blog/starbucks-zweibruecken (own) | opened 31 Oct 2019 |
| S7 | /blog/starbucks-gutschein (own, from Starbucks AGB) | German Starbucks Card valid in Germany only; DR filter = Card accepted |

## 5. Competitors
No editorial competitor covers the topic; the four pages used as the competitor set are the centre pages S2–S5 (one heading each: restaurant entry / press release). Extraction (shuffled): Coffee House, Kaffeehaus, Bäckerei, Sonnenterrasse, Outlet-Stores, Parkplätze, Eröffnung, Happy Hour, Frappuccino, AmRest, Gastronomie.

## 6. Entity ledger → entities.json
T1: Starbucks Outlet, Outlet-Center, Starbucks Deutschland, Öffnungszeiten, Outletcity Metzingen. T2: the other nine centres, Ingolstadt Village, Wertheim Village, Store Locator, AmRest, Starbucks Rewards, WLAN. T3: Roermond, Landquart, Bad Münstereifel.
Relations: 10 centres —have→ Starbucks · all 10 —closed→ Sunday · all 10 —offer→ WF + DR + XO · Halle Leipzig —opened→ 1 Oct 2024 · Zweibrücken —opened→ 31 Oct 2019 · Ingolstadt/Wertheim Village —have no→ Starbucks · Starbucks DE —runs no→ factory outlet.

## 7. Information gain
The full list from first-party data, the negative list, the hours table and the map (hero).

## 8. Internal links
zweibruecken, deutschland-filialen, geoeffnet, in-der-naehe, app, wlan, angebote, preise, gutschein, drive-in, becher-aktuell. Inbound added from deutschland-filialen + zweibruecken. Cannibalisation: /blog/starbucks-zweibruecken stays the detail page for that one store.
