import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from closures import twist, poincare, show
# special of the trefoil quotient in the normalized frame: (c~, d~) = (-10, 1)
S = parse_chain(-1, 9, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—').shift(-8, -24)
c, d = -10, 1
def poly_mul(a, b):
    r = {}
    for i, x in a.items():
        for j, y in b.items(): r[i + j] = r.get(i + j, 0) + x * y
    return r
ok = True
for nu in [2, -2, 4, -4, 6, -6, 8, -8]:
    t = poincare(twist(nu), S, range(-45, 20), range(-90, 40))
    s = show(t); assert len(s) == 1
    dl, = s.keys(); v = s[dl]
    qmin = min(x[1] for x in v); qmax = max(x[1] for x in v)
    pred_d = d - (1 if nu < 0 else 0); pred = (c - 4 + min(0, 2 * nu), c + 4 + max(0, 2 * nu))
    hmin = min(x[0] for x in v)
    got = {x[0] - hmin: x[2] for x in v}
    want = poly_mul(poly_mul({0: 1, 2: 1}, {0: 1, 3: 1}), {i: 1 for i in range(abs(nu))})
    good = (dl == pred_d and (qmin, qmax) == pred and got == want)
    ok &= good
    print('nu=%3d delta=%s (pred %s) q-range %s (pred %s) Poincare ok: %s' % (nu, dl, pred_d, (qmin, qmax), pred, got == want))
print('ALL OK' if ok else 'MISMATCH')
