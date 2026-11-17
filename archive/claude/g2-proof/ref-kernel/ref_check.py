# ref-kernel sanity checks (exact Laurent arithmetic over Z[A, A^-1]); hand-picked words only, no search.
# (1) Off-by-one test: kernel.md 2.4 / Remark (a) claim kappa_f = [T_c0, f] lies in F_2 (and [I_2, I_2]) for every f in SI.
#     F_k = {rho - I = O(h^k)}, and ord_h at t = -e^h equals the power of Phi_8 = A^4 + 1 dividing rho - I.
#     Test f = T_d^2, d = sigma_3(c0): compare kappa = [(s1 s2)^3, f] with kappa' = [(s1 s2)^6, f] = T_gamma T_{f gamma}^-1.
# (2) Theorem A sign convention: r(c0, g c0)(zeta) = |R_g(zeta)|^2 vs (2D - 1)^2, with D from the transvection model,
#     using kernel.md's convention and the mirrored one.
import cmath, itertools
from collections import defaultdict

def padd(p, q, s=1):
    r = defaultdict(int, p)
    for e, c in q.items(): r[e] += s * c
    return {e: c for e, c in r.items() if c}
def pmul(p, q):
    r = defaultdict(int)
    for e1, c1 in p.items():
        for e2, c2 in q.items(): r[e1 + e2] += c1 * c2
    return {e: c for e, c in r.items() if c}
ONE = {0: 1}; ZERO = {}
DELTA = {2: -1, -2: -1}
N = 5
tab = {1:{1:('d',1),2:('d',2),3:(1,1),4:(1,2),5:(1,1)},
       2:{1:(1,3),2:(1,4),3:('d',3),4:('d',4),5:(1,4)},
       3:{1:('d',1),2:(1,1),3:(1,1),4:(1,5),5:('d',5)},
       4:{1:(1,2),2:('d',2),3:(1,4),4:('d',4),5:(1,4)},
       5:{1:('d',1),2:(1,1),3:('d',3),4:(1,3),5:(1,1)}}
def E(i):
    M = [[ZERO]*N for _ in range(N)]
    for j, (c, t) in tab[i].items():
        M[t-1][j-1] = DELTA if c == 'd' else ONE
    return M
