#!/usr/bin/env python3
"""Formal flat object C3 = arc of 5_2 second inversion + its actual square Y + the shift of Y by (h,q) = (-1,0) [X, cancels Y in J]
+ the B1 square (shift (3,6)).  dim N = 15.  Daemi matching on closures of slope +-1/n."""
from b1match import *
fn = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/5_2-2/cxBNr-c2-qs'
comps = parse_file(fn)
arc = [c for c in comps if not c['cyclic']][0]; sq = [c for c in comps if c['cyclic']][0]
def obj(shifts): return [to_typed(arc, name='arc')] + [to_typed(sq, shift=s, name='sq%s' % (s,)) for s in shifts]
analyse('C3: squares Y, Y+(-1,0), Y+(3,6)', obj([(0, 0), (-1, 0), (3, 6)]))
analyse("C3': squares Y, Y+(1,0), Y+(3,6)", obj([(0, 0), (1, 0), (3, 6)]))
