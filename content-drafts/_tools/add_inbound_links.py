"""Inbound links for a new post: TARGETS wrap the first unlinked body mention (inside p/td/li, not headings/summary/links);
REPLACES swap one exact, unique passage for the same passage with a link or one added sentence. Idempotent."""
import re, pathlib

BLOG = pathlib.Path(__file__).resolve().parents[2] / "blog"
KOF, HUND = "/blog/starbucks-koffeinfrei", "/blog/starbucks-hund"
TARGETS = [  # wrap an existing mention (also safe inside FAQ answers: the visible text stays the same)
    ("starbucks-iced-coffee.html", "entkoffeinierter Espresso", KOF),
    ("starbucks-closest-to-me.html", "gut erzogene Hunde", HUND),
]
K, H = f'<a href="{KOF}">', f'<a href="{HUND}">'
REPLACES = [  # exact text that must occur exactly once in the file -> same text with a link or one added sentence
    ("starbucks-americano.html", "Die entkoffeinierte Variante hat im Grande", f"Die {K}entkoffeinierte Variante</a> hat im Grande"),
    ("starbucks-kaffeebohnen.html", "auf Blonde oder Decaf wechseln.", f"auf Blonde oder {K}Decaf</a> wechseln."),
    ("starbucks-kapseln-angebot.html", "Wer entkoffeinierten Kaffee bevorzugt,", f"Wer {K}entkoffeinierten Kaffee</a> bevorzugt,"),
    ("starbucks-tee.html", "greift zu diesen beiden Sorten.", f"greift zu diesen beiden Sorten. Alle Getränke ohne Koffein, auch Kaffee als Decaf, zeigt der Ratgeber {K}Starbucks koffeinfrei</a>."),
    ("starbucks-mocha.html", "gibt es den Mocha auch als Decaf (27,9 mg im Grande).", f"gibt es den Mocha auch {K}als Decaf</a> (27,9 mg im Grande)."),
    ("starbucks-pumpkin-spice-latte.html", "Der Decaf Pumpkin Spice Latte hat nur 3,6 mg Koffein,", f"Der {K}Decaf</a> Pumpkin Spice Latte hat nur 3,6 mg Koffein,"),
    ("starbucks-vanilla-latte.html", "Decaf macht aus dem Getränk einen entkoffeinierten Vanilla Latte.", f"Decaf macht aus dem Getränk einen entkoffeinierten Vanilla Latte. Wie viel Restkoffein bleibt, steht im Ratgeber {K}Starbucks koffeinfrei</a>."),
    ("starbucks-kaffee.html", "oder <strong>Decaf</strong> (3,6 mg Koffein im Grande Latte).", f"oder {K}<strong>Decaf</strong></a> (3,6 mg Koffein im Grande Latte)."),
    ("starbucks-matcha-latte.html", "Wer abends etwas ohne Koffein möchte,", f"Wer abends etwas {K}ohne Koffein</a> möchte,"),
    ("starbucks-protein.html", "oder die Decaf-Version mit 3,6 mg.", f"oder die {K}Decaf-Version</a> mit 3,6 mg."),
    ("starbucks-kalorien-guide.html", "<td>Decaf Caffè Latte</td>", f"<td>{K}Decaf Caffè Latte</a></td>"),
    ("starbucks-fuer-kinder.html", "welche Getränke ohne Kaffee auskommen.", f"welche Getränke ohne Kaffee auskommen. Die offiziellen Koffeinwerte aller Getränke stehen im Ratgeber {K}Starbucks koffeinfrei</a>."),
    ("starbucks-cappuccino.html", "sie unterscheiden sich nur in Milch, Schaum und Sirup.", f"sie unterscheiden sich nur in Milch, Schaum und Sirup. Mit der Bohne Decaf sinkt das Koffein im Grande auf 3,6 mg, siehe {K}Starbucks koffeinfrei</a>."),
    ("starbucks-cold-brew.html", "dann ist mehr Kaffee im Becher.", f"dann ist mehr Kaffee im Becher. Entkoffeiniert gibt es Cold Brew nicht, die Alternativen stehen im Ratgeber {K}Starbucks koffeinfrei</a>."),
    ("starbucks-in-der-naehe.html", "oder barrierefrei erreichbar ist.", f"oder barrierefrei erreichbar ist. Ein Merkmal für Hunde gibt es dort nicht. Was mit Vierbeiner gilt, erklärt der Ratgeber {H}Starbucks mit Hund</a>."),
    ("starbucks-near-me.html", "Sonnenplätze auf der Terrasse für Frühlings- und Sommertage.", f"Sonnenplätze auf der Terrasse für Frühlings- und Sommertage. Was mit Vierbeiner gilt, steht unter {H}Starbucks mit Hund</a>."),
    ("starbucks-deutschland-filialen.html", 'zeigt unser Guide <a href="/blog/starbucks-stadtmitte">Starbucks Stadtmitte</a>.', f'zeigt unser Guide <a href="/blog/starbucks-stadtmitte">Starbucks Stadtmitte</a>. Ob Hunde mit in die Filiale dürfen, hängt vom Standort ab, siehe {H}Starbucks mit Hund</a>.'),
    ("starbucks-drive-in.html", "holst Getränk und Snack am Fenster ab, ohne auszusteigen.", f"holst Getränk und Snack am Fenster ab, ohne auszusteigen. Das ist auch praktisch, wenn ein Hund im Auto sitzt, siehe {H}Starbucks mit Hund</a>."),
    ("starbucks-wlan.html", "führt Steckdosen im Store Locator nicht als Merkmal.", f"führt Steckdosen im Store Locator nicht als Merkmal. Auch für Hunde gibt es dort kein Merkmal, mehr dazu im Ratgeber {H}Starbucks mit Hund</a>."),
    ("starbucks-fuer-kinder.html", "Du bestellst Kindergetränke deshalb aus dem normalen Sortiment.", f"Du bestellst Kindergetränke deshalb aus dem normalen Sortiment. Auch für Hunde gibt es keine eigene Karte, siehe {H}Starbucks mit Hund</a>."),
    ("starbucks-app.html", "in teilnehmenden Filialen, nicht in jedem Store.", f"in teilnehmenden Filialen, nicht in jedem Store. Das hilft auch, wenn du mit Hund unterwegs bist und nur kurz hinein willst, siehe {H}Starbucks mit Hund</a>."),
    ("starbucks-stadtmitte.html", "und Außenplätze in der Fußgängerzone.", f"und Außenplätze in der Fußgängerzone. Was für Besucher mit Hund gilt, steht unter {H}Starbucks mit Hund</a>."),
    ("starbucks-outlet.html", "und Starbucks veröffentlicht sie nicht einheitlich.", f"und Starbucks veröffentlicht sie nicht einheitlich. Ob Hunde mit hinein dürfen, regelt neben der Filiale auch das Center, siehe {H}Starbucks mit Hund</a>."),
    ("starbucks-gebaeck.html", "als saftige Karottentorte mit Cheesecake-Crème und Rosinen.", f"als saftige Karottentorte mit Cheesecake-Crème und Rosinen. Für Hunde sind Rosinen und Schokolade tabu, mehr dazu im Ratgeber {H}Starbucks mit Hund</a>."),
    ("starbucks-heisse-schokolade.html", "dadurch fällt sie süßer und kalorienreicher aus.", f"dadurch fällt sie süßer und kalorienreicher aus. Als Leckerli für Hunde taugt die Sahne nur bedingt, siehe {H}Starbucks mit Hund</a>."),
    ("starbucks-latte.html", 'stehen in unserer Übersicht der <a href="/blog/starbucks-kalorien-guide">Starbucks Nährwerte</a>.', f'stehen in unserer Übersicht der <a href="/blog/starbucks-kalorien-guide">Starbucks Nährwerte</a>. Mit der Bohne Decaf hat ein Grande Latte nur 3,6 mg Koffein, siehe {K}Starbucks koffeinfrei</a>.'),
    ("starbucks-groessen-tall-grande-venti.html", "wer es milder mag, kann das an der Kasse anpassen lassen.", f"wer es milder mag, kann das an der Kasse anpassen lassen. Ohne Koffein geht es mit der Bohne Decaf, siehe {K}Starbucks koffeinfrei</a>."),
    ("starbucks-preise.html", "ohne Aufpreis den helleren Starbucks Blonde Roast wählen.", f"ohne Aufpreis den helleren Starbucks Blonde Roast wählen. Entkoffeiniert gibt es die Getränke mit der Bohne Decaf, siehe {K}Starbucks koffeinfrei</a>."),
    ("starbucks-getraenke.html", '<a href="/blog/starbucks-sirup">Sirup-Shots</a> individuell anpassen.', f'<a href="/blog/starbucks-sirup">Sirup-Shots</a> individuell anpassen. Welche Getränke kein Koffein enthalten, zeigt der Ratgeber {K}Starbucks koffeinfrei</a>.'),
    ("starbucks-menu.html", "weil sie mit aufgeschäumter Milch und Sirup zubereitet werden.", f"weil sie mit aufgeschäumter Milch und Sirup zubereitet werden. Koffeinfrei sind von den Tees nur die Kräutersorten, siehe {K}Starbucks koffeinfrei</a>."),
    ("../iced-caramel-macchiato.html", "Wer es ohne Kaffee möchte, nimmt den Caramel Cream Frappuccino®.", f"Wer es ohne Kaffee möchte, nimmt den Caramel Cream Frappuccino®. Er hat 0 mg Koffein, mehr dazu unter {K}Starbucks koffeinfrei</a>."),
    ("starbucks-flughafen.html", "Das ist der Lizenznehmer von Starbucks in Deutschland.", f"Das ist der Lizenznehmer von Starbucks in Deutschland. An Bahnhöfen und Flughäfen gilt außerdem die Hausordnung des Betreibers, etwa für Hunde, siehe {H}Starbucks mit Hund</a>."),
    ("starbucks-geoeffnet.html", "oft von früh morgens bis spät in die Nacht.", f"oft von früh morgens bis spät in die Nacht. Für Hunde gilt dort die Hausordnung des Betreibers, siehe {H}Starbucks mit Hund</a>."),
    ("starbucks-sirup.html", "welche zuckerfreien Sorten deine Filiale hat.", f"welche zuckerfreien Sorten deine Filiale hat. Für Hunde ist Zuckerfreies tabu, warum, steht im Ratgeber {H}Starbucks mit Hund</a>."),
    ("starbucks-milchalternativen.html", "Für Menschen mit Laktoseintoleranz ist das die wichtigste Falle.", f"Für Menschen mit Laktoseintoleranz ist das die wichtigste Falle. Laktose ist auch der Grund, warum Sahne nicht jedem Hund bekommt, siehe {H}Starbucks mit Hund</a>."),
]


