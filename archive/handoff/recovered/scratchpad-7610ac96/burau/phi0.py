from fractions import Fraction as F
import itertools
def mat_id(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def mul(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def inv2(A):
    # Gauss-Jordan over Fractions
    n=len(A); M=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c]!=0); M[c],M[p]=M[p],M[c]
        pv=M[c][c]; M[c]=[x/pv for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[a-f*b for a,b in zip(M[r],M[c])]
    return [row[n:] for row in M]
def sigma(i,n,t):
    # unreduced Burau: sigma_i acts on strands i,i+1 (1-based) by [[1-t, t],[1,0]]
    M=mat_id(n); i0=i-1
    M[i0][i0]=1-t; M[i0][i0+1]=t; M[i0+1][i0]=F(1); M[i0+1][i0+1]=F(0)
    return M
def word(w,n,t):
    M=mat_id(n)
    for g in w:
        S=sigma(abs(g),n,t)
        if g<0: S=inv2(S)
        M=mul(M,S)
    return M
def A(i,j):
    # pure braid generator A_ij = s_{j-1} ... s_{i+1} s_i^2 s_{i+1}^-1 ... s_{j-1}^-1
    pre=list(range(j-1,i,-1)); return pre+[i,i]+[-k for k in reversed(pre)]
def inv(w): return [-g for g in reversed(w)]
def comm(a,b): return a+b+inv(a)+inv(b)
def run(n,t):
    y1,y2,y3=A(1,4),A(2,4),A(3,4)
    inner=comm(comm(y1,y2),y3)
    full=[1,2]*6
    phi=comm(full,inner)
    M=word(phi,n,t)
    isI = M==mat_id(n)
    return M,isI,len(phi)
for n in (4,5):
    for t in (F(-1),F(2),F(3)):
        M,isI,L=run(n,t)
        print(f"n={n} t={t}: identity={isI} (word length {L})")
        if not isI and n==4:
            print('  row0:',[str(x) for x in M[0]])
# sanity: Brunnian check by deleting strand 4 is structural; check delete strand 1 via Burau at t=2 on B_3 (remove generator 1 usage is not a homomorphism; skip)
