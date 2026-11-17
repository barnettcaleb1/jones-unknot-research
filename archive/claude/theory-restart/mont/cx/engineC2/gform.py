"""Bilinear form of a symmetric 2-slot special region:  R(B) := delta<Theta>/(delta*Delta_2) in t  =  (a,b) G (a~,b~)^T
exactly, for normalised channel vectors (a,b) of the box B (units of B and of its mirror cancel: u * u(1/A) = 1)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import theta, sym, lp, vc
from lp import add, sub, mul, mono, ONE, shift
def raw_t(events):
    """delta<Theta>/(delta Delta_2) as a Laurent poly in t=A^4 (exact; no normalisation); None if not exact"""
    if theta.THETA0_TIMES_DELTA is None: theta.THETA0_TIMES_DELTA=theta.theta_raw(theta.planar_theta())
    r=theta.theta_raw(events)
    q=theta.pdiv(r,theta.THETA0_TIMES_DELTA)
    if q is None: return None
    es=sorted(q); r0=es[0]%4
    if any((e-r0)%4 for e in es): return None
    return {(e-r0)//4:c for e,c in q.items()}, r0
def tilde(p): return {-e:c for e,c in p.items()}
def bil(v,G):
    a,b=v; at,bt=tilde(a),tilde(b)
    return add(mul(mul(a,at),G[0][0]),mul(mul(a,bt),G[0][1]),mul(mul(b,at),G[1][0]),mul(mul(b,bt),G[1][1]))
