"""Exact classification of unit points in the TWO supplied fixed sector tables.

No scan: derivatives give two conics; inequalities handle both infinite tails
of the one unbounded integral conic. Only its two remaining parameters are
evaluated. Run with the theory-restart tools/venv Python (SymPy).
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "collab/data/engineB/exact_sectors.json"
OUT = Path(__file__).with_suffix(".json")
t, m, n = s.symbols("t m n")
k, j = s.symbols("k j", integer=True)
e = {"0": 0, "2": 1, "4": 3}
data = json.loads(INPUT.read_text())
assert len(data) == 2

def D(f):
    return t * s.diff(f, t)

def at_minus_one(f):
    return s.cancel(f).subs(t, -1)

def body(d):
    return {ab: s.sympify(txt, locals={"t": t}) for ab, txt in d["c"].items()}

def moment_data(c):
    raw = [s.S.Zero, s.S.Zero, s.S.Zero]
    table = {}
    for ab, f in c.items():
        q = 2*e[ab[0]]*m + 2*e[ab[1]]*n
        a, b, cc = [at_minus_one(x) for x in (f, D(f), D(D(f)))]
        table[ab] = [str(a), str(b), str(cc)]
        raw[0] += a
        raw[1] += b + q*a
        raw[2] += cc + 2*q*b + q*q*a
    raw = [s.expand(f) for f in raw]
    assert raw[0] == 1
    f1 = raw[1]
    a2 = s.expand(-(raw[2] - f1*f1)/24)
    return raw, f1, a2, table

def F_at(c, mm, nn):
    return s.cancel(sum(f*t**(2*e[ab[0]]*mm + 2*e[ab[1]]*nn)
                        for ab, f in c.items()))

def positive_on_nonnegative_integer_axis(f):
    p = s.Poly(s.expand(f), j)
    # A positive constant and nonnegative other coefficients is sufficient.
    assert p.eval(0) > 0
    assert all(a >= 0 for a in p.all_coeffs())

results = []
for idx, d in enumerate(data, 1):
    c = body(d)
    raw, f1, a2, jets = moment_data(c)
    assert s.cancel(sum(c.values()) - s.sympify(d["Jraw00"])) == 0
    results.append({"template": idx, "V": d["V"], "U": d["U"],
                    "sector_D_jets_at_minus_one": jets,
                    "F0_F1_F2": [str(f) for f in raw],
                    "normalizing_exponent": str(f1), "a2": str(a2)})

c = body(data[0])
assert s.expand(moment_data(c)[2] - (2*m*m + 3*m + 2*n)) == 0
assert (2*m*m + 3*m + 2*n).subs({m: 2*k, n: -4*k*k-3*k}).expand() == 0
den = t**8*(t*t+1)*(t*t+t+1)
tops = {}
rows = {}
for ab, f in c.items():
    p = s.Poly(s.cancel(den*f), t, domain=s.ZZ)
    lo, hi = min(v[0][0] for v in p.terms()), p.degree()
    shift = 4*e[ab[0]]*k + 2*e[ab[1]]*(-4*k*k-3*k)
    tops[ab] = s.expand(hi + shift)
    rows[ab] = {"min_degree": lo, "max_degree": hi,
                "bottom_coefficient": int(p.nth(lo)),
                "top_coefficient": int(p.LC()),
                "shifted_top_on_core": str(tops[ab])}
target_top = 16*k + 20
for ab in tops:
    positive_on_nonnegative_integer_axis((target_top - tops[ab]).subs(k, j+1))
for ab in tops:
    if ab != "00":
        positive_on_nonnegative_integer_axis((tops["00"] - tops[ab]).subs(k, -j-2))
positive_on_nonnegative_integer_axis((tops["00"] - target_top).subs(k, -j-2))
assert rows["00"]["top_coefficient"] == -1
assert F_at(c, -2, -1) == t**-8
J00 = s.cancel(t**-8*F_at(c, 0, 0))
assert J00 != 1
expected1 = -(t-1)*(t+1)**3*(t*t+1)*(t*t-t+1)**2*(t**4-t**3+t*t-t+1)/t**14
assert s.cancel(J00-1-expected1) == 0
results[0].update({"common_denominator": str(den), "numerator_sector_data": rows,
                   "core_integer_locus": "m=2k, n=-4k^2-3k, k in Z",
                   "remaining_k": [-1, 0], "J00_minus_one": str(s.factor(J00-1)),
                   "unit_points": [[-2, -1]], "raw_value_at_unit": "t**(-8)",
                   "simplified_unit_body": "y2.y2.y3.y3.x1",
                   "knot_type_of_unit": "not certified by this computation"})

c = body(data[1])
assert s.expand(moment_data(c)[2] - (2*m*m+3*m+2*n*n+3*n)) == 0
assert s.expand((4*m+3)**2+(4*n+3)**2-18-8*moment_data(c)[2]) == 0
# The only squares <=18 congruent to a square of an integer ==3 (mod4)
# which can sum to18 are9+9; its signed roots ==3 (mod4) are both +3.
assert [(x*x, y*y) for x in (0, 1, 2, 3, 4) for y in (0, 1, 2, 3, 4)
        if x*x+y*y == 18] == [(9, 9)]
assert [r for r in (-3, 3) if r % 4 == 3] == [3]
J00 = F_at(c, 0, 0)
expected2 = (t-1)**2*(t+1)**3*(t*t+1)*(t*t-t+1)*(t**4-t**3+t*t-t+1)/t**11
assert s.cancel(J00-1-expected2) == 0
results[1].update({"core_integer_locus": [[0, 0]],
                   "J00_minus_one": str(s.factor(J00-1)), "unit_points": []})
OUT.write_text(json.dumps({"input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
                           "status": "all exact assertions passed", "results": results}, indent=2)+"\n")
print("PASS: template 1 unit locus {(-2,-1)}; template 2 unit locus empty.")
print("No knot-type or nontriviality certificate is asserted for the unit point.")
print(OUT)
