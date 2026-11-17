#!/usr/bin/env python3
"""The data claim dim N(T) = max(rank HFK^(K), rk Kh~(K_u) rk Kh~(K_l)).
rank HFK^(K): = det K for all knots of the table except 8_19 (5) and 9_42 (9)  [RECALLED: every knot with <= 9 crossings other than
8_19 and 9_42 is Floer-thin; not recomputed here].  det K is computed here from kht++'s Kh~ of the knot itself (Euler characteristic at q = i)."""
import json, os, collections
from chain import kh_of_knot
from analyse import jones_from_kh, det_from_jones
rows = json.load(open('analysis.json'))
HFK_EXC = {'8_19': 5, '9_42': 9}
out = {}; bad_det = []; bad_max = []; cases = collections.Counter()
for nm, r in sorted(rows.items()):
    kh = kh_of_knot('examples/knots/%s/cxCKh-c2' % nm)
    detK = det_from_jones(jones_from_kh(kh))
    knot = nm.split('-')[0]
    hfk = HFK_EXC.get(knot, detK)
    out[nm] = dict(detK=detK, rkKh=len(kh), hfk=hfk)
    if detK != r['det_o'] * r['det_c']:
        bad_det.append((nm, detK, r['det_o'], r['det_c']))
    if 'dimN' in r:
        m = max(hfk, r['prod'])
        if r['dimN'] != m: bad_max.append((nm, r['dimN'], hfk, r['prod']))
        cases[('dimN==hfk', r['dimN'] == hfk, 'dimN==prod', r['dimN'] == r['prod'])] += 1
json.dump(out, open('knots.json', 'w'))
print('det K = det(o) det(c) fails for:', bad_det, ' (checked %d)' % len(rows))
print('dim N != max(rank HFK^, product):', bad_max)
print('case split:', sorted(cases.items(), key=str))
print('knots with rk Kh~(K;F_2) != det K:', sorted(set((nm.split('-')[0], v['rkKh'], v['detK']) for nm, v in out.items() if v['rkKh'] != v['detK'])))
for nm in ['8_19', '9_42', '9_46-1', '9_46-2']:
    r = rows[nm]; print(nm, 'dim N', r['dimN'], 'rank HFK^', out[nm]['hfk'], 'det K', out[nm]['detK'], 'rk Kh~(K)', out[nm]['rkKh'], 'product', r['prod'], '(', r['rk_o'], r['rk_c'], ')')
