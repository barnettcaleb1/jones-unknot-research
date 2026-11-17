"""Fast V3(B) theorem generator: deduplicated automaton edges, float screening of Farkas multipliers, EXACT (Fraction) verification
of every certificate actually used.  Same casework as v3b.py."""
import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen/c1copy')
import v3b
from fractions import Fraction as Fr
EDGES=sorted(set((k if isinstance(k,str) else repr(k), nk if isinstance(nk,str) else repr(nk), l1, l2) for (k,nk,l1,l2) in v3b.EDG))
STATES=sorted(set([e[0] for e in EDGES]+[e[1] for e in EDGES]))
SI={s:i for i,s in enumerate(STATES)}
EI=[(SI[a],SI[b],l1,l2) for a,b,l1,l2 in EDGES]
EF=[(a,b,float(l1),float(l2)) for a,b,l1,l2 in EI]
FIN={}
for k,v in v3b.FIN.items():
    FIN[SI[k if isinstance(k,str) else repr(k)]]=v
INIT=SI['init']
def sup_float(ca,cq,cl,cL):
    n=len(STATES); best=[None]*n; best[INIT]=0.0
    for it in range(n+2):
        ch=False
        for a,b,l1,l2 in EF:
            if best[a] is None: continue
            v=best[a]+ca*l1+cl*l2
            if best[b] is None or v>best[b]+1e-12: best[b]=v; ch=True
        if not ch: break
    else: return None
    return max(best[i]+cq*float(FIN[i][0])+cL*float(FIN[i][1]) for i in FIN if best[i] is not None)
_ex={}
def sup_exact(ca,cq,cl,cL):
    key=(ca,cq,cl,cL)
    if key in _ex: return _ex[key]
    n=len(STATES); best=[None]*n; best[INIT]=Fr(0)
    for it in range(n+2):
        ch=False
        for a,b,l1,l2 in EI:
            if best[a] is None: continue
            v=best[a]+ca*l1+cl*l2
            if best[b] is None or v>best[b]: best[b]=v; ch=True
        if not ch: break
    else:
        _ex[key]=None; return None
    r=max(best[i]+cq*FIN[i][0]+cL*FIN[i][1] for i in FIN if best[i] is not None); _ex[key]=r; return r
YG=[Fr(x) for x in (1,-1,0,Fr(1,2),Fr(-1,2),2,-2,10,-10,100,-100)]
_cand={}
def candidates(coeffs):
    if coeffs in _cand: return _cand[coeffs]
    out=[]
    for ys in itertools.product(YG,repeat=len(coeffs)):
        if all(y==0 for y in ys): continue
        c=[sum(y*e[j] for y,e in zip(ys,coeffs)) for j in range(4)]
        s=sup_float(*[float(x) for x in c])
        if s is not None and s<=1e-9: out.append((ys,tuple(c),s))
    out.sort(key=lambda x:x[2])
    _cand[coeffs]=out
    return out
def prove(Bdata,sigB,nmin,want_cert=False):
    mB=sigB+1
    if mB==0: return False,['sigma(B) = sigma*'],[]
    opn=[]; certs=[]
    for end in ('top','bot'):
        for asg in (1,-1):
            typ='+' if (end=='top')==(asg>0) else '-'
            for a3 in (True,False):
                if typ=='+' and not a3: continue
                for name,eqs,P0 in v3b.cases(Bdata[end],mB,typ,a3):
                    E=list(eqs)+[(0,1,0,0,P0)]
                    coeffs=tuple(tuple(Fr(x) for x in e[:4]) for e in E); rhs=[Fr(e[4]) for e in E]
                    ok=False
                    for ys,c,sf in candidates(coeffs):
                        r=sum(y*x for y,x in zip(ys,rhs))
                        if r>nmin*sf+1e-9 or (r>nmin*sf-1e-9 and sf<0):
                            s=sup_exact(*c)          # exact verification
                            if s is not None and s<=0 and r>nmin*s:
                                ok=True; certs.append((end,asg,a3,name,ys,s,r)); break
                    if not ok: opn.append((end,asg,a3,name))
    return (not opn),opn,certs
if __name__=='__main__':
    import time; t=time.time()
    Z=(Fr(0),Fr(0),Fr(0),Fr(0))
    ok,opn,c=prove({'top':Z,'bot':Z},Fr(0),2)
    print('rational-only V3 re-derivation (n_min=2):',ok,opn,round(time.time()-t,1))
    t=time.time(); ok,opn,c=prove({'top':Z,'bot':Z},Fr(0),1); print('n_min=1:',ok,opn,round(time.time()-t,2))
