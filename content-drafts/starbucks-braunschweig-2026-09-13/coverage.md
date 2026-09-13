# Coverage and editorial QA

Visible-text words: 821. FAQs: 11. Direct-answer block: 52 whitespace-delimited words.

| Check | Result |
|---|---|
| Tier 1 concepts | 4/4 (100%) |
| Tier 2 concepts | 8/8 (100%) |
| Tier 1 attribute/relationship | All four core entities carry an explicit attribute (address, hours, closure date, or founding fact) |
| Heading hierarchy | One H1; two H3 nested correctly under their H2; no skipped levels |
| Heading query ownership | Each H2/H3 owns a distinct phrase; no cannibalising duplicate headings |
| Answer first | Every question-style heading answers in its opening sentence |
| FAQ parity | All 11 FAQ answers match the FAQPage schema text verbatim |
| Schema | JSON valid; author/publication fields left as explicit TODO; not run through an external validator |
| Internal links | None inserted in draft.md (single-location page has no natural mid-body anchor); see article.fragment.html for the two sibling-page links added at insertion time |
| Information gain | "Aktuell vs. veraltet"-Abschnitt, der Kohlmarkt/Schloss-Arkaden explizit als geschlossen benennt — keiner der vier Wettbewerber tut das |

## Evidence for mandatory concept coverage

| Concept | Tier | Covered | Example passage |
|---|---|---|---|
| Starbucks | 1 | Yes | Der einzige aktuelle Starbucks in Braunschweig liegt am Damm 22... |
| Braunschweig | 1 | Yes | ...liegt am Damm 22 in der Fußgängerzone der Innenstadt. |
| Damm 22 | 1 | Yes | Die einzige derzeit betriebene Filiale liegt am Damm 22... |
| Öffnungszeiten | 1 | Yes | Montag – Freitag 08:00 – 20:00 Uhr / Samstag 09:00 – 20:00 Uhr / Sonntag 11:00 – 18:00 Uhr |
| Kohlmarkt 18 | 2 | Yes | Die Filiale am Kohlmarkt lief rund zehn Jahre und wurde etwa 2019 aufgegeben |
| Schloss-Arkaden / Bohlweg 74-75 | 2 | Yes | Die Filiale in den Schloss-Arkaden schloss bereits 2016 |
| Mobile Order & Pay | 2 | Yes | Bestellungen lassen sich vorab über die Starbucks-App aufgeben und im Store abholen |
| Starbucks Rewards | 2 | Yes | gesammelte Sterne können vor Ort eingelöst werden |
| WLAN | 2 | Yes | ein drahtloser Hotspot ist vorhanden |
| Lieferung | 2 | Yes | ist bei Uber Eats, Wolt und Lieferando gelistet |
| Fußgängerzone Damm | 2 | Yes | mitten in der Fußgängerzone zwischen Bohlweg und Kohlmarkt |

Coverage uses surface forms plus manual semantic review; it measures the chosen ledger, not search-engine rankings.

## Competitor-heading matrix

| Recurring function / heading | Coverage decision |
|---|---|
| Address / Filiale-Adresse listing | Covered — but corrected against the two stale competitor addresses |
| Öffnungszeiten | Covered with a table sourced to the official locator, not the aggregators (which showed no hours or a closed-Sunday claim later contradicted by the current store) |
| Kontaktdaten / phone | Skipped — no phone number verified for the current Damm 22 store; not invented |
| "Weitere Angebote in der Nähe" (nearby listings) | Skipped as out of scope for this query's intent |

## Fact review

Address, opening hours, size, and both closure dates trace to research-notes.md (official store locator ID 81776-311207, t-online article, Yelp listing, three delivery-platform pages). No phone number, price, or job-count is stated because no source in this run confirmed one for Damm 22 specifically. The company's stated reasoning for the reopening is paraphrased, not quoted verbatim, since the only source retrieved was itself a translated extraction rather than the original German wording.

## Readability

German, direct address avoided in favor of neutral third-person city-guide tone matching the site's other Standorte pages; short paragraphs, one table, one bullet list. Editorial estimate: grade 8-9 (compound nouns, address/time formatting). No validated German readability model was run.

## E-E-A-T flags for the user

- **TODO:** real author byline/date before publishing (see publishing-notes.md).
- **Time-sensitive:** hours and "only current location" status should be re-verified against the store locator immediately before publishing — this is exactly the kind of stale-data problem the article calls out in competitors.
- No first-person visit claim was written; none of the sources support genuine first-hand experience.
