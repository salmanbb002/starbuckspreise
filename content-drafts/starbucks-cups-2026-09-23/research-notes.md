# Research notes: „starbucks cups“ (merge → /blog/starbucks-becher)

Run date: 2026-09-23. Mode: merge-ready insert. The workbook says "Merge-Recommended (fold into existing starbucks-becher)". 880 searches/month, KD 28.

## Step 1: Intent + SERP
Query: "starbucks cups deutschland kaufen" (US search tool, so treat it as a proxy for the DE SERP).
1. kleinanzeigen.de/s-starbucks-cup: used marketplace
2. amazon.com: Munich "You Are Here" mug
3. ebay.com: Germany Starbucks mug
4. etsy.com/market/starbucks_germany
5. otto.de/haushalt/?marke=starbucks: marketplace brand shop
6. starbucks-mugs.com/tag/germany: collector database
7. ebay.de: Germany City Mug 16 oz
8. thecoffeemugshop.de/collections: private collector shop
9. ebay.de: Wiesbaden Global Icon

**Intent:** buy (transactional) plus know (which cups exist). The SERP mixes reusable cups (Cold Cup/Tumbler) with collector mugs. No featured snippet, lots of marketplace listings.
Fan-out: "starbucks cold cup", "starbucks tumbler", "starbucks cup germany", "starbucks city mug".

## Step 2: Head entities
| Entity | Type | sameAs |
|---|---|---|
| Starbucks | Organization | https://de.wikipedia.org/wiki/Starbucks |
| Cold Cup | Thing (product family) | unlinked |
| Tumbler | Thing (product family) | https://en.wikipedia.org/wiki/Tumbler_(glass) (generic, so it isn't used in schema) |
| You Are Here Collection | Thing (collector series) | unlinked |

## Step 4: Sources
- **starbucks.de/de/menu-merchandise-core** (official): 21 product names, no prices/sizes (full list in the draft). Fetched 2026-09-23.
- **otto.de Starbucks brand page:** 50 items. Cold cups €13.49–€79.00, insulated tumblers €45+, mugs €24.95–€39.00, collabs Snoopy/Owala €37.99–€79.00, delivery 3–4 working days, several "fast ausverkauft". Snapshot 2026-09-23, marketplace prices.
- **thecoffeemugshop.de:** series Discovery, You Are Here, Been There, Global Icons, Espresso, Raritäten. Private site, not affiliated; free shipping from €99.
- **starbucks-mugs.com/tag/germany** (fan collector DB): 15+ German YAH cities (München, Berlin, Frankfurt, Hamburg, Köln, Nürnberg, Leipzig, Stuttgart, Augsburg, Wolfsburg, Metzingen, Bremen, Ramstein, Wiesbaden, Heidelberg); Relief München released Aug 2026; Oktoberfest YAH 2019 and a second version 30 Aug 2023.
- **ehrenkaffee.de** (updated Oct 2022): tumbler €7–€23, 355/473 ml, own-cup discount 30 ct. **Stale.** Not used; the host page already has the current €0.50.
- kleinanzeigen/eBay/Etsy/Amazon: marketplace listings only, no editorial content to extract.

## Step 5/6: Entity ledger
| canonical | type | comp. | tier |
|---|---|---|---|
| Starbucks Cups (Sortiment) | Concept | 4 | 1 |
| Cold Cup | Thing | 3 | 1 |
| Tumbler | Thing | 3 | 1 |
| Mug / Tasse | Thing | 4 | 1 (routed to /blog/starbucks-tassen) |
| Edelstahl (SS) | Material | 2 | 2 |
| Kunststoff (Plas) | Material | 2 | 2 |
| Kernsortiment starbucks.de | Concept | 1 | 2 (official source) |
| Otto | Organization | 1 | 2 |
| Limitierte Kooperationen (Snoopy, Owala) | Thing | 1 | 2 |
| Strohhalm-Set / Dome Lid | Thing | 1 | 2 |
| You Are Here / Been There / Global Icon | Thing | 3 | 2 (mention + route only) |
| Relief München (Aug 2026) | Thing | 1 | 3 |
| Farben/Designs (Grid, Terrazzo, Marbled, Ombre, Beans) | Concept | 1 | 3 |

Relationships: Cold Cup —for→ Kaltgetränke · Tumbler SS —for→ heiß + kalt · "SS" —means→ Edelstahl · "Plas" —means→ Kunststoff · starbucks.de —lists without→ Preise · Otto —sells→ Cold Cups 13,49–79 € · Kooperationen —cost→ 37,99–79 € · City mugs —belong to→ Tassen, not Cups.

Dedupe/parking: city-mug series detail is **parked** to /blog/starbucks-tassen (sister page; avoids cannibalising it). Cleaning/microwave rules are already on the host page (section 7), so they're referenced, not repeated.

## Step 7: Information gain
- **Product-name decoder table** (Plas/SS/Glass/Recycled). No competitor explains Starbucks' internal naming, and it answers "is this cup steel or plastic?" before buying.
- The official current range list is dated (23 Sep 2026). Competitors are either marketplaces or stale (2022).
- ⚠️ **Price discrepancy found:** the host page's section 4 table says tumblers cost ca. 12–23 € new. The only 2026 price data found (Otto) starts around 45 €. The 12–23 € figure matches ehrenkaffee's 2022 range, so it's probably stale. Block C adds the Otto data point. **Recommend re-checking the table's "neu" column in a store.**

## Step 8: Heading map
| Level | Heading | Owns |
|---|---|---|
| H3 (in §2) | Starbucks Cups: Was steckt hinter den englischen Produktnamen? | starbucks cups (focus) |
| H3 (in §2) | Welche Starbucks Cups gibt es gerade im Sortiment? | starbucks cold cup / tumbler (LSI) |
| para (in §4) | — | starbucks cups preis (LSI) |

## Step 8e: Links / cannibalisation
Out: /blog/starbucks-tassen (city mugs). The existing section 7 is referenced. There's no cannibalisation inside the page because the online-shop insert covers buying channels, not the range.

## Step 10: FAQ source map
10 FAQs. Q1, Q2, Q3, Q4, Q5, Q10 → starbucks.de core range. Q6, Q7 → Otto snapshot. Q8 → starbucks-mugs.com / thecoffeemugshop. Q9 → starbucks-mugs.com.
