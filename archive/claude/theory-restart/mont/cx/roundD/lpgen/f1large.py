"""F1, large mB: on the ORDER-2 F1 region (uniform over all multisets of the 1,200 order-3 subclasses, n >= 0), bound
LHS := l3(s2) - l2(s1) - (q3 - p2) = L3a + L3q - L_a + sum_j k_j (l3b_j - l2a_j)  by  a*mB + b  (exact Farkas certificate for
LHS - a*mB >= b' infeasible).  The order-3 equality LHS = mB^2/2 - 4/3 - q3 + p2 then bounds mB."""
import sys, math, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import f1uni, f1o3, lpg, classes, exact, eng
from fractions import Fraction as Fr
import numpy as np
items=exact.load_items()
TOPK=int(sys.argv[2]) if len(sys.argv)>2 else 50
S=f1uni.subclasses(items,classes.top(TOPK))+f1uni.subclasses(items,classes.d2pos())
A=Fr(int(sys.argv[1])) if len(sys.argv)>1 else Fr(4)
def lhs_row(L,cl):
    r={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=f1o3.EL3[i]-l2
        if v: r[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        if f1o3.FL3[s]: r[L.iG+jj]=f1o3.FL3[s]
    for j,b in enumerate(S):
        d3=b.d3[cl['end']]; v=d3[5]-d3[1]
        if v: r[j]=r.get(j,0)+v
    return r
worst=0; t0=time.time()
for cl in lpg.closure_classes():
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    q3s=[f1o3.wq3(cl)[0]]
    if cl['kind']=='H' and abs(cl['mu'])==4: q3s.append(f1o3.lj(eng.W(5 if cl['mu']>0 else -5)[1],cl['end'])[2])
    # maximise LHS - A*mB over the order-2 F1 region (mB = sigma.k - sigstar >= 31 side only)
    L=lpg.build(S,cl,rows,0,kmin=1,extra=[('ub',{j:-c.sig for j,c in enumerate(S) if c.sig},-31-cl['sigstar'])])
    r=lhs_row(L,cl)
    obj={j:-float(v) for j,v in r.items()}
    for j,c in enumerate(S):
        if c.sig: obj[j]=obj.get(j,0)+float(A*c.sig)
    res=lpg.solve_primal(L,obj=obj)
    if res.status==3: print(cl['name'],'UNBOUNDED'); continue
    if res.status==2: print(cl['name'],'region empty for mB>=31'); continue
    opt=-res.fun+float(A*cl['sigstar'])        # max of LHS - A*mB
    bp=Fr(math.floor(opt)+1)
    # exact certificate: LHS - A*(sigma.k - sigstar) >= bp infeasible
    r2={j:-v for j,v in r.items()}
    for j,c in enumerate(S):
        if c.sig: r2[j]=r2.get(j,0)+A*c.sig
    L.add_ub(r2,-bp+A*cl['sigstar'])
    f=lpg.farkas(L)
    okc=isinstance(f,tuple)
    for q3 in q3s:
        c0=Fr(4,3)+q3-cl['p'][1]
        # m^2/2 - c0 - A m < bp  =>  m < A + sqrt(A^2 + 2(bp + c0))
        disc=A*A+2*(bp+c0)
        mmax=float(A)+math.sqrt(float(disc)) if disc>=0 else float('-inf')
        worst=max(worst,mmax)
        print('%-24s q3=%s  max(LHS - %s mB) = %.3f  cert(<%s) %s  => mB < %.2f'%(cl['name'],q3,A,opt,bp,'EXACT' if okc else f,mmax),flush=True)
print('F1 at order 3 impossible for mB >= max(31, %.2f); time %.1f'%(worst,time.time()-t0))
