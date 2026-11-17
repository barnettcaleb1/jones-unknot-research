# Referee check: genus-2 invariant part of a_2(K_c) from the standard Heegaard Seifert form.
# Independent of build-identity's script. Exact rationals.
from fractions import Fraction as F
import itertools, random
# H basis order: a1,b1,a2,b2 ; symplectic a_i.b_i=1
n=4
def J(x,y):
    a1,b1,a2,b2=x; c1,d1,c2,d2=y
    return a1*d1-b1*c1+a2*d2-b2*c2
# Seifert form theta(u,v)=lk(u,v^+): theta(a_i,.)=0, theta(.,b_j)=0, theta(b_i,a_j)=delta_ij
TH=[[0]*4 for _ in range(4)]
TH[1][0]=1; TH[3][2]=1
def theta(x,y): return sum(x[i]*TH[i][j]*y[j] for i in range(4) for j in range(4))
pairs=list(itertools.combinations(range(4),2))
def wedge(x,y): return {p: x[p[0]]*y[p[1]]-x[p[1]]*y[p[0]] for p in pairs}
def L2theta(X,Y):  # Lambda^2 theta on decomposable-basis expansion
    s=0
    for (i,j),xv in X.items():
        for (k,l),yv in Y.items():
            if xv==0 or yv==0: continue
            s+= xv*yv*(TH[i][k]*TH[j][l]-TH[i][l]*TH[j][k])
    return s
def B(X,Y): return F(L2theta(X,Y)+L2theta(Y,X),2)
# volume pairing Q(X,Y)=X^Y/vol, vol=a1^b1^a2^b2
def perm_sign(seq):
    s=1; seq=list(seq)
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            if seq[i]>seq[j]: s=-s
    return s
def Q(X,Y):
    s=0
    for (i,j),xv in X.items():
        for (k,l),yv in Y.items():
            idx=[i,j,k,l]
            if len(set(idx))<4: continue
            s+=xv*yv*perm_sign(idx)
    return s
basis=[{p:(1 if p==q else 0) for p in pairs} for q in pairs]
omega={p:0 for p in pairs}; omega[(0,1)]=1; omega[(2,3)]=1
print("B(omega,e)=0 for all e:", all(B(omega,e)==0 and B(e,omega)==0 for e in basis))
# primitive part [11] = omega^perp under Q ; compute trace of B against Q^{-1} on [11]

def inv(M):
    n=len(M); A=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for c in range(n):
        p=next(r for r in range(c,n) if A[r][c]!=0); A[c],A[p]=A[p],A[c]
        pv=A[c][c]; A[c]=[v/pv for v in A[c]]
        for r in range(n):
            if r!=c and A[r][c]!=0:
                f=A[r][c]; A[r]=[a-f*b for a,b in zip(A[r],A[c])]
    return [row[n:] for row in A]
Gq=[[F(Q(basis[r],basis[c])) for c in range(6)] for r in range(6)]
Gb=[[B(basis[r],basis[c]) for c in range(6)] for r in range(6)]
Qi=inv(Gq)
trQB=sum(Qi[i][k]*Gb[k][i] for i in range(6) for k in range(6))
print("tr_Q(B) on Lambda^2 =", trQB)
print("invariant part of a2 on any splitting =", F(1,4)*F(-2,5)*trQB)
def matmul(A,Bm): return [[sum(A[i][k]*Bm[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def rand_sp():
    M=[[int(i==j) for j in range(4)] for i in range(4)]
    for _ in range(14):
        v=[random.randint(-2,2) for _ in range(4)]; k=random.choice([-1,1])
        # transvection x -> x + k*J(v,x)*v
        T=[[int(i==j)+k*v[i]*Jrow(v)[j] for j in range(4)] for i in range(4)]
        M=matmul(T,M)
    return M
def Jrow(v):
    # J(v,x) = sum_j r_j x_j
    a1,b1,a2,b2=v
    return [-b1,a1,-b2,a2]
ok=True; vals=set()
for t in range(300):
    M=rand_sp()
    cols=[[M[r][i] for r in range(4)] for i in range(4)]
    x,y,x2,y2=cols
    assert J(x,y)==1 and J(x2,y2)==1 and J(x,x2)==0 and J(x,y2)==0 and J(y,x2)==0 and J(y,y2)==0
    a2=theta(x,x)*theta(y,y)-theta(x,y)*theta(y,x)
    o1=wedge(x,y); o2=wedge(x2,y2)
    u={p:o1[p]-o2[p] for p in pairs}
    vals.add(a2)
    if F(a2)!=F(1,4)*B(u,u): ok=False; print("mismatch",a2,B(u,u)); break
    a2b=theta(x2,x2)*theta(y2,y2)-theta(x2,y2)*theta(y2,x2)
    if a2b!=a2: ok=False; print("sides differ",a2,a2b); break
print("a2=(1/4)B(u,u), both sides equal, 300 random splittings:", ok, "sample a2 values:", sorted(vals)[:12])
