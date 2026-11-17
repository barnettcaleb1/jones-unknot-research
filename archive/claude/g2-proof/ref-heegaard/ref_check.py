"""Referee sanity check (single identities only): is the rank-one projector P_s of T_s
B-symmetric for a curve s that is not reflection-symmetric?  Builder's note claims
B(v_s, x) = 0 <=> P_s x = 0 with B the BILINEAR form.  Expect: true for s0 = boundary{1,2,3},
false for s = sigma_3(s0); correct statement uses v_{r(s)}, r = reflection (sigma_i -> sigma_i^{-1})."""
import numpy as np, itertools
N = 6
def nc(pts):
    if not pts: return [dict()]
    out = []; a = pts[0]
    for k in range(1, len(pts), 2):
        b = pts[k]
        for mi in nc(pts[1:k]):
            for mo in nc(pts[k+1:]):
                m = {a: b, b: a}; m.update(mi); m.update(mo); out.append(m)
    return out
BASIS = [tuple(m[i] for i in range(N)) for m in nc(list(range(N)))]
IDX = {m: k for k, m in enumerate(BASIS)}
C = (1, 0, 3, 2, 5, 4)
def loops(m1, m2):
    seen, cnt = set(), 0
    for s in range(N):
        if s in seen: continue
        cnt += 1; x, use1 = s, True
        while True:
            seen.add(x); x = m1[x] if use1 else m2[x]; use1 = not use1
            if x == s and use1: break
            seen.add(x)
    return cnt
def e_act(i, m):
    if m[i] == i + 1: return 1, m
    a, b = m[i], m[i+1]; new = list(m)
    new[i], new[i+1] = i+1, i; new[a], new[b] = b, a
    return 0, tuple(new)
A = 1.37 + 0.0j          # generic real A: B real symmetric, rho real
d = -A*A - 1/(A*A)
G = np.array([[d**loops(m, n) for n in BASIS] for m in BASIS])
def E(i):
    M = np.zeros((5,5), dtype=complex)
    for j, m in enumerate(BASIS):
        k, m2 = e_act(i, m); M[IDX[m2], j] += d**k
    return M
def S(i, inv=False):
    a = 1/A if inv else A
    return a*np.eye(5) + (1/a)*E(i)
def W(word):  # word letters +-(i+1); product left to right as matrices
    M = np.eye(5, dtype=complex)
    for g in word: M = M @ S(abs(g)-1, g < 0)
    return M
print("e_i B-symmetric:", all(np.allclose(G @ E(i), E(i).T @ G) for i in range(5)))
T0 = W([1,2]*3)   # twist about s0 = boundary{1,2,3}
def proj(T):
    P = (T - A**-6*np.eye(5)) / (A**6 - A**-6)
    return P
for name, g in [("s0", []), ("sigma3(s0)", [3]), ("sigma3 sigma2^-1 (s0)", [3,-2])]:
    g_m = W(g); Ts = g_m @ T0 @ np.linalg.inv(g_m); P = proj(Ts)
    rk = np.linalg.matrix_rank(P, tol=1e-8)
    idem = np.allclose(P @ P, P)
    Bsym = np.allclose(G @ P, P.T @ G)
    # v_s = image of P; functional killing ker P
    u, sv, vh = np.linalg.svd(P); v_s = u[:, 0]
    # mirrored curve r(s): word g with every letter inverted
    gr = W([-x for x in g]); v_rs = gr @ (proj(T0) @ u[:,0])  # any vector in image of P_{s0} transported
    v_rs = gr @ np.linalg.svd(proj(T0))[0][:,0]
    # test: P x = 0  <=>  B(w, x) = 0 for w = v_s vs w = v_rs ; use the kernel of P (4-dim)
    ker = np.linalg.svd(P)[2][1:].conj().T   # columns span ker P
    Bvs_on_ker = np.abs(v_s @ G @ ker).max()
    Bvrs_on_ker = np.abs(v_rs @ G @ ker).max()
    print(f"{name:24s} rank P={rk} idempotent={idem} B-symmetric={Bsym} "
          f"max|B(v_s,ker P)|={Bvs_on_ker:.2e} max|B(v_rs,ker P)|={Bvrs_on_ker:.2e}")
# plat bracket sanity: B(c, rho(s2 s4) c) = A^6 delta
c = np.zeros(5); c[IDX[C]] = 1
print("B(c,rho(s2s4)c) - A^6 delta =", abs(c @ G @ (W([2,4]) @ c) - A**6*d))

# bar-symmetry: v_s(1/A) should be parallel to v_{r(s)}(A)  (r = letterwise inversion of the word)
def vs_at(Aval, g):
    global A, d, G
    A = Aval; d = -A*A - 1/(A*A)
    G = np.array([[d**loops(m, n) for n in BASIS] for m in BASIS])
    T0 = W([1,2]*3); gm = W(g); P = proj(gm @ T0 @ np.linalg.inv(gm))
    return np.linalg.svd(P)[0][:,0]
for g in ([3], [3,-2], [2,3,-4]):
    a = 1.37
    v_bar = vs_at(1/a, g)             # coefficients of v_s evaluated at 1/A
    v_r = vs_at(a, [-x for x in g])   # v_{r(s)} at A
    par = np.linalg.matrix_rank(np.vstack([v_bar, v_r]), tol=1e-9) == 1
    print(f"g={g}: bar(v_s) parallel to v_(r s): {par}")
