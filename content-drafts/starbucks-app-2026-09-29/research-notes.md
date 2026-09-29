# Research notes: starbucks app (+ Rewards, Geburtstag)

Run date: 29 Sep 2026 · Site: starbuckspreise.com (DE, du-voice) · Blog post · Slug `/blog/starbucks-app`

## Step 1: Intent + SERP
- **Demand:** Google Trends DE estimates (anchor "starbucks kalorien" = 480): "starbucks app" ~1,200/mo, "starbucks rewards" ~140/mo, "starbucks geburtstag" ~10/mo. The biggest peak was 28 Jun – 4 Jul 2026.
- **Intent:** mixed *website* (download or open the app) and *know* (how Rewards works). A navigational SERP is dominated by the app stores and starbucks.de; our angle is the explainer that sits alongside it.
- **SERP (German DuckDuckGo, 29 Sep):** starbucks.de, starbucks.com, play.google.com ×2, starbucks.de, starbucks.com, apps.apple.com ×2. The Google SERP was captcha-blocked.
- **Fan-out (autocomplete):** starbucks app bestellen / deutschland / germany / vorteile / empfehlungscode; starbucks rewards deutschland / einlösen / geburtstag / 150 stars / card / member; starbucks geburtstag gratis / gratis getränk / freigetränk größe / geburtstagsaktion / geburtstagsrabatt; starbucks gutschein guthaben abfragen.

## Step 2: Head-entity sources
| # | Source | Facts used |
|---|---|---|
| S1 | starbucks.de/rewards (WebFetch) | 3 Sterne pro 1 €, regardless of payment method (Card, cash, debit, credit); 150 Sterne = Freigetränk; 450 = Gold; Gold: free syrups + espresso shots, "Gratis-Refill (Filterkaffee oder Tee) innerhalb des selben Besuchs", Geburtstagsgetränk; app: pre-order, star tracking, marketing preferences |
| S2 | starbucks.de/en/faq-rewards | Rewards Stars "valid for 2 years from the date they are credited"; Tier Stars expire within each Tier Year; below 450 in a Tier Year → back to Green; Gold = birthday drink. No size limit, age, referral or top-up limits are stated |
| S3 | apps.apple.com/de/app/starbucks-deutschland/id948562829 | 4.3★ from 4,267 ratings, iOS 16.4+, 75.4 MB, provider Starbucks Coffee Company (Seattle), pre-order "at participating locations", birthday rewards at Gold |
| S4 | starbucks.de/de/starbucks-card | top-up "in nur wenigen Schritten in der App"; app works like the card; balance safe if card or phone is lost; buy the card in participating stores |
| S5 | play.google.com (id com.starbucks.de), from the search result | Android availability |
| S6 | starbucksfreiburg.de (Freiburg Hbf ordering page) | example prices: Caffè Latte 4,90; PSL 6,20; PS Frappuccino 7,40; Soy Protein Matcha 7,90 |
Head entities: Starbucks® Deutschland App (Thing, app-store sameAs); Starbucks (Q37158, verified). Loyalty program Q1426546 and Mobile app Q620615 verified via wbsearchentities.

## Step 3: Metadata
- Title: Starbucks App Deutschland: Rewards, Sterne & Geburtstag 2026 (60 chars)
- H1: Starbucks App Deutschland: Rewards, Sterne und Geburtstagsgetränk erklärt
- Meta: see meta.json (157 chars)
- Slug: /blog/starbucks-app

## Step 4: Competitors
| # | URL | Date | Headings / notes |
|---|---|---|---|
| C1 | burgerspreises.de/starbucks-rewards-deutschland/ | 08.02.2026 | H2: Was ist Starbucks Rewards Deutschland? / Wie funktioniert das Starbucks-Bonusprogramm…? / Vorteile einer Mitgliedschaft… / So melden Sie sich… an / Verwendung der Starbucks Deutschland App / Maximieren Sie Ihre Starbucks-Prämien… / FAQ / Warum es sich lohnt…. H3 include "Freunde werben" (not supported by starbucks.de) and "Mobile Bestell- und Bezahlfunktion". FAQ verbatim: "Verfallen Sterne?", "Kann ich meine Prämien in allen Starbucks-Filialen in Deutschland einlösen?", "Was passiert, wenn ich mein Handy verliere?", "Kann ich auch ohne die App Sterne sammeln?". Uses Sie-voice. |
| C2 | goldmarie-friends.de/blog/starbucks-rewards-das-beste-kundenbindungsprogramm/ | undated (~2016) | US 2016 program switch, 1 star per $2, "160 in Germany" stores. **Stale/US**, used only as background |
| C3 | starbucks.de/rewards + FAQ (official) | live | S1/S2 |
| C4 | apps.apple.com (official listing) | live | S3 |

