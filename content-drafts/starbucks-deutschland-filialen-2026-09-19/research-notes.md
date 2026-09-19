# Research notes — "starbucks deutschland filialen"

## Step 1 — Intent + SERP

- **Dominant intent:** know / know-simple — "how many Starbucks branches are there in Germany
  and where are they" (a data/overview question), not a proximity query.
- **Secondary intent:** some directory/navigational overlap (users who really want a locator).
- **SERP mix observed** (via WebSearch, not a rendered browser SERP — no PAA/snippet-format
  panel data was directly visible, so featured-snippet format is inferred, not confirmed):
  stats portals (handelsdaten.de, Statista), aggregator directories (meinprospekt.de,
  Cylex, Kaufda), a near-identically-named competitor site **starbuckspreise.de** (.de, not
  our .com), the official Starbucks store locator, and city-specific directory pages
  (in-berlin-brandenburg.com for Berlin, kaufda.de for Hamburg).
- **Query fan-out (from result titles/snippets):** "starbucks anzahl filialen deutschland",
  "starbucks filialen liste", "starbucks filiale eröffnen deutschland" (franchise
  question — out of scope, logged below), "starbucks bundesländer", city-level "starbucks
  filialen <stadt>" queries.
- No FAQ block was found on any fetched competitor page — the FAQ for this draft is built
  from the fan-out + genuine follow-up questions (Step 10 rule).

## Step 2 — Head-entity research (non-competitor sources: Wikipedia, ScrapeHero)

- **Starbucks Corporation** — Org. HQ Seattle, WA, USA. Founded 1971 (Baldwin/Bowker/Siegl);
  Howard Schultz bought it 1987. >30,500 stores globally (Nov 2021 figure, used only as
  scale context, not as a current German number). sameAs: https://de.wikipedia.org/wiki/Starbucks
- **AmRest Coffee Deutschland Sp. z o.o. & Co. KG** — Org, current operator of all German
  Starbucks stores. HQ Munich. Bought 100% of German operations from Starbucks Corp. for
  ~€41M in April 2016. Unlinked entity — no dedicated Wikidata ID found; sameAs left blank.
- **Deutschland (Germany)** — Place. sameAs: https://de.wikipedia.org/wiki/Deutschland
- **KarstadtQuelle AG** — Org, Starbucks's German joint-venture partner 2002–2004, before
  Starbucks took full control. Unlinked entity (no clean current Wikidata match post-2004
  corporate history changes) — recorded without sameAs.

## Step 3 — Title + metadata

- **Title (primary):** Starbucks Filialen in Deutschland 2026: Wie viele & wo? (58 chars)
- **Alt title 1:** Starbucks Deutschland: Alle Filialen, Zahlen & Bundesländer (2026)
- **H1:** Starbucks-Filialen in Deutschland: Wie viele gibt es und wo?
- **Meta description:** Deutschland zählt 179 Starbucks-Filialen (Stand 1. Juli 2026) — mit
  NRW als Spitzenreiter. Alle Zahlen nach Bundesland, Stadt und Geschichte im Überblick.
  (152 chars)
- **URL slug:** starbucks-deutschland-filialen
- **OG title/description:** mirror the above.

## Step 4 — Competitor fetch (4 distinct domains)

1. **handelsdaten.de** — stats page, EHI Retail Institute source. Paywalled beyond one
   number: "Ende Geschäftsjahr 2023/2024: 164 Starbucks-Filialen in Deutschland." No
   headings beyond nav/legal sections, no FAQ, no visible update date.
