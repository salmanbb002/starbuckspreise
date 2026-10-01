"""Wrap the first unlinked body mention (inside p/td/li, not headings/summary/links) with an internal link."""
import re, pathlib

BLOG = pathlib.Path(__file__).resolve().parents[2] / "blog"
WEI, RES, GEB = "/blog/starbucks-weihnachten", "/blog/starbucks-reserve", "/blog/starbucks-gebaeck"
TARGETS = [
    ("starbucks-latte.html", "Toffee Nut Latte", WEI), ("starbucks-pumpkin-spice-latte.html", "Weihnachtskarte", WEI),
    ("starbucks-menu.html", "Lebkuchen Latte", WEI), ("starbucks-frappuccino-sorten.html", "Lebkuchen Coffee Frappuccino", WEI),
    ("starbucks-becher-aktuell.html", "Holiday-Kollektion", WEI), ("starbucks-kapseln-angebot.html", "Weihnachtszeit", WEI),
    ("starbucks-stadtmitte.html", "Starbucks Reserve", RES), ("starbucks-stadtmitte.html", "Reserve-Kaffees", RES),
    ("starbucks-preise.html", "Reserve", RES), ("starbucks-kaffee.html", "Single-Origin-Spezialitäten", RES),
    ("starbucks-fruehstueck.html", "Zimtschnecke", GEB), ("starbucks-menu.html", "Muffins", GEB),
    ("starbucks-kalorien-guide.html", "Carrot Cake", GEB), ("starbucks-preise.html", "Muffin", GEB),
    ("starbucks-vegane-optionen.html", "veganem Gebäck", GEB),
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
