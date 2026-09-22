# Research notes — "starbucks kapseln angebot"

## Step 1 — Intent + SERP analysis

**Dominant intent:** *buy/commercial* (finding current deals/prices on Starbucks capsules) with a strong *know-simple* secondary thread (which machine system they fit, what varieties exist).

**SERP composition** (query: "starbucks kapseln angebot", plus fan-out "starbucks kaffeekapseln angebot sorten test vergleich nespresso dolce gusto", "starbucks kapseln erfahrungen kaufen günstig sorten"):
- Retail/marketplace listings dominate: eBay.de, Kaufland.de, Rossmann.de (JS-wall, no content) — not content competitors, skipped.
- Deal-aggregator content: `aktionspreis.de` (two pages: 12-Stück and Nespresso 10-Stück variants — same domain, one used).
- Direct topical competitor: `starbuckspreise.de` (different TLD/site, same "Starbucks prices" niche as this site) with a dedicated "Nespresso Kapseln Angebot" page.
- Specialist capsule retailer: `tuttocialde.de` (Starbucks-by-Nespresso product page with pricing/intensity/compatibility data).
- Comparison content seen in SERP but unreachable: `vergleich.org/starbucks-kapseln/` ("Test & Vergleich Top 9").
- Official brand page seen: `dolce-gusto.de/kapseln/starbucks` (blocked) and `starbucksathome.com` (Austria domain, fetched — used as Step 2 source, not counted as a competitor since it's the brand's own page).
- No featured snippet/PAA block surfaced directly by the search tool; fan-out reconstructed from `starbuckspreise.de`'s own FAQ block (compatibility, sale frequency, best pricing) plus query variants.

**Query fan-out used as FAQ/PAA proxy:**
- "für welche Maschine sind Starbucks Kapseln" / Nespresso vs. Dolce Gusto
- "wer stellt Starbucks Kapseln her"
- "starbucks kapseln vertuo kompatibel"
- "starbucks kapseln preis pro stück"
- "wann gibt es starbucks kapseln im angebot"
- "starbucks kapseln günstig kaufen"
- "starbucks kapseln großpackung 80 120"
- "starbucks kapseln sorten"
- "starbucks kapseln entkoffeiniert"
- "starbucks kapseln intensität"
- "starbucks kapseln aluminium recycling"

## Step 2 — Head-entity research (non-competitor sources)

- **Starbucks Corporation** — Org. `sameAs: https://de.wikipedia.org/wiki/Starbucks` (already used sitewide).
- **Nestlé S.A.** — Org. `sameAs: https://de.wikipedia.org/wiki/Nestlé`. Verified via search (SEC 8-K filings, Nestlé/Starbucks press releases): on **7 May 2018** Starbucks and Nestlé announced the **Global Coffee Alliance**; the deal closed **28 August 2018**. Nestlé paid **$7.15 billion** for the **perpetual global license** to market, sell and distribute Starbucks, Seattle's Best Coffee, Starbucks Reserve, Teavana, Starbucks VIA and Torrefazione Italia packaged coffee/tea in all at-home and away-from-home retail channels worldwide (excludes ready-to-drink). This is *why* Starbucks-branded capsules exist for Nespresso and Dolce Gusto machines — neither competitor page explains this.
- **Nespresso** — Brand/Org, Nestlé subsidiary. `sameAs: https://de.wikipedia.org/wiki/Nespresso`. Founded 1986, Vevey (Switzerland). "Original Line" capsule format — the format Starbucks capsules use; NOT compatible with the newer **Nespresso Vertuo** line.
- **NESCAFÉ Dolce Gusto** — Brand, Nestlé/Nescafé. `sameAs: https://en.wikipedia.org/wiki/Dolce_Gusto` (no distinct German-language article found under a different title; recorded with the English URL rather than guessing a German one). Launched 2006. Separate, incompatible capsule format from Nespresso; machines made by Krups/De'Longhi.
- Confirmed via `starbucksathome.com/at/produkte/...` (official, fetched): current Dolce Gusto varieties carrying the Starbucks name — Madagascar Vanilla Macchiato (Blonde Roast), White Mocha (Dark Roast), House Blend Grande (Medium Roast), Caramel Macchiato (Medium Roast).

