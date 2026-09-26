# Research notes: starbucks menue / drinks / speisekarte / germany menu / produkte

**Run:** 26 Sep 2026 · merge into `blog/starbucks-menu.html` · Calendar Days #125–129 (480+480+390+320+320)

## Intent + SERP
- **speisekarte / menue / drinks:** *know* (the full menu with prices). SERP (26 Sep): restaurantspeisekartes.de, burgerspreises.de, germanmenus.de, despeisekartes.org, starbuckspreise.de (competitor with the same name on a different TLD), speisekartemenus.de, fastfoodsmenu.com, fastfood-preischeck.de, statista. These are all price-list clones. Host page already outranks them on depth; only meta variants are missing.
- **germany menu:** English-speaking visitors. SERP: TikTok, starbuckspreise.de, fastfoodsmenu.com, Uber Eats (de-en store pages for Hamburg/Nürnberg), wheree.com, **starbucks.de/en/menu** (official English menu), issuu. No page explains the German vocabulary at the counter. **This is the gap.**
- **produkte:** mixed. athome.starbucks.com (US at-home range), about.starbucks.com, eBay.de product listings, starbucks.com. German users mean supermarket products (capsules, beans, chilled cups). The host page mentions capsules only in passing.

## Sources
- starbucks.de/en/menu (fetched 26 Sep): categories Hot Drinks / Iced Drinks / Frappuccino® Blended Beverages / Matcha; Food: Breakfast & Pastries / Bakery / Sandwiches / Snacks & Sweets.
- Site pages: `/blog/starbucks-kapseln-angebot` (Nestlé Global Coffee Alliance 2018, US$7,15 bn; Nespresso Original + Dolce Gusto; Vertuo incompatible), `/blog/starbucks-angebote` (Starbucks at Home; Chilled Classics; Grande Cup Chilled Coffee 330 ml), `/blog/starbucks-menu` (extra shot ≈ 0,80 €; plant milk surcharge).
- Prices: `menu.js`.

## Entity ledger (summary)
Tier 1: Starbucks Menu/Speisekarte, Drinks, Preise, Starbucks Produkte. Tier 2: Nestlé, Starbucks at Home, Nespresso, Dolce Gusto, Chilled Classics, Starbucks Deutschland app, milk vocabulary (Halbfettmilch, Hafer…), sizes. Tier 3: VIA Instant, creamer (US-only, parked).
**Relationships:** Nestlé —licenses (2018)→ packaged Starbucks products · AmRest —operates→ coffee houses · Kapseln —fit→ Nespresso Original / Dolce Gusto (not Vertuo) · starbucks.de/en/menu —lists→ 4 drink categories.

## Heading map
H2 (EN) „Starbucks Germany menu in English …“ → *starbucks germany menu*; H3 „Welche Starbucks Produkte gibt es im Supermarkt?“ → *starbucks produkte*; FAQ „Was bedeutet Starbucks Drinks …“ → *starbucks drinks*; „menue“ → meta + one in-text mention.

## Info gain
Counter vocabulary table (DE→EN) plus a products-by-channel table (Filiale vs Supermarkt vs Nestlé). Neither exists in the SERP.

## Cannibalisation
`/blog/starbucks-kapseln-angebot` owns capsule prices, so Block B only lists and links. `/blog/starbucks-preise` owns the price list, so Block A shows 9 prices and links out.
