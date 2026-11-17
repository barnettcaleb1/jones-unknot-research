#!/usr/bin/env python3
import sys, os, json
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dict_test import *

def onesided(blocks, k):
    """one-sided extended TILT: for k<0 minima strictly decrease with level, for k>0 maxima strictly decrease."""
    lv = defaultdict(list)
    for (c, d, kind) in blocks: lv[d].append(c)
    ds = sorted(lv)
    cons = all(ds[i+1] - ds[i] == 1 for i in range(len(ds)-1))
    mins = all(min(lv[ds[i+1]]) < min(lv[ds[i]]) for i in range(len(ds)-1))
    maxs = all(max(lv[ds[i+1]]) < max(lv[ds[i]]) for i in range(len(ds)-1))
    return cons, mins, maxs

tot = Counter(); bad = defaultdict(list); seen = set()
rows = []
for sub in ['k138', 'tilt', 'dbl', 'comp']:
    for dp, dn, fns in os.walk(os.path.join(ROOT, sub)):
        if not any(f.startswith('cxBNr-c2') for f in fns): continue
        r = analyse(dp)
        name = os.path.relpath(dp, ROOT)
        if r is None or 'err' in r: bad['err'].append(name); continue
        if r['dimW'] == 0: tot['trivial'] += 1; continue
        key = (tuple(sorted((c, str(d), kind) for c, d, kind in r['blocks'])))
        tot[sub] += 1; tot['n'] += 1
        if key in seen: tot['duplicate_config'] += 1
        seen.add(key)
        k = r['info'].get('k')
        for kk in ('D1', 'D2'):
            tot[kk] += r[kk]
            if not r[kk]: bad[kk].append(name)
        ca, sa, _, _ = r['tilt_actual']; ce, se, _, _ = r['tilt_ext']
        tot['tilt_actual'] += (ca and sa); tot['tilt_ext'] += (ce and se)
        cons, mins, maxs = onesided(r['blocks'], k)
        tot['ext_consecutive'] += cons
        if not cons: bad['ext_not_consecutive'].append((name, k))
        if k is not None and k != 0:
            tot['knz'] += 1
            good = mins if k < 0 else maxs
            tot['onesided_ext'] += good
            if not good: bad['onesided'].append((name, k))
            # where is the r level relative to the actual levels?
            lv_act = sorted(set(d for c, d, kind in r['blocks'] if kind == 's'))
            dr = [d for c, d, kind in r['blocks'] if kind == 'r'][0]
            pos = 'below' if dr < lv_act[0] else 'above' if dr > lv_act[-1] else 'bottom' if dr == lv_act[0] else 'top' if dr == lv_act[-1] else 'interior'
            tot['rlevel_%s_k%s' % (pos, '>0' if k > 0 else '<0')] += 1
            # parity rule
            tot['parity_rule'] += ((dr % 2 == 0) == (k < 0))
        # extreme coefficient
        chi = r['chi']
        tot['chi_nonzero'] += bool(chi)
        rows.append((name, k, r['dimW'], r['n_special_components'], r['n_bn_compact']))
print(dict(tot))
for k, v in bad.items():
    print('BAD', k, len(v)); 
    for x in v[:10]: print('   ', x)
json.dump(rows, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rows.json'), 'w'))
