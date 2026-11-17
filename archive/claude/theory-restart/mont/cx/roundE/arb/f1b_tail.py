"""(4b) lpgen's F1' tail: 'd=1 e=-1' at H mu=+2 top / mu=-2 bottom with mB <= -31 (>= 15 aligned a-potential boxes).
Order-3 equality (lpgen 5.9, PROVED): LHS' = mB^2/2 - 4/3 - p3 + q2.  Step 1: asymptotic slope A* = sup dLHS'/d|mB| over the
recession cone of the order-2 F1' region (LP).  Step 2: exact bound LHS' <= A|mB| + b' (A > A*), so |mB| < A + sqrt(A^2 + 2(b'+c0)).
Step 3: order-3 slices from 31 up to that threshold."""
import sys, math, time, pickle
LPG='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'
sys.path.insert(0,LPG); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import numpy as np
from scipy.optimize import linprog
import f1uni, f1b, lpg, classes, exact, runner
from fractions import Fraction as Fr
t0=time.time()
items=exact.load_items()
S=f1uni.subclasses(items,classes.top(300))+f1uni.subclasses(items,classes.d2pos())
print('subclasses',len(S),round(time.time()-t0,1),flush=True)
CL={cl['name']:cl for cl in lpg.closure_classes()}
out={}
for name,sgn in (('H mu=+2 top',-1),('H mu=-2 bot',-1)):
    cl=CL[name]; rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=1 e=-1']
    ex=[('ub',{j:-sgn*c.sig for j,c in enumerate(S) if c.sig},-31-sgn*cl['sigstar'])]
    L=lpg.build(S,cl,rows,0,kmin=1,extra=ex)
    r3=f1b.row3(L,S,cl)
    # recession cone: A_eq d = 0, A_ub d <= 0 (only rows homogeneous), d >= 0; normalise |mB| direction: -sgn*sigma.dk... |mB|=sgn*mB
    Aeq,beq=lpg._mat(L.eq,L.nv); Aub,bub=lpg._mat(L.ub,L.nv)
    nrm=np.zeros(L.nv)
    for j,c in enumerate(S): nrm[j]=float(sgn*c.sig)      # d(|mB|) = sgn * sigma.dk
    c=np.zeros(L.nv)
    for j,v in r3.items(): c[j]=-float(v)                 # maximise dLHS'
    res=linprog(c,A_eq=np.vstack([Aeq,nrm]),b_eq=np.concatenate([np.zeros(len(beq)),[1.0]]),A_ub=Aub,b_ub=np.zeros(len(bub)),
                bounds=[(0,None)]*L.nv,method='highs')
    print(name,'recession LP status',res.status,'A* =',None if res.status!=0 else -res.fun,flush=True)
    # rays with d|mB| = 0 and dLHS' > 0 ?
    res0=linprog(c,A_eq=np.vstack([Aeq,nrm]),b_eq=np.concatenate([np.zeros(len(beq)),[0.0]]),A_ub=np.vstack([Aub,-c[None,:]]),
                 b_ub=np.concatenate([np.zeros(len(bub)),[1.0]]),bounds=[(0,None)]*L.nv,method='highs')
    print('   rays with d|mB| = 0: max dLHS\' (capped at 1) =',None if res0.status!=0 else -res0.fun,flush=True)
    if res.status==0:
        d=res.x; sup=[(S[j].label,round(d[j],4)) for j in range(L.nk) if d[j]>1e-9]
        print('   optimal ray (classes):',sup[:12],'n',round(d[L.iN],4),flush=True)
    out[name]=dict(Astar=None if res.status!=0 else -res.fun, ray0=None if res0.status!=0 else -res0.fun)
pickle.dump(out,open('f1b_tail_step1.pkl','wb'))
print('time',round(time.time()-t0,1))
