"""Fast version of the V3(B) theorem generator: candidate Farkas multipliers are precomputed per equation-coefficient pattern
(B enters only through right-hand sides and kappa = -(sigma(B)+1))."""
import sys, itertools
sys.path.insert(0,'.')
import v3b
from fractions import Fraction as Fr
_cand={}
def candidates(coeffs):
    """coeffs: tuple of (a,b,c,d) rows (last row = P-equation).  -> list of (ys, sup) with finite sup <= 0"""
    if coeffs in _cand: return _cand[coeffs]
    out=[]
    for ys in itertools.product(v3b.Y,repeat=len(coeffs)):
        if all(y==0 for y in ys): continue
        ca=sum(y*e[0] for y,e in zip(ys,coeffs)); cq=sum(y*e[1] for y,e in zip(ys,coeffs))
        cl=sum(y*e[2] for y,e in zip(ys,coeffs)); cL=sum(y*e[3] for y,e in zip(ys,coeffs))
        s=v3b.supg(ca,cq,cl,cL)
        if s is not None and s<=0: out.append((ys,s))
    out.sort(key=lambda x: x[1])   # most negative sup first
    _cand[coeffs]=out
    return out
def prove(Bdata,sigB,nmin):
    mB=sigB+1
    if mB==0: return False,['sigma(B) = sigma*']
    opn=[]
    for end in ('top','bot'):
        for asg in (1,-1):
            typ='+' if (end=='top')==(asg>0) else '-'
            for a3 in (True,False):
                if typ=='+' and not a3: continue
                for name,eqs,P0 in v3b.cases(Bdata[end],mB,typ,a3):
                    E=list(eqs)+[(0,1,0,0,P0)]
                    coeffs=tuple(tuple(Fr(x) for x in e[:4]) for e in E); rhs=[Fr(e[4]) for e in E]
                    ok=False
                    for ys,s in candidates(coeffs):
                        r=sum(y*x for y,x in zip(ys,rhs))
                        if r>nmin*s: ok=True; break
                    if not ok: opn.append((end,asg,a3,name))
    return (not opn),opn
if __name__=='__main__':
    import time; t=time.time()
    Z=(Fr(0),Fr(0),Fr(0),Fr(0))
    print('rational-only V3 re-derivation:',prove({'top':Z,'bot':Z},Fr(0),2),round(time.time()-t,1))
    t=time.time(); print(prove({'top':Z,'bot':Z},Fr(0),2),round(time.time()-t,2))
