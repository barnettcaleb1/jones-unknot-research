"""cross-check of o3v's X1-SLICED tie formulation (used for |a| >= 5, n free) against the pinned lpgen-style T2 rows (|a| = 3):
run the sliced formulation with |a| = 3 data and n pinned to delta + 4; verdicts must agree class by class (sigma = -1 classes)."""
import sys, pickle, collections
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import o3v, lpg
from o3h import comb, rowsL
from multiprocessing import Pool
T=o3v.T
def sliced3(key,d3,end,a):
    cl,p3,q3=o3v.mkcl(end,a); (p1,p2),(q1,q2)=cl['p'],cl['q']
    ra,la,rb,lb=key[0] if end=='top' else key[1]
    l3a,l3b=(d3[0],d3[1]) if end=='top' else (d3[2],d3[3])
    tau=sum((k[3]-k[1]) for k in (key[0],key[1])); dl=Fr(key[3]); taus=Fr(-1,2)
    n=dl+4
    if n<1: return 'n<1'
    if taus-tau+n==0: return 'T3 possible'
    opn=[]
    for x in list(range(-T+1,T))+['big+','big-']:
        for sD in (1,-1):
            L=o3v.single(key,cl,1,npin=n)
            L.add_eq(L.zrow((0,1,0,0)),p1-q1-rb+ra)
            L.add_eq(comb((1,L.zrow((0,0,0,1))),(1,{L.iN:Fr(1)})),p2-q2-(lb-la)-taus+tau)
            L.add_ub({L.iN:Fr(-sD)},sD*(taus-tau)-Fr(1,2))
            RA,RQ=rowsL(L)
            X1=comb((1,RA(1))); cX1=p1+ra; D3f=comb((-1,RQ(3))); cD3=p3-q3+l3a-l3b; c0=taus-tau
            if isinstance(x,int):
                L.add_eq(X1,(1-x)-cX1); L.add_eq(comb((1,D3f),(-x,{L.iN:Fr(1)})),x*c0-cD3)
            else:
                s=1 if x=='big+' else -1
                L.add_ub({i:s*v for i,v in X1.items()},s*(1-cX1)-T)
                L.add_ub(comb((-sD*s,D3f),(T*sD,{L.iN:Fr(1)})),sD*s*cD3-T*sD*c0)
            if o3v.dec(L)!='closed': opn.append((x,sD))
    return 'T2 closed' if not opn else 'T2 open'
def job(j):
    key,d3=j; out=[]
    for end in ('top','bot'):
        for a in (3,-3):
            v1=o3v.tie(key,d3,end,a); v2=sliced3(key,d3,end,a)
            v1s='T2 closed' if v1.startswith('T2 closed') else ('T2 open' if v1.startswith('T2 open') else v1.split(' T3')[0])
            out.append((v1s,v2))
    return out
if __name__=='__main__':
    K3=pickle.load(open('gen1k3_R5_n2.pkl','rb')); O=pickle.load(open('o3h.pkl','rb'))
    keys=[k for k in sorted(set(r[0][0] for r in O['res']),key=str) if k[2]==-1]
    jobs=[(k,d3) for k in keys for d3 in K3.get(k,{})][:300]
    with Pool(2) as P: res=P.map(job,jobs)
    c=collections.Counter((a==b,a,b) for r in res for a,b in r)
    for k,v in c.most_common(): print(k,v)
