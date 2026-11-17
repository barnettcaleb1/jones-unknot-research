#!/usr/bin/env python3
"""Referee check A1: matrix identities behind Theorem A and the normal form (sympy, exact)."""
import sympy as sp
t,xi,eta,lam,mu=sp.symbols('t xi eta lam mu')
rY=sp.Matrix([[1,0],[t**-3,t**-3]]); rX=sp.Matrix([[1,1-t**4],[0,-t]])
ry=rY.inv(); rx=rX.inv()
print('rho(y)=',sp.simplify(ry)); print('rho(x)=',sp.simplify(rx))
E=sp.simplify(ry*rX); print('E=',E, ' E^2=',sp.simplify(E*E))
# (e): general X=[[1,xi],[0,lam]], Y=[[1,0],[eta,mu]];  M = Y X^-1 ; M^2 scalar <=> M scalar or tr M = 0
X=sp.Matrix([[1,xi],[0,lam]]); Y=sp.Matrix([[1,0],[eta,mu]])
M=sp.simplify(Y*X.inv()); print('Y X^-1 =',M,' trace=',sp.simplify(M.trace()))
M2=sp.simplify(M*M)
print('offdiag of (YX^-1)^2:',sp.factor(M2[0,1]),'|',sp.factor(M2[1,0]),' diag diff:',sp.factor(M2[0,0]-M2[1,1]))
sol=sp.solve(sp.Eq(M.trace(),0),xi*eta) if False else None
tr=sp.simplify(M.trace().subs({lam:-t,mu:t**-3}))
print('trace at lam=-t, mu=t^-3:',sp.simplify(tr),' => xi*eta =',sp.solve(tr.subs(xi*eta,sp.Symbol('p')),sp.Symbol('p')) if False else sp.simplify(sp.solve(sp.Eq((1 - sp.Symbol('p')/(-t) + t**-3/(-t)),0),sp.Symbol('p'))[0]))
print('claimed xi*eta = t^-3(1-t^4):',sp.simplify(t**-3*(1-t**4)))
# J of the one-letter-pair YX for all four eigenvalue conventions: 1 + lam + mu
print('J(YX) general = 1 + xi*eta with xi*eta = lam + mu ; check:', sp.simplify((sp.Matrix([[1,0]])*X*Y*sp.Matrix([1,0]))[0]))
# same-handed alternative: relation (Y X)^2 central -> trace(YX)=0
print('trace(YX)=',sp.simplify((Y*X).trace()))
# check rho(Y) rho(X)^-1 squared is scalar for the actual matrices
N=sp.simplify(rY*rx); print('rho(Y)rho(X)^-1 =',N,' square=',sp.simplify(N*N))
# one block formula
def qn(n,z): return sum(z**i for i in range(n))
ok=True
for a in range(1,6):
    for b in range(1,6):
        J=sp.expand((sp.Matrix([[1,0]])*rX**b*rY**a*sp.Matrix([1,0]))[0])
        F=sp.expand(1+t**-3*qn(a,t**-3)*(1-t**4)*qn(b,-t))
        ok&=(sp.simplify(J-F)==0)
print('one-block formula J(Y^a X^b)=1+t^-3[a]_{t^-3}(1-t^4)[b]_{-t}, a,b<=5:',ok)
# mirror conjugation
D=sp.diag(1,-t**3)
print('D rho(y) D^-1 - rho(Y)(1/t) =',sp.simplify(D*ry*D.inv()-rY.subs(t,1/t)))
print('D rho(x) D^-1 - rho(X)(1/t) =',sp.simplify(D*rx*D.inv()-rX.subs(t,1/t)))
# first column / first row facts
print('rho(X)e1=',list(rX*sp.Matrix([1,0])),' e1^T rho(Y)=',list(sp.Matrix([[1,0]])*rY))
print('E e1 =',list(E*sp.Matrix([1,0])),' rho(y) e1 =',list(ry*sp.Matrix([1,0])), ' E rho(y) e1 =',list(sp.simplify(E*ry*sp.Matrix([1,0]))))
