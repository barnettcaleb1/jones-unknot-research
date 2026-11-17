import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/fukaya/scratch')
from khtio import *
from collections import defaultdict
want = sys.argv[1:]
for name, bn, kh in all_tangles():
    if not any(w == name.split(':')[1] for w in want): continue
    print('=====', name)
    arc = [c for c in bn if not c.cyclic][0]
    print(' arc:', arc.word().replace('b-S>c-D>c-S2>c-D>c-S>b','R'), ' first gen (h,q)=', (arc.h[0], arc.q[0]), 'last', (arc.h[-1], arc.q[-1]))
    lev = defaultdict(list)
    for c in bn:
        if c.cyclic:
            d = Fraction(c.q[0], 2) - c.h[0]
            lev[d].append(c.q[0])
    print(' compact comps by level delta: (printed q of each)')
    for d in sorted(lev): print('    delta', d, sorted(lev[d]))
    sp = defaultdict(list); r = None
    for c in kh:
        L = parse_label(c.label)
        if L[0] == 's': sp[L[4]].append(int(L[3]))
        else: r = L
    print(' Khr rational:', r[2], 'q', r[3], 'delta', r[4])
    for d in sorted(sp): print('    level', d, sorted(sp[d]))
