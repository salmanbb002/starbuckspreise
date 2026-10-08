# Research notes – starbucks hund / starbucks puppuccino (2026-10-09)

## 1. Keyword, intent, SERP
- Primary: **starbucks hund** (~20/mo, Research_Oct2026, "New post (Oct 2026)") with **starbucks puppuccino** folded in (under threshold, 6 variants). The sheet's target cell says /blog/starbucks-fuer-kinder (copy error); written as /blog/starbucks-hund.
- Intent: know-simple (may dogs enter?) + know (what is a Puppuccino, is it available in Germany, is it safe?). SERP via WebSearch is US-proxied: dogster.com, querysprout.com, expertbeacon.com, enviroliteracy.org, oodlelife.com, dexerto.com, bark.co, akc.org, marieclaire.co.uk. No German page on the topic was returned. PAA not captured.
- Fan-out, Google Autocomplete hl=de gl=de, live 9 Oct 2026: starbucks hunde erlaubt · starbucks hunde sahne · starbucks hundegetränk · starbucks hundeeis · starbucks hundespielzeug · starbucks hunde erlaubt schweiz · starbucks becher hund · dürfen hunde bei starbucks rein · starbucks puppuccino deutschland / österreich / price / cost / uk / ingredients / japan · puppuccino hund · starbucks pup cup deutschland / price / free / for cats.

## 2. Head entities
| Entity | Type | sameAs | Facts |
|---|---|---|---|
| Puppuccino (Pup Cup) | Product | – (unlinked) | small cup of whipped cream for dogs, off-menu |
| Haushund | Animal | de.wikipedia.org/wiki/Haushund | – |
| Starbucks | Organization | wikidata Q37158 | 170 German branches in the locator (6 Oct 2026) |
| Hausrecht | Concept | de.wikipedia.org/wiki/Hausrecht | operator decides on dogs |

