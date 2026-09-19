# Coverage QA — starbucks zweibrücken

- **Entity coverage**: Tier-1 4/4 (100%), each with a stated attribute (address, hours, outlet context, opening date). Tier-2 3/3 (100%). Tier-3: Rheinland-Pfalz used once naturally, not forced further.
- **Heading architecture**: 1 H1, no skipped levels (H2s + one H3 under "Wo liegt..."), each H2 owns a distinct sub-topic, FAQ last. Reads as a coherent location/hours page.
- **Answer-block check**: Direct-answer block (address + hours + opening date) — slightly over the 40-55 word target (~55 words as written, acceptable given 3 discrete facts required).
- **Competitor-heading matrix**: address (official outlet site ✓), hours (official + directory, conflicting — both cited ✓), opening date (rheinpfalz ✓), product offering (official site ✓), phone (official + directory ✓).
- **Question coverage**: all researched facts mapped to a body section or FAQ; no PAA expansion was available for this low-volume local query (no meaningful "People Also Ask" block surfaced).
- **Fact cross-check**: every number/date in the draft traces to research-notes.md (address, phone, hours ×2 sources, opening date). No invented figures.
- **Intent check**: delivers on visit-in-person intent — address, hours, how to get there context (outlet vs. city center) all present.
- **Readability**: short sentences, concrete facts, roughly grade 7-8 German.
- **E-E-A-T flags**:
  1. `schema.jsonld` datePublished/dateModified left as `TODO:` — set at actual publish time.
  2. Hours discrepancy (official site 10:00-19:00 vs. directory 09:30-19:30) is disclosed, not resolved — recommend a quick manual check against the Starbucks app/store locator before publishing if precision matters.
  3. No first-person "lived experience" claims were fabricated; all claims are sourced to the 3 competitor/directory pages + site's own store dataset.
