# Research notes — starbucks köln tasse

## Step 1 — Intent + SERP
- Dominant intent: **buy** (secondary: **know-simple**, motif/specs). Same pattern as the
  published "starbucks tasse münchen" page.
- SERP dominated by Kleinanzeigen.de listings, one dedicated reseller product page
  (thecoffeemugshop.de), and one collector-blog entry (starbucks-mugs.com). No
  article-format competitor produced a full buying guide — same thin-SERP situation as
  München/Hamburg/Berlin tasse pages, so the site's own sibling pages are the structural
  model (per pipeline fallback rule).
- No People-Also-Ask block observed; fan-out queries: "starbucks tasse köln preis",
  "starbucks tasse köln motiv", "starbucks tasse köln gebraucht".

## Step 2 — Head-entity research
- **Kölner Dom** (Cologne Cathedral) — de.wikipedia.org/wiki/Kölner_Dom
- **Hohenzollernbrücke** — de.wikipedia.org/wiki/Hohenzollernbrücke
- **Starbucks** (Organization) — de.wikipedia.org/wiki/Starbucks
- **You Are Here Collection** — no independent Wikipedia/Wikidata entry; recorded as
  unlinked entity (Starbucks product-line naming, not an external reference topic).

## Step 4 — Competitors fetched
1. thecoffeemugshop.de/products/koeln-city-kaffee-tasse-kaufen — full product page: price
   €32.99, 414 ml, 8.5×9.5 cm, 0.5 kg, "You Are Here Series", released April 2017, gift box,
   14-day return, **currently shown sold out**.
2. starbucks-mugs.com/mug/you-are-here-koln/ — collector write-up: motif = Hohenzollern
   Bridge + Cologne Cathedral, "Koln" German spelling used on the mug itself, first
   spotted at US military bases before German retail (confirmed later at Berlin
   Alexanderplatz/Hauptbahnhof), eBay range ≈ €26.50–104.39, one comment flags €35 as
   overpriced.
3. kleinanzeigen.de listings (aggregate, not a single article) — used only to confirm
   active secondary-market presence and rough price floor (~€20–27 for used), not quoted
   as a single source.
4. This site's own published starbucks-tasse-muenchen draft — used as the structural/tone
   model per the fallback rule (no 4th distinct competitor article existed).

## Step 6 — Entity ledger
See entities.json. Tier-1: You Are Here Collection, Kölner Dom, Hohenzollernbrücke,
Starbucks, thecoffeemugshop.de, 414 ml capacity. Tier-2: Been There Series, eBay,
Kleinanzeigen.de, 30-Cent-Rabatt, April 2017 release, Sirenen-Logo.

**Dedupe/parking note:** the live `blog/starbucks-tassen.html` hub already describes a
*different*, apparently newer Köln mug (Kölner Dom, Rhein, Karnevalsmasken, Kölsch-Glas —
Been-There-style framing, no year given). Rather than silently overwrite or contradict that
description, this draft treats it as a **second, distinct edition** and cross-references it
explicitly (see FAQ "Gibt es auch eine neuere Köln-Tasse aus der Been-There-Serie?") so the
two pages don't conflict. This mirrors how the München draft handled the hub's separate
Been-There description for München.

## Step 7 — Information gain
None of the sources combine: (a) the exact motif (Hohenzollernbrücke + Dom, not just
"Cologne landmarks"), (b) the current sold-out status at the main reseller, and (c) the
US-military-base-first release detail. The new-vs-used comparison table assembling all of
this into one buying decision is the original element, consistent with the münchen page.

## Step 8e — Internal-link / cannibalisation plan
- Link **out** to: `/blog/starbucks-tassen` (hub, disambiguates the two Köln editions),
  `/starbucks-tasse.html#rabatt` (reusable-cup discount), and implicitly the authenticity
  guidance already covered on `/blog/starbucks-tasse`.
- **Publish-step action needed (not done by this fork):** update
  `blog/starbucks-tassen.html` line ~374 (the existing Köln bullet: "Dominiert vom
  majestätischen Kölner Dom, dem Rhein, Karnevalsmasken und dem typischen Kölsch-Glas.")
  to add a cross-link to this new page, the same way the München bullet was updated when
  `starbucks-tasse-muenchen` was published. Suggested addition: "Die ältere
  You-Are-Here-Ausgabe von 2017 zeigt stattdessen den Kölner Dom und die
  Hohenzollernbrücke – Maße, Preise und Kaufkanäle in unserem [Guide zur Starbucks Tasse
  Köln](/blog/starbucks-tasse-koeln)."
- No cannibalisation risk found against any live page — this is the first dedicated
  Köln-mug article on the site.

## Fact-sourcing / flags
- Reseller price (€32.99) and sold-out status: thecoffeemugshop.de (single source, live at
  fetch time — verify before publishing in case stock changed).
- Motif and eBay range: starbucks-mugs.com (single collector source, not independently
  cross-checked against a second collector site).
- No official Starbucks-Corporation source confirms current retail availability in Köln
  stores either way — written as "in der Regel nicht mehr zu finden" (hedged), not a firm
  claim.
