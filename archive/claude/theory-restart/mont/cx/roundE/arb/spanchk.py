"""min span a(B) over all ELIGIBLE depth-one boxes of gen1 n=2 (R(5)) -- needed for the n = 0 case of ARB-1 (mu = +-1 needs
span A >= 5 so that Tot = span A - 2 >= 3)."""
import sys, itertools, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import jbox, lib
R=lib.rational(5); P=[jbox.from_vec(r[1]) for r in R]
mn=None; cnt=collections.Counter()
for idx in itertools.combinations_with_replacement(range(len(R)),2):
    x=jbox.star(P[idx[0]],P[idx[1]])
    for N in range(-4,5):
        y=jbox.ypow(N,x)
        for m in [m for m in range(-7,8) if m]:
            try: key,el,info=jbox.signature(jbox.nest(m,y))
            except AssertionError: continue
            if key is None or not el: continue
            s=info['spana']; cnt[min(s,6)]+=1
            if mn is None or s<mn: mn=s
print('eligible depth-one n=2 boxes: min span a =',mn,' distribution (capped at 6):',sorted(cnt.items()))
