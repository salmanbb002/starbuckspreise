# Research notes: „starbuck karte“ (merge → /blog/starbucks-menu)

Run date: 2026-09-23. Mode: **merge-ready insert** (user's choice). The workbook marks this keyword "Merge-Recommended (fold into existing starbucks-menu)".

## Step 1: Intent + SERP
Query checked: "starbucks karte deutschland" (the US-based search tool can't geo-target DE, so treat it as a proxy).

Top results:
1. apps.apple.com: Starbucks® Deutschland app (Rewards/digital card)
2. eberdt.de: "Starbucks Karten Deutschland" (collector cards)
3. despeisekartes.org/starbucks-speisekarte: Speisekarte (no date, headings say 2024/2025)
4. starbuckspreise.de: competitor price list (2026)
5. kaffeenavigator.de: "Was ist die Starbucks Card…" (published 17 Jan 2015, stale)
6. starbucks.de/en/faq-starbucks-card: official Card FAQ
7. stepmap.com: Germany store map
8–9. ebay.de: collectible Starbucks cards

**Intent: split three ways.** Starbucks Card (know/do: 4 of 9), Speisekarte (know: 2), Landkarte/collectibles (3). The workbook put the keyword under Menu, but the SERP shows the **Card** meaning leads. That's why the merge includes a disambiguation box and a Card section instead of just adding the keyword to the menu page.
SERP features: no featured snippet seen; app result (a navigational signal).
Fan-out: "starbucks karte aufladen", "starbucks card kaufen", "starbucks karte registrieren", "starbucks rewards sterne".

## Step 2: Head entities
| Entity | Type | sameAs |
|---|---|---|
| Starbucks | Organization | https://de.wikipedia.org/wiki/Starbucks |
| Starbucks Card | Thing (stored-value card) | unlinked (no standalone Wikipedia article) |
| Starbucks Rewards | Thing (loyalty programme) | unlinked |
| AmRest (DE operator) | Organization | https://de.wikipedia.org/wiki/AmRest (already cited on the page) |

## Step 4: Sources fetched
- **starbucks.de/en/faq-starbucks-card** (official): where to get the card (participating stores), top-up at the register or in the app, register with a 16-digit card number + 8-digit PIN, reloadable any time, no fees on unused balance, a lost registered card's balance moves to a new card sent by post.
- **starbucks.de/en/faq-rewards** (official): 3 stars per €1; 150 stars = free drink; 450 stars in a tier year = Gold; Gold gets free syrups & toppings, a birthday drink and a free refill with filter coffee/brewed tea; Rewards Stars valid 2 years from crediting; Tier Stars count only within the tier year; some licensed stores can't process card payments (banking regulations).
- **starbucks.de/de/starbucks-card** (official, DE): 3 Sterne je Euro, digital card in the app, gift card promoted. Gives no card price or load limits.
- **kaffeenavigator.de** (2015): load range €5–€150, Postbank (800+ branches, min €25). **Stale, not used.**
- **despeisekartes.org**: Speisekarte headings, prices only up to 2024. Used for competitor heading structure only.
- **starbuckspreise.de**: competitor Speisekarte + price list. Used for heading structure only.
- Not verified, so **not used**: a physical card price of €5 and reload minimum of €10 (these came from a search-snippet summary, not a fetched official page), and REWE (2,800) / Post (800) sales points with €25 cards (third-party snippet, likely dated).

## Step 5/6: Entity ledger (condensed)
| canonical | type | kind | comp. | tier |
|---|---|---|---|---|
| Starbucks Card | Thing | entity | 3 | 1 |
| Starbucks Rewards | Thing | entity | 3 | 1 |
| Speisekarte / Menü | Concept | term | 3 | 1 |
| Stars (3 pro Euro) | Metric | term | 3 | 1 |
| Aufladen (Filiale/App) | Process | term | 3 | 1 |
| Registrieren (16-stellig + 8-stellige PIN) | Process | term | 2 | 2 |
| Gratisgetränk (150 Stars) | Metric | term | 3 | 1 |
| Gold-Status (450 Stars) | Metric | term | 2 | 2 |
| Starbucks-Deutschland-App | Product | entity | 3 | 1 |
| Guthaben / Verlust / Ersatzkarte | Concept | term | 2 | 2 |
| Gebühren (keine) | Concept | term | 2 | 2 |
| Geschenk / verschenken | Concept | term | 2 | 2 |
| Filialkarte / Landkarte | Concept | term | 1 | 3 |
| Lizenzierte Standorte | Concept | term | 1 | 3 |
| Postbank / REWE Verkaufsstellen | Org | entity | 1 | 3 (parked: stale/unverified) |

Relationships: Starbucks Card —earns→ 3 Stars/€ · 150 Stars —redeem for→ Gratisgetränk · 450 Stars/Statusjahr —unlocks→ Gold · Gold —includes→ Sirup/Toppings, Geburtstagsgetränk, Refill · Registrierung —requires→ 16-stellige Nr. + 8-stellige PIN · Registrierung —protects→ Guthaben · Rewards-Stars —valid→ 2 Jahre · Card —loaded via→ Kasse/App · Lizenzierte Standorte —may not accept→ Card.

Dedupe log: "Wie funktioniert Starbucks Rewards in Deutschland?" already exists in the page FAQ, so it isn't repeated. The new FAQs are Card-specific plus star validity and Gold detail. Postbank/REWE are parked as stale or unverified.

## Step 7: Information gain
- No competitor explains the **three meanings** of "Starbucks Karte". The disambiguation table (Block A) is the main info-gain element.
- No competitor converts stars into **euros spent**: 150 Stars = 50 €, Gold = 150 €, shown with a Caramel Macchiato example at the site's own price of 4,99 € (menu.js).
- The only competitor with card logistics (kaffeenavigator) is from 2015. This draft uses only current official FAQ facts.

## Step 8: Heading map (insert)
| Level | Heading | Owns | Question |
|---|---|---|---|
| box | Welche „Starbucks Karte“ suchst du? | starbuck karte (focus) | which Karte? |
| H2 | 8. Was ist die Starbucks Card, die andere „Starbucks Karte“? | starbucks card | what is it |
| H3 | Wo bekommst du eine Starbucks Card? | starbucks card kaufen | where |
| H3 | Wie lädst du die Starbucks Card auf und registrierst sie? | starbucks karte aufladen | how |
| H3 | Was bringt die Starbucks Card bei Starbucks Rewards? | starbucks rewards sterne | value |
| H3 | Was passiert, wenn du die Starbucks Card verlierst? | karte verloren | problem |
The existing H1 ("…Die komplette Karte…") already carries the focus term. No H1 change.

## Step 8e: Internal links / cannibalisation
- Links out: /blog/starbucks-deutschland-filialen, /blog/starbucks-in-der-naehe (for the Landkarte meaning).
- Cannibalisation: none. No page on the site targets Starbucks Card. The Card meaning **could** justify its own post later ("starbucks card", "starbucks karte aufladen"), but none of those keywords is in the workbook. Revisit if GSC shows Card impressions.

## Step 10: FAQ source map
11 FAQs. Q1–Q5, Q9–Q11 → official Card FAQ / starbucks.de Card page. Q6 (star validity) and Q8 (Gold) → official Rewards FAQ. Q7 → arithmetic from the official 3 Stars/€ and 150 Stars.