def mm(X, Y):
    Z = [[ZERO]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            acc = {}
            for k in range(N):
                if X[r][k] and Y[k][c]: acc = padd(acc, pmul(X[r][k], Y[k][c]))
            Z[r][c] = acc
    return Z
I5 = [[ONE if r == c else ZERO for c in range(N)] for r in range(N)]
def gen(i, s):   # sigma_i -> A + A^-1 e_i ; sigma_i^-1 -> A^-1 + A e_i
    a, b = ({1: 1}, {-1: 1}) if s > 0 else ({-1: 1}, {1: 1})
    Ei = E(i)
    return [[padd(a if r == c else ZERO, pmul(b, Ei[r][c])) for c in range(N)] for r in range(N)]
G = {(i, s): gen(i, s) for i in range(1, 6) for s in (1, -1)}
def rho(w):
    M = I5
    for g in w: M = mm(M, G[(abs(g), 1 if g > 0 else -1)])
    return M
inv = lambda w: [-g for g in reversed(w)]
def ord_phi8(p):
    if not p: return 10**9
    lo = min(p); hi = max(p)
    coeffs = [p.get(lo + k, 0) for k in range(hi - lo + 1)]   # ascending powers
    k = 0
    while True:   # divide by 1 + A^4 (ascending)
        if len(coeffs) < 5: return k
        q = coeffs[:]; quo = [0]*(len(q) - 4)
        for d in range(len(q) - 4):
            c = q[d]; quo[d] = c; q[d] -= c; q[d+4] -= c
        if any(q): return k
        coeffs = quo; k += 1
def ord_matrix(M):
    return min(ord_phi8(padd(M[r][c], I5[r][c], -1)) for r in range(N) for c in range(N))


z = cmath.exp(1j*cmath.pi/4)
ev = lambda p: sum(c * z**e for e, c in p.items())
vt = [pmul(DELTA, {0: -1}), ONE, ONE, pmul(DELTA, {0: -1}), {4: 1, 0: 1, -4: 1}]   # v~ = (-d, 1, 1, -d, Delta_2)
def R(w):
    M = rho(w); acc = {}
    for k in range(N):
        if M[4][k] and vt[k]: acc = padd(acc, pmul(M[4][k], vt[k]))
    return acc
a = {1:(1,0,0,0),2:(0,1,0,0),3:(0,0,1,0),4:(0,0,0,1),5:(-1,0,-1,0)}
Om = [[0,1,0,0],[-1,0,1,0],[0,-1,0,1],[0,0,-1,0]]
om = lambda x, y: sum(x[r]*Om[r][c]*y[c] for r in range(4) for c in range(4))
def act(w, x, conv):
    for g in reversed(w):
        s = (1 if g > 0 else -1) * conv
        k = s * om(x, a[abs(g)]); x = tuple(x[r] + k*a[abs(g)][r] for r in range(4))
    return x
def det4(m):
    return sum((-1)**sum(1 for i in range(4) for j in range(i+1,4) if p[i] > p[j]) *
               m[0][p[0]]*m[1][p[1]]*m[2][p[2]]*m[3][p[3]] for p in itertools.permutations(range(4)))
def D(w, conv):
    x, y = a[1], a[2]
    return det4([list(c) for c in zip(x, y, act(w, x, conv), act(w, y, conv))])

if __name__ == '__main__':
    # sanity: braid relations and that ord detects identity
    assert mm(G[(1,1)], mm(G[(2,1)], G[(1,1)])) == mm(G[(2,1)], mm(G[(1,1)], G[(2,1)]))
    Tc  = [1, 2]*3
    Tc2 = [1, 2]*6
    f   = [3] + [1, 2]*6 + [-3]                  # T_d^2, d = sigma_3(c0): a separating twist upstairs, in SI
    kap  = Tc  + f + inv(Tc)  + inv(f)           # [(s1 s2)^3, f]   (kernel.md's universal form)
    kap2 = Tc2 + f + inv(Tc2) + inv(f)           # [(s1 s2)^6, f] = T_gamma T_{f gamma}^-1
    print("(1) ord_{A=zeta}(rho - I):")
    print("    [(s1 s2)^3, T_d^2]  ->", ord_matrix(rho(kap)),  "   (claimed in F_2, i.e. >= 2)")
    print("    [(s1 s2)^6, T_d^2]  ->", ord_matrix(rho(kap2)), "   (T_gamma T_{f gamma}^-1)")
    print("    (T_d^2 itself is not tested: exponent sum 12, so the bracket scalar A^-12 = -1 at zeta hides F_1)")
    
    
    words = {"s3 s4 s3^-1 s2": [3,4,-3,2], "s3^3": [3,3,3], "s3^-3": [-3,-3,-3], "s3 s4 s5 s3": [3,4,5,3],
             "(s3 s4^-1)^2 s2^-1": [3,-4,3,-4,-2], "s3^2 s4 s2^-1 s5": [3,3,4,-2,5], "s4 s3^-2 s2 s5^-1 s4": [4,-3,-3,2,-5,4]}
    print("(2) Theorem A, |R_g(zeta)|^2 vs (2D-1)^2 [kernel.md convention | mirrored convention]:")
    for name, w in words.items():
        r = abs(ev(R(w)))**2; d1 = D(w, 1); d2 = D(w, -1)
        print(f"    {name:24s} |R|^2 = {r:7.3f}   D = {d1:+d} -> {(2*d1-1)**2:3d} {'ok' if abs(r-(2*d1-1)**2)<1e-9 else 'MISMATCH'}"
              f"   | mirrored D = {d2:+d} -> {(2*d2-1)**2:3d} {'ok' if abs(r-(2*d2-1)**2)<1e-9 else 'mismatch'}")
    
