import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/calc')
from hf import *
from collections import Counter

def poly_mul(a, b):
    out = Counter()
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] += x * y
    return Counter({k: v for k, v in out.items() if v})
def geom(n, step=1):
    return Counter({step * i: 1 for i in range(n)})

def rel_gens(res):
    gens = []
    for (q, d2), dim in sorted(res.items()):
        gens += [(q, q - d2, d2)] * dim     # (q, 2h, 2delta)
    gens.sort()
    q0, h0, d0 = gens[0]
    return [(q - q0, (h - h0), (d - d0)) for (q, h, d) in gens]

def thin_t_poly(res):
    """if thin and all generators have (q,h) = (2k,k) relative: return Counter in t=q^2 h, else None"""
    rel = rel_gens(res)
    c = Counter()
    for (q, h2, d2) in rel:
        if d2 != 0 or h2 != q or q % 2: return None
        c[q // 2] += 1
    return c

ok = True
print("== special: P(HF(a(-n), s_2n'(0))) == (1+t^3)[n']_{t^2}[n]_t  (t=q^2 h, single delta) ==")
for npr in range(1, 6):
    S = s_curve(npr)
    assert hf(arc0(), S) == {}
    for n in range(1, 11):
        res = hf(arc_int(-n), S)
        P = thin_t_poly(res)
        pred = poly_mul(poly_mul(Counter({0: 1, 3: 1}), geom(npr, 2)), geom(n))
        good = (P == pred)
        ok &= good
        if not good: print("MISMATCH", npr, n, P, pred)
    res = hf(arcinf(), S); P = thin_t_poly(res)
    pred = poly_mul(Counter({0: 1, 3: 1}), geom(npr, 2))
    ok &= (P == pred)
print("special formula verified for n'<=5, n<=10:", ok)

ok = True
print("== rational: P(HF(a(-n), r_n'(0))) == [n']_t * (1+t+...+t^(n-2)+t^n) (n>=2), [n']_t (n=1) ==")
for npr in range(1, 8):
    R = r_curve(npr)
    for n in range(1, 10):
        res = hf(arc_int(-n), R)
        P = thin_t_poly(res)
        base = Counter({0: 1}) if n == 1 else (geom(n - 1) + Counter({n: 1}))
        pred = poly_mul(geom(npr), base)
        good = (P == pred)
        ok &= good
        if not good: print("MISMATCH", npr, n, P, pred)
    res = hf(arcinf(), R); P = thin_t_poly(res)
    ok &= (P == geom(npr))
    res = hf(arc0(), R)
    rel = rel_gens(res)
    good = rel == [(0, 0, 0), (2 * npr, 2 * (npr - 1), 2)]
    ok &= good
    if not good: print("parallel mismatch", npr, rel)
print("rational formula verified for n'<=7, n<=9 (and parallel case (0,0,0),(2n',n'-1,1)):", ok)

print("== opposite sign arcs a(+n) (mirror direction) ==")
for npr in (1, 2):
    S = s_curve(npr); R = r_curve(npr)
    for n in (1, 2, 3, 4):
        print(f"  HF(a({n}), {S.name}) t-poly:", sorted(thin_t_poly(hf(arc_int(n), S)).items()))
        print(f"  HF(a({n}), {R.name}) t-poly:", sorted(thin_t_poly(hf(arc_int(n), R)).items()))

print("== reversed order HF(gamma, a) ==")
for npr in (1, 2):
    S = s_curve(npr); R = r_curve(npr)
    for n in (1, 2, 3):
        report(hf(S, arc_int(-n)), f"HF({S.name}, a({-n}))")
        report(hf(R, arc_int(-n)), f"HF({R.name}, a({-n}))")
    report(hf(R, arc0()), f"HF({R.name}, a(0))")
    report(hf(S, arc0()), f"HF({S.name}, a(0))")
