"""Theorem generators V3(B) and H(B), version 2: adds the DELTA-LAW in the cases where both ends coincide in degree
(weak-end offset 0: cases 'd=0 r=0' and 'd=0 r=1'): then n = delta(B) - delta* exactly (horizontal; delta*(mu) from q*), and
n = delta(B) + |a| + 1 (vertical, delta*_V = -|a|-1), i.e. n >= delta(B) + 4 (|a| >= 3), = delta(B) + 4 at |a| = 3 (type '-').
With n pinned exactly, a certificate only needs rhs > n * sup(g) (any sign of sup)."""
import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen/c1copy')
import v3b, v3b3, h3b
from fractions import Fraction as Fr
def certify(name,eqs,P0,nmin,npin=None):
    E=list(eqs)+[(0,1,0,0,P0)]
    coeffs=tuple(tuple(Fr(x) for x in e[:4]) for e in E); rhs=[Fr(e[4]) for e in E]
    if npin is not None and npin<nmin: return True
    if npin is None:
        for ys,c,sf in v3b3.candidates(coeffs):
            r=sum(y*x for y,x in zip(ys,rhs))
            if r>nmin*sf+1e-9 or (r>nmin*sf-1e-9 and sf<0):
                s=v3b3.sup_exact(*c)
                if s is not None and s<=0 and r>nmin*s: return True
        return False
    # exact n: need candidates with finite sup of either sign
    for ys,c,sf in candidates_any(coeffs):
        r=sum(y*x for y,x in zip(ys,rhs))
        if r>npin*sf+1e-9:
            s=v3b3.sup_exact(*c)
            if s is not None and r>npin*s: return True
        # and the reversed inequality via -y is covered by the grid symmetry
    return False
_ca={}
def candidates_any(coeffs):
    if coeffs in _ca: return _ca[coeffs]
    out=[]
    for ys in itertools.product(v3b3.YG,repeat=len(coeffs)):
        if all(y==0 for y in ys): continue
        c=[sum(y*e[j] for y,e in zip(ys,coeffs)) for j in range(4)]
        s=v3b3.sup_float(*[float(x) for x in c])
        if s is not None: out.append((ys,tuple(c),s))
    out.sort(key=lambda x:x[2]); _ca[coeffs]=out; return out
def proveV(Bdata,sigB,deltaB,nmin):
    mB=sigB+1
    if mB==0: return False,['sigma(B) = sigma*']
    opn=[]
    for end in ('top','bot'):
        for asg in (1,-1):
            typ='+' if (end=='top')==(asg>0) else '-'
            for a3 in (True,False):
                if typ=='+' and not a3: continue
                for name,eqs,P0 in v3b.cases(Bdata[end],mB,typ,a3):
                    if name.startswith('d=0'):
                        if typ=='-' and a3: ok=certify(name,eqs,P0,nmin,npin=deltaB+4)
                        elif typ=='-': ok=certify(name,eqs,P0,max(nmin,deltaB+6))
                        else: ok=certify(name,eqs,P0,max(nmin,deltaB+4))
                    else: ok=certify(name,eqs,P0,nmin)
                    if not ok: opn.append((end,asg,a3,name))
    return (not opn),opn
def proveH(Bdata,sigB,deltaB,nmin):
    res={}
    for mu in h3b.MUS:
        o,sgs,ds=h3b.WJ[mu]
        mB=sigB-sgs; npin=deltaB-ds
        opn=[]
        if mB==0 and npin>=nmin: opn.append('two-ended tie possible at n=%s'%npin)
        for end in ('top','bot'):
            p,q,_,_=o[end]
            for name,eqs,P0 in h3b.cases_pq(Bdata[end],mB,p,q,allow_r1=(mB!=0)):
                ok=certify(name,eqs,P0,nmin,npin=npin) if name.startswith('d=0') else certify(name,eqs,P0,nmin)
                if not ok: opn.append(end+':'+name)
        res[mu]=opn
    return res
if __name__=='__main__':
    Z=(Fr(0),Fr(0),Fr(0),Fr(0))
    print('V rational-only n>=1:',proveV({'top':Z,'bot':Z},Fr(0),0,1))
    print('H rational-only n>=2:',proveH({'top':Z,'bot':Z},Fr(0),0,2))
