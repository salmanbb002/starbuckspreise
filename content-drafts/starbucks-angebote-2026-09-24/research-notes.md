# Research notes: „starbucks angebote“ (new post)

Run date: 2026-09-24. Keywords "starbucks angebot" 320 (KD 15) + "starbucks angebote" 140 (KD 20). The workbook said "merge into starbucks-kapseln-angebot", but the SERP intent is **all Starbucks deals** (flyer portals for chilled coffee, capsules and beans + coupon sites), not capsules only. So it's a new post that links to kapseln-angebot for the capsule detail.

## Step 1: SERP + intent
Query "starbucks angebote deutschland aktuell": discounto.de, kaufda.de, speisekartemenus.de, aktionspreis.de (x2), marktguru.de, prospektguru.de, meinprospekt.de. Coupon SERP: mydealz, sparwelt, couponster, gutschein.pro.
Intent: **buy/deal**. Dominated by flyer aggregators (retail products), with a secondary intent for in-store discounts/codes. No snippet.
Fan-out: "starbucks angebot diese woche", "starbucks gutschein", "starbucks rabatt", "starbucks kapseln angebot".

## Step 2: Head entities
Starbucks (Org, wiki) · Starbucks Rewards (unlinked) · Starbucks at Home / Nestlé (Org, https://de.wikipedia.org/wiki/Nestl%C3%A9) · Starbucks Chilled Classics (unlinked) · retailers Lidl, REWE, Kaufland, ALDI, EDEKA, Rossmann, METRO (Orgs).

## Step 4: Sources
- **marktguru.de/b/starbucks** (fetched 24 Sep): active offers: Lidl Grande Cup 330 ml 1,99 € (23–26 Sep 2026), REWE capsules Smooth Caramel 3,69 € (51 g) or House Blend Lungo (20–26 Sep). Expired: August 2026 offers at PENNY, EDEKA, Marktkauf (Frappuccino, Chilled Coffee).
- **kaufda.de** (fetched): KW 39: Grande Cup Chilled Coffee Lidl 1,99 € vs UVP 2,89 €; REWE Smooth Caramel 3,69 €; retailers ALDI Nord, EDEKA, ALDI SÜD, Lidl, Kaufland, Marktkauf, Netto, REWE.
- **discounto.de** (fetched): Frappuccino Creamy Coffee 1,49–2,49 €, Caffè Latte 2,99 €, Caramel Macchiato Eiskaffee 2,99 €, Nespresso capsules 4,69 €; retailers ALDI Nord, Rossmann, myTime, Lidl, REWE, Kaufland; valid until 3 Oct 2026. **Product→retailer mapping not given, so the draft doesn't assign retailers to products except the two explicit KW39 deals.**
- Search snippet: cheapest 1,49 € at METRO until 5 Sep 2026 (product not specified), so it's only used to name METRO as a retailer.
- **mydealz Magazin (15 Apr 2026)**: GLAMOUR25, 25 % off one handmade drink, 14 Mar–12 Jun 2026, participating DE coffee houses, once per person, not combinable.
- **starbucks.de/en/faq-rewards** (fetched 23 Sep): 3 stars/€, 150 = free drink, Gold 450/tier year, Gold perks. **starbucks.de/en/rewards**: "exclusive offers", early access.
- **Site becher page**: own cup 0,50 € discount, Pfandbecher 2,50 €. **Site menu.js**: Caffè Latte 4,59 €, Iced Caffè Latte 5,40 €.
- Starbucks at Home "Deine Tasse" promo: from the 23 Sep research (T&C excerpt; the direct fetch was 403).
- Not used: "free shipping from 50 € in the Starbucks online shop" (coupon-site claim, contradicts our finding that there's no DE online shop), and coupon-portal "50 %" codes (unverifiable).

## Step 6: Entity ledger
T1: Starbucks Angebote, Supermarkt/Prospekt, Coffee House, Rewards (150/450), eigener Becher 0,50 €, Chilled Coffee, Kapseln. T2: Lidl/REWE/Kaufland/ALDI/EDEKA/Rossmann/METRO, UVP, KW 39, Pfandbecher 2,50 €, GLAMOUR25, Starbucks at Home, Nestlé, Deine Tasse, Gold perks, AmRest. T3: marktguru/kaufDA/discounto, Happy Hour, Geburtstagsgetränk.
Relationships: supermarket products —sold by→ retailers, not coffee houses · Rewards —3 stars/€→ 150 = free drink ≈ 50 € · own cup —saves→ 0,50 €/drink · Chilled cup 1,99 € ≈ 1/3 of Iced Caffè Latte 5,40 € · supermarket purchases —don't earn→ stars.

## Step 7: Information gain
1. **Two-worlds table** (supermarket vs coffee house). Competitors are either pure flyer lists or pure coupon lists.
2. **Typical deal-price benchmarks** ("above this = not a deal").
3. **Savings calculator** for a 5×/week latte drinker (own cup + Rewards).
4. A warning that coupon-site "online shop" codes don't apply in DE.

## Step 8e: Links / cannibalisation
Out: /blog/starbucks-kapseln-angebot (capsule detail, deliberately not duplicated), /blog/starbucks-becher, /blog/starbucks-menu (Card section). **Cannibalisation check:** kapseln-angebot H2 5 "Wann und wo gibt es die besten Starbucks Kapseln Angebote?" overlaps only on capsules. This post keeps capsules to one short H3 + link. The workbook's other "starbucks kapseln angebot rewe / nespresso kapseln angebot" merge rows still belong to kapseln-angebot.