2. **meinprospekt.de/filialen/starbucks-de** — directory listing (H1 "Alle Starbucks
   Filialen in Deutschland"), ~33 individual addresses shown, no aggregate total stated,
   no FAQ, no date.
3. **starbuckspreise.de/starbucks-in-meiner-nahe** (note: **.de**, a distinct competitor,
   not our own .com site) — richest content found: H1 "Starbucks in meiner Nähe –
   Öffnungszeiten & Filialen finden"; H2 Frankfurt-area location table; H2 "Beliebte
   Starbucks-Standorte in Deutschland" with a location-type split (40% Einkaufszentren /
   30% Bahnhöfe-Flughäfen / 30% Fußgängerzonen) and city counts (Berlin 20–30, München 15+,
   Frankfurt 10–15); H4 opening hours/services; H4 visit tips; H4 conclusion. No FAQ
   section, no visible date, figures are round estimates ("150–160", "15+") not a hard count.
4. **de.statista.com** — paywalled beyond headline. H1s reference data through fiscal 2025;
   exact figure hidden behind subscription ("rund *** Cafés"). Published 7 Sep 2026,
   updated 28 Apr 2026. No FAQ.

**Fetch failure:** filialfinder.cylex.de returned HTTP 403 — substituted de.statista.com
as the 4th distinct domain per pipeline rule (no fabrication).

### Per-competitor extraction

**handelsdaten.de**
| term | type | canonical | kind |
|---|---|---|---|
| Starbucks-Kaffeebars | Concept | Starbucks-Filialen | term |
| Geschäftsjahr 2023/2024 | Date | 2023/2024 (Geschäftsjahr) | entity |
| 164 Filialen | Metric | 164 Starbucks-Filialen (2023/24) | term |
| EHI Retail Institute | Org | EHI Retail Institute | entity |
Numbers: 164, 2009/2010, 2024/2025. Contextual words: Gastronomie, Catering, Zeitreihe, Statistik. Count: 8.

**meinprospekt.de**
| term | type | canonical | kind |
|---|---|---|---|
| Filialen | Concept | Starbucks-Filialen | term |
| Berlin | Place | Berlin | entity |
| Hamburg | Place | Hamburg | entity |
| Frankfurt | Place | Frankfurt am Main | entity |
| Köln | Place | Köln | entity |
| Postleitzahl | Concept | Postleitzahl | term |
Numbers: 33 (approx. locations shown). Contextual words: Prospekte, Angebote, Filialfinder, Postleitzahl-Suche. Count: 9.

**starbuckspreise.de**
| term | type | canonical | kind |
|---|---|---|---|
| Öffnungszeiten | Concept | Öffnungszeiten | term |
| Filialen | Concept | Starbucks-Filialen | term |
| Berlin | Place | Berlin | entity |
| München | Place | München | entity |
| Frankfurt | Place | Frankfurt am Main | entity |
| Hamburg | Place | Hamburg | entity |
| Köln | Place | Köln | entity |
| Stuttgart | Place | Stuttgart | entity |
| Dortmund | Place | Dortmund | entity |
| Einkaufszentren | Concept | Einkaufszentrum | term |
| Bahnhöfe/Flughäfen | Concept | Bahnhof/Flughafen-Standort | term |
| Drive-Thru | Product/Service | Drive-Thru | term |
| Mobile Order | Product/Service | Mobile Order & Pay | term |
| Rewards-Programm | Product/Service | Starbucks Rewards | term |
Numbers: 150-160, 20-30, 15+, 10-15, 40%, 30%, 30%. Contextual words: Third Place, Fazit, Tipps, Besuch, kontaktlos. Count: 21.

**de.statista.com**
| term | type | canonical | kind |
|---|---|---|---|
| Restaurants/Cafés | Concept | Starbucks-Filialen | term |
| Starbucks Coffee Deutschland GmbH | Org | AmRest Coffee Deutschland Sp. z o.o. & Co. KG | entity |
| Geschäftsjahr 2025 | Date | 2025 (Geschäftsjahr) | entity
Numbers: 2009, 2025, *** (hidden). Contextual words: Erfolgskurs, Themen, Statistiken. Count: 6.

## Step 5/6 — Entity map + tiers

