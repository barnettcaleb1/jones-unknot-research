#!/usr/bin/env python3
"""Doubles: inequality and l-graded refinement.  Part 1: the doubles rebuilt by me (N from my own kht++ rerun, components traced by me).
Part 2: all doubles with stored data (N from stored cxBNr-c2-d via my parser, cross-checked with gtilde jset; Kh~(K) from my own kht++ run of the knot word)."""
import json, os, sys, collections, subprocess
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import gtilde
from chain import b_generators, kh_of_knot
from analyse import poly_l, pmulc, refinement, jones_from_kh
DBL = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots'
info = json.load(open('dbl_info.json'))
print('PART 1: rebuilt doubles')
for nm in sorted(info, key=lambda s: (int(s[1:].split('_')[0]), int(s.split('_')[1]))):
    n = b_generators('examples/dbl/%s_T/cxBNr-c2' % nm)
    ko = kh_of_knot('examples/dbl/%s_o/cxCKh-c2' % nm); kc = kh_of_knot('examples/dbl/%s_c/cxCKh-c2' % nm); kk = kh_of_knot('examples/dbl/%s_K/cxCKh-c2' % nm)
    assert jones_from_kh(ko) == [tuple(x) for x in info[nm]['jones_o']] and jones_from_kh(kc) == [tuple(x) for x in info[nm]['jones_c']]
    PN = poly_l(n); W = pmulc(poly_l(ko), poly_l(kc))
    good, divisible = refinement(PN, W)
    print('  %-6s dim N = %3d  rk Kh~(open) = %2d rk Kh~(closed) = %2d  product = %3d  Kh~(open)==Kh~(closed)==Kh~(K) bigraded: %s  admissible c: %s  2lk = %d  R: %s'
          % (nm, len(n), len(ko), len(kc), len(ko) * len(kc), ko == kc == kk, [c for c, R in good], info[nm]['lk2'], [sorted(R.items()) for c, R in good]))
    print('         l-distribution of N       :', sorted(PN.items()))
    print('         l-distribution of Kh~(x)Kh~:', sorted(W.items()))
