# Coverage / QA: starbucks-protein-2026-09-29

- **Entity coverage:** tier 1 is 7/7 (100%), each stated with a value. Tier 2 is 17/17 (100%). Tier 3 is 4/6 used; the quote and the exact soybean percentage were skipped.
- **Headings:** one H1, seven numbered H2s plus the FAQ, and 12 H3s. There are no hierarchy errors (finalize.py). Each H2 owns a distinct phrase.
- **Answer block:** 52 words; it names both drinks, their prices, about 17 g protein and the RTD bottle. Every H2 and H3 answers in its first sentence.
- **Questions:** 10 FAQs. The autocomplete intents (protein latte, matcha protein, vanilla protein, iced sugar free vanilla, protein drink, protein coffee) are all covered.
- **Fact check:**
  - All nutrition values were checked row by row against S1.
  - Prices come from S3, vegan status from S2, launch and operator from S5/S6, and RTD facts from S8.
  - Derived numbers were re-computed: +5,7 g and +6,5 g protein, +1,00 €, and protein per euro of 2,8 / 2,2 / 2,2 / 2,1 g.
- **Removed during QA:** the unsourced "Joghurt/Mahlzeit" comparison; "Hälfte" was corrected to "gut die Hälfte (14,2 g)".
- **Schema:** BlogPosting + FAQPage + BreadcrumbList. about/mentions use Thing/Brand/Organization, with no Product type on the menu items. **TODO:** publisher logo, then run the Rich Results Test.
- **Intent:** the know intent (what, how much protein, price) is answered in the direct answer. The buy intent is covered in §6.
- **Readability:** about grade 8, with tables for numbers.
- **E-E-A-T / YMYL-light:** the post-workout FAQ is hedged, with no health claims.

## Flags
See research-notes.md "Open flags".
