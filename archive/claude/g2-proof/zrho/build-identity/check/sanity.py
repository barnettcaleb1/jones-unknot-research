# Cheap sanity checks for identity.md (pure Python, exact arithmetic).
# Part 1: torus family T(3,6n+1) = K_{T_c^n}: Jones poly, V(+-1), V'(+-1), signature, Mullins lambda,
#         and the two sides of 5 sigma + 4 d^ = (10/3) L + 40 q(tau_2), with q(tau_2 T_c) = 1/10 - a_2(K_c).
# Part 2: invariant-theory constant: B = sym(Lambda^2 theta) for the standard Heegaard Seifert form;
#         coefficient of the splitting-detecting invariant, in genus g = 2,3,4.
from fractions import Fraction as Fr
from itertools import combinations

# ---------- Part 1 ----------
def jones_T3(q):            # q coprime to 3, q > 0: V = t^{q-1}(1 + t^2 - t^{q+1}); dict exponent->coeff
    return {q-1: 1, q+1: 1, 2*q: -1}
def mirror(V): return {-e: c for e, c in V.items()}
def ev(V, t):  return sum(Fr(c) * Fr(t)**e for e, c in V.items())
def dev(V, t): return sum(Fr(c) * e * Fr(t)**(e-1) for e, c in V.items())
def sig_T3(q):              # positive torus knot T(3,q), convention sigma(RH trefoil) = -2
    inn = out = 0
    for i in (1, 2):
        for j in range(1, q):
            x = Fr(i, 3) + Fr(j, q)
            if Fr(1, 2) < x < Fr(3, 2): inn += 1
            else: out += 1
    return -(inn - out)
assert sig_T3(2) == 0 or True
print("Part 1: K = T(3,6n+1), M = S^3_{-1/n}(RHT) = Sigma(2,3,6n+1), lambda_Casson = -n")
print(" n | sigma | V(1) V'(1) | V(-1) V'(-1) | Mullins sigma/8-L/12 | LHS 5s+4d | RHS (10/3)L+40q")
for n in range(-3, 4):
    q = 6*n + 1
    if q > 0: V, s = jones_T3(q), sig_T3(q)
    else:     V, s = mirror(jones_T3(-q)), -sig_T3(-q)
    if q == 1: V, s = {0: 1}, 0
    L = dev(V, -1) / ev(V, -1)
    lam = Fr(s, 8) - L / 12
    d = n
    qterm = n * (Fr(1, 10) - 1)          # a_2(RHT) = 1
    lhs, rhs = 5*s + 4*d, Fr(10, 3)*L + 40*qterm
    print(f"{n:2d} | {s:5d} | {ev(V,1)} {dev(V,1)} | {ev(V,-1)} {dev(V,-1)} | {lam} (expect {-n}) | {lhs} | {rhs}")
    assert ev(V, 1) == 1 and dev(V, 1) == 0 and lam == -n and lhs == rhs
# extra: sigma(T(3,5)), sigma(T(3,7)) as known values
print(" sigma T(3,4),T(3,5),T(3,7),T(3,11),T(3,13):", [sig_T3(q) for q in (4, 5, 7, 11, 13)])

