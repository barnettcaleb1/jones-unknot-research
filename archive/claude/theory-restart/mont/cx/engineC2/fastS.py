"""Fast exact J for symmetric 2-slot closures: R = (a,b) G (a~,b~)^T = Phat/Phi3^2,  Phat = sum Ghat_cc' chan_c chan~_c'."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp, vc
from lp import add, mul, top, bot, span
PHI3SQ={0:1,1:2,2:3,3:2,4:1}
def tilde(p): return {-e:c for e,c in p.items()}
def Phat(G,v):
    a,b=v; at,bt=tilde(a),tilde(b)
    return add(mul(G[0][0],mul(a,at)),mul(G[0][1],mul(a,bt)),mul(G[1][0],mul(b,at)),mul(G[1][1],mul(b,bt)))
def tops(G,v):
    a,b=v
    return (top(G[0][0])+span(a), top(G[0][1])+top(a)-bot(b), top(G[1][0])+top(b)-bot(a), top(G[1][1])+span(b))
def R_of(G,v):
    P=Phat(G,v)
    q=vc.divexact(P,PHI3SQ)
    assert q is not None
    return q
def J_of(G,v):
    R=R_of(G,v)
    return lp.normalize(R)
def gates(J):
    import cmath
    z=cmath.exp(2j*cmath.pi/10)
    val=sum(c*z**e for e,c in J.items())
    return lp.a2(J), abs(val-1)<1e-9
