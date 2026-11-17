#!/usr/bin/env python3
"""Formal flat object B1 = (arc of 5_2 second inversion) + (its square shifted by (h,q) = (3,6)): closures of slope +-1/n via
HF(a(+-1/n), Cone_H(component)) (engine: lit/kwz-linear/calc/hf.py), then the largest matching by pairs of bidegree (r, 2r-2), r >= 2
(Daemi's degree rule).  Comparison with the actual tangle (square not shifted)."""
import sys, os
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/calc')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hf as HF
from khparse import parse_file
from collections import Counter, defaultdict

def to_typed(comp, shift=(0, 0), name='comp'):
    gens = comp['gens']
    idem = [0 if g[0] == '⬮' else 1 for g in gens]
    arrows = []
    for (s, t, kind, p) in comp['arrows']:
        lab = kind if p == 1 else '%s%d' % (kind, p)
        arrows.append((s, t, lab))
    X = HF.TypeD(name, idem, arrows, base=0)
    # absolute gradings: q, d2 = 2 delta = q - 2h
    h0, q0 = gens[0][1] + shift[0], gens[0][2] + shift[1]
    X.q = [q + q0 for q in X.q]
    X.d2 = [d + (q0 - 2 * h0) for d in X.d2]
    for g, (i, h, q) in enumerate(gens):
        assert X.q[g] == q + shift[1] and X.d2[g] == (q + shift[1]) - 2 * (h + shift[0]), (g, X.q[g], X.d2[g], h, q)
    return X
def cone_abs(X):
    Y = HF.cone_H(X)
    n = len(X.idem)
    # cone_H regrades from base 0; restore absolute: [q^-1 d^1/2 X -> q^1 d^1/2 X]: first copy q-1, 2delta+1 ; second q+1, 2delta+1
    dq = (X.q[0] - 1) - Y.q[0]; dd = (X.d2[0] + 1) - Y.d2[0]
    Y.q = [q + dq for q in Y.q]; Y.d2 = [d + dd for d in Y.d2]
    for g in range(n):
        assert Y.q[g] == X.q[g] - 1 and Y.q[g + n] == X.q[g] + 1 and Y.d2[g] == X.d2[g] + 1 and Y.d2[g + n] == X.d2[g] + 1
    return Y
def closure(comps, arc):
    tot = Counter()
    for X in comps:
        res = HF.hf(arc, cone_abs(X))
        for (q, d2), dim in res.items():
            assert (q - d2) % 2 == 0
            tot[((q - d2) // 2, q)] += dim          # (h, q)
    return tot
def max_matching(gens):
    """gens: list of (h,q); edges between (h,q) and (h+r, q+2r-2), r>=2"""
    n = len(gens)
    adj = [[] for _ in range(n)]
    for i, (h, q) in enumerate(gens):
        for j, (h2, q2) in enumerate(gens):
            r = h2 - h
            if r >= 2 and q2 - q == 2 * r - 2: adj[i].append(j); adj[j].append(i)
    side = [(q // 2 - h) % 2 for (h, q) in gens]     # delta parity: bipartite
    mate = [-1] * n
    def aug(u, seen):
        for v in adj[u]:
            if v in seen: continue
            seen.add(v)
            if mate[v] == -1 or aug(mate[v], seen):
                mate[v] = u; mate[u] = v; return True
        return False
    size = 0
    for u in range(n):
        if side[u] == 0 and aug(u, set()): size += 1
    return size
def analyse(name, comps, ns=(1, 2, 3)):
    for n in ns:
        for sgn in (1, -1):
            arc = HF.arc_inv(sgn * n)
            tot = closure(comps, arc)
            gens = [k for k, v in tot.items() for _ in range(v)]
            chi = Counter()
            for (h, q) in gens: chi[q] += (-1) ** (h % 2)
            chi = {q: c for q, c in sorted(chi.items()) if c}
            dlev = Counter((q // 2 - h) if q % 2 == 0 else (q - 2 * h) / 2 for (h, q) in gens)
            left = len(gens) - 2 * max_matching(gens)
            print('%-34s slope %+d/%d: rank %3d  delta-levels %s  Jones (signed q-counts) %s  unmatched after (r,2r-2)-matching: %d' %
                  (name, sgn, n, len(gens), dict(sorted(dlev.items())), chi, left))
if __name__ == '__main__':
    fn = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/5_2-2/cxBNr-c2-qs'
    comps = parse_file(fn)
    arc = [c for c in comps if not c['cyclic']][0]; sq = [c for c in comps if c['cyclic']][0]
    print('arc b-generators:', [(h, q) for (i, h, q) in arc['gens'] if i == '⬮'], ' square b-generators:', [(h, q) for (i, h, q) in sq['gens'] if i == '⬮'])
    actual = [to_typed(arc, name='arc'), to_typed(sq, name='square')]
    b1 = [to_typed(arc, name='arc'), to_typed(sq, shift=(3, 6), name='square shifted')]
    analyse('actual 5_2 second inversion', actual)
    analyse('B1 (square shifted by (3,6))', b1)
