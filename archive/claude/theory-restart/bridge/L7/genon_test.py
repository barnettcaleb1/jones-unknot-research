"""Test the GENON IDENTITY  |V_L(zeta_10)| = |Z_Fib(Sigma_2(L))| / |Z_Fib(S^3)|  numerically.
Kauffman bracket via 4-ended tangle algebra (conventions of tools/jq_tangle.py), Fib modular data via SL(2,Z) rep.
"""
import cmath, math, itertools
import numpy as np

def bracket_ops(A):
    d = -A**2 - A**-2
    def add(p, q): return (d*p[0]*q[0] + p[0]*q[1] + p[1]*q[0], p[1]*q[1])
    def comp(p, q): return (p[0]*q[0], p[0]*q[1] + p[1]*q[0] + d*p[1]*q[1])
    def vert(a): return (A**a, ((-A**-3)**a - A**a)/d)
    def N(p): return p[0]*d + p[1]*d**2
    def D(p): return p[0]*d**2 + p[1]*d   # denominator closure
    return d, add, comp, vert, N, D

def absV_rational(cf, A):
    """|V| of numerator closure of rational tangle with regular continued fraction cf=[a1,...,ak] = a1+1/(a2+...)."""
    d, add, comp, vert, N, D = bracket_ops(A)
    INF = (1, 0); ZERO = (0, 1)
    one = vert(1)
    def horiz(a):
        T = ZERO
        if a >= 0:
            for _ in range(a): T = add(T, one)
        else:
            m = vert(-1)
            for _ in range(-a): T = add(T, m)
        return T
    # build from inside: fraction f -> f + a  (add horiz(a)),  f -> 1/(b + 1/f) (comp vert(b))
    k = len(cf)
    T = horiz(cf[-1]); frac_is_recip = False
    # T has fraction a_k. next: a_{k-1} + 1/a_k : need 1/T then add. 1/(b+1/f) via comp gives reciprocal form.
    # Use: a_{k-1} + 1/f = rotate? Instead build with alternating ops on reciprocals:
    # f_k = a_k ; g = 1/f_k ... we track T with fraction F and use identity 1/(a + 1/F) = comp(T, vert(a)).
    # Let r_k = 1/a_k = comp(INF, vert(a_k)). Then r_{k-1} := 1/(a_{k-1} + r_k)?? that is 1/(a + 1/(1/r)) -- need a + r, not a + 1/r.
    # So alternate: F_k = a_k (horiz). F_{k-1} = a_{k-1} + 1/F_k. Write 1/F_k = comp-construct: 1/(0 + 1/F_k)= comp(T,vert(0)) is identity. Hmm.
    # Cleaner: rational tangle of [a1,...,ak] = horiz(a1) + R(1/[a2..ak]) and R(1/x) = comp-rotation. Use 1/[a2,...,ak] = 1/(a2 + 1/[a3..]) = comp(R([a3..]) , vert(a2)) since comp(T, vert(b)) has fraction 1/(b + 1/F(T)).
    def R(c):
        if len(c) == 0: return INF            # fraction infinity, so 1/(b+1/inf) = 1/b
        if len(c) == 1: return horiz(c[0])
        inner = R(c[2:])                        # fraction [a3..]
        recip = comp(inner, vert(c[1]))         # fraction 1/(a2 + 1/[a3..]) = 1/[a2,a3..]
        return add(horiz(c[0]), recip)          # a1 + 1/[a2..]
    T = R(list(cf))
    return abs(N(T))/abs(d), N(T), d

def cf_of(p, q):
    out = []
    while q:
        a = p // q; out.append(a); p, q = q, p - a*q
    return out

# ---- Fibonacci modular data ----
phi = (1 + 5**0.5)/2
def fib_data(theta_tau):
    dims = np.array([1.0, phi]); Dg = math.sqrt(1 + phi**2)
    S = np.array([[1, phi], [phi, -1]])/Dg
    T = np.diag([1, theta_tau])
    return dims, Dg, S, T

def negcf(p, q):
    """p/q = b1 - 1/(b2 - 1/(...)) with b_i >= 2 (Hirzebruch-Jung) for p>q>0."""
    out = []
    while q:
        b = -(-p // q)  # ceil
        out.append(b); p, q = q, b*q - p
    return out

def absZ_lens(p, q, theta_tau):
    dims, Dg, S, T = fib_data(theta_tau)
    M = S.copy()
    for b in negcf(p, q):
        M = M @ np.linalg.matrix_power(T, b) if b >= 0 else M @ np.linalg.matrix_power(np.linalg.inv(T), -b)
        M = M @ S
    return abs(M[0, 0]) / S[0, 0]

def absV_pretzel(ps, A):
    d, add, comp, vert, N, D = bracket_ops(A)
    T = (0, 1)
    for p in ps: T = add(T, vert(p))
    return abs(N(T))/abs(d)

def absZ_seifert_keychain(fs, theta_tau):
    """Surgery on unknot (framing 0) with meridians of integer framings fs; ratio |Z(M)|/|Z(S^3)| up to the
    overall normalisation, calibrated below."""
    dims, Dg, S, T = fib_data(theta_tau)
    tot = 0
    for c in range(2):
        term = S[0, c]**(2 - len(fs))
        for f in fs:
            Tf = np.linalg.matrix_power(T, f) if f >= 0 else np.linalg.matrix_power(np.linalg.inv(T), -f)
            term *= (S @ Tf @ S)[0, c]
        tot += term
    return abs(tot)

if __name__ == '__main__':
    t = cmath.exp(1j*math.pi/5)          # primitive 10th root
    A = t**(-0.25)
    for th_name, th in [('Fib', cmath.exp(4j*math.pi/5)), ('Fib-bar', cmath.exp(-4j*math.pi/5))]:
        print('=== 2-bridge knots, category', th_name)
        bad = 0
        for p in range(3, 40, 2):
            for q in range(1, p):
                if math.gcd(p, q) != 1: continue
                v, _, _ = absV_rational(cf_of(p, q), A)
                z = absZ_lens(p, q, th)
                if abs(v - z) > 1e-9: bad += 1
                if p <= 9: print(f'  K({p}/{q}): |V(z10)|={v:.6f}  |Z_Fib(L(p,q))|/|Z(S3)|={z:.6f}')
        print('  mismatches for odd p<40:', bad)
