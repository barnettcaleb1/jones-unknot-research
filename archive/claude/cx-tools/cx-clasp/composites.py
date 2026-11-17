#!/usr/bin/env python3
"""
composites.py -- three-component links that the prime Hoste-Thistlethwaite
table omits (connected sums, split links) and the hand candidates of the
task, each built explicitly from a braid word / PD code / tangle sum, with
bracket, determinant, linking numbers and comparison with the twelve forced
double corners C00*(m, eps) (and the extended family) up to +-A^k.

Constructions (all PD codes are emitted into composites.json):
  * T(2,+-4) # Hopf[+-]     : connected_sum_links(closure sigma_1^(+-4), closure sigma_1^(+-2))
                              (spliced along one edge of each; bracket = product, checked)
  * Hopf # Hopf (3-chain)   : closure of the 3-braid sigma_1^2 sigma_2^2 (and sign variants)
  * Hopf # Hopf # unknot    : same link as the 3-chain (sum with the unknot is trivial)
  * Hopf u O, T(2,4) u O    : split unions (PD with an extra kinked unknot component)
  * T(2,4) # T(2,4)         : closure of sigma_1^4 sigma_2^4
  * T(2,4) + unknotted third component linking it: closures of sigma_1^4 * w,
    w a word of length <= 2 in A13^(+-1) = (sigma_2 sigma_1^2 sigma_2^-1)^(+-1),
    A23^(+-1) = sigma_2^(+-2); includes the braid axis sigma_1^4 sigma_2 sigma_1^2 sigma_2
  * pretzel (2,2,2), (2,2,-2), (-2,-2,-2): spherogram RationalTangle(1,p) sums, numerator closure
  * T(3,3)                  : closure of (sigma_1 sigma_2)^3
  * Hopf u axis             : closure of sigma_1^2 sigma_2 sigma_1^2 sigma_2
  * "two fingers through one loop": pure 3-braid closures A12^a A13^c A23^b in every
    order with (|a|,|b|,|c|) a permutation of (1,1,2) or (1,1,1), all signs
  * systematic: every pair of 2-component prime links with <= 10 crossings in total
    and det product 8 (bracket of the sum = product of brackets), with mirrors
Table links L6a4 (Borromean), L6a5, L6n1 are reported from table_scan.json.
Writes composites.json and composites.txt.
"""

import itertools
import json
import os
import warnings

warnings.filterwarnings("ignore")
from common import (pmul, pshift, pscale, DELTA, pstr, pmirror, unit_equiv,  # noqa: E402
                    kauffman_bracket, kauffman_bracket_naive, Diagram, pd_mirror,
                    braid_closure_pd, connected_sum_links, link_record, strip_private,
                    det_from_bracket, normalise_unit, jones_from_bracket, jones_str, WORKDIR)
import snappy  # noqa: E402
from spherogram import Link, RationalTangle  # noqa: E402


def load_targets():
    with open(os.path.join(WORKDIR, "c00star.json")) as fh:
        data = json.load(fh)
    main = [(r["m"], r["eps"], {int(e): c for e, c in r["C00star_dict"].items()}) for r in data["polys"]]
    ext = [(r["m"], r["eps"], {int(e): c for e, c in r["C00star_dict"].items()}) for r in data["family_extended"]]
    return main, ext


def load_table():
    with open(os.path.join(WORKDIR, "table_scan.json")) as fh:
        data = json.load(fh)
    recs = data["records"]
    for r in recs:
        r["_bracket"] = {int(e): c for e, c in r["bracket"].items()}
    return recs


TARGETS, EXT = load_targets()
MAIN_KEYS = {(m, e) for m, e, _ in TARGETS}
TABLE = load_table()


def matches_of(br):
    out = []
    done = set()
    for (m, e, C) in TARGETS + EXT:
        if (m, e) in done:
            continue
        ue = unit_equiv(C, br)
        if ue:
            done.add((m, e))
            out.append({"m": m, "eps": e, "sign": ue[0], "A_power": ue[1], "A_power_mod4": ue[1] % 4,
                        "in_main_twelve": (m, e) in MAIN_KEYS})
    return out


def table_identification(br):
    """Table links whose bracket (or mirror bracket) is unit-equivalent to br."""
    ids = []
    for r in TABLE:
        if unit_equiv(br, r["_bracket"]):
            ids.append(r["name"])
        elif unit_equiv(br, pmirror(r["_bracket"])):
            ids.append(r["name"] + "*")
    return ids


def snappy_identify(pd):
    try:
        L = Link([tuple(int(x) for x in c) for c in pd])
        M = L.exterior()
        return [str(x) for x in M.identify()]
    except Exception as exc:
        return ["identify failed: %s" % type(exc).__name__]


# pure braid generators on 3 strands
A12 = [1, 1]
A12i = [-1, -1]
A23 = [2, 2]
A23i = [-2, -2]
A13 = [2, 1, 1, -2]
A13i = [2, -1, -1, -2]


def power(gen, geni, n):
    return (gen if n > 0 else geni) * abs(n)


