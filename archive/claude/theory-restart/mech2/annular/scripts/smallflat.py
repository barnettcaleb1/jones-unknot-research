#!/usr/bin/env python3
"""All formal flat configurations with unit arrows and dim N <= 13, tested against the (r, 2r-2) matching on closures of slope +-1/n."""
from b1match import *
import hf as HF
fn = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/5_2-2/cxBNr-c2-qs'
comps = parse_file(fn)
arc = [c for c in comps if not c['cyclic']][0]; sq = [c for c in comps if c['cyclic']][0]
print('--- l = 1, one square at the flat position, moved by s\'(-4,1) in the lattice, s\' even: (h,q)-shift (3+s\', 6) of the actual square')
for sp_ in (0, 2, -2, 4, -4):
    analyse("B1_s'=%d" % sp_, [to_typed(arc, name='arc'), to_typed(sq, shift=(3 + sp_, 6), name='sq')], ns=(1, 2))
print('--- l = 0 (arc a(0)), two squares at lattice offset s(-4,1), s odd: (h,q)-offset (s, 0)')
pt = HF.arc0(); pt.q = [0]; pt.d2 = [0]
for s in (1, -1, 3, -3):
    analyse('B0_s=%d' % s, [pt, to_typed(sq, name='sq'), to_typed(sq, shift=(s, 0), name='sq shifted')], ns=(1, 2))
