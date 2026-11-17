"""Exact checks of TL branching / pullback / scalar claims (Kauffman bracket normalization).
sigma_i -> A*1 + A^-1 e_i ; delta = -A^2 - A^-2.  Cell (link-state) modules W(n,j), j = #through strands.
Exact arithmetic over Q at rational A (generic enough for n<=6: quantum integers nonzero)."""
from fractions import Fraction as F
import itertools, random, sys

def link_states(n, j):
    """all planar link states on n points with j defects; state = tuple p, p[i]=partner or -1 (defect)."""
    out = []
    def rec(i, p, stack):
        # stack: open arc starts not yet closed; defects can't be enclosed by arcs
        if i == n:
            if not stack and p.count(-1) == j:
                out.append(tuple(p))
            return
        # option 1: open an arc at i
        rec(i+1, p+[None], stack+[i])
        # option 2: close the most recent open arc
        if stack:
            a = stack[-1]
            q = p[:] + [a]
            q[a] = i
            rec(i+1, q, stack[:-1])
        # option 3: defect at i (only if no open arc, else the defect is enclosed)
        if not stack:
            rec(i+1, p+[-1], stack)
    rec(0, [], [])
    return out

def e_action(n, j, A):
    states = link_states(n, j)
    idx = {s: k for k, s in enumerate(states)}
    d = -A*A - 1/(A*A)
    mats = []
    for i in range(n-1):
        M = [[F(0)]*len(states) for _ in states]
        for c, s in enumerate(states):
            s = list(s)
            a, b = s[i], s[i+1]
            if a == i+1:  # arc (i,i+1)
                M[c][c] += d
                continue
            if a == -1 and b == -1:
                continue  # zero in cell module
            t = s[:]
            if a != -1 and b != -1:
                t[a] = b; t[b] = a
            elif a != -1 and b == -1:
                t[a] = -1
            elif a == -1 and b != -1:
                t[b] = -1
            t[i] = i+1; t[i+1] = i
            M[idx[tuple(t)]][c] += 1
        mats.append(M)
    return states, mats

def mat_mul(X, Y):
    n, m, p = len(X), len(Y), len(Y[0])
    return [[sum(X[r][k]*Y[k][c] for k in range(m)) for c in range(p)] for r in range(n)]

def ident(n):
    return [[F(1) if r == c else F(0) for c in range(n)] for r in range(n)]

def add(X, Y, a=F(1), b=F(1)):
    return [[a*X[r][c] + b*Y[r][c] for c in range(len(X[0]))] for r in range(len(X))]

class Rep:
    def __init__(self, n, j, A):
        self.n, self.j, self.A = n, j, A
        self.states, self.e = e_action(n, j, A)
        self.dim = len(self.states)
        I = ident(self.dim)
        self.s = [add(I, E, A, 1/A) for E in self.e]
        self.si = [add(I, E, 1/A, A) for E in self.e]
    def word(self, w):
        M = ident(self.dim)
        for g in w:  # g = +k or -k, generator sigma_{|k|} (1-based)
            M = mat_mul(M, self.s[g-1] if g > 0 else self.si[-g-1])
        return M

def tr(M):
    return sum(M[i][i] for i in range(len(M)))

def is_scalar(M):
    lam = M[0][0]
    return all(M[r][c] == (lam if r == c else 0) for r in range(len(M)) for c in range(len(M))), lam

def full_twist(n):
    d = list(range(1, n))  # sigma_1..sigma_{n-1}
    return d * n  # (s1...s_{n-1})^n = Delta^2

def report(A):
    print(f"=== A = {A} ===")
    W60, W51, W53, W55 = Rep(6,0,A), Rep(5,1,A), Rep(5,3,A), Rep(5,5,A)
    W40, W42, W31, W62 = Rep(4,0,A), Rep(4,2,A), Rep(3,1,A), Rep(6,2,A)
    print("dims W60,W51,W53,W40,W42,W31,W62:", W60.dim, W51.dim, W53.dim, W40.dim, W42.dim, W31.dim, W62.dim)
    # e1 == e3 on W(4,0)
    print("e1 == e3 on W(4,0):", W40.e[0] == W40.e[2])
    # Delta^2 scalars vs predicted (-1)^(j+n) A^(j^2+2j-3n)
    for R in (W60, W51, W53, W55, W40, W42, W31, W62):
        ok, lam = is_scalar(R.word(full_twist(R.n)))
        pred = (-1)**(R.j+R.n) * A**(R.j*R.j+2*R.j-3*R.n)
        print(f"Delta^2 on W({R.n},{R.j}): scalar={ok}, equals predicted (-1)^(j+n)A^(j^2+2j-3n): {lam == pred}, exponent {R.j*R.j+2*R.j-3*R.n}")
    # sphere relation x = s1 s2 s3 s4 s5 s5 s4 s3 s2 s1 on W(6,0)
    x = [1,2,3,4,5,5,4,3,2,1]
    ok, lam = is_scalar(W60.word(x))
    print("sphere-relation braid acts on W(6,0) as scalar:", ok, "lambda==A^-6 ?", lam == A**-6, "lambda==A^6?", lam == A**6)
    ok2, _ = is_scalar(W62.word(x))
    print("sphere-relation braid scalar on W(6,2)?", ok2)
    # Delta_5^2 (strands 1..5) on W(6,0): scalar?
    ok, lam = is_scalar(W60.word(full_twist(5)))
    print("Delta_5^2 on W(6,0) scalar:", ok, "== A^-12:", lam == A**-12)
    # random-word trace identities
    random.seed(1)
    bad = {"6,0|B5 vs 5,1": 0, "5,1|B4 vs 4,0+4,2": 0, "4,0 vs 3,1 pullback": 0, "4,0 vs 4,2 iso?": 0}
    for trial in range(60):
        L = random.randint(1, 14)
        w5 = [random.choice([1,2,3,4,-1,-2,-3,-4]) for _ in range(L)]
        if tr(W60.word(w5)) != tr(W51.word(w5)): bad["6,0|B5 vs 5,1"] += 1
        w4 = [random.choice([1,2,3,-1,-2,-3]) for _ in range(L)]
        if tr(W51.word(w4)) != tr(W40.word(w4)) + tr(W42.word(w4)): bad["5,1|B4 vs 4,0+4,2"] += 1
        pw = [ (1 if abs(g)==3 else abs(g)) * (1 if g>0 else -1) for g in w4]
        if tr(W40.word(w4)) != tr(W31.word(pw)): bad["4,0 vs 3,1 pullback"] += 1
    print("trace mismatches over 60 random words:", bad)
    # note: equal characters on all words of B5 => isomorphic semisimple reps (TL semisimple at this A)

if __name__ == "__main__":
    for A in (F(3,2), F(5,7)):
        report(A)
