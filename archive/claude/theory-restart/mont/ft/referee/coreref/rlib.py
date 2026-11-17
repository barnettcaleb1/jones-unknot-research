"""Referee's own helpers (independent of core/clib.py). Exact integer/Fraction arithmetic only.
Laurent polys: dict {exp: int}. J from lp.J (the definition); V_K from kauffman.bracket with my own normalisation."""
import sys, random, math
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, kauffman, alex, flat_search as fs
from fractions import Fraction as Fr

def cl(p): return {e:c for e,c in p.items() if c}
def padd(*ps):
    r={}
    for p in ps:
        for e,c in p.items(): r[e]=r.get(e,0)+c
    return cl(r)
def psub(p,q): return padd(p,{e:-c for e,c in q.items()})
def pmul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,0)+c*d
    return cl(r)
def ppow(p,n):
    r={0:1}
    for _ in range(n): r=pmul(r,p)
    return r
def subst_neg(p): return {e:c*(-1)**(e%2) for e,c in p.items()}      # p(-t)
def subst_pow(p,k): return {k*e:c for e,c in p.items()}             # p(t^k)
def mom(p,k): return sum(c*(-1)**(e%2)*e**k for e,c in p.items())   # sum p_e (-1)^e e^k = k![h^k] p(-e^h)
def mom1(p,k): return sum(c*e**k for e,c in p.items())             # k![h^k] p(e^h)
def deriv_at(p,k,x):
    tot=Fr(0)
    for e,c in p.items():
        f=1
        for i in range(k): f*=(e-i)
        tot+=c*f*Fr(x)**(e-k)
    return tot
def span(p): return max(p)-min(p) if p else None

def divmod_laurent(p,q):
    """exact division of Laurent p by Laurent q (q has unit leading AND trailing coeff). Returns quotient or None if not divisible."""
    p=cl(p)
    if not p: return {}
    qt=max(q); qb=min(q); assert abs(q[qt])==1 and abs(q[qb])==1
    r=dict(p); out={}
    # long division from the top
    while r:
        e=max(r)
        if e-qt < min(p)-qb: break
        c=r[e]*q[qt]; s=e-qt
        out[s]=out.get(s,0)+c
        for f,d in q.items():
            r[f+s]=r.get(f+s,0)-c*d
            if r[f+s]==0: del r[f+s]
    return cl(out) if not r else None

def VK(word):
    """V_K in the standard variable t = A^-4 (as clib), normalised V(1)=1, V'(1)=0. Own implementation."""
    kb=kauffman.bracket(word)
    if kb is None: return None
    kb=cl(kb)
    if not kb: return None
    exps=sorted(kb); r=exps[0]%4
    if any((e-r)%4 for e in exps): return None
    V={(r-e)//4:c for e,c in kb.items()}     # t = A^-4  ->  A^e = t^{-e/4} up to the common offset
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}
    d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}

def a2V(V): return -deriv_at(V,2,1)/6
def v3V(V): return -(deriv_at(V,3,1)+3*deriv_at(V,2,1))/36

ONE={0:1}
T1={0:1,1:1}; TM={0:-1,1:1}; C4={0:1,2:1}; C6={0:1,1:-1,2:1}; C3={0:1,1:1,2:1}; C5={0:1,1:1,2:1,3:1,4:1}
D7=pmul(pmul(ppow(T1,2),TM),pmul(C4,C6))
D8=pmul(T1,D7)
MODD=pmul(pmul({0:-1,2:1},{0:-1,3:1}),{0:-1,5:1})   # (t^2-1)(t^3-1)(t^5-1)

def rand_word(rnd,Lmin,Lmax):
    while True:
        w=fs.gen(rnd,rnd.randint(Lmin,Lmax))
        if not w: continue
        J=lp.J(w)
        if J is None: continue
        return w,J