## Step 4 — Competitor fetches

Target: 4 distinct-domain organic competitors.

| # | Domain | Result |
|---|---|---|
| 1 | vergleich.org/starbucks-kapseln/ | **Blocked (403)** — skipped, substituted |
| 2 | coffeefriend.de/.../starbucks-kaffee-kapseln/ | **Blocked (403)** — skipped, substituted |
| 3 | kapsel-kaffee.net/.../starbucks-kaffeekapseln-fuer-nespresso-maschinen-im-test/ | **Blocked (403)** — skipped, substituted |
| 4 | dolce-gusto.de/kapseln/starbucks | **Blocked (403)** — skipped, used starbucksathome.com instead for official data |
| 5 | rossmann.de/.../starbucks/... | **JS wall** (client-side error page, no content) — skipped |
| 6 | kaufland.de/t/kaffeekapseln/starbucks-kapseln/ | **Blocked (403)** — skipped |
| 7 | frag-mutti.de/kaffeekapseln-test-vergleich-.../ | **Blocked (403)** — skipped |
| 8 | idealo.at/preisvergleich/... | **Fetch failed** (tool error) — skipped |
| 9 | aktionspreis.de/angebote/starbucks-kapseln-12-stueck | ✅ Fetched |
| 10 | starbuckspreise.de/starbucks-nespresso-kapseln-angebot/ | ✅ Fetched |
| 11 | tuttocialde.de/starbucks-kapseln-von-nespresso | ✅ Fetched |
| 12 | roastmarket.de/magazin/kaffeekapsel-test/ | ✅ Fetched, but **no Starbucks products mentioned at all** — used only as supplementary market-context (waste/ownership stats), not counted as a Starbucks-specific competitor |

**No browser-tool fallback was available in this run** (Chrome extension not connected) — per pipeline rule, failures were substituted with the next-ranking distinct domain rather than fabricated. Net: **3 usable Starbucks-specific competitor pages** (rather than 4) after 8 substitution attempts; proceeding with 3 rather than continuing to burn attempts on a long tail of blocked German retail/review domains. Flagged here rather than inventing a 4th.

### Per-competitor extraction

**aktionspreis.de** ("Aktuelle Starbucks Kapseln Angebote", live tracker, page date 22.09.2026) — headings: Alternative Produkte, Prospekte in der Nähe, Entwicklung der Aktionspreise, Weitere Produkte von Starbucks, Starbucks Kapseln Sorten, Aktuelle TOP-Händler, Aktuelle Angebote, Das könnte Sie auch interessieren, Fehler melden — 9 total.
- terms/entities: Aktionspreis, Preisverlauf, Selgros, Tegut, Dolce Gusto, Dallmayr Capsa, Nespresso, Jacobs, 12-Stück-Packung — 9 total.
- Price-history table (Q3 2024 3,65€ → Q2 2026 3,95€, quarterly) — used as the information-gain data point.

**starbuckspreise.de** ("Starbucks Nespresso Kapseln Angebot – Die besten Deals in Deutschland 2026") — headings: Was sind Starbucks Nespresso Kapseln?, Wo kaufen in Deutschland, Beliebte Sorten, Preisvergleich, FAQ — 5 total.
- terms/entities: Nestlé, Original Line, Arabica, Amazon.de, REWE Online, EDEKA24, MediaMarkt, Saturn, Nespresso Shop, Lidl, Aldi, dm, Rossmann, Blonde Espresso Roast, House Blend, Pike Place Roast, Espresso Roast — 17 total.
- FAQ (verbatim topics, reused below): compatibility (Original Line only), sale frequency (Black Friday, Prime Day, Christmas, Easter, supermarket promos), best pricing (online + supermarket promos).
- Price table: 10 Kapseln 3,49€ regulär / ab 2,99€ Angebot; 80 Kapseln 27,99€/ab 21,99€; 120 Kapseln 41,99€/ab 34,99€. "bis zu 25%" Ersparnis.

