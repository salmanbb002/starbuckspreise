# Coverage & QA — starbucks-menu (2026-09-21)

**Length:** ~2,420 words total (body ≈1,900 + FAQ) · **FAQ:** 13 (min. 10) · **Direct-answer block:** 44 words (target 40–55; doesn't restate H1; paragraph format).

## Entity coverage (surface-form / paraphrase check against `entities.json`)
- **Tier 1:** 16/16 mentioned (100 %). Attribute/relationship stated for 14/16; **2 thin** — *Heiße Schokolade* (name + category only, no price: none traceable) and *Snacks & Leckereien* (examples only). Not padded with invented numbers.
- **Tier 2:** 10/10 (100 %), all with at least one stated attribute (price delta, date, launch cities, ml, …).
- **Tier 3:** 2/7 used naturally; unused (deliberate): Eggnog Latte, Snack Mints/Gold Coin, Kapseln, Allergene, Gründer/Geschichte — see parked log in `research-notes.md`.
- Note: coverage is a regex proxy for concept presence, not an NLP salience score.

## Heading architecture
One H1 · 8 H2 (7 + FAQ) · 29 H3-level (incl. FAQ questions as H3 on the page) · **no skipped levels** (checked programmatically on the built page). Each H2/H3 owns a distinct phrase; `starbucks getränke` intentionally left to `/blog/starbucks-getraenke` (no heading-level cannibalisation). Read alone, the H2 list gives the logic: structure → drinks → food → extras → price → decide → order → FAQ.
H2 count vs question set: all cluster variants (menü/karte/speisekarte/sortiment/produkte/frühstück/kalte getränke/sorten) map to a section or the hub as a whole.

## Answer-block / QUORA check
Direct answer matches the intent (definition + price range + "no prices on starbucks.de"). Question-style H2s answer in the first sentence. Weakest: H3 "Wie unterscheidet sich die Karte je nach Filiale?" opens with a statement, fine.

## Competitor-heading matrix (4 fetched pages)
| recurring H2 | covered? |
|---|---|
| Heiße Espresso-/Kaffeegetränke | yes (H3, official 14-item list) |
| Frappuccino® | yes |
| Tee / Chai / Matcha, Iced Tea | yes |
| Heiße Schokolade | yes (thin) |
| Sandwiches / Desserts / Snacks / Frühstück | yes (3 H3) |
| Flaschengetränke, Kaffeebohnen | yes |
| Merchandise | short + links (own spokes) |
| Nährwerte / Allergene | decision-table row + link (Nährwerte); Allergene skipped |
| Öffnungszeiten | 1 sentence + link |
| Filialen/Standorte | intro + FAQ |
| Full per-product price tables | **intentionally skipped** — contradictory sources; linked to `/blog/starbucks-preise` |

## Question coverage
PAA / autocomplete **not captured** (see research notes) — mapped: 13 own FAQ + competitor FAQs "Filialen, Zahlung, Lieferservice, vegan, App, Drive-Thru, Preise gleich, Frühstück, reservieren, Eggnog, Nachfüllungen". **Left unanswered:** Zahlungsmöglichkeiten (only one third-party source), reservieren (trivial), Eggnog Latte, Nachfüllungen (US-centric).

## Fact cross-check
| claim | source | status |
|---|---|---|
| Menu categories (Getränke/Essen/To Go/Highlights; 10 drink rubrics) | starbucks.de `/de/menu`, `/en/menu-drinks-categories` | ✔ fetched 2026-09-21 (drink rubric names are the **English** labels of the German site) |
| 14 Hot Coffees items | starbucks.de `/de/menu-drinks-hot-coffees` | ✔ |
| "keine Preise auf den Menüseiten von starbucks.de" | 3 pages fetched, none show prices | ⚠ verified on those pages only; the app/order flow may show prices |
| First stores Berlin May 2002; AmRest since April 2016, Lizenzbasis | de.wikipedia + food-service.de (2024) | ✔ (Wikipedia: "bis April 2016 Starbucks Coffee Deutschland GmbH") |
| ~179 Filialen, 77 Städte, NRW 36 (1 Jul 2026) | own page `starbucks-deutschland-filialen` (ScrapeHero) | ✔ own live page; other lists 154–181 (Statista 154 for 2024 via search snippet, fastfoodsmenu 181) |
| All € price bands in the category table + Größen/Extras/10–15 % | **own** `/blog/starbucks-preise` | ⚠ site's own numbers; **they conflict** with `/blog/starbucks-getraenke` (e.g. Latte ab 4,45 € vs Tall 3,90 €) — see flags |
| 8,50 € top price | Tiramisu Frappuccino 8,50 € (speisekartemenus) + own FAQ "5,40–8,50 €" | ✔ third-party + own |
| Cappuccino 3,90 € vs 5,20–6,20 € on one page | starbuckspreise.de | ✔ as observed 2026-09-21 |
| Saisonal 6,20–7,50 €; PSL/Toffee Nut/Lebkuchen in 2026 lists | speisekartemenus, fastfoodsmenu (summer 6,20–7,40), fastfoodpreis-info FAQ | ⚠ third-party |
| Sandwich 3,20–5,60 €; Muffin bis 3,99 € | speisekartemenus | ⚠ third-party |
| Pike Place 250 g 6,99 €; Single-Origin ~9,90 € | own page + speisekartemenus | ✔ two sources |
| Rewards: 3 Stars/€, 150 Stars, 450 Gold, Nachfüll-Kaffee | starbucks.de/en/app | ✔ |
| Uber Eats since 7 Dec 2021, Frankfurt/Hamburg/München | uber.com/de/newsroom | ✔ (date is launch; current coverage unverified) |
| Pfand 2,50 € grüner Becher; eigener weißer Reusable Cup | starbucks.de article 491 | ✔ (discount amount deliberately omitted — see flags) |
| Venti 591 ml heiß / 709 ml kalt | own pages (getraenke, groessen) | ✔ own |
| Cold Brew ~20 h; Refresha mit Fruchtsaft + Grünkaffee-Extrakt | own `starbucks-getraenke` | ✔ own |
| Innenstadt schließt 19:30–20:30 | own `starbucks-geoeffnet` | ✔ own |
| Bestellen im Voraus in teilnehmenden Filialen | own `starbucks-in-der-naehe` | ⚠ **not on starbucks.de/en/app**; own-site claim only |
| Americano ~15 kcal / Cold Brew ~5 kcal | own `starbucks-getraenke` table (Grande) | ⚠ third-party lists show 11 / 22 kcal — order of magnitude "kaum Kalorien" holds |

## Intent check
Delivers a navigational hub: structure of the whole karte, what's in each category, price bands with honest caveats, a "what should I order" table, and ordering routes. Does **not** try to be the price list (that's `/starbucks-preise`).

