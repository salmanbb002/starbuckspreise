# QA / Coverage — starbucks-mainz (2026-09-17)

- **Tier-1 coverage:** 5/5 (100%) — Starbucks, Mainz, Mainz Hauptbahnhof, Bahnhofsplatz 1, Öffnungszeiten all stated with an attribute/relationship (address, hours, 2nd-floor location, operator source), not just named.
- **Tier-2 coverage:** 5/5 (100%) — Römerpassage, Wiesbaden, DB Station&Service, Fairtrade-Espresso, Mobile Order & Pay all covered.
- **Heading architecture:** one H1, valid H2→H3 nesting (one H3 under section 1), no skipped levels, each H2 owns a distinct phrase, order follows the spine (what → hours → info-gain history → how-to-get-there → offer → delivery → alternatives → FAQ).
- **Answer-block check:** direct-answer block is 46 words, doesn't restate the H1, states location + hours + no-second-store fact.
- **Question coverage:** "mainz hauptbahnhof", "öffnungszeiten", "adresse", "römerpassage" all mapped to a section; no PAA left unanswered based on the fan-out captured in Step 1.
- **Fact cross-check:** every number/date traced to research-notes.md (bahnhof.de for hours, sensor-magazin.de for the 2011/Römerpassage history, Wikipedia for population/station stats, kaufda/Yelp for Wiesbaden hours). No invented figures.
- **Intent check:** delivers what "mainz starbucks" searchers want — confirms existence, gives exact location + hours, resolves a real historical confusion (Römerpassage), and gives a fallback (Wiesbaden) if the traveler wants alternatives.
- **Readability:** approx. grade 8-9 German (Kassel/Trier-page register), short paragraphs, no jargon.
- **E-E-A-T flags for the user:**
  - No named human author/byline (site convention: "StarbucksPreise Redaktion" org author, same as all other location posts — not a new gap).
  - Opening-hours discrepancy across directories is disclosed in-body rather than silently resolved — recommend a manual phone/on-site check if hour-accuracy is business-critical.
  - Phone number (06131 1431478) sourced from directories only, not independently verified against the official Starbucks site (starbucks.de fetch returned 403).
