# Research notes — "mainz starbucks" (2026-09-17)

## Step 1 — Intent + SERP
- Dominant intent: **visit-in-person / navigational** ("is there a Starbucks in Mainz, where is it, when is it open") — same shape as the site's existing Kassel/Trier/Würzburg location posts.
- SERP is dominated by directory aggregators (Tiendeo, kaufda, meinprospekt, 11880, oeffnungszeitenbuch) plus the official Starbucks store locator and Yelp/Uber Eats listings. No strong editorial competitor — same pattern as other city pages on this site.
- Query fan-out observed: "starbucks mainz öffnungszeiten", "starbucks mainz hauptbahnhof", "starbucks mainz adresse", "starbucks römerpassage" (2011 rumor, see Step 7).

## Step 2 — Head-entity research
- **Starbucks** (Organization) — sameAs https://de.wikipedia.org/wiki/Starbucks
- **Mainz** (Place) — sameAs https://de.wikipedia.org/wiki/Mainz — ~217,000-218,000 Einwohner (Wikipedia, Einwohnerentwicklung von Mainz)
- **Mainz Hauptbahnhof** (Place/TrainStation) — sameAs https://de.wikipedia.org/wiki/Mainz_Hauptbahnhof — busiest station in Rhineland-Palatinate, ~60,000 travelers/day, opened 1884.

## Step 3 — Title/metadata
- Title: "Starbucks Mainz: Filiale am Hauptbahnhof, Öffnungszeiten und Anfahrt · StarbucksPreise"
- Matches site convention (Kassel/Trier use "· StarbucksPreise" suffix, front-loaded keyword).

## Step 4 — Source fetches (competitor/directory layer)
Fetched (WebFetch):
- bahnhof.de/en/mainz-hbf/shopping-and-eating/starbucks — **authoritative** (station operator DB AG): location "2. Etage, Bahnsteig 3/4", hours "Mo–So inkl. Feiertage, 08:00–20:00".
- meinprospekt.de/mainz/filialen/starbucks-de/230046 — address confirmed (Bahnhofsplatz 1, 55116 Mainz), phone (06131) 1431478; **hours field garbled** ("00:00–02:30, 03:30–00:00" — a known scraping artifact on this directory, not usable).
- kaufda.de/Filialen/Mainz/Starbucks-Bahnhofsplatz — same garbled-hours artifact; confirms address/phone only.
- sensor-magazin.de/starbucks-in-mainz/ (May 2011 article) — confirms the Mainz store opened ~2011; the **Römerpassage was a rumored candidate location, not where it actually opened** (editor's note in the article corrects this to the Hauptbahnhof).
- WebFetch to starbucks.de official store-locator page returned **403 Forbidden** — noted plainly, not fabricated; relied on the two independent search-result snippets (starbucks.com store-locator listing + Apple Maps) plus bahnhof.de instead, which corroborate address/name ("Mainz Hauptbahnhof", Bahnhofplatz 1).
- Search confirmed **no second Mainz city-center Starbucks** exists (the 2011 Römerpassage plan never materialized as a separate store); nearest additional stores are ~45km away in **Wiesbaden**: Bahnhofsplatz 3 (Mo–Fr 07:00–20:00, Sa 08:00–20:00, So 10:30–18:00) and Kirchgasse 35–43 (daily ~10:30–18:00), per kaufda/Yelp listings.

## Step 5/6 — Entity ledger (condensed; see entities.json)
Tier 1: Starbucks, Mainz, Mainz Hauptbahnhof, Bahnhofsplatz 1 (address), Öffnungszeiten.
Tier 2: Römerpassage (rumor/disambiguation), Wiesbaden (nearest alternate city), DB/Bahnhof operator, Fairtrade-Espresso.
Tier 3: Frappuccino, Caramel Macchiato, New York Cheesecake (menu items mentioned on bahnhof.de).

Relationships:
- Starbucks Mainz —located on→ 2. Etage / Bahnsteig 3–4, Mainz Hauptbahnhof
- Mainz Hauptbahnhof —operated by→ DB Station&Service (bahnhof.de)
- Starbucks Mainz —opened→ 2011 (per sensor-magazin)
- Römerpassage —was rumored, not actual→ opening location
- Wiesbaden —nearest city with additional Starbucks→ 2 stores, ~45km from Mainz

## Step 7 — Information gain
All directory aggregators repeat the same garbled/conflicting hours and none mention the 2011 Römerpassage rumor. **Original element added:** a short "was 2011 wirklich geplant war" section that resolves the Römerpassage vs. Hauptbahnhof confusion using a primary local-press source, plus a comparison table of the nearest additional stores in Wiesbaden (mirrors the Trier page's "nearest alternatives" table pattern).

## Step 8 — Heading map
1. Wo liegt der Starbucks in Mainz? (know-simple, direct answer)
2. Öffnungszeiten am Hauptbahnhof (table)
3. Was 2011 wirklich geplant war: die Römerpassage-Verwechslung (info-gain)
4. Anfahrt: zu Fuß, mit Bus/Bahn und mit dem Auto
5. Was bietet die Filiale?
6. Lieferung und Mobile Order
7. Weitere Filialen in der Region: Wiesbaden (table)
8. FAQ (12 questions)

## Internal-link plan
- /blog/starbucks-preise (pricing)
- /blog/starbucks-groessen-tall-grande-venti (sizes)
- /blog/starbucks-geoeffnet (general hours rules)
- /blog/starbucks-in-der-naehe (locator hub)
No existing cannibalising page for "mainz starbucks" — clear to publish as new page.

## Fact-check flags for the user
- **Hours**: bahnhof.de (official station operator) says daily 08:00–20:00 incl. holidays; two independent directories return corrupted/implausible hour strings. Used bahnhof.de as authoritative and noted the directory discrepancy inline, matching the Kassel-page convention — recommend a manual spot-check before publishing if precision matters.
- starbucks.de store-locator page returned 403 on direct fetch; address/name corroborated via starbucks.com listing + Apple Maps + bahnhof.de instead.
- No phone-number verification beyond directory listings (06131 1431478) — not fabricated, but not independently confirmed via the official site.
