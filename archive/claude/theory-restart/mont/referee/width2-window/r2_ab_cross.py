"""(a) cross-check F(m,n) = sum c_ab t^(2e_a m+2e_b n) against lp.J on literal halfwords and against direct matrix action;
(b) F1, F2, a2 symbolic; numeric check of a2 against lp.a2(lp.J)."""
import sys, time, pickle, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window')
from r2lib import *
T0 = time.time()
cab = pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window/r2_cab.pkl', 'rb'))
cab = {k: {kk: sp.sympify(v, locals={'t': t}) for kk, v in c.items()} for k, c in cab.items()}
TEMPL = {1: ('x0.y2.y2.x1.x1', 'x1.x1.y0.x1'), 2: ('y0.y2.y1.x0.x3.y2', 'y3.x2.x2.y3.x0.x1')}
e = {'0': 0, '2': 1, '4': 3}
m_, n_ = sp.symbols('m n', integer=True)
def q(key, m, n): return 2 * e[key[0]] * m + 2 * e[key[1]] * n
def F_sector(k, m, n):
    expr = sp.cancel(sum(c * t**q(key, m, n) for key, c in cab[k].items()))
    num, den = sp.fraction(expr)
    pn = sp.Poly(num, t); pd = sp.Poly(den, t)
    assert len(pd.terms()) == 1, ('not Laurent', k, m, n, den)
    (de,), dc = pd.terms()[0]
    return {mon[0] - de: sp.Integer(cf) / dc for mon, cf in pn.terms()}
def tolint(F):
    out = {}
    for k_, v in F.items():
        assert v == int(v); out[int(k_)] = int(v)
    return out
# ---- (b) moments, symbolic ----
res = {}
for k in (1, 2):
    F1 = 0; F2 = 0; F0 = 0
    trip = {}
    for key, c in cab[k].items():
        Dc = sp.cancel(t * sp.diff(c, t)); D2c = sp.cancel(t * sp.diff(Dc, t))
        c0, c1, c2 = [sp.nsimplify(sp.cancel(x).subs(t, -1)) for x in (c, Dc, D2c)]
        trip[key] = (c0, c1, c2)
        qq = q(key, m_, n_)
        F0 += c0; F1 += c1 + qq * c0; F2 += c2 + 2 * qq * c1 + qq**2 * c0
    F1 = sp.expand(F1); F2 = sp.expand(F2)
    a2 = sp.expand(-(F2 - F1**2) / 24)
    res[k] = (F0, F1, F2, a2)
    print('TEMPLATE', k, 'triples (c,Dc,D^2c)(-1):', {kk: tuple(int(x) for x in v) for kk, v in sorted(trip.items())})
    print('   F0 =', F0, ' F1 =', F1, ' F2 =', F2, ' a2 =', a2)
# ---- (a) cross-checks ----
random.seed(20261117)
pairs = {1: [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1), (2, -1), (-2, -1), (-2, 1), (2, 1),
             (0, -2), (0, 2), (2, -3), (-4, -10), (-3, 2), (3, -2), (1, -2), (-2, 3), (2, -7), (4, -22)],
         2: [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1), (2, -1), (-2, -1), (-2, 1), (2, 1),
             (0, -2), (0, 2), (2, -3), (-3, 2), (3, -2), (1, -2), (-2, 3), (3, 3), (-3, -3), (2, 2)]}
nck = 0
for k, (Vw, Uw) in TEMPL.items():
    F0, F1, F2, a2 = res[k]
    for (m, n) in pairs[k]:
        W = body(Vw, Uw, m, n)
        hw = halfword(W)
        Fs = tolint(F_sector(k, m, n))
        Fd = F_raw_direct(W)
        Jlp = lp.J(hw)
        Js = normalize(Fs)
        ok_dir = (Fs == Fd)
        ok_lp = (Js == Jlp)
        # value / moment checks
        val = sum(c * (-1)**(ee % 2) for ee, c in Fs.items())
        f1 = sum(ee * c * (-1)**(ee % 2) for ee, c in Fs.items())
        a2num = lp.a2(Jlp)
        ok_mom = (val == 1 and f1 == F1.subs({m_: m, n_: n}) and abs(a2num - float(a2.subs({m_: m, n_: n}))) < 1e-9)
        unit = (Jlp == {0: 1})
        nck += 1
        print('T%d (m,n)=(%3d,%3d) |W|=%3d sector==direct:%s sector==lp.J:%s F(-1)=%d F1=%d a2(lp)=%s a2(formula)=%s J==1:%s' % (
            k, m, n, len(W), ok_dir, ok_lp, val, f1, a2num, a2.subs({m_: m, n_: n}), unit))
        assert ok_dir and ok_lp and ok_mom, (k, m, n)
print('all', nck, 'cross-checks passed; time', round(time.time() - T0, 1))
pickle.dump({k: tuple(str(x) for x in v) for k, v in res.items()}, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window/r2_moments.pkl', 'wb'))
