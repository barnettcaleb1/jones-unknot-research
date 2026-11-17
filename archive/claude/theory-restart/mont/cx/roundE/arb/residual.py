"""NORMALISATION test: residual R(F_m(Y^N P)) := (log-jet of a' minus log-jet of a_P (order 2) at both ends,
q'-data (deg, lc, l1, l2) at both ends).  By rule R3, R depends only on the slope state of P and m.  Count distinct residuals
for n = 2, 3 (R(5)) and n = 4, 5 (R(4)), split generic / special products (z_P of order one at both ends or not)."""
import sys, itertools, random, collections, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import jbox, lib
from jauto import logs
from fractions import Fraction as Fr
MS=[m for m in range(-7,8) if m]; NS=list(range(-4,5))
def ldata(s,K=2):
    d,c,ser=jbox.endjet(s,K); return d,c,logs(ser)
def resid(y,z):
    out=[]
    for e in ('top','bot'):
        dA,cA,lA=ldata(y[e][0]); da,ca,la=ldata(z[e][0]); db,cb,lb=ldata(z[e][1])
        out.append((la[0]-lA[0],la[1]-lA[1],db-da,cb/ca,lb[0]-la[0],lb[1]-la[1]))
    return tuple(out)
def zshape(y):
    # generic iff z = (q-1)/(q-e2) of order one at both ends: top deg q not in {0 (lc 1), -1 (lc -1)}; bottom ord q not in {0 (lc 1), 1 (lc -1)}
    sh=[]
    for e in ('top','bot'):
        da,ca,_=jbox.endjet(y[e][0],0); db,cb,_=jbox.endjet(y[e][1],0)
        dq=db-da; cq=Fr(cb)/Fr(ca)
        e2deg=-1 if e=='top' else -1     # reflected bottom: e2(1/t) = -t/(1+t^2) again, top degree -1
        sh.append('near1' if (dq==0 and cq==1) else ('neare2' if (dq==e2deg and cq==-1) else 'gen'))
    return tuple(sh)
random.seed(3)
seen={}
for L,n,samp in ((5,2,None),(5,3,2500),(4,4,1500),(4,5,1500)):
    R=lib.rational(L); P=[jbox.from_vec(r[1]) for r in R]
    idxs=list(itertools.combinations_with_replacement(range(len(R)),n))
    if samp and len(idxs)>samp: idxs=random.sample(idxs,samp)
    cnt=collections.Counter(); new=collections.Counter(); tot=collections.Counter()
    for idx in idxs:
        x=P[idx[0]]
        for i in idx[1:]: x=jbox.star(x,P[i])
        for N in NS:
            y=jbox.ypow(N,x)
            try: sh=zshape(y)
            except AssertionError: continue
            g='gen' if sh==('gen','gen') else 'special'
            for m in MS:
                try:
                    z=jbox.nest(m,y); r=resid(y,z)
                except AssertionError: continue
                except Exception: continue
                tot[g]+=1
                key=(g,m,r)
                if key not in seen: seen[key]=(L,n); new[g]+=1
    print('R(%d) n=%d (%s multisets): boxes gen %d special %d | NEW residuals gen %d special %d | cumulative distinct gen %d special %d'%(
        L,n,len(idxs),tot['gen'],tot['special'],new['gen'],new['special'],sum(1 for k in seen if k[0]=='gen'),sum(1 for k in seen if k[0]=='special')),flush=True)
pickle.dump(seen,open('residual.pkl','wb'))
