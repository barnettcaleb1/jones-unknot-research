#!/usr/bin/env python3
"""Apply the annular closure functor to every saved BNr; check convergence to Kh(unknot) componentwise; then to Codex's formal object B."""
import sys, os, glob, json
from fractions import Fraction
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khparse import *
from annfun import *
ROOT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out'

def jk_from_kh(khc):
    for comp in khc:
        li = label_info(comp['label'])
        if li and li['type'] == 'r':
            k = int(li['slope']); qr = li['q']
            j24 = qr - Fraction(k * (abs(k) + 2), abs(k) + 1)
            assert j24.denominator == 1 and j24.numerator % 24 == 0, (k, qr)
            return k, j24.numerator // 24
    raise ValueError

tot = Counter(); bad = []
for sub in ['k138', 'tilt', 'dbl', 'comp']:
    for dp, dn, fns in os.walk(os.path.join(ROOT, sub)):
        bn = glob.glob(os.path.join(dp, 'cxBNr-c2*')); kh = glob.glob(os.path.join(dp, 'cxKhr-c2*'))
        if not bn or not kh: continue
        bnc = parse_file(bn[0]); khc = parse_file(kh[0])
        if len(bnc) == 1 and len(bnc[0]['gens']) == 1: continue      # trivial tangle
        name = os.path.relpath(dp, ROOT)
        try: k, j = jk_from_kh(khc)
        except Exception as e: bad.append((name, 'jk', str(e))); continue
        tot['n'] += 1
        okall = True
        dimW = 0; dim0 = 0
        for comp in bnc:
            gens, diff = annular_complex([comp], shift=(-8*j, -24*j))
            Ht = homology(gens, diff, 'tot')
            if comp['cyclic']:
                tot['compact'] += 1
                if len(Ht) == 0: tot['compact_acyclic'] += 1
                else: okall = False
            else:
                tot['arc'] += 1
                if Ht == Counter({(0, -1): 1, (0, 1): 1}): tot['arc_unknot'] += 1
                else: okall = False
            if sub == 'k138' or len(gens) < 4000:
                Ha = homology(gens, diff, 'ann')
                dimW += sum(v for key, v in Ha.items() if key[2] == 2); dim0 += sum(v for key, v in Ha.items() if key[2] == 0)
                assert sum(v for key, v in Ha.items() if key[2] == 2) == sum(v for key, v in Ha.items() if key[2] == -2)
        tot['ok'] += okall
        if not okall: bad.append((name, 'homology'))
        if dimW: tot['dim0==2dimW' if dim0 == 2*dimW else 'dim0!=2dimW'] += 1
print(dict(tot)); print(bad[:10])

# ---- Codex's formal object B = a(0) + S + hS ----
print('\nFormal object B = a(0) + S + hS:')
a0 = component(0, 0, ['⬮'], [])
Sline = '1) h^-1 q^9 δ^11/2 ⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—'
h, q, gens, arrows, rest = parse_line(Sline)
for shift_h in (0, 1):
    S = component(h + shift_h, q, gens, arrows)
    g, d = annular_complex([S])
    print('  summand S shifted by h^%d: closes up: %s; total homology: %s' % (shift_h, S['ok'], dict(homology(g, d, 'tot'))))
    Ha = homology(g, d, 'ann')
    for kk in (2, 0, -2): print('    AKh k=%d:' % kk, fmtH(Ha, kk))
B = [a0, component(h, q, gens, arrows), component(h + 1, q, gens, arrows)]
g, d = annular_complex(B)
print('  B total homology:', dict(homology(g, d, 'tot')))
Ha = homology(g, d, 'ann')
print('  B dims by weight:', {kk: sum(v for key, v in Ha.items() if key[2] == kk) for kk in (2, 0, -2)})
chi = Counter()
for (hh, qq, kk), v in Ha.items():
    if kk == 2: chi[qq] += (-1)**(hh % 2) * v
print('  B: Euler characteristic of the weight-two space:', {q_: c for q_, c in chi.items() if c})
