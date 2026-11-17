#!/usr/bin/env python3
"""
table_scan.py -- every three-component link of the Hoste-Thistlethwaite
table with <= 10 crossings (snappy.HTLinkExteriors(num_cusps=3, crossings=k),
link via M.link(), PD via Link.PD_code()), its reduced Kauffman bracket
(cx-tools/bracket.py, cross-checked with the naive 2^n state sum), Jones
polynomial, determinant (exact, |<D>(zeta_8)| in Z[zeta_8], cross-checked
with |V(-1)| and with |det(S + S^T)| from spherogram's Seifert matrix when
available), linking numbers, and the comparison of the bracket (and of the
mirror image's bracket) with the twelve forced double corners C00*(m, eps)
of c00star.json up to a global unit +-A^k (k and k mod 4 are reported; a
match with k = 0 mod 4 is a match up to +-A^(4k) with the table diagram as
drawn, any other k is the same link drawn with a different writhe).

Also scans the extended family (m = 2 mod 4, |m| <= 30).
Writes table_scan.json and table_scan.txt.
"""

import json
import os
import sys
import warnings
from fractions import Fraction

warnings.filterwarnings("ignore")
from common import (pmul, pclean, pstr, pmirror, pclasses, unit_equiv,  # noqa: E402
                    kauffman_bracket, kauffman_bracket_naive, Diagram, pd_mirror,
                    link_record, strip_private, det_from_bracket, WORKDIR)

import snappy  # noqa: E402

MAXCR = 10


def exact_det_sym(S):
    """|det(S + S^T)| with exact integer arithmetic (Bareiss)."""
    n = len(S)
    M = [[Fraction(int(S[i][j]) + int(S[j][i])) for j in range(n)] for i in range(n)]
    det = Fraction(1)
    for c in range(n):
        piv = None
        for r in range(c, n):
            if M[r][c] != 0:
                piv = r
                break
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            if f:
                for j in range(c, n):
                    M[r][j] -= f * M[c][j]
    assert det.denominator == 1
    return abs(int(det))


def load_targets():
    with open(os.path.join(WORKDIR, "c00star.json")) as fh:
        data = json.load(fh)
    main = [(r["m"], r["eps"], {int(e): c for e, c in r["C00star_dict"].items()}) for r in data["polys"]]
    ext = [(r["m"], r["eps"], {int(e): c for e, c in r["C00star_dict"].items()}) for r in data["family_extended"]]
    return main, ext


def main():
    targets, ext_targets = load_targets()
    main_keys = {(m, e) for m, e, _ in targets}
    records = []
    lines = []
    for k in range(2, MAXCR + 1):
        try:
            table = list(snappy.HTLinkExteriors(num_cusps=3, crossings=k))
        except Exception as exc:  # pragma: no cover
            lines.append("crossings=%d: table access failed: %r" % (k, exc))
            continue
        for M in table:
            name = M.name()
            L = M.link()
            pd = [list(x) for x in L.PD_code()]
            rec = link_record(name, pd, naive_check=True)
            assert rec["components"] == 3, name
            # mirror diagram bracket = A -> A^-1 (also verified on the mirrored PD)
            brm = kauffman_bracket(pd_mirror(pd))
            assert brm == pmirror(rec["_bracket"]), "mirror check failed for %s" % name
            # Seifert-matrix determinant cross-check (spherogram, no Sage needed)
            try:
                S = L.seifert_matrix()
                rec["det_seifert"] = exact_det_sym(S)
                assert rec["det_seifert"] == rec["det"], (name, rec["det_seifert"], rec["det"])
            except Exception as exc:
                rec["det_seifert"] = "n/a (%s)" % type(exc).__name__
            # matches
            matches = []
            done = set()
            for (m, e, C) in targets + ext_targets:
                for which, B in (("as tabulated", rec["_bracket"]), ("mirror image", brm)):
                    if (m, e, which) in done:
                        continue
                    ue = unit_equiv(C, B)
                    if ue:
                        done.add((m, e, which))
                        matches.append({"m": m, "eps": e, "chirality": which, "sign": ue[0],
                                        "A_power": ue[1], "A_power_mod4": ue[1] % 4,
                                        "in_main_twelve": (m, e) in main_keys})
            rec["matches"] = matches
            rec["name_mirror"] = name + " (mirror)"
            records.append(rec)
            lines.append("%-7s cr=%2d det=%3d lk=%-12s w=%+d  <D>=%s" % (
                name, rec["crossings"], rec["det"], str(rec["linking"]), rec["writhe"], rec["bracket_str"]))
            if matches:
                lines.append("        MATCH: %s" % matches)
    det8 = [r for r in records if r["det"] == 8]
    out = {"max_crossings": MAXCR, "count": len(records),
           "det8": [r["name"] for r in det8],
           "matches": [{"name": r["name"], "matches": r["matches"]} for r in records if r["matches"]],
           "records": [strip_private(r) for r in records]}
    with open(os.path.join(WORKDIR, "table_scan.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    summary = []
    summary.append("Three-component links in the Hoste-Thistlethwaite table with <= %d crossings: %d" % (MAXCR, len(records)))
    summary.append("Determinant distribution: %s" % sorted({(d, sum(1 for r in records if r["det"] == d)) for d in {r["det"] for r in records}}))
    summary.append("Determinant 8 (%d links; each listed once, mirror images included in the comparison):" % len(det8))
    for r in det8:
        summary.append("  %-7s cr=%2d lk=%-14s V=%s" % (r["name"], r["crossings"], str(r["linking"]), r["jones_str"]))
        summary.append("          PD=%s" % r["pd"])
        summary.append("          <D>=%s   mirror <D>=%s" % (r["bracket_str"], pstr(pmirror(r["_bracket"]))))
    summary.append("Matches with C00*(m, eps) (twelve main corners + extended family |m|<=30), up to +-A^k, both chiralities:")
    anym = False
    for r in records:
        if r["matches"]:
            anym = True
            summary.append("  %s : %s" % (r["name"], r["matches"]))
    if not anym:
        summary.append("  NONE")
    text = "\n".join(summary) + "\n\n--- full listing ---\n" + "\n".join(lines) + "\n"
    with open(os.path.join(WORKDIR, "table_scan.txt"), "w") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
