"""Seven-sector analysis (Codex WIDTH2-SECTORS) in engineB's module: joint spectral decomposition of the commuting
normalised twists X1 (legs 0,1) and X3 (legs 2,3), eigenvalues 1, -t, t^3 on fusion colours 0, 2, 4.
mod-p tools: eigenbasis B (columns), inverse, block structure; c_ab(U,V) = (w_U B)_block . (B^-1 u_V)_block."""
import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import rho2
def evt(poly, t, P): return sum(c * pow(t, e % (P - 1), P) for e, c in poly.items()) % P
def mm(A, B, P):
    Bt = list(zip(*B)); return [[sum(a * b for a, b in zip(r, c)) % P for c in Bt] for r in A]
def sub_scalar(A, lam, P):
    n = len(A); return [[(A[i][j] - (lam if i == j else 0)) % P for j in range(n)] for i in range(n)]
def scal(A, s, P): return [[x * s % P for x in r] for r in A]
def rank(A, P):
    M = [r[:] for r in A]; n = len(M); m = len(M[0]); rk = 0; col = 0
    for col in range(m):
        piv = next((i for i in range(rk, n) if M[i][col]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        iv = pow(M[rk][col], P - 2, P)
        M[rk] = [x * iv % P for x in M[rk]]
        for i in range(n):
            if i != rk and M[i][col]:
                f = M[i][col]; M[i] = [(x - f * y) % P for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
def colspace_basis(A, P):
    """basis (list of column vectors) of the column space of A"""
    n = len(A); cols = [[A[i][j] for i in range(n)] for j in range(n)]
    basis = []
    for c in cols:
        test = basis + [c]
        M = [[v[i] for v in test] for i in range(n)]
        if rank(M, P) == len(test): basis.append(c)
    return basis
def inv(A, P):
    n = len(A); M = [r[:] + [1 if i == j else 0 for j in range(n)] for i, r in enumerate(A)]
    for col in range(n):
        piv = next(i for i in range(col, n) if M[i][col])
        M[col], M[piv] = M[piv], M[col]
        iv = pow(M[col][col], P - 2, P); M[col] = [x * iv % P for x in M[col]]
        for i in range(n):
            if i != col and M[i][col]:
                f = M[i][col]; M[i] = [(x - f * y) % P for x, y in zip(M[i], M[col])]
    return [r[n:] for r in M]
COL = {0: 0, 1: 2, 2: 4}
def setup(t, P):
    MT, VT, PHIT = rho2.normalised()
    X1 = [[evt(x, t, P) for x in r] for r in MT['x1']]
    X3 = [[evt(x, t, P) for x in r] for r in MT['x3']]
    lam = [1, (-t) % P, pow(t, 3, P)]
    I = [[1 if i == j else 0 for j in range(9)] for i in range(9)]
    def proj(X, a):
        R = I
        for b in range(3):
            if b == a: continue
            R = mm(R, scal(sub_scalar(X, lam[b], P), pow((lam[a] - lam[b]) % P, P - 2, P), P), P)
        return R
    P1 = [proj(X1, a) for a in range(3)]; P3 = [proj(X3, b) for b in range(3)]
    E = {}; ranks = {}
    for a in range(3):
        for b in range(3):
            E[(COL[a], COL[b])] = mm(P1[a], P3[b], P)
            ranks[(COL[a], COL[b])] = rank(E[(COL[a], COL[b])], P)
    # eigenbasis
    cols = []; blocks = {}
    for key in sorted(E):
        bs = colspace_basis(E[key], P)
        blocks[key] = list(range(len(cols), len(cols) + len(bs)))
        cols.extend(bs)
    Bm = [[cols[j][i] for j in range(9)] for i in range(9)]
    Binv = inv(Bm, P)
    return {'E': E, 'ranks': ranks, 'B': Bm, 'Binv': Binv, 'blocks': blocks, 'lam': lam}
if __name__ == '__main__':
    P = (1 << 61) - 1; t = random.Random(1).randrange(2, P - 1)
    S = setup(t, P)
    print('joint ranks', {k: v for k, v in S['ranks'].items() if v}, 'zero sectors', [k for k, v in S['ranks'].items() if not v])
    print('blocks', S['blocks'])
