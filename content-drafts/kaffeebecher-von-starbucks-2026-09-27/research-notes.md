# Research notes: "kaffeebecher von starbucks" (27 Sep 2026)

Calendar row: Day 49, vol 390, KD 21, Informational/Transactional, workbook label "Merge-Recommended → starbucks-becher". **User asked for a standalone blog post.** The angle was chosen to limit cannibalisation (see §8).

## 1. SERP + intent

WebSearch "kaffeebecher von starbucks" (27 Sep):
1. ebay.de/shop/starbucks-kaffeebecher: marketplace
2. ehrenkaffee.de/kaffeebecher-to-go-starbucks/: blog, Oct 2022
3. thermobechertests.de/starbucks/: **domain now a casino site** (fetched 27 Sep), unusable
4. lionshome.de, Starbucks Kaffeebecher: shopping aggregator, **403**
5. my-up2u.shop, "Die Starbucks-Becher-Alternative": brand blog, 14 Apr 2022
6.–9. eBay item pages

- **Intent:** buy (commercial investigation) + know. Searchers want to know which model and where to buy it. The SERP is shopping-heavy, and the editorial results are 2019–2022.
- **SERP features:** shopping/marketplace results, no featured snippet seen. A definition-list answer plus a comparison table fits best.
- **Fan-out (from follow-up searches):** starbucks thermobecher test, dicht/auslaufsicher, eigener becher rabatt, mehrwegbecher pfand, pappbecher kaufen, starbucks tumbler.

## 2. Head entities

| Entity | Type | sameAs | Attributes |
|---|---|---|---|
| Starbucks | Organization | https://www.wikidata.org/wiki/Q37158 | starbucks.de merchandise catalogue has no shop (site research, 23 Sep 2026) |
| Tumbler / Thermobecher | Product type | unlinked | stainless, double-wall |
| Starbucks Reusables / Pfandbecher | Program | https://www.starbucks.de/de/article/491/starbucks-reusables | green cup €2.50 Pfand, return anytime; "weißen Starbucks Reusable Cup oder eigenen Tumbler, Tasse, Becher" accepted |
| Stiftung Warentest | Organization | https://www.wikidata.org/wiki/Q326003 | Thermobecher test 4/2020 |

## 3. Fact ledger

