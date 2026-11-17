"""Referee's own exact Laurent-polynomial arithmetic (dict exponent -> int) and the matrices of Theorem A."""
from collections import defaultdict
def clean(p): return {e:c for e,c in p.items() if c}
def add(p,q):
    r=defaultdict(int)
    for e,c in p.items(): r[e]+=c
    for e,c in q.items(): r[e]+=c
    return clean(r)
def mul(p,q):
    r=defaultdict(int)
    for e1,c1 in p.items():
        for e2,c2 in q.items(): r[e1+e2]+=c1*c2
    return clean(r)
def neg(p): return {e:-c for e,c in p.items()}
ONE={0:1}; ZERO={}
def mon(e,c=1): return {e:c}
def mmul(M,N):
    return tuple(tuple(add(mul(M[i][0],N[0][j]),mul(M[i][1],N[1][j])) for j in range(2)) for i in range(2))
def mapply(M,v):
    return (add(mul(M[0][0],v[0]),mul(M[0][1],v[1])),add(mul(M[1][0],v[0]),mul(M[1][1],v[1])))
RHO={'Y':((ONE,ZERO),(mon(-3),mon(-3))),
     'X':((ONE,{0:1,4:-1}),(ZERO,mon(1,-1))),
     'y':((ONE,ZERO),(mon(0,-1),mon(3))),
     'x':((ONE,{-1:1,3:-1}),(ZERO,mon(-1,-1)))}
ID=((ONE,ZERO),(ZERO,ONE))
# sanity: inverses
assert mmul(RHO['Y'],RHO['y'])==ID and mmul(RHO['X'],RHO['x'])==ID
E=mmul(RHO['y'],RHO['X'])
assert E==((ONE,{0:1,4:-1}),(mon(0,-1),mon(0,-1))), E
assert mmul(E,E)==((mon(4),ZERO),(ZERO,mon(4)))
def Jword(word):
    """word = string in YXyx, L_1 first (nearest the cap). returns (1 0) rho(L_m)..rho(L_1) (1 0)^T"""
    v=(ONE,ZERO)
    for L in word: v=mapply(RHO[L],v)
    return v[0]
def F(ns):
    """F(n_0..n_{k-1}) = (1 0) E Y^{n_{k-1}} E ... E Y^{n_0} (1 0)^T"""
    v=(ONE,ZERO)
    for n in ns:
        for _ in range(abs(n)): v=mapply(RHO['Y' if n>0 else 'y'],v)
        v=mapply(E,v)
    return v[0]
def deg(p): return max(p)
def lc(p): return p[max(p)]
def span(p): return max(p)-min(p)
def is_unit(p): return len(p)==1 and abs(list(p.values())[0])==1
def subs_inv(p): return {-e:c for e,c in p.items()}
