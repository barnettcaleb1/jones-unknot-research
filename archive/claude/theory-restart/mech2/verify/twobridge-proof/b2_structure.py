#!/usr/bin/env python3
"""Referee check B2: steps (a)-(d) of the proof of Theorem A inside the 5-dimensional skein module S of the disc with points (T,0,1,2,3,4).
Builds the 5x5 matrices of X, Y on S, the projector P = (1-U_1/delta)(1-U_3/delta) (Jones-Wenzl on the bands (1,2), (3,4)),
the functional phi = (close 0 with 1, coefficient of b), and checks each claim."""
import sympy as sp, itertools
from lp import *
from skein import *
A=sp.symbols('A')
def lp2sp(p): return sum(c*A**e for e,c in p.items()) if p else sp.Integer(0)
# basis of S: all crossingless matchings of the cyclically ordered points T,0,1,2,3,4
pts=['T',0,1,2,3,4]
def noncrossing(n):
    """noncrossing perfect matchings of positions 0..n-1 on a circle"""
    if n==0: return [[]]
    out=[]
    for j in range(1,n,2):
        for a in noncrossing(j-1):
            for b in noncrossing(n-j-1):
                out.append([(0,j)]+[(x+1,y+1) for x,y in a]+[(x+j+1,y+j+1) for x,y in b])
    return out
basis=[norm([(pts[x],pts[y]) for x,y in m]) for m in noncrossing(6)]
assert len(basis)==5 and E1 in basis and E0 in basis and E2 in basis
idx={m:i for i,m in enumerate(basis)}
def name(m): return ''.join('(%s %s)'%tuple(sorted(map(str,p),key=lambda s:(s!='T',s))) for p in sorted(m,key=lambda p:sorted(map(str,p),key=lambda s:(s!='T',s))))
print('basis of S:',[name(m) for m in basis])
def op_matrix(f):
    M=sp.zeros(5,5)
    for j,m in enumerate(basis):
        img=f({m:ONE})
        for mm,c in img.items(): M[idx[mm],j]=lp2sp(c)
    return M
MX=op_matrix(lambda s: apply_word(s,LETTER['X'])); MY=op_matrix(lambda s: apply_word(s,LETTER['Y']))
Mx=op_matrix(lambda s: apply_word(s,LETTER['x'])); My=op_matrix(lambda s: apply_word(s,LETTER['y']))
assert sp.simplify(MX*Mx)==sp.eye(5) and sp.simplify(MY*My)==sp.eye(5)
U1=op_matrix(lambda s: U(s,1)); U3=op_matrix(lambda s: U(s,3))
d=-A**2-A**-2
P=sp.simplify((sp.eye(5)-U1/d)*(sp.eye(5)-U3/d))
print('P^2=P:',sp.simplify(P*P-P)==sp.zeros(5,5),'  rank P =',P.rank(),'  [P,X]=0:',sp.simplify(P*MX-MX*P)==sp.zeros(5,5),'  [P,Y]=0:',sp.simplify(P*MY-MY*P)==sp.zeros(5,5))
def vec(m): 
    v=sp.zeros(5,1); v[idx[m]]=1; return v
e1,e0,e2=vec(E1),vec(E0),vec(E2)
# phi: close (0,1), coefficient of b
phi=sp.zeros(1,5); psi=sp.zeros(1,5)
for j,m in enumerate(basis):
    img=close_bottom({m:ONE},0,5)
    phi[0,j]=lp2sp(img.get(B4,{})); psi[0,j]=lp2sp(img.get(C4,{}))
print('phi on basis:',list(phi),'  (coefficient of c:',list(psi),')')
print('(b)  P E1 - (E1 - E0/delta) =',list(sp.simplify(P*e1-(e1-e0/d))))
print('(b)  X E0 - E0 =',list(sp.simplify(MX*e0-e0)),'  Y E0 - E0 =',list(sp.simplify(MY*e0-e0)),'  phi(E0) =',phi*e0,'  phi(E1) =',phi*e1)
print('(b)  phi P - phi on S:',list(sp.simplify(phi*P-phi)),'   <- phi(P s) = phi(s) only on the span of the orbit of E1; see next line')
print('(b)  phi(P s) - phi(s) for s = E2:',sp.simplify((phi*P*e2-phi*e2)[0]))
# (c) eigen-claims on H = Im P
h1=sp.simplify(P*e1); h2=sp.simplify(P*e2)
k1=sp.simplify((MX*h1)[idx[E1]]/h1[idx[E1]])
print('(c)  X (P E1) = kappa (P E1):',sp.simplify(MX*h1-k1*h1)==sp.zeros(5,1),' kappa =',sp.factor(k1))
# phi Y = theta phi on Im P
th=sp.simplify((phi*MY*h1)[0]/(phi*h1)[0])
print('(c)  phi Y = theta phi on Im P:',sp.simplify((phi*MY*P-th*phi*P))==sp.zeros(1,5),' theta =',sp.factor(th))
# 2x2 matrices in the basis (h1, f), f in ker phi cap Im P
c2=sp.simplify((phi*h2)[0]/(phi*h1)[0]); f=sp.simplify(h2-c2*h1)
assert sp.simplify((phi*f)[0])==0
B=sp.Matrix.hstack(h1,f)
def restrict(M):
    # solve M*B = B*R
    R=sp.zeros(2,2)
    for j in range(2):
        col=M*B[:,j]
        sol=sp.linsolve((B,col)); (s,)=sol; R[:,j]=sp.Matrix(s)
    return sp.simplify(R)
RX=restrict(MX)/k1; RY=restrict(MY)/th
RX=sp.simplify(RX); RY=sp.simplify(RY)
print('normalised rho(X) on (PE1,F):',sp.factor(RX)); print('normalised rho(Y) on (PE1,F):',sp.factor(RY))
print('(d)  lam =',sp.factor(RX[1,1]),'  mu =',sp.factor(RY[1,1]),'  xi*eta =',sp.factor(RX[0,1]*RY[1,0]))
t=sp.symbols('t')
print('     with t = A^-4:  lam + t =',sp.simplify(RX[1,1]+A**-4),'  mu - t^-3 =',sp.simplify(RY[1,1]-A**12),'  xi*eta - t^-3(1-t^4) =',sp.simplify(RX[0,1]*RY[1,0]-A**12*(1-A**-16)))
N=sp.simplify(RY*RX.inv()); print('(e)  (rho(Y)rho(X)^-1)^2 =',sp.simplify(N*N),' trace =',sp.simplify(N.trace()))
# full twist: (Y x)^2 on S restricted to Im P is scalar
D2=sp.simplify(MY*Mx*MY*Mx*P); lamD=sp.simplify(D2[idx[E1],idx[E1]]/P[idx[E1],idx[E1]])
print('(e)  (Y x)^2 P = scalar * P:',sp.simplify(D2-lamD*P)==sp.zeros(5,5),' scalar =',sp.factor(lamD))
