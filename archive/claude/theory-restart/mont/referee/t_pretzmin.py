"""Pretzel minima: genuine pretzels (k=0), rows odd |r| in [3,RMAX], n=2..5, |mu|<=6: min span J (multisets of rows)."""
import itertools, sys, time
from rcore import *
from t_pretzel import rowvec
RMAX=int(sys.argv[1]) if len(sys.argv)>1 else 11
vals=[s*r for r in range(3,RMAX+1,2) for s in (1,-1)]
ch={r:(ach(rowvec(r)),bch(rowvec(r))) for r in vals}
t0=time.time()
for n in range(2,6):
    best=None; cnt=0
    for rows in itertools.combinations_with_replacement(vals,n):
        A=fprod([ch[r][0] for r in rows]); B=fprod([ch[r][1] for r in rows])
        for mu in [m for m in range(-6,7) if m]:
            G=ad(ml(w1(mu),A),ml(w3(mu),B)); s_=sp(G)-2; cnt+=1
            if best is None or s_<best[0]: best=(s_,mu,rows)
            if s_<3*n: print('PRETZEL SPAN < 3n',s_,mu,rows)
    print('n',n,'pretzels',cnt,'min span',best,'max(3n,4n-3)=',max(3*n,4*n-3),flush=True)
print('time',round(time.time()-t0,1))
