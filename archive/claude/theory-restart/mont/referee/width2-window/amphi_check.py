"""(c) AMPHI-PAIR checks: pole spread, delta/sigma doubling for q(t)q(1/t), parity of products,
geometric (letter-swap) mirror is channel-wise with a fixed monomial factor on rational boxes, vertical contrast."""
import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import sympy as sp
import vc
from lp import mul, top, bot, span, clean
t = sp.symbols('t')

def delta_sigma(q):
    """delta = deg - ord; sigma = s_inf + s_0 from normalised end expansions of rational q."""
    q = sp.cancel(sp.together(q))
    num, den = sp.fraction(q)
    pn, pd = sp.Poly(num, t), sp.Poly(den, t)
    deg = pn.degree() - pd.degree()
    # ord at 0: lowest exponents
    def low(p):
        terms = p.terms(); return min(m[0][0] for m in terms)
    ordq = low(pn) - low(pd)
    # normalised expansions
    ser_inf = sp.series(sp.expand(q.subs(t, 1/t) / ( (1/t)**deg )), t, 0, 2).removeO()
    c_inf = ser_inf.subs(t, 0); s_inf = sp.simplify(ser_inf.coeff(t, 1) / c_inf)
    ser0 = sp.series(sp.expand(q / t**ordq), t, 0, 2).removeO()
    c0 = ser0.subs(t, 0); s0 = sp.simplify(ser0.coeff(t, 1) / c0)
    return deg - ordq, s_inf + s0, deg, ordq

print('--- pole -w1/w3 of the horizontal special twist ---')
for mu in list(range(-8, 0)) + list(range(1, 9)):
    w1 = t + (1 + t**2) * (-t)**mu
    w3 = (1 + t**2) * (1 - (-t)**mu)
    d, s, dg, od = delta_sigma(-w1 / w3)
    print('mu=%3d  delta=%d  sigma=%s' % (mu, d, s))
print('mu=0: w3 =', sp.simplify((1 + t**2) * (1 - (-t)**0)), '(pole undefined)')

print('--- vertical closure contrast: delta_V = span w1(a) - span wV(a) ---')
for a in [-7, -5, -3, 3, 5, 7]:
    w1 = sp.expand((t + (1 + t**2) * (-t)**a) * t**20)
    wV = sp.expand(((-t)**a * t + t**(3*a - 1) * (1 + t + t**2 + t**3 + t**4)) * t**30)
    sw1 = sp.Poly(w1, t); swV = sp.Poly(wV, t)
    sp1 = sw1.degree() - min(m[0][0] for m in sw1.terms()); spV = swV.degree() - min(m[0][0] for m in swV.terms())
    print('a=%3d  delta*_V = %d  (parity %s)' % (a, sp1 - spV, 'even' if (sp1 - spV) % 2 == 0 else 'odd'))

print('--- random rational q: delta(Q)=2delta(q), sigma(Q)=2sigma(q) for Q = eps t^l q(t) q(1/t) ---')
rng = random.Random(5)
def rpoly():
    lo = rng.randint(-3, 3); n = rng.randint(1, 5)
    cs = [rng.randint(-3, 3) for _ in range(n)]
    cs[0] = cs[0] or 1; cs[-1] = cs[-1] or 2
    return sum(c * t**(lo + i) for i, c in enumerate(cs))
bad = 0
for i in range(40):
    q = rpoly() / rpoly()
    eps, l = rng.choice([-1, 1]), rng.randint(-4, 4)
    Q = eps * t**l * q * q.subs(t, 1/t)
    d, s, _, _ = delta_sigma(q); D2, S2, _, _ = delta_sigma(Q)
    if D2 != 2 * d or sp.simplify(S2 - 2 * s) != 0: bad += 1; print('MISMATCH', q, d, s, D2, S2)
print('random pairs checked: 40, mismatches:', bad)
# products of several pairs (and swapped-channel variant q(t)/q(1/t)) keep even delta
odd = 0
for i in range(20):
    Q = 1
    for j in range(rng.randint(1, 3)):
        q = rpoly() / rpoly()
        Q *= q * (q.subs(t, 1/t) if rng.random() < 0.5 else 1 / q.subs(t, 1/t))
    if delta_sigma(Q)[0] % 2: odd += 1
print('products of 1-3 pairs (mixed q(1/t)^(+-1)): odd delta count =', odd)

print('--- geometric mirror (letter swap X<->x, Y<->y) on rational boxes: channel-wise with fixed monomial? ---')
def inv(p): return {-e: c for e, c in p.items()}
SW = {'X': 'x', 'x': 'X', 'Y': 'y', 'y': 'Y'}
found = {}
for i in range(300):
    w = ''.join(rng.choice('XxYy') for _ in range(rng.randint(1, 9)))
    v = vc.rat(w); vm = vc.rat(''.join(SW[c] for c in w))
    if v is None or vm is None: continue
    a, b = v; am, bm = vm
    lhs = mul(bm, inv(a)); rhs = mul(am, inv(b))   # want lhs = c t^l rhs
    if not lhs or not rhs:
        found.setdefault('zero-channel', 0); found['zero-channel'] += 1; continue
    l = top(lhs) - top(rhs); c = lhs[top(lhs)] / rhs[top(rhs)]
    ok = clean({e: lhs.get(e, 0) - c * rhs.get(e - l, 0) for e in set(lhs) | {e + l for e in rhs}}) == {}
    key = (c, l) if ok else 'NOT channel-wise'
    found[key] = found.get(key, 0) + 1
print('q(mirror)(t) = c t^l q(t^-1):', found)
