# Elementary (no Brownawell-Masser) computation of the GLOBAL unit locus of a twist family,
# by exponent-coincidence linear algebra. Test case: L2's twist2 family
#   delta^2 <D(n1,n2)> = (delta^2-1)[ -A^{n1-n2} + (-1)^{n1} A^{-3n1-n2} + (-1)^{n2} A^{n1+3n2} ]
#                        + (-1)^{n1+n2} A^{3(n2-n1)},     delta^2 = A^4 + 2 + A^-4.
# Unit <=> delta^2<D> - sig * delta^2 * A^m == 0 for some sign sig, integer m.  Variables v=(n1,n2,m).
from fractions import Fraction as Fr
from itertools import combinations
import collections

def terms(sig):
    T = []
    # (coef, e0, w (coeffs of n1,n2,m), s (parity character exponents on n1,n2,m))
    for d, c in ((4,1),(0,1),(-4,1)):           # delta^2 - 1 = A^4 + 1 + A^-4
        T.append((-c, d, (1,-1,0), (0,0,0)))
        T.append(( c, d, (-3,-1,0), (1,0,0)))
        T.append(( c, d, (1,3,0), (0,1,0)))
    T.append((1, 0, (-3,3,0), (1,1,0)))
    for d, c in ((4,1),(0,2),(-4,1)):           # - sig * delta^2 * A^m
        T.append((-sig*c, d, (0,0,1), (0,0,0)))
    return T

def evaluate_zero(T, v):
    acc = collections.Counter()
    for c, e0, w, s in T:
        e = e0 + sum(wi*vi for wi, vi in zip(w, v))
        sgn = (-1)**(sum(si*vi for si, vi in zip(s, v)) % 2)
        acc[e] += c*sgn
    return all(x == 0 for x in acc.values())

def solve3(rows):  # rows: list of (a(3), b) ; solve a.v = b exactly; return unique rational sol or None
    import copy
    M = [list(map(Fr, a)) + [Fr(b)] for a, b in rows]
    n = 3; r = 0; piv = []
    for col in range(n):
        p = next((i for i in range(r, len(M)) if M[i][col] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][col]; M[r] = [x/pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                f = M[i][col]; M[i] = [x - f*y for x, y in zip(M[i], M[r])]
        piv.append(col); r += 1
    for i in range(r, len(M)):
        if M[i][n] != 0: return 'inconsistent'
    if r < 3: return None
    return tuple(M[i][n] for i in range(3))

found_points = set(); found_lines = []
for sig in (1, -1):
    T = terms(sig)
    H = set()
    for (c1,e1,w1,s1),(c2,e2,w2,s2) in combinations(T, 2):
        a = tuple(x - y for x, y in zip(w1, w2))
        if any(a): 
            b = e2 - e1
            g = 0
            from math import gcd
            for x in a: g = gcd(g, abs(x))
            if b % g: continue
            a = tuple(x//g for x in a); b //= g
            if next(x for x in a if x) < 0: a = tuple(-x for x in a); b = -b
            H.add((a, b))
    H = sorted(H)
    # points: all triple intersections with integer solution
    for h1, h2, h3 in combinations(H, 3):
        sol = solve3([h1, h2, h3])
        if sol in (None, 'inconsistent'): continue
        if all(x.denominator == 1 for x in sol):
            v = tuple(int(x) for x in sol)
            if evaluate_zero(T, v): found_points.add((v[0], v[1]))
    # lines: pairwise intersections; test generic integer points of each parity on the line
    for h1, h2 in combinations(H, 2):
        (a1,b1),(a2,b2) = h1, h2
        d = (a1[1]*a2[2]-a1[2]*a2[1], a1[2]*a2[0]-a1[0]*a2[2], a1[0]*a2[1]-a1[1]*a2[0])
        if not any(d): continue
        from math import gcd
        g = abs(d[0]); g = gcd(g, abs(d[1])); g = gcd(g, abs(d[2])); d = tuple(x//g for x in d)
        # find an integer point: brute force small search on the line via third equation x_k = t
        base = None
        for k in range(3):
            if d[k] == 0: continue
            for t in range(-60, 61):
                e = [0,0,0]; e[k] = 1
                sol = solve3([h1, h2, (tuple(e), t)])
                if sol not in (None,'inconsistent') and all(x.denominator == 1 for x in sol):
                    base = tuple(int(x) for x in sol); break
            if base: break
        if not base: continue
        for par in (0, 1):
            tt = 10**6 + par
            v = tuple(b + tt*di for b, di in zip(base, d))
            v2 = tuple(b + (tt+2)*di for b, di in zip(base, d))
            if evaluate_zero(T, v) and evaluate_zero(T, v2):
                found_lines.append((sig, base, d, par))
# Report: lines projected to (n1,n2)
proj = set()
for sig, base, d, par in found_lines:
    proj.add(((d[0], d[1]) if (d[0],d[1]) != (0,0) else 'point', ))
print("positive-rank families (projected directions in (n1,n2)):", sorted(set((d[0], d[1]) for _, _, d, _ in found_lines)))
on_axes = {p for p in found_points if p[0] == 0 or p[1] == 0}
print("isolated points off the axes n1=0, n2=0:", sorted(found_points - on_axes))
# cross-check with brute force on a big grid
bf = set()
for n1 in range(-40, 41):
    for n2 in range(-40, 41):
        if n1 == 0 or n2 == 0: continue
        for sig in (1,-1):
            T = terms(sig)
            # unit test: try all m in a range covering exponents
            for m in range(-250, 251):
                if evaluate_zero(T, (n1, n2, m)): bf.add((n1, n2)); break
print("brute force |n_i|<=40, off-axis unit points:", sorted(bf))
