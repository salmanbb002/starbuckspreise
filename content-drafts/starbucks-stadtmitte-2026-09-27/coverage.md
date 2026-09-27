# Coverage + QA: starbucks-stadtmitte (27 Sep 2026)

**Title tag:** Starbucks Stadtmitte: Filialen, Adressen & Öffnungszeiten 2026 (61 chars)
**Meta:** Starbucks Stadtmitte in Berlin, Düsseldorf & Stuttgart: alle 6 Filialen mit Adresse und Öffnungszeiten, plus welche Einträge veraltet sind. Jetzt prüfen. (~150)
**Slug:** /blog/starbucks-stadtmitte · Words: ~1,730 · FAQ: 11 · H2: 9

## Entity coverage
- Tier 1: 8/8 covered (100%). All 8 carry an attribute/relationship (address, hours, location).
- Tier 2: 8/8 (100%).
- Tier 3 used: Checkpoint Charlie, Quartier 206, Uber Eats, Mobile Order, Hbf Kiosk, Rotebühlplatz. Unused: Pei Cobb Freed (no reader value).

## Heading architecture
One H1; H2 → H3 only (§4 and §5 have H3s); no skipped levels. Each H2 owns a distinct city or sub-intent phrase; no two target the same query. The heading list alone reads as: overview → why ambiguous → Berlin → Düsseldorf → Stuttgart → closed → how to check → prices → FAQ. ✔

## Answer block
Direct answer ~55 words: names all 6 stores and the Esslingen closure, and doesn't restate the H1. Every H2 opens with a definite answer sentence. ✔

## Competitor matrix
Directory templates (Info / Öffnungszeiten / Adresse / Bewertungen / Haltestellen) are covered via table + city sections. Photo galleries and "Objekte in der Nähe" are skipped (not text value).

## Question coverage
Fan-out (berlin / düsseldorf / stuttgart / öffnungszeiten / sonntag / königsallee / esslingen) is all answered. No PAA was captured, which is a limitation.

## Fact-check flags ⚠ (need you)
1. **Opening hours are from directories/snippets, not a rendered official locator page** (starbucks.de pages are JS/403). Verify all 5 published hour sets in the Starbucks app before going live, especially Schadowstraße Sunday 12–18 and Königstraße 44 at 7:00 vs 7:30.
2. **Steinstraße 1-3:** the "opened 2018" date is based on a May 2018 announcement ("summer 2018"). The exact date is unverified.
3. **Schadowstraße 11 vs 84:** golocal says 84; dasoertliche/kaufda/meinprospekt say 11. The draft uses 11.
4. **Königsbau Passagen 26 vs 28:** the draft uses 26 (centre operator) and notes that some directories say 28.
5. **"Friedrichstraße 96 is ~1 km north"** is an estimate. Check it on a map.
6. **§8 Bahnhof pricing** ("often franchise-run, prices can differ") has no hard source. It's consistent with blog/starbucks-in-der-naehe's FAQ, but it's a generalisation.
7. Esslingen closure: Esslinger Zeitung (Feb 2020); "Villa Berg" successor is from the search summary (named in the notes, not in the draft).

## Intent
visit-in-person/know-simple: delivered (addresses + hours + a disambiguation table).

## Readability
~Grade 8. The table is dense but scannable; short sentences.

## E-E-A-T
Byline is "StarbucksPreise Redaktion" (site convention). There are no first-person claims. The "Unser Tipp" line in §6 is advice, not lived experience. No YMYL.

## Build notes
Hero image TODO (img/blog/starbucks-stadtmitte-hero.webp, 1600×1000, no Starbucks logo). `#direct-answer` id on the blockquote. Add links FROM in-der-naehe §7 and deutschland-filialen §6. datePublished TODO.
