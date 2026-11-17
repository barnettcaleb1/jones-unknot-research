#!/usr/bin/env python3
"""validate.py -- runs every check of the toolkit and writes VALIDATION.md.
Run from the venv:  ./venv/bin/python validate.py [--quick]"""
import os, sys, json, time, random, warnings, platform
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bracket as B
import twist as T
import certify as C
from bracket import (jones_from_pd, jones_str, parse_poly_t, same_up_to_mirror, pclean,
                     kauffman_bracket_naive, Diagram, pmul)

QUICK = "--quick" in sys.argv
try:
    import snappy, spherogram
    HAVE = True
except Exception as ex:
    HAVE = False
    SNAPPY_ERR = repr(ex)

rows = []
timings = []       # (name, crossings, seconds, max_states, max_width)
LOG = []


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


def check(section, name, pd, expected=None, note="", mirror_ok=True, naive=True, exact_only=False):
    """Compute V for pd, compare with expected (half-exponent dict), record."""
    stats = {}
    t0 = time.perf_counter()
    V = jones_from_pd(pd, stats=stats)
    dt = time.perf_counter() - t0
    status = "computed"
    if expected is not None:
        if pclean(V) == pclean(expected):
            status = "PASS exact"
        elif mirror_ok and not exact_only and same_up_to_mirror(V, expected):
            status = "PASS up to t->1/t"
        else:
            status = "FAIL"
    notes = [note] if note else []
    if naive and len(pd) <= 12:
        nb = kauffman_bracket_naive(pd)
        if nb == stats["bracket"]:
            notes.append("naive 2^n state sum agrees")
        else:
            notes.append("NAIVE STATE SUM DISAGREES")
            status = "FAIL (naive)"
    row = dict(section=section, name=name, n=len(pd), expected=jones_str(expected) if expected is not None else "",
               got=jones_str(V), status=status, time=dt, note="; ".join(notes),
               states=stats["max_states"], width=stats["max_width"], components=stats["components"], writhe=stats["writhe"])
    rows.append(row)
    timings.append((name, len(pd), dt, stats["max_states"], stats["max_width"]))
    log("[%s] %-34s n=%-3d %-18s %.3fs  V=%s" % (section, name, len(pd), status, dt, jones_str(V)))
    return V


def pdiv_exact(num, den):
    """exact division of dict-polynomials (integer exponents), den has nonzero lowest term"""
    r = dict(num)
    q = {}
    d0 = min(den)
    while r:
        e = min(r)
        c = r[e] // den[d0]
        assert c * den[d0] == r[e]
        q[e - d0] = c
        for k, v in den.items():
            r[e - d0 + k] = r.get(e - d0 + k, 0) - c * v
            if r[e - d0 + k] == 0:
                del r[e - d0 + k]
    return q


