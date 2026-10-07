# Research notes – starbucks stanley (2026-10-07)

## 1. Keyword, intent, SERP
- Primary: **starbucks stanley** · ~50/mo (Research_Oct2026, peak 16–22 Nov 2025). Sheet decision was "Merge into starbucks-becher"; that page had no Stanley mention. Owner asked for a standalone post.
- Intent: know-simple (is it sold in Germany?) + buy. SERP (WebSearch, US-proxied): eBay.de, Kleinanzeigen, breuninger.com (Stanley), starbuckspreise.de/starbucks-tasse, lecker.de, lionshome.de, and two shop domains with "stanley" in the name whose operators could not be verified. PAA not captured.
- Fan-out (Autocomplete_Oct2026): starbucks stanley / 2025 / 2026 / cup / cup 2026 / japan / sakura / thailand / tumbler / x stanley / x stanley cup.

## 2. Head entities
| Entity | Type | sameAs | Facts |
|---|---|---|---|
| Stanley | Organization | en.wikipedia.org/wiki/Stanley_(drinkware_company) | maker of the Quencher; EU shop eu.stanley1913.com (30 oz = 0,89 l, 40 oz = 1,18 l) |
| Starbucks x Stanley Quencher | Product | – (unlinked) | 40 oz stainless tumbler, limited colours |
| Starbucks | Organization | wikidata Q37158 | DE stores run by AmRest |

## 3. Sources
| # | Source | Date | Facts used |
|---|---|---|---|
| S1 | about.starbucks.com/press/2024/thoughtful-mothers-day-gifts-at-starbucks | 9 Apr 2024 | Sky Blue Stanley Quencher 40 oz, $49.95 |
| S2 | about.starbucks.com/press/2024/new-starbucks-merchandise-to-match-all-the-summer-vibes | 7 May 2024 | Sunset Gradient Quencher 40 oz, $54.95, participating U.S. stores |
| S3 | about.starbucks.com/press/2024/new-starbucks-merchandise-for-on-the-go-summer-sipping | 25 Jun 2024 | Lime Green Quencher 40 oz, $54.95 |
| S4 | about.starbucks.com/press/2024/starbucks-new-fall-merchandise | 21 Aug 2024 | Olive Green Quencher 40 oz, $54.95, from 22 Aug |
| S5 | about.starbucks.com/stories/2024/the-holidays-are-back-at-starbucks-beginning-nov-7 | 30 Oct 2024 | Berry Pink Glitter Stanley Tumbler 40 oz, $54.95, from 7 Nov |
| S6 | today.com/food/news/starbucks-pink-stanley-cup-target-rcna132157 | 3 Jan 2024 | Winter Pink, Starbucks stores at Target only, $49.95, "It will not be restocked", third co-branded release |
| S7 | cnbc.com/2024/01/05/… | 5 Jan 2024 | eBay bids over $200; Target limit two per person |
| S8 | variety.com/2023/shopping/news/starbucks-stanley-tumbler-… | 14 Nov 2023 | red holiday Quencher released 2 Nov 2023; resale from ~$155 |
| S9 | thekrazycouponlady.com/tips/store-hacks/stanley-starbucks-cup | upd. 7 Nov 2024 | first collab May 2023, Target-exclusive peach-pink, ~$45; 2024 drop dates |
| S10 | wwdjapan.com/articles/2337446 | 2 Mar 2026 | Sakura wave 2 on 4 Mar 2026 (online 3 Mar); Stanley tumbler 414 ml ¥5.200, Stanley bottle 473 ml ¥5.700 |
| S11 | about.starbucks.com 2026 holiday merch + menu previews | 5 Oct 2026 | US holiday from 5 Nov; no Stanley item named ("first look") |
| S12 | starbucks.de/de/menu-merchandise-core · starbucksfreiburg.de · starbucks.co.uk/merchandise/autumn-2026 | 7 Oct 2026 | no Stanley item; DE steel cups: Cold Cup Dual Lid Green 26,90 €, Tumbler Grid Green 24,90 €, Tumbler Luxor Black 24,90 €, Cold Cup Beans 24,90 €, Tumbler Lucy 19,90 €; Venti cold cup 24 oz (709 ml) |
| S13 | zoll.de (Internetbestellungen aus Nicht-EU-Staaten) | 7 Oct 2026 | EUSt 19 % from 0 €; since 1 Jul 2026 flat duty 3 € per goods category for consignments up to 150 €; from 150 € regular duty on total incl. postage |
| S14 | starbucks.de order menu (product JSON 106985) | 7 Oct 2026 | Einwegbecher +0,05 €, Mehrwegbecher +2,50 € Pfand |
- about.starbucks.com read with headless Chrome (curl/WebFetch 403). thekitchn.com → 403 (PerimeterX). thestreet.com → empty. eu.stanley1913.com search → 429.

## 4. Competitors
C1 KCL (S9): release schedule, why popular, dupes. C2 Variety (S8): where to buy, resale, dupes. C3 TODAY (S6): launch chaos, price, no restock. C4 CNBC (S7): resale prices. starbuckspreise.de/starbucks-tasse ranks for the query but does not mention Stanley.
Extraction (shuffled): Quencher, FlowState, 40-ounce, vacuum-insulated, Target-exclusive, Winter Pink, limited-edition, resale, eBay, campouts, restock, dupes, $49.95, $54.95.

## 5. Entity ledger → entities.json
T1: Starbucks Stanley Cup, Stanley, Quencher, Starbucks Deutschland, Preis. T2: 40 oz, Winter Pink, Target, Wiederverkauf, Tumbler, Edelstahl, Sakura-Kollektion 2026, Einfuhrumsatzsteuer, AmRest, Tumbler Luxor Black. T3: Berry Pink Glitter, Sunset Gradient, Thailand, Dupes (parked: US retailers).
Relations: Starbucks x Stanley —sold in→ USA, Asia · not —sold in→ Germany · price —rose→ $49.95 → $54.95 (May 2024) · Winter Pink —exclusive to→ Target · import —triggers→ 19 % EUSt + 3 € · Tumbler Luxor Black —alternative→ 24,90 €.

## 6. Information gain
A sourced "no" for Germany, the release table with source per row, import cost under the rule in force since 1 Jul 2026, and German alternatives with prices.

## 7. Internal links
becher, becher-aktuell, tassen, groessen, weihnachten. Inbound added from becher. Cannibalisation: /blog/starbucks-becher owns "tumbler/thermobecher"; this page owns "stanley".