**tuttocialde.de** ("STARBUCKS® Kapseln von Nespresso®") — headings: STARBUCKS® by Nespresso® Kapseln, Kompatibilität mit Kaffeemaschinen, STARBUCKS® Kapseln by Nespresso® — 3 total.
- terms/entities: Probierset (70 Kapseln, 26,50€), Sonderangebot (160 Kapseln, 48€→39,99€), Blonde Espresso-Roast (Intensität 6), Ristretto Shot (Intensität 11), Breakfast Blend (Intensität 7), Chocolate Hazelnut (Intensität 5), House Blend (Intensität 8), Caffè Verona (Intensität 10), Decaf, Colombia, Guatemala, Sumatra (Single-Origin), Italian Roast, Creamy Vanilla, Smooth Caramel, Lattissima One, Essenza Mini, Pixie, Citiz, U, Inissia — 20 total.
- Price-per-capsule: 0,42€ (10er) / 0,408€ (120er). Seit 2005, >2,5 Mio. Bestellungen, 17 Bewertungen (5,0).

## Step 6 — Entity ledger + tiers

| Canonical | Type | Kind | sameAs | Competitor count | In title/H2 | Tier |
|---|---|---|---|---|---|---|
| Starbucks | Organization | entity | de.wikipedia.org/wiki/Starbucks | 3/3 | yes | 1 |
| Starbucks Kapseln (umbrella) | Product | term | — | 3/3 | yes | 1 |
| Angebot / Rabatt / Preis | Concept/Money | term | — | 3/3 | yes | 1 |
| Nespresso (Original Line) | Organization/Product | entity | de.wikipedia.org/wiki/Nespresso | 3/3 | yes | 1 |
| NESCAFÉ Dolce Gusto | Product | entity | en.wikipedia.org/wiki/Dolce_Gusto | 2/3 (+ official) | yes | 1 |
| Nestlé | Organization | entity | de.wikipedia.org/wiki/Nestlé | 2/3 (+ official) | no | 2 |
| Sorten/Röstungen (Blonde Espresso, House Blend, Pike Place, Caffè Verona, Ristretto, Chocolate Hazelnut …) | Product | term | — | 3/3 | no | 1 |
| Intensität (Skala) | Metric | term | — | 1/3 | no | 2 |
| Preis pro Kapsel (~0,30–0,50 €) | Money | term | — | 3/3 | yes | 1 |
| Multipack / Großpackung (80/120 Stück) | Product | term | — | 2/3 | no | 2 |
| Händler (Amazon, REWE, EDEKA, Lidl, Aldi, dm, Rossmann, Kaufland, Selgros, Tegut, Marktkauf) | Organization | entity (list, unlinked) | — | 3/3 | no | 2 |
| Preisverlauf/Preishistorie (Aktionspreis-Tracker) | Metric | term | — | 1/3 | no | 2 |
| Nespresso Vertuo | Product | entity (unlinked) | — | 0/3 (Step 2 clarification) | no | 2 |
| Rabattzeiträume (Black Friday, Prime Day, Weihnachten, Ostern) | Event | term | — | 1/3 | no | 2 |
| Decaf/Entkoffeiniert | Product | term | — | 2/3 | no | 3 |
| Global Coffee Alliance (Starbucks–Nestlé, 2018, 7,15 Mrd. USD) | Event | entity (unlinked) | — | 0/3 (Step 2 only) | no | 1 |
| Aluminiumkapsel/Recycling | Concept | term | — | 1/3 | no | 3 |
| Kompatible Maschinen (Lattissima, Essenza, Pixie, Citiz, Inissia / Krups, De'Longhi) | Product | term | — | 1/3 | no | 3 |

**Relationships (triples):**
- Starbucks — lizenziert Verpackungsprodukte an → Nestlé (Global Coffee Alliance, 7,15 Mrd. USD, geschlossen 28.8.2018)
- Nestlé — produziert → Starbucks-Kapseln für Nespresso Original Line und NESCAFÉ Dolce Gusto
- Nespresso Original Line — kompatibel mit → Lattissima/Essenza/Pixie/Citiz/Inissia-Maschinen, NICHT mit Vertuo
- NESCAFÉ Dolce Gusto — kompatibel mit → eigene Krups/De'Longhi-Dolce-Gusto-Maschinen, NICHT mit Nespresso
- Starbucks-Kapsel (Nespresso) — kostet pro Stück → ca. 0,30–0,50 € (je nach Packungsgröße/Angebot)
- Aktionspreis.de-Tracker — zeigt Durchschnittspreis (12er-Packung) → 3,95 € (Q2 2026), gestiegen von 3,65 € (Q3 2024)
- Starbucks-Kapseln — im Angebot am günstigsten bei → Supermarkt-Aktionen und Black-Friday/Prime-Day-Rabatten

**Dedupe log:**
- "Kaffeekapseln" / "Kapseln" folded into canonical "Starbucks Kapseln".
- "Aktionspreis"/"Rabatt"/"Angebot"/"Deal" folded into one tier-1 concept row.
- General capsule-market sustainability stats from roastmarket.de (5.000 t Kapselmüll 2015, 13%→30% Haushaltsbesitz, 3,4 Mrd. Kapseln/Jahr) parked — not Starbucks-specific, no verified more-recent figure found; mentioned only briefly as context, not built into a dedicated section, since roastmarket.de doesn't cover Starbucks products at all.
- Individual product-line names not carrying Starbucks branding (Lavazza, J. Hornig, Kimbo, etc. from roastmarket.de) dropped entirely — off-topic for a Starbucks-branded page.

Tier-1 sanity check against Step 1 intent: buyer intent keyword ("angebot") — Preis/Angebot, the two machine systems (so buyers don't purchase the wrong capsule type), and the varieties are correctly weighted tier 1; the corporate-history relationship (Nestlé license) is tier 1 because it's the single biggest information-gain fact and directly explains the product's existence, which no competitor states.

## Step 7 — Information-gain pass

None of the 3 fetched competitors:
1. Explain **why** Starbucks capsules exist at all — the Nestlé license (Global Coffee Alliance, 2018) is never mentioned by any of them.
2. Give a clear **Nespresso vs. Dolce Gusto compatibility table** side by side — starbuckspreise.de only covers Nespresso; tuttocialde.de only covers Nespresso; the Dolce Gusto side is only documented on the (blocked) dolce-gusto.de and the official starbucksathome.com product page.
3. Combine **price-per-capsule math** across pack sizes with **real historical pricing data** (aktionspreis.de has the price history but no variety/compatibility info; starbuckspreise.de and tuttocialde.de have pricing but no history).

**Committed information-gain element:** a Nespresso-vs-Dolce-Gusto compatibility comparison table (which machines, which varieties, which is NOT interchangeable with the other) plus a short "Warum gibt es Starbucks-Kapseln?" explainer box citing the Nestlé license — content no single competitor page has all of.

## Step 8 — Heading + keyword + question map

| Level | Heading | Focus/LSI phrase | Question answered | Tier-1/2 carried |
|---|---|---|---|---|
| H1 | Starbucks Kapseln Angebot: Preise, Sorten & die besten Deals 2026 | starbucks kapseln angebot (focus) | — | Starbucks Kapseln, Angebot/Preis |
| — | Direct-answer block | — | Was kosten Starbucks Kapseln und wo gibt es sie im Angebot? | Preis pro Kapsel, Nestlé, Händler |
| H2 | Was sind Starbucks Kapseln – und wer stellt sie eigentlich her? | starbucks kapseln nestlé | Wer produziert die Starbucks Kapseln? | Nestlé, Global Coffee Alliance |
| H2 | Nespresso oder Dolce Gusto – welches System passt zu welcher Maschine? | starbucks kapseln nespresso dolce gusto | Für welche Kapselmaschine sind Starbucks Kapseln geeignet? | Nespresso, Dolce Gusto, Vertuo |
| H3 | Starbucks für Nespresso Original Line | starbucks nespresso kapseln | Sind Starbucks Kapseln mit Nespresso Vertuo kompatibel? | Nespresso, Vertuo |
| H3 | Starbucks für NESCAFÉ Dolce Gusto | starbucks dolce gusto kapseln | Welche Starbucks-Sorten gibt es für Dolce Gusto? | Dolce Gusto, Sorten |
| H2 | Welche Sorten und Röstungen gibt es? | starbucks kapseln sorten | Welche Geschmacksrichtungen gibt es? | Sorten, Intensität, Decaf |
| H2 | Was kostet eine Starbucks Kapsel? | starbucks kapseln preis | Wie viel kostet eine Starbucks Kapsel im Schnitt? | Preis pro Kapsel, Multipack |
| H2 | Wann und wo gibt es die besten Starbucks Kapseln Angebote? (Info-Gain: Preisverlauf) | starbucks kapseln angebot günstig | Wann lohnt sich der Kauf am meisten? | Rabattzeiträume, Preisverlauf, Händler |
| H2 | Nachhaltigkeit: Aluminium, Recycling & Entkoffeiniert | starbucks kapseln nachhaltigkeit | Sind Starbucks Kapseln recycelbar? | Aluminiumkapsel, Decaf |
| H2 | Häufig gestellte Fragen | — | (FAQ) | — |

Heading list read alone conveys: what it is/who makes it → which machine it fits → varieties → price → when/where to catch a deal → sustainability. Core-before-outer respected (product identity + machine-fit + price before the sustainability/decaf tail section).

## Step 8e — Internal-link plan

No existing page on this site covers capsules/offers — this is the canonical new home for the "Angebote & Kapseln" pillar, no cannibalisation risk found in the Content_Calendar for this exact keyword.

- "Starbucks Preise" (drink menu) → `/` (from the intro/price section)
- "Starbucks Menu 2026" → `/blog/starbucks-menu` (from the "was sind Starbucks Kapseln" intro, as the packaged-goods vs. in-store-menu disambiguation)
- "Starbucks Becher" → `/blog/starbucks-becher` (from the sustainability section — both cover Starbucks' reusable/recycling angle)
- "Starbucks in meiner Nähe" → `/starbucks-in-meiner-naehe` (from the "wo kaufen" context, for readers who'd rather just visit a store)
- Inbound: add a link to the new page from `blog/starbucks-menu.html` (packaged-goods/at-home section) and `blog/starbucks-becher.html` (sustainability section) where it fits naturally.

## FAQ source map

1. "Für welche Kapselmaschinen gibt es Starbucks Kapseln?" — SERP fan-out + Step 2/6.
2. "Wer produziert die Starbucks Kapseln?" — Step 2 (Nestlé license), not stated by any competitor.
3. "Sind Starbucks Nespresso Kapseln auch für Nespresso Vertuo geeignet?" — tuttocialde.de + Step 2.
4. "Wie viel kostet eine Starbucks Kapsel im Schnitt?" — tuttocialde.de (0,42€/0,408€) + starbuckspreise.de (2,99€/10=0,30€).
5. "Wann gibt es die besten Angebote für Starbucks Kapseln?" — starbuckspreise.de FAQ, verbatim topic.
6. "Wo finde ich aktuell die günstigsten Starbucks Kapseln?" — aktionspreis.de (händler + tracker) + starbuckspreise.de (Händlerliste).
7. "Lohnt sich eine Großpackung mit 80 oder 120 Kapseln?" — starbuckspreise.de + tuttocialde.de price tables.
8. "Welche Sorten (Röstungen) gibt es bei Starbucks Kapseln?" — tuttocialde.de + starbucksathome.com.
9. "Gibt es entkoffeinierte Starbucks Kapseln?" — WebSearch summary (110er-Set) + tuttocialde.de (Decaf options).
10. "Wie stark sind Starbucks Kapseln im Vergleich zu anderen Marken?" — tuttocialde.de intensity scale.
11. "Wie hat sich der Preis für Starbucks Kapseln zuletzt entwickelt?" — aktionspreis.de price-history table, genuine information-gain follow-up.
12. "Sind Starbucks-Kapseln aus Aluminium recycelbar?" — tuttocialde.de (Aluminiumkapsel) + general, well-established Nespresso aluminum-recycling program (stated generally, no invented statistic).