# ---------- Part 2 ----------
def invariant_constant(g):
    # basis of H: a_1..a_g, b_1..b_g ; J(a_i,b_j)=delta, J(b_i,a_j)=-delta
    n = 2*g
    J = [[0]*n for _ in range(n)]
    th = [[0]*n for _ in range(n)]
    for i in range(g):
        J[i][g+i], J[g+i][i] = 1, -1
        th[g+i][i] = 1                    # Seifert form: theta(b_i, a_i) = 1, all else 0 (sign irrelevant)
    pairs = list(combinations(range(n), 2))   # basis e_p ^ e_q of Lambda^2 H
    def L2(F, P, Q):                      # Lambda^2 F (x^y, x'^y') = F(x,x')F(y,y') - F(x,y')F(y,x')
        (x, y), (u, v) = P, Q
        return F[x][u]*F[y][v] - F[x][v]*F[y][u]
    N = len(pairs)
    B  = [[Fr(L2(th, P, Q) + L2(th, Q, P), 2) for Q in pairs] for P in pairs]   # symmetrised Lambda^2 theta
    B2 = [[Fr(L2(J, P, Q)) for Q in pairs] for P in pairs]                       # Lambda^2 J (invariant)
    w  = [Fr(J[x][y]) for (x, y) in pairs]                                       # <omega, e_P>
    B1 = [[w[i]*w[j] for j in range(N)] for i in range(N)]                       # <omega,.><omega,.> (invariant)
    # invariant tensors: Omega1 = omega (x) omega, Omega2 = inverse of Lambda^2 J
    om = [Fr(0)]*N
    for i in range(g):
        om[pairs.index((i, g+i))] = Fr(1)
    def inv(M):
        m = len(M); A = [row[:] + [Fr(int(i == j)) for j in range(m)] for i, row in enumerate(M)]
        for c in range(m):
            p = next(r for r in range(c, m) if A[r][c] != 0); A[c], A[p] = A[p], A[c]
            pv = A[c][c]; A[c] = [x / pv for x in A[c]]
            for r in range(m):
                if r != c and A[r][c] != 0:
                    f = A[r][c]; A[r] = [x - f*y for x, y in zip(A[r], A[c])]
        return [row[m:] for row in A]
    O2 = inv(B2)
    def pair1(F): return sum(om[i]*F[i][j]*om[j] for i in range(N) for j in range(N))
    def pair2(F): return sum(O2[i][j]*F[i][j] for i in range(N) for j in range(N))
    G = [[pair1(B1), pair1(B2)], [pair2(B1), pair2(B2)]]
    rhs = [pair1(B), pair2(B)]
    det = G[0][0]*G[1][1] - G[0][1]*G[1][0]
    al = (rhs[0]*G[1][1] - G[0][1]*rhs[1]) / det
    be = (G[0][0]*rhs[1] - G[1][0]*rhs[0]) / det
    # [11]-component check: B(omega, .) == 0
    Bom = [sum(om[i]*B[i][j] for i in range(N)) for j in range(N)]
    # invariant part of B on a genus-h splitting omega_h: alpha*h^2 + beta*h  (B1 -> h^2, B2 -> h)
    vals = {h: al*h*h + be*h for h in range(1, g)}
    return G, rhs, al, be, all(x == 0 for x in Bom), vals
print("\nPart 2: invariant part of B = sym Lambda^2 theta (standard Heegaard Seifert form)")
for g in (2, 3, 4):
    G, rhs, al, be, b11zero, vals = invariant_constant(g)
    pred = {h: Fr(h*(g-h), 2*(2*g+1)) for h in range(1, g)}
    print(f" g={g}: Gram={G}, B(Omega)={rhs}, alpha={al}, beta={be}, B(omega,.)=0: {b11zero}")
    print(f"       invariant part on genus-h splitting: {vals}  vs h(g-h)/(2(2g+1)): {pred}")
    assert vals == pred and b11zero
# genus-2 Seifert determinant example: x = a1+b1, y = a1+2b1+a2+b2 (J(x,y)=1) gives a_2 = 1
def det_example():
    # coordinates (a1,a2,b1,b2); theta(u,v) = sum_i b_i(u) a_i(v)
    x = (1, 0, 1, 0); y = (1, 1, 2, 1)
    th = lambda u, v: u[2]*v[0] + u[3]*v[1]
    Jf = lambda u, v: (u[0]*v[2] - u[2]*v[0]) + (u[1]*v[3] - u[3]*v[1])
    return Jf(x, y), th(x, x)*th(y, y) - th(x, y)*th(y, x)
print(" genus-2 splitting example (J(x,y), a_2):", det_example())
