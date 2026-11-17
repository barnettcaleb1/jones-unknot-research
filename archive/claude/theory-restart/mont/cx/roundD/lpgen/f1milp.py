"""integer check (MILP) of the two real-open order-3 F1 slices; also rerun of f1uni at larger |mB|."""
import sys, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import f1uni, f1o3, lpg, classes, exact
from fractions import Fraction as Fr
items=exact.load_items()
S=f1uni.subclasses(items,classes.top(50))+f1uni.subclasses(items,classes.d2pos())
CL={cl['name']:cl for cl in lpg.closure_classes()}
for name in ('V top a+ typ+ |a|=3','V bot a- typ+ |a|=3'):
    cl=CL[name]; m=Fr(4); q3=Fr(1,3)
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m)
    r={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=l2-f1o3.EL3[i]
        if v: r[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        if f1o3.FL3[s]: r[L.iG+jj]=-f1o3.FL3[s]
    for j,b in enumerate(S):
        d3=b.d3[cl['end']]; v=-(d3[5]-d3[1])
        if v: r[j]=v
    L.add_eq(r,Fr(4,3)+q3-cl['p'][1]-m*m/2)
    res=lpg.solve_primal(L,integral=True)
    print(name,'mB=4 MILP status',res.status,res.message[:80])
    if res.x is not None:
        print('   integer solution:',{S[j].label:int(round(v)) for j,v in enumerate(res.x[:L.nk]) if v>0.5},'n=',round(res.x[L.iN],3))
