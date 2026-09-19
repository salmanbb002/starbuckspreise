# Research notes — "starbucks filialen"

## Step 1 — Intent + SERP

Query: "starbucks filialen" (and "starbucks filialen deutschland" as a close variant).

Top organic results (non-directory, non-stats-paywall) reviewed:

| # | Domain | URL | Title | Type | Date shown |
|---|---|---|---|---|---|
| 1 | starbuckspreise.de | /starbucks-in-meiner-nahe/ | "Starbucks in meiner Nähe – Öffnungszeiten & Filialen finden" | blog (near-me) | none |
| 2 | filial-verzeichnis.de | /trinken/kaffehauser/starbucks/ | "Starbucks – Filial-Verzeichnis" | directory | none |
| 3 | lexpress-franchise.com | /de/artikel/eine-starbucks-filiale-eroeffnen/ | "Starbucks Franchise in Deutschland: geht das?" | blog/franchise-info | 19 June 2026 |
| 4 | meinprospekt.de | /filialen/starbucks-de | "Alle Starbucks Filialen" | directory/store list | none |
| — | de.statista.com, handelsdaten.de | various | Starbucks branch-count stats | stats/paywalled | various |
| — | starbucks.de/store-locator | — | official store locator | tool | — |

**Dominant intent:** mixed — *know-simple* ("how many branches / where are they") is the single biggest cluster, with a secondary *do* ("find my nearest one" — already served by starbuckspreise.de and our own near-me page) and a smaller *know* tail around "is this a franchise / can I open one." No single competitor answers all three; the directory sites (#2, #4) are thin, address-list only, no explanatory prose.

**SERP features:** no featured snippet observed for the bare query; Statista/handelsdaten entries suggest a "stats" sub-intent; no PAA box captured directly, autocomplete/related used instead (below).

**Query fan-out (autocomplete + related + inferred PAA):**
- starbucks filialen deutschland
- wie viele starbucks filialen gibt es in deutschland
- starbucks filiale eröffnen / franchise
- starbucks filialen berlin / münchen
- starbucks filialsuche
- ist starbucks ein franchise
- wem gehören die starbucks filialen in deutschland

## Step 2 — Head-entity research (non-competitor)

- **Starbucks Corporation** — Organization. Founded 30 March 1971 (Gordon Bowker, Jerry Baldwin, Zev Siegl), Seattle, Washington, USA. HQ: Seattle. `sameAs`: https://de.wikipedia.org/wiki/Starbucks
- **AmRest Holdings** — Organization, Polish restaurant group. Master licensee for Starbucks in Germany since May 2016 (deal signed April 2016, closed 23 May 2016). `sameAs`: https://en.wikipedia.org/wiki/AmRest
- **Germany (Starbucks market)** — unlinked entity (no single Wikidata ID for "Starbucks Germany" as a distinct thing); treated as a concept/attribute of Starbucks Corporation.

## Step 4 — Competitor fetches (all 4 succeeded, no substitutions needed)

### starbuckspreise.de/starbucks-in-meiner-nahe/
- H1: "Starbucks in meiner Nähe – Öffnungszeiten & Filialen finden"
- H2: Frankfurt-area location table (15 branches, addresses, hours 05:30–23:00 range)
- H2: "Beliebte Starbucks-Standorte in Deutschland – Überblick über große Städte" — Berlin 20-30, Munich 15+, Frankfurt 10-15, plus Hamburg/Cologne/Stuttgart/Dortmund; **40% shopping centers / 30% transit hubs / 30% pedestrian zones**
- H3: "Öffnungszeiten und Services" — weekday 7:00-20:00 typical, drive-thru, mobile order, sustainability
- H3: "Tipps für den perfekten Besuch" — Rewards app, seasonal drinks, contactless
- H3: "Fazit"
- No FAQ block, no date shown.
- Heading count: 1 H1, 2 H2, 3 H3 (6 total)

### filial-verzeichnis.de/trinken/kaffehauser/starbucks/
- H1: "Starbucks"
- H2: "Filial-Verzeichnis" (category directory, not Starbucks-specific)
- H2: "Filialen suchen"
- H2: "Kategorien"
- Thin/templated directory page — no unique prose, no FAQ, no stats, no date. Confirms this SERP slot is winnable with real content.
- Heading count: 1 H1, 3 H2 (4 total)

### lexpress-franchise.com/de/artikel/eine-starbucks-filiale-eroeffnen/ (dated 19 June 2026)
- H1: "Kann man eine Starbucks-Filiale in Deutschland eröffnen?"
- H2: "Ist Starbucks ein Franchise-Unternehmen?" — company-owned + licensing, not classic franchise; founded 1971 Seattle; personalised cups/Wi-Fi/standardised offer as brand pillars
  - Stats block: 40,000+ locations worldwide, 160 in Germany (2026), 80+ countries, ~52% company-operated / 48% licensed, USA 16,864 stores, China 8,011 stores, listed as "Starbucks Corporation"
- H2: "Lizenz statt klassisches Franchise: das Geschäftsmodell" — direct ops + licensed partners (airports/stations/supermarkets), licensees are established operators not individual founders; **AmRest = master licensee for Germany, opened the 150th German location in Munich, Feb 2025**
- H3: "1) Coffee Fellows" — €15k entry fee, €50k capital, €150k-€400k total investment, 5% franchise fee, 2% marketing
- H3: "2) Balzac Coffee" — founded 1998 Hamburg, part of Espresso House since 2017
- H3: "3) Coffee & Friends" — Vienna concept, 2015
- H3: "4) Segafredo Zanetti Espresso Bar" — founded 1973 Bologna, ~110 countries
- No FAQ block.
- Heading count: 1 H1, 2 H2, 4 H3 (7 total)
- Numbers/stats (shuffled): 40,000+, 160, 2026, 80+, 52%, 48%, 16,864, 8,011, 150th, Feb 2025, €15,000, €50,000, €150,000–€400,000, 5%, 2%, 1998, 2017, 2015, 1973, ~110

### meinprospekt.de/filialen/starbucks-de
- H1: "Alle Starbucks Filialen in Deutschland"
- H2: "Wähle ein Postleitzahlengebiet, um deine Filialen zu finden!"
- H2: "Starbucks Filialen" — 31 listed branches (Berlin, Hamburg, Frankfurt, Cologne, etc.) with distances from a reference postcode (80539 München)
- H2: "Weitere Geschäfte Filialen" — unrelated retailer cross-links (boesner, Butlers, McPaper)
- H3: "Starbucks Filialen" (intro line), H3: "MeinProspekt App" — 4.5/5, 29,000+ ratings (app promo, not Starbucks-relevant)
- No FAQ, no date.
- Heading count: 1 H1, 3 H2, 2 H3 (6 total)

**Fetch note:** all 4 succeeded directly; no substitutions were needed.

## Step 5/6 — Entity ledger + tiers

| canonical | type | aliases | sameAs | kind | competitor_count | in_title/H2 | tier |
|---|---|---|---|---|---|---|---|
| Starbucks Corporation | Organization | Starbucks | https://de.wikipedia.org/wiki/Starbucks | entity | 4/4 | yes | 1 |
| Starbucks Filialen Deutschland (count, ~150-160) | Concept/Metric | Anzahl Filialen | — (unlinked) | term | 3/4 | yes | 1 |
| AmRest | Organization | — | https://en.wikipedia.org/wiki/AmRest | entity | 1/4 | no | 1 |
| Lizenz-/Franchise-Modell | Concept | Lizenzmodell | — | term | 2/4 | yes | 1 |
| Berlin (Starbucks-Standort) | Place | — | https://de.wikipedia.org/wiki/Berlin | entity | 2/4 | no | 2 |
| München (Starbucks-Standort) | Place | Munich | https://de.wikipedia.org/wiki/München | entity | 2/4 | no | 2 |
| Store Locator (starbucks.de) | Product/Tool | Filialsuche | https://www.starbucks.de/de/store-locator | entity | 2/4 | no | 2 |
| Öffnungszeiten (typisch 7-20 Uhr) | Concept | — | — | term | 1/4 | no | 2 |
| Drive-Thru | Concept | — | — | term | 1/4 | no | 2 |
| Mobile Order & Pay | Product | — | — | term | 1/4 | no | 2 |
| Starbucks Rewards | Product | — | — | term | 1/4 | no | 2 |
| Postleitzahlen-Suche (PLZ) | Concept | Postal code search | — | term | 1/4 | no | 3 |
| Coffee Fellows | Organization | — | — | entity | 1/4 | no | 3 |
| Balzac Coffee | Organization | — | — | entity | 1/4 | no | 3 |
| Segafredo Zanetti Espresso Bar | Organization | — | — | entity | 1/4 | no | 3 |
| Coffee & Friends | Organization | — | — | entity | 1/4 | no | 3 |

**Relationships (backbone):**
1. Starbucks —founded in→ 1971, Seattle
2. Starbucks —operates→ 40.000+ Filialen weltweit in 80+ Ländern (source: lexpress-franchise.com, 2026 figure)
3. Starbucks Deutschland —eröffnete erste Filiale→ 2002, Berlin
4. Starbucks Deutschland —zählt aktuell→ rund 150–160 Filialen
5. AmRest —ist Masterlizenznehmer für→ Starbucks in Deutschland (seit Mai 2016)
6. AmRest —eröffnete→ 150. deutsche Filiale in München (Februar 2025)
7. Starbucks —betreibt Filialen über→ Lizenzmodell, nicht klassisches Franchise
8. Berlin —beherbergt→ höchste Filialdichte Deutschlands (~20-30)
9. München —beherbergt→ zweithöchste Konzentration (15+)
10. Starbucks-Filialen —liegen typischerweise in→ Einkaufszentren (~40%), Verkehrsknotenpunkten (~30%), Fußgängerzonen (~30%)
11. Starbucks-Filialsuche (starbucks.de) —dient zum Finden von→ Adresse, Öffnungszeiten der einzelnen Filiale

**Dedupe log:**
- "Franchise" merged into "Lizenz-/Franchise-Modell" — same concept, competitors use both words; canonical term reflects the actual (non-franchise) model to avoid misleading the reader.
- Coffee Fellows/Balzac/Segafredo/Coffee & Friends parked at tier 3 — they're franchise *alternatives*, not Starbucks entities; relevant only as a one-line aside answering "is Starbucks a franchise," not a full comparison (that's lexpress-franchise.com's own angle, not this page's).
- "MeinProspekt App" rating dropped entirely — unrelated to Starbucks, pure competitor-site cross-promo.
- Individual Frankfurt-table addresses (15 rows) and meinprospekt's 31-row list dropped — those are near-me/locator content, explicitly out of scope for this hub page (see Step 8e cannibalisation note).

