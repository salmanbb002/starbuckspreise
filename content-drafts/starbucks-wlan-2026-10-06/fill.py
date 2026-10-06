"""fill.py <stores.json> — fill draft.template.md with store-locator counts → draft.annotated.md + CSV."""
import json, collections, csv, re, sys, pathlib
d = pathlib.Path(__file__).parent
st = json.load(open(sys.argv[1]))
de = [v for v in st.values() if v["address"]["countryCode"] == "DE"]
NORM = {"Muenchen": "München", "Munich": "München", "Koeln": "Köln", "Cologne": "Köln", "Duesseldorf": "Düsseldorf",
        "Dusseldorf": "Düsseldorf", "Nuernberg": "Nürnberg", "Frankfurt": "Frankfurt am Main"}
city = lambda v: NORM.get(v["address"]["city"], v["address"]["city"])
has = lambda v: any(f["code"] == "WF" for f in (v.get("features") or []))
def kind(n):
    n = n.lower()
    if re.search(r"bahnhof(?!str|spl)|hbf|\bhb\b|main station", n): return "Bahnhof"
    if re.search(r"flughafen|airport|terminal|^fra |^muc|bbi", n): return "Flughafen"
    if re.search(r"autohof|\(a\d|\ba\d{1,2}\b", n): return "Autobahn und Autohof"
    return "Einkaufszentrum und Sonstige"
wf = [v for v in de if has(v)]; no = [v for v in de if not has(v)]
c = collections.Counter(map(city, de)); w = collections.Counter(map(city, wf))
with open(d / "store-locator-wlan-2026-10-06.csv", "w", newline="") as f:
    wr = csv.writer(f); wr.writerow(["name", "city", "postal", "features", "wlan_listed", "type"])
    for v in sorted(de, key=lambda v: (city(v), v["name"])):
        wr.writerow([v["name"], city(v), v["address"]["postalCode"], "/".join(x["code"] for x in (v.get("features") or [])), int(has(v)), kind(v["name"])])
DISPLAY = json.load(open(d / "display-names.json")) if (d / "display-names.json").exists() else {}
bk = collections.defaultdict(list)
for v in no: bk[kind(v["name"])].append(DISPLAY.get(v["name"], v["name"]))
for city_hbf in ("Berlin Hauptbahnhof", "Koeln Hauptbahnhof", "Duesseldorf Hauptbahnhof", "Hannover Hauptbahnhof", "Leipzig Hauptbahnhof", "Nuernberg Hauptbahnhof"):
    assert any(v["name"].startswith(city_hbf) for v in wf), city_hbf
tok = {"DE": len(de), "WF": len(wf), "NO": len(no), "PCT": round(100 * len(wf) / len(de)),
       "NOFEAT": sum(1 for v in no if not v.get("features")),
       "NO_BAHN": len(bk["Bahnhof"]), "NO_AUTO": len(bk["Autobahn und Autohof"]), "NO_FLUG": len(bk["Flughafen"]),
       "CITYTABLE": "\n".join(f"| {k} | {n} | {w[k]} |" for k, n in c.most_common(8)),
       "NOTABLE": "\n".join(f"| {k} | {len(v)} | {', '.join(sorted(v)[:4])} |" for k, v in sorted(bk.items(), key=lambda x: -len(x[1])))}
t = (d / "draft.template.md").read_text()
for k, v in tok.items(): t = t.replace("{{%s}}" % k, str(v))
assert "{{" not in t
(d / "draft.annotated.md").write_text(t)
print({k: v for k, v in tok.items() if k not in ("CITYTABLE", "NOTABLE")}); print(tok["CITYTABLE"]); print(tok["NOTABLE"])
for v in sorted(no, key=lambda v: v["name"]): print("  NO:", v["name"], "|", city(v), "|", kind(v["name"]))
