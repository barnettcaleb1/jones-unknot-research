#!/usr/bin/env python3
"""Validate kb.py against Knot Atlas reference polynomials (cx-tools/katlas_reference.json,
read-only) and against geometric Hopf-link / 2-unlink diagrams built with geom.py."""
import json, re, sys, math
import numpy as np
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
import kb, geom

def parse_q(s):
    """parse strings like '-q^-4+q^-3+q^-1' or 'q^2+q^-2-q-q^-1+1' into dict exp->coeff (integer t-exponents)."""
    s = s.replace(' ', '').replace('{', '').replace('}', '')
    out = {}   # keys: exponent of t^(1/2)
    for m in re.finditer(r'([+-]?)(\d*)(q(?:\^\(?(-?\d+)(?:/(\d))?\)?)?)?', s):
        sign, coef, qpart, exp, den = m.groups()
        if not m.group(0):
            continue
        c = int(coef) if coef else 1
        if sign == '-':
            c = -c
        if qpart is None:
            e = 0
        else:
            e = (int(exp) if exp is not None else 1) * (2 if den is None else 1)
        out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}

ref = json.load(open('/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-tools/katlas_reference.json'))
ok_all = True
for name, d in sorted(ref.items()):
    pd = d['pd_list']
    V, w, mx = kb.jones_from_pd(pd)
    # V keys are exponents of t^(1/2); knots -> even keys
    want = parse_q(d['jones_clean'])
    ok = (V == want)
    ok_all &= ok
    print("%-7s writhe %3d  maxstates %4d  V=%s  %s" % (name, w, mx, kb.jones_str(V), "OK" if ok else "MISMATCH want %s" % want))

# geometric tests: Hopf link (two linked circles) and 2-component unlink (two stacked circles)
th = np.linspace(0, 2 * math.pi, 400, endpoint=False)
c1 = np.column_stack([np.cos(th), np.sin(th), 0 * th])
# second circle in the xz-plane through the centre of the first: Hopf link
c2 = np.column_stack([1 + np.cos(th), 0 * th, np.sin(th)])
rot = geom.rotation_matrix(0.4, 0.3, 0.2)
pd, signs, comps, lk = geom.pd_from_curves([c1, c2], rot)
V, w, mx = kb.jones_from_pd(pd, signs=signs)
print("Hopf: crossings", len(pd), "lk", lk[0, 1], "writhe", w, "V =", kb.jones_str(V))
# mirror Hopf
c2m = np.column_stack([1 + np.cos(th), 0 * th, -np.sin(th)])
pd, signs, comps, lk = geom.pd_from_curves([c1, c2m], rot)
V2, w, mx = kb.jones_from_pd(pd, signs=signs)
print("Hopf mirror: lk", lk[0, 1], "V =", kb.jones_str(V2))
assert set([tuple(sorted(V.items())), tuple(sorted(V2.items()))]) == set([tuple(sorted({1: -1, 5: -1}.items())), tuple(sorted({-1: -1, -5: -1}.items()))])
# 2-unlink: two overlapping circles, one above the other
c3 = np.column_stack([1 + np.cos(th), np.sin(th), 0 * th + 1.0])
pd, signs, comps, lk = geom.pd_from_curves([c1, c3], rot)
V3, w, mx = kb.jones_from_pd(pd, signs=signs)
print("2-unlink: crossings", len(pd), "lk", lk[0, 1], "V =", kb.jones_str(V3))
assert V3 == kb.UNLINK2
# unknot with a kink (figure: circle plus a loop) built geometrically: trefoil-ish? use a (2,3) torus knot
t = np.linspace(0, 2 * math.pi, 1200, endpoint=False)
R, r = 2.0, 0.8
tor = np.column_stack([(R + r * np.cos(3 * t)) * np.cos(2 * t), (R + r * np.cos(3 * t)) * np.sin(2 * t), r * np.sin(3 * t)])
pd, signs, comps, lk = geom.pd_from_curves([tor], rot)
V4, w, mx = kb.jones_from_pd(pd, signs=signs)
print("torus(2,3): crossings", len(pd), "writhe", w, "V =", kb.jones_str(V4))
assert V4 in ({2: 1, 6: 1, 8: -1}, {-2: 1, -6: 1, -8: -1})
print("ALL OK" if ok_all else "FAILURES")
