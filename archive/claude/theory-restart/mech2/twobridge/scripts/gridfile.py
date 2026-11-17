#!/usr/bin/env python3
"""lattice picture of N from a chain file. usage: gridfile.py CHAINFILE ..."""
import sys,os,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import chain, run as R
from hull_formula import hull,edges
for fn in sys.argv[1:]:
    rec={'word':fn,'bn':[l for l in open(fn,encoding='utf-8').read().splitlines() if not l.startswith('%')]}
    an=R.analyse(rec)
    print('==',fn); print('  arc moves:',' '.join(an['moves']),' tail',an['tail'],' x0',an['x0'],' squares',sorted(an['squares']),'other',an['other'])
    print(R.grid(an)); print('  J =',R.Jpoly(an))
    d=collections.Counter(an['N'])
    if len(d)>2: print('  hull:',[(e[0],e[1]) for e in edges(hull(list(d)))])
