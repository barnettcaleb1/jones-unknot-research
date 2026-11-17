"""Independent implementation of the regular reduced-axis model of ft_integral_referee.md (Sections 1-4),
used by the note's Section 6.  Checks the local root facts and evaluates actual bodies in V1 x V2.

Two evaluations:
  * generic numeric q (complex, generic), s = sqrt(q+1/q): compare b/a of each body with the TL3 (Kauffman) b/a;
  * exact root q=i, s=0 (Gaussian integers): check the body operator is c*(Id x Pi_w1 + (-1)^n0 Id x Pi_odd).
"""
import numpy as np, itertools, sys, json

def modules(q, s):
    # V1: u+ (index 0, wt 1), u- (index 1, wt -1); E u- = u+, F u+ = u-
    E1 = np.zeros((2, 2), complex); F1 = np.zeros((2, 2), complex)
    E1[0, 1] = 1; F1[1, 0] = 1
    K1 = np.diag([q, 1 / q]).astype(complex)
    w1 = [1, -1]
    # V2: w0 (wt 2), w1 (wt 0), w2 (wt -2); E w1 = s w0, E w2 = s w1, F w0 = s w1, F w1 = s w2
    E2 = np.zeros((3, 3), complex); F2 = np.zeros((3, 3), complex)
    E2[0, 1] = s; E2[1, 2] = s; F2[1, 0] = s; F2[2, 1] = s
    K2 = np.diag([q ** 2, 1, q ** -2]).astype(complex)
    w2 = [2, 0, -2]
    return dict(E={1: E1, 2: E2}, F={1: F1, 2: F2}, K={1: K1, 2: K2}, wt={1: w1, 2: w2}, dim={1: 2, 2: 3})

def qint(n, q): return (q ** n - q ** -n) / (q - 1 / q)
def qfact(n, q):
    r = 1
    for k in range(1, n + 1): r *= qint(k, q)
    return r

def Rmat(M, a, b, q):
    """R_ab = D_ab sum_n q^{n(n-1)/2}(q-q^-1)^n/[n]! E^n x F^n  (ft_integral sec 3)"""
    da, db = M['dim'][a], M['dim'][b]
    D = np.diag([q ** (M['wt'][a][i] * M['wt'][b][j] / 2) for i in range(da) for j in range(db)]).astype(complex)
    S = np.zeros((da * db, da * db), complex)
    En = np.eye(da, dtype=complex); Fn = np.eye(db, dtype=complex)
    for n in range(0, min(a, b) + 1):
        S += q ** (n * (n - 1) / 2) * (q - 1 / q) ** n / qfact(n, q) * np.kron(En, Fn)
        En = M['E'][a] @ En; Fn = M['F'][b] @ Fn
    return D @ S

def flip(da, db):
    P = np.zeros((da * db, da * db), complex)
    for i in range(da):
        for j in range(db): P[j * da + i, i * db + j] = 1
    return P

def Bmat(M, a, b, q):
    return flip(M['dim'][a], M['dim'][b]) @ Rmat(M, a, b, q)

def coprod(M, a, b):
    E = np.kron(M['E'][a], M['K'][b]) + np.kron(np.eye(M['dim'][a]), M['E'][b])
    F = np.kron(M['F'][a], np.eye(M['dim'][b])) + np.kron(np.linalg.inv(M['K'][a]), M['F'][b])
    K = np.kron(M['K'][a], M['K'][b])
    return E, F, K

def cupcap2(q):
    coev = np.zeros(9, complex); coev[0 * 3 + 2] = q ** 2; coev[1 * 3 + 1] = -q ** 2; coev[2 * 3 + 0] = 1
    ev = np.zeros(9, complex); ev[0 * 3 + 2] = 1; ev[1 * 3 + 1] = -q ** -2; ev[2 * 3 + 0] = q ** -2
    return coev, ev

def ip_maps(q, s):
    d = q ** 2 + 1 + q ** -2
    i = np.zeros((6, 2), complex)     # V1 -> V1 x V2 ; index u*3+w
    i[0 * 3 + 1, 0] = q ** 2; i[1 * 3 + 0, 0] = -s
    i[1 * 3 + 1, 1] = -1; i[0 * 3 + 2, 1] = q * s
    p = np.zeros((2, 6), complex)
    p[0, 0 * 3 + 1] = 1 / d; p[0, 1 * 3 + 0] = -s / (q * d)
    p[1, 1 * 3 + 1] = -q ** -2 / d; p[1, 0 * 3 + 2] = s / d
    return i, p

# ---------- body evaluation in V1 x V2^{x k} by Morse sweep ----------
def apply_local(vec, dims, pos, op, nin, nout_dims):
    """vec: tensor with shape dims; op acts on factors pos..pos+nin-1 (matrix (prod out) x (prod in));
    returns tensor with those factors replaced by nout_dims"""
    T = vec
    din = dims[pos:pos + nin]
    T = np.moveaxis(T, list(range(pos, pos + nin)), list(range(len(dims) - nin, len(dims))))
    sh = T.shape[:len(dims) - nin]
    T = T.reshape(sh + (int(np.prod(din)) if din else 1,))
    T = T @ op.T
    T = T.reshape(sh + tuple(nout_dims))
    nd = len(sh) + len(nout_dims)
    T = np.moveaxis(T, list(range(len(sh), nd)), list(range(pos, pos + len(nout_dims))))
    newdims = dims[:pos] + list(nout_dims) + dims[pos + nin:]
    return T, newdims

def body_operator(Bword, q, s, sign_x=+1):
    """Operator of the body on V1 x V2 (axis at 0, the arc's V2 strand at 1).
    x_s (s>=1): B22^{sign_x}; y_s: inverse.  x0: full twist T^{sign_x}; y0: inverse.  l/r: coev; u: ev."""
    M = modules(q, s)
    B22 = Bmat(M, 2, 2, q); B22i = np.linalg.inv(B22)
    B12 = Bmat(M, 1, 2, q); B21 = Bmat(M, 2, 1, q)
    T = B21 @ B12; Ti = np.linalg.inv(T)
    coev, ev = cupcap2(q)
    toks = [(t[0], int(t[1:])) for t in Bword.split('.') if t]
    cols = []
    for basis in range(6):
        v = np.zeros(6, complex); v[basis] = 1
        T_ = v.reshape(2, 3); dims = [2, 3]
        for c, k in toks:
            if c in 'xy':
                if k == 0:
                    op = T if (c == 'x') == (sign_x > 0) else Ti
                    T_, dims = apply_local(T_, dims, 0, op, 2, [2, 3])
                else:
                    op = B22 if (c == 'x') == (sign_x > 0) else B22i
                    T_, dims = apply_local(T_, dims, k, op, 2, [3, 3])
            elif c in 'lr':
                # insert V2 x V2 coev at strand positions k, k+1 (half-positions k-1,k -> tensor factors k, k+1)
                T_, dims = apply_local(T_, dims, k, coev.reshape(9, 1), 0, [3, 3])
            elif c == 'u':
                T_, dims = apply_local(T_, dims, k, ev.reshape(1, 9), 2, [])
        assert dims == [2, 3], dims
        cols.append(T_.reshape(6))
    return np.array(cols).T

def channels(beta, q, s):
    i, p = ip_maps(q, s)
    P1 = i @ p; P3 = np.eye(6) - P1
    a = np.trace(beta @ P1) / np.trace(P1)
    b = np.trace(beta @ P3) / np.trace(P3)
    resid = np.linalg.norm(beta - a * P1 - b * P3)
    return a, b, resid
