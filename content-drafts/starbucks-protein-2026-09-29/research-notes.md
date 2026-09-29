# Research notes: starbucks protein

Run date: 29 Sep 2026 · Site: starbuckspreise.com (DE, du-voice) · Blog post · Slug `/blog/starbucks-protein`

## Step 1: Intent + SERP
- **Demand:** Google Trends DE (anchor "starbucks kalorien" = 480) gives "starbucks protein" about 970/mo, peaking 19–25 Apr 2026, which matches the April launch.
- **Intent:** *know* (what is it, how much protein, price), with *buy* as a secondary intent (supermarket bottle).
- **SERP:** the German DuckDuckGo scrape was rate-limited for this query and the Google SERP was captcha-blocked. The WebSearch results were: about.starbucks.com (US bottled protein), einzelhandel-news.de, tee-trinker.de, haushaltsbibel.de (the same Alpro press release), starbuckschilledcoffee.com/de (RTD), protein.starbucks.com (US), and our own competitor starbuckspreise.de (homepage only).
- **Fan-out (autocomplete):** starbucks protein / protein coffee / protein drink / protein latte; starbucks matcha protein; starbucks vanilla protein latte; starbucks iced protein sugar free vanilla latte; protein latte starbucks; brunch protein starbucks.

## Step 2: Head-entity sources
| # | Source | Facts used |
|---|---|---|
| S1 | Starbucks DE Nährwerte PDF, Autumn 10.09.2026 | every protein, kcal, sugar and caffeine value (Vanilla/Matcha by size, hot and iced; Caffè Latte Halbfett/Soja; Caramel Protein Americano Blonde/Decaf: Grande 100 kcal, 16,4 g) |
| S2 | Starbucks DE Allergen PDF (Getränke), same date | Soy Protein Latte, Iced, Protein Matcha and Iced: vegan "ja", vegetarisch "ja" |
| S3 | starbucksfreiburg.de (Freiburg Hbf ordering) | Soy Protein Vanilla Latte 5,90 € (hot and iced), Soy Protein Matcha 7,90 € (hot and iced), Caffè Latte 4,90 € |
| S4 | starbucks.de hot/iced/matcha menu pages | DE menu names; no Protein Americano, no protein cold foam listed |
| S5 | einzelhandel-news.de (07.07.2026), tee-trinker.de (06.07.2026) | Alpro Plant Protein Sojadrink, 5 g/100 ml, names "Protein Vanilla/Matcha Plant-Based Latte", hot and cold, usable in any drink, nationwide |
| S6 | greenqueen.com.hk (03.04.2026, upd. 05.04) | Central Europe launch incl. Germany, operated by AmRest; free soy swap until 21 April; EMEA whey protein cold foams (not DE); Alpro 13.1 % vs 8.3 % soybeans |
| S7 | vegconomist.com (title only, via search) | "Add Plant Protein Soy Drink to Permanent Menu" |
| S8 | starbuckschilledcoffee.com/de protein drink page + rewe.de listings (search) | 3 flavours; 6.1 g protein, 51 kcal, 3.8 g sugar per 100 ml; ingredients 75 % milk 1.3 %, 20.9 % coffee, 3.8 % milk protein, acesulfame-K; 330 ml, 20 g protein; REWE lists Caffè Latte and Caramel Hazelnut |
Entities: Starbucks Q37158 (verified). AmRest Q4738898 (verified via API: "Spanish fast food company", HQ Madrid). Soy milk Q192199 and Protein Q8054 verified. Alpro: the Wikidata search returned a wrong hit, so only the Wikipedia URL (HTTP 200) is used.

## Step 3: Metadata
- Title: Starbucks Protein Latte 2026: Preis, Protein & Kalorien (55 chars)
- H1: Starbucks Protein Drinks: Protein Latte, Matcha und Protein-Kaffee im Check
- Meta: see meta.json
- Slug: /blog/starbucks-protein

## Step 4: Competitors (fetched)
| # | URL | Headings (verbatim) |
|---|---|---|
| C1 | einzelhandel-news.de/alpro-starbucks-protein-vanilla-matcha-plant-based-lattes | Alpro und Starbucks bringen innovative pflanzliche Protein-Kaffeespezialitäten in Deutschland / Starbucks-Gäste wählen Protein Vanilla Plant Based Latte mit Espresso / Alpro Protein Sojadrink: Fünf Gramm Protein pro 100 Milliliter / …erweitert Starbucks-Angebot um pflanzliche Proteinvielfalt / …ohne Geschmacksverlust / Protein Vanilla- und Matcha-Lattes jetzt deutschlandweit in Starbucks-Filialen erhältlich. No prices or kcal. |
| C2 | tee-trinker.de/alpro-starbucks-protein-vanilla-matcha-plant-based-lattes | same press release, no prices or kcal |
| C3 | greenqueen.com.hk (EN) | launch markets, AmRest, cold foam EMEA, protein 8–22 g per drink |
| C4 | starbuckschilledcoffee.com/de (RTD) | product facts |
Substitution: starbuckspreise.de (competitor) had no protein content on the fetched page, so it was dropped.

