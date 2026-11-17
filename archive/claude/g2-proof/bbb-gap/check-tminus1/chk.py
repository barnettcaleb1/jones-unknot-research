from fractions import Fraction as F
import itertools
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def mul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][l]*B[l][j] for l in range(k)) for j in range(m)] for i in range(n)]
def tr(A): return [list(r) for r in zip(*A)]
def inv(A):
    n=len(A); M=[r[:]+e for r,e in zip([x[:] for x in A],eye(n))]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c]!=0); M[c],M[p]=M[p],M[c]
        pv=M[c][c]; M[c]=[x/pv for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[a-f*b for a,b in zip(M[r],M[c])]
    return [r[n:] for r in M]
# generator matrices
def unred(n,i,t,T=False):
    M=eye(n); b=[[1-t,t],[F(1),F(0)]]
    if T: b=tr(b)
    for r in range(2):
        for c in range(2): M[i-1+r][i-1+c]=b[r][c]
    return M
def red(n,i,t,T=False):
    d=n-1; M=eye(d); k=i-1
    # standard reduced Burau: row k gets: M[k][k-1]=t, M[k][k]=-t, M[k][k+1]=1
    M[k][k]=-t
    if k-1>=0: M[k][k-1]=t
    if k+1<d: M[k][k+1]=F(1)
    return tr(M) if T else M
def rep(kind,n,t,T):
    g={}
    for i in range(1,n):
        A=kind(n,i,F(t),T); g[i]=A; g[-i]=inv(A)
    return g
def ev(g,w,n):
    M=eye(n)
    for x in w: M=mul(M,g[x])
    return M
def winv(w): return [-x for x in reversed(w)]
def comm(a,b): return a+b+winv(a)+winv(b)
def A(i,j):
    up=list(range(j-1,i,-1)); return up+[i,i]+winv(up)
A14,A24,A34=A(1,4),A(2,4),A(3,4)
print("A14,A24,A34 =",A14,A24,A34)
a=[1,2]*6; b=comm(comm(A14,A24),A34); phi0=comm(a,b)
print("len",len(phi0))
for kind,name in ((unred,"unreduced"),(red,"reduced")):
    for T in (False,True):
        for n in (4,5):
            d=n if kind is unred else n-1
            for tv in (-1,2,F(1,3)):
                g=rep(kind,n,tv,T)
                # braid relation sanity
                for i in range(1,n-1):
                    assert ev(g,[i,i+1,i],d)==ev(g,[i+1,i,i+1],d)
                for i in range(1,n):
                    for j in range(i+2,n): assert ev(g,[i,j],d)==ev(g,[j,i],d)
                print(f"{name:9s} T={T!s:5s} B{n} t={str(tv):>4s}: rho(Phi0)==I {ev(g,phi0,d)==eye(d)}; rho((s1s2)^6)==I {ev(g,a,d)==eye(d)}; rho(b)==I {ev(g,b,d)==eye(d)}")
