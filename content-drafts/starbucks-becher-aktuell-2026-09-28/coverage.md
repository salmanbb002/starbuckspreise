# Coverage / QA: starbucks-becher-aktuell

- Words: about 2,030 in total (1,615 body plus 12 FAQs). Direct answer: 49 words, not a restatement of the H1.
- Tier-1 coverage: 6/6, each with at least one attribute or relationship stated. Tier-2 coverage: 9/9.
- Heading architecture: one H1, 9 H2s, 3 H3s under H2s (§2 ×2, §3 ×1), no skipped levels. Each H2 owns a distinct phrase.
- Information gain: the dated Becher-Kalender 2026 table and the 5-step list for getting a limited cup.
- FAQ: 12 questions. The on-page text matches the FAQPage JSON-LD verbatim (both are generated from draft.md).
- Schema: Article + FAQPage + BreadcrumbList. `about`/`mentions` use Thing, CreativeWork or Organization only, with no Product or Event types (GSC rule). The Wikidata IDs were verified through the API.
- Layout check: `scripts/check-blog-layout.py` passes.

## Fact cross-check
All dates, prices and limits trace to S1–S10 in research-notes.md.

## Open flags (need a human)
1. **Peanuts in Germany:** global/Europe availability comes from Starbucks Stories search results. The press page could not be fetched (403 / JS wall / browser extension offline), and there is no DE-specific confirmation. The page tells readers to ask their store.
2. **"Deine Tasse" dates (16.06.–19.10.2025)** come from a search-result summary of a page that now returns 404. They could not be re-read directly.
3. **The Autumn 2026 product list is the UK list.** Starbucks says the range varies by store, and the DE range is not published.
4. There are no official EUR prices for any limited cup. The page gives US prices only, labelled as such.
5. **Freshness:** the Holiday 2026 date is unknown. Update this page when the Holiday drop is announced.
6. Hero image: the existing `starbucks-becher-hero.webp` is reused (gold studded cold cups).
