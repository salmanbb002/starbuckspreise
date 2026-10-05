# Research notes – starbucks black friday (run 2026-10-05, calendar slot 2026-10-23)

## Intent / SERP (WebSearch, US-proxied, German queries, 5 Oct 2026)
- ~60/mo (Research_Oct2026, Trends estimate ±50 %), seasonal, peak 23–29 Nov 2025. Intent: know (is there a deal / when) + buy (capsules, beans at retailers).
- Results are dominated by US pages (primetimer, rollingout, milehighonthecheap: "$5 eGift with $25 spend", groupon) and by German deal aggregators (mydealz, aktionspreis.de, supersales.de, prospektangebote.de, blackfriday.de/nespresso, starbuckspreise.de Kapseln-Angebot). No German editorial article answers the query for Starbucks Deutschland → clear gap.
- SERP features seen: none reliable via the search tool (no rendered SERP — Chrome extension was not connected). PAA not captured; FAQ built from fan-out + competitor FAQs.
- Fan-out used: black friday 2026 datum, black week, cyber monday, starbucks kapseln black friday, becher black friday, gutschein/geschenkkarte bonus, rabattcode, geöffnet.

## Head entities (Step 2)
- Black Friday – https://de.wikipedia.org/wiki/Black_Friday (Friday after Thanksgiving, 23–29 Nov, start of Christmas shopping; "Black Week" = extension).
- Cyber Monday – https://de.wikipedia.org/wiki/Cyber_Monday (Monday after Thanksgiving; Verbraucherzentrale NRW warns about discounts measured against UVP).
- Starbucks – Wikidata Q37158; DE stores operated by AmRest Coffee Deutschland.

## Competitors fetched (Step 4)
| # | URL | Result |
|---|---|---|
| C1 | blackfriday.de/nespresso | fetched – dates 2026 (Black Week 23–30 Nov, BF 27 Nov, weekend 28–29, CM 30 Nov), "Noch kein Deal für 2026", past Nespresso deals 2017–2022 |
| C2 | aktionspreis.de/hersteller/starbucks-angebote | fetched – week 5–11 Oct 2026: Starbucks Coffee 220 ml ab 1,29 € (48 %), Nespresso Kapseln 10 St ab 3,69 € (18 %, 0,37 €/St) |
| C3 | starbuckspreise.de/starbucks-nespresso-kapseln-angebot | fetched – headings + FAQ (Black Friday, Prime Day, Weihnachten/Ostern as sale periods), price table 10/80/120 caps |
| C4 | supersales.de/marke/starbucks | fetched – 156 products, 22 on sale, up to 36 % |
| C5 | mydealz.de search "starbucks" | fetched – Amazon Ristretto Shot 100 caps 19,84 € Spar-Abo vs 38,70 €; Rossmann 3,69 € / 2,94 € with coupon; Kaufland 220 ml 0,79 € vs 2,49 €; Jawoll 1,29 € vs REWE 2,49 €; Corporate Benefits 15 %; KwK 150 Sterne (deal dates not shown on listing) |
| – | prospektangebote.de/geschaefte/starbucks/black-friday | HTTP 202 empty body – not usable, skipped |
| – | mydealz.de/gruppe/kaffee | fetched – no Starbucks deal; guidance "guter Kapselpreis unter 20 Cent" (generic compatible capsules) |

