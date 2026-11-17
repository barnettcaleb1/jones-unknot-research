#!/usr/bin/env python3
"""compare direct annular Khovanov homology (akh.py) with the functor applied to kht++'s BNr (annfun.py)"""
import sys, os, glob, re, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khparse import *
from annfun import *
from annfun_lib import jk_from_kh
import akh
folder = sys.argv[1]
kht = folder.rstrip('/') + '.kht'
word = re.search(r"Simplifies with options '-qs' to (\S+)", open(kht).read()).group(1)
bnc = parse_file(glob.glob(os.path.join(folder, 'cxBNr-c2*'))[0]); khc = parse_file(glob.glob(os.path.join(folder, 'cxKhr-c2*'))[0])
k, j = jk_from_kh(khc)
gens, diff = annular_complex(bnc, shift=(-8*j, -24*j))
Ha = homology(gens, diff, 'ann')
t = time.time()
r = akh.khovanov(word, [('top', 0, True), (1, 2, True)])
print(os.path.basename(folder), 'k=%d j=%d' % (k, j), 'word', word, 'crossings', r['n'], 'time %.0fs' % (time.time() - t))
print('  direct Kh:', akh.fmt(r['Kh']))
print('  direct AKh == functor(BNr) in all weights, absolute gradings:', dict(r['AKh']) == dict(Ha))
for kk in (2, 0, -2):
    print('  k=%d dims: direct %d, functor %d' % (kk, sum(v for key, v in r['AKh'].items() if key[2] == kk), sum(v for key, v in Ha.items() if key[2] == kk)))
print('  AKh k=2 (h,q):', fmtH(Ha, 2))
