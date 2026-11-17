"""(c) template 1: integer core, numerator degree table, case analysis; direct J along the core k=-6..6."""
import sys, time, pickle
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window')
from r2lib import *
T0 = time.time()
cab = pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window/r2_cab.pkl', 'rb'))
c1 = {kk: sp.sympify(v, locals={'t': t}) for kk, v in cab[1].items()}
k, j = sp.symbols('k j', integer=True)
m_, n_ = sp.symbols('m n', integer=True)
# integer solutions of a2 = 2m^2+3m+2n = 0
a2 = 2 * m_**2 + 3 * m_ + 2 * n_
print('a2 on m=2k, n=-4k^2-3k:', sp.expand(a2.subs({m_: 2 * k, n_: -4 * k**2 - 3 * k})))
# brute check that every integer zero with |m|<=200 is of that form (and parity argument)
sols = [(m, -(2 * m * m + 3 * m) // 2) for m in range(-200, 201) if (2 * m * m + 3 * m) % 2 == 0]
assert all(m % 2 == 0 and n == -4 * (m // 2)**2 - 3 * (m // 2) for m, n in sols)
d = t**8 * (t**2 + 1) * (t**2 + t + 1)
e = {'0': 0, '2': 1, '4': 3}
rows = {}
print('sector  mindeg maxdeg botcoef topcoef  shifted-top-on-conic')
for key in ['00', '02', '20', '22', '24', '42', '44']:
    p = sp.cancel(d * c1[key])
    P = sp.Poly(p, t)
    assert P.domain == sp.ZZ or all(cf.is_integer for cf in P.coeffs()), key
    degs = [mon[0] for mon in P.monoms()]
    lo, hi = min(degs), max(degs)
    top = P.coeff_monomial(t**hi); bot = P.coeff_monomial(t**lo)
    sh = sp.expand(hi + 2 * e[key[0]] * (2 * k) + 2 * e[key[1]] * (-4 * k**2 - 3 * k))
    rows[key] = (lo, hi, bot, top, sh)
    print('  %s    %3d   %3d    %3d    %3d     %s' % (key, lo, hi, bot, top, sh))
target = sp.expand(sp.Poly(d, t).degree() + 8 * (2 * k) + 8)
print('target top degree (deg d + F1):', target, ' F1 on core =', sp.expand(8 * 2 * k + 8), ' lead coeff of d =', sp.Poly(d, t).LC())
# k>=1: target - shifted > 0
def nonneg_poly_in_j(expr):
    P = sp.Poly(sp.expand(expr), j)
    cs = P.all_coeffs()
    return all(c >= 0 for c in cs) and cs[-1] > 0
print('k>=1 : all (target - shifted) positive:', all(nonneg_poly_in_j((target - rows[kk][4]).subs(k, j + 1)) for kk in rows))
others = [kk for kk in rows if kk != '00']
print('k<=-2: 00 strictly highest:', all(nonneg_poly_in_j((rows['00'][4] - rows[kk][4]).subs(k, -j - 2)) for kk in others),
      '; target <= -12 :', sp.expand(target.subs(k, -2)), '; top coeff of 00 =', rows['00'][3])
# brute consistency of the case analysis for |k|<=400 directly from the table
for kv in range(-400, 401):
    if kv in (-1, 0): continue
    tops = {kk: int(rows[kk][4].subs(k, kv)) for kk in rows}
    tg = int(target.subs(k, kv))
    mx = max(tops.values())
    winners = [kk for kk in tops if tops[kk] == mx]
    assert (mx < tg) or (len(winners) == 1 and mx != tg), kv
print('table-level case analysis brute-checked for |k|<=400')
# ---- direct J along the core (matrix action from JSON; no projectors) ----
Vw, Uw = 'x0.y2.y2.x1.x1', 'x1.x1.y0.x1'
for kv in range(-6, 7):
    m, n = 2 * kv, -4 * kv * kv - 3 * kv
    W = body(Vw, Uw, m, n)
    F = F_raw_direct(W)
    J = normalize(F)
    unit = (J == {0: 1})
    rawunit = (len(F) == 1)
    Jm1 = (sp.factor(S(J) - 1) if not unit else 0) if kv in (-1, 0) else None
    print('k=%2d (m,n)=(%3d,%4d) |W|=%4d  J==1:%s  raw unit:%s  span J=%s  %s' % (kv, m, n, len(W), unit, rawunit, max(J) - min(J), ('F=' + str(F)) if rawunit else ''))
    if kv in (-1, 0): print('      J-1 =', Jm1)
print('time', round(time.time() - T0, 1))