def candidate_from_pd(name, construction, pd):
    rec = link_record(name, pd, naive_check=(len(pd) <= 14))
    rec["construction"] = construction
    rec["matches"] = matches_of(rec["_bracket"])
    rec["matches_mirror"] = matches_of(pmirror(rec["_bracket"]))
    rec["bracket_equals_table"] = table_identification(rec["_bracket"])
    rec["snappy_identify"] = snappy_identify(pd)
    return rec


def candidate_from_bracket(name, construction, br, components):
    rec = {"name": name, "construction": construction, "components": components,
           "bracket_str": pstr(br), "det": det_from_bracket(br), "_bracket": br,
           "matches": matches_of(br), "matches_mirror": matches_of(pmirror(br)),
           "bracket_equals_table": table_identification(br)}
    return rec


def fmt(rec):
    s = "%-34s comps=%s det=%s" % (rec["name"], rec.get("components"), rec["det"])
    if "linking" in rec:
        s += " lk=%s w=%+d cr=%d" % (rec["linking"], rec["writhe"], rec["crossings"])
    s += "\n      construction: %s" % rec["construction"]
    s += "\n      <D> = %s" % rec["bracket_str"]
    if "jones_str" in rec:
        s += "\n      V   = %s" % rec["jones_str"]
    if "pd" in rec:
        s += "\n      PD  = %s" % rec["pd"]
    if rec.get("snappy_identify"):
        s += "\n      snappy identify: %s" % rec["snappy_identify"]
    s += "\n      bracket equals table link(s): %s" % (rec["bracket_equals_table"] or "none (not a prime link bracket in the table)")
    s += "\n      MATCHES C00*: %s" % (rec["matches"] or "none")
    if rec["matches_mirror"]:
        s += "\n      mirror MATCHES C00*: %s" % rec["matches_mirror"]
    return s


