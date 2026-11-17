"""exact-enough rank tests: rank of an integer/rational matrix modulo large primes"""
from fractions import Fraction as F
PR=[2**61-1, 1000000007, 998244353]
def rank_mod(M, p):
    A=[]
    for row in M:
        r=[]
        for v in row:
            v=F(v); r.append((v.numerator % p) * pow(v.denominator % p, p-2, p) % p)
        A.append(r)
    n=len(A); m=len(A[0]) if A else 0; rk=0; col=0
    for col in range(m):
        piv=next((i for i in range(rk,n) if A[i][col]),None)
        if piv is None: continue
        A[rk],A[piv]=A[piv],A[rk]
        inv=pow(A[rk][col],p-2,p)
        A[rk]=[x*inv%p for x in A[rk]]
        for i in range(n):
            if i!=rk and A[i][col]:
                f=A[i][col]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[rk])]
        rk+=1
    return rk
def in_span(A, b):
    """returns (rank A, rank [A|b]) for each prime"""
    out=[]
    for p in PR:
        Ab=[row+[bi] for row,bi in zip(A,b)]
        out.append((rank_mod(A,p),rank_mod(Ab,p)))
    return out

def certificate(A, b):
    """exact rational elimination: returns y (dict row->coef) with sum_i y_i A[i] = 0 and sum_i y_i b_i != 0, or None"""
    rows=[]   # each: (vector list of Fractions incl b, provenance dict)
    piv={}    # col -> index in basis
    basis=[]
    m=len(A[0])
    for i,(ra,bi) in enumerate(zip(A,b)):
        v=[F(x) for x in ra]+[F(bi)]; prov={i:F(1)}
        for col in range(m):
            if v[col]!=0 and col in piv:
                bv,bp=basis[piv[col]]
                f=v[col]/bv[col]
                v=[x-f*y for x,y in zip(v,bv)]
                for k,c in bp.items(): prov[k]=prov.get(k,F(0))-f*c
        nz=next((col for col in range(m) if v[col]!=0),None)
        if nz is None:
            if v[m]!=0:
                return {k:c for k,c in prov.items() if c!=0}, v[m]
            continue
        piv[nz]=len(basis); basis.append((v,prov))
    return None
