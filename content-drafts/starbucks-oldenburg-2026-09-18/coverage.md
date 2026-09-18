# Coverage and editorial QA — starbucks-oldenburg

Visible-text words (draft.md, excl. FAQ): ~685. FAQs: 11. Direct-answer block: 46 whitespace-delimited words.

| Check | Result |
|---|---|
| Tier 1 concepts | 3/3 (100%) — Starbucks, Oldenburg, Bremen (Marktstraße 3/Bahnhofsplatz 15) all carry an explicit attribute (absence-of-branch fact, population, or address+distance) |
| Tier 2 concepts | 3/3 (100%) — Carl von Ossietzky Universität Oldenburg, Käthe Kaffee, Oldenburg Indiana (USA) |
| Tier 1 attribute/relationship | All three core entities carry an explicit attribute, not a bare mention |
| Heading hierarchy | One H1; one H3 nested correctly under its H2 (disambiguation aside); no skipped levels |
| Heading query ownership | Each H2/H3 owns a distinct phrase; no cannibalising duplicate headings |
| Answer-first (QUORA order) | Every question-style heading answers in its opening sentence |
| FAQ parity | All 11 FAQ answers match the FAQPage schema text verbatim |
| Schema | JSON valid (checked with `python3 -m json.tool`); author field uses existing site convention (Organization, no invented person); not run through an external Rich Results validator — user should do so before deploy |
| Internal links | `/blog/starbucks-geoeffnet`, `/blog/starbucks-in-der-naehe` — both already exist on the site |
| Information gain | (1) an explicit sourced "no branch" answer plus a real address/distance table for the four Bremen branches, where every aggregator returns only empty/generic results; (2) the "Oldenburg, Indiana" disambiguation, absent from every competitor source; (3) a genuinely rated local alternative (Käthe Kaffee, 4.7★) instead of a generic "try a local café" line |

## Fact cross-check (every number/date/name traced to a source)

| Fact | Source |
|---|---|
| Kein Starbucks-Eintrag für Oldenburg im deutschen Filialverzeichnis | meinprospekt.de/filialen/starbucks-de (full directory, checked directly — no Oldenburg entry) |
| Marktstraße 3, 28195 Bremen; Bahnhofsplatz 15, 28195 Bremen; AG-Weser-Straße 1 & 3, 28237 Bremen; Hans-Bredow-Straße 19, 28307 Bremen | kaufda.de/Filialen/Bremen/Starbucks/v-r494 |
| Fahrstrecke Oldenburg–Bremen rund 47–55 km, ca. 40–45 Minuten | ViaMichelin / ADAC Maps / planroute.de / entfernung.site route results (via search snippets) |
| Oldenburg: 176.530 Einwohner (Stand 31.12.2025, +462 ggü. Vorjahr) | Stadt Oldenburg, offizielle Einwohnerprognose/Bevölkerungszahl-Seite |
| Carl von Ossietzky Universität Oldenburg: 14.770 Studierende (WiSe 2025/26) | uol.de/zahlen-fakten (offizielle Seite) |
| Stadtweit rund 18.000 Studierende an fünf Hochschulen (~10 % der Bevölkerung) | Suchergebnis-Zusammenfassung, referenzierend auf Studis Online / studieren-in-niedersachsen.de |
| Käthe Kaffee, Kaiserstraße 28, 4,7★ (26 Bewertungen) | Tripadvisor Oldenburg café ranking (via search snippet); Instagram-Profil @kaethekaffeeoldb bestätigt Standortnamen |
| Oldenburg, Indiana (USA), nahe Batesville; Starbucks-Filiale in Batesville | Grubhub-Ergebnis "Starbucks Delivery in Oldenburg, IN" + Yelp/Yellowpages-Ergebnisse für Batesville, IN 47006 |
| Schlosshöfe Oldenburg: 12.500 m², eröffnet 2011, kein Starbucks unter den Mietern | en.wikipedia.org/wiki/Schlosshöfe (via search snippet); keine Starbucks-Nennung in Mieterlisten/Suchergebnissen |

**Fetch note:** 11880.com returned HTTP 403 on fetch attempt; substituted meinprospekt.de (already a distinct domain in the competitor table) rather than fabricating 11880's content — flagged in research-notes.md Step 4.

## Intent check

Delivers on the dominant **know-simple / visit-in-person** intent (a clear yes/no answer plus where to actually go instead) and pre-empts the international name-collision confusion a plain directory listing doesn't address.

## Readability

Estimated grade ~8-9 (German Realschule-level prose, short paragraphs, one idea per sentence) — in line with the Trier/Siegen sibling pages.

## E-E-A-T flags (need user's manual input before publishing)

- **"No branch" claim rests on directory cross-referencing, not a direct call to Starbucks or a live scrape of the official JS-rendered store locator** — the official starbucks.de/de/store-locator page could not be fetched directly (JS-rendered SPA); the negative claim is backed by the full meinprospekt.de directory (no Oldenburg entry) instead. Recommend a manual spot-check of starbucks.de/de/store-locator before publishing, since a brand-new opening would not yet be reflected in either source.
- Author is listed as "StarbucksPreise Redaktion" (Organization), matching every sibling page — no individual byline/credentials exist to add.
- `datePublished`/`dateModified` set to 2026-09-18; update `dateModified` if this page is edited later.
- Run `schema.jsonld` through the Rich Results Test / schema.org validator before deploy (not done in this pass).
- Driving-distance range (47–55 km) is quoted as a range rather than a single number, since different route-planner sources disagreed slightly — disclosed in-copy rather than silently picking one figure.
- Käthe Kaffee's rating (4.7★/26 reviews) is a live, changeable figure from a review aggregator — reasonable to spot-check before publishing if this page will be updated periodically.
