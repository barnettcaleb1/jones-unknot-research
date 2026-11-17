"""t-polynomial helpers on top of lp.py; preferred body vectors computed independently (raw TL3 sandwich)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/nest')
import lp
from lp import add, mul, sub, mono, ONE, P, shift, normalize, ev
from nlib import divexact
import r2lib
PHI3=P((1,0),(1,1),(1,2)); PHI5=P((1,0),(1,1),(1,2),(1,3),(1,4))
OMT3=P((1,0),(-1,3))          # 1 - t^3
def unit_to(p,q):
    """(s,k) with q = s t^k p, else None"""
    if not p or not q: return None
    k=max(q)-max(p); s=q[max(q)]//p[max(p)]
    if s not in (1,-1): return None
    return (s,k) if {e+k:s*c for e,c in p.items()}==q else None
def body_raw_t(B):
    """raw (a,b) of body B as t-polys sharing one A-class; returns (r,a,b)"""
    da,db=r2lib.body_ab(B)
    a=r2lib.pdivexact(da,r2lib.DELTA); b=r2lib.pdivexact(db,r2lib.DELTA)
    assert a is not None and b is not None, 'delta does not divide'
    ra,at=r2lib.to_t(a); rb,bt=r2lib.to_t(b)
    assert ra==rb, 'a,b in different A-classes'
    return ra,at,bt
def body_pref(B):
    """preferred channel amplitudes (A,B) of body B, from the raw TL3 sandwich"""
    r,a,b=body_raw_t(B)
    na=normalize(a)
    if na is None: return None
    s,k=unit_to(a,na)
    return na, {e+k:s*c for e,c in b.items()}
def ab_from_v(v):
    return v[0], add(v[0], mul(OMT3, v[1]))
def v_from_ab(a,b):
    q=divexact(sub(b,a),OMT3)
    return None if q is None else [a,q]
def vert_formula(A,B,a):
    lam2={a:((-1)**(a%2))}
    lam2=mono(a,(-1)**(a%2))
    num=add(mul(mono(1),A), mul(lam2, add(mul(P((1,0),(1,2)),A), mul(mono(1),B))), mul(mono(3*a-1), mul(PHI5,B)))
    q=divexact(num,PHI3)
    return q
def vword(B,a):
    tw=('x2.' if a>0 else 'y2.')*abs(a)
    return 's.l1.'+(B+'.' if B else '')+tw+'u1'
def tw1(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def neck_body(m,Bs): return 'r2.'+tw1(m)+'.'.join(Bs)+'.u1'
def star_ab(p,q): return mul(p[0],q[0]), mul(p[1],q[1])
def Xpow_first_row_apply(mu, v):
    """e1^T X^mu v  with v in TH-2BR coords"""
    M=lp.Xm if mu>=0 else lp.Xi
    w=[v[0],v[1]]
    for _ in range(abs(mu)): w=lp.mvec(M,w)
    return w
