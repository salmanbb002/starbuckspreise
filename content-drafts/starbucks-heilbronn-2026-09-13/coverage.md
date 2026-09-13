# Coverage and editorial QA

Visible-text words: 585. FAQs: 10. Direct-answer block: 47 whitespace-delimited words.

| Check | Result |
|---|---|
| Tier 1 concepts | 4/4 (100%) |
| Tier 2 concepts | 5/5 (100%) |
| Tier 1 attribute/relationship | All four core entities carry an explicit attribute (address, hours) |
| Heading hierarchy | One H1, flat H2 structure (no H3 needed — single-location page, unlike the multi-branch Essen/Braunschweig cases) |
| Heading query ownership | Each H2 owns a distinct phrase; no cannibalising duplicates |
| Answer first | Every question-style heading answers in its opening sentence |
| FAQ parity | All 10 FAQ answers match the FAQPage schema text verbatim |
| Schema | JSON valid; author/publication fields left as explicit TODO; not run through an external validator |
| Internal links | None inserted in draft.md; two sibling-page links added in article.fragment.html at insertion time |
| Information gain | Explicit "sources agree" confidence note + a parking paragraph sourced only to the city's own finder — no competitor combines both |

## Evidence for mandatory concept coverage

| Concept | Tier | Covered | Example passage |
|---|---|---|---|
| Starbucks | 1 | Yes | Der Starbucks in Heilbronn liegt an der Kilianstraße 6... |
| Heilbronn | 1 | Yes | ...liegt an der Kilianstraße 6, mitten in der Innenstadt. |
| Kilianstraße 6 | 1 | Yes | Die Adresse lautet Kilianstraße 6, 74072 Heilbronn. |
| Öffnungszeiten | 1 | Yes | Montag – Freitag 08:30 – 21:00 Uhr / Samstag 08:30 – 21:30 Uhr / Sonntag 08:30 – 20:30 Uhr |
| Parkplätze | 2 | Yes | verzeichnet für die Kilianstraße Parkplätze in der Nähe |
| Mobile Order & Pay | 2 | Yes | Bestellungen lassen sich vorab über die Starbucks-App aufgeben und im Store abholen |
| Starbucks Rewards | 2 | Yes | gesammelte Sterne können vor Ort eingelöst werden |
| WLAN | 2 | Yes | ein drahtloser Hotspot ist vorhanden |
| Lieferung | 2 | Yes | die Filiale ist bei Uber Eats, Wolt und Lieferando gelistet |

## Competitor-heading matrix

| Recurring function / heading | Coverage decision |
|---|---|
| Address / Filiale-Adresse | Covered — and flagged as unusually consistent across all four sources |
| Öffnungszeiten | Covered with a table sourced to the official locator, cross-checked against Kaufda |
| Kontaktdaten / phone | Skipped — no phone number verified from an authoritative-enough source for this draft |
| Speisekarte / menu items | Skipped as out of scope for a navigational city-location query |

## Fact review

Address and hours trace to research-notes.md (official store locator ID 53134-281941, City of Heilbronn shop/gastro finder, Kaufda, delivery-platform pages). No price or store-size claim is made — no source in this run stated one.

## Readability

German, neutral third-person city-guide tone matching the site's other Standorte pages; short paragraphs, one table, two bullet-style sections. Editorial estimate: grade 7-8 — this page is structurally simpler than the multi-branch Essen/Braunschweig drafts since only one location exists. No validated German readability model was run.

## E-E-A-T flags for the user

- **TODO:** real author byline/date before publishing.
- **Time-sensitive:** hours should be re-verified against the store locator immediately before publishing.
- No first-person visit claim was written.
