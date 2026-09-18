# Coverage / QA — starbucks-tasse-hamburg

- **Tier-1 coverage:** 4/4 (Starbucks, Hamburg, You Are Here Series, Hamburger Rathaus) —
  100%, each with a stated attribute (Rathaus = front motif; You Are Here = 2016 release,
  discontinued 2018).
- **Tier-2 coverage:** 7/7 (HafenCity, Been There Series, Global Icon Series,
  thecoffeemugshop.de, Keramik, SKU-Aufkleber, Zweitmarkt) — 100%.
- **Heading architecture:** 1 H1, 8 H2s (incl. FAQ), no H3s, no skipped levels, no two H2s
  target the same query. Heading list read alone conveys the page logic (motif → series/
  currency status → price → where to buy → regional exclusivity → authenticity → specs
  table → FAQ).
- **Answer-block check:** 52 words, doesn't restate the H1, leads with the motif + series +
  the "no confirmed current edition" fact up front (matches the info-gain angle rather than
  a plain snippet format, since no competitor had a snippet to match).
- **Competitor-heading matrix:** starbucks-mugs.com (single collector-blog heading, no
  structured H2s to match) / thecoffeemugshop.de (product page, no internal headings) /
  queenshop.ch (product page, no headings) / one-million-places.com (editorial headings,
  but never mentions Hamburg) — none had a comparable Hamburg-specific heading structure to
  match against, confirming the same information-gap pattern as the Berlin sibling page.
- **Question coverage:** all fan-out questions mapped to a section or FAQ, including the
  "is there a current edition" question none of the four sources answered directly.
- **Fact cross-check:** every price, date, dimension, and motif claim traced to
  `research-notes.md` (thecoffeemugshop.de, starbucks-mugs.com, queenshop.ch,
  one-million-places.com fetches, plus one search-synthesis fact — the Rathaus/HafenCity
  motif — flagged below since it wasn't from a single fetched page).
- **Intent check:** delivers *know-simple* (motif), *know* (is it still current), and *buy*
  (price/where) in the first three sections, matching the mixed intent found in Step 1.
- **Readability:** approx. grade 8-9 (German B2), consistent with the site's existing tone
  and the Berlin sibling page.
- **E-E-A-T / fact-check flags for the user:**
  1. **Motif description (Rathaus front / HafenCity back / dark blue) came from web-search
     synthesis, not a single fetched competitor page** — none of the 4 primary sources
     described the design in that much detail; a collector-directory site
     (starbucks-city-mugs.com) was checked as corroboration but its product page didn't
     render through fetch. Recommend the user visually confirm the motif against a real
     product photo before publishing, or soften the claim if a photo isn't available.
  2. **"No current Been-There Hamburg mug" is an absence claim** — based on not finding one
     across 4 competitor pages + 2 targeted searches, not on an authoritative
     "discontinued" statement from Starbucks. The draft phrases this as "konnte nicht
     bestätigt werden" (could not be confirmed) rather than asserting discontinuation as
     fact — keep that hedge if republishing/updating.
  3. **queenshop.ch's 16 fl oz vs. the other two sources' 14 fl oz (414ml)** is a genuine
     source discrepancy, called out in-body and in the table rather than silently resolved
     — re-verify with the retailer if this becomes a point of customer complaints.
  4. **Zweitmarkt price range is in US dollars** (sourced from an English-facing collector
     blog covering eBay) while the rest of the piece prices in euros/francs — inherent to
     the source, flagged rather than converted (conversion would imply a live FX rate
     the piece doesn't otherwise cite).
  5. Author byline is the generic "Redaktion starbuckspreise.com" placeholder, matching
     every other post on the site.
  6. `schema.jsonld` `datePublished`/`dateModified` left as `TODO:` — fill in on publish.
- **Content-calendar note (not a QA flag, but relevant before publishing):** the calendar's
  URL slug for this row is `/standorte/starbucks-tasse-hamburg`, but the site's real
  Tassen & Merch URL convention is `/blog/starbucks-tasse-hamburg.html` (matching the
  sibling `starbucks-tasse-berlin.html`) — used the real site convention in `schema.jsonld`
  and the internal-link plan, flagging the calendar's placeholder path as likely stale.
