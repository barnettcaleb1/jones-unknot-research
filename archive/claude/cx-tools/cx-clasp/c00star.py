#!/usr/bin/env python3
"""
c00star.py -- the forced double corner of the two-slot shell.

Designer's equations:  C01 = C10 =: r,   C00 = delta (delta^2-3)^2 r - F C11,
delta = -A^2 - A^-2,  F = (delta^2-2)(delta^2-4).
Specification: C11 = u = 1 (monomial, unknot), C01 = C10 = r = Hopf-link
raw bracket.  Exponent-class rule for the four corners of ONE diagram
(turning a site back changes the circle count of every state by one):
every exponent of r/u is 2 mod 4 and every exponent of C00/u is 0 mod 4.
The bare Hopf bracket -A^4 - A^-4 has exponents 0 mod 4, so the admissible
single corners are
        r(m, eps) = eps * A^m * (-A^4 - A^-4),   m = 2 mod 4, eps = +-1,
and the forced double corner is
        C00*(m, eps) = delta (delta^2-3)^2 r(m, eps) - F.

This script:
  * computes r_H = <closure of sigma_1^(+-2)> with the validated tool
    (both are -A^4 - A^-4) and shows, by turning each bigon site of those
    diagrams back, that the relative framings realised by the 2-crossing
    Hopf diagrams are m = +6 and m = -6 (eps = +1);
  * computes C00*(m, eps) exactly for m in {-10,-6,-2,2,6,10}, eps = +-1,
    checks all exponents are 0 mod 4 and |C00*(zeta_8)| = 8 in Z[zeta_8],
    and writes each in the variable t = A^-4 (up to units);
  * proves C00*(+-6, +1) = <T(2,4)> * <Hopf> = bracket of T(2,4) # Hopf;
  * also tabulates the extended family |m| <= 30 (m = 2 mod 4) for the
    table scan.
Output: c00star.json (read by table_scan.py and composites.py).
"""

import json
import os
from common import (pmul, padd, psub, pshift, pneg, pclean, DELTA, ONE, pstr,
                    pclasses, pspan, t_up_to_units, poly_in_t, tstr,
                    z8_eval, z8_norm2, z8_str, det_from_bracket,
                    kauffman_bracket, kauffman_bracket_naive, Diagram,
                    jones_from_bracket, braid_closure_pd, turn_back_site,
                    connected_sum_links, unit_equiv, WORKDIR)
from twist import parallel_edge_pairs

M_SET = [-10, -6, -2, 2, 6, 10]


def bracket_checked(pd):
    br = kauffman_bracket(pd)
    assert kauffman_bracket_naive(pd) == br
    return br


