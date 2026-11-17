"""store the exact uniform Farkas certificates of THEOREM M300 (top-300 classes, >= 2 non-rational boxes, n >= 0) and re-verify them
from scratch with an independent exact check of the dual conditions."""
import sys, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import classes, runner, lpg, run_uni
from fractions import Fraction as Fr
S=classes.top(300)
t0=time.time(); store={}; bad=[]
for cl,nm,rows,m,nr in run_uni.jobs(S,0,2,None,8):
    L=lpg.build(S,cl,rows,0,kmin=2,slice_m=m,nrule=nr)
    f=lpg.farkas(L)
    if f is None or f=='unverified': bad.append((cl['name'],nm,m)); continue
    u,w,val=f
    # independent re-check: for x' >= 0 the combination sum u_i (A_eq x)_i + w_i (A_ub x)_i has nonnegative coefficients,
    # while the right-hand side combination is negative
    lb=L.lb; ok=True
    col={}
    for (r,b),ui in zip(L.eq,u):
        for j,v in r.items(): col[j]=col.get(j,0)+ui*v
    for (r,b),wi in zip(L.ub,w):
        assert wi>=0
        for j,v in r.items(): col[j]=col.get(j,0)+wi*v
    rhs=sum(ui*(b-sum(v*lb[j] for j,v in r.items())) for (r,b),ui in zip(L.eq,u))+sum(wi*(b-sum(v*lb[j] for j,v in r.items())) for (r,b),wi in zip(L.ub,w))
    if any(c<0 for c in col.values()) or not rhs<0: bad.append((cl['name'],nm,m,'recheck')); continue
    nz=sum(1 for x in list(u)+list(w) if x)
    store[(cl['name'],nm,m)]=dict(u=u,w=w,val=val,nonzero=nz,maxden=max(x.denominator for x in list(u)+list(w)))
pickle.dump(store,open('certs_M300.pkl','wb'))
print('certificates stored',len(store),'failed',bad,'max denominator',max(v['maxden'] for v in store.values()),'time',round(time.time()-t0,1))
