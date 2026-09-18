# Research notes — "starbucks oldenburg"

Date researched: 2026-09-18. Language: de-DE. Page type: City/Location blog post (Content_Calendar keyword "starbucks oldenburg", SV 170 / KD 29, Priority Low). Angle: **no confirmed branch in the city** — same structural pattern as the existing starbucks-trier.html page, not the "has a branch" pattern used for Siegen/Braunschweig/etc.

## Step 1 — Intent + SERP

Dominant intent: **visit-in-person / navigational**, with a strong secondary **know-simple** ("gibt es überhaupt einen Starbucks in Oldenburg") since the honest answer is no. SERP is dominated by directory aggregators (11880.com, meinprospekt.de, Cylex Filialfinder, Yelp) that return generic "Starbucks near you" results rather than a confirmed Oldenburg address — a sign no real branch exists. No featured snippet, no PAA box surfaced. Two international name collisions pollute results: **Oldenburg, Indiana** (a real small town near Batesville, IN, USA) and unrelated Yelp categories.

Query fan-out: "starbucks oldenburg öffnungszeiten", "starbucks oldenburg schlosshöfe", "nächster starbucks oldenburg", "starbucks oldenburg lieferservice".

## Step 2 — Head-entity research

- **Starbucks** — Organization. `sameAs`: https://de.wikipedia.org/wiki/Starbucks.
- **Oldenburg (Oldb)** — Place (Niedersachsen). `sameAs`: https://de.wikipedia.org/wiki/Oldenburg_(Oldb). Einwohner: 176.530 (Stand 31.12.2025, Stadt Oldenburg, +462 ggü. Vorjahr).
- **Carl von Ossietzky Universität Oldenburg** — Organization. `sameAs`: https://de.wikipedia.org/wiki/Carl_von_Ossietzky_Universit%C3%A4t_Oldenburg. 14.770 Studierende im Wintersemester 2025/26 (offizielle Zahlen-&-Fakten-Seite der Uni); stadtweit rund 18.000 Studierende an insgesamt fünf Hochschulen (~10 % der Bevölkerung).

## Step 3 — Title/metadata

