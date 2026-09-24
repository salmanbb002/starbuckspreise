# Merge-Insert: „starbucks caramel macchiato“ → /iced-caramel-macchiato

> **Einbau-Anleitung (nicht veröffentlichen).** Ergänzt die Root-Seite `iced-caramel-macchiato.html` um die heiße Variante und damit um „starbucks caramel macchiato“ (720 Suchen/Monat, KD 28). Die Seite nutzt das ältere Root-Template: nur `<h2>`, FAQ als `<p><strong>`, **kein JSON-LD**.
>
> 1. **Korrekturen zuerst** (Fehler auf der Live-Seite):
>    - FAQ „Wie viel Koffein enthält er?“: „Ein Grande enthält etwa 75 mg“ ist falsch. Laut Starbucks-US-Nährwerten hat ein Tall 75 mg und ein Grande 150 mg. Ersatz-Antwort steht in Block C.
>    - Größenliste: „Venti (591 ml)“ gilt für heiße Getränke. Ein Iced Venti hat laut unserer eigenen Menü-Seite 709 ml. Auf „Venti (709 ml)“ ändern.
>    - Kalorienabsatz: „Ein Grande Iced Caramel Macchiato … 847 kJ / 201 kcal“. Unsere `menu.js` führt 201 kcal ohne Größenangabe, und bei der heißen Variante entspricht derselbe Wert (214 kcal) laut fddb einem **Tall**. Empfehlung: „Grande“ durch „Tall“ ersetzen oder die Größe weglassen.
> 2. **Block A** als neue H2 nach „Was steckt drin?“ einfügen (vor „Preis & Größen 2026“).
> 3. **Block B** (H2) direkt nach Block A.
> 4. **Block C** an die FAQ anhängen, im bestehenden `<p><strong>Frage</strong> Antwort</p>`-Format.
> 5. Title optional erweitern auf **„Iced Caramel Macchiato & Caramel Macchiato: Preis 2026 – Starbucks“** (57 Zeichen). Meta-Description optional: **„Starbucks Caramel Macchiato heiß ab 4,99 €, Iced ab 5,79 €: Preise, Kalorien, Koffein und der Unterschied zum Latte im Überblick – aktuell für 2026.“** H1 und URL bleiben.
> 6. `schema.jsonld` enthält ein **vollständiges** Graph (Article + FAQPage) für diese Seite, da sie bisher keins hat.

---

## Block A (neue H2)

## Caramel Macchiato heiß: Was unterscheidet ihn vom Iced Caramel Macchiato?

Der heiße **Caramel Macchiato** hat dieselben vier Zutaten wie die **Iced-Version**, nur mit gedämpfter statt kalter Milch und ohne Eis: **Vanillesirup**, aufgeschäumte Milch, **Espresso** obenauf und **Karamellsauce** als Topping. Auf unserer Preisliste kostet er ab **4,99 €** und ist damit 0,80 € günstiger als der **Iced Caramel Macchiato** ab **5,79 €**.

Der Name verrät den Aufbau. „**Macchiato**“ ist italienisch für „**gefleckt**“ oder „**markiert**“, und **Starbucks** beschreibt das Getränk selbst als Milch mit **Vanillesirup**, die mit **Espresso** „markiert“ wird. Der Espresso kommt also zuletzt in die Tasse und zeichnet sich als dunkler Fleck im Milchschaum ab. Der **Karamell-Drizzle** schließt das Getränk oben ab.

| | Caramel Macchiato (heiß) | Iced Caramel Macchiato |
|---|---|---|
| Preis laut unserer Liste | ab 4,99 € | ab 5,79 € |
| Energie (kleinste Größe) | 901 kJ / 214 kcal | 847 kJ / 201 kcal |
| Milch | gedämpft und aufgeschäumt | kalt, auf Eis |
| Venti-Füllmenge | 591 ml | 709 ml |
| Koffein Tall / Grande* | 75 mg / 150 mg | 75 mg / 150 mg |
| Passt zu | Herbst und Winter, zum Mitnehmen | Sommer, mit Strohhalm |

*Koffeinwerte laut **Starbucks**-USA-Nährwertangaben; deutsche Rezepturen können abweichen.

In der kleinsten Größe hat die **Iced-Variante** etwas weniger **Energie** (201 statt 214 **kcal**), vermutlich weil Eiswürfel einen Teil der Milch ersetzen. Wer den Geschmack will, aber auf den **Preis** achtet, fährt mit der heißen Version günstiger.

---

## Block B (neue H2)

## Wie viele Kalorien, wie viel Zucker und Koffein hat ein Caramel Macchiato?

Ein **heißer Caramel Macchiato** in **Tall**-Größe (355 ml) hat rund 214 **kcal**. Das deckt sich mit fddb, wo ein Tall mit 213 kcal, 8,9 g Fett, 25,9 g Kohlenhydraten und 7,8 g Eiweiß geführt wird. Pro 100 ml sind das etwa 60 kcal und 7 g **Zucker**.

Hochgerechnet steckt in einem **Tall** damit knapp 25 g **Zucker**, in einem **Venti** (591 ml) laut Yazio 41,2 g bei 312 **kcal**. Beim **Koffein** zählt die Zahl der **Espresso-Shots**: Laut **Starbucks** USA hat ein Tall **75 mg**, **Grande** und Venti je **150 mg**. Den größten Hebel gegen **Kalorien** haben die Milchsorte und der **Sirup**. Konkrete Tipps stehen im Abschnitt „Kalorien sparen“ weiter unten.