| canonical | type | kind | competitor_count | in_title_or_h2 | tier | sameAs |
|---|---|---|---|---|---|---|
| Deutschland | Place | entity | 4 | yes | 1 | wikipedia:Deutschland |
| Starbucks-Filialen (Anzahl) | Concept | term | 4 | yes | 1 | — |
| Starbucks Corporation | Org | entity | 2 | no | 1 | wikipedia:Starbucks |
| AmRest Coffee Deutschland | Org | entity | 1 | no | 1 | — (unlinked) |
| Nordrhein-Westfalen | Place | entity | 0* | no | 2 | wikipedia:Nordrhein-Westfalen |
| Berlin | Place | entity | 2 | no | 2 | wikipedia:Berlin |
| Bayern / München | Place | entity | 2 | no | 2 | wikipedia:Bayern |
| KarstadtQuelle AG | Org | entity | 0* | no | 2 | — (unlinked) |
| Frankfurt am Main | Place | entity | 2 | no | 2 | wikipedia:Frankfurt_am_Main |
| Öffnungszeiten | Concept | term | 2 | no | 2 | — |
| Hamburg | Place | entity | 3 | no | 3 | wikipedia:Hamburg |
| Köln | Place | entity | 2 | no | 3 | wikipedia:Köln |
| Store Locator / App | Product | term | 1 | no | 3 | — |
| Drive-Thru | Product | term | 1 | no | 3 | — |
| Mobile Order & Pay | Product | term | 1 | no | 3 | — |
| Howard Schultz | Person | entity | 0* | no | 3 | wikipedia:Howard_Schultz |
| EHI Retail Institute | Org | entity | 1 | no | 3 | — |

\* NRW/KarstadtQuelle/Howard Schultz came from the Step 2 non-competitor sources
(Wikipedia + ScrapeHero), not the 4 fetched competitor pages — promoted to tier 1/2
because they're central to answering the exact query (state breakdown, ownership) and
none of the thin competitor pages cover them, which is itself the information gain.

**Relationships (triples):**
- Deutschland —hat (Stand 1. Juli 2026)→ 179 Starbucks-Filialen
- Nordrhein-Westfalen —hat die meisten Filialen mit→ 36 Standorten (20 %)
- AmRest Coffee Deutschland —betreibt seit April 2016 alle→ deutschen Starbucks-Filialen
- Starbucks Corporation —verkaufte 2016 die deutschen Filialen an→ AmRest (für ca. 41 Mio. €)
- Starbucks —eröffnete die ersten deutschen Filialen 2002 in→ Berlin
- Starbucks Deutschland —wurde 2002–2004 als Joint Venture betrieben mit→ KarstadtQuelle AG
- Berlin —zählt als Bundesland/Stadt→ 19 Filialen
- Frankfurt am Main —zählt (Stadt-Ebene, höchster Wert außerhalb Stadtstaaten)→ 14 Filialen

