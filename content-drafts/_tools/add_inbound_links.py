"""Wrap the first unlinked body mention (inside p/td/li, not headings/summary/links) with an internal link."""
import re, pathlib

BLOG = pathlib.Path(__file__).resolve().parents[2] / "blog"
MOC, FLU, LOGO = "/blog/starbucks-mocha", "/blog/starbucks-flughafen", "/blog/starbucks-logo-name-bedeutung"
TARGETS = [
    ("starbucks-kaffee.html", "Caffè Mocha", MOC), ("starbucks-menu.html", "Caffè Mocha", MOC),
    ("starbucks-kalorien-guide.html", "Caffè Mocha", MOC), ("starbucks-getraenke.html", "Caffè Mocha", MOC),
    ("starbucks-heisse-schokolade.html", "Mocha-Sauce", MOC), ("starbucks-preise.html", "Caffè Mocha", MOC),
    ("starbucks-kapseln-angebot.html", "White Mocha", MOC),
    ("starbucks-preise.html", "Bahnhöfen und Flughäfen", FLU), ("starbucks-deutschland-filialen.html", "Bahnhöfen und Flughäfen", FLU),
    ("starbucks-geoeffnet.html", "Flughafenfilialen", FLU), ("starbucks-in-der-naehe.html", "Flughäfen oder Raststätten", FLU),
    ("starbucks-near-me.html", "Hauptbahnhöfen und Flughäfen", FLU), ("starbucks-greding.html", "Autobahn A9", FLU),
    ("starbucks-menu.html", "Bahnhofs- und Flughafen-Filialen", FLU), ("starbucks-mocha.html", "Bahnhöfen und Flughäfen", FLU),
    ("starbucks-kaffee.html", "Howard Schultz", LOGO), ("starbucks-becher.html", "Sirenen-Logo", LOGO),
    ("starbucks-tassen.html", "Sirenen-Logo", LOGO), ("starbucks-kapseln-angebot.html", "Sirenen-Logo", LOGO),
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