| Größe | Füllmenge | Kalorien (ca.) | Koffein* |
|---|---|---|---|
| Tall | 355 ml | 213–214 kcal | 75 mg |
| Grande | 473 ml | 250 kcal* | 150 mg |
| Venti | 591 ml | 312 kcal | 150 mg |

*Grande-**Kalorien** und Koffeinwerte laut **Starbucks** USA (mit 2 %-Milch). **Tall** laut unserer Preisliste und fddb, **Venti** laut Yazio. Deutsche Rezepturen können leicht abweichen.

Wer statt des **Caramel Macchiato** einen ungesüßten Klassiker sucht: Ein [**Latte Macchiato**](/blog/starbucks-latte-macchiato) hat mit 147 **kcal** rund ein Drittel weniger **Energie**, weil kein **Sirup** hineinkommt.

---

## Block C: FAQ

**Ersatz-Antwort für „Wie viel **Koffein** enthält er?“:**
Ein **Tall** **Iced Caramel Macchiato** enthält laut **Starbucks**-USA-Angaben etwa **75 mg** **Koffein**, ein **Grande** etwa **150 mg**, weil er zwei **Espresso-Shots** bekommt. Das ist ein moderater Wert für ein Espressogetränk.

**Neue FAQs:**

**Was ist ein **Caramel Macchiato** bei **Starbucks**?**
Ein **Caramel Macchiato** ist ein Espressogetränk aus **Vanillesirup**, gedämpfter Milch und **Espresso**, der zuletzt obenauf gegossen wird, mit **Karamellsauce** als Topping. **Starbucks** bietet ihn heiß und als **Iced Caramel Macchiato** an.

**Was kostet ein **Caramel Macchiato** bei **Starbucks**?**
Der heiße **Caramel Macchiato** kostet laut unserer Preisliste ab **4,99 €**, der **Iced Caramel Macchiato** ab **5,79 €**. An Bahnhöfen und Flughäfen liegen die Preise meist höher.

**Wie viele **Kalorien** hat ein **Caramel Macchiato**?**
Ein heißer **Tall** (355 ml) hat rund 214 **kcal**, ein **Venti** (591 ml) etwa 312 kcal. Die **Iced-Variante** liegt in der kleinsten Größe bei etwa 201 kcal.

**Wie viel **Zucker** ist in einem **Caramel Macchiato**?**
Rund 7 g pro 100 ml. Ein **Tall** enthält damit knapp 25 g **Zucker**, ein **Venti** laut Yazio 41,2 g. Der Zucker kommt aus **Vanillesirup**, **Karamellsauce** und dem Milchzucker.

**Was bedeutet „**Macchiato**“?**
„**Macchiato**“ ist italienisch und bedeutet „**gefleckt**“ oder „**markiert**“. Beim **Caramel Macchiato** markiert der zuletzt eingegossene **Espresso** die Milch, er bildet einen dunklen Fleck im Schaum.

**Was ist der Unterschied zwischen **Caramel Macchiato** und **Caffè Latte**?**
Beim **Caffè Latte** kommt der **Espresso** zuerst in die Tasse und wird mit Milch aufgegossen, **Sirup** gibt es nur auf Wunsch. Der **Caramel Macchiato** enthält immer **Vanillesirup**, der Espresso kommt zuletzt, und obenauf gibt es **Karamellsauce**. Laut unserer Liste kostet ein Caffè Latte ab 4,59 € und hat rund 151 **kcal**.

**Was ist der Unterschied zwischen **Caramel Macchiato** und **Latte Macchiato**?**
Beide sind geschichtet, aber der **Latte Macchiato** kommt ohne **Sirup** und ohne **Karamell** aus. Er hat deshalb nur rund 147 **kcal** statt 214 kcal und kostet laut unserer Liste ab 4,70 €.

**Ist ein **Caramel Macchiato** stark?**
Nein, er ist ein milchbetontes Getränk. Ein **Tall** enthält mit **75 mg** **Koffein** etwa so viel wie ein einzelner **Espresso**-Shot, der Geschmack wird von Milch, Vanille und **Karamell** bestimmt.

**Welche **Größen** gibt es beim **Caramel Macchiato**?**
In Deutschland gibt es ihn in **Tall** (355 ml), **Grande** (473 ml) und **Venti** (591 ml heiß bzw. 709 ml iced). Die Preise steigen mit der Größe, beim **Iced Caramel Macchiato** von **5,79 €** (Tall) bis 6,90 € (Venti).

**Gibt es **Caramel Macchiato** von **Starbucks** für zu Hause?**
Ja, als Kapsel für Nescafé Dolce Gusto. **Starbucks** führt dort den **Caramel Macchiato** (Medium Roast) mit Milchpulver. Aktuelle Angebote stehen in unserem Ratgeber zum [Starbucks Kapseln Angebot](/blog/starbucks-kapseln-angebot).


---
## Unused-term notes
- None unused.
- Deliberately skipped: US dollar prices (DE site), birthday-drink/deals questions (belong to the Rewards/Karte insert), and a 'healthy?' verdict (no source).
