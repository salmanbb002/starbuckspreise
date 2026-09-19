# Coverage scorecard — starbucks göttingen

- **Entity coverage**: Tier 1: 2/2 covered with attributes (Göttingen: population + university-city status; Starbucks: confirmed absent + nearest branch). Tier 2: 3/3 covered with attributes (Universität: student share; Espresso House: address + hours; Kassel branch: distance + transit time).
- **Heading architecture**: 1 H1, 6 H2s + FAQ, no skipped levels, each heading owns a distinct sub-topic, order follows core (existence) → practical (nearest store) → context (why) → alternative → tangential (packaged products) → forward-looking (new opening) → FAQ.
- **Answer-block check**: direct-answer block ~45 words, standalone claim, doesn't restate H1, matches "no branch + nearest alternative" pattern used across the site's sibling pages.
- **Competitor-heading matrix**: N/A — no article-format competitors exist for this query (documented in research-notes.md, not fabricated).
- **Question coverage**: all fan-out angles found (existence, nearest branch, why not, alternative, packaged products, future opening) answered in-body and in FAQ; no PAA block was available to cross-check against (thin SERP).
- **Fact cross-check**: population figure and Kassel distance traced to research-notes.md; Espresso House address/hours traced to the chain's own site (primary source, single-sourced).
- **Intent check**: delivers the know-simple answer ("no branch") immediately, then serves the visit-in-person follow-up (nearest real option) — matches the dominant intent.
- **Readability**: plain German, short sentences, roughly grade 8-9 equivalent — consistent with sibling pages.
- **E-E-A-T flags**:
  1. No named supermarkets for the "packaged products" FAQ — search-engine-synthesized retailer list looked unreliable (included a chain, Wasgau, that doesn't operate in this region), so left generic rather than risk a wrong claim. Fill in only if the user has verified local retailers.
  2. Kassel/Hannover/Braunschweig distances are haversine (straight-line) estimates, not routed driving distances.
  3. `schema.jsonld` datePublished/dateModified are `TODO:` placeholders — set on actual publish.
  4. Population figure (127,259) is single-sourced (Statista/Wikipedia synthesis via search), not independently cross-verified against a second source.
