"""ORDER-3 cut for the universal open case F1 ('d=-1 e=-1': offset -1 at the weak end, eps = -1).  PROVED necessary condition:
 F/(lc t^d) = s2 - u s1 = 1 + u + u^2 + 0 u^3 + ...  with X2 = l1(s2) = 2 forces  l2(s2) = X1 - 1  and
 l3(s2) - l2(s1) = (X1 - 2)^2/2 - 4/3  >=  -4/3.
 Rational third-order data: l3 of D on each automaton edge (a function of (state, next, l1, l2), CHECKED) and l3(q) = FIN[s][2].
 Box-level third-order data from exact vectors.  Closure third-order jets: V '+' q3 = 1/3, '-' q3 = 0; H from eng.W (|mu| >= 5 class
 added at order 3)."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import lpg, jauto, v3b3, eng, ser, jets
from fractions import Fraction as Fr
order,trans=jauto.build(3,verbose=False)
L3={}
for (k,m),(Dj,nk) in trans.items():
    d,lc,s=jauto.norm_jet(Dj); l=jauto.logs(s)
    key=(v3b3.SI[k if isinstance(k,str) else repr(k)],v3b3.SI[nk if isinstance(nk,str) else repr(nk)],l[0],l[1])
    assert L3.get(key,l[2])==l[2]; L3[key]=l[2]
EL3=[L3[(a,b,l1,l2)] for (a,b,l1,l2) in lpg.EI]
FL3={s:v3b3.FIN[s][2] for s in lpg.FINS}
def lj(f,end,K=3):
    d=ser.pdata(f,end,K); return jets.logs(d[2])
def boxdata3(v):
    """per end: (l1a,l2a,l3a,l1b,l2b,l3b)"""
    return {e:lj(v[0],e)+lj(v[1],e) for e in ('top','bot')}
def wq3(cl):
    if cl['kind']=='V': return Fr(1,3) if cl['typ']=='+' else Fr(0), Fr(0)
    mu=cl['mu']; mus=[mu] if abs(mu)<4 else [mu]
    w1,w3=eng.W(mu); return lj(w3,cl['end'])[2], lj(w1,cl['end'])[2]
def f1_lp(boxes,cl,nmin=0,mu5=False,eq=True):
    """boxes: list of (Cls with .top/.bot order-2 data, d3 = boxdata3); fixed multiplicity 1 each.  Returns LP with the order-3 cut."""
    S=[b[0] for b in boxes]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    L=lpg.build(S,cl,rows,nmin,fixk={j:1 for j in range(len(S))})
    q3,_=wq3(cl)
    if mu5: q3=lj(eng.W(5 if cl['mu']>0 else -5)[1],cl['end'])[2]
    p2=cl['p'][1]
    # -L3a - L3q + L_a - sum_j (l3b_j - l2a_j) k_j <= 4/3 + q3 - p2
    r={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=l2-EL3[i]
        if v: r[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        if FL3[s]: r[L.iG+jj]=-FL3[s]
    for j,b in enumerate(boxes):
        d3=b[1][cl['end']]; v=-(d3[5]-d3[1])
        if v: r[j]=v
    # X1 is PINNED in F1: alpha + P = 2 - K2 and P = P0 give X1 = 2 - mB, so the order-3 condition is the EQUALITY
    #   l3(s2) - l2(s1) = mB^2/2 - 4/3
    mB=sum(b[0].sig for b in boxes)-cl['sigstar']
    if eq: L.add_eq(r,Fr(4,3)+q3-p2-mB*mB/2)
    else: L.add_ub(r,Fr(4,3)+q3-p2)
    return L
