"""Shared helpers for lane CORE (exact arithmetic only)."""
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, kauffman
from fractions import Fraction as F

def M(Jn,k):
    """k-th moment: sum_e J_e (-1)^e e^k  (= k! [h^k] J(-e^h))"""
    return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())

def der(V,k,x=1):
    """k-th derivative of Laurent poly V at x (exact Fraction)"""
    tot=F(0)
    for e,c in V.items():
        f=1
        for i in range(k): f*=(e-i)
        tot+=c*f*F(x)**(e-k)
    return tot

def VK(word):
    """Jones polynomial of the full symmetric knot K of a half-word, normalised V(1)=1, V'(1)=0 (t = A^-4)."""
    kb=kauffman.bracket(word)
    if not kb: return None
    kb={e:c for e,c in kb.items() if c}
    es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={-(e-r)//4:c for e,c in kb.items()}
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}
    d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}

def a2_of_V(V): return F(-der(V,2),6)
def v3_of_V(V): return F(-(der(V,3)+3*der(V,2)),36)

def pdiv(p,q):
    """exact division of Laurent poly p by Laurent poly q with +-1 leading coeff.
    returns (quotient, remainder) with p = q*quot + rem, rem supported in degrees < min(p)+deg-span(q) window."""
    p={e:c for e,c in p.items() if c}
    if not p: return {},{}
    qb=min(q); qt=max(q); qc=q[qt]
    assert abs(qc)==1
    pb=min(p)
    r=dict(p); out={}
    while r and max(r)-qt >= pb-qb:
        e=max(r); c=r[e]; k=c*qc; s=e-qt
        out[s]=out.get(s,0)+k
        for f,d in q.items():
            r[f+s]=r.get(f+s,0)-k*d
            if r[f+s]==0: del r[f+s]
    return {e:c for e,c in out.items() if c}, r

def polypow(p,n):
    r=lp.ONE
    for _ in range(n): r=lp.mul(r,p)
    return r

T1=lp.P((1,0),(1,1))      # 1+t
Tm=lp.P((-1,0),(1,1))     # t-1
C4=lp.P((1,0),(1,2))      # 1+t^2
C6=lp.P((1,0),(-1,1),(1,2))  # 1-t+t^2
C3=lp.P((1,0),(1,1),(1,2))   # 1+t+t^2
def D(a,b=1):
    """(t+1)^a (t-1)^b (t^2+1)(t^2-t+1)"""
    r=polypow(T1,a); r=lp.mul(r,polypow(Tm,b)); r=lp.mul(r,C4); r=lp.mul(r,C6); return r

def randJ(rnd, Lmin=6, Lmax=16):
    while True:
        w=fs.gen(rnd,rnd.randint(Lmin,Lmax))
        if not w: continue
        Jn=lp.J(w)
        if Jn is None: continue
        return w,Jn

def pdiv_poly(p,q):
    """polynomial division (nonnegative exponents) by monic-up-to-sign q; returns (quot, rem) with deg rem < deg q"""
    p={e:c for e,c in p.items() if c}
    qt=max(q); qc=q[qt]; assert abs(qc)==1 and min(q)>=0
    r=dict(p); out={}
    while r and max(r)>=qt:
        e=max(r); c=r[e]; k=c*qc; s=e-qt
        out[s]=out.get(s,0)+k
        for f,d in q.items():
            r[f+s]=r.get(f+s,0)-k*d
            if r[f+s]==0: del r[f+s]
    return out,r

def G_of(J):
    q,r=pdiv(lp.sub(J,lp.ONE),lp.P((1,0),(2,1),(1,2)))
    assert not r
    return q
def j_of(J):
    d=der(J,1,1); assert d%8==0
    return int(-d//8)
def V_branch(J,n):
    """V(T(1/n)) from BRIEF 1.3: t^{12 j [n odd]} { 1 + (1 - (-t)^{-n}) Phi_3 G }"""
    G=G_of(J)
    f=lp.sub(lp.ONE,{-n:(-1)**(n%2)})          # 1 - (-t)^{-n}
    V=lp.add(lp.ONE,lp.mul(lp.mul(f,C3),G))
    if n%2: V=lp.shift(V,12*j_of(J))
    return V
def hexp(V,kmax=4):
    import math
    return [F(sum(c*(-1)**(e%2)*e**k for e,c in V.items()),math.factorial(k)) for k in range(kmax+1)]
