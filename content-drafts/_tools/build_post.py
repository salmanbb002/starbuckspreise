"""build_post.py <draft-folder> <post.json> — render draft.md into blog/<slug>.html using the site's blog template.

post.json: {"category","keywords","date_de","published","hero_alt","credit_html","card_text"}
Template head/header/footer are copied from blog/starbucks-tee.html so every post stays in sync.
"""
import html, json, math, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
d = pathlib.Path(sys.argv[1]).resolve()
post = json.loads(pathlib.Path(sys.argv[2]).read_text())
meta = json.loads((d / "meta.json").read_text())
md = (d / "draft.md").read_text()
schema = json.loads((d / "schema.jsonld").read_text())
slug = meta["slug"].rsplit("/", 1)[-1]
url = f"https://starbuckspreise.com/blog/{slug}"
tpl = (ROOT / "blog/starbucks-tee.html").read_text()
head_top = tpl[:tpl.index("<title>")]
site_header = tpl[tpl.index('<body class="blog-page">'):tpl.index('<main class="blog-shell"')]
footer = tpl[tpl.index('<footer class="site-footer">'):]


def anchor(text):
    t = re.sub(r"^\d+\.\s*", "", text.lower())
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss"), ("&", "amp")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:40].strip("-")


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\[(.+?)\]\((.+?)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)


def lead_bold(item, ordered):
    # re-bold the list label the clean draft lost ("Label: text" / "Step. text")
    m = re.match(r"^([^:.]{2,45}[:.])\s", item) if ordered else re.match(r"^([^:]{2,45}:)\s", item)
    return f"<strong>{inline(m.group(1))}</strong>{inline(item[len(m.group(1)):])}" if m else inline(item)


lines = md.split("\n")
h1 = lines[0][2:].strip()
direct = re.search(r"\*\*Direkt-Antwort:\*\* (.+)", md).group(1)
body_md = md.split("\n", 1)[1]
body_md = body_md[body_md.index("\n", body_md.index("Direkt-Antwort")):]
main_md, faq_md = body_md.split("## Häufig gestellte Fragen", 1)

out, toc = [], []
blocks = re.split(r"\n(?=## )", main_md.strip())
intro = blocks.pop(0) if not blocks[0].startswith("## ") else ""


