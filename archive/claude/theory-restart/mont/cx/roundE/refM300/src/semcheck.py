"""refM300: GENERAL semantic Farkas checker (own).  A case system is given by semantic rows
    sum_boxes z_r . vec(box)  +  sum_j cls_r(j) k_j  +  n_r n   (= or <=)  b_r
over: rational boxes (vec = (rho_a, rho_q, l2a, lambda_q, l3a, l3q) at the weak end; the SET of these vectors is read off
the OWN K=3 automaton; bottom = top by R2), class multiplicities k_j >= 0 (OWN class data), n >= nmin.
Multipliers y (eq free, ub >= 0).  For every feasible configuration Phi = sum_r y_r (lhs_r - b_r) <= 0, while
Phi >= sum_boxes G + sum_j col_j k_j + cn n - sum y_r b_r >= (g0 + cn) nmin - sum y b  if col_j >= 0 and g0 + cn >= 0,
G = sum_r y_r z_r . vec, g0 = exact min of G over all rational boxes.  Valid certificate <=> (g0+cn) nmin - y.b > 0."""
import sys
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rauto
_A=None
def auto():
    global _A
    if _A is None:
        order,trans=rauto.build(3); E=rauto.edges(order,trans); FIN={k:rauto.qdata(k,3) for k in order if k!='init'}
        _A=(order,E,FIN)
    return _A
_gc={}
def gmin(z):
    """z = (c_ra, c_rq, c_la, c_lq, c_l3a, c_l3q): exact min over rational boxes (None if unbounded below)"""
    z=tuple(Fr(x) for x in z)
    if z in _gc: return _gc[z]
    order,E,FIN=auto()
    v=rauto.extremum(order,E,FIN,lambda l:z[0]*l[0]+z[2]*l[1]+z[4]*l[2],lambda f:z[1]*f[2][0]+z[3]*f[2][1]+z[5]*f[2][2],'min')
    _gc[z]=v; return v
def check(rows,y,nclass,nmin):
    """rows: list of dict(kind='eq'|'ub', z=6-tuple, cls=list of nclass coefficients (or dict j->c), n=coef, b=rhs)."""
    assert len(rows)==len(y)
    for r,yy in zip(rows,y):
        if r['kind']=='ub' and yy<0: return False,{'err':'negative ub multiplier'}
    Z=[Fr(0)]*6; col=[Fr(0)]*nclass; cn=Fr(0); yb=Fr(0)
    for r,yy in zip(rows,y):
        if not yy: continue
        for i in range(6): Z[i]+=yy*r['z'][i]
        c=r['cls']
        if isinstance(c,dict):
            for j,v in c.items(): col[j]+=yy*v
        else:
            for j,v in enumerate(c): col[j]+=yy*v
        cn+=yy*r['n']; yb+=yy*r['b']
    g0=gmin(Z) if any(Z) else Fr(0)
    if g0 is None: return False,{'err':'G unbounded'}
    mc=min(col) if col else Fr(0)
    ok=(mc>=0) and (g0+cn>=0) and ((g0+cn)*nmin-yb>0)
    return ok,dict(g0=g0,mincol=mc,cn=cn,yb=yb)
