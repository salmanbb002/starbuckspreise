# Research notes: starbucks logo bedeutung (+ name, geschichte, gründer)

Run date: 1 Oct 2026. Target: `/blog/starbucks-logo-name-bedeutung`, voice: du. Queue item #4 (~640/mo, evergreen).

## Step 1: Intent + SERP

- **Dominant intent:** know (meaning of logo + name). **Secondary:** know-simple (Gründer, warum grün), know (Geschichte/Evolution).
- **SERP (WebSearch):** designenlassen.de, designtagebuch.de (2011 redesign), istitutomarangoni.com (EN), logogeist.de, logo-story.ch (25 Mar 2026), huffpost (EN), de.newsner.com, eBay listings. About.starbucks.com "The Evolution of Our Logo" ranks for the EN query.
- **SERP features (inferred):** image pack (logo versions), PAA ("Was ist auf dem Starbucks Logo?", "Warum ist das Starbucks Logo grün?"), knowledge panel for Starbucks.
- **Fan-out (Autocomplete_Oct2026):** geschichte starbucks logo, starbucks bedeutung (logo/name), starbucks logo 2026 / alt / evolution / früher / neu / history, starbucks figur/frau bedeutung, starbucks name (auf becher, fails, herkunft, meme, origin, wrong, namen falsch), starbucks gründer (buch, howard schultz, vermögen, yacht), starbucks geschichte (und entwicklung).

## Step 2: Head-entity sources

| # | Source | Used for |
|---|---|---|
| S1 | en.wikipedia.org/wiki/Starbucks | founded 30 Mar 1971 Seattle (Pike Place), founders Baldwin/Siegl/Bowker, "st" words → "Starbo" (mining town, Cascade Range) → Starbuck; Bowker: coincidental; Heckler; logo 1987/1992/2011; Schultz CEO 1986/87–2000, 2008–2017, left again 2022/23; Brian Niccol CEO from Aug/Sep 2024; 40,990 stores / 87 countries (2025) |
| S2 | about.starbucks.com/history/the-evolution-of-our-logo (403 on fetch; facts via search snippets of it + looka/historyoasis summaries) | Heckler 1971, 16th-c. Norse woodcut in old marine books; 1987 merge with Il Giornale, green replaces brown; hair repositioned for delivery trucks; 1992 face focus; 2011 siren stands alone |
| S3 | designtagebuch.de "Starbucks ohne Starbucks im neuen Markenlogo" (5 Jan 2011) | 2011: Lippincott, ring + "Starbucks Coffee" removed, rationale (sells more than coffee), reader poll 55 % against / 3,751 votes |
| S4 | logogeist.de (9 Dec 2019) | 1971 bare siren, navel, brown; 1987 covered, wordmark with two stars, green; 1992 close-up, navel gone; 2011 wordmark + stars removed |
| S5 | logo-story.ch (25 Mar 2026) | 2008 retro brown logo attempt; 1971 text "Coffee, Tea, and Spices"; first decade only beans/tea/spices |
| S6 | designenlassen.de | siren symbolism (Seattle, sea), two tails, green = freshness/nature/growth; FAQs "Was ist auf dem Starbucks Logo?", "Warum ist das Starbucks Logo grün?" |
| S7 | starbuckspreise.com/blog/starbucks-deutschland-filialen (own site) | 179 stores (1 Jul 2026), May 2002 Berlin, AmRest since Apr 2016 |
| S8 | Melville, *Moby-Dick* (1851) | Starbuck = chief mate of the Pequod, Ahab's counterpart (general knowledge) |

## Step 3: Metadata

- **Title:** Starbucks Logo Bedeutung: Sirene, Name & Geschichte erklärt (59)
- **H1:** Starbucks Logo Bedeutung: Wer ist die Sirene und woher kommt der Name?
- **Meta:** see meta.json (150)
- **Slug:** /blog/starbucks-logo-name-bedeutung

## Step 4: Competitors (top 4 distinct, fetched)

| C | URL | H2/H3 | FAQ |
|---|---|---|---|
| C1 | designenlassen.de/blog/bekannte-logos/starbucks-logo/ | Geschichte des Starbucks-Logos / Bedeutung und Geheimnisse / FAQs / Fazit | "Was ist auf dem Starbucks Logo?", "Warum ist das Starbucks Logo grün?" |
| C2 | logo-story.ch/2026/03/25/so-wurde-starbucks-zur-globalen-kultmarke/ | Die Geschichte vom Starbucks-Logo (1971/1987/1992/2008/2011) / 4 Lektionen (Mut zur Veränderung, Vereinfachung, Farbgebung, Langlebigkeit) / Schlusswort | none |
| C3 | logogeist.de/blog/bersicht-ber-die-designgeschichte-des-starbucks-logos | 01 Geschichte und Herkunft / 02 Entwicklung / 03 Design-Elemente | none |
| C4 | designtagebuch.de/starbucks-ohne-starbucks-im-neuen-markenlogo/ | news article (2011 redesign) | none |

## Step 5: Extraction (condensed)

