# Research notes: „starbucks nährwerte“ (+ „starbucks kalorie“)

**Run:** 26 Sep 2026 · **Mode:** merge-rewrite into `blog/starbucks-kalorien-guide.html` · **Calendar:** Day #166 (590/mo, KD 25) + Day #168 „starbucks kalorie“ (260/mo, KD 19)

## Step 1: Intent + SERP

- **Intent:** *know-simple* / lookup: people want a table of values for a specific drink. Secondary: *know* (which drinks are lighter).
- **Top results (WebSearch, US-proxied, 26 Sep 2026):**
  1. fatsecret.de/Kalorien-Ernährung/starbucks: database, German data, only portion + kcal on the listing page
  2. yazio.com/de/kalorientabelle/starbucks: database, ~30 items, kcal only on the listing page, mixed US/DE portions (e.g. Caramel Macchiato 591 ml = US Venti)
  3. foodplaner.de/kalorientabelle-marke-starbucks: database
  4. **starbucks.de official PDF** (Spring, 02.02.2026 Getränke-Nährwerte): ranks directly
  5. fddb.info/db/de/hersteller/starbucks: database, 11 pages
  6. starbuckspreise.de: competitor with the same brand name on a different TLD (price site)
- **SERP features:** no featured snippet; PDF result; database listings. No PAA captured (US-proxied search).
- **Fan-out (derived):** starbucks nährwerte tabelle, starbucks kalorien latte, starbucks zucker, starbucks koffein, starbucks nährwerte pdf, starbucks allergene, starbucks kalorien frappuccino, starbucks kalorie (typo/singular).

## Step 2: Head entities (primary source)

| Entity | Type | Source | Key attributes |
|---|---|---|---|
| Starbucks Nährwertinformationen DE | Document | starbucks.de/nutrition → PDFs „Autumn, 10.09.2026“ (Getränke Nährwerte, Getränke Allergene, Food) | ESHA R&D SQL® calculation; standard recipes; values per size × milk; 10 nutrient columns; food per 100 g + per piece; cross-contamination note |
| Starbucks | Organization | de.wikipedia.org/wiki/Starbucks | operator DE: AmRest (from host page) |
| Koffein | Concept | de.wikipedia.org/wiki/Coffein; EFSA 2015 opinion | EFSA: ≤400 mg/day, ≤200 mg single dose (adults); ≤200 mg/day pregnancy |
| Freier Zucker | Concept | WHO guideline „Sugars intake for adults and children“ (2015) | <10 % energy, conditional <5 % |
| Laktose | Concept | de.wikipedia.org/wiki/Lactose | counted in „davon Zucker“, not a free sugar per WHO |

**Source files kept in session scratchpad** (PDFs downloaded and text-extracted): Spring 02.02.2026 drinks, Autumn 10.09.2026 drinks + food.

### Key extracted values (Autumn 10.09.2026, Grande, Halbfettmilch unless noted)
See draft tables; all numbers are transcribed from the PDF rows, e.g.
`Caffe Latte - Halbfettmilch Grande 636 151 5,2 3,4 15 14,2 0,3 10,9 0,32 89,1`.
Extremes (script over all rows): max kcal = Signature Hot Chocolate Vollmilch Venti 499; max sugar = Pumpkin Spice Coffee Frappuccino Venti 59,8 g; max caffeine = Freshly Brewed Coffee Venti 324,2 mg.

**Spring → Autumn change:** Caffe Latte Halbfettmilch Tall 129 kcal / 44,5 mg → 124 kcal / 89,1 mg; Venti 204 kcal / 89,1 mg → 204 kcal / 133,6 mg. New in Autumn: Pumpkin Spice range, Pecan Maple Macchiato, Soy Protein Latte/Matcha Latte.

## Step 4/5: Competitors in depth

Only database pages rank, with no editorial H2s. Extraction by heading therefore yields almost nothing:
- **yazio:** H2 „Beliebte Lebensmittel“, „Sortiert nach Kategorien“; H3 categories (Kaffeegetränke 19, Kuchen & Torten 4…). Terms: Kalorientabelle, Nährwerttabelle, Portion, 100 ml. Uses **US** sizes (591 ml Caramel Macchiato 312 kcal), which doesn't match the German menu.
- **fatsecret:** H1 „Starbucks Produkte, Kalorien und Nährwertangaben“; German data (Zimtschnecke 355 kcal, NY Cheesecake 370 kcal, which match the official food PDF). Only kcal + portion on the list.
- **foodplaner / fddb:** product-database listings, per-product pages, no dates.
- **starbucks.de PDF:** raw table, no explanation.

## Step 6: Entity ledger (tiers)