**Dedupe log:** "Restaurants" (Statista's label) merged into canonical "Starbucks-Filialen".
"Starbucks Coffee Deutschland GmbH" (old/former legal name, used by Statista) merged into
canonical "AmRest Coffee Deutschland" with a note that the name changed in 2016 — kept as
an alias, not a separate entity. Parked out-of-scope: "Starbucks Filiale eröffnen"
(franchise/how-to-open-a-store query) — different search intent (do/commercial), belongs
in its own article, not absorbed here.

## Step 7 — Information-gain pass

All 4 competitors are either paywalled past one soft figure (handelsdaten.de, Statista),
a bare address directory with no total (meinprospekt.de), or use **rounded estimates**
with no state-level breakdown and no visible date (starbuckspreise.de: "150–160", "15+").
**None give an exact, dated, complete national figure, and none break the country down by
all 16 Bundesländer.**

**Committed information-gain element:** a full **state-by-state (Bundesland) table** and
a **top-cities table**, both sourced from a July 2026 count (179 stores, ScrapeHero), plus
a short "Vom ersten Standort bis heute" ownership/history timeline (KarstadtQuelle →
Starbucks-Vollkontrolle 2004 → AmRest-Übernahme 2016) that none of the 4 competitors
mention at all. This also answers the un-covered fan-out question "wer betreibt Starbucks
in Deutschland".

## Step 8 — Heading + keyword + question map

| Level | Heading | Focus/LSI phrase | Question answered | Tier-1/2 carried |
|---|---|---|---|---|
| H1 | Starbucks-Filialen in Deutschland: Wie viele gibt es und wo? | starbucks deutschland filialen | — | Deutschland, Starbucks-Filialen |
| (answer block) | — | — | direct count | Deutschland → 179 Filialen |
| H2 | Wie viele Starbucks-Filialen gibt es in Deutschland? | starbucks filialen anzahl | know-simple count | Deutschland, Starbucks-Filialen, Starbucks Corporation |
| H2 | Starbucks-Filialen nach Bundesland | starbucks bundesländer | where regionally | NRW, Bayern, Berlin |
| H2 | Die Städte mit den meisten Starbucks-Filialen | starbucks filialen städte | which cities | Berlin, Frankfurt, München, Hamburg, Köln |
| H2 | Wer betreibt Starbucks in Deutschland? | starbucks deutschland betreiber | ownership | AmRest, Starbucks Corporation, KarstadtQuelle |
| H2 | Geschichte: Vom ersten Standort in Berlin bis heute | starbucks geschichte deutschland | how it grew | Berlin, KarstadtQuelle, AmRest, Starbucks Corporation |
| H2 | Starbucks-Filiale in deiner Nähe finden | starbucks in der nähe (deliberate, light touch — links out) | how do I find the nearest one | Store Locator/App |
| H2 | Häufig gestellte Fragen | — | fan-out + FAQ | mixed |

No skipped levels; no H2 repeats the same phrase; the "in deiner Nähe" H2 is deliberately
short (2–3 sentences + internal links) so it doesn't re-fight the near-me pages for the
same query — see cannibalisation note below.

## Step 8e — Internal-link plan / cannibalisation check

**⚠️ Cannibalisation flag — read before publishing:**
`/starbucks-in-meiner-naehe.html` (root pillar) already has an H2 "Starbucks-Standorte nach
Stadt" listing the same six major cities (Berlin, München, Hamburg, Köln, Frankfurt,
Stuttgart) with similar branch-density claims. `/blog/starbucks-near-me.html` also has an
H2 "Filialdichte & Hotspots in deutschen Großstädten" covering the same ground.

This draft is written to **not duplicate** those: it owns the *nationwide count + full
16-state breakdown + ownership/history* angle (a data/reference page), while the existing
pages own the *"find the nearest one to me right now" procedural* angle (store locator,
app, drive-thru, mobile order, WLAN). The new "Starbucks-Filiale in deiner Nähe finden" H2
here is intentionally thin and links out rather than re-explaining store-locator mechanics.
**Recommend the user still eyeball both live pages once this is published** — if the
"Starbucks-Standorte nach Stadt" section on the root pillar page keeps growing, that specific
section is the one at highest risk of drifting into this page's territory, not the reverse.

**Internal links:**
- "Starbucks in deiner Nähe finden" → `/starbucks-in-meiner-naehe`
- "Schnellste Wege zur nächsten Filiale" → `/blog/starbucks-near-me`
- "vollständige Starbucks Preise Übersicht" → `/` (site convention, used on the near-me page)

## FAQ source map

Sourced from genuine fan-out gaps (none of the 4 competitors answer these clearly):
count as of a specific date, state ranking, who owns/runs the brand in Germany, first
store date/city, whether every state has a location, franchise/opening-your-own-store
question (answered briefly + pointed elsewhere since it's a different intent), city
totals, growth trend, difference between company-run vs licensed locations, where to find
a live/current list.
