"""Horizontal theorem generator H(B): closures X^mu Y^N (B u_1...u_n), rational non-integral u_i (n >= n_min), any N, all mu != 0.
Same weak-end casework and Farkas certificates as v3b3.py with (w_1, w_3)(mu) in place of (w_1, wV)(a)."""
import sys, itertools
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import v3b3, eng, ser, jets
from fractions import Fraction as Fr
def lj(f,end):
    d=ser.pdata(f,end,2); return d[0],jets.logs(d[2])
def wj(mu):
    a1,a3=eng.W(mu); out={}
    for end in ('top','bot'):
        d1,p=lj(a1,end); d3,q=lj(a3,end)
        out[end]=(p,q,d1,d3)
    sig=sum(out[e][0][0]-out[e][1][0] for e in out)
    dq={e:(out[e][3]-out[e][2]) for e in out}   # deg of -w1/w3 is d1-d3; q* degree
    dstar=(out['top'][2]-out['top'][3])-(out['bot'][2]-out['bot'][3])
    return out,sig,dstar
MUS=[1,-1,2,-2,3,-3,4,-4]
WJ={mu:wj(mu) for mu in MUS}
# stability of order-2 jets for |mu| >= 4
for mu in range(5,11):
    for s in (1,-1):
        o,sg,ds=wj(s*mu); r=WJ[4*s]
        assert all(o[e][0]==r[0][e][0] and o[e][1]==r[0][e][1] for e in o) and sg==r[1] and ds==r[2], ('unstable',s*mu)
def cases_pq(Bd,mB,p,q,allow_r1=True):
    import v3b
    (p1,p2),(q1,q2)=p,q
    ra,la,rb,lb=Bd
    K1=p1+ra; K2=q1+rb; M1=p2+la; M2=q2+lb
    P0=mB+(p1-q1)-rb+ra
    out=[]
    out.append(('d>=3',[(1,0,0,0,1-K1),(0,0,1,0,1-M1-Fr(1,2))],P0))
    for e in (1,-1):
        out.append(('d=2 e=%d'%e,[(1,0,0,0,1-K1),(0,0,1,0,1-M1-Fr(1,2)-e)],P0))
        X1=1-e
        out.append(('d=1 e=%d'%e,[(1,0,0,0,X1-K1),(e,e,1,0,1-M1-Fr(X1*X1,2)-e*K2)],P0))
        X2=1-e
        out.append(('d=-1 e=%d'%e,[(1,1,0,0,X2-K2),(e,0,1,1,1-M2-Fr(X2*X2,2)-e*K1)],P0))
        out.append(('d=-2 e=%d'%e,[(1,1,0,0,1-K2),(0,0,1,1,1-M2-Fr(1,2)-e)],P0))
    out.append(('d<=-3',[(1,1,0,0,1-K2),(0,0,1,1,1-M2-Fr(1,2))],P0))
    kap=K1-K2-P0
    X1=(2+kap)/2; X2=(2-kap)/2
    out.append(('d=0 r=0',[(2,1,0,0,2-K1-K2),(0,0,2,1,2-M1-M2-X1*X1/2-X2*X2/2)],P0))
    if allow_r1 and kap!=0:
        out.append(('d=0 r=1',[(-kap,0,0,1,M1-M2+kap*K1-kap*kap/2-kap)],P0))
    return out
def run_cases(cs,nmin):
    opn=[]
    for name,eqs,P0 in cs:
        E=list(eqs)+[(0,1,0,0,P0)]
        coeffs=tuple(tuple(Fr(x) for x in e[:4]) for e in E); rhs=[Fr(e[4]) for e in E]
        ok=False
        for ys,c,sf in v3b3.candidates(coeffs):
            r=sum(y*x for y,x in zip(ys,rhs))
            if r>nmin*sf+1e-9 or (r>nmin*sf-1e-9 and sf<0):
                s=v3b3.sup_exact(*c)
                if s is not None and s<=0 and r>nmin*s: ok=True; break
        if not ok: opn.append(name)
    return opn
def prove(Bdata,sigB,deltaB,nmin):
    """returns dict mu-class -> list of open items ([] = proved)"""
    res={}
    for mu in MUS:
        o,sgs,ds=WJ[mu]
        mB=sigB-sgs
        opn=[]
        if mB==0:
            exc=deltaB-ds          # the only n with a possible first-order two-ended tie
            if exc>=nmin: opn.append('two-ended tie possible at n=%s'%exc)
        for end in ('top','bot'):
            p,q,_,_=o[end]
            for nm in run_cases(cases_pq(Bdata[end],mB,p,q,allow_r1=(mB!=0)),nmin): opn.append(end+':'+nm)
        res[mu]=opn
    return res
if __name__=='__main__':
    for mu in MUS: print('mu',mu,'sigma*',WJ[mu][1],'delta*',WJ[mu][2],{e:(WJ[mu][0][e][0],WJ[mu][0][e][1]) for e in ('top','bot')})
    Z=(Fr(0),Fr(0),Fr(0),Fr(0))
    import time; t=time.time()
    r=prove({'top':Z,'bot':Z},Fr(0),0,2)
    print('rational-only (Q-MONT re-derivation, n>=2):',r,round(time.time()-t,1))
