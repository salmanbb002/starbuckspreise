"""Wrap the first unlinked body mention (inside p/td/li, not headings/summary/links) with an internal link."""
import re, pathlib

BLOG = pathlib.Path(__file__).resolve().parents[2] / "blog"
HAL, VAN = "/blog/starbucks-halloween", "/blog/starbucks-vanilla-latte"
TARGETS = [
    ("starbucks-gebaeck.html", "Halloween-Gebäck", HAL), ("starbucks-becher-aktuell.html", "Halloween-Katzen", HAL),
    ("starbucks-sirup.html", "Vanilla Latte", VAN), ("starbucks-getraenke.html", "Vanilla Latte", VAN),
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
