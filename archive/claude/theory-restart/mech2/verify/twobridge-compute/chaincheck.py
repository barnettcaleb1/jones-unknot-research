#!/usr/bin/env python3
"""Fourth leg on the saved data: J from the saved BN~ chain files (b-generators read directly off the chains, no rule)
against J from the Kh~ component rule and against the matrix formula."""
import json, os, collections
from reflib import *
from chainparse import *
base = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
DICT = {'y0': 'Y', 'x0': 'y', 'x1': 'X', 'y1': 'x'}
def twoletter(word):
    toks = word.split('.')
    if toks[0] != 's' or toks[1] not in ('l1', 'r1') or toks[-1] != 'u2': return None
    mid = toks[2:-1]
    if any(t not in DICT for t in mid): return None
    return ''.join(DICT[t] for t in mid)
items = []
for l in open(base + 'k138/k138.jsonl'):
    r = json.loads(l); nm = r['file'].replace('^', '-')
    items.append(('k138', nm, base + 'k138/examples/si/' + nm + '.kht', base + 'k138/examples/si/' + nm + '/', r))
for l in open(base + 'tilt/run_3_45.jsonl'):
    r = json.loads(l); nm = os.path.basename(r['file']).replace('.kht', '')
    d = base + 'tilt/examples/strong_inversions/2-bridge_knots/'
    items.append(('tilt', nm, d + nm + '.kht', d + nm + '/', r))
st = collections.Counter(); bad = []
for src, nm, fn, d, r in items:
    if not os.path.exists(fn): continue
    word = open(fn).read().split('\n')[1].strip()
    bn = [f for f in (os.listdir(d) if os.path.isdir(d) else []) if f.startswith('cxBNr')]
    if not bn: st['no BN chain file'] += 1; continue
    st['BN chain files'] += 1
    try:
        comps = parse_file(d + bn[0])
    except Exception as e:
        bad.append((src, nm, 'parse error', repr(e))); continue
    Jbn = J_from_BN(comps)
    nb = sum(1 for c in comps for g in c['gens'] if g[0] == 'b')
    khr = r.get('khr')
    if khr:
        jd = J_from_khr(khr)
        if jd is not None:
            st['compared with Kh~ rule'] += 1
            ok = (pnorm(Jbn) == pnorm(jd[2])) and nb == len(jd[3])
            # stronger: same multiset of (q/2, sign) up to a common shift, same number of generators
            st['BN = Kh~ rule (J up to unit, and number of b-generators)'] += ok
            if not ok: bad.append((src, nm, word, 'BN', pnorm(Jbn), nb, 'rule', pnorm(jd[2]), len(jd[3])))
            # exact (no unit): the rule claims the absolute gradings
            st['BN = Kh~ rule exactly (no unit)'] += (Jbn == jd[2])
    w = twoletter(word)
    if w is not None:
        st['two-letter with BN file'] += 1
        ok = pnorm(Jbn) == pnorm(J_matrix(w))
        st['BN = matrix formula'] += ok
        if not ok: bad.append((src, nm, word, w, 'BN vs matrix', pnorm(Jbn), pnorm(J_matrix(w))))
print(dict(st))
print('problems:', len(bad))
for b in bad[:30]: print('  ', b)
