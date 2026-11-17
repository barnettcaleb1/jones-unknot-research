import sys, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import diag, lp, words
def vstr(V): return ' '.join('%+d*t^%d'%(c,e) for e,c in sorted(V.items()))
names={}
def name(V):
    key=tuple(sorted(V.items()))
    known={((0,1),):'0_1', ((1,1),(3,1),(4,-1)):'3_1(t+t3-t4)', ((-4,-1),(-3,1),(-1,1)):'3_1*(mirror)',
           ((-2,1),(-1,-1),(0,1),(1,-1),(2,1)):'4_1'}
    return known.get(key,vstr(V))
cands=['s.r2.r1.y0.y2.u1.u1','s.r2.r1.x0.x2.u1.u1','s.l1.y0.y1.u1','s.l1.y1.y0.y1.u1','s.l1.y0.y1.y0.u1',
       's.l1.x0.y1.u1','s.l1.y1.x0.y1.u1','s.l1.y0.x1.y0.u1','s.l1.y1.y1.y0.u1','s.l1.y0.y0.y1.u1','s.l1.y0.y0.y0.y1.u1',
       's.l1.y1.y1.y1.y0.u1','s.l1.y0.y1.y1.u1','s.l1.x0.y1.y1.u1','s.l1.y1.x0.x0.y1.u1','s.l1.y0.y1.y1.y0.u1']
for w in cands:
    J=lp.J(w)
    inv=diag.all_invariants(w)
    if inv is None or J is None: print(w,'not a knot'); continue
    print(w,' K=',name(inv['K']['V']),' Kin=',name(inv['Kin']['V']),' Kout=',name(inv['Kout']['V']),
          ' Uin=',name(inv['Uin']['V']),' Uout=',name(inv['Uout']['V']),' J=',vstr(J))
