#!/usr/bin/env python3
"""
certify.py -- certificate data for a candidate counterexample to the Jones
unknot conjecture (a nontrivial knot with V(t) = 1).

certify(pd) returns a dict with
  V, V_str, V_is_one       Jones polynomial (dict: key k means t^(k/2))
  det                      |V(-1)| = |Delta(-1)| (exact integer)
  V_at_i                   V(i) as an exact element of Z[zeta_8] (coefficients
                           of 1, z, z^2, z^3 with z = e^{i pi/4}) plus a float
  arf                      Arf invariant for knots (V(i) = (-1)^Arf), else None
  components, writhe, crossings
and, when snappy/spherogram import:
  alexander                Conway-normalised Alexander polynomial from the
                           Seifert matrix (exact; pure-Python Bareiss +
                           interpolation), dict {power: coeff}
  signature                exact signature (Sylvester inertia of S + S^T, sign
                           convention: right-handed trefoil = -2)
  det_seifert              |det(V + V^T)|   (must equal det)
  hfk                      knots only: total_rank, seifert_genus, fibered,
                           tau, epsilon, nu, and the Alexander polynomial
                           recovered as the graded Euler characteristic
  hfk_nontrivial           True iff HFK total rank > 1  (certifies a
                           nontrivial knot: HFK-hat detects the unknot)
  volume, solution_type, identify, group (generators/relators after SnapPea
                           simplification), group_is_Z (certifies the unknot
                           when True; False is inconclusive)
  verdict                  one-line summary

Usage:  certify.py FILE.json      where FILE.json is a PD code (list of
        4-lists) or {"pd": [...]}, {"braid_closure": [...]}, or
        {"plat_closure": [...], "n_strands": 4}.
"""

import sys
import json
import time
import math
from fractions import Fraction

from bracket import (Diagram, jones_from_pd, jones_str, jones_t, pclean)

try:
    import warnings
    warnings.filterwarnings("ignore")
    import snappy
    import spherogram
    HAVE_SNAPPY = True
except Exception as _ex:          # pragma: no cover
    HAVE_SNAPPY = False
    SNAPPY_ERROR = repr(_ex)


# ---------------------------------------------------------------- V(-1), V(i)

def jones_at_minus_one(V):
    """|V(-1)| as an exact integer.  t = -1 means t^(1/2) = i."""
    re = im = 0
    for k, c in V.items():
        r = k % 4
        if r == 0:
            re += c
        elif r == 1:
            im += c
        elif r == 2:
            re -= c
        else:
            im -= c
    if re and im:
        return math.hypot(re, im)       # cannot happen for a link
    return abs(re) + abs(im)


def jones_at_i(V):
    """V(i) exactly in Z[z], z = exp(i pi/4) (t^(1/2) = z); returns
    (coeffs [c0,c1,c2,c3] meaning c0 + c1 z + c2 z^2 + c3 z^3, complex)."""
    co = [0, 0, 0, 0]
    for k, c in V.items():
        r = k % 8
        sgn = -1 if r >= 4 else 1
        co[r % 4] += sgn * c
    z = complex(math.cos(math.pi / 4), math.sin(math.pi / 4))
    val = co[0] + co[1] * z + co[2] * z ** 2 + co[3] * z ** 3
    return co, val


# ------------------------------------------------- exact Seifert-matrix work

