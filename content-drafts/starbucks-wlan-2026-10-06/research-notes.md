# Research notes – starbucks wlan (run 2026-10-06, calendar slot 2026-10-28)

## Intent / SERP (WebSearch, US-proxied, German queries, 6 Oct 2026)
- ~30/mo (Trends estimate ±50 %), flagged seasonal. Intent: know-simple ("hat Starbucks WLAN", "gratis") + do ("anmelden", "name", "passwort").
- Calendar type "FAQ / short answer post"; written to the network standard (1.500+ words).
- Organic is old: teltarif.de (2010), connect-professional (2010), helpster.de, macuser.de thread (2011), webwork-magazin (410 Gone), tripadvisor review, thefastcode (machine-translated US how-to). No current German page answers the query with data.
- No rendered SERP (Chrome extension not connected) → PAA not captured. Fan-out from Autocomplete_Oct2026: hat starbucks wlan, gratis wlan, wlan anmelden, wlan name, wlan passwort.

## Head entities (Step 2)
- WLAN-Hotspot (de.wikipedia "Hot Spot (WLAN)"), Captive Portal, Starbucks (Wikidata Q37158), Store Locator starbucks.de.

## Competitors (Step 4)
| # | URL | Result |
|---|---|---|
| C1 | teltarif.de/starbucks-wlan…/news/39822.html (23 Aug 2010) | fetched – BT Openzone, ~140 German stores, up to 2 h free; before: T-Mobile since 2003, 7,95 €/h or 24,95 €/24 h |
| C2 | macuser.de thread 570930 (30 Jan 2011) | fetched – login window on iPhone/iPad, "Codes sind nicht mehr nötig", 2 h free in Hamburg |
| C3 | helpster.de "Im Starbucks das WLAN kostenlos nutzen" | 403 – only search snippet (ask staff for login; first use asks name, e-mail, postcode) – not used as a fact |
| C4 | thefastcode.com/de-eur "So verbinden Sie sich mit Starbucks Wi-Fi" | 403 – US-centred, not used |
| – | coffeenearyou.com guide (2026) | search snippet only – US "Google Starbucks" SSID and 60-minute limit; NOT applied to Germany |

## Fact ledger
| Fact | Source |
|---|---|
| Store features for DE: WF "Drahtloser Hotspot", DR "Reward einlösen", XO "Mobiles Bestellen und Bezahlen", DT "Drive-Through"; shown under "Annehmlichkeiten" | starbucks.de/api/v2/storeFeatures + page translations (6 Oct 2026) |
| 170 DE stores collected, 150 with WF (88 %), 20 without; 17 of those 20 have no features at all | starbucks.de/api/v2/stores (coordinate sweep, 6 Oct 2026) → store-locator-wlan-2026-10-06.csv + raw JSON in this folder |
| No-WF by type: 9 Autobahn/Autohof, 7 Bahnhof, 2 Flughafen, 2 other (Hamburg Phoenix-Center, Magdeburg) | same (type derived from store name – FLAG derived) |
| WF present at Hbf Berlin, Köln, Düsseldorf, Hannover, Leipzig, Nürnberg and at airport stores FRA / MUC / BER | same |
| City counts: Berlin 19/17, München 14/14, Frankfurt 13/12, Hamburg 12/8, Köln 7/7, Düsseldorf 6/6, Stuttgart 5/4, Leipzig 5/5 | same |
| starbucks.de FAQ / store locator pages publish no SSID, password or time limit | starbucks.de/de/faq, /de/store-locator (raw page data, 6 Oct 2026) |
| WIFI@DB: ~600 stations, no registration, unlimited use, accept AGB | bahnhof.de/service/wlan |
| BSI tips: WLAN only when needed; no confidential data on foreign WLAN, else VPN; disable file sharing; disable auto-connect | bsi.bund.de "Sicherheitstipps für privates und öffentliches WLAN" (page text + search summary for the last two) |
| Troubleshooting steps (captive portal, VPN, private DNS, forget network) | general networking practice – no single source, FLAG editorial |

## Sweep caveat
The API only returns stores near a coordinate. Grid sweep + re-query around every found store + named cities; starbucks.de started returning 429 before the last gap-filling pass finished, so the list may miss isolated stores. The article says so. Kassel Königsplatz (own page /blog/starbucks-kassel) returned 0 results at its coordinates while the API was throttling – unresolved, re-check before trusting either way.

## Tiers / relationships
T1: Starbucks WLAN, kostenlos, Anmeldung, Store Locator / Drahtloser Hotspot, Filiale. T2: Passwort, Netzname, Zeitlimit, Anmeldeseite, Bahnhof, VPN, Sicherheit, BT Openzone / T-Mobile. T3: WIFI@DB, BSI, Steckdosen, Drive-Thru, Flughafen.
- Starbucks —bietet→ WLAN (150 von 170 Filialen) · Filiale —führt→ „Drahtloser Hotspot“ · WLAN —kostenlos seit→ August 2010 (BT) · Bahnhof-Kiosk —ohne Eintrag→ WIFI@DB als Alternative.

## Information gain
No competitor has current data. Original: (1) count of German stores with the hotspot amenity from the official locator, by city; (2) which store types lack it; (3) dated provider/price history table; (4) honest "not published" on SSID / limit instead of copied US values.

## Own-site corrections made in this run
/blog/starbucks-in-der-naehe claimed "alle Standardfilialen" have WLAN "ohne … zeitliche Beschränkung" (unsourced) → replaced with the locator share + link (visible FAQ and FAQPage schema kept identical).

## Internal links / cannibalisation
Out: in-der-naehe, preise, app, flughafen, drive-in, deutschland-filialen, geoeffnet. In: in-der-naehe, stadtmitte, braunschweig, heilbronn, giessen, kassel, siegen, loerrach. Cannibalisation: none.

## FAQ source map
Hat Starbucks WLAN / gratis / Passwort / Name (autocomplete) · Zeitlimit (C1/C2) · Anmeldeseite öffnet nicht (C2) · Bahnhof / Flughafen (locator data) · Online-Banking (BSI) · App nötig (gap) · Steckdosen (own essen/in-der-naehe pages) · Drive-Thru (gap).
