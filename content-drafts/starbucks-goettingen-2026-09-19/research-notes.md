# Research notes — starbucks göttingen

## Step 1 — Intent + SERP
Query: "starbucks göttingen gibt es" / "Starbucks Göttingen Filiale 2026" / "Starbucks Göttingen Adresse Öffnungszeiten Store Locator" (WebSearch, no live-browser SERP available this run).
- No article-format organic competitors exist for this exact query — results are Kleinanzeigen listings (used mugs/merch), a directory stub (handelsangebote.de, formerly marktjagd.de) that returns **unrelated Rewe-Nürnberg results** under a "STARBUCKS® Filialen Göttingen" header, aktionspreis.de (packaged-coffee retail offers), and Espresso House's own Göttingen Hauptbahnhof page.
- Intent: mixed *know-simple* ("is there one") + *visit-in-person* (local). Same shape as the site's existing Bamberg/Trier/Würzburg/Chemnitz/Oldenburg pages.
- No featured snippet, no PAA block, no knowledge panel observed in the synthesized results — thin/local SERP, consistent with the sibling "no-store" city pages already on this site.

## Step 2 — Head-entity research
- **Göttingen**: Lower Saxony university city, 127,259 inhabitants (end of 2024, Statista/Wikipedia), home to Georg-August-Universität Göttingen (oldest/largest university in Lower Saxony; students >20% of population). sameAs: https://de.wikipedia.org/wiki/G%C3%B6ttingen
- **Starbucks**: sameAs https://de.wikipedia.org/wiki/Starbucks

## Step 3/4 — Competitor fetch
No substantive competitor articles exist (confirmed via 2 distinct search queries + 1 directory-page fetch that returned junk data). Per pipeline fallback rule: structural model = this site's own live sibling pages (starbucks-trier.html, starbucks-bamberg.html), not an external competitor. Logged plainly rather than fabricating a 4-competitor extraction table.

## Step 5/6 — Entity ledger (condensed; thin-SERP fallback)
| canonical | type | kind | tier | note |
|---|---|---|---|---|
| Göttingen | Place | entity | 1 | head entity |
| Starbucks | Organization | entity | 1 | head entity |
| Georg-August-Universität Göttingen | Organization | entity | 2 | explains demand/no-store contrast |
| Espresso House (Göttingen Hauptbahnhof) | Organization | entity | 2 | nearest in-city alternative |
| Kassel (Königsplatz 59) | Place | entity | 2 | nearest confirmed Starbucks, ~40 km |
| Store Locator (starbucks.de) | Thing | term | 3 | how to check for a future opening |

Relationships: `Göttingen —has no confirmed→ Starbucks branch`; `Espresso House —operates at→ Göttingen Hauptbahnhof, Bahnhofsplatz 1`; `Kassel branch —nearest confirmed store, ~40 km from→ Göttingen`; `Georg-August-Universität —drives→ large student population (>20%)`.

Dedupe/parking: dropped "Starbucks Coffee 220ml Becher" retail-offer entities (aktionspreis.de) — packaged-product retail, not a café location, out of scope for the "is there a branch" query but used once generically in the FAQ (no specific supermarket named, since the search-engine-synthesized retailer list for Göttingen — Aldi Nord/Wasgau/Handelshof/CC Großmarkt — could not be independently verified per-store and Wasgau is a southwest-Germany chain unlikely to operate in Lower Saxony; used the same unverified-but-safe generic phrasing the sibling pages already use instead).

## Step 7 — Information gain
None of the thin results address: (a) the actual distance/route to the nearest real store, (b) a named in-city alternative with address, (c) the size/university-city contrast that makes the absence notable. Info-gain element: a distance table (Kassel vs. general "no branch" framing) **plus** an explicit population/student-body contrast against Kassel (which does have a branch despite being only moderately larger) — this specific comparison appears nowhere in the search results.

## Step 8 — Heading map
1. H1 — Starbucks Göttingen: Gibt es eine Filiale in der Stadt? (direct-answer block)
2. H2 Gibt es einen Starbucks in Göttingen? — tier 1 Göttingen/Starbucks
3. H2 Wo liegt der nächstgelegene Starbucks? — tier 2 Kassel
4. H2 Warum hat die Universitätsstadt Göttingen noch keinen Starbucks? — tier 2 Universität
5. H2 Welche Alternative gibt es direkt in Göttingen? — tier 2 Espresso House
6. H2 Kann ich trotzdem Starbucks-Produkte kaufen?
7. H2 Eine Neueröffnung im Blick behalten
8. H2 FAQ (10 Q)

## Step 8e — Internal links / cannibalisation
- Outbound: /blog/starbucks-kassel (nearest store + already claims "kein Coffee House" for Göttingen — verified still accurate, cross-linked back), /blog/starbucks-geoeffnet, /blog/starbucks-in-der-naehe, and the other no-store siblings (trier/würzburg/chemnitz/oldenburg/bamberg).
- No cannibalisation risk: no existing page on this site targets "starbucks göttingen".
- Recommend adding a reciprocal link from blog/starbucks-kassel.html's existing "Göttingen oder Marburg" mention to this new page once published.

## Step 12 — QA flags
- No specific Göttingen supermarket names used in the "packaged products" FAQ answer — search-engine synthesis produced an inconsistent/likely-unreliable retailer list (included Wasgau, a southwest-German chain), so the answer stays generic per the sibling-page pattern. Flag for manual verification if the user wants named retailers.
- Kassel distance (~40 km) is a great-circle (haversine) estimate from published coordinates, not a routed driving distance — same caveat as the Bamberg draft.
- Espresso House address/hours sourced directly from the chain's own website (de.espressohouse.com) — single-source but primary/official, low risk.
- Population figure (127,259, end of 2024) sourced from Statista/Wikipedia synthesis — one source, not cross-verified against a second.
