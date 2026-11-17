#!/usr/bin/env python3
"""Lattice picture of N from a BN~ chain file: b-generators as rho + aD + bP (D=(1,2), P=(5,8)); rho = b-generator at the tail end of the arc
(or the first b-generator of the arc).  usage: gridbn.py cxBNr-file"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khparse import parse_file
from collections import Counter
def lattice(h, q):
    # h = a + 5b, q = 2a + 8b  =>  b = (2h - q)/2 , a = h - 5b
    assert (2*h - q) % 2 == 0
    b = (2*h - q) // 2; a = h - 5*b
    return a, b
def main(fn):
    comps = parse_file(fn)
    arc = [c for c in comps if not c['cyclic']][0]
    bs_arc = [(h, q) for (i, h, q) in arc['gens'] if i == '⬮']
    # rho: the arc b-generator adjacent to the tail (the end of the arc that is a c-generator), else last
    gens = arc['gens']
    if gens[0][0] == '⬯': rho = bs_arc[0]
    elif gens[-1][0] == '⬯': rho = bs_arc[-1]
    else: rho = bs_arc[-1]
    S = Counter(); kinds = {}
    for c in comps:
        for (i, h, q) in c['gens']:
            if i != '⬮': continue
            ab = lattice(h - rho[0], q - rho[1]); S[ab] += 1
    A = [a for a, b in S]; B = [b for a, b in S]
    print('dim N =', sum(S.values()), ' rho (h,q) =', rho, ' squares:', sum(1 for c in comps if c['cyclic']), ' arc b-gens:', len(bs_arc))
    for b in range(max(B), min(B) - 1, -1):
        row = ''
        for a in range(min(A), max(A) + 1):
            c = S.get((a, b), 0)
            row += ('%d' % c if c < 10 else '+') if c else '.'
            row += '*' if (a, b) == (0, 0) else ' '
        print('b=%3d  %s' % (b, row))
    print('       a from %d to %d' % (min(A), max(A)))
    # q extremes: q = 2a + 8b
    byq = Counter(); rows_at = {}
    for (a, b), m in S.items():
        q = 2*a + 8*b; rows_at.setdefault(q, Counter())[b] += m
    qmax, qmin = max(rows_at), min(rows_at)
    print('top q (rel):', qmax, 'rows', dict(rows_at[qmax]), ' bottom q:', qmin, 'rows', dict(rows_at[qmin]))
    # Euler characteristic by q: sign (-1)^(a+b)
    chi = Counter()
    for (a, b), m in S.items(): chi[2*a + 8*b] += m * (-1) ** ((a + b) % 2)
    nz = {q: c for q, c in sorted(chi.items()) if c}
    print('J (signed counts by q):', nz)
    zero = [q for q in rows_at if chi[q] == 0]
    print('q-degrees where N is non-zero but the Euler characteristic vanishes:', sorted(zero))
if __name__ == '__main__': main(sys.argv[1])
