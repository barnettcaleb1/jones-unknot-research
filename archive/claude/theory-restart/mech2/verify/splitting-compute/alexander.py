#!/usr/bin/env python3
"""Referee's own Alexander polynomial of a 1-1 tangle knot word (Wirtinger arcs + Alexander-quandle relations
L = t R + (1-t) O at each crossing, O = over arc, L/R = under arc to the left/right of the oriented over-strand).
Determinant by exact evaluation at integer points + Lagrange interpolation (no external library)."""
from fractions import Fraction
from morse import parse, Trace

def alexander_matrix(events):
    tr = Trace(events, 1, close11=True)
    assert len(tr.components()) == 1
    o = tr.orient
    # segments of each monotone strand: strand s is cut at every crossing where it is the under-strand.
    # segment id = (s, j), j = number of under-crossings passed so far going down
    par = {}
    def find(a):
        par.setdefault(a, a)
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    def union(a, b):
        par[find(a)] = find(b)
    seg = {s: 0 for s in range(tr.nstrands)}      # current segment index while sweeping down
    cur = list(range(tr.ntop)); nxt = tr.ntop
    rels = []
    find((0, 0))
    for (c, i) in events:
        if c in 'xy':
            sa, sb = cur[i], cur[i + 1]      # top-left, top-right
            if c == 'x': over, under = sa, sb
            else:        over, under = sb, sa
            O = (over, seg[over])
            top = (under, seg[under]); seg[under] += 1; bot = (under, seg[under])
            find(top); find(bot); find(O)
            # which under segment lies to the left of the oriented over-strand
            if c == 'x':
                L, R = (top, bot) if o[over] == -1 else (bot, top)
            else:
                L, R = (bot, top) if o[over] == -1 else (top, bot)
            rels.append((L, R, O))
            cur[i], cur[i + 1] = sb, sa
        elif c in 'lr':
            a, b = nxt, nxt + 1; nxt += 2
            cur[i:i] = [a, b]
            union((a, 0), (b, 0))
        else:
            a, b = cur[i], cur[i + 1]
            union((a, seg[a]), (b, seg[b]))
            del cur[i:i + 2]
    # closure: bottom end joined to top end
    b = cur[0]
    union((b, seg[b]), (0, 0))
    arcs = sorted(set(find(x) for x in list(par)))
    idx = {a: k for k, a in enumerate(arcs)}
    rows = []
    for L, R, O in rels:
        row = {}
        for a, coef in ((find(L), (1, 0)), (find(R), (0, -1)), (find(O), (-1, 1))):   # L - t R - (1-t) O ; coef = (const, t-coefficient)
            k = idx[a]
            c0, c1 = row.get(k, (0, 0))
            row[k] = (c0 + coef[0], c1 + coef[1])
        rows.append(row)
    return rows, len(arcs)

def det_int(M):
    """exact determinant of a square matrix of Fractions"""
    n = len(M); M = [r[:] for r in M]; d = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None: return Fraction(0)
        if p != c:
            M[c], M[p] = M[p], M[c]; d = -d
        d *= M[c][c]
        inv = 1 / M[c][c]
        for r in range(c + 1, n):
            if M[r][c] != 0:
                f = M[r][c] * inv
                for k in range(c, n):
                    M[r][k] -= f * M[c][k]
    return d

def alexander(events):
    """normalised Alexander polynomial as list of coefficients (lowest degree first), Delta(1) = 1"""
    rows, na = alexander_matrix(events)
    n = len(rows)
    if n == 0: return [1]
    assert na == n, (na, n)
    # delete last row and last column; entries are linear in t => det has degree <= n-1
    pts = list(range(2, 2 + n + 1))
    vals = []
    for tv in pts:
        M = [[Fraction(0)] * (n - 1) for _ in range(n - 1)]
        for r in range(n - 1):
            for k, (c0, c1) in rows[r].items():
                if k < n - 1:
                    M[r][k] = Fraction(c0 + c1 * tv)
        vals.append(det_int(M))
    # Lagrange interpolation -> coefficients
    m = len(pts)
    coef = [Fraction(0)] * m
    for j in range(m):
        # basis polynomial
        b = [Fraction(1)]
        den = Fraction(1)
        for k in range(m):
            if k == j: continue
            b = [Fraction(0)] + b
            for q in range(len(b) - 1):
                b[q] -= pts[k] * b[q + 1]
            den *= (pts[j] - pts[k])
        for q in range(len(b)):
            coef[q] += vals[j] * b[q] / den
    assert all(c.denominator == 1 for c in coef)
    c = [int(x) for x in coef]
    while c and c[-1] == 0: c.pop()
    while c and c[0] == 0: c.pop(0)
    if not c: return [0]
    if sum(c) < 0: c = [-x for x in c]
    assert sum(c) == 1, c
    return c

if __name__ == '__main__':
    for w in ['r1.y0.y0.y0.u1', 'r1.y0.y0.y0.y0.y0.u1', 'r1.r2.y0.y1.y0.y1.y0.y1.y0.y1.u2.u1', 'l1.y0.y0.x1.x1.u0', 'r1.y0.x0.x0.y0.u1']:
        print(w, alexander(parse(w)))
