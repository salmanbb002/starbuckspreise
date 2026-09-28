# Research notes: "starbucks becher aktuell" (260/mo, KD 32)

Run date: 2026-09-28. Site: starbuckspreise.com (de-DE). Page type: blog post, new standalone.

## 0. Cannibalisation decision
The calendar marked this row "Merge-Recommended → starbucks-becher". The user chose the **hybrid** option (2026-09-28): a standalone post for "becher aktuell" with a different angle, which is **what is new or limited right now, with dates**. The existing `starbucks-becher` page is the evergreen guide to types, sizes, price, discount and care. This page only covers the time-sensitive part and links to the evergreen guide for everything else. Watch GSC for overlap on "starbucks becher" (head term), because both pages carry it.

## 1. Intent + SERP
- Intent: *know* (fresh). Secondary: *visit-in-person* (where do I get it).
- SERP (WebSearch, 2026-09-28): starbucksathome.com "Deine Tasse" FAQ (promo ended; the page now returns 404), starbuckspreise.de/starbucks-tasse, starbucks.de, vergleich.org/starbucks-tassen, eBay listings, thecoffeemugshop.de. No featured snippet was visible. Shopping and eBay results dominate.
- Fan-out: "starbucks becher neu", "starbucks herbst 2026 becher", "starbucks snoopy becher", "bearista deutschland", "starbucks becher 2026", "starbucks weihnachtsbecher".

## 2. Head entities
- Starbucks (Q37158).
- Peanuts (Q7115636), Snoopy (Q207369), It's the Great Pumpkin, Charlie Brown (Q596994, 1966). All three IDs were verified through the Wikidata/Wikipedia API. The first guesses were wrong and have been fixed.
- Starbucks Rewards and the Bearista Cold Cup have no Wikidata entry, so they are recorded as unlinked.

## 3. Sources (fetched)
| # | Source | Date | Facts used |
|---|---|---|---|
| S1 | starbucks.co.uk/merchandise/autumn-2026 (curl) | fetched 2026-09-28 | Autumn 2026 product names and oz sizes; "For a limited time only, while stocks last. Range availability may vary by store." |
| S2 | starbucks.de/de/menu-merchandise-core (curl) | fetched 2026-09-28 | Full core list, identical to the 2026-09-23 snapshot. There is no seasonal merch page on .de (probed seasonal/herbst/autumn/peanuts etc., all 404). |
| S3 | wienerbezirksblatt.at/starbucks-peanuts | 2026-09-18 | Peanuts launch 15.09.2026 (Austria); Snoopy Bearista-style glass tumbler only for Rewards members; cups, tumblers, mugs, bags; "solange der Vorrat reicht" |
| S4 | aktien.news Snoopy/SpongeBob | 2026-09-19 | Peanuts fall collection launched on a Tuesday; Snoopy glass cold cup; about 40 USD on the Starbucks website, Etsy up to 120 USD (~200 %); nearly sold out online |
| S5 | watson.de | 2026-01-24 | Bearista Cold Cup in DE from 23.01.2026; earlier in AT/CH; Vienna sold out in under 1 hour; strictly limited |
| S6 | wunderweib.de | 2026-01-22 | DE launch 23.01.2026; max. 2 cups per purchase; Hamburg named |
| S7 | berliner-kurier.de | 2026-01-23 | Berlin sold out in about 20 minutes |
| S8 | mydealz.de/magazin | 2026-07-14 | Pink Bearista: 13.07.2026 Rewards members, 14.07.2026 everyone; coffee houses only, not online in DE; max. 2; no restock; US 29.95 USD; winter 2025 edition = green hat |
| S9 | packaging-journal.de | 2025-05-14 | Mineral-coated hot cup (diatomaceous earth), cellulose lid; rollout from May 2025 with DE among the first markets (IT, DE, FR, SE, AT, CH, ES, HU); Transcend, Ystrad Mynach, Wales; home-compostable and recyclable |
| S10 | food-service.de | 2025-05-09 | Corroborates the DE rollout from May 2025 and that the look is unchanged |
| S11 | WebSearch summary of the starbucksathome.com "Deine Tasse" FAQ | — | Promo ran 16.06.2025–19.10.2025. The page itself now returns 404 (curl, 2026-09-28), so this was **not fetched directly** (flag). |
| S12 | Starbucks Stories EMEA / about.starbucks.com Peanuts release (search results only; 403 via WebFetch, JS wall via curl, Chrome extension offline) | 2026 | Global launch 15.09 in participating coffeehouses including Europe; 60th anniversary. **Germany is not explicitly confirmed** (flag). |

Competitors (Step 4): starbuckspreise.de/starbucks-tasse (headings: history, types, where to buy, benefits, collector tips; no FAQ; own-cup discount 0,30 €), thecoffeemugshop.de Neuheiten 2026 (reseller of collectible city mugs DS/YAH/BTS, 37,99–95,99 €, no German cities in the first 30), vergleich.org (403), starbucksathome (404). The fourth distinct domain was not reachable, and the news pages S5–S8 were used as the substitute set.

## 6. Entity ledger (tiers)
- Tier 1: Starbucks; Starbucks Becher (seasonal/limited); Peanuts-Kollektion / Snoopy-Glasbecher; Bearista Cold Cup; Herbstkollektion 2026; Kernsortiment.
- Tier 2: Starbucks Rewards (early access); limit of 2 per person; Zweitmarkt/resale; Cold Cup; Tumbler; kompostierbarer Pappbecher; Pfandbecher 2,50 €; Holiday-Kollektion; "Deine Tasse" promo.
- Tier 3: You Are Here / Been There series (linked out to the tassen page); EU packaging regulation (linked out); Owala (skipped).

Relationships: Peanuts collection → launched → 15.09.2026; Snoopy glass cup → Rewards-only → in AT; Bearista → DE launch → 23.01.2026; Pink Bearista → Rewards presale → 13.07.2026; limited cups → sold only in → coffee houses (not online in DE); limited cups → limit → 2 per purchase; Autumn range → availability → varies by store; hot cup → coating → mineral (diatomaceous earth) since May 2025; "Deine Tasse" → ended → 19.10.2025.

## 7. Information gain
None of the competitors has a dated list of 2026 drops in Germany. This page adds:
- **Becher-Kalender 2026** (table with date, cup, access, limit and outcome).
- A step list on how to get a limited cup.
- A split between the current and core ranges, with the .de core list re-verified.
- A stale-promo correction: "Deine Tasse" has ended, while competitors still link to it.

## 8. Heading map
H1 Starbucks Becher aktuell (focus) → H2 1 welche gibt es aktuell (Tier-1 split) → H2 2 Herbstkollektion 2026 (H3 Becher und Tumbler; H3 auch in Deutschland?) → H2 3 Peanuts (H3 Preis) → H2 4 Becher-Kalender (info-gain) → H2 5 wie bekommst du (numbered steps) → H2 6 Kernsortiment → H2 7 Pappbecher neu → H2 8 Gratis-Aktion? → H2 9 Holiday next → FAQ (12).

## 8e. Internal links
Outbound: /blog/starbucks-becher (plus the #welche-starbucks-cups… and #rabatt-und-pfand anchors), /starbucks-in-meiner-naehe, /blog/starbucks-kapseln-angebot, /blog/starbucks-tassen. Inbound to add: starbucks-becher §2 "aktuelles Sortiment" → this page; kaffeebecher-von-starbucks §1 (Saisonkollektionen) → this page; blog index card; sitemap.
