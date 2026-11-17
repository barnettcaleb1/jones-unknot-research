# Sanity check of ONE identity (build-finite, Lemma C1):
#   for separating curves c, c' the t=-1 root projections satisfy
#   tr(P_c P_c') = (2n-1)^2  (an odd square), in particular never 0.
# P_c is read off Jones's matrices as in read-kasahara/check/zphi1.py:
#   Delta_1(psi_0) = d/dh rho(psi_0) at t=-e^h, h=0, and P_c = (6I - Delta_1)/30.
# Conjugates P_{gc} = rho_{-1}(g) P_c rho_{-1}(g)^{-1}, g random words in z1, xi.
from fractions import Fraction as F
import random, math
class D:
    def __init__(s,a,b=0): s.a=F(a); s.b=F(b)
    def __add__(s,o): o=o if isinstance(o,D) else D(o); return D(s.a+o.a,s.b+o.b)
    __radd__=__add__
    def __neg__(s): return D(-s.a,-s.b)
    def __mul__(s,o): o=o if isinstance(o,D) else D(o); return D(s.a*o.a,s.a*o.b+s.b*o.a)
    __rmul__=__mul__
    def inv(s): return D(1/s.a,-s.b/(s.a*s.a))
    def __pow__(s,n):
        r=D(1)
        if n<0: s=s.inv(); n=-n
        for _ in range(n): r=r*s
        return r
t=D(-1,-1)   # t = -e^h to first order
def mat(rows): return [[x if isinstance(x,D) else D(x) for x in r] for r in rows]
def dmul(A,B): return [[sum((A[i][k]*B[k][j] for k in range(5)),D(0)) for j in range(5)] for i in range(5)]
z1=mat([[-t**-2,0,0,0,t**3],[0,-t**-2,t**-2,0,0],[0,0,t**3,0,0],[0,0,t**-2,-t**-2,0],[0,0,0,0,t**3]])
xi=mat([[0,0,1,0,0],[0,0,0,0,1],[1,0,0,0,0],[0,1,0,0,0],[0,0,0,1,0]])
xiT=[[xi[j][i] for j in range(5)] for i in range(5)]
z2=dmul(dmul(xi,z1),xiT); w=dmul(dmul(z1,z2),z1); psi=dmul(dmul(w,w),dmul(w,w))
I=[[F(int(i==j)) for j in range(5)] for i in range(5)]
Delta=[[psi[i][j].b for j in range(5)] for i in range(5)]
P=[[(6*I[i][j]-Delta[i][j])/30 for j in range(5)] for i in range(5)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
def minv(A):
    n=5; M=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c]!=0); M[c],M[p]=M[p],M[c]
        pv=M[c][c]; M[c]=[x/pv for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[x-f*y for x,y in zip(M[r],M[c])]
    return [row[n:] for row in M]
tr=lambda A: sum(A[i][i] for i in range(5))
print("P_c =",[[int(x) for x in r] for r in P])
print("P^2==P:",mm(P,P)==P," tr P =",tr(P))
g1=[[x.a for x in r] for r in z1]; g2=[[x.a for x in r] for r in xi]
gens=[g1,g2,minv(g1),minv(g2)]
random.seed(1)
vals={}; bad=0; N=4000
for _ in range(N):
    g=I
    for _ in range(random.randint(1,18)): g=mm(g,random.choice(gens))
    Q=mm(mm(g,P),minv(g))
    T=tr(mm(P,Q))
    ok = T.denominator==1 and T>0 and math.isqrt(int(T))**2==int(T) and int(T)%2==1
    if not ok: bad+=1
    vals[T]=vals.get(T,0)+1
print("samples:",N," violations of 'odd square':",bad)
print("values of tr(P_c P_gc) seen:",sorted((int(k) if k.denominator==1 else k,v) for k,v in vals.items())[:12])
