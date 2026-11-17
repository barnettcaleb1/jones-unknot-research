import sys, json
import sympy as sp
t=sp.symbols('t')
F=json.load(open('nest/p4_functionals.json'))
def topoly(L): return sum(c*t**e for e,c in L)
ab={}
for a,(L1,L2) in F.items():
    a=int(a); l1=topoly(L1); l2=topoly(L2)
    beta=sp.cancel(l2/(1-t**3)); alpha=sp.cancel(l1-l2/(1-t**3))
    ab[a]=(alpha,beta)
    print('a=%d  alpha_a = %s   beta_a = %s'%(a,sp.factor(alpha),sp.factor(beta)))
# fit alpha_a = u_a (h01 + h21 (-t)^a), beta_a = u_a (h23 (-t)^a + h43 t^(3a)), u_a = s^((a-1)/2) t^(k a)
lam0,lam2,lam4=1,-t,t**3
best=[]
for k in range(-12,13):
    for s in (1,-1):
        u=lambda a: s**((a-1)//2)*t**(k*a)
        # solve from a=1,3
        h01,h21,h23,h43=sp.symbols('h01 h21 h23 h43')
        eqs=[sp.Eq(ab[a][0], u(a)*(h01*lam0**a+h21*lam2**a)) for a in (1,3)]+[sp.Eq(ab[a][1], u(a)*(h23*lam2**a+h43*lam4**a)) for a in (1,3)]
        sol=sp.solve(eqs,[h01,h21,h23,h43],dict=True)
        if not sol: continue
        sol=sol[0]
        ok=True
        for a in ab:
            if sp.simplify(ab[a][0]-u(a)*(sol[h01]*lam0**a+sol[h21]*lam2**a))!=0 or sp.simplify(ab[a][1]-u(a)*(sol[h23]*lam2**a+sol[h43]*lam4**a))!=0:
                ok=False; break
        if ok:
            best.append((k,s,{str(x):sp.factor(sol[x]) for x in sol}))
for b in best: print('FIT u_a = (%d)^((a-1)/2) t^(%d a):'%(b[1],b[0]),b[2])
if not best: print('no fit with u_a = s^((a-1)/2) t^(k a) and eigenvalues (1,-t,t^3)')