## Step 5/6: Entities, tiers, relationships
- **Tier 1:** Starbucks App, Starbucks Rewards, Sterne, Freigetränk, Gold-Status, Geburtstagsgetränk, Starbucks Deutschland.
- **Tier 2:** Starbucks Card, Mobile Order, teilnehmende Filialen, Tier-Jahr/Tier-Sterne, Green, Refill, Sirup/Extra-Shot, App Store/Google Play, Guthabenschutz, Empfehlungscode.
- **Tier 3:** Seattle publisher, Datenschutz, eigener Becher.
- **Relationships:**
  - 1 € —earns→ 3 Sterne.
  - 150 Sterne —redeem→ Freigetränk (= 50 €).
  - 450 Sterne/Tier-Jahr —unlocks→ Gold (= 150 €).
  - Gold —includes→ Sirup/Shots gratis, Refill, Geburtstagsgetränk.
  - Rewards-Sterne —valid→ 2 Jahre.
  - Tier-Sterne —expire→ end of Tier-Jahr.
  - <450 → Green.
  - App —pays with→ Starbucks Card.
  - Card registered —protects→ balance.
  - Mobile Order —available at→ participating stores.
- **Parked:** "Freunde werben" (C1 claim, not on starbucks.de, so answered as not offered with a date stamp); PayPal/Apple Pay in app (unverified); the own-cup discount amount (0,30 vs 0,50 € unverified sitewide, see project memory), so it is deliberately not quantified.

## Step 7: Information gain
- No competitor calculates **what a star is worth**. Our additions are the redemption-value table (9.8–15.8 % back per 50 €) and the yearly visitor-type table.
- C1 claims a "Freunde werben" program. We state plainly that it is not on starbucks.de (Sept 2026).
- We explain the Gold-only birthday drink clearly (autocomplete shows people search "geburtstag gratis getränk").

## Step 8: Heading map
| Level | Heading | Phrase | Carries |
|---|---|---|---|
| H1 | Starbucks App Deutschland: Rewards, Sterne und Geburtstagsgetränk erklärt | starbucks app | app, rewards |
| H2 | 1. Was kann die Starbucks App in Deutschland? | app deutschland / vorteile | features, store data |
| H2 | 2. Wie funktioniert Starbucks Rewards? | rewards deutschland | 3/€ |
| H3 | Wie viele Sterne brauchst du für ein Freigetränk? | 150 sterne | value table |
| H3 | Verfallen Starbucks Sterne? | sterne verfallen | 2 years, tier |
| H2 | 3. Was bringt der Gold-Status? | gold status | 450, perks |
| H2 | 4. Bekommst du … ein Getränk zum Geburtstag? | geburtstag gratis getränk | Gold-only |
| H2 | 5. Wie bestellst du mit der Starbucks App vor? | app bestellen | HowTo 5 steps |
| H2 | 6. Wie lädst du die Starbucks Card in der App auf? | starbucks card | top-up, protection |
| H2 | 7. Lohnt sich die Starbucks App? | lohnt sich | yearly table |
| H2 | Häufig gestellte Fragen | — | 11 Q |

**Internal links:**
- /blog/starbucks-in-der-naehe
- /blog/starbucks-angebote
- /blog/starbucks-becher

**Add later:**
- A link from /blog/starbucks-angebote §3 (Rewards) to this page.
- A link from the PSL draft's FAQ "Rewards" to this page.

**Cannibalisation:** /blog/starbucks-angebote touches Rewards in one section, so it stays the deals hub and this page becomes the Rewards/app hub.

## FAQ source map
- kostenlos: fan-out.
- Sterne pro Euro: S1.
- Ausgeben für Freigetränk: S1.
- ohne App: C1 FAQ verbatim idea.
- Empfehlungscode: autocomplete.
- Verfall: C1 FAQ / S2.
- Handy verloren: C1 FAQ / S4.
- jede Filiale: C1 FAQ.
- Ausland: inferred scope.
- Gold: S1/S2.
- eigener Becher: cross-link.

## Open flags (need user)
1. **Birthday drink = Gold only.** This follows the official FAQ. A search snippet from the DE registration text mentions a birthday drink at sign-up in general. Check in the app whether Green members get anything.
2. "Zum Vorbestellen brauchst du ein Rewards-Konto" and "in der App zahlst du mit dem Card-Guthaben" come from the app/card descriptions and are not explicitly stated as the only way. Verify this in the app.
3. The "Ausland" FAQ (German stars not valid abroad) is inferred from the app being a DE-specific program. Verify it.
4. The free-drink value table uses Freiburg Hbf prices; other stores may differ.
5. The hero image should be a phone showing a generic coffee-app screen, with no Starbucks logo.