- Title: "Starbucks Oldenburg: Gibt es eine Filiale? Standorte & Alternativen" (67 chars)
- H1: "Starbucks Oldenburg: Gibt es eine Filiale? Standorte und Alternativen"
- Meta description: "Starbucks in Oldenburg: Aktuell gibt es in der Stadt kein eigenes Coffee House. Die nächsten Filialen liegen in Bremen — plus gute Alternativen vor Ort." (153 chars)
- Slug: starbucks-oldenburg (site convention: `/blog/starbucks-oldenburg`; the calendar's `/standorte/...` path is a placeholder, not the live URL pattern)

## Step 4 — Competitor fetch / sources (4 distinct domains + official-adjacent)

| id | URL | Notes |
|---|---|---|
| meinprospekt | https://www.meinprospekt.de/filialen/starbucks-de | Full German branch directory by postal-code region — **no Oldenburg entry appears**, confirming no listed branch. |
| kaufda-bremen | https://www.kaufda.de/Filialen/Bremen/Starbucks/v-r494 | Lists all 5 Bremen branches with exact addresses: Marktstraße 3 (28195), Bahnhofsplatz 15 (28195), AG-Weser-Straße 1 "Waterfront C02" (28237), AG-Weser-Straße 3 "Waterfront Kiosk" (28237), Hans-Bredow-Straße 19 "Weserpark" (28307). |
| tripadvisor | https://www.tripadvisor.com/Restaurants-g187353-c8-Oldenburg_Lower_Saxony.html | Top-rated Oldenburg cafés — Käthe Kaffee (4.7★, 26 Bewertungen), Café Cantuccini (4.9★), Koffie Kliek (4.7★) — all independent, none a Starbucks. |
| grubhub-us | https://www.grubhub.com/food/starbucks/in-oldenburg | US delivery-app result for "Oldenburg, IN" (Indiana) — direct evidence of the international name collision polluting search results. |
| 11880 | https://www.11880.com/suche/starbucks/oldenburg | **Fetch failed (HTTP 403)** — substituted meinprospekt.de (already a distinct domain in this table) as the next-ranking directory source rather than fabricating its content. |

**Fetch note:** 11880.com blocked the fetch (403); not retried with fabricated data, meinprospekt.de covers the same "no listed branch" claim independently.

## Step 5/6 — Entity ledger (consolidated, tiered)

| canonical | type | tier | competitor_count | in_title_or_h2 | relationship |
|---|---|---|---|---|---|
| Starbucks | Organization | 1 | 5 | yes | Betreibt aktuell kein eigenständiges Coffee House in Oldenburg. |
| Oldenburg (Oldb) | Place | 1 | 5 | yes | Stadt in Niedersachsen mit 176.530 Einwohnern (Stand 31.12.2025). |
| Bremen (Marktstraße 3 / Bahnhofsplatz 15) | Place (store address) | 1 | 2 | yes | Nächstgelegene Filialen, rund 50 km bzw. 40–45 Fahrminuten von Oldenburg entfernt. |
| Carl von Ossietzky Universität Oldenburg | Organization | 2 | 1 | no | 14.770 Studierende im WiSe 2025/26, rund 18.000 Studierende stadtweit an fünf Hochschulen. |
| Käthe Kaffee | Organization (café) | 2 | 1 | no | Unabhängige Rösterei/Café, Kaiserstraße 28, 4,7★ (26 Bewertungen) — meistgenannte lokale Alternative. |
| Oldenburg, Indiana (USA) | Place | 2 | 2 | no | Kleinstadt bei Batesville, Indiana, USA — Namensverwechslung, da US-Lieferdienste unter "Oldenburg" Treffer für die Starbucks-Filiale in Batesville liefern. |
| Schlosshöfe Oldenburg | Place (mall) | 3 | 1 | no | Einkaufszentrum in der Innenstadt (12.500 m², eröffnet 2011) — kein Starbucks unter den Mietern gelistet. |
| Weserpark / Waterfront (Bremen) | Place | 3 | 2 | no | Zwei weitere Bremer Filialen, rund 10 km von der Bremer Innenstadt, aber weiter von Oldenburg entfernt als Marktstraße/Bahnhofsplatz. |

**Dedupe log:** "Starbucks Bremen" (mehrere Adressen bei kaufda) zu einem Bremen-Cluster zusammengeführt, aber die zwei nächstgelegenen (Marktstraße 3, Bahnhofsplatz 15) separat als Tier-1-Fakt behandelt, da sie die tatsächliche Antwort auf "wo ist der nächste Starbucks" sind. Kein Tier-1/2-Begriff verworfen.

## Step 7 — Information-gain pass

None of the directory aggregators state plainly that Oldenburg has **no** branch — they just return empty/generic "near you" results, which reads as inconclusive rather than a clear answer. **Committed information-gain elements:**
1. An explicit, sourced "no" (cross-checked against the full German branch directory) instead of a vague empty result, plus a real distance/address table for the two nearest Bremen branches — no aggregator gives exact addresses + driving distance together.
2. The **Oldenburg, Indiana** disambiguation — none of the German-market competitors address why US delivery-app results for "Starbucks Oldenburg" surface at all; mirrors the site's existing Trier (Saarbrücken/Weil am Rhein) and Siegen (Baton Rouge) disambiguation pattern, but for a genuinely different collision.
3. A genuine, rated local alternative (Käthe Kaffee, 4.7★) instead of a generic "try a local café" line.

## Step 8 — Heading map

| # | Level | Heading | Phrase owned | Question answered | Tier-1/2 carried |
|---|---|---|---|---|---|
| — | H1 | Starbucks Oldenburg: Gibt es eine Filiale? Standorte und Alternativen | focus keyword | Is there a Starbucks in Oldenburg | Starbucks, Oldenburg |
| 1 | H2 | Gibt es einen Starbucks in Oldenburg? | starbucks oldenburg | core answer | Starbucks, Oldenburg |
| — | H3 | Warum taucht bei der Suche manchmal ein Ergebnis aus den USA auf? | oldenburg indiana | disambiguation | Oldenburg, Indiana (USA) |
| 2 | H2 | Wo liegen die nächstgelegenen Filialen? | nächster starbucks oldenburg | nearest branch | Bremen (Marktstraße 3 / Bahnhofsplatz 15), Weserpark/Waterfront |
| 3 | H2 | Warum hat eine Stadt wie Oldenburg trotz rund 176.500 Einwohnern noch keinen Starbucks? | starbucks oldenburg öffnungszeiten (negation) | why no branch | Oldenburg (population), Universität Oldenburg |
| 4 | H2 | Gute Alternativen direkt in Oldenburg | starbucks oldenburg schlosshöfe | alternatives | Käthe Kaffee, Schlosshöfe |
| 5 | H2 | So behalten Sie eine mögliche Neueröffnung im Blick | starbucks oldenburg lieferservice (folded in) | monitoring / delivery | Starbucks |
| — | H2 | FAQ | — | — | all tier-1/2 recap |

## Step 8e — Internal links / cannibalisation

- Link to `/blog/starbucks-geoeffnet` (allgemeine Öffnungszeiten-Regeln) and `/blog/starbucks-in-der-naehe` (Standort-Übersicht) from the closing section — matches the Trier/Kassel pattern.
- **Cannibalisation check:** no existing page on starbuckspreise.com targets "starbucks oldenburg" — confirmed via `ls` on the live `blog/` folder before starting research. No merge needed.

## FAQ source map

Sourced from: the "no listed branch" fact (meinprospekt full directory), the kaufda Bremen branch table, the Tripadvisor café ranking, the Grubhub Oldenburg-Indiana collision, and genuine fan-out questions (delivery, Schlosshöfe, reopening watch). No competitor publishes a usable FAQ block for this query — all 11 questions are fan-out/aggregator-gap-derived, each traceable to a row in the entity ledger above.