def jones_data_3comp(C):
    """For a class-0 bracket C of a would-be 3-component link: P(t) with
    C = A^c P(t); the Jones polynomial is s t^j P(t) with s = sign(P(1))
    (V(1) = (-2)^2 = 4), and V'(1) = 6 * lk_total forces
    lk_total = (4 j + s P'(1)) / 6, i.e. lk_total = s P'(1)/2 mod 2."""
    c, P = poly_in_t(C)
    P1 = sum(P.values())
    dP1 = sum(m * v for m, v in P.items())
    s = 1 if P1 > 0 else -1
    assert abs(P1) == 4
    assert (s * dP1) % 2 == 0
    lk_parity = (s * dP1 // 2) % 2
    return c, P, P1, dP1, lk_parity


def main():
    out = {}
    delta = dict(DELTA)
    delta2 = pmul(delta, delta)
    d2m3 = padd(delta2, {0: -3})
    F = pmul(padd(delta2, {0: -2}), padd(delta2, {0: -4}))
    coef = pmul(delta, pmul(d2m3, d2m3))          # delta (delta^2-3)^2
    print("delta              =", pstr(delta))
    print("delta^2 - 3        =", pstr(d2m3))
    print("F = (d^2-2)(d^2-4) =", pstr(F))
    print("delta (d^2-3)^2    =", pstr(coef))
    print("delta(zeta_8) =", z8_str(z8_eval(delta)), "   F(zeta_8) =", z8_str(z8_eval(F)))
    assert z8_eval(delta) == [0, 0, 0, 0] and z8_eval(F) == [8, 0, 0, 0]
    out.update({"delta": pstr(delta), "F": pstr(F), "delta_d2m3_sq": pstr(coef)})

    # --- Hopf diagrams, their brackets, and the framings their sites realise
    hopf = {}
    for label, word in (("sigma_1^2", [1, 1]), ("sigma_1^-2", [-1, -1])):
        pd = braid_closure_pd(word)
        br = bracket_checked(pd)
        D = Diagram(pd)
        hopf[label] = {"pd": pd, "bracket": br, "writhe": D.writhe()}
        print("\nHopf diagram %-10s PD=%s writhe=%+d comps=%d  r_H = %s"
              % (label, pd, D.writhe(), D.num_components(), pstr(br)))
    rH = {4: -1, -4: -1}
    assert hopf["sigma_1^2"]["bracket"] == hopf["sigma_1^-2"]["bracket"] == rH
    out["r_H"] = pstr(rH)
    out["hopf_pd"] = {k: v["pd"] for k, v in hopf.items()}

    sites = []
    print("\nTurning each bigon site of the Hopf diagrams back (cup-cap for identity):")
    for label, h in hopf.items():
        pd = h["pd"]
        seen = set()
        for e1, e2, fi in parallel_edge_pairs(pd):
            key = (min(e1, e2), max(e1, e2), fi)
            if key in seen:
                continue
            seen.add(key)
            pd0 = turn_back_site(pd, e1, e2, face=fi)
            D0 = Diagram(pd0)
            u = bracket_checked(pd0)
            V = jones_from_bracket(u, D0.writhe())
            is_unknot = (D0.num_components() == 1 and pclean(V) == {0: 1})
            # relative framing: r_H = A^m * u  <=>  the single corner is A^-m... we record
            # u = A^k; relative to u = 1 the Hopf corner is A^-k * r_H, i.e. m = -k
            assert len(u) == 1
            k = next(iter(u))
            sites.append({"hopf": label, "site_edges": [e1, e2], "face": fi, "turned_pd": pd0,
                          "components": D0.num_components(), "writhe": D0.writhe(),
                          "u": pstr(u), "is_unknot_diagram": is_unknot,
                          "relative_framing_m": -k, "eps": 1 if u[k] > 0 else -1})
            print("  %-10s site (%s,%s) face %d -> %s : comps=%d writhe=%+d  u=%s  unknot=%s  => r/u = A^%d r_H (m=%+d, eps=%+d)"
                  % (label, e1, e2, fi, pd0, D0.num_components(), D0.writhe(), pstr(u), is_unknot, -k, -k, 1 if u[k] > 0 else -1))
    out["sites"] = sites
    realised = sorted({(s["relative_framing_m"], s["eps"]) for s in sites})
    print("  realised (m, eps) by 2-crossing Hopf diagrams:", realised)
    out["realised_m_eps"] = realised

    T1 = pmul(coef, rH)
    print("\nT1 = delta (d^2-3)^2 r_H =", pstr(T1), " classes mod 4:", pclasses(T1))
    print("F                        =", pstr(F), " classes mod 4:", pclasses(F))
    out["T1"] = pstr(T1)

    # --- the bare Hopf bracket (m = 0) is NOT admissible relative to u = 1
    C0 = psub(T1, F)
    print("\nBare Hopf corner r = -A^4 - A^-4 (m = 0) with u = 1:  C00* = %s" % pstr(C0))
    print("   exponent classes mod 4: %s  -> two classes, not the bracket of any diagram (inadmissible)" % pclasses(C0))
    assert pclasses(C0) == [0, 2]
    out["m0_inadmissible"] = {"C00star_A": pstr(C0), "classes_mod4": pclasses(C0)}

    # --- the twelve admissible double corners
    print("\n=== C00*(m, eps) = eps A^m T1 - F,  m in %s, eps = +-1 ===" % M_SET)
    polys = []
    for m in M_SET:
        for eps in (1, -1):
            C = psub(pshift(T1, m) if eps == 1 else pneg(pshift(T1, m)), F)
            val = z8_eval(C)
            n2 = z8_norm2(val)
            det = det_from_bracket(C)
            cls = pclasses(C)
            c, P, P1, dP1, lkpar = jones_data_3comp(C)
            rec = {"m": m, "eps": eps, "r": "%sA^%d (-A^4 - A^-4)" % ("" if eps == 1 else "-", m),
                   "C00star_A": pstr(C), "C00star_dict": {str(e): v for e, v in sorted(C.items())},
                   "classes_mod4": cls, "span_A": pspan(C), "span_t": pspan(C) // 4,
                   "C00star_at_zeta8": z8_str(val), "abs2_at_zeta8": n2, "det": det,
                   "P_t_exact": "A^%d * (%s)" % (c, tstr(P)),
                   "in_t_up_to_units": t_up_to_units(C),
                   "P(1)": P1, "P'(1)": dP1, "lk_total_parity": lkpar,
                   "_C": C}
            polys.append(rec)
            assert cls == [0], "class violation for m=%d eps=%d: %s" % (m, eps, cls)
            assert n2 == 64 and det == 8
            print("\nm=%+3d eps=%+d :  r = %s" % (m, eps, rec["r"]))
            print("   C00* = %s" % pstr(C))
            print("   classes mod 4 = %s, span_A = %d (span_t = %d)" % (cls, pspan(C), pspan(C) // 4))
            print("   C00*(zeta_8) = %s, |.|^2 = %d, det = %d" % (z8_str(val), n2, det))
            print("   in t: %s ;  up to units: %s" % (rec["P_t_exact"], rec["in_t_up_to_units"]))
            print("   P(1) = %+d, P'(1) = %+d  => total linking number of any realising 3-component link is %s"
                  % (P1, dP1, "odd" if lkpar else "even"))
    out["polys"] = [{k: v for k, v in r.items() if not k.startswith("_")} for r in polys]

    # --- identification with T(2,4) # Hopf
    print("\n=== connected sums T(2,4) # Hopf (explicit PD via connected_sum_links; product formula checked) ===")
    ident = []
    for word4 in ([1, 1, 1, 1], [-1, -1, -1, -1]):
        for word2 in ([1, 1], [-1, -1]):
            pd4 = braid_closure_pd(word4)
            pd2 = braid_closure_pd(word2)
            b4 = bracket_checked(pd4)
            b2 = bracket_checked(pd2)
            prod = pmul(b4, b2)
            pdsum = connected_sum_links(pd4, pd2)
            bsum = bracket_checked(pdsum)
            Ds = Diagram(pdsum)
            assert bsum == prod
            name = "T(2,%s4) # Hopf[%s]" % ("+" if word4[0] > 0 else "-", "+" if word2[0] > 0 else "-")
            matches = []
            for r in polys:
                ue = unit_equiv(r["_C"], bsum)
                if ue:
                    matches.append({"m": r["m"], "eps": r["eps"], "sign": ue[0], "A_power": ue[1]})
            print("%-20s PD=%s  comps=%d writhe=%+d det=%d  bracket=%s\n   matches: %s"
                  % (name, pdsum, Ds.num_components(), Ds.writhe(), det_from_bracket(bsum), pstr(bsum), matches or "none"))
            ident.append({"name": name, "braid_T24": word4, "braid_Hopf": word2, "sum_pd": pdsum,
                          "bracket": pstr(bsum), "det": det_from_bracket(bsum), "matches": matches})
    out["T24_Hopf"] = ident

    # --- extended family for the scans
    fam = []
    for m in range(-30, 31):
        if m % 4 != 2:
            continue
        for eps in (1, -1):
            C = psub(pshift(T1, m) if eps == 1 else pneg(pshift(T1, m)), F)
            assert pclasses(C) == [0] and z8_norm2(z8_eval(C)) == 64
            fam.append({"m": m, "eps": eps, "C00star_dict": {str(e): v for e, v in sorted(C.items())},
                        "C00star_A": pstr(C), "span_A": pspan(C), "in_t_up_to_units": t_up_to_units(C)})
    out["family_extended"] = fam

    with open(os.path.join(WORKDIR, "c00star.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote c00star.json")


if __name__ == "__main__":
    main()