def link(fname, txt, href):
    f = BLOG / fname
    s = f.read_text()
    if f'href="{href}"' in s:
        return "already linked"
    start = s.find('<div class="article-content">')
    start = start if start > 0 else s.find("<main")
    for m in re.finditer(re.escape(txt), s[start:]):
        i = start + m.start()
        before = s[:i]
        if before.rfind(">") < before.rfind("<"):
            continue  # inside a tag or attribute
        stack = []
        for close, t in re.findall(r"<(/?)(a|p|td|li|h[1-6]|summary|script)\b", before[-4000:]):
            if close and t in stack:
                del stack[len(stack) - 1 - stack[::-1].index(t)]
            elif not close:
                stack.append(t)
        if {"a", "script", "h1", "h2", "h3", "h4", "summary"} & set(stack) or not {"p", "td", "li"} & set(stack):
            continue
        f.write_text(s[:i] + f'<a href="{href}">{txt}</a>' + s[i + len(txt):])
        return "linked"
    return "NO SPOT"


for fname, txt, href in TARGETS:
    print(f"{link(fname, txt, href):14} {fname} :: {txt}")

for fname, old, new in REPLACES:
    f = BLOG / fname
    t = f.read_text()
    href = re.search(r'href="(/blog/[^"]+)">(?!.*href=")', new, flags=re.S).group(1)
    if new in t:
        res = "already linked"
    elif t.count(old) != 1:
        res = f"NO SPOT ({t.count(old)}x)"
    else:
        f.write_text(t.replace(old, new)); res = "linked"
    print(f"{res:14} {fname} :: {href}")
