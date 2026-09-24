# Coverage / QA: „starbuck karte“ merge insert

**Entity coverage:** Tier 1: 8/8 (100%), each with an attribute or relationship stated (e.g. Card → 3 Stars/€, 150 Stars → Gratisgetränk). Tier 2: 5/5 (100%). Tier 3: Filialkarte used (Block A); Lizenzierte Standorte used; Postbank/REWE parked (stale/unverified).

**Heading architecture:** Insert adds 1 H2 (numbered "8.", matching the page's 1–7 scheme) + 4 H3s, all nested correctly. No second H1. Each H3 owns a distinct fan-out phrase (kaufen / aufladen+registrieren / rewards / verlieren). The disambiguation box is a styled block, not a heading, so it doesn't compete with the existing H1.

**Answer block:** Block A opening sentence is 43 words and answers "what does Starbucks Karte mean" directly. Every H3 opens with a direct answer.

**Competitor-heading matrix:**
| Recurring competitor H2 | Covered? |
|---|---|
| Card: wo bekommen / aktivieren | yes (H3) |
| Aufladen & registrieren | yes (H3) |
| Rewards / Vorteile | yes (H3 + table) |
| Guthaben übertragen / verlieren | yes (H3) |
| App | yes (throughout) |
| Verschenken | yes (FAQ) |
| Speisekarte categories/prices | already on host page (sections 1–7) |

**Question coverage:** All fan-out (aufladen, kaufen, registrieren, sterne) answered. Existing FAQ "Wie funktioniert Starbucks Rewards" was left unchanged, not duplicated.

**Fact cross-check:** 
- 3 Stars/€, 150, 450, Gold perks, 2-year validity, licensed-store exception → starbucks.de/en/faq-rewards ✅
- 16-digit / 8-digit PIN, reload anywhere/anytime, no fees, lost-card transfer by post → starbucks.de/en/faq-starbucks-card ✅
- Gift card → starbucks.de/de/starbucks-card ✅
- 4,99 € Caramel Macchiato → site's own menu.js ✅
- 50 € / 150 € → arithmetic ✅
- ⚠️ **Conflict to fix on the host page:** its existing FAQ says Gold gives "zusätzliche Shots oder Sirup". The official EN FAQ (fetched today) says "free syrups and toppings" plus a birthday drink and a refill. It doesn't mention free shots, though a third-party search summary did. Recommend aligning the existing answer with the official wording.
- ⚠️ The official Rewards FAQ says stars are earned by paying with Card or App. A third-party summary said stars are earned "regardless of payment method". The draft uses the official wording.

**Intent check:** The SERP is split (Card > Speisekarte > Landkarte). The merge serves all three: the host page covers the menu, Block B covers the Card and Block A routes map-seekers.

**Readability:** Short sentences, roughly grade 7–8.

**E-E-A-T / manual flags:**
1. Physical card price and min/max load amounts aren't published on the official DE pages fetched. They were deliberately left out. If you know them from a store visit, add them.
2. The "Rechnet man das um" table is our own calculation. That's fine, but keep it labelled as an example.
3. No first-person claims were written, so there's nothing to replace.
