# Research notes — starbucks flat white / flat white starbucks coffee

Keyword source: Content_Calendar row "flat white starbucks coffee" (vol 110, KD 27, Informational, Low priority,
FAQ/short-answer post). Merge targets absorbed: "flat white starbucks drink" (vol 110, KD 33) and
"starbucks flat white" (vol 90, KD 23) — both Clean_Keywords rows tagged
`Merge-Recommended (planned flat-white-starbucks-coffee post)`.

## Step 1 — Intent + SERP

- Dominant intent: **know-simple / know** (what is it, price, calories, difference vs. latte/cappuccino).
  Secondary: transactional (price lookup).
- International SERP for "flat white starbucks coffee": athome.starbucks.com/recipe/flat-white,
  starbucks.com/menu/product/565/hot, en.wikipedia.org/wiki/Flat_white, CopyKat recipe clone,
  athome.starbucks.com/caffe-latte-vs-flat-white, starbucks.com iced variant + nutrition pages.
  athome.starbucks.com and starbucks.com are JS-rendered SPAs — WebFetch returned "Parse Error: Header
  overflow" / empty content on every attempt; not usable as fetched sources, so their content is
  referenced only via WebSearch snippets, not quoted as if fetched in full.
- German SERP ("Starbucks Flat White Preis Kalorien Deutschland"): starbuckspreise.de (has a dedicated
  Flat White article), speisekartemenus.de/starbucks-preise (general price list, no dedicated Flat White
  page), fatsecret.de, fddb.mobi (nutrition DBs), supermarktcheck.de (retail can product page).
- No PAA/autocomplete panel available through the search tool used (text-only WebSearch); fan-out inferred
  from the two merged sub-keywords ("flat white starbucks drink", "starbucks flat white") plus the natural
  questions a "what is X" + "what does it cost" query implies (origin, vs. latte/cappuccino, iced version).
- No featured snippet format observable via this tool; targeting a direct-answer paragraph block (matches
  "know-simple" intent) as the two prior short-answer posts in this cluster did.

## Step 2 — Head-entity research (non-competitor)

- **Flat white** (Wikipedia, en.wikipedia.org/wiki/Flat_white): "a drink consisting of espresso coffee and
  steamed milk", higher espresso-to-milk ratio than a latte, no thick cappuccino-style foam. Industry-
  standard composition: double espresso (50 ml) + ~130 ml steamed milk with ~5 mm microfoam, served in a
  175-200 ml ceramic cup. Type: Product/beverage (unlinked to a single canonical Starbucks SKU — it's a
  generic coffee-drink type Starbucks also serves).
- Origin dispute, both claims unresolved:
  - Australia: Sydney café review referencing "flat white coffee" (May 1983); Alan Preston added it to
    Moors Espresso Bar's menu in 1985, said he imported the idea from far north Queensland; Parliament
    House Canberra cafeteria posted a "flat white only" sign (Jan 1985).
  - New Zealand: Derek Townsend and Darrell Ahlers of Café DKD (Auckland) claim invention as a
    latte alternative; Bar Bodega (Wellington) claims a "failed cappuccino" inspired it, 1989.
  - Coffee historian Ian Bersten: probably originated in England in the 1950s; term attested in print by
    1971 and appears in a 1963 British film — earlier than either national claim.
- **Starbucks** (Organization, sameAs de.wikipedia.org/wiki/Starbucks, already used in sibling posts):
  introduced the Flat White to its US stores on **6 January 2015**. By 2024, ~1 in 3 UK Starbucks
  consumers chose a Flat White (Wikipedia); no equivalent German-market share figure found — not stated
  in the draft.

## Step 3 — Title + metadata

- Title: "Starbucks Flat White: Preis, Kalorien und Unterschied zum Latte 2026" (~62 chars, keyword
  front-loaded, no fabricated freshness beyond the sitewide "2026" convention already used on sibling
  posts).
- H1 differs slightly, more direct: "Starbucks Flat White: Was steckt drin, was kostet er?"
- Meta description (~150 chars): "Starbucks Flat White: was drin steckt, was er kostet (4,71 €) und wie er
  sich von Latte und Cappuccino unterscheidet – inklusive der Eiskaffee-Dose aus dem Supermarkt."
