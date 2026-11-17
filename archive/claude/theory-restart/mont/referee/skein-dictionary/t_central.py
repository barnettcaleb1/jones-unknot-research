import sympy as sp
t,xi,eta=sp.symbols('t xi eta')
X=sp.Matrix([[1,1-t**4],[0,-t]]); Y=sp.Matrix([[1,0],[t**-3,t**-3]])
M=Y*X.inv()
print('(Y X^-1)^2 =',sp.simplify(M*M))
print('(Y X)^2 scalar?', sp.simplify((Y*X)**2))
# general xi,eta: trace condition
Xg=sp.Matrix([[1,xi],[0,-t]]); Yg=sp.Matrix([[1,0],[eta,t**-3]])
print('tr(Y X^-1)=0 <=> xi*eta =', sp.solve(sp.simplify((Yg*Xg.inv()).trace()),xi*eta) or sp.solve(sp.simplify((Yg*Xg.inv()).trace()),xi))
# v(P1), v(P3), channels and product
a,b=sp.symbols('a b')
v=sp.Matrix([a,(b-a)/(1-t**3)])
print('Y v = v(Y-box) check: Y*v(a,b) - v(a, t^-3 b):', sp.simplify(Y*v - sp.Matrix([a,(t**-3*b-a)/(1-t**3)])))
print('e1^T X^-m first row off-diag value/deriv at -1 for m=1..4:',[ (sp.simplify((X**-m)[0,1]).subs(t,-1), sp.simplify(sp.diff((X**-m)[0,1],t)).subs(t,-1)) for m in range(1,5)])
