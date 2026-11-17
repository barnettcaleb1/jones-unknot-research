#!/usr/bin/env python3
"""The annular closure functor on type D structures over the Bar-Natan algebra B (F_2 coefficients).

Input: components as parsed by khparse (generators (idem,h,q), arrows (src,dst,kind,power)).
Module A (Khovanov TQFT of the closure by the two arcs of Q_inf, which run once around the annulus):
  A(⬯) = V⊗V : basis 11 (deg +2, k=+2), 1x, x1 (deg 0, k=0), xx (deg -2, k=-2)
  A(⬮) = <1, x>: deg +1, -1, k = 0
Arrow maps (x --b--> y contributes y ⊗ F(b)(a) to d(x ⊗ a)):
  S: ⬯->⬮ merge:  11->1, 1x->x, x1->x, xx->0          S: ⬮->⬯ split: 1 -> 1x + x1, x -> xx
  D on ⬯ (= x_* - x_1) and S^2 on ⬯ (= split∘merge): 11 -> 1x + x1, 1x -> xx, x1 -> xx
  D on ⬮, S^2 on ⬮, D^n (n>=2), S^n (n>=3): 0   (char 2, H = 0)
The differential splits as d_0 (k-preserving) + d_- (k drops by 2).
"""
import sys, os
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khparse import *
from akh import rank_f2

BASIS = {'⬯': [('11', 2, 2), ('1x', 0, 0), ('x1', 0, 0), ('xx', -2, -2)], '⬮': [('1', 1, 0), ('x', -1, 0)]}
def act(kind, power, src, dst, a):
    """returns list of basis labels of A(dst)"""
    if kind == 'S' and power == 1:
        if src == '⬯' and dst == '⬮': return {'11': ['1'], '1x': ['x'], 'x1': ['x'], 'xx': []}[a]
        if src == '⬮' and dst == '⬯': return {'1': ['1x', 'x1'], 'x': ['xx']}[a]
        raise ValueError
    if (kind == 'D' and power == 1) or (kind == 'S' and power == 2):
        assert src == dst
        if src == '⬯': return {'11': ['1x', 'x1'], '1x': ['xx'], 'x1': ['xx'], 'xx': []}[a]
        return []
    return []

def annular_complex(comps, shift=(0, 0)):
    """returns gens: list of (h,q,k,(ci,gi,label)), diff: dict index -> list of indices"""
    gens = []; index = {}
    for ci, comp in enumerate(comps):
        for gi, (idem, h, q) in enumerate(comp['gens']):
            for (lab, dq, k) in BASIS[idem]:
                index[(ci, gi, lab)] = len(gens)
                gens.append((h + shift[0], q + dq + shift[1], k, (ci, gi, lab)))
    diff = defaultdict(list)
    for ci, comp in enumerate(comps):
        for (s, d, kind, power) in comp['arrows']:
            si, di = comp['gens'][s][0], comp['gens'][d][0]
            for (lab, dq, k) in BASIS[si]:
                for lab2 in act(kind, power, si, di, lab):
                    diff[index[(ci, s, lab)]].append(index[(ci, d, lab2)])
    # sanity: degrees
    for i, tg in diff.items():
        for j in tg:
            assert gens[j][0] == gens[i][0] + 1 and gens[j][1] == gens[i][1] and gens[j][2] in (gens[i][2], gens[i][2] - 2), (gens[i], gens[j])
    return gens, diff

def homology(gens, diff, mode):
    """mode 'ann': differential d_0, sectors (q,k);  mode 'tot': full differential, sectors q.  returns Counter (h,q[,k]) -> dim"""
    sectors = defaultdict(lambda: defaultdict(list))
    for i, (h, q, k, _) in enumerate(gens):
        key = (q, k) if mode == 'ann' else (q,)
        sectors[key][h].append(i)
    H = Counter()
    for key, byh in sectors.items():
        rk = {}
        for h in sorted(byh):
            pos = {i: n for n, i in enumerate(byh.get(h + 1, []))}
            rows = []
            for i in byh[h]:
                v = 0
                for j in diff.get(i, []):
                    if mode == 'ann' and gens[j][2] != gens[i][2]: continue
                    v ^= 1 << pos[j]
                rows.append(v)
            rk[h] = rank_f2(rows)
        for h in sorted(byh):
            d = len(byh[h]) - rk[h] - rk.get(h - 1, 0)
            if d: H[(h,) + key] += d
    return H

def fmtH(H, k=None):
    return ', '.join('(%d,%d):%d' % (key[0], key[1], v) for key, v in sorted(H.items()) if k is None or key[2] == k)

if __name__ == '__main__':
    ROOT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out'
    fn = sys.argv[1] if len(sys.argv) > 1 else ROOT + '/tilt/examples/strong_inversions/2-bridge_knots/b3_2/cxBNr-c2-qs'
    j = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    comps = parse_file(fn)
    gens, diff = annular_complex(comps, shift=(-8*j, -24*j))
    Ha = homology(gens, diff, 'ann'); Ht = homology(gens, diff, 'tot')
    print('total homology (h,q):', fmtH(Ht))
    for k in (2, 0, -2): print('AKh k=%d:' % k, fmtH(Ha, k))