- Slug: `starbucks-flat-white` (sitewide "starbucks-<drink>" convention, matches starbucks-latte-macchiato,
  starbucks-iced-coffee — not the calendar's suggested `/getraenke/...` nested path, which the live site
  doesn't use anywhere).

## Step 4 — Competitors fetched (4)

1. **starbuckspreise.de** — homepage table row (Flat White: 4,71 €, 318 kJ/76 kcal) +
   dedicated article `flat-white-klein-stark-und-voller-charakter/`. Full heading structure:
   H1 "Flat White: Klein, stark und voller Charakter" → H2 "Was macht den Flat White besonders?" → H2
   "Preis und Nährwerte im Überblick" (table: Preis 4,71 €, Energie 318 kJ/76 kcal) → H2 "Für wen eignet
   sich der Flat White?" → H2 "Fazit". No FAQ block, no size options, no origin story, no iced/retail
   variant, no date shown. Thin, four H2s only.
2. **speisekartemenus.de/starbucks-preise/** — full German Starbucks price list (lattes, mochas,
   cappuccinos, frappuccinos, specialty drinks) that **omits Flat White entirely** — a real ranking
   competitor with a genuine content gap on this exact query, used as an information-gain point rather
   than a source of facts.
3. **supermarktcheck.de/product/386680-starbucks-flat-white-eiskaffee-220ml** — retail can product page:
   Starbucks Flat White Eiskaffee, 220 ml, €2.29 (Rewe), per-100ml: 66 kcal/277 kJ, 2.8 g protein, 6.0 g
   carbs (5.7 g sugar), 3.2 g fat (2.1 g saturated), 0.03 g sodium; Nutri-Score B; ingredients "Trinkmilch
   4,16% Fett (75%), Kaffeezubereitung (Wasser, Kaffee-Extrakt) (22%), Zucker (2%), Chicorée-Inulin,
   natürliches Kaffeearoma, Säureregulator Kaliumkarbonat, Stabilisatoren Carrageen/Guarkernmehl"; sold at
   EDEKA and Rewe.
4. **fddb.mobi/de/starbucks_flat_white_vollmilch.html** — nutrition DB entry for "Flat White, 3,5%
   Vollmilch + Vanilla Flavor" (a flavoured variant, not the plain café drink): 57 kcal/100ml; portions
   listed (200 ml glass 113 kcal, 50 ml cup 28 kcal, 300 ml 170 kcal, 460 ml bottle 260 kcal). Page itself
   flags **"Angaben noch nicht bestätigt"** (unconfirmed) — used only as a secondary, explicitly-flagged
   data point, not as the primary calorie figure (that's starbuckspreise.de's 76 kcal, cross-checked
   against a WebSearch AI-summary of fatsecret.de/fddb.de that separately gave 76 kcal Vollmilch/Short and
   70 kcal Hafermilch/Short — consistent with each other, inconsistent with this flavoured-variant entry,
   so the flavoured-variant numbers are not used in the draft).

Manufacturer fact (separate WebSearch, not a competitor for the keyword but a genuine info-gain source):
Starbucks ready-to-drink coffee-milk beverages for Europe/Middle East/Africa are produced under a
**21-year license by Arla Foods** (Danish dairy cooperative), at Arla's plant in **Esbjerg, Denmark**,
using Arla milk + 100% Arabica Starbucks coffee; Arla Foods Deutschland GmbH (Düsseldorf) distributes in
Germany; >10 million units sold in Germany in the reported year, +33% over three years. Sources:
lebensmittelpraxis.de, rundschau.de, arlafoods.de press release, lebensmittelzeitung.net (converging,
independent trade-press reporting — treated as reliable). Contrasts with the **PepsiCo/NACP** manufacturing
fact already used in the sibling `starbucks-iced-coffee` post for the US market — a genuine EU-vs-US
manufacturing-partner difference, not previously stated on this site.

## Step 5/6 — Entity ledger + tiers

| canonical | type | aliases | sameAs | kind | competitor_count | in_title_or_h2 | tier |
|---|---|---|---|---|---|---|---|
| Flat White | Product/beverage type | — | en.wikipedia.org/wiki/Flat_white | entity | 4/4 | yes | 1 |
| Starbucks | Organization | — | de.wikipedia.org/wiki/Starbucks | entity | 3/4 | yes | 1 |
| Café Latte | Product/beverage type | Latte | — | entity | 2/4 (starbuckspreise.de mentions comparison, Wikipedia) | yes (H2) | 2 |
| Cappuccino | Product/beverage type | — | — | entity | 2/4 | yes (H2) | 2 |
| Origin dispute (Australia/NZ) | Event/Concept | — | — | term | 1/4 (Wikipedia only, but core to "what is it") | no | 2 |
| Iced Flat White | Product | — | — | entity | 1/4 (Wikipedia/SERP title only) | no | 2 |
| Starbucks Flat White Eiskaffee (Dose) | Product | RTD can | — | entity | 1/4 (supermarktcheck.de) | no | 2 |
| Arla Foods | Organization | — | — | entity | 0/4 (separate research, not a competitor page) | no | 2 |
| Nutri-Score B | Metric | — | — | term | 1/4 | no | 3 |
| Hafermilch-Variante | Concept | oat milk | — | term | 1/4 (WebSearch nutrition summary) | no | 3 |
| Vanilla-Flavor-Variante (fddb) | Product | — | — | term | 1/4, flagged unconfirmed | no | 3 (unused — see below) |

**Relationships (12):**
1. Flat White —besteht aus→ doppeltem Espresso (50 ml) + ~130 ml gedämpfter Milch, ~5 mm Mikroschaum
2. Flat White —hat weniger Milch/Schaum als→ Café Latte
3. Flat White —hat keinen dicken Schaum wie→ Cappuccino
4. Starbucks —führte den Flat White in US-Filialen ein am→ 6. Januar 2015
5. Flat White (Starbucks DE, Café) —kostet→ 4,71 € (Drittquelle)
6. Flat White (Vollmilch, Short) —enthält→ 76 kcal
7. Flat White (Hafermilch, Short) —enthält→ 70 kcal
8. Flat White-Herkunft —wird beansprucht von→ Australien (Alan Preston/Moors Espresso Bar, 1985) und Neuseeland (Café DKD, Bar Bodega, 1989)
9. Starbucks Flat White Eiskaffee (Dose, 220 ml) —kostet→ ca. 2,29 € (Rewe)
10. Starbucks Flat White Eiskaffee —wird hergestellt von→ Arla Foods
11. Arla Foods —hält eine→ 21-Jahres-Lizenz für Starbucks-RTD-Getränke in EMEA, Produktion in Esbjerg (DK)
12. speisekartemenus.de-Preisliste (Wettbewerber) —lässt aus→ den Flat White vollständig

**Dedupe / parked:** the fddb.mobi "Vanilla Flavor" variant's calorie figures are parked, not used —
explicitly unconfirmed on-page and inconsistent with the two cross-checked plain-Flat-White figures
(76/70 kcal); stated here rather than silently dropped. "Ristretto" as a separate entity was folded into
the Flat White composition sentence rather than given its own section — single-competitor term, not
distinct enough from "double espresso" to warrant separate tier-2 treatment.

## Step 7 — Information-gain pass

- All 4 sources omit or under-serve: (a) the Australia/New Zealand origin dispute — starbuckspreise.de
  skips it entirely; (b) the exact difference vs. latte/cappuccino as anything other than a vague
  adjective ("kompakt, intensiv"); (c) the retail canned product and who actually makes it.
- speisekartemenus.de, a real ranking competitor for general Starbucks pricing, **omits Flat White from
  its price list altogether** — a genuine content gap named plainly in the draft (not fabricated).
- **Original element committed to:** a comparison table (Flat White vs. Latte vs. Cappuccino by espresso
  amount / milk amount / foam thickness) plus the Arla Foods manufacturing fact for the retail can —
  neither appears on any of the 4 fetched pages, and the Arla fact creates a genuine cross-post
  relationship-web with the sibling `starbucks-kapseln-angebot` (Nestlé/home range) and
  `starbucks-iced-coffee` (PepsiCo/NACP, US market) posts already on this site.

## Step 8 — Heading + keyword + question map

| # | Level | Phrase (focus/LSI) | User question | Tier-1/2 carried |
|---|---|---|---|---|
| H1 | H1 | Starbucks Flat White | (macro topic) | Flat White, Starbucks |
| — | direct-answer | — | "Was ist ein Starbucks Flat White?" | Flat White composition |
| 1 | H2 | Was ist ein Flat White genau? | "starbucks flat white" (know-simple) | Flat White (composition) |
| 2 | H2 | Woher kommt der Flat White – Australien oder Neuseeland? | fan-out (origin) | Origin dispute |
| 3 | H2 | Flat White vs. Latte vs. Cappuccino | "flat white starbucks drink" (comparison) | Café Latte, Cappuccino |
| 4 | H2 | Was kostet der Flat White bei Starbucks in Deutschland? | "flat white starbucks coffee" (price) | Starbucks price/kcal |
| 5 | H2 | Gibt es den Flat White auch als Eiskaffee zum Mitnehmen? | "starbucks flat white" (retail variant) | Iced Flat White, Eiskaffee-Dose, Arla Foods |
| 6 | H2 | Häufig gestellte Fragen | FAQ | all |

Order rationale: definition (core, know-simple) → origin (background, satisfies curiosity before the
comparison) → comparison table (the second core block — this is what most "flat white starbucks coffee"
searchers actually want to know) → price/kcal (transactional close) → iced/retail (peripheral extension) →
FAQ last.

## Internal-link plan

- Inbound (add link **to** this new page from): `starbucks-latte-macchiato.html` (natural "vs. Flat White"
  mention), `starbucks-iced-coffee.html` (already covers Doubleshot/PepsiCo — Flat White Eiskaffee is the
  natural sibling product), `starbucks-kaffee.html`, `starbucks-menu.html`.
- Outbound (from the new page): `/blog/starbucks-preise` (full price list), `/blog/starbucks-latte-macchiato`
  (comparison entity), `/blog/starbucks-iced-coffee` (Eiskaffee/RTD sibling), `/blog/starbucks-kapseln-angebot`
  (parallel Nestlé-vs-Arla manufacturing-partner fact).
- Cannibalisation check: Content_Calendar had no existing "fold into existing starbucks-flat-white" rows
  before this run (only the two "planned...post" rows being absorbed now) — no existing live page already
  targets this exact intent.

## FAQ source map (12, min. 10)

1. Was ist ein Flat White bei Starbucks? — Step 2/Wikipedia definition
2. Was kostet ein Starbucks Flat White in Deutschland? — starbuckspreise.de
3. Wie viele Kalorien hat ein Starbucks Flat White? — starbuckspreise.de + fatsecret/fddb cross-check
4. Worin unterscheidet sich der Flat White vom Latte? — Wikipedia
5. Worin unterscheidet sich der Flat White vom Cappuccino? — Wikipedia
6. Kommt der Flat White aus Australien oder Neuseeland? — Wikipedia (origin dispute)
7. Seit wann gibt es den Flat White bei Starbucks? — Wikipedia (6 Jan 2015)
8. Gibt es den Flat White auch als Iced-Variante? — starbucks.com/menu/product/565/iced (SERP title;
   content itself not fetchable, so phrased generically, not quoting unseen page text)
9. Was ist die Starbucks Flat White Eiskaffee-Dose? — supermarktcheck.de
10. Wer produziert die Starbucks-Eiskaffee-Dosen in Deutschland? — Arla Foods trade-press research
11. Kann man den Flat White mit pflanzlicher Milch bestellen? — WebSearch nutrition summary (Hafermilch)
12. Warum taucht der Flat White nicht auf jeder Starbucks-Preisliste auf? — speisekartemenus.de gap
    (information-gain point, stated as an observation about third-party lists, not a Starbucks fact)

## Fact cross-check note

Every number in the draft traces to one of: starbuckspreise.de (price, kcal Vollmilch), the WebSearch
nutrition-summary result (kcal Hafermilch — flagged as an AI-summarized secondary source, not a directly
fetched page, in coverage.md), supermarktcheck.de (can price/size/Nutri-Score/ingredients), Wikipedia
(composition ml/mm figures, dates, origin claims), or the Arla trade-press cluster (license length,
location, distributor). No number is invented. The fddb "Vanilla Flavor" figures are explicitly excluded
from the draft, not silently reconciled.