| canonical | type | kind | comp. count | tier |
|---|---|---|---|---|
| Starbucks Nährwerte | Concept | entity | 4 | 1 |
| Kalorien (kcal) | Metric | term | 4 | 1 |
| Zucker | Metric | term | 2 | 1 |
| Koffein | Metric | term | 1 (PDF) | 1 (intent) |
| Fett / Eiweiß / Kohlenhydrate | Metric | term | 2 | 2 |
| Größen Short/Tall/Grande/Venti | Concept | term | 2 | 2 |
| Milchsorte (Halbfett, Voll, Mager, Mandel, Soja, Hafer, Kokos) | Product | term | 1 (PDF) | 2 |
| Frappuccino® | Product | entity | 3 | 2 |
| Caffè Latte / Caramel Macchiato / White Mocha | Product | entity | 3 | 2 |
| Muffin / Zimtschnecke / Cheesecake | Product | entity | 2 | 2 |
| Allergene | Concept | term | 1 | 3 |
| Ballaststoffe, Salz, kJ | Metric | term | 1 | 3 |

**Relationships:** Nährwerte —published by→ Starbucks DE (PDF, seasonal) · Werte —calculated with→ ESHA R&D SQL · Milchsorte —drives→ kcal/Zucker/Eiweiß · Größe —scales→ kcal proportionally · Tall/Grande —share→ 2 Shots (89,1 mg) · Venti —has→ 3 Shots · Espresso-Shot —contains→ 44,5 mg Koffein · Frappuccino —uses→ Kaffeebasis (low caffeine) · „davon Zucker“ —includes→ Laktose · WHO —limits→ free sugar <50 g · EFSA —limits→ 400 mg/day, 200 mg single · Carrot Cake —exceeds→ every drink (817 kcal).

**Heading keyword set:** (a) focus: starbucks nährwerte, starbucks kalorien, starbucks kalorie, starbucks nährwerttabelle. (b) LSI: starbucks zucker, starbucks koffein, milch kalorien starbucks, starbucks snacks kalorien, kalorienärmste starbucks getränke.

**Dedupe/parked:** „starbucks allergene“ parked (separate intent, only one FAQ); vegan milks' prices parked → /blog/starbucks-vegane-optionen.

## Step 7: Information gain

- All four database competitors show **kcal only** on their listing pages; none puts fat/sugar/protein/caffeine in one table, and yazio mixes in US sizes.
- None explains that **„Zucker“ includes lactose**, or that **Tall and Grande have the same caffeine**.
- **Original elements committed:** (1) a milk-comparison table for one drink; (2) a „what changed in Autumn 2026“ box (Tall/Venti shot change); (3) a caffeine-by-size table with EFSA context; (4) a corrected savings list with exact numbers.

## Step 8: Heading + keyword + question map

| Level | Heading | Owns | Answers | Carries |
|---|---|---|---|---|
| H1 | Starbucks Nährwerte & Kalorien: die Tabelle für 2026 | starbucks nährwerte + kalorien | macro | Starbucks, Nährwerte |
| H2 | 1. Wo findest du die offiziellen Starbucks Nährwerte? | nährwerte pdf | where is the source | PDF, ESHA, Allergene |
| H3 | Was hat sich in der Autumn-Liste 2026 geändert? | – | freshness | Tall/Venti shots |
| H2 | 2. Nährwerttabelle: die wichtigsten Starbucks-Getränke | nährwerttabelle | the table | kcal, Fett, Zucker, Eiweiß, Koffein |
| H3 | Wie verändern die Größen … die Werte? | größen kalorien | size scaling | Short–Venti |
| H2 | 3. Wie viele Kalorien haben Starbucks-Getränke? | starbucks kalorie(n) | ranges | kcal |
| H3 | Die kalorienärmsten … / Die kalorienreichsten … | kalorienarm | lists | – |
| H2 | 4. Wie stark verändert die Milchsorte die Nährwerte? | milch kalorien | milk | 7 milks |
| H3 | Welche Milch passt zu welchem Ziel? | – | decision | Soja, Mandel, Hafer |
| H2 | 5. Wie viel Zucker steckt in Starbucks-Getränken? | starbucks zucker | sugar | Laktose, WHO |
| H2 | 6. Wie viel Koffein hat welches Starbucks-Getränk? | starbucks koffein | caffeine | Shot, EFSA |
| H2 | 7. Nährwerte der Starbucks Snacks und Speisen | snacks kalorien | food | Muffin, Carrot Cake |
| H2 | 8. Wie sparst du bei Starbucks Kalorien und Zucker? | kalorien sparen | action | Größe, Milch, Sirup |
| H2 | Häufige Fragen … | – | FAQ | – |

## Step 8e: Internal links + cannibalisation

- Out-links: /#getraenke (Preisübersicht), /blog/starbucks-vegane-optionen, /blog/starbucks-frappuccino-sorten, /blog/starbucks-latte-macchiato, /blog/starbucks-groessen-tall-grande-venti, /blog/starbucks-preise, /blog/starbucks-menu.
- **Cannibalisation:** none. „Kalorien“ is only on this page as a primary target. `/blog/starbucks-flat-white` and `iced-caramel-macchiato.html` cite drink-level kcal, which is fine (different macro).
- **Recommended in-link:** from `/blog/starbucks-menu` (§5 prices or FAQ) with anchor „Starbucks Nährwerte“.

## FAQ source map

3 original FAQs kept and rewritten (source, verbindlich, kalorienbewusst). Added: Standardmilch, Caffè-Latte kcal, max kcal, max caffeine, Frappuccino caffeine, lactose, protein, muffin kcal, Allergene. All sourced from the PDFs.