## Fact ledger
| Fact | Source |
|---|---|
| BF 2026 = 27 Nov; Black Week 23–30 Nov; CM 30 Nov | blackfriday.de (C1) |
| BF 2025 = 28 Nov | blackfriday.de snippet (Black Week 24 Nov–1 Dec 2025) + calendar |
| BF 2027 = 26 Nov | calendar arithmetic (4th Thursday 25 Nov 2027) |
| No DE café promo announced; none found for 2025 | starbucks.de pages fetched 5 Oct + searches (absence of evidence – FLAG) |
| No official DE online shop | own check, /blog/starbucks-angebote |
| US 2025: $5 bonus eGift with $25 | search-result titles only (milehighonthecheap, Facebook group) – FLAG, snippet-level |
| Starbucks Card only in AmRest stores, DE only | starbucks.de FAQ + AGB (fetched 5 Oct) |
| Capsule prices, chilled prices | C2, C5 |
| "üblicher Preis rund 4,49 €" | derived: 3,69 € ÷ 0,82 (aktionspreis 18 %) – FLAG derived |
| Grande Cup 330 ml 1,99 € (UVP 2,89 €) | /blog/starbucks-angebote (Lidl KW 39) |
| Pike Place 450 g 14,89 € → 33,09 €/kg | research 3 Oct (Google Shopping), cold-brew notes |
| Rewards 3 Sterne/€, 150 = Freigetränk | starbucks.de AGB |
| Weihnachtskarte start 4 Nov 2024 / 6 Nov 2025 | weihnachten notes 2 Oct |
| Kapseln/Bohnen = Nestlé (Starbucks at Home) | /blog/starbucks-angebote, kapseln-angebot |
| UVP warning | de.wikipedia Cyber Monday (Verbraucherzentrale NRW) |

## Tiers / relationships
T1: Black Friday, Starbucks (Deutschland), Datum 27.11.2026, Angebote/Rabatte, Kapseln. T2: Black Week, Cyber Monday, Bohnen, Eiskaffee/Chilled, Becher, Online-Shop (keiner), Starbucks Rewards, Starbucks Card, Amazon/Spar-Abo, Preis pro Kapsel, UVP. T3: Thanksgiving, Prime Day, Corporate Benefits, Verbraucherzentrale NRW, Nestlé.
- Black Friday —fällt 2026 auf→ 27. November · Starbucks DE —hat→ keinen Online-Shop · Rabatte —kommen von→ Händlern · Kapsel —guter Preis→ < 0,30 € · Starbucks Card —gilt nur in→ AmRest-Stores · Weihnachtskarte —läuft während→ Black Week.

## Information gain (Step 7)
All sources are either US content or price lists. Nobody states plainly that Starbucks DE has no café promo and no shop. Original elements: (1) regular-vs-deal price table, (2) worked price-per-capsule calculation with thresholds, (3) 2026 date table.

## Heading map (Step 8)
| H | Heading | Phrase | Question |
|---|---|---|---|
| H1 | Starbucks Black Friday 2026: Wo es wirklich Rabatte gibt (und wo nicht) | starbucks black friday | — |
| H2 | 1. Wann ist Black Friday 2026? | black friday 2026 datum | when |
| H2 | 2. Gibt es bei Starbucks Deutschland Black-Friday-Angebote? | starbucks black friday angebote | is there a deal |
| H3 | Gelten die Black-Friday-Deals aus den USA auch in Deutschland? | starbucks black friday usa | US deals |
| H2 | 3. Welche Starbucks Produkte sind am Black Friday reduziert? | kapseln/bohnen black friday | what |
| H2 | 4. Woran erkennst du einen echten Starbucks Deal? | deal check | how to judge |
| H2 | 5. Wie sparst du am Black Friday im Starbucks Coffee House? | sparen filiale | café |
| H2 | 6. Lohnt sich das Warten auf den Black Friday? | lohnt sich | decision |

## Internal links / cannibalisation
Out: app, gutschein, kapseln-angebot, kaffeebohnen, becher-aktuell, weihnachten, angebote, preise. In: kapseln-angebot ("Black Friday"), angebote §5. Cannibalisation: /blog/starbucks-angebote (evergreen offers) and /blog/starbucks-kapseln-angebot mention Black Friday in one line each; this page owns the dated query.

## FAQ source map
geöffnet (US SERP pattern "will Starbucks be open") · Gratisgetränke (US SERP) · Rabattcode (fan-out) · Kapseln günstigsten (C3 FAQ "Wo finde ich die günstigsten Preise") · Becher (fan-out) · Geschenkkarte Bonus (US SERP) · Cyber Monday (fan-out) · 2027 (fan-out) · Sterne Handel (own angebote FAQ) · Spar-Abo (C5) · Kapseln = Café? (C3).
