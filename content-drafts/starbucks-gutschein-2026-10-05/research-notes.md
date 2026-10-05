# Research notes – starbucks gutschein (run 2026-10-05, calendar slot 2026-10-26; absorbs "starbucks geschenkkarte")

## Intent / SERP (WebSearch, US-proxied, German queries, 5 Oct 2026)
- ~30/mo + geschenkkarte (Trends estimate ±50 %), seasonal peak mid-December. Intent: buy (where to get a gift card) + know (redeem, balance, validity); secondary: discount-code seekers.
- Organic: bitrefill, geschenkkarten.de, eneba, kartedirekt (product + blog), wunschgutschein.de, giftcard.de, coingate; plus starbucks.de terms, hrmony help article, kaffeenavigator (2015), bezahlen.net, gcb.today balance checker.
- SERP is almost entirely resellers. No rendered SERP available (Chrome extension not connected) → PAA not captured.

## Head entities (Step 2) – official source
- Starbucks Card – starbucks.de/de/starbucks-card, /de/faq-starbucks-card, /de/terms-of-use (all fetched by curl 5 Oct 2026). Issuer: AmRest Coffee Deutschland Sp. z o.o. & Co. KG.
- Geschenkkarte – https://de.wikipedia.org/wiki/Geschenkkarte (prepaid stored-value card).

## Competitors (Step 4)
| # | URL | Result |
|---|---|---|
| C1 | wunschgutschein.de/pages/starbucks | fetched – 15–200 €, universal voucher, 500+ shops, 3 Jahre gültig, Post gratis / E-Mail 15 Min |
| C2 | coingate.com/de/gift-cards/starbucks | fetched – eGift per E-Mail ~1 Min, Region Deutschland, "verfällt nicht", FAQ (Bargeld? Speisen? Guthaben prüfen? international? SMS?) |
| C3 | kaffeenavigator.de (17 Jan 2015) | fetched – outdated: Postbank 800 Filialen, 5–150 € je Aufladung, starbucks.de/card balance check |
| C4 | bezahlen.net/ratgeber/starbucks-reward | fetched – outdated: 1 Stern je 2 €, REWE 2.800 Märkte, Deutsche Post; cards not valid across countries |
| – | kartedirekt.de blog + product, geschenkkarten.de, giftcard.de, bitrefill, hrmony.zendesk | HTTP 403 (WebFetch and curl) – not read; only search snippets known. Substituted C2–C4. |
| – | eneba | "page currently unavailable" |

## Fact ledger (all starbucks.de, fetched 5 Oct 2026 unless noted)
| Fact | Source |
|---|---|
| "grundsätzlich als Gutschein und wie Bargeld zu behandeln" | FAQ Starbucks Card |
| Card only in store, not online, except digital card in app; franchise stores excluded | FAQ |
| Only AmRest-run houses; list of Lizenzstores (Berlin Zoo, BER T1, Erfurt Hbf, FRA T1 B/C, T2, The Squaire, HH Hbf Südsteg+West, HH Airport, Dammtor, Stuttgart Hbf, Bremen HBF, Mainz HBF, 8 Raststätten) | FAQ |
| Filter "Redeem Rewards" in Store Locator | FAQ |
| Register with 16-digit number + 8-digit PIN | FAQ |
| No fees on unused balance; loss → e-mail Starbucks.Gaesteservice@amrest.eu, balance frozen, replacement card by post, free | FAQ |
| Min 5 €, max 250 € per month; top-up with Kreditkarte/EC/Bargeld in store, Kreditkarte online | AGB |
| Auto reload: threshold 10–75 €, amount 5–75 € | AGB |
| No fees for issue/activation/use/top-up; "Es gelten die gesetzlichen Verjährungsfristen" | AGB |
| No payout; registration may be removed after 3 years inactivity; refund if Starbucks terminates | AGB |
| 3 Sterne/€, 150 Sterne = Free Drink; birthday voucher expires after 30 days | AGB |
| Registered cards are personal, not transferable | AGB |
| Balance on receipt and on starbucks.de; no statements | AGB |
| Verjährung "in der Regel drei Jahre zum Jahresende" | general German law (§§ 195, 199 BGB), not fetched – FLAG |
| mydealz: KwK 150 Sterne each | mydealz listing, undated – FLAG (conflicts with /blog/starbucks-app "kein offizielles Programm, Stand Sept 2026") |

## Tiers / relationships
T1: Starbucks Gutschein, Starbucks Card, kaufen, einlösen, Guthaben. T2: Geschenkkarte, Starbucks App, AmRest, Lizenzstore, Registrierung (16/8), Mindestbetrag 5 €, 250 €/Monat, Gültigkeit/Verjährung, Auszahlung, Rabattcode, Starbucks Rewards, WUNSCHGUTSCHEIN. T3: CoinGate, Store Locator-Filter, automatische Aufladung, Geburtstagsgutschein.
- Starbucks Card —wird ausgegeben von→ AmRest · —gilt nur in→ AmRest-Coffee-Houses · —lädt ab→ 5 € · Registrierung —schützt→ Guthaben · Guthaben —wird nicht→ ausgezahlt.

## Information gain
Resellers explain only their own product; old guides list sales points that Starbucks' FAQ no longer names. Original: (1) buying-route comparison table, (2) full official list of non-accepting Lizenzstores, (3) rules table (5 €/250 €/auto reload), (4) correction of outdated Postbank/REWE claims.

## Heading map
H1 Starbucks Gutschein: Geschenkkarte kaufen, einlösen und Guthaben prüfen (2026) · H2 1 Was ist ein Starbucks Gutschein? · 2 Wo kann ich einen Starbucks Gutschein kaufen? (H3 Coffee House / App / Drittanbieter) · 3 Wie viel Guthaben passt auf eine Starbucks Card? · 4 Wo kann ich den Starbucks Gutschein einlösen? (H3 Ausland / Was bezahlen) · 5 Wie prüfe ich das Guthaben? (HowTo; H3 Registrieren) · 6 Wie lange gültig? · 7 Gutscheincodes mit Rabatt? · 8 Wie verschenke ich richtig?

## Internal links / cannibalisation
Out: app, flughafen, angebote, black-friday, preise. In: app, menu, angebote, flughafen ("Starbucks Card"). Cannibalisation: /blog/starbucks-menu §8 and /blog/starbucks-app both explain the Card briefly; this page is now the canonical Card/Gutschein page (both link here).

## FAQ source map
online kaufen (SERP) · REWE/dm/Tankstelle (C3/C4 claims) · Mindestbetrag (AGB) · Auszahlung (C2 FAQ "gegen Bargeld") · verfällt (C2) · Flughafen/Bahnhof (hrmony snippet + FAQ) · App vorbestellen (own app page) · mehrere Karten (C3 "Guthaben übertragen") · funktioniert nicht (AGB) · Sterne (AGB) · USA (C2 "international") · WUNSCHGUTSCHEIN (C1).