## 3. Sources (fetched 9 Oct 2026 unless noted)
| # | Source | Facts used |
|---|---|---|
| S1 | hogapage.de "Dürfen Wirte Hunde verbieten?" (dpa-tmn, Markus Jergler, 5 Jun 2018) | "Eine gesetzliche Regelung, die Hunde in Restaurants oder Kneipen verbietet, gibt es aber nicht."; Hausrecht per Deutscher Anwaltverein; no sign at the door → owners may assume dogs are allowed |
| S2 | eur-lex.europa.eu, VO (EG) 852/2004 Anhang II Kapitel IX Nr. 4 (consolidated 24.03.2021) | procedures must prevent pets from accessing rooms where food is prepared, handled or stored |
| S3 | gesetze-im-internet.de/bgg/__12e.html | operators may not refuse access because of the assistance dog unless unverhältnismäßige oder unbillige Belastung; (4) dog must be marked; (6) names Blindenführhunde |
| S4 | starbucks.de/de/faq (payload searched) | no entry containing "Hund", "Haustier" or "Assistenz" |
| S5 | starbucks.de/api/v2/storeFeatures | four features only: DR Reward einlösen, DT Drive-Through, WF Drahtloser Hotspot, XO Mobiles Bestellen und Bezahlen |
| S6 | store-locator sweep of 6 Oct 2026 (content-drafts/starbucks-wlan-2026-10-06/…csv) | 170 branches; type from store name (derived, flagged): 133 Einkaufszentrum und Sonstige, 21 Bahnhof, 10 Autobahn und Autohof, 6 Flughafen; DT: Düsseldorf Erkrather Straße, Feuchtwangen Autohof (Schnelldorf); XO in 145 of 170 |
| S7 | bahnhof.de Hausordnung (PDF, Stand November 2024) Nr. 1.14 | prohibited: "Führen von Hunden ohne Leine und ohne geeigneten Maulkorb. Kosten für die Beseitigung von Verschmutzungen durch Hunde werden in Rechnung gestellt" |
| S8 | dexerto.com (Lauren Lewis, 26 Feb 2024) | "A Puppuccino is just a small Starbucks cup, with a helping of whipped cream inside."; secret menu item; not orderable in the app; "Most of the time, you won't be charged" (US) |
| S9 | Order menu starbucks.de (135 products) + starbucksfreiburg.de | no product named Puppuccino / Pup Cup / anything for animals; latte product page lists topping "Sahne" without a price |
| S10 | Allergen-PDF „Autumn – 10.09.2026 (Getränke)“ | "Schlagsahne Topping": 16 g (hot Short), 19 g (hot Tall), 22 g (hot Grande/Venti), 25 g (cold Tall), 35 g (cold Grande), 32 g (cold Venti); "Vegane Schlagcreme Topping"; sugar-free syrups marked "** Kann bei übermäßigem Verzehr abführend wirken" |
| S11 | starbucks.de/de/menu-drinks-hot-chocolates | Signature Hot Chocolate "gekrönt mit gesüßter Schlagsahne" |
| S12 | milchindustrie.de Milkipedia "Schlagsahne" | at least 30 % fat → 16–35 g ≈ 4,8–10,5 g fat (own calculation) |
| S13 | akc.org "Restaurants With Dog Treats" (Jessika Zachary, updated 17 Feb 2026) | lists the Puppuccino; treats "may not be suitable if your dog is dealing with obesity or canine diabetes, … history of intolerance to dairy products, … gastrointestinal issues and pancreatitis"; "ask your veterinarian when in doubt". (Its line "made out with a small amount of espresso" is an error in the AKC text and was NOT used.) |
| S14 | fressnapf.de Magazin "Dürfen Hunde Milch trinken?" (31 Jan 2025) | lactase; adult dogs often lose it; diarrhoea, flatulence, cramps, vomiting; low-lactose: Quark, Hüttenkäse, Joghurt |
| S15 | fressnapf.de Magazin "Giftige Lebensmittel für Hunde" (20 Apr 2026) | theobromine, "Je dunkler die Schokolade, desto mehr Theobromin"; caffeine dangerous; xylitol → blood-sugar drop |
| S16 | tasso.net Wissensportal "Problematische und giftige Lebensmittel für Hund und Katze" | coffee, tea, cola problematic; theobromine toxic; xylitol: "Selbst kleinste Mengen … tödliche Unterzuckerung, Krämpfe oder Leberversagen"; raisins → kidney damage; macadamia → neurological symptoms |
| S17 | petbook.de "Leckerlis für Hunde" (Manuela Bauer, 17 Sep 2022) | treats under ten percent of the daily food amount |
| S18 | starbucks.de/de/menu-merchandise-core | cups, mugs, tumblers only; nothing for dogs |
- Not reachable: about.starbucks.com (Cloudflare, also in headless Chrome today), news.starbucks.com (connection refused), dogster.com and rover.com (403), wamiz.co.uk (410). No official Starbucks statement on the Puppuccino was found; the article says so.

## 4. Competitors
| # | URL | Headings / what it has |
|---|---|---|
| C1 | querysprout.com/does-starbucks-allow-dogs (Marques Thomas, Sep 2023) | Pet Policy · Dogs On the Patio · Service Animals · What Is the Pup Cup · What Stores Allow Dogs. US health-code framing |
| C2 | oodlelife.com/starbucks-puppuccino (Chris Allen, updated 4 Mar 2024) | What Is · National Puppuccino Day · How To Order · Cost · Safe For My Dog · Lactose Intolerant · Homemade / Lactose-free Recipe · What Is In It · Official Item? · Can I Get My Dog Into Starbucks · Only At Starbucks? |
| C3 | dexerto.com (see S8) | what it is, how to order, price |
| C4 | akc.org (see S13) | health caveats |
- None covers Germany: no Hausrecht, no § 12e BGG, no station rules, no German menu check.