| Fact | Source |
|---|---|
| Green reusable cup, 2,50 € Pfand, return anytime | starbucks.de/de/article/491 (fetched 27 Sep) |
| Own cups accepted: white Reusable Cup, own tumbler, Tasse, Becher | same |
| Discount amount **not stated** on the official page. 2020–2022 sources say 0,30 €; the site's becher page says 0,50 € | lebensmittelpraxis 2020, ehrenkaffee 2022, blog/starbucks-becher. **Unresolved, so the draft states no number** |
| Otto: Cold Cups 13,49–79,00 €, tumblers from ~45 €, Snoopy/Owala collabs (23 Sep 2026) | blog/starbucks-becher §4 (own research record) |
| No official DE online shop; merchandise page has no prices or basket | blog/starbucks-becher §8 (23 Sep 2026) |
| Stiftung Warentest 4/2020: 15 thermal mugs at 6–35 €, incl. Starbucks Edelstahlbecher (SKU 011082067); only 7/15 dishwasher-safe; some leaked when tipped (Bodum, McDonald's); McCafé lost 19 °C in 1 h; ≥50 uses to pay off ecologically | test.de (fetched). Starbucks grade is paywalled |
| User reports of some Starbucks tumblers leaking over time | ehrenkaffee.de / thermobechertests snippet (WebSearch) |
| oz → ml: 8=237, 12=354, 16=473, 20=591, 24=709; Short/Tall/Grande/Venti | blog/starbucks-groessen-tall-grande-venti |
| German mugs are the "You Are Here" series | memory (verified 26 Sep 2026) |
| Paper cups sold online via eBay/Amazon | ehrenkaffee 2022 |

## 4. Competitor extraction

**C1 ehrenkaffee.de (Oct 2022).** H2s: Selbst Becher zu Starbucks mitbringen & Rabatt bekommen · Wohlgewärmt durch Herbst & Winter · Starbucks Holiday Blend · Der nächste Sommer … · Welche Thermobecher von Starbucks du kaufen kannst · Bilder-Galerie: Starbucks Tumbler Becher · Starbucks positioniert sich … Müllvermeidung · Der wiederverwendbare Kaffeebecher to go von Starbucks · Wo kann man den Starbucks Tumbler & andere Becher … kaufen? · Starbucks Thermobecher Preis · Kann ich auch die bekannten Starbucks Pappbecher kaufen? · Kaffeetassen … für Zuhause & Büro · City Mugs … · Geschichte
| term | type | canonical | kind |
|---|---|---|---|
| Tumbler | Product | Tumbler | entity |
| Thermobecher | Product | Tumbler | term |
| Pappbecher | Product | Pappbecher | term |
| Rabatt | Concept | Eigener-Becher-Rabatt | term |
| Holiday | Event | Holiday-Saison | term |
| Edelstahl, Onyx-Schwarz, Silber | Concept | Material | term |
| eBay, Amazon | Org | Marktplätze | entity |
| City Mugs | Product | You Are Here (DE) | entity |
Numbers: 10 ct (US), 30 ct, 5 ct Einweg-Aufschlag (pilot HH/B), 7–23 €, 1971, 2002, 158 stores (2016). Total: 8

**C2 my-up2u.shop (Apr 2022).** H2s: Unser MuC … als echte Starbucks-Becher-Alternative · Zum Kaffee-Unternehmen · Kleine Cafés gehen unter · Statussymbol: Starbucks-Cup · Die Alternative · Facts über den MuC · up2u MuC vs Starbucks-Becher
| Polyethylen-Beschichtung | Concept | Pappbecher-Material | term |
| Sirene | Concept | Sirene (Logo) | entity |
| Recycling | Concept | Recycling | term |
| spülmaschinenfest, BPA-frei | Concept | Pflege | term |
Numbers: 28.000 stores, 65 countries, €22.39 bn, 1.6 m trees, 4 m cups. Total: 4

**C3 ehrenkaffee.de/test (2019/20).** Relevant H2: Für markenbewusste Kaffee-Genießer: Die Starbucks Thermobecher; Ein guter Isolierbecher muss vor allem eins können: dicht sein!
| dicht | Concept | Dichtigkeit | term |
| Isolierbecher | Product | Tumbler | term |
| Contigo West Loop, Emsa Travel Mug | Product | Alternativen | entity |
Total: 3

**C4 (substitute for the casino/403 pages) test.de Thermobecher 4/2020.** Covered in the fact ledger. Terms: Warmhalten, Dichtigkeit, Schadstoffe (Naphthalin), Spülmaschine, 50 Nutzungen. Total: 5

Failed: thermobechertests.de (casino), lionshome.de (403), thermoskanne-test.de (500), kaffeepioniere.de (404).

## 5. Entity ledger (tiered). See entities.json

- **Tier 1:** Starbucks; Kaffeebecher/Tumbler (Edelstahl); Cold Cup / Reusable Cup; Pappbecher; Pfandbecher 2,50 €; Preis.
- **Tier 2:** Dichtigkeit/auslaufsicher; Warmhalten; Stiftung Warentest; Spülmaschine; Größen/oz; Tall/Grande/Venti; Otto/eBay/Amazon; eigener Becher Rabatt; Original/Fälschung; Sirene.
- **Tier 3:** Holiday/Saisonkollektion; Snoopy/Owala; You Are Here; Contigo/Emsa alternatives (unused, off-brand); Polyethylen; Kleinanzeigen.

**Relationships:** Tumbler —keeps warm longer than→ Cold Cup · Cold Cup —designed for→ Kaltgetränke · Pfandbecher —costs→ 2,50 € Pfand —refunded at→ any Coffee House · 16 oz —equals→ 473 ml = Grande · 24 oz —equals→ Venti kalt · Stiftung Warentest —tested→ Starbucks Edelstahlbecher (4/2020) · only 7/15 → dishwasher-safe · Thermobecher —pays off after→ ≥50 uses · starbucks.de —has no→ online shop · Otto —sells→ Cold Cups from 13,49 € · Starbucks —accepts→ own cups of any brand.

**Heading keyword set:** (a) kaffeebecher von starbucks, starbucks kaffeebecher, starbucks to-go-becher. (b) starbucks becher arten, welcher becher, thermobecher dicht/warm, oz ml grande, starbucks becher kaufen, eigener becher rabatt, spülmaschine, original fälschung.

**Parked:** up2u's MuC/competitor-brand content (off-intent); Starbucks corporate history (belongs elsewhere); 5-ct Einweg pilot (2020, stale and unverified for 2026).

## 6. Information gain

- Every competitor dates from 2019–2022; none mentions the green Pfandbecher, current Otto prices, or the fact that starbucks.de has no shop. ehrenkaffee even says it is unclear whether the discount applies in Germany.
- The thermobechertests.de result is now a casino page, so the SERP has a gap.
- **Original elements:** (1) a use-case decision checklist; (2) an oz → ml → Starbucks-size matching table; (3) a 4-type comparison table with Sept 2026 prices; (4) the Stiftung Warentest context stated honestly (Starbucks grade paywalled).

## 7. Heading map

| Lvl | Heading | Owns | Question |
|---|---|---|---|
| H1 | Kaffeebecher von Starbucks: Welcher To-go-Becher passt zu dir? | kaffeebecher von starbucks | Which cup? |
| H2 | 1. Welche Kaffeebecher von Starbucks gibt es? | starbucks becher arten | What types? |
| H2 | 2. Welcher Becher passt zu welchem Einsatz? | welcher starbucks becher | Which for me? |
| H2 | 3. Hält ein Starbucks Thermobecher dicht und warm? | thermobecher dicht | Does it leak? |
| H2 | 4. Passt mein Becher zu Tall, Grande oder Venti? | starbucks becher oz ml | Size fit? |
| H2 | 5. Wo kann man … kaufen? | kaffeebecher starbucks kaufen | Where to buy? |
| H2 | 6. Eigenen Becher mitbringen | eigener becher rabatt | Discount? |
| H2 | 7. Pflege | spülmaschine | Care? |
| H2 | 8. Original oder Fälschung | original starbucks becher | Real? |
| H2 | Häufig gestellte Fragen | | 11 Qs |

## 8. Internal links + cannibalisation

- **High overlap with `blog/starbucks-becher`** (3,191 words; types/prices/Pfand/care/buying/fakes). The risk is **real**. Mitigation: this post owns the *selection/buyer's-decision* angle (checklist, oz table, leak/warmth test). Pricing and the discount program are summarised and linked with `#rabatt-und-pfand`, not repeated. **Alternative:** publish it as a new H2 block on starbucks-becher instead. Decide before publishing.
- Also add a link from becher → this page ("Welcher Becher passt zu dir?").
- Out-links: /blog/starbucks-becher (+#rabatt-und-pfand), /blog/starbucks-tasse, /blog/starbucks-groessen-tall-grande-venti, /starbucks-in-meiner-naehe, /blog/starbucks-tassen.

## 9. FAQ source map
Price → §3 Otto · Pappbecher → ehrenkaffee · Pfand → starbucks.de · other brands → starbucks.de · warm → test.de/physics · Cold Cup hot → becher page care section · 16 oz → groessen · shop → becher §8 · Deutschland-Motiv → memory (YAH) · test → test.de · oz → general.
