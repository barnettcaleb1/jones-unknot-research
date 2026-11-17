"""Parse fetched Knot Atlas Data: pages (treated as untrusted data) into JSON."""
import re, html, json, sys, os
d = sys.argv[1]
out = {}
for fn in sorted(os.listdir(d)):
    m = re.fullmatch(r"(jones|pd)_(.+)\.html", fn)
    if not m:
        continue
    kind, name = m.groups()
    s = open(os.path.join(d, fn), encoding="utf-8", errors="replace").read()
    body = re.search(r'<div class="mw-parser-output">(.*?)</div>', s, re.S)
    txt = html.unescape(re.sub(r"<[^>]+>", "", body.group(1))) if body else ""
    mm = re.search(r"\[math\]\\displaystyle\{(.*?)\}\[/math\]", txt, re.S)
    val = mm.group(1).strip() if mm else txt.strip()
    out.setdefault(name, {})[kind] = val
for name, v in out.items():
    pdtxt = v.get("pd", "")
    # Knot Atlas compact notation: X4251 (single digits) or X5,12,6,13
    xs = []
    for tok in re.findall(r"X[\d,]+", pdtxt):
        body = tok[1:]
        if "," in body:
            xs.append([int(z) for z in body.split(",")])
        else:
            xs.append([int(z) for z in body])
    v["pd_list"] = [x for x in xs if len(x) == 4]
    if any(len(x) != 4 for x in xs):
        v["pd_parse_warning"] = "some X tokens did not have 4 entries: %r" % [x for x in xs if len(x) != 4]
    # normalise jones text: remove spaces, "\ " etc
    j = v.get("jones", "")
    j = j.replace("\\ ", "").replace(" ", "").replace("{", "").replace("}", "")
    # LaTeX fractions used on link pages, e.g. -\frac1\sqrtq-\frac1q^5/2
    j = j.replace("\\frac1\\sqrtq", "q^(-1/2)")
    j = re.sub(r"\\frac1q\^(\d+)/2", r"q^(-\1/2)", j)
    j = re.sub(r"\\frac1q\^(\d+)", r"q^-\1", j)
    j = j.replace("\\sqrtq", "q^(1/2)")
    v["jones_clean"] = j
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[2])), os.path.basename(sys.argv[2])), "w"), indent=1)
for name, v in out.items():
    print(name, "| jones:", v["jones_clean"], "| pd crossings:", len(v["pd_list"]), "| raw pd:", v.get("pd","")[:90])
