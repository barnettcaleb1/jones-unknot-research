#!/usr/bin/env python3
"""D-domino decomposition of N(T_K) in coordinates (H = a+3b + 2*s0h, level b) vs the tensor-square dominoes of Kh~(K)."""
import sys,os,glob,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import lattice
from habiro import knot_kh,D
def kh_struct(name):
    kh=knot_kh(name)
    free=[(h,q) for h,q,k in kh if k=='free'][0]
    tor=sorted(h-free[0] for h,q,k in kh if k=='tor')
    doms=tor[0::2]
    for i in range(0,len(tor),2): assert tor[i+1]==tor[i]+1
    # dominos: but several at same position possible; pair as (h,h+1) by H-arrows: knot_kh appends pairs consecutively
    doms=[]
    khl=[(h-free[0]) for h,q,k in kh if k=='tor']
    doms=sorted(khl[0::2])
    return free,doms
def n_dominoes(name):
    rho,arc,sq,other=lattice(os.path.join(D,name,'cxBNr-c2-d'))
    doms=[]; pt=None
    # arc: D-dominoes are consecutive arc points differing by (1,0)
    used=set()
    for i in range(len(arc)-1):
        (a,b),(a2,b2)=arc[i],arc[i+1]
        if b==b2 and abs(a-a2)==1:
            doms.append((min(a,a2),b)); used.add(i); used.add(i+1)
    rest=[arc[i] for i in range(len(arc)) if i not in used]
    assert len(rest)==1,rest
    for (a,b) in sq:
        doms.append((a,b)); doms.append((a,b+1))
    return rest[0],doms,arc,sq
def show(name):
    free,doms=kh_struct(name)
    pt,nd,arc,sq=n_dominoes(name)
    # shift: a+3b = H + const ; determine const from extremes
    hs=[0]+[d for d in doms]+[d+1 for d in doms]
    T=sorted(x+y for x in hs for y in hs)
    pts=[pt]+[(a,b) for a,b in nd]+[(a+1,b) for a,b in nd]
    Nl=sorted(a+3*b for a,b in pts)
    shift=Nl[0]-T[0]
    assert [v+shift for v in T]==Nl
    print('==',name,' Kh~: free at 0, dominoes at',doms,'  (a+3b = H + %d)'%shift, ' unpaired point at (H,level)=',(pt[0]+3*pt[1]-shift,pt[1]))
    td=collections.defaultdict(list)
    for d in doms: td[d]+= ['g*%d'%d,'%d*g'%d]
    for d in doms:
        for e in doms:
            td[d+e].append('%d*%d'%(d,e)); td[d+e+1].append("%d*%d'"%(d,e))
    nn=collections.defaultdict(list)
    for a,b in nd: nn[a+3*b-shift].append(b)
    for H in sorted(set(td)|set(nn)):
        print('   H=%3d  levels %-28s  tensor dominoes %s'%(H,sorted(nn[H]),' '.join(td[H])))
for n in sys.argv[1:]: show(n)
