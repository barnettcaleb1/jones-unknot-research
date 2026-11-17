"""CHECK 1 (INTEGRAL EIGENPAIR).  On actual box vectors: a = A - B, b = A - eB, (ta + (1+t^2)b)/Phi3 = A; raw outer map
X^-m: (A,B) -> (A, (-t)^-m B) (independent rho(X) matrix powers on (a,c)); preferred framing unit of vc.F; Y^N matrix;
star product in eigen-coordinates with e = -t/(1+t^2) as a genuine rational function (sympy), result must be Laurent and
equal the eigenpair of the integral star product; z-composition law; horizontal closure A - (-t)^mu B vs rho(X)^mu and vs
(w1 a + w3 b)/Phi3; ROOTS facts a(1) = a(i) = 1 and gcd(A,B) = gcd(a,c)."""
import sys, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/arb-resonance')
from common import *
rng = random.Random(20261117)
t0 = time.time()
L = rational_all() + general_all() + nested_random(rng, 200) + frontier(rng)
print('library: %d bodies (rational %d, general %d, nested 200, frontier %d)' % (len(L), len(R5), 50, len(L) - len(R5) - 250), flush=True)
cnt = dict(basic=0, outer=0, outer_unit=0, Y=0, Ydet=0, star=0, star_laurent=0, zlaw=0, hclose=0, w13=0, roots=0, gcd=0)
bad = []
def matpow(M, k, s):
    for _ in range(k): s = lp.mvec(M, list(s))
    return tuple(s)
def ival(p, z):  # exact value at a Gaussian integer root of unity z in {1, i, -1, -i}: returns complex with int parts
    re = im = 0
    for e, c in p.items():
        k = e % 4
        if z == 'i':
            v = [(1, 0), (0, 1), (-1, 0), (0, -1)][k]
        else:
            v = (1, 0)
        re += c * v[0]; im += c * v[1]
    return (re, im)
states = []
for lab, v, T in L:
    s = th(v); a, c = s; b = v[1]
    A, B = eig(s)
    ok = eqp(a, sub(A, B)) and eqp(mul(T2P1, b), add(mul(T2P1, A), shift(B, 1))) and eqp(add(shift(a, 1), mul(T2P1, b)), mul(PHI3, A))
    cnt['basic'] += ok
    if not ok: bad.append(('basic', lab))
    # outer map
    for m in rng.sample([-3, -2, -1, 1, 2, 3], 2):
        if eqp(v[0], v[1]): continue
        raw = matpow(lp.Xm if -m >= 0 else lp.Xi, abs(m), s)          # X^-m (a,c)
        Ar, Br = eig(raw)
        ok = eqp(Ar, A) and eqp(Br, mul(tm(-m), B))
        cnt['outer'] += ok
        if not ok: bad.append(('outer', lab, m))
        vF = vc.F(m, v); Af, Bf = eig(th(vF))
        eps = vc.ev(v[1], -1); u = {2*m*(1 - eps): 1}
        ok = eqp(Af, mul(u, A)) and eqp(Bf, mul(u, mul(tm(-m), B)))
        cnt['outer_unit'] += ok
        if not ok: bad.append(('outer_unit', lab, m))
    # Y^N
    N = rng.choice([-3, -2, -1, 1, 2, 3])
    sY = matpow(lp.Ym if N > 0 else lp.Yi, abs(N), s)
    AY, BY = eig(sY)
    r = {-3*N: 1}; k = vc.divexact(sub(r, ONE), PHI3)
    M11 = add(ONE, mul(T2P1, k)); M12 = shift(k, 1); M21 = mul(T2P1, k); M22 = add(ONE, shift(k, 1))
    ok = eqp(AY, add(mul(M11, A), mul(M12, B))) and eqp(BY, add(mul(M21, A), mul(M22, B)))
    cnt['Y'] += ok
    if not ok: bad.append(('Y', lab, N))
    cnt['Ydet'] += eqp(sub(mul(M11, M22), mul(M12, M21)), r)
    # horizontal closure
    mu = rng.randint(-8, 8)
    f1 = tuple(matpow(lp.Xm if mu >= 0 else lp.Xi, abs(mu), s))[0]
    f2 = sub(A, mul(tm(mu), B))
    cnt['hclose'] += eqp(f1, f2)
    if not eqp(f1, f2): bad.append(('hclose', lab, mu))
    w1 = add(shift(ONE, 1), mul(T2P1, tm(mu))); w3 = mul(T2P1, sub(ONE, tm(mu)))
    cnt['w13'] += eqp(add(mul(w1, a), mul(w3, b)), mul(PHI3, f2))
    # ROOTS facts and gcd
    cnt['roots'] += (vc.ev(a, 1) == 1 and ival(a, 'i') == (1, 0) and vc.ev(A, 1) == 1 and vc.ev(a, -1) == 1)
    if not (vc.ev(a, 1) == 1 and ival(a, 'i') == (1, 0)): bad.append(('roots', lab, vc.ev(a, 1), ival(a, 'i')))
    states.append((lab, s, (A, B)))
print('per-body checks done %.1fs' % (time.time() - t0), flush=True)
# gcd(A,B) = gcd(a,c) on a subset (sympy)
for lab, s, (A, B) in rng.sample(states, 200):
    if iszero(B): continue
    g1 = gcdL(A, B); g2 = gcdL(s[0], s[1])
    cnt['gcd'] += (g1 == g2)
    if g1 != g2: bad.append(('gcd', lab, g1, g2))
# star product in eigen-coordinates, e as a rational function
e = -t/(1 + t**2)
npairs = 0
for _ in range(300):
    (l1, s1, (A1, B1)), (l2, s2, (A2, B2)) = rng.sample(states, 2)
    s12 = star_th(s1, s2); A12, B12 = eig(s12)
    SA1, SB1, SA2, SB2 = map(to_sym, (A1, B1, A2, B2))
    fA = laurent_from_sym(SA1*SA2 - e*SB1*SB2)
    fB = laurent_from_sym(SA1*SB2 + SB1*SA2 - (1 + e)*SB1*SB2)
    cnt['star_laurent'] += (fA is not None and fB is not None)
    ok = fA is not None and fB is not None and eqp(fA, A12) and eqp(fB, B12)
    cnt['star'] += ok
    if not ok: bad.append(('star', l1, l2))
    if npairs < 60 and not iszero(B1) and not iszero(B2) and not iszero(A12):
        z1 = SB1/SA1; z2 = SB2/SA2
        lhs = to_sym(B12)/to_sym(A12)
        rhs = (z1 + z2 - (1 + e)*z1*z2)/(1 - e*z1*z2)
        cnt['zlaw'] += (sp.cancel(sp.together(lhs - rhs)) == 0)
        npairs += 1
# off-lattice control: the star formula is NOT integral without B in C*Lambda
ctrl = laurent_from_sym(1*1 - e*1*1)
print('off-lattice control (A_i,B_i) = (1,1): A12 Laurent? ', ctrl is not None)
print('counts:', cnt, 'star pairs 300, zlaw pairs', npairs)
print('failures:', len(bad), bad[:10])
print('time %.1f' % (time.time() - t0))
