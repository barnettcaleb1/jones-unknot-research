#!/usr/bin/env python3
"""Check the matrix forms of Birman-Brendle, Braids: a survey (arXiv math/0409205v2), Section 4.2, p. 46:
   unreduced  s_i -> I_{i-1} + [[1-t, t], [1, 0]] + I_{n-i-1}           (identical to the note's U)
   reduced    s_i -> I_{i-2} + [[1, -t, 0], [0, -t, 0], [0, -1, 1]] + I_{n-i-2}, -t at (i, i)
and how they relate to the script's R (row i of I_{n-1} replaced by (t, -t, 1)).
Also: is R(mirror w)(t) conjugate to R(w)(1/t) by a fixed matrix (as U is)?"""
from fractions import Fraction as Fr
src = open('$HOME/jones-adversarial-pass/bbb-gap-note/check/final-verify-compute/conv_check.py').read()
exec(src.split("CONVS = {")[0])          # reuse my own Laurent/matrix helpers and words

def BB05R_gen(n, a):
    """BB05 reduced: identity except column i (1-based) = (-t, -t, -1) in rows i-1, i, i+1 (rows outside 1..n-1 dropped)."""
    i = abs(a) - 1
    G = eye(n - 1)
    for r, v in ((i - 1, {1: -1}), (i, {1: -1}), (i + 1, {0: -1})):
        if 0 <= r < n - 1: G[r][i] = v
    if a > 0: return G
    # inverse: G = I + u e_i^T with u = col_i - e_i; G^-1 = I - u e_i^T / (1 + u_i), u_i = -t - 1, 1 + u_i = -t
    H = eye(n - 1)
    for r, v in ((i - 1, {0: -1}), (i, {-1: -1}), (i + 1, {-1: -1})):
        if 0 <= r < n - 1: H[r][i] = v
    return H
def BB05R(w, n): return prod(lambda a: BB05R_gen(n, a), w, n - 1)

for n in (3, 4, 5):
    rel = all(BB05R(u, n) == BB05R(v, n) for i in range(1, n - 1) for u, v in [([i, i + 1, i], [i + 1, i, i + 1])]) \
        and all(BB05R(u, n) == BB05R(v, n) for i in range(1, n) for j in range(i + 2, n) for u, v in [([i, j], [j, i])]) \
        and all(BB05R([i, -i], n) == eye(n - 1) for i in range(1, n))
    D = [[{0: (-1) ** k} if k == j else ZERO for j in range(n - 1)] for k in range(n - 1)]
    sign_conj = all(BB05R_gen(n, a) == mm(mm(D, tr(R_gen(n, a))), D) for i in range(1, n) for a in (i, -i))
    print(f"n={n}: BB05 reduced is a representation: {rel};  BB05 reduced(s_i^+-1) == D * R(s_i^+-1)^T * D, D = diag((-1)^k): {sign_conj}")

M = BB05R(Phi0, 4)
print("BB05 reduced, Phi0 in B4: I at t=-1:", isI(evM(M, -1)), "; not I at 2, 1/2, 3, 1/3:",
      all(not isI(evM(M, x)) for x in (Fr(2), Fr(1, 2), Fr(3), Fr(1, 3))))
MX, MD = minusI(BB05R(X, 4)), minusI(BB05R(D3sq, 4))
print("BB05 reduced: rho(X)-I == (1+t^3)(rho(D3^2)-I):", MX == mapM(lambda p: mul({0: 1, 3: 1}, p), MD),
      "; with (1+t^-3):", MX == mapM(lambda p: mul({0: 1, -3: 1}, p), MD))
print("BB05 reduced: rho(Delta_3^2) in B3 =", [[dict(p) for p in r] for r in BB05R(D3sq, 3)])
print("U: rho(Delta_3^2) in B3 eigen-check: U(D3sq)-I times (t^3-1)^-1 ... entries:", [[dict(sorted(p.items())) for p in r] for r in minusI(U(D3sq, 3))])

# Mirror relation for R: solve C R(s_i)(1/t0) = R(s_i^-1)(t0) C for all i at a numeric t0, check uniqueness/invertibility
def solve_conj(n, t0):
    m = n - 1
    gens = [(evM(R_gen(n, i), 1 / t0), evM(R_gen(n, -i), t0)) for i in range(1, n)]
    # unknowns C[r][c], equations (C A - B C) = 0
    rows = []
    for A, B in gens:
        for r in range(m):
            for c in range(m):
                eq = [Fr(0)] * (m * m)
                for k in range(m):
                    eq[r * m + k] += A[k][c]
                    eq[k * m + c] -= B[r][k]
                rows.append(eq)
    # nullspace by Gaussian elimination over Q
    A = [row[:] for row in rows]; piv = []; R_ = 0
    for col in range(m * m):
        p = next((i for i in range(R_, len(A)) if A[i][col] != 0), None)
        if p is None: continue
        A[R_], A[p] = A[p], A[R_]
        pv = A[R_][col]; A[R_] = [x / pv for x in A[R_]]
        for i in range(len(A)):
            if i != R_ and A[i][col] != 0:
                f = A[i][col]; A[i] = [x - f * y for x, y in zip(A[i], A[R_])]
        piv.append(col); R_ += 1
    free = [c for c in range(m * m) if c not in piv]
    return len(free), free, A, piv
for n in (4, 5):
    t0 = Fr(5, 3)
    dim, free, A, piv = solve_conj(n, t0)
    print(f"n={n}: space of C with C R(s_i)(1/t0) = R(s_i^-1)(t0) C for all i (t0=5/3) has dimension {dim}")
    if dim == 1:
        m = n - 1; sol = [Fr(0)] * (m * m); sol[free[0]] = Fr(1)
        for i, col in enumerate(piv): sol[col] = -A[i][free[0]]
        C = [sol[r * m:(r + 1) * m] for r in range(m)]
        # determinant via fraction Gaussian elimination
        Mx = [r[:] for r in C]; det = Fr(1)
        for c in range(m):
            p = next((i for i in range(c, m) if Mx[i][c] != 0), None)
            if p is None: det = Fr(0); break
            if p != c: Mx[c], Mx[p] = Mx[p], Mx[c]; det = -det
            det *= Mx[c][c]
            for i in range(c + 1, m):
                f = Mx[i][c] / Mx[c][c]; Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[c])]
        print(f"      that C is invertible: {det != 0}")
