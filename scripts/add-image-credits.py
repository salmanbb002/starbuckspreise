#!/usr/bin/env python3
"""Render hero-image credits from img/blog/ATTRIBUTION.md onto article pages. Idempotent."""
import html, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LICENSES = {  # ledger text -> creativecommons.org path
    'CC BY-SA 4.0': 'by-sa/4.0', 'CC BY-SA 3.0 DE': 'by-sa/3.0/de', 'CC BY-SA 3.0': 'by-sa/3.0',
    'CC BY-SA 2.5': 'by-sa/2.5', 'CC BY-SA 2.0 DE': 'by-sa/2.0/de', 'CC BY-SA 2.0': 'by-sa/2.0', 'CC BY 2.0': 'by/2.0',
}

def ledger():
    out = {}
    for block in re.split(r'^## ', (ROOT / 'img/blog/ATTRIBUTION.md').read_text(), flags=re.M)[1:]:
        name = block.split()[0]
        src = re.search(r'- Source: (\S+)', block)
        author = re.search(r'- Author: (.+)', block)
        lic = re.search(r'- License: (CC BY[^—\n]*?)\s*(?:—|$)', block, re.M)
        if src and author and lic and lic.group(1).strip() in LICENSES:
            a = re.sub(r',? via Wikimedia Commons|,? Wikimedia Commons$', '', author.group(1).strip())
            out[name] = (src.group(1), a, lic.group(1).strip())
    return out

def credit(src, author, lic):
    return (f'<p class="img-credit">Foto: {html.escape(author)}, '
            f'<a href="https://creativecommons.org/licenses/{LICENSES[lic]}/deed.de" rel="noopener">{lic}</a>, '
            f'via <a href="{html.escape(src)}" rel="noopener">Wikimedia Commons</a></p>')

def main():
    credits, changed = ledger(), []
    for page in sorted((ROOT / 'blog').glob('*.html')):
        t = page.read_text()
        t2 = re.sub(r'<p class="img-credit">.*?</p>', '', t)  # re-render from ledger
        def add(m):
            name = m.group(2)
            return m.group(1) + credit(*credits[name]) if name in credits else m.group(1)
        t2 = re.sub(r'(<div class="featured-img">\s*<img [^>]*src="/img/blog/([\w.-]+)"[^>]*>)', add, t2)
        if t2 != t:
            page.write_text(t2); changed.append(page.name)
    print(f'{len(credits)} creditable images, {len(changed)} pages updated')

if __name__ == '__main__':
    main()