def render(chunk, region_id):
    res, buf, i = [], [], 0
    rows = chunk.strip().split("\n")
    while i < len(rows):
        r = rows[i]
        if not r.strip():
            i += 1; continue
        if r.startswith("### "):
            res.append(f'<h3 id="{anchor(r[4:])}">{inline(r[4:])}</h3>'); i += 1; continue
        if r.startswith("!["):  # ![alt](/img/blog/file.webp "caption")
            alt, src, cap = re.match(r'!\[(.*?)\]\((\S+?)(?:\s+"(.*)")?\)', r).groups()
            try:
                from PIL import Image
                dims = ' width="%d" height="%d"' % Image.open(ROOT / src.lstrip("/")).size
            except Exception:
                dims = ""
            res.append(f'<figure class="inline-img"><img src="{src}" alt="{html.escape(alt)}"{dims} loading="lazy" decoding="async">'
                       + (f"<figcaption>{inline(cap)}</figcaption>" if cap else "") + "</figure>"); i += 1; continue
        if r.startswith("|"):
            tb = []
            while i < len(rows) and rows[i].startswith("|"):
                tb.append([c.strip() for c in rows[i].strip("|").split("|")]); i += 1
            head, body = tb[0], tb[2:]
            res.append(f'<div class="table-wrap" tabindex="0" role="region" aria-labelledby="{region_id}">\n<table>\n<thead>\n<tr>\n'
                       + "".join(f"<th>{inline(c)}</th>\n" for c in head) + "</tr>\n</thead>\n<tbody>\n"
                       + "".join("<tr>\n" + "".join(f"<td>{inline(c)}</td>\n" for c in row) + "</tr>\n" for row in body)
                       + "</tbody>\n</table>\n</div>")
            continue
        if re.match(r"^(- |\d+\. )", r):
            ordered = bool(re.match(r"^\d+\. ", r)); items = []
            while i < len(rows) and re.match(r"^(- |\d+\. )", rows[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", rows[i])); i += 1
            tag = "ol" if ordered else "ul"
            res.append(f"<{tag}>\n" + "".join(f"<li>{lead_bold(x, ordered)}</li>\n" for x in items) + f"</{tag}>")
            continue
        para = []
        while i < len(rows) and rows[i].strip() and not re.match(r"^(### |\||- |\d+\. |!\[)", rows[i]):
            para.append(rows[i]); i += 1
        res.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(res)


sections = []
for b in blocks:
    title, rest = b.split("\n", 1)
    title = title[3:].strip(); aid = anchor(title)
    toc.append(f'              <li><a href="#{aid}">{inline(title)}</a></li>')
    sections.append(f'        <section class="article-section" aria-labelledby="{aid}">\n          <h2 id="{aid}">{inline(title)}</h2>\n{render(rest, aid)}\n        </section>')
toc.append('              <li><a href="#faq">Häufig gestellte Fragen (FAQ)</a></li>')

faqs = re.findall(r"### (.+?)\n\n(.+?)(?=\n### |\Z)", faq_md, flags=re.S)
faq_html = "\n".join(f'            <details>\n              <summary><h3>{inline(q.strip())}</h3></summary>\n              <p>{inline(" ".join(a.split()))}</p>\n            </details>' for q, a in faqs)

words = len(re.findall(r"\w+", md))
mins = max(3, math.ceil(words / 230))

# schema: reuse the draft's graph, normalised to the site's conventions
graph = schema["@graph"]
art = graph[0]
art["@type"] = "Article"; art["@id"] = url + "/#article"
art["author"] = {"@type": "Organization", "name": "StarbucksPreise Redaktion", "url": "https://starbuckspreise.com"}
art["publisher"] = {"@type": "Organization", "name": "StarbucksPreise Deutschland", "url": "https://starbuckspreise.com"}
art["datePublished"] = art["dateModified"] = post["published"]
art["image"] = f"https://starbuckspreise.com/img/blog/{slug}-hero.webp"
art["headline"] = h1
graph[1]["@id"] = url + "/#faq"
graph[2]["@id"] = url + "/#breadcrumb"
graph[2]["itemListElement"][0]["item"] = "https://starbuckspreise.com"
graph[2]["itemListElement"][1]["item"] = "https://starbuckspreise.com/blog"
ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)

t, desc = html.escape(meta["title"]), html.escape(meta["description"])
page = f"""{head_top}<title>{t} · StarbucksPreise</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{html.escape(post['keywords'])}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="StarbucksPreise">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://starbuckspreise.com/img/blog/{slug}-hero.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://starbuckspreise.com/img/blog/{slug}-hero.webp">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Plus+Jakarta+Sans:wght@600;700&family=Sofia+Sans:wght@600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="stylesheet" href="/blog.css?v=20260928">
<script src="/blog.js?v=20260919" defer></script>

<script type="application/ld+json">
{ld}
</script>
</head>
{site_header}<main class="blog-shell" id="main-content" tabindex="-1">
  <article class="blog-article" aria-labelledby="article-title">
    <div class="breadcrumb"><a href="/">Startseite</a> / <a href="/blog">Ratgeber</a> / <span>{html.escape(meta['crumb'])}</span></div>
    <header class="article-header">
      <div class="article-heading">
        <span class="category-tag">{post['category']}</span>
        <h1 id="article-title">{inline(h1)}</h1>
        <div class="article-meta"><span>{post['date_de']}</span> • <span>{mins} Min. Lesezeit</span> • <span>StarbucksPreise Redaktion</span></div>
      </div>
      <div class="featured-img">
        <img src="/img/blog/{slug}-hero.webp" alt="{html.escape(post['hero_alt'])}" loading="eager" fetchpriority="high" decoding="async" width="1600" height="1000">{post['credit_html']}
      </div>
    </header>

    <div class="article-layout">
      <aside class="article-sidebar">
        <details class="article-toc" open="">
          <summary>Inhaltsverzeichnis</summary>
          <nav aria-label="Inhaltsverzeichnis">
            <ol>
{chr(10).join(toc)}
            </ol>
          </nav>
        </details>
      </aside>

      <div class="article-content">

        <blockquote>
          <p id="direct-answer"><strong>Direkt-Antwort:</strong> {inline(direct)}</p>
        </blockquote>

{render(intro, 'article-title')}

{chr(10).join(sections)}

        <section class="article-section" aria-labelledby="faq">
          <h2 id="faq">Häufig gestellte Fragen (FAQ)</h2>
          <div class="faq">
{faq_html}
          </div>
        </section>

      </div>
    </div>
  </article>
</main>

{footer}"""
(ROOT / "blog" / f"{slug}.html").write_text(page)
print(slug, words, "words", mins, "min", len(faqs), "faqs")
