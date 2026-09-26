# Research notes: „starbucks allemagne“

**Run:** 26 Sep 2026 · merge into `blog/starbucks-deutschland-filialen.html` · Calendar Day #158 (590/mo, KD 53)

## Intent + SERP
- **Language:** French („Allemagne“ = Germany). **Intent:** *know* (Starbucks in Germany: how many, where, price), partly *buy* (Amazon „Starbucks Allemagne Vous êtes Ici“ = the Germany „You Are Here“ mug).
- **Results (WebSearch, 26 Sep):** amazon.de (Germany YAH mug), en.wikipedia Starbucks, Tripadvisor Starbucks Pariser Platz Berlin, Google Play Starbucks Deutschland app, Instagram @starbucksde, tastingtable (German bakery menu), starbucks.com store locator (Germany), areas.com (Starbucks at German transport hubs), Bloomberg company profile.
- French-language follow-up search („Starbucks en Allemagne prix café nombre de magasins“): Statista FR (paywall), fastfood-preischeck.de/fr/prix-starbucks, cashmireplus (price by country), menuprix.fr. No French page answers store count + prices + operator together. **This is the gap.**
- **SERP features:** none captured; mixed-language, brand-heavy SERP (explains the KD 53).

## Head entities (source = host page, already researched 19 Sep)
179 stores (1 Jul 2026, ScrapeHero), 77 cities, 16 Länder; NRW 36 / Bayern 29 / Hessen 22; Berlin 19 / Frankfurt 14 / Hamburg 12 / München 11 / Köln 7; AmRest Coffee Deutschland (Munich) since April 2016; first stores in Berlin, May 2002; city-centre hours ~7–8 h to 20–21 h. Prices: `menu.js` (Espresso 2,75, Americano 3,10, Cappuccino 3,90, Latte 4,59, Caramel Macchiato 4,99, Coffee Frappuccino 5,29).

## Entity ledger
| canonical | type | tier | note |
|---|---|---|---|
| Starbucks (Deutschland) | Org | 1 | |
| Allemagne / Deutschland | Place | 1 | |
| Nombre de cafés (179) | Metric | 1 | |
| Prix (cappuccino etc.) | Money | 1 | |
| AmRest | Org | 2 | operator |
| Villes (Berlin, Francfort, Hambourg, Munich, Cologne) | Place | 2 | |
| Länder (NRW, Bavière, Hesse) | Place | 2 | |
| Horaires | Concept | 2 | |
| „You Are Here“ mug | Product | 3 | not in block; covered on /blog/starbucks-tassen (link opportunity) |

**Relationships:** Starbucks DE —operated by→ AmRest (2016) · Allemagne —has→ 179 cafés · Berlin —has most→ 19 · Cappuccino —costs→ 3,90 €.

## Heading/keyword map
H2 (FR) „Starbucks en Allemagne : l'essentiel en français“ owns *starbucks allemagne / starbucks en allemagne*; bold lead-ins answer où / combien coûte / qui exploite / horaires; 3 FR FAQs.

## Info gain
Only result combining store count + regional split + price table + operator **in French**.

## Internal links
→ /blog/starbucks-preise, /blog/starbucks-a-proximite (FR sibling). Recommend a reverse link from `starbucks-a-proximite` („Starbucks en Allemagne : chiffres et prix“ → `#starbucks-allemagne`). **Cannibalisation:** `starbucks-a-proximite` targets *near me* (FR), a different intent. No conflict.
