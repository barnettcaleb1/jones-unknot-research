"""probe the integer F1' survivors: 3 x d2_497 (mu = +2, top) / 3 x d2_460 (mu = -2, bottom): LP solution (n, rational sums)
and EXACT search of the products (all boxes of the subclass, n rational boxes from R(4)/R(5) around the LP value)."""
import sys, pickle, itertools, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import f1uni, f1b, f1o3, lpg, classes, exact, runner, lib, eng
from fractions import Fraction as Fr
items=exact.load_items()
S=f1uni.subclasses(items,classes.top(300))+f1uni.subclasses(items,classes.d2pos())
CL={cl['name']:cl for cl in lpg.closure_classes()}
lab={b.label:j for j,b in enumerate(S)}
for name,lb,m in (('H mu=+2 top','d2_497/16',-7),('H mu=-2 bot','d2_460/12',-7)):
    cl=CL[name]; j=lab[lb]; b=S[j]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=1 e=-1']
    L=lpg.build(S,cl,rows,0,fixk={j:3},kmin=0,slice_m=Fr(m))
    L.add_eq(f1b.row3(L,S,cl),Fr(m*m,2)-Fr(4,3)-f1b.p3of(cl)+cl['q'][1])
    r=lpg.solve_primal(L)
    print(name,lb,'status',r.status,'n=',None if r.x is None else round(r.x[L.iN],3))
    # boxes in this subclass
    xs=[x for x in classes.SIGS[b.key] if (lambda d3:(d3['top'][2],d3['top'][5],d3['bot'][2],d3['bot'][5]))(f1o3.boxdata3(items[x][2]))==(b.d3['top'][2],b.d3['top'][5],b.d3['bot'][2],b.d3['bot'][5])]
    print('   boxes in subclass',len(xs),xs[:6],'tree',items[xs[0]][1])
    # min n over the LP region
    for nn in range(0,8):
        L2=lpg.build(S,cl,rows,nn,fixk={j:3},kmin=0,slice_m=Fr(m)); L2.add_eq({L2.iN:Fr(1)},Fr(nn))
        L2.add_eq(f1b.row3(L2,S,cl),Fr(m*m,2)-Fr(4,3)-f1b.p3of(cl)+cl['q'][1])
        print('   n=%d feasible: %s'%(nn,lpg.solve_primal(L2).status==0))
