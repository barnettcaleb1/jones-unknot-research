#!/usr/bin/env python3
import json, os, re, sys
from math import floor
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from count_test import tab, sig_2bridge
rows = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rows.json')))
ROOT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out'
from khparse import parse_line
import glob

def knot_complex(dp):
    """read cxCKh-c2 (complex of the symmetric knot itself) if present: returns (s, list of bar lengths)"""
    fn = os.path.join(dp, 'cxCKh-c2')
    if not os.path.exists(fn): return None
    s = None; bars = []
    for line in open(fn, encoding='utf-8'):
        m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)', line)
        if not m: continue
        chain = m.group(4)
        if chain == '⬮': s = int(m.group(2)) if int(m.group(1)) == 0 else s
        else:
            mm = re.search(r'H(?:\^(\d+))?', chain); bars.append(int(mm.group(1) or 1))
    return s, bars

res = Counter(); bad = []
for name, k, dimW, nspec, nbn in rows:
    N = dimW // 4; base = os.path.basename(name)
    if name.startswith('tilt'):
        kc = knot_complex(os.path.join(ROOT, name))
        if kc is None: res['tilt_noknot'] += 1; continue
        s, bars = kc
        thin = all(b == 1 for b in bars)
        pred = len(bars) + abs(s) // 2     # (det-1)/2 + |sigma|/2 for thin knots
        res['tilt'] += 1; res['tilt_thin'] += thin
        if N == pred: res['tilt_ok'] += 1
        else: bad.append((base, k, N, pred, s, bars))
    elif name.startswith('dbl'):
        m = re.match(r'k(\d+)_(\d+)', base)
        if not m: res['dbl_unparsed'] += 1; continue
        p, q = int(m.group(1)), int(m.group(2))
        sg = abs(sig_2bridge(p, q))
        pred = (p*p - 1 + 2*sg) // 2
        res['dbl'] += 1
        if N == pred: res['dbl_ok'] += 1
        else: bad.append((base, k, N, pred, p, q, sg))
    elif name.startswith('comp'):
        res['comp'] += 1
        parts = re.findall(r'(\d+_\d+)(i\d)?(m?)', base)
        det = 1; sg = 0
        for kn, inv, mir in parts:
            d, s_ = tab[kn]; det *= d; sg += (-s_ if mir else s_)
        pred = (det - 1 + abs(sg)) // 2
        if N == pred: res['comp_ok'] += 1
        else: bad.append((base, k, N, pred, det, sg))
print(dict(res))
for b in bad[:40]: print('MISMATCH', b)
