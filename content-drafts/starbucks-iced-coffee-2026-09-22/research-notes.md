# Research notes — starbucks iced coffee

## Step 1 — Intent + SERP analysis

Query: `starbucks iced coffee` (390 vol, KD 22, Informational+Transactional, target market Germany/de-DE).

Mixed SERP: the exact US-branded product ranks alongside German menu/price aggregators and
comparison articles. Two clusters:
- English "menu clone" sites (starbucksxmenu.com, starbucksreserveonly.com, starbucksmenu.us,
  starbucksmenuus.info, bucksmenu.store) — US prices/calories, templated.
- German price aggregators (speisekartemenus.de) and general comparison content
  (cold brew vs iced coffee vs Americano).

**Search intent:** dominant = *know* (what is it, is it on the German menu), secondary = *buy*
(price, where to get it). Germans searching this English phrase are mostly asking "does this
exist here and what's the closest thing / what does it cost", not just "what is iced coffee."

**SERP features:** no featured snippet observed directly; PAA-style questions inferred from
competitor FAQ blocks (see Step 4). No knowledge panel, no local pack (not a location query),
no video pack.

**Query fan-out** (from Content_Calendar `Merge-Recommended (planned starbucks-iced-coffee post)`
rows + related searches):
- `starbucks iced` (260 vol, KD22, Transactional)
- `iced caffe latte starbucks` (170 vol, KD24, Informational)
- `starbucks ice coffee` (110 vol, KD21, Transactional — typo variant)
- related: iced coffee vs cold brew, iced coffee vs iced americano, starbucks iced coffee kalorien,
  starbucks iced coffee preis

## Step 2 — Head-entity research (non-competitor)