## Readability
Short sentences, mostly one idea each; estimated Flesch-DE ≈ 55–65 (grade ~8). Densest passage: the 14-item Hot Coffees list (unavoidable, it is a list in prose).

## E-E-A-T / manual flags (need a human before publishing)
1. **Own-site price conflicts.** `/blog/starbucks-preise` (Latte Tall 3,90 €) vs `/blog/starbucks-getraenke` (Latte ab 4,45 €) and `/blog/starbucks-becher` (own-cup discount **0,50 €**) vs `/blog/starbucks-getraenke` (**30 Cent**). I used the price page's bands and left the discount amount out — but the site itself needs one truth. Also verify against a real Starbucks receipt/app price at least once.
2. **Prices are third-party/own, not official** — starbucks.de publishes none on the menu pages. The category price table says "Richtwert"; don't remove that.
3. **PAA / autocomplete not observed** — check a real German SERP (and snippet format) and adjust H2 phrasing if PAA differs.
4. **Author/E-E-A-T:** author is the site's Organization byline "StarbucksPreise Redaktion" (as on other pages) — no named human, no first-hand claim was fabricated; the draft contains **no** first-person experience lines.
5. **Order-ahead + Drive-Thru + Uber Eats current coverage** rest on own pages / 2021 press note; confirm.
6. **Hero image** reuses `starbucks-getraenke-hero.webp` (site convention: generic hero reuse) — swap for a menu-specific photo if desired.
7. **Schema** is generated, not validated: run Rich Results Test. No TODO placeholders needed (Organization author, no invented URLs).
