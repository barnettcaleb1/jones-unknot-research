import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/fukaya/scratch')
from khtio import *
from collections import Counter, defaultdict
ROW = 'b-S>c-D>c-S2>c-D>c-S>b'
arcshapes = Counter(); ex = {}
pairs = Counter(); pair_ex = defaultdict(list)
ncomp = Counter()
for name, bn, kh in all_tangles():
    arc = [c for c in bn if not c.cyclic][0]
    cps = [c for c in bn if c.cyclic]
    w = arc.word()
    w2 = w.replace(ROW, 'R')
    arcshapes[w2] += 1; ex.setdefault(w2, name)
    ncomp[len(cps)] += 1
    # relative positions between compact components: (dq, dh)
    for i in range(len(cps)):
        for j in range(len(cps)):
            if i == j: continue
            dq = cps[j].q[0] - cps[i].q[0]; dh = cps[j].h[0] - cps[i].h[0]
            dd = Fraction(dq, 2) - dh
            if dd in (0, 1) and abs(dq) <= 12:
                if dd == 0 and dq < 0: continue
                pairs[(dq, dh)] += 1
                if len(pair_ex[(dq, dh)]) < 3: pair_ex[(dq, dh)].append(name)
print('number of compact comps distribution', sorted(ncomp.items()))
print('--- arc shapes (R = row b-S>c-D>c-S2>c-D>c-S>b)')
for w, v in sorted(arcshapes.items(), key=lambda x: (len(x[0]), x[0])): print(v, ex[w], w)
print('--- compact-compact relative positions (dq, dh) with ddelta in {0,1}, |dq|<=12:  count, examples')
for k, v in sorted(pairs.items(), key=lambda x: (Fraction(x[0][0],2)-x[0][1], x[0][0])): print(k, 'ddelta', Fraction(k[0],2)-k[1], v, pair_ex[k])
