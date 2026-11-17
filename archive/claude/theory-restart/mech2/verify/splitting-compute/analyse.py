#!/usr/bin/env python3
"""Main referee check.  For each table inversion: Kh~ (F_2, kht++) of the two components of T(0); Euler characteristic against my Jones
polynomial; inequality dim N >= product; l-graded refinement; determinant product."""
import json, os, sys, collections
from chain import kh_of_knot
info = json.load(open('split_info.json'))
N = json.load(open('N_from_chains.json'))

def poly_l(gens):
    p = collections.Counter()
    for h, q in gens:
        p[h - q] += 1
    return p
def pmulc(p, q):
    r = collections.Counter()
    for a, x in p.items():
        for b, y in q.items():
            r[a + b] += x * y
    return r
def div1px(d):
    """d = Counter (Laurent polynomial).  Return list of coefficients of R with d = (1+x) R, or None if not divisible; flag non-negativity."""
    d = {k: v for k, v in d.items() if v}
    if not d:
        return {}, True
    lo, hi = min(d), max(d)
    r = {}; prev = 0; nonneg = True
    for k in range(lo, hi + 1):
        cur = d.get(k, 0) - prev
        r[k] = cur
        if cur < 0: nonneg = False
        prev = cur
    if prev != 0:      # remainder: coefficient at hi+1 must vanish
        return None, False
    r = {k: v for k, v in r.items() if v}
    return r, nonneg
def refinement(PN, W):
    """all shifts c such that PN - x^c W = (1+x) R with R >= 0; also those with R of mixed sign"""
    good = []; divisible = []
    lo = min(PN) - max(W) - 2; hi = max(PN) - min(W) + 2
    for c in range(lo, hi + 1):
        d = collections.Counter(PN)
        for k, v in W.items():
            d[k + c] -= v
        r, nonneg = div1px(d)
        if r is None: continue
        divisible.append(c)
        if nonneg: good.append((c, r))
    return good, divisible
def jones_from_kh(gens):
    p = collections.Counter()
    for h, q in gens:
        p[q] += (-1) ** (h % 2)
    return sorted((k, v) for k, v in p.items() if v)
def det_from_jones(j):
    # V(t=-1): q = i  -> sum c_k i^k ; all k even for knots
    s = 0
    for k, c in j:
        assert k % 2 == 0
        s += c * (-1) ** ((k // 2) % 2)
    return abs(s)


if __name__ == '__main__':
    rows = {}
    for nm in sorted(info):
        r = info[nm]
        kh = {}
        for tag in 'oc':
            p = 'examples/comp/%s_%s/cxCKh-c2' % (nm, tag)
            kh[tag] = kh_of_knot(p)
        jo = jones_from_kh(kh['o']); jc = jones_from_kh(kh['c'])
        assert jo == [tuple(x) for x in r['jones_open']], (nm, 'open Jones mismatch', jo, r['jones_open'])
        assert jc == [tuple(x) for x in r['jones_closed']], (nm, 'closed Jones mismatch', jc, r['jones_closed'])
        row = dict(rk_o=len(kh['o']), rk_c=len(kh['c']), det_o=det_from_jones(jo), det_c=det_from_jones(jc),
                   kh_o=kh['o'], kh_c=kh['c'], lk2=r['lk2'])
        row['prod'] = row['rk_o'] * row['rk_c']
        if nm in N:
            n = [tuple(x) for x in N[nm]]
            row['dimN'] = len(n)
            PN = poly_l(n); W = pmulc(poly_l(kh['o']), poly_l(kh['c']))
            good, divisible = refinement(PN, W)
            row['good_c'] = [c for c, R in good]
            row['R'] = {c: sorted(R.items()) for c, R in good}
            row['divisible_c'] = divisible
            row['PN'] = sorted(PN.items()); row['W'] = sorted(W.items())
        rows[nm] = row
    json.dump(rows, open('analysis.json', 'w'))
    # report
    viol = [nm for nm, r in rows.items() if 'dimN' in r and r['dimN'] < r['prod']]
    noref = [nm for nm, r in rows.items() if 'dimN' in r and not r['good_c']]
    eq = [nm for nm, r in rows.items() if 'dimN' in r and r['dimN'] == r['prod']]
    strict = [nm for nm, r in rows.items() if 'dimN' in r and r['dimN'] > r['prod']]
    print('components computed for', len(rows), 'inversions;  with N(T) data:', sum(1 for r in rows.values() if 'dimN' in r))
    print('Jones (Euler characteristic of kht++ Kh~) == my Kauffman-bracket Jones for all components: OK (asserted)')
    print('violations of dim N >= rk_o*rk_c:', viol)
    print('no shift c with (1+x)R, R>=0:', noref)
    print('equality dim N = product:', len(eq), '   strict:', [(nm, rows[nm]['dimN'], rows[nm]['rk_o'], rows[nm]['rk_c']) for nm in strict])
    multi = [(nm, rows[nm]['good_c']) for nm in rows if 'dimN' in rows[nm] and len(rows[nm]['good_c']) != 1]
    print('number of admissible shifts c != 1:', multi)
    both_knotted = [nm for nm, r in rows.items() if r['rk_o'] > 1 and r['rk_c'] > 1]
    print('both components knotted (rank > 1):', len(both_knotted), both_knotted)
    thick = [nm for nm, r in rows.items() if r['rk_o'] != r['det_o'] or r['rk_c'] != r['det_c']]
    print('a component with rank Kh~ != det:', [(nm, rows[nm]['rk_o'], rows[nm]['det_o'], rows[nm]['rk_c'], rows[nm]['det_c']) for nm in thick])

