#!/usr/bin/env python3
"""Test the annular dictionary on all saved kht++ outputs:
 (D1) Gen_inf(Khr) = (q + q^-1 h^-1) * Gen_inf(BNr) as bigraded multisets;
 (D2) W := Gen_inf(BNr) = sum over specials (c,d) of q^{c-3} h^{c/2-1-d} (1+u+u^2+u^3)  +  string of r_1(k);
 (D3) extended TILT: include the virtual blocks of r_1(k) at their true level.
"""
import sys, os, glob, json
from fractions import Fraction
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khparse import *

ROOT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out'

def blocks_from_kh(khc):
    """from Khr components: list of (c, d, kind) blocks; kind 's' actual, 'r' virtual.  Uses only generators at ⬯."""
    blocks = []; info = {}
    for comp in khc:
        li = label_info(comp['label'])
        g = sorted((h, q) for (i, h, q) in comp['gens'] if i == '⬯')
        if not g: 
            if li and li['type'] == 'r': info['k'] = 0; info['r_label'] = li
            continue
        deltas = set(Fraction(q, 2) - h for (h, q) in g)
        assert len(deltas) == 1, ('not delta-homogeneous', comp['label'], deltas)
        d = deltas.pop()
        qs = sorted(q for (h, q) in g)
        n = len(g)
        # shape must be (1+u)(1+u+...+u^{n/2-1}) starting at qs[0]
        expect = Counter()
        for a in (0, 1):
            for b in range(n // 2):
                expect[qs[0] + 2*(a + b)] += 1
        assert Counter(qs) == expect, ('shape', comp['label'], qs)
        m = n // 2          # length of the string in W
        # string in W: q0 = qs[0] + 1 ... (dividing by q^-1 h^-1 (1+u)); W string starts at q = qs[0]+1, level delta d - 1/2
        q0 = qs[0] + 1
        if li['type'] == 's':
            assert m % 4 == 0
            for i in range(m // 4):
                blocks.append((q0 + 3 + 8*i, d, 's'))
        else:
            info['k'] = int(li['slope']) if li['slope'] not in ('∞',) else None
            info['r_label'] = li
            info['r_string'] = (q0, d, m)
            if m % 4 == 0:
                for i in range(m // 4):
                    blocks.append((q0 + 3 + 8*i, d, 'r'))
            else:
                info['r_not_div4'] = m
    return blocks, info

def tilt_check(blocks):
    lv = defaultdict(list)
    for (c, d, kind) in blocks: lv[d].append(c)
    ds = sorted(lv)
    consecutive = all(ds[i+1] - ds[i] == 1 for i in range(len(ds)-1))
    strict = all(min(lv[ds[i+1]]) < min(lv[ds[i]]) and max(lv[ds[i+1]]) < max(lv[ds[i]]) for i in range(len(ds)-1))
    steps = [(min(lv[ds[i]]) - min(lv[ds[i+1]]), max(lv[ds[i]]) - max(lv[ds[i+1]])) for i in range(len(ds)-1)]
    return consecutive, strict, steps, ds

def analyse(dirpath):
    bn = glob.glob(os.path.join(dirpath, 'cxBNr-c2*')); kh = glob.glob(os.path.join(dirpath, 'cxKhr-c2*'))
    if not bn or not kh: return None
    bnc = parse_file(bn[0]); khc = parse_file(kh[0])
    if not all(c['ok'] for c in bnc + khc): return dict(err='chain does not close')
    Wb = W_of(bnc); Wk = W_of(khc)
    # (D1)
    pred = Counter()
    for (h, q), m in Wb.items():
        pred[(h, q + 1)] += m; pred[(h - 1, q - 1)] += m
    D1 = (pred == Wk)
    try:
        blocks, info = blocks_from_kh(khc)
    except AssertionError as e:
        return dict(err=str(e), D1=D1)
    # (D2) W from blocks
    Wp = Counter()
    for (c, d, kind) in blocks:
        for i in range(4):
            q = c - 3 + 2*i; h = Fraction(q, 2) - (d - Fraction(1, 2))
            assert h.denominator == 1
            Wp[(int(h), q)] += 1
    if 'r_not_div4' in info:
        q0, d, m = info['r_string']
        for i in range(m):
            q = q0 + 2*i; h = Fraction(q, 2) - (d - Fraction(1, 2)); Wp[(int(h), q)] += 1
    D2 = (Wp == Wb)
    res = dict(D1=D1, D2=D2, dimW=sum(Wb.values()), blocks=blocks, info=info)
    res['tilt_actual'] = tilt_check([b for b in blocks if b[2] == 's'])
    res['tilt_ext'] = tilt_check(blocks)
    # Euler characteristic of W and extreme coefficients
    chi = Counter()
    for (h, q), m in Wb.items(): chi[q] += (-1)**(h % 2) * m
    chi = {q: c for q, c in chi.items() if c}
    res['chi'] = chi
    res['n_special_components'] = sum(1 for c in khc if (label_info(c['label']) or {}).get('type') == 's')
    res['n_bn_compact'] = sum(1 for c in bnc if c['cyclic'])
    return res

if __name__ == '__main__':
    subs = sys.argv[1:] or ['k138', 'tilt', 'dbl', 'comp', 'rand', 'si', 'arc']
    tot = Counter(); fails = defaultdict(list)
    out = []
    for sub in subs:
        for dp, dn, fns in os.walk(os.path.join(ROOT, sub)):
            if not any(f.startswith('cxBNr-c2') for f in fns): continue
            r = analyse(dp)
            if r is None: continue
            name = os.path.relpath(dp, ROOT)
            tot['n'] += 1
            if 'err' in r:
                tot['err'] += 1; fails['err'].append((name, r['err'])); continue
            for key in ('D1', 'D2'):
                if r[key]: tot[key] += 1
                else: fails[key].append(name)
            ca, sa, stepsa, dsa = r['tilt_actual']; ce, se, stepse, dse = r['tilt_ext']
            if ca and sa: tot['tilt_actual'] += 1
            else: fails['tilt_actual'].append(name)
            if ce and se: tot['tilt_ext'] += 1
            else: fails['tilt_ext'].append((name, r['info'].get('k'), sorted(r['blocks'], key=lambda b: (b[1], b[0]))))
            if r['chi']: tot['chi_nonzero'] += 1
            else: fails['chi_zero'].append(name)
            k = r['info'].get('k')
            tot['k=%s' % ('0' if k == 0 else 'nz')] += 1
            out.append(dict(name=name, k=k, dimW=r['dimW'], blocks=[(c, str(d), kind) for (c, d, kind) in r['blocks']],
                            nspec=r['n_special_components'], nbn_compact=r['n_bn_compact'],
                            r_string=[str(x) for x in r['info'].get('r_string', ())],
                            steps_ext=stepse, levels_ext=[str(x) for x in dse]))
    print(dict(tot))
    for k, v in fails.items():
        print('FAIL', k, len(v))
        for x in v[:12]: print('   ', x)
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dict_test_out.json'), 'w'), indent=0)
