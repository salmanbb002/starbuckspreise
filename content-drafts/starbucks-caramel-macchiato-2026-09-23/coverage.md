# Coverage / QA: „starbucks caramel macchiato“ merge insert

**Entity coverage:** Tier 1: 8/8 (100%), each with an attribute stated (price 4,99/5,79 €; 214/201 kcal; espresso → added last; vanilla/caramel → components). Tier 2: 6/6 (100%). Tier 3: 2/2 used (macros in Block B; Dolce Gusto in FAQ).

**Heading architecture:** 2 new H2s on a flat-H2 page (the template has no H3s, and the inserts follow suit). Valid. ⚠️ Mild overlap: new "Wie viele Kalorien…" H2 vs existing "Kalorien & Nährwerte" H2. The new one covers the hot drink and all sizes, the old one the iced drink. You could merge them (see research-notes §8).

**Answer blocks:** Both H2s answer in their first sentence (≈45 words / ≈30 words).

**Competitor matrix:**
| Competitor topic | Covered |
|---|---|
| Calories per size | ✅ table |
| Caffeine per size | ✅ table + corrected FAQ |
| Macros per 100 ml | ✅ |
| Ingredients / build | ✅ |
| Price | ✅ DE prices (US prices intentionally skipped) |
| "Is it strong?" | ✅ FAQ |
| "vs Latte" | ✅ FAQ (Caffè Latte + Latte Macchiato) |
| "Is it healthy?" | ➜ implicitly via sugar data. There's no health verdict, deliberately (not YMYL-safe without a source) |
| Birthday drink / deals | ➜ skipped. Rewards birthday drink is Gold-only per the official FAQ and belongs on the menu/Karte insert |

**Fact cross-check:**
- 4,99 / 5,79 / 4,59 / 4,70 €, 214/201/151/147 kcal → menu.js ✅
- Tall 213 kcal + macros, 7 g sugar/100 ml → fddb ✅
- Venti 312 kcal, 41,2 g sugar → yazio ✅
- Grande 250 kcal, 75/150 mg caffeine → starbucksmenususa (third-party, US) ⚠️ labelled "laut Starbucks USA" in copy. The official starbucks.com nutrition page would not render for the fetcher. **Recommend a manual check at starbucks.com/menu/product/413/hot/nutrition.**
- "≈25 g Zucker im Tall" → arithmetic 7 g × 3.55 ✅
- Description "marked with espresso" → starbucks.com search snippet ✅
- "Macchiato = gefleckt" → general Italian vocabulary ✅
- Iced Venti 709 ml / hot 591 ml → site's own menu page ✅
- "Iced Grande 150 mg" assumes the iced build matches the hot one (2 shots in Grande). ⚠️ Not separately verified.
- 6,30 € (Grande iced) / 6,90 € (Venti iced) → existing page's own list ✅

**Intent check:** Know-simple (what, price, calories) is fully served at the top of the new H2s.

**Readability:** Grade ~7–8. The tables carry the numbers, so the prose stays light.

**E-E-A-T / manual flags:**
1. ⚠️ Fix 3 live-page errors (Grande caffeine, Iced Venti ml, Grande/Tall kcal label).
2. ⚠️ The page has no JSON-LD at all. The provided graph includes the existing 3 FAQs (caffeine answer corrected) + 10 new ones. Fill the `datePublished` TODO.
3. The "vermutlich weil Eiswürfel…" sentence is a reasoned guess and is hedged as one. Remove it if you prefer.
4. No first-person claims.
