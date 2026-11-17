import sys, pickle, itertools, random; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from load import *
allp=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts/allp.pkl','rb'))
def cen2(p):
    """specials as (c'', 2d'') integer pairs"""
    j=int(p['j']); S=Counter()
    for (c,d),m in p['S'].items(): S[(c-24*j, 2*(d-4*j)-1)]+=m
    return S
def Jset(S,k):
    J=Counter(); J[(2*k,0)]+=1
    for (c,e),m in S.items():
        J[(c+4,(e-1)//2)]+=m; J[(c-4,(e+1)//2)]+=m
    return J
def prof(S):
    lv=sorted(set(d for c,d in S))
    return [(d,min(c for c,dd in S if dd==d),max(c for c,dd in S if dd==d)) for d in lv]
def tilt(S,step):
    pr=prof(S)
    return all(pr[i+1][0]-pr[i][0]==step for i in range(len(pr)-1)) and all(pr[i+1][1]<pr[i][1] and pr[i+1][2]<pr[i][2] for i in range(len(pr)-1))
def overhang(S,k):
    if not S: return True
    if k>0: return max(c for c,d in S)>=2*k+2
    if k<0: return min(c for c,d in S)<=2*k-2
    return True
def anchor(S):
    lv=[e for c,e in S]
    if not lv: return True
    return min(lv)<=1 and max(lv)>=-1
def sumrule(S1,k1,S2,k2):
    S=Counter()
    for (c,e),m in S1.items(): S[(c+2*k2,e)]+=m
    for (c,e),m in S2.items(): S[(c+2*k1,e)]+=m
    for (c1,e1),m1 in S1.items():
        for (c2,e2),m2 in S2.items():
            S[(c1+c2+4,e1+e2)]+=m1*m2      # centered: (c1+c2+4, d1+d2-1/2) -> 2d = e1+e2+2-1-... see check below
            S[(c1+c2-4,e1+e2+2)]+=m1*m2
    return S
# NOTE on levels: e=2d''. pair product in centered coords: (c1+c2+4, d1+d2-1/2) and (c1+c2-4, d1+d2+1/2); with e=2d'': e1+e2-1 and e1+e2+1.
def sumrule(S1,k1,S2,k2):
    S=Counter()
    for (c,e),m in S1.items(): S[(c+2*k2,e)]+=m
    for (c,e),m in S2.items(): S[(c+2*k1,e)]+=m
    for (c1,e1),m1 in S1.items():
        for (c2,e2),m2 in S2.items():
            S[(c1+c2+4,e1+e2-1)]+=m1*m2
            S[(c1+c2-4,e1+e2+1)]+=m1*m2
    return S
recs=[]; seen=set()
for tag,name,p in allp:
    S=cen2(p); key=(p['k'],tuple(sorted(S.items())))
    if key in seen: continue
    seen.add(key); recs.append((tag,name,p['k'],S))
print('distinct data records',len(recs))
c=Counter()
for tag,name,k,S in recs:
    if not S: print('EMPTY',tag,name,k)
    c[('tiltS',tilt(S,2))]+=1; c[('Jtilt',tilt(Jset(S,k),1))]+=1; c[('anchor',anchor(S))]+=1; c[('overhang',overhang(S,k))]+=1
    if not anchor(S): print('ANCHOR FAIL',tag,name,k,prof(S))
print(sorted(c.items()))
# sanity: sum rule reproduces the composite 3_1#3_1
S31=[S for tag,name,k,S in recs if name=='3_1'][0]
print('3_1#3_1 by rule:',sorted(sumrule(S31,-4,S31,-4).items()))
# virtual sums of all pairs (incl. mirrors)
def mir(S,k): return Counter({(-c,-e):m for (c,e),m in S.items()}),-k
pool=[]
for tag,name,k,S in recs:
    pool.append((name,k,S)); S2,k2=mir(S,k); pool.append((name+'m',k2,S2))
print('pool',len(pool))
res=Counter(); bad=[]
small=[x for x in pool if sum(x[2].values())<=40]
print('pool with <=40 specials',len(small))
for (n1,k1,S1),(n2,k2,S2) in itertools.combinations_with_replacement(small,2):
    S=sumrule(S1,k1,S2,k2); k=k1+k2
    t=tilt(S,2); jt=tilt(Jset(S,k),1); o=overhang(S,k); a=anchor(S)
    res[(t,jt,o,a)]+=1
    if not (t and jt and o and a) and len(bad)<10: bad.append((n1,n2,t,jt,o,a))
print('virtual sums (tiltS,Jtilt,overhang,anchor):',sorted(res.items())); print(bad)
