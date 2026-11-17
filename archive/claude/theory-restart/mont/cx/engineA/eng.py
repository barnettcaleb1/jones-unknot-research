"""ENGINE A search engine: exact candidate sets for closures of a product p=(A,B) (channel coords, normalised vectors).
LEMMA (two-summand end coincidence; PROVED): if F = S1 + S2 with span S1, span S2 >= 3 and F = u Phi_3 (u unit), then
  top S1 = top S2 or bot S1 = bot S2.  (If both differ, span F >= max span S_i >= 3.)
  Horizontal closure  J Phi_3 = w_1(mu) A + w_3(mu) t^-3N B  (integral part N, twist mu != 0):
     for fixed mu, N in {N_top, N_bot} (end coincidence), these depend only on the class of mu (>=2, 1, -1, <=-2);
     for fixed N, J_mu = P_N + (-t)^mu Q_N, Q_N = (1+t^2)(A-B_N)/Phi_3 != 0 has span >= 2, so mu in {top P-top Q, bot P-bot Q}
     unless P_N is a monomial (then brute force |mu| <= MUBF).  COMPLETE for units.
  Vertical closure    J Phi_3 = w_1(a) A + wV(a) t^-3N B,  wV(a) = (-t)^a t + t^(3a-1) Phi_5  (a odd):
     for fixed a, N in {N_top(a), N_bot(a)};  a-window |a| <= max(span A, span B) + 8 (block separation; see REPORT).
"""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc
from vc import add, sub, mul, shift, top, bot, PHI3, PHI5, T2P1, divexact, tmono, norm
MUBF=40
def w1(mu): return add({1:1}, mul(tmono(mu),T2P1))
def w3(mu): return mul(T2P1, sub({0:1}, tmono(mu)))
def wV(a): return add(shift(tmono(a),1), shift(PHI5,3*a-1))
_W={}
def W(mu):
    if mu not in _W: _W[mu]=(w1(mu),w3(mu))
    return _W[mu]
_WV={}
def WV(a):
    if a not in _WV: _WV[a]=(w1(a),wV(a))
    return _WV[a]
REP={'ge2':5,'1':1,'-1':-1,'le-2':-5}
def cls(mu): return 'ge2' if mu>=2 else ('le-2' if mu<=-2 else str(mu))
def ncands_h(A,B):
    """{class: set of N} for horizontal closures (from end coincidence at fixed mu-class)"""
    out={}
    for c,mu in REP.items():
        a1,a3=W(mu)
        s=set()
        nt=top(a3)+top(B)-top(a1)-top(A); nb=bot(a3)+bot(B)-bot(a1)-bot(A)
        for x in (nt,nb):
            if x%3==0: s.add(x//3)
        out[c]=s
    return out
def PQ(A,BN):
    P=divexact(add(shift(A,1),mul(T2P1,BN)),PHI3)
    Q=divexact(mul(T2P1,sub(A,BN)),PHI3)
    return P,Q
def hclosures(p, want_all=False):
    """all candidate (mu,N) for the horizontal twisted closure of product p; returns list of (mu,N,Jraw)"""
    A,B=p
    res=[]
    if len(A)<=2 or span(A)<3:
        Ns=set(range(-12,13))
        cand={c:Ns for c in REP}
    else:
        cand=ncands_h(A,B)
    allN=set()
    for c,s in cand.items(): allN|=s
    for N in allN:
        BN=shift(B,-3*N)
        P,Q=PQ(A,BN)
        if not Q:   # one channel (A = B_N, scalar box state): J = P for every mu
            res.append(('all',N,P)); continue
        mus=set()
        if len(P)<=1:
            mus=set(range(-MUBF,MUBF+1))
        else:
            mus={top(P)-top(Q), bot(P)-bot(Q)}
        for mu in mus:
            if mu==0: continue
            if N not in cand[cls(mu)]: continue
            J=add(P,mul(tmono(mu),Q))
            res.append((mu,N,J))
    return res
def span(p): return max(p)-min(p) if p else -1
def vclosures(p):
    """candidate (a,N) for vertical closures of product p; returns list of (a,N,Jraw)"""
    A,B=p
    res=[]
    amax=max(span(A),span(B))+8
    for a in range(-amax,amax+1,2) if amax%2 else range(-amax-1,amax+2,2):
        a1,aV=WV(a)
        tS1=top(a1)+top(A); bS1=bot(a1)+bot(A)
        nt=top(aV)+top(B)-tS1; nb=bot(aV)+bot(B)-bS1
        small=(tS1-bS1)<3
        Ns=set(x//3 for x in (nt,nb) if x%3==0)
        if small: Ns=set(range(-12,13))
        S1=None
        for N in Ns:
            if not small:
                # unit => cancellation of the leading coefficient at a coincident end (or coincidence at both ends)
                ct = (3*N==nt) and (a1[top(a1)]*A[top(A)] + aV[top(aV)]*B[top(B)]==0)
                cb = (3*N==nb) and (a1[bot(a1)]*A[bot(A)] + aV[bot(aV)]*B[bot(B)]==0)
                both = (nt==nb)
                if not (ct or cb or both): continue
            if S1 is None: S1=mul(a1,A)
            F=add(S1,shift(mul(aV,B),-3*N))
            Jr=divexact(F,PHI3)
            res.append((a,N,Jr))
    return res
def is_unit(J): return J is not None and len(J)==1