- **C1:** Gordon Bowker, Zev Siegl, Jerry Baldwin, Pequod, Moby-Dick, Starbuck, Pike Place Market, Terry Heckler, Holzschnitt 16. Jh. (nordisch), braun → grün 1987, Howard Schultz 1982/1987 CEO, Krone, 1992, 2011 40. Jubiläum, Sirene, Seattle, Meer, Verführung, zwei Schwänze, Grün = Rohkaffee/Natur/Nachhaltigkeit. (21)
- **C2:** 1971 Holzschnitt-Stil, Coffee Tea and Spices, Moby-Dick, Heckler, Schultz-Übernahme, Kaffeebar-Konzept, 1992 Börsengang, 2008 Vintage-Logo abgelehnt, 2011 Schriftzug weg, Nike-Vergleich, Grün, Symbolik, Italienreise 1984, Hear Music. (14)
- **C3:** 30. März 1971, Seattle, Baldwin/Siegl/Bowker, Pequod, Starbuck, griechische Mythologie, doppelte Fischschwänze, Bauchnabel, Kaffeebraun, zwei Sterne, Grün-Weiß, Heckler, nordischer Holzschnitt, Kreisform, Wortmarke. (15)
- **C4:** 5. Januar 2011, März 2011, 40. Jubiläum, Lippincott, Schultz-Zitat, Ring entfernt, Schwarz → Grün, Stern auf dem Kopf, Tee-Produkte, Umfrage 55/30/15 %, 3.751 Stimmen. (11)

## Step 6: Entity ledger

See entities.json (29 rows: 10 tier-1, 12 tier-2, 7 tier-3).

**Relationships**
- Starbucks-Logo —shows→ Sirene mit zwei Schwänzen
- Sirene —based on→ nordischer Holzschnitt, 16. Jh.
- Terry Heckler —designed→ Logo 1971 (+ 1987 rework)
- Lippincott —designed with Starbucks→ Logo 2011
- Name Starbucks —from→ Starbuck, Erster Steuermann, Moby-Dick
- Gründer —rejected→ "Pequod"; —found→ "Starbo" on mining map
- Logo colour —brown (1971) → green (1987)← Il Giornale merger
- Howard Schultz —joined→ 1982; —bought→ Starbucks 1987; —CEO→ to 2000, 2008–2017
- 2011 logo —removed→ ring + "Starbucks Coffee" (sells more than coffee)
- Starbucks DE —opened→ May 2002 Berlin; —licensee→ AmRest (2016)

**Parked:** Gründer Vermögen/Yacht/Buch (Schultz personal wealth, different intent, unverified numbers), Hear Music, "name fails/meme" beyond one FAQ, Pantone code.

## Step 7: Information gain

- C1–C3 are design-focused and **skip the name origin details** ("Starbo" step, Bowker's "coincidence" quote) and **Germany** context.
- C1/C3 wrongly imply Schultz-era design; C2 says Heckler designed the 1987 logo "commissioned by Schultz" (consistent with S2), C1 lists Schultz as joining 1982 + CEO 1987 (OK).
- No competitor clears up the common **"Schultz = Gründer"** confusion (autocomplete "starbucks gründer howard schultz") → explicit H3 + FAQ.
- Original elements: **"Logo-Details auf einen Blick" table** (each element → meaning, with "offiziell nicht erklärt" where true) and the **history timeline including Germany (2002, 2016)**.

## Step 8: Heading map

| Lvl | Heading | Owns phrase | Question |
|---|---|---|---|
| H1 | Starbucks Logo Bedeutung: Wer ist die Sirene …? | starbucks logo bedeutung | — |
| H2 | 1. Was bedeutet das Starbucks-Logo? | logo bedeutung | meaning |
| H3 | Warum hat die Sirene zwei Schwänze? | figur bedeutung | — |
| H3 | Warum ist das Starbucks-Logo grün? | logo grün | PAA |
| H2 | 2. Woher kommt der Name Starbucks? | name bedeutung / herkunft | — |
| H3 | Von „Pequod“ über „Starbo“ zu Starbucks | name origin | — |
| H2 | 3. Wie hat sich das Starbucks-Logo entwickelt? | logo evolution | — |
| H3 | Das alte Starbucks-Logo von früher | logo alt / früher | — |
| H3 | Das neue Logo seit 2011 | logo neu / 2026 | — |
| H2 | 4. Wer hat Starbucks gegründet? | starbucks gründer | — |
| H3 | Howard Schultz und der Wandel zum Coffee House | gründer howard schultz | — |
| H2 | 5. Starbucks Geschichte und Entwicklung in Zahlen | geschichte und entwicklung | — |
| H2 | 6. Die Logo-Details auf einen Blick | (info gain) | — |
| H2 | Häufig gestellte Fragen | 11 Q | — |

**Internal links:** /blog/starbucks-deutschland-filialen, /blog/starbucks-kaffee, /blog/starbucks-becher-aktuell. **Inbound candidates:** starbucks-kaffee (Howard Schultz paragraph), starbucks-becher / starbucks-tassen (mention "Sirene"), starbucks-deutschland-filialen (2002 history), starbucks-aktie.html (company profile).
**Cannibalisation:** none. starbucks-kaffee mentions Schultz in a roast-history context only.

## FAQ source map

C1 FAQs (2, verbatim intent), autocomplete (frau/figur, name auf becher, logo 2026, gründer howard schultz), follow-ups (Stern, wer entwarf, Moby-Dick, braun, Deutschland seit wann).

## Open flags (need user)

1. **Asymmetric face** (Logo-Details table): from Starbucks' own 2011 refresh story (widely reported), but about.starbucks.com returned 403 to our fetch. Please verify or remove the row.
2. **Melusine** comparison is general heraldry knowledge, not from a Starbucks source.
3. Schultz first CEO year: S1 says 1986/1987 (sources differ). The draft avoids the start year ("führte das Unternehmen bis 2000").
4. 40,990 stores / 87 countries comes from Wikipedia (2025 figure).