def main():
    cands = []

    # --- T(2,+-4) # Hopf
    for w4 in ([1] * 4, [-1] * 4):
        for w2 in ([1, 1], [-1, -1]):
            pd = connected_sum_links(braid_closure_pd(w4), braid_closure_pd(w2))
            name = "T(2,%s4) # Hopf[%s]" % ("+" if w4[0] > 0 else "-", "+" if w2[0] > 0 else "-")
            rec = candidate_from_pd(name, "connected_sum_links(closure %s, closure %s)" % (w4, w2), pd)
            prod = pmul(kauffman_bracket(braid_closure_pd(w4)), kauffman_bracket(braid_closure_pd(w2)))
            assert prod == rec["_bracket"]
            cands.append(rec)

    # --- Hopf # Hopf (3-chain) and Hopf # Hopf # unknot
    for w in ([1, 1, 2, 2], [1, 1, -2, -2], [-1, -1, -2, -2]):
        pd = braid_closure_pd(w)
        rec = candidate_from_pd("Hopf # Hopf (3-chain) %s" % w, "closure of 3-braid %s (= Hopf # Hopf # unknot)" % w, pd)
        hb = kauffman_bracket(braid_closure_pd([1, 1]))
        assert rec["_bracket"] == pmul(hb, hb)
        cands.append(rec)

    # --- split unions (extra kinked unknot component)
    hopf_pd = braid_closure_pd([1, 1])
    split_hopf = [list(x) for x in hopf_pd] + [[5, 5, 6, 6]]
    rec = candidate_from_pd("Hopf u O (split)", "Hopf PD plus a disjoint kink [5,5,6,6]", split_hopf)
    assert rec["_bracket"] == pmul(DELTA, pmul(kauffman_bracket(hopf_pd), {-3: -1})) or \
        rec["_bracket"] == pmul(DELTA, pmul(kauffman_bracket(hopf_pd), {3: -1}))
    cands.append(rec)
    t24_pd = braid_closure_pd([1] * 4)
    split_t24 = [list(x) for x in t24_pd] + [[9, 9, 10, 10]]
    cands.append(candidate_from_pd("T(2,4) u O (split)", "T(2,4) PD plus a disjoint kink [9,9,10,10]", split_t24))

    # --- T(2,4) # T(2,4)
    cands.append(candidate_from_pd("T(2,4) # T(2,4)", "closure of sigma_1^4 sigma_2^4", braid_closure_pd([1] * 4 + [2] * 4)))

    # --- T(2,4) with an unknotted third component linking it
    letters = {"A13": A13, "A13^-1": A13i, "A23": A23, "A23^-1": A23i}
    seen = {}
    for length in (1, 2):
        for combo in itertools.product(letters.keys(), repeat=length):
            word = [1] * 4
            for c in combo:
                word += letters[c]
            pd = braid_closure_pd(word)
            D = Diagram(pd)
            if D.num_components() != 3:
                continue
            br = kauffman_bracket(pd)
            key = normalise_unit(br)
            label = "sigma_1^4 " + " ".join(combo)
            if key in seen:
                seen[key]["also"].append(label)
                continue
            rec = candidate_from_pd("T(2,4) + unknot: %s" % label, "closure of 3-braid %s" % word, pd)
            rec["also"] = []
            seen[key] = rec
            cands.append(rec)
    # mirror images of this family are covered by matches_mirror

    # --- pretzels, T(3,3), Hopf u axis
    for p in ((2, 2, 2), (2, 2, -2), (-2, -2, -2)):
        T = RationalTangle(1, p[0]) + RationalTangle(1, p[1]) + RationalTangle(1, p[2])
        L = T.numerator_closure()
        pd = [list(x) for x in L.PD_code()]
        cands.append(candidate_from_pd("pretzel %s" % (p,), "spherogram RationalTangle(1,p) sum, numerator_closure", pd))
    cands.append(candidate_from_pd("T(3,3)", "closure of (sigma_1 sigma_2)^3", braid_closure_pd([1, 2] * 3)))
    cands.append(candidate_from_pd("T(3,3) mirror", "closure of (sigma_1^-1 sigma_2^-1)^3", braid_closure_pd([-1, -2] * 3)))
    cands.append(candidate_from_pd("Hopf u axis", "closure of sigma_1^2 sigma_2 sigma_1^2 sigma_2", braid_closure_pd([1, 1, 2, 1, 1, 2])))
    cands.append(candidate_from_pd("T(2,4) u axis", "closure of sigma_1^4 sigma_2 sigma_1^2 sigma_2 (braid axis of sigma_1^4)", braid_closure_pd([1, 1, 1, 1, 2, 1, 1, 2])))

    # --- fingers: pure 3-braids, |lk| patterns (1,1,2) and (1,1,1)
    finger = {}
    gens = {"A12": (A12, A12i), "A13": (A13, A13i), "A23": (A23, A23i)}
    for pattern in ((1, 1, 2), (1, 1, 1)):
        for exps in set(itertools.permutations(pattern)):
            for signs in itertools.product((1, -1), repeat=3):
                for order in itertools.permutations(("A12", "A13", "A23")):
                    word = []
                    for g, n, s in zip(("A12", "A13", "A23"), exps, signs):
                        pass
                    e = dict(zip(("A12", "A13", "A23"), exps))
                    sg = dict(zip(("A12", "A13", "A23"), signs))
                    for g in order:
                        word += power(gens[g][0], gens[g][1], sg[g] * e[g])
                    pd = braid_closure_pd(word)
                    D = Diagram(pd)
                    assert D.num_components() == 3
                    br = kauffman_bracket(pd)
                    key = normalise_unit(br)
                    mkey = normalise_unit(pmirror(br))
                    if key in finger or mkey in finger:
                        continue
                    rec = candidate_from_pd("fingers |lk|=%s: %s" % (pattern, " ".join("%s^%d" % (g, sg[g] * e[g]) for g in order)),
                                            "closure of pure 3-braid %s" % word, pd)
                    finger[key] = rec
    cands.extend(finger.values())

    # --- systematic composite scan: pairs of 2-component prime links
    two = []
    for k in range(2, 9):
        for M in snappy.HTLinkExteriors(num_cusps=2, crossings=k):
            pd = [list(x) for x in M.link().PD_code()]
            r = link_record(M.name(), pd, naive_check=True)
            two.append(r)
    pair_results = []
    for i, r1 in enumerate(two):
        for r2 in two[i:]:
            if r1["crossings"] + r2["crossings"] > 10:
                continue
            if r1["det"] * r2["det"] != 8:
                continue
            for c1, b1 in (("", r1["_bracket"]), ("*", pmirror(r1["_bracket"]))):
                for c2, b2 in (("", r2["_bracket"]), ("*", pmirror(r2["_bracket"]))):
                    br = pmul(b1, b2)
                    rec = candidate_from_bracket("%s%s # %s%s" % (r1["name"], c1, r2["name"], c2),
                                                 "product of brackets (connected sum along any components)", br, 3)
                    pair_results.append(rec)
    cands.extend(pair_results)

    # --- table links of the original hand list
    table_hand = [r for r in TABLE if r["name"] in ("L6a4", "L6a5", "L6n1")]

    lines = []
    for rec in cands:
        lines.append(fmt(rec))
        if rec.get("also"):
            lines.append("      same bracket also from: %s" % rec["also"])
    lines.append("\n--- table links named in the task (from table_scan.json) ---")
    for r in table_hand:
        lines.append("%-8s det=%d lk=%s <D>=%s V=%s matches=%s" % (r["name"], r["det"], r["linking"], r["bracket_str"], r["jones_str"], r["matches"] or "none"))
    lines.append("\n2-component prime links used for the composite scan: %s" % ["%s(det %d)" % (r["name"], r["det"]) for r in two])
    any_match = [rec["name"] for rec in cands if rec["matches"] or rec["matches_mirror"]]
    lines.append("\nCandidates whose bracket (or mirror) matches some C00*(m, eps): %s" % any_match)
    text = "\n".join(lines) + "\n"
    with open(os.path.join(WORKDIR, "composites.txt"), "w") as fh:
        fh.write(text)
    with open(os.path.join(WORKDIR, "composites.json"), "w") as fh:
        json.dump({"candidates": [strip_private(r) for r in cands],
                   "two_component_links": [strip_private(r) for r in two]}, fh, indent=1)
    print(text)


if __name__ == "__main__":
    main()
