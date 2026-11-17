# Decompose <D(n1,n2)> = sum_{e1,e2} c_{e1e2} lam_{e1}^{n1} mu_{e2}^{n2}, lam=(A,-A^-3), mu=(A^-1,-A^3)
import sympy as sp
from twist2 import tangle, D
A=sp.symbols('A')
def topoly(p): return sum(c*A**e for e,c in p.items())
lam=[A,-A**-3]; mu=[A**-1,-A**3]
cs=sp.symbols('c00 c01 c10 c11')
eqs=[]
for (n1,n2) in [(0,0),(1,0),(0,1),(1,1)]:
    val=topoly(D(*tangle(n1,n2)))
    eqs.append(sp.Eq(sum(cs[2*a+b]*lam[a]**n1*mu[b]**n2 for a in (0,1) for b in (0,1)),val))
sol=sp.solve(eqs,cs,dict=True)[0]
for c in cs: print(c,'=',sp.factor(sp.simplify(sol[c])))
# check on a grid
ok=all(sp.simplify(sum(sol[cs[2*a+b]]*lam[a]**n1*mu[b]**n2 for a in (0,1) for b in (0,1))-topoly(D(*tangle(n1,n2))))==0
       for n1 in range(-3,4) for n2 in range(-3,4))
print('decomposition verified on 7x7 grid:',ok)
