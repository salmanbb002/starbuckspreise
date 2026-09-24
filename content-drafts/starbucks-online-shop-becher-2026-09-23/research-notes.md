# Research notes: „starbucks online shop becher“ (merge → /blog/starbucks-becher)

Run date: 2026-09-23. Mode: merge-ready insert. The workbook says "Merge-Recommended (fold into existing starbucks-becher)". 720 searches/month, KD 22.

## Step 1: Intent + SERP
Query: "starbucks online shop becher" (US search tool, so treat it as a proxy).
1. ebay.de/b/Starbucks-Becher: 2,900+ listings (per search summary)
2. ebay.de Starbucks Kaffeetassen und Becher
3. etsy.com/market/starbucks_becher: personalised cups, 24 oz reusable, stainless tumblers
4. starbucksathome.com/de/deine-tasse/faq-teilnahmebedingungen: promo T&Cs
5. ehrenkaffee.de/kaffeebecher-to-go-starbucks (updated Oct 2022)
6. thecoffeemugshop.de You Are Here series
7. starbucksathome.com/de
8. ebay.de Becher to Go
9. starbucks.de/de/menu-merchandise-core

**Intent:** buy (transactional) and website (navigational: "is there an official shop?"). The SERP shows **no official Starbucks shop result with a basket**. That absence is itself the answer to the navigational intent.
Fan-out: "starbucks becher online kaufen", "starbucks tasse gratis", "starbucks becher bestellen".

## Step 2: Head entities
| Entity | Type | sameAs |
|---|---|---|
| Starbucks | Organization | https://de.wikipedia.org/wiki/Starbucks |
| Starbucks at Home | Brand (Nestlé licence) | unlinked (no DE Wikipedia article); site starbucksathome.com |
| Otto | Organization | https://de.wikipedia.org/wiki/Otto_(Versandhandel) |
| eBay | Organization | https://de.wikipedia.org/wiki/EBay |
| Etsy | Organization | https://de.wikipedia.org/wiki/Etsy |

## Step 4: Sources
- **starbucks.de/de/menu-merchandise-core:** product names and images only. **No prices, no sizes, no basket** in the fetched content (2026-09-23).
- **starbucksathome.com/de/deine-tasse/faq-teilnahmebedingungen:** direct fetch returned **HTTP 403**, so the facts come from the search-result excerpt of that page plus dealdoktor/mein-deal/kostenlos.de listings: ≥3 products → 1 cup + pen after receipt check; participating products are Starbucks by Nespresso, by Nescafé Dolce Gusto and Signature Chocolate; excluded are chilled coffee mixed drinks and coffee-shop purchases; max 3 participations per person. **Promo period unknown.**
- **otto.de** Starbucks brand page (fetched): prices as in the cups draft; delivery 3–4 working days.
- **thecoffeemugshop.de** (fetched): private, not affiliated, free shipping from 99 €, series list.
- **ehrenkaffee.de** (2022): stale prices and the 30 ct discount. Not used.
- A search-engine summary claimed "starbucks.de: shipping free from €50". That could **not** be verified on any fetched starbucks.de page, so it's treated as unreliable and not used.

## Step 5/6: Entity ledger
| canonical | type | comp. | tier |
|---|---|---|---|
| Online-Shop (offiziell?) | Concept | 4 | 1 |
| starbucks.de Merchandise-Katalog | Thing | 2 | 1 |
| Otto | Org | 2 | 1 |
| eBay | Org | 3 | 1 |
| Starbucks at Home | Brand | 2 | 1 |
| „Deine Tasse“-Aktion | Event (promo) | 1 | 2 |
| Teilnehmende Produkte (Nespresso, Dolce Gusto, Signature Chocolate) | Product | 1 | 2 |
| Etsy (personalisiert) | Org | 2 | 2 |
| The Coffee Mug Shop | Org | 1 | 2 |
| Kleinanzeigen (gebraucht) | Org | 2 | 2 |
| Echtheit / Bodenstempel | Concept | 1 | 2 |
| Lieferzeit / Versandkosten | Metric | 2 | 3 |

Relationships: starbucks.de —shows→ catalogue without prices · Otto —sells→ new cups (13,49–79 €) · Starbucks at Home —gives→ cup + pen for 3 products · Aktion —excludes→ chilled drinks, coffee-house purchases · Aktion —limit→ 3 per person · The Coffee Mug Shop —is→ private, not affiliated · Etsy —mostly→ personalised, non-official.

## Step 7: Information gain
1. **Correction:** the host page claims an "offizieller Starbucks Online-Shop" exists. Every source checked today says otherwise. Fixing it removes a factual error (a trust signal).
2. **Channel comparison table** (official? / new-used / price / what to check). No competitor has one; they're all single-channel listings.
3. **Free-cup promo** explained with its exclusions. None of the ranking pages combine it with buying advice.

## Step 8: Heading map
| Level | Heading | Owns |
|---|---|---|
| H2 (renamed §8) | 8. Wo kaufen, auch online, und woran erkennt man ein Original? | starbucks online shop becher (focus, partial) |
| H3 | Wo kann man Starbucks Becher online kaufen? | starbucks becher online kaufen |
| H3 | Gibt es Starbucks Becher als Online-Aktion? | starbucks tasse gratis |

## Step 8e: Links / cannibalisation
Out: /blog/starbucks-kapseln-angebot (promo needs capsule purchases). Existing links in §8 to the Tasse fake-check guide are kept. Overlap with the cups insert: none (range vs channels). Existing FAQ "Wo kann man originale Starbucks Becher kaufen?" is **rewritten**, not duplicated.

## Step 10: FAQ source map
10 new + 1 replacement. Q1 → starbucks.de fetch. Q2, Q9 → Otto. Q3–Q5 → Starbucks at Home T&C excerpt. Q6 → Etsy SERP snippet. Q7 → thecoffeemugshop.de. Q8 → host-page fake-check guidance. Q10 → host-page §4 table (ab ca. 4 €).
