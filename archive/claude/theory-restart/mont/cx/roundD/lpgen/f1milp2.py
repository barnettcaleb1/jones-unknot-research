"""MILP (integer k, n) check of the real-open order-3 F1 slices of f1uni_30_<TOPK>.pkl."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import f1uni, f1o3, lpg, classes, exact
from fractions import Fraction as Fr
TOPK=int(sys.argv[1])
res=pickle.load(open('f1uni_30_%d.pkl'%TOPK,'rb'))
items=exact.load_items()
S=f1uni.subclasses(items,classes.top(TOPK))+f1uni.subclasses(items,classes.d2pos())
CL={cl['name']:cl for cl in lpg.closure_classes()}
for name,m,q3,v,sol in res:
    if v!='OPEN': continue
    cl=CL[name]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m)
    r={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        vv=l2-f1o3.EL3[i]
        if vv: r[L.iF+i]=vv
    for jj,s in enumerate(lpg.FINS):
        if f1o3.FL3[s]: r[L.iG+jj]=-f1o3.FL3[s]
    for j,b in enumerate(S):
        d3=b.d3[cl['end']]; vv=-(d3[5]-d3[1])
        if vv: r[j]=vv
    L.add_eq(r,Fr(4,3)+q3-cl['p'][1]-m*m/2)
    rr=lpg.solve_primal(L,integral=True)
    print(name,'mB=%s q3=%s MILP status %d %s'%(m,q3,rr.status,rr.message[:60]),flush=True)
    if rr.x is not None and rr.status==0:
        print('   INTEGER OPEN:',{S[j].label:int(round(x)) for j,x in enumerate(rr.x[:L.nk]) if x>0.5},'n=',round(rr.x[L.iN],3),flush=True)