## Step 7 — Information-gain pass

All 4 competitors fail on at least one of:
- **starbuckspreise.de**: no source cited for the 150-160 figure, no date, no mention of AmRest/licensing at all.
- **filial-verzeichnis.de / meinprospekt.de**: pure address directories, zero explanatory content, no branch-count, no licensing info, no date.
- **lexpress-franchise.com**: best on stats + licensing, but frames everything around "can *I* open one" (franchise-seeker angle) rather than "how many are there / where / how do I find mine" (the actual dominant searcher intent for the bare query); also doesn't address the near-me use case at all.

**None of the four combine**: a dated, sourced branch-count with the discrepancy between sources acknowledged, a plain-language explanation of who actually runs the stores (AmRest, licence not franchise), a distribution overview by city, and a clear next step for someone who actually just wants to find a branch.

**Information-gain element committed to:** a dated "Starbucks-Filialen in Deutschland auf einen Blick" table (count, model, top cities, first opened) plus an explicit "Stand: September 2026" freshness note — none of the competitors date-stamp their figures. This also functions as the differentiation device vs. the site's own near-me page (see 8e).

## Step 8 — Heading architecture

| # | Level | Heading | Focus/LSI phrase | Question answered | Tier-1/2 carried |
|---|---|---|---|---|---|
| — | H1 | Starbucks Filialen in Deutschland: Wie viele es gibt und wo sie liegen | starbucks filialen (focus) | What is this page about | Starbucks Corp, Filialen-Anzahl |
| — | answer block | (direct answer, no heading) | — | How many Starbucks branches are in Germany, who runs them | Filialen-Anzahl, AmRest |
| 1 | H2 | Wie viele Starbucks-Filialen gibt es in Deutschland? | starbucks filialen deutschland | know-simple count question | Filialen-Anzahl, Berlin, München |
| 1a | H3 | Wie hat sich die Zahl seit der ersten Filiale 2002 entwickelt? | erste starbucks filiale deutschland | historical growth | Starbucks Corp, Filialen-Anzahl |
| 2 | H2 | Wer betreibt die Starbucks-Filialen in Deutschland – ist das ein Franchise? | starbucks filiale franchise | ownership/licensing question | AmRest, Lizenzmodell |
| 2a | H3 | Was unterscheidet Lizenz und klassisches Franchise bei Starbucks? | starbucks franchise werden | franchise-alternatives aside | Lizenzmodell |
| 3 | H2 | In welchen Städten liegen die meisten Filialen? | starbucks filialen berlin münchen | distribution question | Berlin, München, Store Locator |
| 3a | H3 | Wo befinden sich Starbucks-Filialen typischerweise? | — | shopping centre / transit / pedestrian split | — (tier-3 stat) |
| 4 | H2 | Wie finden Sie die nächste Starbucks-Filiale in Ihrer Nähe? | starbucks filialsuche | do-intent, practical | Store Locator, internal links |
| 5 | H2 | Starbucks-Filialen in Deutschland auf einen Blick (Stand September 2026) | — (info-gain table) | quick reference / freshness | all tier-1 |
| 6 | H2 | Häufig gestellte Fragen (FAQ) | — | leftover questions | mixed |

