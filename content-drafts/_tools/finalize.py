"""finalize.py <draft-folder> — annotated → clean draft.md, schema.jsonld from meta.json + FAQ, QA stats."""
import json, re, sys, pathlib

d = pathlib.Path(sys.argv[1])
meta = json.loads((d / "meta.json").read_text())
ann = (d / "draft.annotated.md").read_text()

clean = re.sub(r"<!--.*?-->", "", ann, flags=re.S)
clean = clean.replace("**Direkt-Antwort:**", "\0DA\0")
clean = clean.replace("**", "").replace("\0DA\0", "**Direkt-Antwort:**")
clean = re.sub(r"\n{3,}", "\n\n", clean).strip() + "\n"
(d / "draft.md").write_text(clean)

lines = clean.split("\n")
heads = [(len(m.group(1)), m.group(2)) for l in lines if (m := re.match(r"^(#{1,6}) (.+)", l))]
# hierarchy check
errs, prev = [], 0
for lvl, h in heads:
    if lvl > prev + 1: errs.append(f"skipped level before: {h}")
    prev = lvl
assert sum(1 for l, _ in heads if l == 1) == 1, "need exactly one H1"

da = re.search(r"\*\*Direkt-Antwort:\*\* (.+)", clean).group(1)
faq_part = clean.split("## Häufig gestellte Fragen", 1)[1]
faqs = re.findall(r"### (.+?)\n\n(.+?)(?=\n### |\Z)", faq_part, flags=re.S)
body_words = len(re.findall(r"\w+", re.sub(r"[|#*\-]", " ", clean)))

url = f"https://starbuckspreise.com{meta['slug']}"
graph = [
    {"@type": "BlogPosting", "@id": url + "#article", "headline": meta["title"],
     "description": meta["description"], "inLanguage": "de-DE",
     "datePublished": meta["date"], "dateModified": meta["date"],
     "mainEntityOfPage": url, "image": f"https://starbuckspreise.com/img/blog/{meta['slug'].split('/')[-1]}-hero.webp",
     "author": {"@type": "Organization", "name": "StarbucksPreise Redaktion", "url": "https://starbuckspreise.com/ueber-uns"},
     "publisher": {"@type": "Organization", "name": "StarbucksPreise", "url": "https://starbuckspreise.com/",
                   "logo": {"@type": "ImageObject", "url": "TODO: https://starbuckspreise.com/<logo-file>"}},
     "about": meta["about"], "mentions": meta["mentions"],
     "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#direct-answer"]}},
    {"@type": "FAQPage", "@id": url + "#faq",
     "mainEntity": [{"@type": "Question", "name": q.strip(),
                     "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\[(.+?)\]\(.+?\)", r"\1", a.strip())}}
                    for q, a in faqs]},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://starbuckspreise.com/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://starbuckspreise.com/blog/"},
        {"@type": "ListItem", "position": 3, "name": meta["crumb"], "item": url}]},
]
if meta.get("howto"):
    graph.append(meta["howto"])
(d / "schema.jsonld").write_text(json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2))

stats = {"words": body_words, "direct_answer_words": len(da.split()), "faq_count": len(faqs),
         "h2": [h for l, h in heads if l == 2], "h3_count": sum(1 for l, _ in heads if l == 3),
         "hierarchy_errors": errs,
         "question_h2_first_sentences": []}
# first sentence after each H2/H3 (QUORA check)
for i, l in enumerate(lines):
    if re.match(r"^#{2,3} ", l) and "Häufig" not in l:
        nxt = next((x for x in lines[i + 1:] if x.strip()), "")
        stats["question_h2_first_sentences"].append((l, nxt[:110]))
print(json.dumps(stats, ensure_ascii=False, indent=1))
