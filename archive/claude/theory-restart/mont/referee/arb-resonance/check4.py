"""CHECK 4 (formal budget-exhausting state, Codex section 4 / note section 5).
 (a,c) = (1 + (s-1) C E, E), s = (-t)^mu:  A = 1 + sCE, B = CE, A - sB = 1; contents; jets at -1; root gates; both ends cancel when
 the support of sCE straddles exponent 0 (simultaneous resonance, H = tau0 + tauinf).  Plus: survey of exact root-of-unity
 residues of actual bodies (a, b, c mod Phi_n) to see which finite scalar gates actual bodies satisfy, and whether Codex's E
 (divisible by (t+1)^k Phi6 Phi10) meets all of them or needs extra cyclotomic factors."""
import sys, random, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/arb-resonance')
from common import *
rng = random.Random(99)
PHI = {1: {0: -1, 1: 1}, 2: {0: 1, 1: 1}, 3: PHI3, 4: T2P1, 6: {0: 1, 1: -1, 2: 1}, 5: PHI5, 10: {0: 1, 1: -1, 2: 1, 3: -1, 4: 1}, 12: {0: 1, 2: -1, 4: 1}}
def rem(f, n):
    """residue of Laurent f modulo Phi_n, as a canonical tuple (sympy rem over ZZ, monic divisor)"""
    f = clean(dict(f)); lo = bot(f) if f else 0
    P = to_poly(f) if f else sp.Poly(0, t, domain='ZZ')
    # multiply residue by t^lo mod Phi_n: t is invertible mod Phi_n
    r = sp.rem(P * sp.Poly(t, t)**0, sp.Poly(to_sym(PHI[n]), t, domain='ZZ'))
    x = sp.rem(r * sp.Poly(t**(lo % (12*n)), t), sp.Poly(to_sym(PHI[n]), t, domain='ZZ')) if lo >= 0 else None
    if lo < 0:
        # t^-1 mod Phi_n: t^(ord-1) where t^ord = 1 mod Phi_n (ord = n)
        k = (-lo) * (n - 1)
        x = sp.rem(r * sp.Poly(t**k, t), sp.Poly(to_sym(PHI[n]), t, domain='ZZ'))
    return tuple(int(c) for c in x.all_coeffs())
def unit_res(n):
    """residues of +-t^k mod Phi_n"""
    out = set()
    for k in range(2*n):
        for sg in (1, -1):
            out.add(rem({k: sg}, n))
    return out
UR = {n: unit_res(n) for n in PHI}
ONE_R = {n: rem(ONE, n) for n in PHI}
ZERO_R = {n: rem({}, n) if False else (0,) for n in PHI}
def classify(f, n):
    r = rem(f, n)
    if r == ONE_R[n]: return '1'
    if r == (0,) or all(c == 0 for c in r): return '0'
    if r in UR[n]: return 'unit'
    return 'other'
# survey actual bodies
L = rational_all() + general_all() + nested_random(rng, 200) + frontier(rng)
L = [x for x in L if not eqp(x[1][0], x[1][1])]
sv = collections.defaultdict(collections.Counter)
for lab, v, T in L:
    a, c = th(v); b = v[1]; A, B = eig((a, c))
    for n in (1, 3, 4, 6, 10, 12):
        sv[('a', n)][classify(a, n)] += 1
        sv[('b', n)][classify(b, n)] += 1
        sv[('A', n)][classify(A, n)] += 1
    sv[('a mod (t+1)^2 == 1',)][vc.nunit(a) == (1, 0)] += 1
    sv[('eps=b(-1)',)][vc.ev(b, -1)] += 1
    sv[('c(-1)',)][vc.ev(c, -1)] += 1
print('ACTUAL BODIES (%d): residue classes (1 / unit=+-t^k / 0 / other):' % len(L))
for k in sorted(sv, key=str): print('  ', k, dict(sv[k]))
# the formal state
fs = collections.Counter(); notes = []
for trial in range(60):
    mu = rng.choice([x for x in range(-5, 6) if x])
    s = tm(mu)
    k = rng.randint(2, 6)
    E = {0: 1}
    for _ in range(k): E = mul(E, PHI[2])
    E = mul(E, mul(PHI[6], PHI[10]))
    extra = trial % 2 == 1
    if extra: E = mul(E, mul(PHI3, T2P1))       # referee's augmentation: also kill Phi3, Phi4 residues
    E = mul(E, {rng.randint(0, 3): 1, rng.randint(4, 8): rng.choice([1, -1, 2])})
    E = shift(E, -(top(mul(C, E)) + bot(mul(C, E)))//2 - mu)   # centre the support of s C E around 0
    a = add(ONE, mul(sub(s, ONE), mul(C, E))); c = E
    A, B = eig((a, c))
    fs['A=1+sCE'] += eqp(A, add(ONE, mul(s, mul(C, E))))
    fs['B=CE'] += eqp(B, mul(C, E))
    fs['A-sB=1'] += eqp(sub(A, mul(s, B)), ONE)
    fs['gcd(a,c)=1'] += (gcdL(a, c) == {0: 1})
    fs['gcd(A,B)=1'] += (gcdL(A, B) == {0: 1})
    fs['a=1 mod (t+1)^k'] += (nu_poly(sub(a, ONE), PHI[2]) >= k)
    b = add(a, mul(D3, c))
    for n in (1, 3, 4, 6, 10, 12):
        fs['%s a(Phi%d)=%s' % ('aug' if extra else 'codex', n, classify(a, n))] += 1
        fs['%s b(Phi%d)=%s' % ('aug' if extra else 'codex', n, classify(b, n))] += 1
    fs['eps=+1'] += (vc.ev(b, -1) == 1)
    # simultaneous resonance at m = -mu: both ends aligned, unit, budget exhausted
    m = -mu
    nu0 = bot(B) - bot(A); ninf = top(A) - top(B)
    f = sub(A, mul(tm(-m), B))
    straddle = bot(mul(s, mul(C, E))) < 0 < top(mul(s, mul(C, E)))
    if straddle:
        fs['straddle'] += 1
        H = span(A)
        tau0 = max(bot(f) - bot(A), 0); tauinf = max(top(A) - top(f), 0)
        fs['kappa=0'] += (nu0 + ninf == 0)
        fs['m=nu0=-ninf'] += (m == nu0 == -ninf)
        fs['H=tau0+tauinf'] += (H == tau0 + tauinf and isunit(f))
print('FORMAL STATE (60 trials, half with E also divisible by Phi3*Phi4):')
for k in sorted(fs): print('  ', k, fs[k])
