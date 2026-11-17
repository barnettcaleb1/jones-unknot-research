#!/usr/bin/env python3
"""Hybrid positive calculus for normal forms (n_0; n_1..n_{k-1}):  F = (1 0) E Y^{n_{k-1}} E ... E Y^{n_0} (1 0)^T.
   Positive lifts:  EE = [[x^4/y, x^4(1+y)/y],[1,1]]  (lift of -E),  M_Y^n,  Mt_y^m,  and runs of interior n_i = -1 are taken as
   letters x (Mt_x), since  E Y^-1 E = t^4 * (E rho(x))... (scalars/units ignored).
   Test: the top t-degree part (t-degree = a + 4b) of the resulting positive polynomial is a single monomial."""
import sys,itertools,collections
def mono_mul(p,m,c=1):
    return collections.Counter({(a+m[0],b+m[1]):v*c for (a,b),v in p.items()})
def add(*ps):
    r=collections.Counter()
    for p in ps:
        for k,v in p.items(): r[k]+=v
    return r
U=(1,-1); X=(1,0); Yv=(0,1)
def MY(v,n):   # [[1,0],[u[n]_u, u^n]]
    v1,v2=v
    s=add(*[mono_mul(v1,(j,-j)) for j in range(1,n+1)])
    return v1, add(s,mono_mul(v2,(n,-n)))
def MYinv(v,m):  # [[1,0],[(y/x^4)[m]_{1/u}, u^-m]]
    v1,v2=v
    s=add(*[mono_mul(v1,(-4-j,1+j)) for j in range(0,m)])
    return v1, add(s,mono_mul(v2,(-m,m)))
def EE(v):     # [[x^4/y, x^4/y + x^4],[1,1]]
    v1,v2=v
    return add(mono_mul(v1,(4,-1)),mono_mul(v2,(4,-1)),mono_mul(v2,(4,0))), add(v1,v2)
def MXinv(v):  # [[1, x^3(1+y)/y],[0,1/x]]
    v1,v2=v
    return add(v1,mono_mul(v2,(3,-1)),mono_mul(v2,(3,0))), mono_mul(v2,(-1,0))
def hybrid(ns):
    """ns = (n_0,...,n_{k-1}); process Y^{n_0}, then for i>=1: E Y^{n_i} (with n_i=-1 -> letter x applied after the previous E... ), final E."""
    v=(collections.Counter({(0,0):1}),collections.Counter())
    n0=ns[0]
    v=MY(v,n0) if n0>0 else (MYinv(v,-n0) if n0<0 else v)
    v=EE(v)
    for n in ns[1:]:
        if n==-1: v=MXinv(v)          # E Y^-1 E  ~  E x   (the E has already been applied)
        else:
            v=MY(v,n) if n>0 else MYinv(v,-n)
            v=EE(v)
    return v[0]
def tdeg(k): return k[0]+4*k[1]
if __name__=='__main__':
    maxe=int(sys.argv[1]) if len(sys.argv)>1 else 3
    maxk=int(sys.argv[2]) if len(sys.argv)>2 else 4
    inner=[e for e in range(-maxe,maxe+1) if e!=0]
    bad=0; tot=0
    for k in range(1,maxk+1):
        for n0 in [e for e in range(-maxe,maxe+1) if e not in (0,-1)]:
            for rest in itertools.product(inner,repeat=k-1):
                ns=(n0,)+rest
                P=hybrid(ns); tot+=1
                top=max(tdeg(m) for m in P)
                tops=[(m,c) for m,c in P.items() if tdeg(m)==top]
                if len(tops)!=1 or tops[0][1]!=1:
                    bad+=1
                    if bad<8: print('TOP NOT UNIQUE',ns,tops)
    print('normal forms:',tot,' with non-unique top t-degree monomial:',bad)
