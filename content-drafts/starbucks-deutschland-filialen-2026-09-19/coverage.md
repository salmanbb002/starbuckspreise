# Coverage / QA — "starbucks deutschland filialen"

## Entity coverage
- **Tier 1 (4/4 covered, 100%):** Deutschland, Starbucks-Filialen (Anzahl), Starbucks
  Corporation, AmRest Coffee Deutschland — all four carry at least one stated attribute/
  relationship (not bare mentions): Deutschland→179 Filialen; AmRest→betreibt seit 2016,
  gekauft für ~41 Mio. €; Starbucks Corporation→verkaufte 2016, gründete 2002 in Berlin.
- **Tier 2 (6/6 covered, 100%):** Nordrhein-Westfalen, Berlin, Bayern, KarstadtQuelle AG,
  Frankfurt am Main, Öffnungszeiten.
- **Tier 3 (5/6 used, 83%):** Hamburg, Köln, Store Locator/App, Drive-Thru, Mobile Order &
  Pay used. Howard Schultz deliberately **not** used — logged in the annotated draft
  (global 1987 acquisition isn't specific to the German-expansion story this piece tells).

## Heading architecture check
- One H1, no skipped levels, every H3-equivalent nests under an H2. (This draft uses only
  H1/H2 — no H3 was needed; each H2 covers one single sub-topic, so no forced nesting.)
- No two H2s target the same query. Each maps to a distinct Step 8 row.
- Heading list read alone conveys the logic: count → by state → by city → who runs it →
  history → find one near you → FAQ.

## Answer-block check
- Direct-answer block: 47 words, doesn't restate the H1, leads with the number (matches a
  paragraph-snippet format, the likely format given the query is a simple stat lookup).
- Each question-style FAQ entry answers in its first sentence.

## Competitor-heading matrix
| Recurring competitor heading | Covered? |
|---|---|
| Filialzahl / count (handelsdaten, Statista) | Yes — with a newer, exact, dated number |
| Address directory by city (meinprospekt) | Partially — top-cities table, not a full address list (that's the locator pages' job, linked out) |
| "Beliebte Standorte" by city (starbuckspreise.de) | Yes — top-cities table, sourced/dated rather than rounded |
| Öffnungszeiten (starbuckspreise.de) | Yes — one paragraph, kept brief since it's not this page's core angle |
| Ownership / who runs it | Not covered by any of the 4 — this draft's own addition |
| State-by-state breakdown | Not covered by any of the 4 — this draft's own addition (info-gain element) |

## Question coverage
All fan-out questions from research-notes.md are answered in the body or FAQ. One
question — "Starbucks Filiale eröffnen" (franchise how-to) — is intentionally answered
only briefly in the FAQ and pointed elsewhere, since it's a different (do/commercial)
search intent that deserves its own article; logged in the dedupe log, not silently
dropped.

## Fact cross-check
Every number in the draft traces to research-notes.md:
- 179 filialen / 1 July 2026 / state table / city table → ScrapeHero (Step 2)
- 164 filialen, Geschäftsjahr 2023/24 → handelsdaten.de (Step 4)
- 158 filialen (2016) → de.wikipedia.org/wiki/Starbucks_Coffee_Deutschland (Step 2)
- AmRest purchase, ~€41M, April 2016, Munich HQ → Wikipedia (Step 2)
- May 2002 Berlin opening, KarstadtQuelle JV 2002–2004 → Wikipedia (Step 2)
- Statista publish/update dates → de.statista.com page metadata (Step 4)

**Flag:** the "übrige 6 Bundesländer" row and the "no Bundesland has zero stores" claim
both rest on a single third-party aggregator (ScrapeHero) that wasn't cross-verified
against a second independent count — reasonable for a blog post, but flag as the one
number worth spot-checking before publish if precision matters to the client.

## Intent check
Delivers a direct, dated count plus the regional/ownership context a "how many / where"
searcher wants; routes proximity-intent readers to the existing near-me pages rather than
duplicating them.

## Readability
Estimated grade 8-9 (German). A few sentences in the "Geschichte" and "Wer betreibt"
sections run long — acceptable for this piece's semi-explanatory register but worth a
trim pass if the client wants tighter German.

## E-E-A-T flags (need manual input before publishing)
- **Author byline/credentials** — `schema.jsonld` has a `TODO:` placeholder; no real
  person is named.
- **datePublished/dateModified** — placeholders; set on actual publish.
- **No first-person "as an expert" scaffolding was added** in this draft (topic doesn't
  call for it — it's a data/reference piece), so nothing to flag there.
- **Single-source figures** — see the ScrapeHero flag above; consider a second source
  (e.g. the official Starbucks store locator's own count) if this needs to withstand
  scrutiny.
- Not strictly YMYL, but it's a factual/statistical claim about a real company — keep the
  "Stand 1. Juli 2026" date visible on-page so it reads as a snapshot, not an evergreen
  claim, and revisit the count periodically.

## Cannibalisation flag (carried from research-notes.md)
Overlaps in subject matter (not in target query) with `/starbucks-in-meiner-naehe.html`
and `/blog/starbucks-near-me.html`. This draft was deliberately scoped to the count/
state/ownership/history angle and kept the "find one near you" section thin with outbound
links rather than re-covering store-locator mechanics. Recommend a human check of the
three live pages side by side before publishing to confirm the boundary held.
