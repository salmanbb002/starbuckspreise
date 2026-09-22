# Research notes — starbucks heiße schokolade

Content type per calendar: **FAQ / short answer post** (Low priority, vol 90, KD 20, Informational). Scaled to a shorter piece than the two prior full posts this session.

## Step 1 — Intent + SERP

- Dominant intent: **know-simple** (what varieties exist, what they cost, calories). Secondary: commercial (retail cocoa powder purchase).
- No featured snippet / PAA block visible in the search-tool results returned (text-summary SERP, not a rendered browser SERP — Chrome tools not invoked for this short post, scope didn't warrant it).
- Query fan-out found via search: "starbucks heiße schokolade kalorien", "weiße Schokolade Starbucks", "Starbucks Signature Chocolate 42/70", "starbucks java chip chocolate" (this one is a Frappuccino, not a hot chocolate — see Step 7).

## Step 2 — Head-entity research (non-competitor)

- **Starbucks** — Organization, coffeehouse chain, sameAs `https://de.wikipedia.org/wiki/Starbucks`. Already the head entity on every other post on this site.
- **Signature Hot Chocolate** — Starbucks-branded café product, unlinked entity (no dedicated Wikipedia page), type Product.
- **Starbucks® at Home** — Starbucks' retail/home-use product line, licensed to **Nestlé** since the 2018 Global Coffee Alliance (same licensing fact already established and sourced in `content-drafts/starbucks-kapseln-angebot-2026-09-22/research-notes.md` — reused here, not re-derived).

## Step 3 — Title + metadata

- Title: "Starbucks Heiße Schokolade: Sorten, Preise & Kalorien 2026" (56 chars)
- H1: "Starbucks Heiße Schokolade: Sorten, Preise und Kalorien 2026"
- Meta description: "Starbucks Heiße Schokolade: die 3 Sorten (Classic, White, Signature), Preise, Kalorien und der Unterschied zu Starbucks Signature Chocolate für zu Hause."
- Slug: `starbucks-heisse-schokolade` (ß→ss, site's transliteration convention — see starbucks-wuerzburg, starbucks-tuebingen-style slugs)

## Step 4 — Competitor fetch (top 4 attempted, 3 usable + 1 authoritative nutrition DB)

1. **starbuckspreise.de** (fetched OK) — lists Signature Hot Chocolate 6,40 €/351 kcal, Hot White Chocolate 6,40 €/357 kcal, Classic Hot Chocolate 4,99 €/311 kcal — but its own FAQ answer on the same page contradicts the menu price, saying "Ab 4,80 €". **Internal inconsistency on a competitor page — flagged, not resolved by inventing a single "true" number.**
2. **speisekartemenus.de** (fetched OK) — lists "Premium Hot Chocolate" / "Premium Hazelnut Hot Chocolate" / "Premium Caramel Hot Chocolate" / "Salted Caramel Hot Chocolate" with Tall/Grande/Venti pricing (€3,99–5,29). **These product names don't match the actual German Starbucks menu** (official site lists only Classic/White/Signature, no Hazelnut or Salted Caramel hot chocolate) — looks like unadapted US-template data. Used as the **information-gain point**: a reader following this competitor's product names into a German store will not find them.
3. **fddb.info** (fetched OK) — German nutrition database, real measured data: 56 kcal/100 g; **Tall (250 g) = 140 kcal**, Glass (200 g) = 112 kcal, Cup (422 g) = 236 kcal. Materially lower and more granular than starbuckspreise.de's 311–357 kcal figures — likely different recipe/size basis; both are cited, draft states them as distinct data points rather than picking one as "correct" without a primary source.
4. **starbucks.de official menu** (`/de/menu-drinks-hot-chocolates`) — authoritative for which 3 products actually exist and their German descriptions. No prices or kcal shown on-site (matches this site's own prior finding on `starbucks-menu.html`: "auf den Menüseiten von starbucks.de stehen keine Preise").
5. Additional: **starbucksathome.com** (DE + AT product pages) for the two retail cocoa-powder SKUs — Signature Chocolate 42% (185 kcal/cup per search-tool summary) and 70% (dark, 5 tsp per 200 ml milk per prep instructions). **sweet-universe.de** — retail price for the 70% powder: 7,79 € / 330 g (23,61 €/kg).
6. **veganfreundlich.org** checked for a vegan angle — page doesn't mention hot chocolate at all, so not used as a source; reused this site's own already-published vegan fact from `blog/starbucks-getraenke.html` instead ("Bei Frappuccinos und Kakaogetränken muss lediglich auf die Schlagsahne verzichtet werden").

## Step 5/6 — Entity map + tiers

| canonical | type | aliases | sameAs | kind | competitor_count | tier |
|---|---|---|---|---|---|---|
| Starbucks | Organization | — | de.wikipedia.org/wiki/Starbucks | entity | 4 | 1 |
| Signature Hot Chocolate | Product | Heiße Schokolade | — (unlinked) | entity | 3 | 1 |
| Classic Hot Chocolate | Product | — | — | entity | 2 | 1 |
| White Hot Chocolate | Product | Hot White Chocolate | — | entity | 2 | 1 |
| Starbucks Signature Chocolate 42% | Product | Kakaopulver 42% | — | entity | 1 (own search) | 2 |
| Starbucks Signature Chocolate 70% | Product | Kakaopulver 70% | — | entity | 1 (own search) | 2 |
| Starbucks Java Chip Chocolate Frappuccino | Product | Java Chip | — | entity | 0 (keyword-only) | 2 |
| Nestlé | Organization | — | de.wikipedia.org/wiki/Nestlé | entity | reused from sibling post | 3 |
| fddb.info kcal figures | Metric | — | — | term | 1 | 2 |

Relationships: `Signature Hot Chocolate —besteht aus→ gedämpfte Milch + Schokoladensoße + Schlagsahne + Schokodrizzle`; `White Hot Chocolate —besteht aus→ weiße Schokoladensauce + gedämpfte Milch + Schlagsahne`; `Starbucks Signature Chocolate 42%/70% —lizenziert von→ Nestlé (Starbucks at Home, seit 2018)`; `Java Chip Chocolate —ist ein→ Frappuccino, nicht eine heiße Schokolade`.

Dedupe/parked: "starbucks choc" (vague head term) — folded into the general Classic/Signature coverage, not a separate section. "starbucks java chip chocolate" — kept as its own short disambiguation section rather than forced into the hot-chocolate body, since it's a different product category (info-gain, not padding).

## Step 7 — Information-gain element

Two: (1) naming the starbuckspreise.de price self-contradiction and the speisekartemenus.de non-existent "Hazelnut/Salted Caramel" varieties plainly, rather than repeating either as fact; (2) explicit Java Chip Chocolate disambiguation (it's a Frappuccino, not a hot chocolate) — a genuine reader confusion this keyword's clustering surfaced.

## Step 8 — Heading map

1. H2 `#sorten` — "Welche heißen Schokoladen gibt es bei Starbucks?" — Classic/White/Signature, tier-1 entities + attributes
2. H2 `#preise` — "Was kostet eine heiße Schokolade bei Starbucks?" — price table + the source-conflict note
3. H2 `#kalorien` — "Wie viele Kalorien hat eine Starbucks Heiße Schokolade?" — fddb figures
4. H2 `#zuhause` — "Starbucks Signature Chocolate zum Selbermachen" — 42%/70% retail powder, Nestlé link, cross-link to kapseln-angebot post
5. H2 `#java-chip` — "Ist Starbucks Java Chip Chocolate eine heiße Schokolade?" — disambiguation
6. H2 `#vegan` — "Ist heiße Schokolade bei Starbucks vegan möglich?" — short, reuses own site's established fact
7. H2 FAQ (12 Qs)

## Step 8e — Internal links

Inbound (adding link to this new page from): `blog/starbucks-getraenke.html` (already mentions "Heiße Schokolade" in vegan FAQ — turn into a link), `blog/starbucks-menu.html` (Hot Chocolates row + prose mention), `blog/starbucks-kapseln-angebot.html` (Nestlé/at-home section, natural tie-in). Outbound from new page: `/blog/starbucks-preise`, `/blog/starbucks-menu`, `/blog/starbucks-kapseln-angebot`, `/blog/starbucks-getraenke`, `/blog/starbucks-frappuccino-sorten` (for the Java Chip disambiguation link).

No existing page currently targets "heiße schokolade" as its primary keyword — no cannibalisation found; this is a new canonical home for the intent.

## FAQ source map

Q1–3 general (own synthesis of Steps 1-6 facts), Q4 Java Chip (Step 7 info-gain), Q5 vegan (reused site fact), Q6 Classic vs Signature (Step 5 attributes), Q7–9 Signature Chocolate 42/70% (Step 4.5 research), Q10 White Hot Chocolate caffeine (general knowledge: hot chocolate has no espresso, so no added caffeine beyond trace cocoa — flagged in coverage.md as needing a source if published as an absolute claim), Q11 Iced Chocolate category (from starbucks-menu.html's existing "Iced Chocolates" category mention), Q12 where to buy retail powder (sweet-universe.de + general German grocery/online retail, kept generic — no single retailer named as exclusive).