def torus2(n):
    """V of T(2,n), n odd positive, as half-exponent dict:
    t^((n-1)/2) (1 - t^3 - t^(n+1) + t^(n+2)) / (1 - t^2)"""
    q = pdiv_exact({0: 1, 3: -1, n + 1: -1, n + 2: 1}, {0: 1, 2: -1})
    return {2 * (e + (n - 1) // 2): c for e, c in q.items()}


KA = json.load(open(os.path.join(HERE, "katlas_reference.json")))
TASK_REF = {
    "3_1": "t + t^3 - t^4",
    "4_1": "t^-2 - t^-1 + 1 - t + t^2",
    "5_1": "t^2 + t^4 - t^5 + t^6 - t^7",
    "7_4": "t - 2t^2 + 3t^3 - 2t^4 + 3t^5 - 2t^6 + t^7 - t^8",
    "8_19": "t^3 + t^5 - t^8",
    "10_132": "t^-2 + t^-4 - t^-5 + t^-6 - t^-7",
}

log("=== environment: python", platform.python_version(), "snappy", HAVE and snappy.__version__,
    "spherogram", HAVE and spherogram.__version__)

# ---------------------------------------------------------------- 1. unknots
sec = "unknot"
one = {0: 1}
check(sec, "positive kink [[1,1,2,2]]", [[1, 1, 2, 2]], one)
check(sec, "negative kink [[1,2,2,1]]", [[1, 2, 2, 1]], one)
check(sec, "2-crossing clasp unknot", T.clasp_unknot_pd(), one)
check(sec, "braid closure s1 s1 s1^-1 (3 cr.)", T.braid_closure_pd([1, 1, -1]), one)
check(sec, "two kinks, braid s1^-1 s1 s1^-1", T.braid_closure_pd([-1, 1, -1]), one)
check(sec, "plat s2 s1^2 (3 cr., kinks)", T.plat_closure_pd([2, 1, 1], 4), one)
# conjugate of s1 s2 (whose closure is the unknot) by g = s1 s2^-1 s1: closure is the unknot by Markov conjugation
check(sec, "unknot: conjugate g(s1 s2)g^-1, g=s1 s2^-1 s1 (8 cr.)", T.braid_closure_pd([1, -2, 1, 1, 2, -1, 2, -1]), one)

# ---------------------------------------------------------------- 2. Knot Atlas PD codes vs Knot Atlas Jones
sec = "KnotAtlas-PD"
for name in ["3_1", "4_1", "5_1", "5_2", "6_1", "7_2", "7_4", "8_1", "8_19", "10_132", "K11n42"]:
    ref = KA[name]
    exp = parse_poly_t(ref["jones_clean"])
    check(sec, name + " (KA PD, KA Jones)", ref["pd_list"], exp, exact_only=False)

sec = "KnotAtlas-PD-vs-task"
for name, s in TASK_REF.items():
    check(sec, name + " (KA PD, task value)", KA[name]["pd_list"], parse_poly_t(s))

# ---------------------------------------------------------------- 3. links
sec = "links"
hopf_exp = parse_poly_t(KA["L2a1"]["jones_clean"])          # -q^(-1/2)-q^(-5/2)
check(sec, "Hopf link L2a1 (KA PD)", KA["L2a1"]["pd_list"], hopf_exp)
check(sec, "Hopf link braid s1^2", T.braid_closure_pd([1, 1]), hopf_exp)
check(sec, "Hopf link braid s1^-2", T.braid_closure_pd([-1, -1]), hopf_exp)
unlink2 = parse_poly_t("-t^(1/2)-t^(-1/2)")
check(sec, "2-comp unlink braid s1 s1^-1", T.braid_closure_pd([1, -1]), unlink2)
check(sec, "2-comp unlink braid s1^-1 s1 s1^-1 s1", T.braid_closure_pd([-1, 1, -1, 1]), unlink2)
check(sec, "3-comp unlink braid s1 s1^-1 s2 s2^-1", T.braid_closure_pd([1, -1, 2, -2]), pmul(unlink2, unlink2))

# ---------------------------------------------------------------- 4. spherogram PD codes
if HAVE:
    sec = "spherogram-PD"
    sph = {}
    for name in ["3_1", "4_1", "5_1", "5_2", "6_1", "7_4", "8_19", "10_132", "K11n42", "L2a1"]:
        L = snappy.Link(name)
        pd = [list(x) for x in L.PD_code()]
        sph[name] = pd
        exp = parse_poly_t(KA[name]["jones_clean"])
        V = check(sec, name + " (spherogram PD, KA Jones)", pd, exp)
        D = Diagram(pd)
        w_me, w_sp = D.writhe(), L.writhe()
        rows[-1]["note"] += "; writhe mine=%d spherogram=%d %s" % (w_me, w_sp, "ok" if w_me == w_sp else "MISMATCH")
        if w_me != w_sp:
            rows[-1]["status"] = "FAIL (writhe)"

# ---------------------------------------------------------------- 5. twist.py validation
sec = "twist.py"
tref = parse_poly_t(TASK_REF["3_1"])
fig8 = parse_poly_t(TASK_REF["4_1"])
check(sec, "(a) braid closure s1^3 = 3_1", T.braid_closure_pd([1, 1, 1]), tref)
check(sec, "(a) braid closure (s1 s2^-1)^2 = 4_1", T.braid_closure_pd([1, -2, 1, -2]), fig8)
check(sec, "(a) braid closure s1^-3 = mirror 3_1", T.braid_closure_pd([-1, -1, -1]), parse_poly_t(KA["3_1"]["jones_clean"]))
check(sec, "(b) plat s2^3 (4 strands) = 3_1", T.plat_closure_pd([2, 2, 2], 4), tref)
twistknots = {1: "3_1", 2: "4_1", 3: "5_2", 4: "6_1", 5: "7_2"}
for n, nm in twistknots.items():
    check(sec, "(b) plat s2^%d s1^-1 s2 = %s" % (n, nm), T.plat_closure_pd([2] * n + [-1, 2], 4),
          parse_poly_t(KA[nm]["jones_clean"]))
clasp = T.clasp_unknot_pd()
D = Diagram(clasp)
faces = [[e for e, _, _ in f] for f in D.faces()]
log("clasp unknot faces:", faces, " writhe", D.writhe())
for n, nm in {-1: "3_1", -2: "5_2", -3: "7_2", 1: "4_1", 2: "6_1", 3: "8_1"}.items():
    pd = T.insert_full_twists(clasp, 2, 4, n)
    check(sec, "(c) clasp unknot + %+d full twists on edges 2,4 = %s" % (n, nm), pd, parse_poly_t(KA[nm]["jones_clean"]))
    if HAVE:
        try:
            L = spherogram.Link(pd)
            idn = [str(m) for m in L.exterior().identify()]
            h = L.knot_floer_homology()
            rows[-1]["note"] += "; snappy identify=%s HFK rank=%d genus=%d" % (idn, h["total_rank"], h["seifert_genus"])
        except Exception as ex:
            rows[-1]["note"] += "; snappy check error %r" % (ex,)
# twist insertion on a non-trivial knot: twisting a crossing of the trefoil (edges around a face)
# check Reidemeister-II like consistency: n twists then -n twists at the same site must give the same V
# In the braid closure of s1^3 (PD [[3,1,4,6],[1,5,2,4],[5,3,6,2]]) edges 1 and 4 are the two braid
# strands between crossings 0 and 1 (they bound a bigon).  n full twists there give s1^(3+2n):
pd0 = T.braid_closure_pd([1, 1, 1])
assert (1, 4, 0) in T.parallel_edge_pairs(pd0) or any(s[:2] in ((1, 4), (4, 1)) for s in T.parallel_edge_pairs(pd0))
check(sec, "(c) 3_1 + 2 full twists on braid strands = T(2,7)", T.insert_full_twists(pd0, 1, 4, 2), torus2(7))
check(sec, "(c) 3_1 - 2 full twists on braid strands = s1^-1 = unknot", T.insert_full_twists(pd0, 1, 4, -2), one)
check(sec, "(c) 3_1 - 3 full twists on braid strands = s1^-3 = mirror 3_1", T.insert_full_twists(pd0, 1, 4, -3),
      parse_poly_t(KA["3_1"]["jones_clean"]))
check(sec, "(c) 3_1 + 4 full twists on braid strands = T(2,11)", T.insert_full_twists(pd0, 1, 4, 4), torus2(11))

# ---------------------------------------------------------------- 6. big examples / speed
sec = "speed"
t21 = torus2(21)
check(sec, "T(2,21) braid closure s1^21", T.braid_closure_pd([1] * 21), t21, naive=False)
if HAVE:
    check(sec, "T(2,21) spherogram PD", [list(x) for x in snappy.Link("T(2,21)").PD_code()], t21, naive=False)
k31 = T.braid_closure_pd([1, 1, 1])
k41 = T.braid_closure_pd([1, -2, 1, -2])
check(sec, "3_1 # 4_1 (connected_sum_pd)", T.connected_sum_pd(k31, k41), pmul(tref, fig8))
tt = T.braid_closure_pd([1] * 21)
cs = T.connected_sum_pd(T.connected_sum_pd(tt, tt), tt)
check(sec, "T(2,21)#T(2,21)#T(2,21) (63 cr.)", cs, pmul(pmul(t21, t21), t21), naive=False)
cs5 = T.connected_sum_pd(T.connected_sum_pd(cs, tt), tt)
check(sec, "T(2,21)^#5 (105 cr.)", cs5, pmul(pmul(pmul(pmul(t21, t21), t21), t21), t21), naive=False)
big_braid = T.braid_closure_pd([1, -2, 3, -4] * 12)   # 48 crossings, 5 strands
check(sec, "braid (s1 s2^-1 s3 s4^-1)^12 (48 cr.)", big_braid, None, naive=False)

# ---------------------------------------------------------------- 7. random knots: internal consistency + Seifert det
if HAVE:
    sec = "random"
    random.seed(20261103)
    budget = time.perf_counter()
    sizes = [8, 10, 12, 12, 20, 30, 40, 50, 60, 70, 80] if not QUICK else [8, 10, 12, 20, 30]
    for want in sizes:
        if time.perf_counter() - budget > 420:
            log("time budget exhausted; skipping remaining random sizes")
            break
        try:
            L = spherogram.random_link(want, num_components=1, initial_map_gives_link=True)
        except Exception as ex:
            log("random_link failed:", ex)
            continue
        pd = [list(x) for x in L.PD_code()]
        n = len(pd)
        name = "random knot (asked %d, got %d cr.)" % (want, n)
        V = check(sec, name, pd, None, naive=(n <= 12))
        r = rows[-1]
        D = Diagram(pd)
        ok = True
        v1 = sum(V.values())
        co, _ = C.jones_at_i(V)
        detV = C.jones_at_minus_one(V)
        try:
            S = [[int(x) for x in row] for row in L.seifert_matrix()]
            Ssym = [[S[i][j] + S[j][i] for j in range(len(S))] for i in range(len(S))]
            detS = abs(C._bareiss_det(Ssym))
        except Exception as ex:
            detS = "err %r" % (ex,)
        w_ok = (D.writhe() == L.writhe())
        notes = ["V(1)=%d" % v1, "V(i)=%s" % (co,), "|V(-1)|=%s" % detV, "Seifert det=%s" % detS,
                 "writhe %s" % ("ok" if w_ok else "MISMATCH")]
        ok = (v1 == 1) and (co in ([1, 0, 0, 0], [-1, 0, 0, 0])) and (detV == detS) and w_ok
        r["note"] = (r["note"] + "; " if r["note"] else "") + ", ".join(notes)
        r["status"] = ("PASS consistency" if ok else "FAIL consistency") + ("" if r["status"] == "computed" else " / " + r["status"])
        log("    ->", r["status"], r["note"])

# ---------------------------------------------------------------- 8. certify() end-to-end
sec = "certify"
cert_results = {}
for name, pd in [("unknot kink", [[1, 1, 2, 2]]),
                 ("unknot conjugate g(s1 s2)g^-1 (8 cr.)", T.braid_closure_pd([1, -2, 1, 1, 2, -1, 2, -1])),
                 ("3_1 (braid s1^3)", T.braid_closure_pd([1, 1, 1])),
                 ("K11n42 (KA PD)", KA["K11n42"]["pd_list"]),
                 ("7_2 from twisting clasp unknot", T.insert_full_twists(T.clasp_unknot_pd(), 2, 4, -3)),
                 ("Hopf link", KA["L2a1"]["pd_list"])]:
    t0 = time.perf_counter()
    res = C.certify(pd)
    dt = time.perf_counter() - t0
    cert_results[name] = res
    summary = {k: res.get(k) for k in ["V_str", "V_is_one", "det", "det_seifert", "arf", "alexander_str", "signature",
                                       "hfk_nontrivial", "alexander_consistent", "volume", "identify", "group_is_Z", "verdict"]}
    if "hfk" in res:
        summary["hfk_total_rank"] = res["hfk"]["total_rank"]
        summary["hfk_genus"] = res["hfk"]["seifert_genus"]
    log("[certify] %-36s %.2fs %s" % (name, dt, json.dumps(C._json_safe(summary))))
    rows.append(dict(section=sec, name=name, n=len(pd), expected="", got=res["V_str"], status="see note",
                     time=dt, note=json.dumps(C._json_safe(summary)), states="", width="", components=res["components"], writhe=res["writhe"]))

# ---------------------------------------------------------------- write VALIDATION.md
def md_escape(s):
    return str(s).replace("|", "\\|")

out = []
out.append("# VALIDATION.md -- cx-tools validation record\n")
out.append("Generated by `validate.py` on %s.  Python %s; snappy %s, spherogram %s, knot_floer_homology (HFK calculator) %s.\n" % (
    time.strftime("%Y-%m-%d %H:%M"), platform.python_version(),
    HAVE and snappy.__version__, HAVE and spherogram.__version__, HAVE and "available"))
out.append("Conventions: V(t) = (-A^3)^(-w) <D>, t = A^-4; PD = [a,b,c,d] counterclockwise from the incoming under-edge; "
           "A-smoothing joins (a,b),(c,d).  'PASS exact' = identical to the reference; 'PASS up to t->1/t' = equal to the "
           "mirror image's value (the reference source's chirality convention differs from the diagram's).  "
           "Reference values come from the task statement (`task value`) and from Knot Atlas Data pages fetched with curl "
           "into `katlas/` and parsed by `parse_katlas.py` into `katlas_reference.json` (treated as data).  "
           "spherogram's own `jones_polynomial()` needs Sage and was NOT available as a cross-check.\n")
n_pass = sum(1 for r in rows if r["status"].startswith("PASS"))
n_fail = sum(1 for r in rows if r["status"].startswith("FAIL"))
n_other = len(rows) - n_pass - n_fail
out.append("**Summary: %d PASS, %d FAIL, %d informational rows.**\n" % (n_pass, n_fail, n_other))
for sec_name in dict.fromkeys(r["section"] for r in rows):
    out.append("\n## %s\n" % sec_name)
    out.append("| name | crossings | comps | writhe | expected | computed V | status | time (s) | max states / width | notes |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        if r["section"] != sec_name:
            continue
        out.append("| %s | %d | %s | %s | %s | %s | %s | %.3f | %s / %s | %s |" % (
            md_escape(r["name"]), r["n"], r["components"], r["writhe"], md_escape(r["expected"]), md_escape(r["got"]),
            r["status"], r["time"], r["states"], r["width"], md_escape(r["note"])))
out.append("\n## Timing summary (Jones polynomial via bracket.py, this machine)\n")
out.append("| diagram | crossings | seconds | max states | max boundary width |")
out.append("|---|---|---|---|---|")
for name, n, dt, st, w in sorted(timings, key=lambda x: x[1]):
    out.append("| %s | %d | %.3f | %s | %s |" % (md_escape(name), n, dt, st, w))
under = [t for t in timings if t[2] < 60]
if under:
    bestn = max(under, key=lambda x: x[1])
    out.append("\nLargest crossing number computed in under one minute: **%d** (%s, %.1f s)." % (bestn[1], bestn[0], bestn[2]))
rnd = [t for t in timings if t[0].startswith("random") and t[2] < 60]
if rnd:
    b = max(rnd, key=lambda x: x[1])
    out.append("Largest RANDOM knot diagram (spherogram random_link) under one minute: **%d crossings** (%.1f s, max states %s, width %s)." % (b[1], b[2], b[3], b[4]))
tj = os.path.join(HERE, "timing.json")
if os.path.exists(tj):
    tr = [r for r in json.load(open(tj)) if r.get("status") == "ok" and r.get("seconds", 1e9) < 60]
    if tr:
        b = max(tr, key=lambda r: r["n"])
        out.append("\nLarge-diagram runs (speed_driver.py, see TIMING.md): largest finished in under 60 s: **%d crossings** (%s, %.1f s, width %s, %s states)." % (
            b["n"], b["name"], b["seconds"], b["greedy_width"], b["max_states"]))
out.append("\n## Log\n```\n" + "\n".join(LOG) + "\n```\n")
open(os.path.join(HERE, "VALIDATION.md"), "w").write("\n".join(out))
json.dump(C._json_safe(cert_results), open(os.path.join(HERE, "certify_examples.json"), "w"), indent=1)
log("wrote VALIDATION.md: %d PASS, %d FAIL, %d other" % (n_pass, n_fail, n_other))
