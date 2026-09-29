# Coverage / QA: starbucks-app-2026-09-29

- **Entity coverage:** tier 1 is 7/7 (100%), each stated with a value (3/€, 150, 450, 2 Jahre, Gold-only). Tier 2 is 12/12 (100%). Tier 3 is 3/5; "Freunde werben" is answered as not offered, and US Rewards is off-intent.
- **Headings:** one H1, seven numbered H2s plus the FAQ, and 13 H3s. There are no hierarchy errors (finalize.py). Each H2 owns a distinct phrase: app deutschland, rewards, gold, geburtstag, bestellen, starbucks card, lohnt sich.
- **Answer block:** 47 words, covering the app, the Card, 3 Sterne/€, 150 → Freigetränk and 450 → Gold. Every H2 and H3 opens with the answer.
- **Questions:** 11 FAQs. The C1 FAQ questions (Verfallen Sterne? / alle Filialen? / Handy verloren? / ohne App?) are all answered, and the autocomplete intents (bestellen, vorteile, empfehlungscode, geburtstag, einlösen) are covered.
- **Fact check:** every star, threshold, expiry and Gold perk traces to S1/S2. App store data comes from S3, card facts from S4 and prices from S6. The yearly table math was re-computed:
  - 58,80 € → 176 Sterne → 1 Freigetränk.
  - 254,80 € → 764 Sterne → 5 Freigetränke, Gold.
  - 764,40 € → 2,293 Sterne → 15 Freigetränke.
- **Removed during QA (unsourced):** partner-operated stores not participating; prizes "nicht rückwirkend".
- **Schema:** BlogPosting + FAQPage + BreadcrumbList + HowTo (the real 5-step list in §5). The app is typed `Thing`, not `SoftwareApplication`, so GSC won't flag an unqualified rich-result item. **TODO:** publisher logo URL, then run the Rich Results Test.
- **Intent:** the know intent is covered in full, and the website intent is served via the app-store sameAs links. Consider adding store badges/links on the page.
- **Readability:** about grade 8, with short sentences and 3 tables.
- **E-E-A-T:** no first-person claims. Program rules can change, and the Recherchestand line date-stamps them.

## Flags
See research-notes.md "Open flags" (Gold-only birthday, the order/pay mechanics, the abroad inference, and the hero image).