## Step 8e — Internal-link plan + cannibalisation check

**Cannibalisation risk — explicitly checked and resolved:** the site already has `blog/starbucks-in-der-naehe.html` and `blog/starbucks-near-me.html` (personalised "find one near me" intent) plus 11 city pages (Kassel, Trier, Gießen, etc. — single-branch deep dives) and `blog/starbucks-geoeffnet.html` (opening-hours/"is it open now" intent). This new page targets a **different, broader intent**: "how many branches exist / who runs them / how are they distributed" — an overview/explainer, not a locator or a single-city page. It does **not** repeat the Frankfurt/near-me address table or duplicate detailed opening-hours content — those are linked out to instead. Sibling forks in this batch are separately writing "starbucks deutschland filialen" (full nationwide list) and "starbucks in der nähe maps" (map-based lookup); this page stays at the explainer/overview altitude and links to both use cases rather than absorbing them, so all three keywords can coexist without targeting the same query.

**Internal links (anchor → target):**
- "Finden Sie Ihre Filiale in der Nähe" → /blog/starbucks-near-me.html (or starbucks-in-der-naehe.html)
- "aktuelle Öffnungszeiten einer Filiale" → /blog/starbucks-geoeffnet.html
- "Preise nach Getränk und Größe" → /blog/starbucks-preise.html
- City examples: "Starbucks Gießen", "Starbucks Trier", "Starbucks Kassel" → respective /blog/ city pages