def _bareiss_det(M):
    """Exact determinant of an integer matrix (fraction-free)."""
    A = [list(r) for r in M]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if sw is None:
                return 0
            A[k], A[sw] = A[sw], A[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def alexander_from_seifert(S):
    """det(S - t S^T) by exact evaluation/interpolation; returns a dict
    {power: coeff} normalised to be symmetric (Conway form) with Delta(1)=1
    for knots.  For links (Delta(1) = 0) the sign is fixed so that the
    leading coefficient is positive."""
    g2 = len(S)
    if g2 == 0:
        return {0: 1}
    ST = [[S[j][i] for j in range(g2)] for i in range(g2)]
    pts = list(range(g2 + 1))
    vals = [_bareiss_det([[S[i][j] - t * ST[i][j] for j in range(g2)] for i in range(g2)]) for t in pts]
    # Lagrange interpolation -> coefficients (exact)
    coeffs = [Fraction(0)] * (g2 + 1)
    for a, ya in zip(pts, vals):
        basis = [Fraction(1)]
        denom = Fraction(1)
        for b in pts:
            if b == a:
                continue
            basis = [Fraction(0)] + basis
            for k in range(len(basis) - 1):
                basis[k] -= b * basis[k + 1]
            denom *= (a - b)
        for k in range(len(basis)):
            coeffs[k] += ya * basis[k] / denom
    poly = {k: int(c) for k, c in enumerate(coeffs) if c}
    assert all(c.denominator == 1 for c in coeffs)
    if not poly:
        return {}
    lo, hi = min(poly), max(poly)
    if (lo + hi) % 2 == 0:
        sh = (lo + hi) // 2
        poly = {k - sh: c for k, c in poly.items()}
    at1 = sum(poly.values())
    if at1 == 1 or at1 == -1:
        if at1 == -1:
            poly = {k: -c for k, c in poly.items()}
    elif poly[max(poly)] < 0:
        poly = {k: -c for k, c in poly.items()}
    return poly


def inertia(M):
    """(pos, neg, zero) of a symmetric rational matrix (Sylvester)."""
    A = [[Fraction(x) for x in r] for r in M]
    n = len(A)
    idx = list(range(n))
    pos = neg = zero = 0
    while idx:
        piv = next((i for i in idx if A[i][i] != 0), None)
        if piv is not None:
            d = A[piv][piv]
            if d > 0:
                pos += 1
            else:
                neg += 1
            idx.remove(piv)
            for i in idx:
                if A[i][piv] == 0:
                    continue
                f = A[i][piv] / d
                for j in idx:
                    A[i][j] -= f * A[piv][j]
            for i in idx:
                A[i][piv] = A[piv][i] = Fraction(0)
            continue
        pair = None
        for i in idx:
            for j in idx:
                if i < j and A[i][j] != 0:
                    pair = (i, j)
                    break
            if pair:
                break
        if pair is None:
            zero += len(idx)
            break
        i, j = pair
        m = A[i][j]
        pos += 1
        neg += 1
        idx.remove(i)
        idx.remove(j)
        # Schur complement w.r.t. block [[0,m],[m,0]]^-1 = [[0,1/m],[1/m,0]]
        for r in idx:
            ci, cj = A[r][i], A[r][j]
            if ci == 0 and cj == 0:
                continue
            for s in idx:
                A[r][s] -= (ci * A[j][s] + cj * A[i][s]) / m
        for r in idx:
            A[r][i] = A[r][j] = A[i][r] = A[j][r] = Fraction(0)
    return pos, neg, zero


def alexander_from_hfk(ranks):
    poly = {}
    for (a, m), r in ranks.items():
        poly[a] = poly.get(a, 0) + (-1) ** m * r
    return pclean(poly)


def poly_str(p, var="t"):
    from bracket import pstr
    return pstr(p, var)


# ----------------------------------------------------------------- certify

def certify(pd, use_snappy=True, hfk=True, geometry=True):
    pd = [list(x) for x in pd]
    out = {"crossings": len(pd), "timings": {}}
    D = Diagram(pd)
    out["components"] = D.num_components()
    out["writhe"] = D.writhe()
    t0 = time.perf_counter()
    stats = {}
    V = jones_from_pd(pd, stats=stats)
    out["timings"]["jones"] = time.perf_counter() - t0
    out["V"] = V
    out["V_str"] = jones_str(V)
    out["V_is_one"] = (pclean(V) == {0: 1})
    out["bracket_max_states"] = stats.get("max_states")
    out["det"] = jones_at_minus_one(V)
    co, val = jones_at_i(V)
    out["V_at_i"] = {"zeta8_coeffs": co, "complex": [val.real, val.imag]}
    if out["components"] == 1:
        if co == [1, 0, 0, 0]:
            out["arf"] = 0
        elif co == [-1, 0, 0, 0]:
            out["arf"] = 1
        else:
            out["arf"] = None
            out["warning_arf"] = "V(i) is not +-1 for a knot: something is wrong"
    else:
        out["arf"] = None
    out["snappy"] = HAVE_SNAPPY and use_snappy
    if not (HAVE_SNAPPY and use_snappy):
        out["verdict"] = _verdict(out)
        return out
    L = spherogram.Link(pd)
    out["spherogram_components"] = len(L.link_components)
    out["spherogram_writhe"] = L.writhe()
    t0 = time.perf_counter()
    S = L.seifert_matrix()
    S = [[int(x) for x in row] for row in S]
    out["seifert_matrix_size"] = len(S)
    try:
        alex = alexander_from_seifert(S)
        out["alexander"] = alex
        out["alexander_str"] = poly_str(alex)
        Ssym = [[S[i][j] + S[j][i] for j in range(len(S))] for i in range(len(S))]
        out["det_seifert"] = abs(_bareiss_det(Ssym))
        p, nn, z = inertia(Ssym)
        # Sign convention: "positive knots have negative signature" (the
        # right-handed trefoil, V = t + t^3 - t^4, gets -2; this is the
        # KnotInfo convention and spherogram's new_convention=True).  The raw
        # inertia of spherogram's seifert_matrix() has the opposite sign, so
        # it is negated here.
        out["signature"] = -(p - nn)
        out["signature_convention"] = "right-handed trefoil = -2 (negated inertia of spherogram S+S^T)"
        out["seifert_nullity"] = z
    except Exception as ex:
        out["alexander_error"] = repr(ex)
    out["timings"]["seifert"] = time.perf_counter() - t0
    if hfk and out["components"] == 1:
        t0 = time.perf_counter()
        try:
            try:
                h = L.knot_floer_homology()
            except ValueError as ex:
                # Szabo's calculator refuses diagrams with a reducing R1 move;
                # retry on a simplified copy (same knot type).
                L2 = L.copy()
                L2.simplify("global")
                if len(L2.crossings) == 0:
                    h = {"total_rank": 1, "seifert_genus": 0, "fibered": True, "tau": 0, "epsilon": 0, "nu": 0,
                         "L_space_knot": True, "modulus": 2, "ranks": {(0, 0): 1}}
                    out["hfk_note"] = "diagram simplified to 0 crossings (unknot); HFK filled in by hand: %s" % ex
                else:
                    h = L2.knot_floer_homology()
                    out["hfk_note"] = "computed on a simplified copy (%d crossings): %s" % (len(L2.crossings), ex)
            out["hfk"] = {k: v for k, v in h.items() if k != "ranks"}
            out["hfk"]["ranks"] = {"%d,%d" % k: v for k, v in h["ranks"].items()}
            out["hfk"]["alexander_from_hfk"] = poly_str(alexander_from_hfk(h["ranks"]))
            out["hfk_nontrivial"] = h["total_rank"] > 1
            if "alexander" in out:
                out["alexander_consistent"] = (alexander_from_hfk(h["ranks"]) == out["alexander"])
        except Exception as ex:
            out["hfk_error"] = repr(ex)
        out["timings"]["hfk"] = time.perf_counter() - t0
    if geometry:
        t0 = time.perf_counter()
        try:
            E = L.exterior()
            out["volume"] = float(E.volume())
            out["solution_type"] = E.solution_type()
            try:
                out["identify"] = [str(m) for m in E.identify()]
            except Exception as ex:
                out["identify"] = "error: %r" % (ex,)
            G = E.fundamental_group()
            out["group"] = {"generators": G.num_generators(),
                            "relators": [str(r) for r in G.relators()]}
            out["group_is_Z"] = (G.num_generators() == 1 and len(G.relators()) == 0)
        except Exception as ex:
            out["geometry_error"] = repr(ex)
        out["timings"]["geometry"] = time.perf_counter() - t0
    out["verdict"] = _verdict(out)
    return out


def _verdict(out):
    if out["components"] != 1:
        return "link with %d components; V = %s" % (out["components"], out["V_str"])
    if not out["V_is_one"]:
        return "V != 1 (V = %s): not a candidate" % out["V_str"]
    if out.get("hfk_nontrivial") is True:
        return ("V = 1 AND HFK total rank %d > 1: nontrivial knot with trivial Jones "
                "polynomial -- COUNTEREXAMPLE to the Jones unknot conjecture (recheck everything!)"
                % out["hfk"]["total_rank"])
    if out.get("hfk_nontrivial") is False:
        return "V = 1 and HFK rank 1 (genus 0): this is the unknot; not a counterexample"
    if out.get("group_is_Z"):
        return "V = 1 and knot group simplifies to Z: unknot; not a counterexample"
    return "V = 1 but nontriviality undetermined (no HFK available)"


def _load(path):
    with open(path) as fh:
        data = json.load(fh)
    if isinstance(data, list):
        return data
    if "pd" in data:
        return data["pd"]
    import twist
    if "braid_closure" in data:
        return twist.braid_closure_pd(data["braid_closure"], data.get("n_strands"))
    if "plat_closure" in data:
        return twist.plat_closure_pd(data["plat_closure"], data["n_strands"])
    raise ValueError("no PD code found in %s" % path)


def _json_safe(o):
    if isinstance(o, dict):
        return {str(k): _json_safe(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_json_safe(v) for v in o]
    if isinstance(o, (bool, int, float, str)) or o is None:
        return o
    return str(o)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    pd = _load(sys.argv[1])
    t0 = time.perf_counter()
    res = certify(pd)
    res["timings"]["total"] = time.perf_counter() - t0
    print(json.dumps(_json_safe(res), indent=1))
