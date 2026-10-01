# Coverage / QA: starbucks-flughafen-2026-10-01

- **Words:** 1,786. **Direct answer:** ~50 words (finalize.py counts 43 on the captured line), list-style statement. **FAQ:** 11.
- **Tier-1 coverage:** 8/8 (100%), each with location + hours or a relationship.
- **Tier-2 coverage:** 13/13 (100%).
- **Tier-3 used:** Greding, Holledau, Fläming, A3/A7/A61/A5 Raststätten, Dammtor/Zoo/Erfurt, Preise (9/10). Unused: SSP (operator unconfirmed).
- **Heading architecture:** 1 H1, 5 numbered H2 + FAQ H2, 8 body H3 + 11 FAQ H3, no skipped levels (finalize.py: 0 errors).
- **QUORA check:** every section opens with a direct answer ("Starbucks gibt es 2026 an fünf deutschen Flughäfen…", "Ja, in vielen großen Hauptbahnhöfen…").
- **Question coverage:** fan-out cities covered: Frankfurt (incl. Terminal 1), München, Berlin, Köln, Hamburg, Düsseldorf; Bahnhof Berlin/Bremen/Hamburg/Hannover/Leipzig/Münster/Stuttgart/Frankfurt (FAQ). **Not covered:** Augsburg Bahnhof (no station store found; Augsburg Königsbau is a city store), Autobahn A1/A2 (no official evidence), "richtung münchen" (Holledau covers it implicitly).
- **Fact cross-check:** all hours → S1/S4/S5/S7/S8; licence list → S3; DUS → S6; BER size/seats → S9; airports without Starbucks → S10 (phrased as "nicht gefunden"); Pasing/Siegen/Lörrach → S11 (labelled "laut OpenStreetMap"). Autobahn numbers for Fernthal/Medenbach (A3), Brohltal West (A61), Ellwanger Berge/Holmmoor (A7), Bruchsal (A5) come from general knowledge of the rest-stop locations, not from a Starbucks source. **Please spot-check.** Feuchtwangen was left without an A-number on purpose.
- **Intent check:** yes, it's a lookup page with tables first and explanation second.
- **E-E-A-T:** no first-person claims. Hours are volatile, so the page carries a dated "Recherchestand" line. Refresh it quarterly.

## Flags
1. Spot-check the A-number mapping for the 7 card-FAQ Raststätten.
2. Hamburg Airport store status (locator has no data).
3. Hero image needed (airport/terminal coffee scene, no Starbucks logo).
4. Consider a monthly re-pull of S1 (the script pattern is in this run's notes: curl store page → parse `storeDetails`).
