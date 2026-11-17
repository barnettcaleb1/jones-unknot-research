"""R2 referee library (independent of Codex's gate scripts and of engineB's exact_sectors.py).
Reads ONLY rho2_matrices.json for the module; lp.J (flat_search bracket) is the independent oracle."""
import json, sys
import sympy as sp
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp

JSON = '/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/collab/data/engineB/rho2_matrices.json'
t = sp.symbols('t')
D = json.load(open(JSON))

def L_of(entry):
    """[[exp,coeff],...] -> dict"""
    out = {}
    for e, c in entry:
        out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}

M = {L: [[L_of(D['M'][L][i][j]) for j in range(9)] for i in range(9)] for L in D['M']}
V0 = [L_of(x) for x in D['V']['l1.l1']]
PHI = [L_of(x) for x in D['PHI']['u2.u2']]

# --- Laurent dict arithmetic ---
def padd(p, q, c=1):
    r = dict(p)
    for e, v in q.items():
        r[e] = r.get(e, 0) + c * v
    return {e: v for e, v in r.items() if v}
def pmul(p, q):
    r = {}
    for e, a in p.items():
        for f, b in q.items():
            r[e + f] = r.get(e + f, 0) + a * b
    return {e: v for e, v in r.items() if v}
def mat_vec(A, v):
    out = []
    for i in range(9):
        acc = {}
        for j in range(9):
            if A[i][j] and v[j]:
                for e, a in A[i][j].items():
                    for f, b in v[j].items():
                        acc[e + f] = acc.get(e + f, 0) + a * b
        out.append({e: c for e, c in acc.items() if c})
    return out
def covec_mat(w, A):
    out = []
    for j in range(9):
        acc = {}
        for i in range(9):
            if w[i] and A[i][j]:
                for e, a in w[i].items():
                    for f, b in A[i][j].items():
                        acc[e + f] = acc.get(e + f, 0) + a * b
        out.append({e: c for e, c in acc.items() if c})
    return out
def dot(w, v):
    acc = {}
    for a, b in zip(w, v):
        if a and b:
            for e, x in a.items():
                for f, y in b.items():
                    acc[e + f] = acc.get(e + f, 0) + x * y
    return {e: c for e, c in acc.items() if c}
def div1pt(p, n):
    """exact division by (1+t)^n of a Laurent dict"""
    for _ in range(n):
        if not p: return {}
        lo, hi = min(p), max(p)
        r = dict(p); q = {}
        for e in range(lo, hi):
            c = r.get(e, 0)
            if c:
                q[e] = c; r[e] = 0; r[e + 1] = r.get(e + 1, 0) - c
        r = {e: c for e, c in r.items() if c}
        if r: raise ArithmeticError('not divisible by 1+t')
        p = q
    return p
def S(p):
    return sum(c * t**e for e, c in p.items()) if p else sp.Integer(0)
def Smat(A):
    return sp.Matrix(9, 9, lambda i, j: S(A[i][j]))

def words(W):
    return [x for x in W.split('.') if x] if isinstance(W, str) else list(W)

def apply_word(W, v):
    for L in words(W):
        v = mat_vec(M[L], v)
    return v

def F_raw_direct(W):
    """raw invariant t^2 PHI.rho(W).V0/(1+t)^4 by direct letter-by-letter matrix action (no projectors)"""
    v = apply_word(W, V0)
    y = dot(PHI, v)
    y = div1pt(y, 4)
    return {e + 2: c for e, c in y.items()}

def body(Vw, Uw, m, n):
    mid = (['x1'] * (2 * m) if m >= 0 else ['y1'] * (-2 * m)) + (['x3'] * (2 * n) if n >= 0 else ['y3'] * (-2 * n))
    return words(Vw) + mid + words(Uw)

def halfword(W):
    return 's.l1.l1.' + '.'.join(W) + '.u2.u2'

def normalize(F):
    return lp.normalize(F)
