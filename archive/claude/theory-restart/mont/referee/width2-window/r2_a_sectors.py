"""(a) recompute the seven sector coefficients from rho2_matrices.json; projectors from eigenvalues 1,-t,t^3."""
import sys, time, pickle, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window')
from r2lib import *

T0 = time.time()
I9 = sp.eye(9)
X = {L: Smat(M[L]) for L in M}
# relations
for i in range(4):
    P = (X['x%d' % i] * X['y%d' % i]).applyfunc(sp.expand)
    assert P == I9, i
assert (X['x1'] * X['x3'] - X['x3'] * X['x1']).applyfunc(sp.expand) == sp.zeros(9), 'X1 X3 do not commute'
lam = [sp.Integer(1), -t, t**3]
for L in ['x1', 'x3']:
    Z = ((X[L] - lam[0] * I9) * (X[L] - lam[1] * I9) * (X[L] - lam[2] * I9)).applyfunc(sp.expand)
    assert Z == sp.zeros(9), L
    # eigen multiplicities: ranks of (X - lam) at generic t
    mult = []
    for a in range(3):
        rk = (X[L] - lam[a] * I9).subs(t, sp.Rational(7, 3)).rank()
        mult.append(9 - rk)
    print(L, 'minimal poly (X-1)(X+t)(X-t^3)=0 OK; eigen multiplicities (1,-t,t^3) =', mult)
# numerator matrices N_a = prod_{b!=a}(X - lam_b), den_a = prod_{b!=a}(lam_a - lam_b)
def Nmat(L, a):
    R = I9
    for b in range(3):
        if b != a: R = R * (X[L] - lam[b] * I9)
    return R.applyfunc(sp.expand)
den = []
for a in range(3):
    d = sp.Integer(1)
    for b in range(3):
        if b != a: d *= (lam[a] - lam[b])
    den.append(sp.factor(d))
print('projector denominators', den)
N1 = [Nmat('x1', a) for a in range(3)]
N3 = [Nmat('x3', a) for a in range(3)]
COL = [0, 2, 4]
E = {}
for a in range(3):
    for b in range(3):
        E[(COL[a], COL[b])] = ((N1[a] * N3[b]).applyfunc(sp.expand), den[a] * den[b])
# projector checks: idempotent, complete
P1 = [(N1[a] / den[a]).applyfunc(sp.cancel) for a in range(3)]
P3 = [(N3[a] / den[a]).applyfunc(sp.cancel) for a in range(3)]
for P in (P1, P3):
    assert (P[0] + P[1] + P[2] - I9).applyfunc(sp.cancel) == sp.zeros(9)
    for a in range(3):
        assert (P[a] * P[a] - P[a]).applyfunc(sp.cancel) == sp.zeros(9)
print('projectors idempotent and complete: OK')
ranks = [[None] * 3 for _ in range(3)]
zero = []
for a in range(3):
    for b in range(3):
        Nn, dd = E[(COL[a], COL[b])]
        if Nn == sp.zeros(9): zero.append('%d%d' % (COL[a], COL[b])); ranks[a][b] = 0; continue
        r1 = Nn.subs(t, sp.Rational(7, 3)).rank(); r2 = Nn.subs(t, sp.Rational(-11, 5)).rank()
        ranks[a][b] = (r1, r2)
print('joint ranks (two generic t):', ranks)
print('identically zero joint projectors:', zero)

TEMPL = {1: ('x0.y2.y2.x1.x1', 'x1.x1.y0.x1'), 2: ('y0.y2.y1.x0.x3.y2', 'y3.x2.x2.y3.x0.x1')}
out = {}
for k, (Vw, Uw) in TEMPL.items():
    vv = apply_word(Vw, V0)
    ww = PHI
    for L in words(Uw):
        # covector after U: phi . M[U_last] ... M[U_1]; so apply in order U_1 first to the vector -> covector multiplies on the right in reverse order
        pass
    # covector: phi * M[U_n] * ... * M[U_1]
    ww = PHI
    for L in reversed(words(Uw)):
        ww = covec_mat(ww, M[L])
    vvS = sp.Matrix(9, 1, lambda i, j: S(vv[i]))
    wwS = sp.Matrix(1, 9, lambda i, j: S(ww[j]))
    c = {}
    for key, (Nn, dd) in E.items():
        if Nn == sp.zeros(9): continue
        num = sp.expand((wwS * Nn * vvS)[0, 0])
        c['%d%d' % key] = sp.factor(sp.cancel(t**2 * num / ((1 + t)**4 * dd)))
    out[k] = c
    print('\nTEMPLATE', k, 'V =', Vw, 'U =', Uw)
    for key in ['00', '02', '20', '22', '24', '42', '44']:
        print('  c%s =' % key, c[key])
    tot = sp.factor(sp.cancel(sum(c.values())))
    direct = F_raw_direct(words(Vw) + words(Uw))
    print('  sum c_ab =', tot, '; direct F(0,0) matches:', sp.expand(tot - S(direct)) == 0)
pickle.dump({k: {kk: str(v) for kk, v in c.items()} for k, c in out.items()}, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window/r2_cab.pkl', 'wb'))
print('time', round(time.time() - T0, 1))
