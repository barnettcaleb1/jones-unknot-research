#!/usr/bin/env python3
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts')
from hfk_word import pd_of_word
import spherogram
for w in sys.argv[1:]:
    pd=pd_of_word(w)
    K=spherogram.Link(pd)
    n0=len(K.crossings)
    K.simplify('basic')
    print(w,'crossings',n0,'->',len(K.crossings))
    h=K.knot_floer_homology()
    print({k:h[k] for k in h if k!='ranks'})
    print('ranks',sorted(h['ranks'].items()))
    print('PD',K.PD_code())
