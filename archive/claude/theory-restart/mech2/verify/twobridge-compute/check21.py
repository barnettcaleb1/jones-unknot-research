#!/usr/bin/env python3
"""Section 2.1 of the report (marked DATA / CONJECTURED there): two-variable formula
   P_w(x,y) = (1 0) M_X^{b_n} M_Y^{a_n} ... M_X^{b_1} M_Y^{a_1} (1 0)^T,  M_Y = [[1,0],[u,u]], M_X = [[1,1+y],[0,x]], u = x/y,
for positive words, against the saved data: lattice coordinates of the b-generators relative to rho (the b-generator of
the rational component): b = -(delta - delta_rho), a = (q - q_rho)/2 - 4b; P = sum x^a y^b (exact, no normalisation)."""
import json, os, collections
from reflib import *
base = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
DICT = {'y0': 'Y', 'x0': 'y', 'x1': 'X', 'y1': 'x'}
def twoletter(word):
    toks = word.split('.')
    if toks[0] != 's' or toks[1] not in ('l1', 'r1') or toks[-1] != 'u2': return None
    mid = toks[2:-1]
    if any(t not in DICT for t in mid): return None
    return ''.join(DICT[t] for t in mid)
# two-variable polynomials: dict {(i,j): c} meaning c x^i y^j
def add2(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
        if r[k] == 0: del r[k]
    return r
def mul2(p, q):
    r = {}
    for (a, b), v in p.items():
        for (c, d), w in q.items():
            k = (a + c, b + d); r[k] = r.get(k, 0) + v * w
            if r[k] == 0: del r[k]
    return r
ONE = {(0, 0): 1}; U = {(1, -1): 1}; X = {(1, 0): 1}; YP = {(0, 0): 1, (0, 1): 1}
def P_formula(w):
    v1, v2 = ONE, {}
    for L in w:
        if L == 'Y': v1, v2 = v1, mul2(U, add2(v1, v2))
        elif L == 'X': v1, v2 = add2(v1, mul2(YP, v2)), mul2(X, v2)
        else: raise ValueError
    return v1
items = []
for l in open(base + 'k138/k138.jsonl'):
    r = json.loads(l); nm = r['file'].replace('^', '-')
    items.append(('k138', nm, base + 'k138/examples/si/' + nm + '.kht', r))
for l in open(base + 'tilt/run_3_45.jsonl'):
    r = json.loads(l); nm = os.path.basename(r['file']).replace('.kht', '')
    items.append(('tilt', nm, base + 'tilt/examples/strong_inversions/2-bridge_knots/' + nm + '.kht', r))
st = collections.Counter(); bad = []; seen = set()
for src, nm, fn, r in items:
    if not os.path.exists(fn) or not r.get('khr'): continue
    w = twoletter(open(fn).read().split('\n')[1].strip())
    if w is None or not w or set(w) - set('XY'): continue
    st['positive words (letters Y, X only)'] += 1
    jd = J_from_khr(r['khr'])
    k, j, J, pts = jd
    q0, d0 = pts[0]
    P = {}
    ok = True
    for (q, d) in pts:
        b = -(d - d0); a2 = (q - q0) - 8 * b
        if a2 % 2: ok = False; break
        key = (a2 // 2, b); P[key] = P.get(key, 0) + 1
    if not ok: bad.append((src, nm, w, 'odd')); continue
    F = P_formula(w)
    good = (P == F)
    st['formula 2.1 = data (whole multiset, rho at origin)'] += good
    proper = w[0] == 'Y' and w[-1] == 'X'
    st['of which proper form Y..X'] += proper
    blocks = sum(1 for i in range(len(w)) if w[i] == 'X' and (i + 1 == len(w) or w[i + 1] == 'Y'))
    st['blocks=%d' % blocks] += 1
    seen.add(w)
    if not good: bad.append((src, nm, w, sorted(P.items()), sorted(F.items())))
print(dict(st)); print('distinct positive words:', len(seen), ' max length', max(map(len, seen)))
print('mismatches:', len(bad))
for b in bad[:10]: print('  ', b)