## FAQ source map

Sourced from: fan-out questions, the franchise angle in competitor #3, and genuine gaps none of the four answered (below, "gaps" marked).
1. Wie viele Starbucks-Filialen gibt es in Deutschland? (from Step 1 fan-out)
2. Wo wurde die erste Starbucks-Filiale in Deutschland eröffnet? (gap — no competitor states this clearly)
3. Ist Starbucks in Deutschland ein Franchise? (from competitor #3's core question)
4. Wer betreibt die Starbucks-Filialen in Deutschland? (gap — only #3 names AmRest, buried)
5. Kann ich selbst eine Starbucks-Filiale eröffnen? (from competitor #3)
6. In welcher Stadt gibt es die meisten Starbucks-Filialen? (from #1's city overview)
7. Wo finde ich die Starbucks-Filiale in meiner Nähe? (do-intent fan-out; links out rather than re-answering)
8. Gibt es in jeder deutschen Stadt eine Starbucks-Filiale? (gap — addressed via the Trier/Bamberg no-branch cases the site already covers)
9. Sind alle Starbucks-Filialen in Deutschland gleich ausgestattet (Drive-Thru, WLAN etc.)? (gap)
10. Nimmt die Zahl der Starbucks-Filialen in Deutschland noch zu? (gap — stagnation/slight decline noted in Step 1 synthesis)
