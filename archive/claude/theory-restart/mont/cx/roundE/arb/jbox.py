"""ENGINE ARB: jet-level box arithmetic at BOTH ends (precision-tracked truncated Laurent series; jauto.S semantics:
coefficients exact for degrees >= P).  Bottom end = top expansion of the reflected polynomial f(1/t).
Rules (all exact identities in Lambda^2, channel coords v = (a,b)):
  star: (a,b)*(a',b') = (aa', bb');  Y^N: b -> t^-3N b;  X^mu: alpha = (t a + (1+t^2) b)/Phi3, beta = (a-b)/Phi3,
  X^mu v = alpha (1,1) + (-t)^mu beta (1+t^2, -t);  nesting F_m = X^-m (Theorem O unit irrelevant for jets/signatures).
Signature = C1's key: (top (l1a,l2a,l1b,l2b), bot (...), sigma = s1_top(q)+s1_bot(q), delta = deg_top q - ord_bot q),
eligible iff |lc b/lc a| = 1 at both ends and span a >= 1."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
from jauto import S, padd, pneg, pshift, pmul, pinv, logs
from fractions import Fraction as Fr
KP=8
def refl(f): return {-e:c for e,c in f.items()}
def trunc(f,K=KP):
    d=max(f); return S({e:c for e,c in f.items() if e>=d-K},d-K)
CONST={}
for end in ('top','bot'):
    r=(lambda f:f) if end=='top' else refl
    CONST[end]=dict(T=S(r({1:1}),None),T2P1=S(r({0:1,2:1}),None),PHI3I=pinv(S(r({0:1,1:1,2:1}),None)))
def tm(mu,end):
    return S({(mu if end=='top' else -mu):(-1)**(mu%2)},None)
def from_vec(v,K=KP):
    a,b=v
    return {'top':(trunc(a,K),trunc(b,K)),'bot':(trunc(refl(a),K),trunc(refl(b),K))}
def star(x,y): return {e:(pmul(x[e][0],y[e][0]),pmul(x[e][1],y[e][1])) for e in ('top','bot')}
def ypow(N,x):
    return {'top':(x['top'][0],pshift(x['top'][1],-3*N)),'bot':(x['bot'][0],pshift(x['bot'][1],3*N))}
def xpow(mu,x):
    out={}
    for e in ('top','bot'):
        A,B=x[e]; C=CONST[e]
        al=pmul(padd(pmul(C['T'],A),pmul(C['T2P1'],B)),C['PHI3I'])
        be=pmul(padd(A,pneg(B)),C['PHI3I'])
        TM=tm(mu,e)
        a2=padd(al,pmul(pmul(TM,C['T2P1']),be)); b2=padd(al,pneg(pmul(pmul(TM,C['T']),be)))
        out[e]=(a2,b2)
    return out
def nest(m,x): return xpow(-m,x)
def relprec(s):
    d=s.lead()
    if d is None: return -1
    return 10**9 if s.P is None else d-s.P
def endjet(s,K):
    d=s.lead(); c0=s.c[d]
    return d,c0,tuple(s.c.get(d-i,Fr(0))/c0 for i in range(1,K+1))
def signature(x,K=2):
    """returns (key, eligible, info) or (None, False, 'lowprec')"""
    D={}
    for e in ('top','bot'):
        A,B=x[e]
        if relprec(A)<K or relprec(B)<K: return None,False,'lowprec'
        D[e]=(endjet(A,K),endjet(B,K))
    bd={}; s1={}; dq={}; elig=True
    for e in ('top','bot'):
        (da,ca,sa),(db,cb,sb)=D[e]
        la=logs(sa); lb=logs(sb)
        bd[e]=(la[0],la[1],lb[0],lb[1]); s1[e]=lb[0]-la[0]; dq[e]=db-da
        if abs(Fr(cb)/Fr(ca))!=1: elig=False
    spana=D['top'][0][0]+D['bot'][0][0]
    if spana<1: elig=False
    key=(bd['top'],bd['bot'],s1['top']+s1['bot'],dq['top']+dq['bot'])
    return key,elig,dict(lc=(D['top'][1][1]/D['top'][0][1],D['bot'][1][1]/D['bot'][0][1]),spana=spana)
