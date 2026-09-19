# Coverage / QA — "starbucks filialen"

## Entity coverage
- **Tier 1 (4 items):** 100% covered, all with a stated attribute/relationship — Starbucks Corporation (founding, HQ, global scale), Filialen-Anzahl (150-160, sourced + dated), AmRest (master licensee since 2016, relationship to Starbucks), Lizenz-/Franchise-Modell (52/48% split, contrasted with true franchise).
- **Tier 2 (7 items):** 100% covered after the Rewards fix — Berlin, München, Store Locator, Öffnungszeiten, Drive-Thru, Mobile Order & Pay, Starbucks Rewards (added to §4 step 2 on second pass, see draft.annotated.md note).
- **Tier 3 (5 items):** 4/5 used naturally (Postleitzahlen-Suche via "Postleitzahl eingeben," Coffee Fellows, Balzac Coffee, Segafredo Zanetti Espresso Bar). "Coffee & Friends" deliberately skipped — logged in draft.annotated.md, three examples were enough.

## Heading architecture check
- Exactly 1 H1; H2→H3 nesting valid throughout (§1, §2, §3 each have one H3 child; §4 and §5 have none); no skipped levels.
- Every H2/H3 targets a distinct question/phrase — no two headings compete for the same query.
- Heading list read alone: count → who runs them/licensing → where they're concentrated → how to find yours → dated summary table → FAQ. Conveys the page's logic without the body.
- H2 count (5, excl. FAQ) is proportionate to the fan-out set captured in Step 1 (7 fan-out phrases, all mapped to a heading or FAQ entry).

## Answer-block check
- Direct-answer block: 52 words. Doesn't restate the H1. Answers count + operator in one shot, matching the "know-simple" dominant intent (no snippet format was observed on the live SERP to match against).
- Each question-style H2/H3 opens with a direct answer sentence before expanding (verified §1, §1a, §2, §2a, §3, §3a).

## Competitor-heading matrix

| Recurring competitor heading | Covered? |
|---|---|
| Branch count / "how many" (starbuckspreise.de, lexpress-franchise.com implicitly) | Yes — §1, with date + source discrepancy disclosed |
| City/location overview (starbuckspreise.de, meinprospekt.de) | Yes — §3, without duplicating the address-list format |
| Franchise/licensing (lexpress-franchise.com) | Yes — §2, reframed toward the "who runs my local store" reader rather than the franchise-seeker |
| Raw address directory (filial-verzeichnis.de, meinprospekt.de) | Intentionally skipped — that's the near-me page's job, not this hub page's; linked out instead (§4) |
| Öffnungszeiten detail table (starbuckspreise.de) | Intentionally skipped — general pattern only (§1a context), detailed hours linked to starbucks-geoeffnet.html |

## Question coverage
All Step 1 fan-out questions and all 10 FAQ-source questions are mapped to a section or FAQ entry (see research-notes.md FAQ source map). None left unanswered.

## Fact cross-check
Every number in the draft traces to research-notes.md:
- 150-160 Filialen → starbuckspreise.de + lexpress-franchise.com (160, 2026)
- 164 (2023/24) → Statista/Handelsdaten (search snippet only, not directly fetched — see flag below)
- 40,000+ worldwide, 80+ countries, 16,864 US, 8,011 China, 52%/48% → lexpress-franchise.com
- 2002 Berlin first store, Feb 2025 150th store in Munich → lexpress-franchise.com + search synthesis
- AmRest since May 2016 → WebSearch synthesis (amrest.eu press releases, not directly fetched)
- Berlin 20-30, Munich 15+, 40/30/30 location-type split → starbuckspreise.de
- Founded 1971, Seattle → Wikipedia-derived search synthesis

**⚠️ Fact-check flags for manual verification before publishing:**
1. **Global store count discrepancy**: one search pass returned "32,000+ worldwide" (unsourced AI synthesis), while the fetched lexpress-franchise.com page states "40,000+ worldwide, 80+ countries, USA 16,864, China 8,011" with more internal precision. The draft uses the more specific figure, but neither was cross-checked against Starbucks' own FY2025/2026 investor filing — **verify against news.starbucks.com or the latest 10-K before publishing.**
2. **164 vs 150-160 for Germany**: the 164 figure (Statista/Handelsdaten, FY2023/24) was seen only in WebSearch snippets, not fetched directly — treat as approximate, already framed as "older" in the draft.
3. **AmRest May 2016 date**: sourced from WebSearch synthesis of amrest.eu press-release titles, not a direct fetch of the press release text — low risk (dates were consistent across two independent snippet titles) but not independently verified.
4. **"150th store, Feb 2025, Munich"**: appears once, inside the lexpress-franchise.com competitor page — single-sourced. Recommend a quick corroborating search before publishing since it's a specific, checkable claim.

## Intent check
Serves the dominant know-simple intent (branch count) first, then the secondary know intent (licensing/franchise), then the distribution question, then routes the do-intent searchers (find my nearest) to the site's existing near-me and city pages rather than duplicating them. Matches what none of the 4 competitors did in one page.

## Readability
Estimated grade level: ~8-9 (German Realschule/Gymnasium Mittelstufe equivalent) — matches the site's existing city-page drafts (e.g. Gießen). No single paragraph exceeds 4 sentences.

## E-E-A-T flags (need real human input before publishing)
- **Author byline + credentials**: `schema.jsonld` has `TODO:` placeholders — needs a real name.
- **datePublished/dateModified**: placeholders — set on actual publish.
- **No first-person "as an expert" scaffolding was used in this draft** (unlike some earlier site drafts) — the topic (corporate/franchise facts) didn't call for a lived-experience angle, so none was invented.
- **YMYL**: low — this is corporate/franchise-structure information, not health/finance/legal advice. No disclaimer needed beyond the standard "Recherchestand" freshness note already in the draft.
- **HowTo schema**: deliberately not generated. §4 lists five alternative ways to find a branch (not a single sequential procedure), so a `HowTo` type would misrepresent the content — flagging this decision rather than forcing the schema.

## Word count
~1,180 words (body + FAQ, excluding headings/table markup).

## FAQ count
10.