- **Starbucks Iced Coffee** (Product/Concept, unlinked — no single Wikipedia article, general
  concept page exists at https://en.wikipedia.org/wiki/Iced_coffee). Per Starbucks' own US menu:
  hot-brewed coffee, chilled and served unsweetened over ice; "notes of malted milk chocolate and
  brown-sugar sweetness" (starbucks.com/menu/product/2123863/iced). Suggested home ratio: 3 Tbsp
  coffee per 6 fl oz water, poured hot over ice to chill.
- **Starbucks Corporation** (Organization) — sameAs https://de.wikipedia.org/wiki/Starbucks
  (reused from the kapseln-angebot piece, same head entity).
- **Confirmed directly on starbucks.de** (`/de/menu-drinks-iced-coffees`, fetched live
  2026-09-22): the German café menu's "Iced Coffees" category lists **Cold Brew, Cold Brew Latte,
  Iced Latte Macchiato, Iced Cappuccino, Iced Latte, Iced Caramel Macchiato, Iced White Mocha,
  Iced Mocha, Iced Americano** — a plain "Iced Coffee" as sold in the US **is not a listed
  drink on the German menu**. This is the single most important fact for this piece and the
  thing no competitor states plainly for a German audience.
- **Starbucks Doubleshot® Iced Coffee** — a canned/bottled ready-to-drink (RTD) product, sold at
  German retailers (Flink, Kaffeegemeinde, Interspar/AT) confirmed via live search. RTD Starbucks
  products (Doubleshot, Frappuccino bottles) are made under the **North American Coffee
  Partnership (NACP)**, a joint venture between Starbucks and **PepsiCo** dating to 1994,
  extended to PepsiCo Europe for the European market (pepsico.com press release 2009;
  pepsicopartners.com brand page). This is a **different** corporate partner from the Nestlé
  Global Coffee Alliance that makes the Starbucks capsules covered in the sibling
  `starbucks-kapseln-angebot` post — Nestlé = at-home packaged/capsules, PepsiCo/NACP = RTD
  cans/bottles. Useful contrast for cross-linking and reader value.

## Step 3 — Title + metadata set

- **Title (primary):** "Starbucks Iced Coffee: Gibt es das in Deutschland? Preis & Alternativen 2026" (~63 char)
- **Alt 1:** "Starbucks Iced Coffee Deutschland: Was steckt dahinter?"
- **H1:** "Starbucks Iced Coffee in Deutschland: Was es wirklich ist und was es kostet"
- **Meta description (~150 char):** "Starbucks Iced Coffee: In den USA ein eigenes Getränk, in Deutschland nicht auf der Karte. Die echten Alternativen, Preise und Kalorien im Überblick."
- **URL slug:** `starbucks-iced-coffee`
- **OG title/description:** mirror title + meta.

## Step 4 — Competitors fetched (top 4, distinct domains)

1. **starbucksxmenu.com/starbucks-iced-coffee/** — US menu-clone. H2s: What Is Starbucks Iced
   Coffee?, Popular Varieties, Prices 2026, Calories, Nutrition Facts (Grande), Caffeine Levels,
   Menu Highlights, New Innovations 2026, How to Order Healthier, FAQs, Final Thoughts. USD price
   table (Tall $1.95–4.63 / Grande $2.45–4.95 / Venti $2.95–5.17 / Trenta $3.45–5.39). Calorie: 0
   sugar/fat/carbs. Caffeine 165–185mg Grande, ~235mg Trenta. FAQ (5 questions, verbatim below).
2. **starbucksreserveonly.com/starbucks-iced-coffee/** — US content site. H2s: Why It's a Go-To,
   What Is It Made Of, Taste Review, Price 2026, Calories & Nutrition, **vs Cold Brew**, **vs
   Iced Americano**, Is It Strong Enough, Best/Worst Occasions, Customize, Pros/Cons, FAQs.
   Price table Tall $3.95/Grande $4.45/Venti $4.95/Trenta $5.45. Nutrition table: Calories
   5/5/10, Sugar 0g, Carbs 0g, Caffeine 120/165/235mg (Tall/Grande/Venti). FAQ (10 questions,
   verbatim below).
3. **speisekartemenus.de/starbucks-preise/** — German price aggregator, no exact "Iced Coffee"
   term used, but real **EUR** prices for the closest German-menu drinks: Iced Caffè Latte
   €3.99–4.99, Iced Vanilla Latte €4.49–5.49, Iced Caramel Macchiato €4.79–5.79, Iced Caffè
   Mocha €4.79–5.79, **Iced Americano €3.39–4.39**. One FAQ: "Wie teuer ist ein Kaffee bei
   Starbucks 2026?"
4. **groundstobrew.com/starbucks-iced-coffee-versus-cold-brew/** (published 2022-02-21, still
   ranking) — dedicated Iced-Coffee-vs-Cold-Brew comparison. 9-point breakdown: blend/flavor
   (caramel+cola vs chocolate+citrus), brew temp (near-boiling vs room temp), brew time (minutes
   vs ~20h), body (medium vs full/syrupy), acidity/sweetness, serving (Classic syrup 80 cal
   Grande vs plain 5 cal Grande), caffeine (Grande cold brew 205mg, Nitro 285mg, iced coffee
   165mg), decaf availability, price (~$3.45 vs ~$4.25, Nitro +$1). FAQ: 2 questions (verbatim
   below).

**Fetch failures, substituted:** bucksmenu.store/iced-coffee/ → 404; starbucksmenuus.info →
HTTP 520; starbucksmenu.us/iced-coffee-menu/ → 403. Official Starbucks "Coffee Science" story
(about.starbucks.com, 2026, Iced Americano/Cold Brew/Iced Coffee explainer) → 403, blocked;
its content is only known via the WebSearch snippet summary (used as general-knowledge
confirmation, not quoted verbatim, and not counted as one of the 4 fetched competitors).

## Step 5 — Entity + term extraction (per competitor, by heading)

### starbucksxmenu.com
| term/entity | type | canonical | kind |
|---|---|---|---|
| Starbucks Iced Coffee | Product | Starbucks Iced Coffee | entity |
| Iced Caffè Latte | Product | Iced Caffè Latte | entity |
| Iced Caramel Macchiato | Product | Iced Caramel Macchiato | entity |
| Grande / Tall / Venti / Trenta | Metric | Cup size | term |
| calories | Metric | Kalorien | term |
| caffeine | Metric | Koffein | term |
| 2026 pricing | Date/Money | Preis 2026 | term |
Numbers/stats: 1.95, 4.63, 2.45, 4.95, 2.95, 5.17, 3.45, 5.39, 165, 185, 235, 130
Contextual words: refreshing, unsweetened, cold, brewed, customizable, protein-enhanced, viral, seasonal
Count: 12

### starbucksreserveonly.com
| term/entity | type | canonical | kind |
|---|---|---|---|
| Starbucks Iced Coffee | Product | Starbucks Iced Coffee | entity |
| Cold Brew | Product | Cold Brew | entity |
| Iced Americano | Product | Iced Americano | entity |
| Tall/Grande/Venti/Trenta | Metric | Cup size | term |
| sugar/carbs/calories | Metric | Nährwerte | term |
| caffeine mg | Metric | Koffein | term |
Numbers/stats: 3.95, 4.45, 4.95, 5.45, 5, 10, 0, 120, 165, 235
Contextual words: watery, smooth, light, overpriced, affordable, strong, customize, pros, cons
Count: 9

### speisekartemenus.de
| term/entity | type | canonical | kind |
|---|---|---|---|
| Iced Caffè Latte | Product | Iced Caffè Latte | entity |
| Iced Vanilla Latte | Product | Iced Vanilla Latte | entity |
| Iced Caramel Macchiato | Product | Iced Caramel Macchiato | entity |
| Iced Caffè Mocha | Product | Iced Caffè Mocha | entity |
| Iced Americano | Product | Iced Americano | entity |
| Tall/Grande/Venti | Metric | Cup size | term |
Numbers/stats: 3.99, 4.99, 4.49, 5.49, 4.79, 5.79, 3.39, 4.39
Contextual words: Preisliste, teuer, 2026
Count: 8

### groundstobrew.com
| term/entity | type | canonical | kind |
|---|---|---|---|
| Starbucks Iced Coffee | Product | Starbucks Iced Coffee | entity |
| Cold Brew | Product | Cold Brew | entity |
| Nitro Cold Brew | Product | Nitro Cold Brew | entity |
| Classic Syrup | Product | Classic Syrup | entity |
| brewing temperature | Process | Brühtemperatur | term |
| brewing time | Process | Brühzeit | term |
| body/acidity/sweetness | Concept | Körper/Säure/Süße | term |
Numbers/stats: 205, 285, 165, 80, 5, 3.45, 4.25, 12, 24, 20
Contextual words: caramel, cola, chocolate, citrus, full-bodied, syrupy, room-temperature, decaf
Count: 8

## Step 6 — Entity map + tiering

| canonical | type | aliases | sameAs | kind | competitor_count | in_title_or_h2 | tier |
|---|---|---|---|---|---|---|---|
| Starbucks Iced Coffee | Product | iced coffee, starbucks ice coffee | https://en.wikipedia.org/wiki/Iced_coffee | entity | 4 | yes | 1 |
| Cold Brew | Product | — | — | entity | 3 (starbucksreserveonly, groundstobrew, DE menu) | yes | 1 |
| Iced Americano | Product | — | — | entity | 3 (starbucksreserveonly, speisekartemenus, DE menu) | yes | 1 |
| Preis / Kosten | Money | price | — | term | 4 | yes | 1 |
| Starbucks (Corp) | Organization | Starbucks Corporation | https://de.wikipedia.org/wiki/Starbucks | entity | 4 (implicit) | yes | 1 |
| Nicht auf der deutschen Karte | Concept | unavailable in Germany | — | term | 0 (own research, not a competitor claim) | no | 1 |
| Kalorien / Koffein | Metric | calories, caffeine | — | term | 3 | no | 2 |
| Iced Caffè Latte | Product | — | — | entity | 2 (starbucksxmenu, speisekartemenus + DE menu) | yes | 2 |
| Starbucks Doubleshot Iced Coffee | Product | Doubleshot | — | entity | 0 (own research; genuine info-gain) | no | 2 |
| PepsiCo / North American Coffee Partnership | Organization | NACP | https://de.wikipedia.org/wiki/PepsiCo | entity | 0 (own research) | no | 2 |
| Nestlé (contrast) | Organization | — | https://de.wikipedia.org/wiki/Nestlé | entity | 0 (own research, cross-link) | no | 2 |
| Brühmethode (heiß vs. kalt) | Process | brewing method | — | term | 2 (starbucksreserveonly, groundstobrew) | no | 2 |
| Iced Caramel Macchiato | Product | — | — | entity | 2 | no | 3 |
| Grande/Tall/Venti/Trenta | Metric | cup sizes | — | term | 3 | no | 3 |
| Nitro Cold Brew | Product | — | — | entity | 1 | no | 3 |

**Relationships (backbone):**
- Starbucks Iced Coffee —is brewed hot, then cooled and served over→ Eis (unsweetened base)
- Deutsche Starbucks-Filialen —führen keine eigenständige→ "Iced Coffee"-Position
- Iced Americano —ist die nächstliegende Alternative zu→ Starbucks Iced Coffee (in Deutschland)
- Cold Brew —wird kalt extrahiert über→ 20 Stunden (kein Hitzeeinsatz)
- Starbucks Doubleshot Iced Coffee —wird hergestellt von→ PepsiCo (North American Coffee Partnership, seit 1994)
- Starbucks Kapseln (Sibling-Artikel) —werden hergestellt von→ Nestlé (Global Coffee Alliance, 2018)
- Iced Caffè Latte —kostet in Deutschland→ 3,99–4,99 €
- Iced Americano —kostet in Deutschland→ 3,39–4,39 €

**Dedupe log:** "starbucks iced" and "starbucks ice coffee" (fan-out) folded into the main
keyword/entity (same intent, typo/truncation variants) — not separate sections. "iced caffe
latte starbucks" folded into the Iced Caffè Latte tier-2 mention. Frappuccino (appeared in one
SERP snippet) parked out-of-scope — distinct product family, already covered contextually on
`starbucks-frappuccino-sorten`, not duplicated here.

## Step 7 — Information-gain pass

All 4 competitors (and every English "menu clone" site behind them) present **US menu/prices**
as if globally applicable, without ever checking whether "Iced Coffee" is actually a menu item
outside the US. None mention that the German Starbucks menu has no plain "Iced Coffee" listing,
none mention the Doubleshot RTD can as the actual retail product Germans can buy under that name,
and none mention the PepsiCo/NACP vs Nestlé licensing split.

**Original element committed:** a direct comparison table — "Was es in den USA ist" vs. "Was es
in Deutschland gibt" — plus the Doubleshot-RTD-via-PepsiCo fact, tying back to the sibling
capsules article's Nestlé fact for a clean "two different corporate partners, two different
product categories" explainer no competitor offers.

## Step 8 — Heading architecture

| level | heading | focus/LSI phrase | question answered | tier-1/2 carried |
|---|---|---|---|---|
| H1 | Starbucks Iced Coffee in Deutschland: Was es wirklich ist und was es kostet | starbucks iced coffee | what is it / does it exist here | Iced Coffee, Starbucks |
| — | Direct-answer block | — | one-line answer | Iced Coffee, Iced Americano, Preis |
| H2 | Gibt es "Iced Coffee" auf der Starbucks-Karte in Deutschland? | starbucks iced coffee deutschland | is it on the German menu | Nicht auf der Karte, Cold Brew, Iced Americano |
| H3 | Die nächstliegenden Alternativen: Iced Americano und Cold Brew | starbucks iced / cold brew | what to order instead | Iced Americano, Cold Brew |
| H2 | Starbucks Doubleshot Iced Coffee: die Dose aus dem Supermarkt | starbucks doubleshot iced coffee | where to actually buy "iced coffee" branded | Doubleshot, PepsiCo |
| H2 | Was kostet ein Iced Coffee bei Starbucks? | starbucks iced coffee preis | how much does it cost | Preis, Iced Caffè Latte |
| H3 | Iced Coffee vs. Cold Brew vs. Iced Americano im Preisvergleich | starbucks ice coffee | price comparison | Preis, Cold Brew, Iced Americano |
| H2 | Kalorien und Koffein: wie stark ist Iced Coffee wirklich? | starbucks iced coffee kalorien | calories/caffeine | Kalorien, Koffein |
| H2 | Iced Coffee, Cold Brew oder Iced Americano: der Unterschied in der Zubereitung | iced caffe latte starbucks (adjacent) | brewing difference | Brühmethode, Cold Brew |
| H2 | Häufig gestellte Fragen | — | FAQ | all |

## Step 8e — Internal-link plan

- `starbucks-kaffee.html` (Cold Brew section, ~line 333) → inbound link to this new page.
- `starbucks-preise.html` → inbound link (price comparison context).
- `starbucks-menu.html` → inbound link (already links out to sibling drink pages).
- `starbucks-kapseln-angebot.html` → inbound + outbound link (Nestlé/PepsiCo contrast, both
  "packaged Starbucks product made by a licensing partner" pieces).
- Outbound from new page: starbucks-kaffee, starbucks-preise, starbucks-menu,
  starbucks-kapseln-angebot, starbucks-getraenke.
- **Cannibalisation check:** no existing page already targets "starbucks iced coffee" or its
  fan-out (`starbucks-iced`, `iced caffe latte starbucks`, `starbucks ice coffee`) — confirmed
  against Content_Calendar; `iced-caramel-macchiato` is a separate, already-published page for a
  different specific drink, not a duplicate of this one.

## FAQ source map

Sourced from competitor FAQs (reused verbatim where the question itself is generic, translated
to German where German-audience-specific), PAA-style gaps, and the genuine "is it available here"
gap:
1. Gibt es Starbucks Iced Coffee in Deutschland? (own research gap — none of the 4 competitors ask this)
2. Was ist der Unterschied zwischen Iced Coffee und Cold Brew? (groundstobrew FAQ)
3. Wie viele Kalorien hat ein Starbucks Iced Coffee? (starbucksxmenu + starbucksreserveonly FAQ)
4. Enthält Starbucks Iced Coffee Koffein? (starbucksreserveonly FAQ)
5. Was ist die nächstliegende Alternative zu Iced Coffee bei Starbucks in Deutschland? (own gap)
6. Wer stellt die Starbucks Doubleshot Iced Coffee Dose her? (own research gap)
7. Ist Starbucks Iced Coffee süß? (starbucksreserveonly FAQ)
8. Was kostet ein Iced Americano bei Starbucks in Deutschland? (speisekartemenus price data)
9. Kann man Starbucks Iced Coffee selbst zu Hause machen? (starbucks.com athome page)
10. Ist Starbucks Iced Coffee gut für eine Diät / kalorienarm? (starbucksreserveonly FAQ)
11. Was ist der Unterschied zwischen Iced Coffee und Iced Americano? (starbucksreserveonly FAQ)
12. Gibt es Starbucks Iced Coffee entkoffeiniert? (groundstobrew "available as decaf" point)