## Step 5/6: Ledger (entities.json)
- **Tier 1:** Protein Latte, Soy Protein Vanilla Latte, Soy Protein Matcha Latte, Alpro Plant Protein Sojadrink, Protein g, Preis, Starbucks DE.
- **Tier 2:** 5 g/100 ml, kcal, Zucker, Koffein, sugar-free vanilla syrup, sizes, iced, vegan, laktosefrei, Soja allergen, RTD Protein Drink, 330 ml / 20 g, Caffè Latte comparison, Protein Cold Foam (not DE), AmRest, Danone, protein swap in any drink.
- **Tier 3:** Caramel Protein Americano, Rewe, Acesulfam-K, Decaf, Borghardt quote (unused), soybean share.
- **Relationships:**
  - Alpro Plant Protein —provides→ 5 g/100 ml.
  - Vanilla Grande —has→ 16,6 g / 194 kcal / 8 g sugar / 89,1 mg; costs 5,90 €.
  - Matcha Grande —has→ 17 g / 192 kcal / 86 mg; costs 7,90 €.
  - Vanilla Tall —has→ 44,5 mg (one shot fewer than Caffè Latte Tall, 89,1).
  - Venti 89,1 vs 133,6.
  - Protein lattes —are→ vegan (S2).
  - RTD —contains→ milk protein → not vegan; 330 ml → 20 g.
  - AmRest —operates→ Starbucks DE.
  - Protein Cold Foam —not in→ DE list.
- **Parked:**
  - The RTD price: menu.js says 2,94 € but its origin is unknown and REWE shows no price in search, so it is not stated.
  - The US protein range.
  - The Protein Joghurt (food).

## Step 7: Information gain
- No competitor gives **nutrition values, prices or a comparison**; C1 and C2 are pure press release copies.
- **Original elements:**
  - (1) a protein-per-euro table versus a normal latte;
  - (2) the finding that the Vanilla Protein Latte has **one fewer shot** in Tall and Venti;
  - (3) the note that the café lattes are vegan while the supermarket bottle is milk-based;
  - (4) the DE-vs-US cold foam clarification.

## Step 8: Heading map
| Level | Heading | Phrase |
|---|---|---|
| H1 | Starbucks Protein Drinks: Protein Latte, Matcha und Protein-Kaffee im Check | starbucks protein |
| H2 | 1. Welche Protein-Getränke gibt es bei Starbucks? | protein drink |
| H2 | 2. Wie viel Protein hat ein Starbucks Protein Latte? | protein latte |
| H3 | Nährwerte nach Größe | kalorien |
| H3 | Wie viel Zucker steckt drin? | zucker / sugar free vanilla |
| H2 | 3. Lohnt sich der Protein Latte im Vergleich…? | protein latte vs latte |
| H2 | 4. Kann man jedes Starbucks Getränk mit Protein bestellen? | protein milch |
| H2 | 5. Ist der Starbucks Protein Latte vegan? | vegan |
| H2 | 6. Starbucks Protein Drink aus dem Supermarkt | protein drink / protein coffee |
| H2 | 7. Welcher Protein-Drink passt zu dir? | matcha protein / vanilla protein |
| H2 | Häufig gestellte Fragen | 10 Q |

**Internal links:**
- /blog/starbucks-vegane-optionen
- /blog/starbucks-angebote
- /blog/starbucks-kalorien-guide
- /blog/starbucks-matcha-latte

**Add later:**
- A link from /blog/starbucks-matcha-latte and /blog/starbucks-vegane-optionen to this page.

**Cannibalisation:** none. No page targets "protein".

## Open flags (need user)
1. **No price for the protein swap** in other drinks after 21 Apr 2026. The draft says to ask in the store.
2. **RTD bottle price** is not stated (menu.js 2,94 € is unverified).
3. **Caramel Protein Americano** appears in the nutrition PDF but not on the online menu. The FAQ says to ask in the store.
4. "Juli 2026 fester Bestandteil" rests on the vegconomist headline and the July press dates; the April start is from greenqueen.
5. **Hero image:** a latte or matcha with a plant-milk carton, no Starbucks logo.
