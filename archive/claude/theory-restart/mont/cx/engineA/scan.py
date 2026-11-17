"""Shared scan utilities: cancellation depths, gates, unit verification."""
import sys, cmath
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import vc, eng, lp
from vc import top, bot, shift, mul, add
def depths(S1,S2,F):
    """(r_top, r_bot, generic span, actual span of F)"""
    T=max(top(S1),top(S2)); Bt=min(bot(S1),bot(S2))
    return T-top(F), bot(F)-Bt, T-Bt, top(F)-bot(F)
def gates(Jraw):
    J=vc.norm(Jraw)
    if J is None: return None
    a2=lp.a2(J)
    z=cmath.exp(2j*cmath.pi/10)
    v10=sum(c*z**e for e,c in J.items())
    cyc=abs(v10-1)<1e-9
    # (t+1)-adic order of J-1
    D=dict(J); D[0]=D.get(0,0)-1; D={e:c for e,c in D.items() if c}
    o=0
    if D:
        p=D
        while True:
            # divide by (t+1) if p(-1)==0
            if sum(c*(-1)**(e%2) for e,c in p.items())!=0: break
            q=vc.divexact(p,{0:1,1:1})
            if q is None: break
            p=q; o+=1
            if not p: break
    else: o=99
    return dict(a2=a2,cyc10=cyc,ord1=o,span=(max(J)-min(J)))
def verify(word):
    """exact recomputation + nontriviality data"""
    import alex
    J=lp.J(word)
    det=alex.alex_eval(word,-1); d2=alex.alex_eval(word,2); d3=alex.alex_eval(word,3)
    return J,det,d2,d3