## 5. Entity ledger → entities.json
T1: Starbucks, Hund, Puppuccino / Pup Cup, Hausrecht, Schlagsahne, Starbucks Deutschland, Filiale. T2: Assistenzhund, § 12e BGG, VO (EG) 852/2004, Bahnhof / Hausordnung der Deutschen Bahn, Drive-Through, Bestellkarte, Laktose, Fett, Zucker, Tierarzt, Koffein, Schokolade / Theobromin, Xylit, Preis, App, Filialfinder. T3: Hundeeis, Hundespielzeug, Hundebecher, Vegane Schlagcreme, Rosinen, Macadamia, American Kennel Club, TASSO, Petbook.
Relations: Filiale —decides via→ Hausrecht · no law —bans→ dogs in cafés · VO 852/2004 —keeps pets out of→ food preparation rooms · § 12e BGG —grants access to→ Assistenzhunde · DB Hausordnung —requires→ leash and muzzle · Puppuccino = Schlagsahne in a small cup · German order menu (135 products) —lists no→ Puppuccino · Schlagsahne —contains→ lactose, ≥30 % fat, sugar · AKC —advises against for→ obesity, diabetes, dairy intolerance, pancreatitis · coffee / chocolate / xylitol —are toxic to→ dogs · 2 of 170 branches —have→ Drive-Through · 145 of 170 —offer→ mobile ordering.
Dedupe / parked: patio rule (US concept, no German source), National Puppuccino Day, homemade recipe (different intent), "only at Starbucks?" (other chains), Austria / Switzerland (not researched), first-ever pet collection (could not be verified).

## 6. Information gain
(1) German legal frame with primary sources. (2) Location matrix from the store locator (170 branches, who decides where). (3) Check of the German order menu: no Puppuccino among 135 products. (4) Official topping weight (16–35 g) and "gesüßte Schlagsahne". (5) "Which dog may have it" table. (6) "What not to share" table mapped to the German menu. (7) Checklist. Two inline figures.

## 7. Heading + keyword + question map
| Lvl | Heading | Phrase | Carries |
|---|---|---|---|
| H1 | Starbucks mit Hund: Sind Hunde erlaubt und gibt es den Puppuccino? | starbucks hund | focus |
| H2 | 1. Sind Hunde bei Starbucks in Deutschland erlaubt? | starbucks hunde erlaubt | Hausrecht, VO 852/2004 |
| H3 | Was gilt für Assistenzhunde? | – | § 12e BGG |
| H2 | 2. Welche Regeln gelten am Bahnhof, im Einkaufszentrum und am Flughafen? | – | locator data, DB Hausordnung |
| H3 | Drive-Through und mobiles Bestellen | – | DT, XO |
| H2 | 3. Was ist ein Puppuccino? | starbucks puppuccino | Pup Cup |
| H2 | 4. Gibt es den Puppuccino bei Starbucks in Deutschland? | puppuccino deutschland | Bestellkarte |
| H3 | Wie fragst du nach einem Puppuccino? | – | HowTo |
| H2 | 5. Ist Schlagsahne für Hunde gesund? | starbucks hunde sahne | Laktose, Fett, Zucker, AKC |
| H3 | Welche Alternative ist besser verträglich? | – | Quark, vegane Schlagcreme |
| H2 | 6. Was darf dein Hund bei Starbucks nicht bekommen? | starbucks hundegetränk | Koffein, Theobromin, Xylit |
| H2 | 7. Gibt es Hundeeis, Hundebecher oder Hundespielzeug bei Starbucks? | hundeeis, hundespielzeug, becher hund | merchandise |
| H2 | 8. Checkliste: So klappt der Besuch mit Hund | – | checklist |

## 8. Internal links
Out: flughafen, drive-in, app, in-der-naehe, koffeinfrei, becher-aktuell, halloween, becher, wlan, geoeffnet, deutschland-filialen, outlet, heisse-schokolade, sirup, gebaeck, milchalternativen, fuer-kinder. In (16): in-der-naehe, near-me, deutschland-filialen, drive-in, wlan, fuer-kinder, app, stadtmitte, outlet, gebaeck, heisse-schokolade, closest-to-me, flughafen, geoeffnet, sirup, milchalternativen. Published 9 Oct 2026, commit e513174. Cannibalisation: /blog/starbucks-closest-to-me has one FAQ on dogs ("in den allermeisten … Stores … herzlich willkommen", unsourced); it now links here.
