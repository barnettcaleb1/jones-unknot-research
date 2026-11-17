"""Referee's own quotient constituent knots K_in = k u A_in, K_out = k u A_out (Morse words; my bracket + Alexander).
Model (re-derived in ident.md sec. 3 from the quotient map w -> w^2): axis segment at position 0, arc half-strand j at
position j+1; an on-axis letter c0 becomes the full twist (c,0),(c,0) of the arc around A_in; K_out deletes them.
hand=-1 reverses the winding handedness (c0 -> (c',0),(c',0) with c' the other letter) for a discrimination test."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex, refinv as R
from t_local import bracket_tokens, divpoly, DELTA
def tokens(word, which, hand=1):
    out=[('r',0)]
    for c,s in alex.parse(word):
        if s==0 and c in 'xy':
            if which=='in':
                cc=c if hand==1 else {'x':'y','y':'x'}[c]
                out+=[(cc,0),(cc,0)]
        else: out.append((c,s))
    out.append(('u',0)); return out
def alex_of_tokens(full):
    cr=alex.diagram(full)
    if cr is None: return None
    n=len(cr)
    if n==0: return {0:1}
    res=[]
    for p in R.PRIMES:
        xs=list(range(1,n+1)); ys=[]
        for x in xs:
            M,_=alex.alex_matrix(cr,x); ys.append(R.det_mod([r[:-1] for r in M[:-1]],p))
        res.append(R.interp_mod(xs,ys,p))
    Pt=1
    for p in R.PRIMES: Pt*=p
    co=[]
    for i in range(n):
        x=0
        for p,cc in zip(R.PRIMES,res):
            q=Pt//p; x=(x+cc[i]*q*pow(q,p-2,p))%Pt
        co.append(x-Pt if x>Pt//2 else x)
    P={i:cc for i,cc in enumerate(co) if cc}
    if not P: return None
    lo,hi=min(P),max(P)
    if (lo+hi)%2: return None
    mid=(lo+hi)//2; P={e-mid:cc for e,cc in P.items()}; s=sum(P.values())
    if s not in (1,-1): return None
    return {e:s*cc for e,cc in P.items()}
def inv_tokens(toks, with_alex=True):
    B=bracket_tokens(toks); kb=divpoly(B,DELTA)
    if kb is None: return None
    V=R.V_from_bracket(kb)
    if V is None: return None
    a2,v3,j4=R.vinv(V); out=dict(V=V,a2=a2,v3=v3,j4=j4)
    if with_alex:
        D=alex_of_tokens(toks[1:])
        if D is None: return None
        a2c,a4=R.conway_a2a4(D)
        if a2c!=a2: return None
        out.update(Delta=D,a4=a4,det=abs(sum(c*(-1)**e for e,c in D.items())))
    return out
def constituents(word, with_alex=True, hand=1):
    return {w:inv_tokens(tokens(word,w,hand),with_alex) for w in ('in','out')}
