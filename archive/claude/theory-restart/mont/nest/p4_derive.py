import sympy as sp
t,up,um=sp.symbols('t u_p u_m')
Phi3=1+t+t**2
# channel functionals as (coefA, coefB)
f0=(sp.Integer(1), (1+t**2)/t)                         # a=0: partial trace over the V_2 loop
f1=(-1/(t*Phi3), (1+t)*(1+t**2)/(t*Phi3))              # a=1: e_1^T X^-1 (necklace closure, Theorem N)
fm1=(-t**3/Phi3, (1+t)*(1+t**2)/Phi3)                  # a=-1: e_1^T X
lam=[sp.Integer(1),-t,t**3]
M=sp.Matrix([[1,1,1],[lam[0],lam[1],lam[2]],[1/lam[0],1/lam[1],1/lam[2]]])
Minv=M.inv()
K={}
for comp in (0,1):
    rhs=sp.Matrix([f0[comp], up*f1[comp], um*fm1[comp]])
    sol=Minv*rhs
    for c in range(3): K[(c,comp)]=sp.simplify(sol[c])
eqs=[sp.Eq(sp.numer(sp.together(K[(0,1)])),0), sp.Eq(sp.numer(sp.together(K[(2,0)]*0+K[(2,0)]-K[(2,0)]+K[(2,0)]*0+K[(2,0)]*0+K[(2,0)]*0+K[(2,0)]*0+K[(2,0)]*0+K[(2,0)]*0+K[(2,0)]*0+K[(2,0)]*0)),sp.numer(sp.together(K[(2,0)])))]
eqs=[sp.numer(sp.together(K[(0,1)])), sp.numer(sp.together(K[(2,0)+()] if False else K[(2,0)]))]
# admissibility zeros: K_0 has no B part, K_4 has no A part
cond=[sp.numer(sp.together(K[(0,1)])), sp.numer(sp.together(K[(2,0)]))]
s=sp.solve(cond,[up,um],dict=True)
print('admissibility forces:',s)
for sl in s:
    print('K_0 =',sp.factor(K[(0,0)].subs(sl)),'*A +',sp.factor(K[(0,1)].subs(sl)),'*B')
    print('K_2 =',sp.factor(K[(1,0)].subs(sl)),'*A +',sp.factor(K[(1,1)].subs(sl)),'*B')
    print('K_4 =',sp.factor(K[(2,0)].subs(sl)),'*A +',sp.factor(K[(2,1)].subs(sl)),'*B')
