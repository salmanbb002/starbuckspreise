# Coverage / QA: starbucks-tee-2026-09-28
- The heading architecture has one H1, H2 sections 1–8, and H3s only under H2s. The layout check passes.
- The direct answer is 45–53 words. There are 12 FAQs, and the FAQPage JSON-LD is generated from the same draft.md, so it matches the page verbatim.
- Every number traces to S2 (nutrition PDF row), S3 or S4 (prices), or S1 (names/counts). Nothing is estimated.
- Schema: Article + FAQPage + BreadcrumbList. about/mentions use Thing/Brand/Organization only (no Product/Event), and the Wikidata IDs were verified via the API.
- The hero is a generic Commons photo, credited on-page via scripts/add-image-credits.py.

## Flags
See research-notes.md "Open flags".
