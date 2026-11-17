import itertools, sys
from fractions import Fraction as Fr
# polynomials in t as dict exp->coef ; matrices over Z[t,t^-1] via evaluation at integer points + interpolation is heavy; use sympy-free approach: evaluate at several t values and compare with target values
def burau(n,i,t):
    # unreduced Burau for sigma_i (1-indexed), n strands, numeric t
    M=[[Fr(1) if r==c else Fr(0) for c in range(n)] for r in range(n)]
    M[i-1][i-1]=1-t; M[i-1][i]=t; M[i][i-1]=Fr(1); M[i][i]=Fr(0)
    return M
def mul(A,B):
    n=len(A); return [[sum(A[r][k]*B[k][c] for k in range(n)) for c in range(n)] for r in range(n)]
def det(M):
    n=len(M); M=[r[:] for r in M]; d=Fr(1)
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=0),None)
        if p is None: return Fr(0)
        if p!=c: M[c],M[p]=M[p],M[c]; d=-d
        d*=M[c][c]
        for r in range(c+1,n):
            f=M[r][c]/M[c][c]
            M[r]=[a-f*b for a,b in zip(M[r],M[c])]
    return d
def alex_val(n,word,t):
    t=Fr(t)
    M=[[Fr(1) if r==c else Fr(0) for c in range(n)] for r in range(n)]
    for i in word: M=mul(M,burau(n,i,t))
    # reduced: det(I - M) with one row/col removed * (1-t)/(1-t^n)
    A=[[ (Fr(1) if r==c else Fr(0))-M[r][c] for c in range(n-1)] for r in range(n-1)]
    return det(A)
def perm_cycles(n,word):
    p=list(range(n))
    for i in word: p[i-1],p[i]=p[i],p[i-1]
    seen=set(); c=0
    for s in range(n):
        if s in seen: continue
        c+=1; x=s
        while x not in seen: seen.add(x); x=p[x]
    return c
def target_val(t):
    t=Fr(t); return (t**20-1)*(t-1)/((t**4-1)*(t**5-1))
if __name__=='__main__':
    hits=[]
    for gam in itertools.product([1,2,3],repeat=6):
        w=[1,3]+list(gam)+[3]+list(gam)[::-1]
        if perm_cycles(4,w)!=1: continue
        ok=True
        for t in (2,3,5):
            v=alex_val(4,w,t); tv=target_val(t)
            # equal up to sign and power of t
            r=v/tv
            # r must be +- t^k
            x=abs(r); k=0
            while x>1: x/=t; k+=1
            while x<1: x*=t; k-=1
            if x!=1: ok=False;break
        if ok: hits.append(gam)
    print('gamma with closure Alexander polynomial of T(4,5):',len(hits)); print(hits[:20])
