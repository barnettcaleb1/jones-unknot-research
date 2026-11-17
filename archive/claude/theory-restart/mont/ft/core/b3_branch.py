import clib, lp
known={'T(3,5)':{4:1,6:1,10:-1},'T(3,7)':{6:1,8:1,14:-1},'P(-2,3,7)':{5:1,7:1,11:-1,12:1,13:-1}}
def ident(V):
    k=tuple(sorted(V.items()))
    for nm,W in known.items():
        if k==tuple(sorted(W.items())): return nm
        if k==tuple(sorted({-e:c for e,c in W.items()}.items())): return nm+'*'
    return '?'
cases={'RHT':'s.l1.y0.x1.u2','LHT':'s.l1.x0.y1.u2','4_1 h1':'s.l1.y0.y0.x1.u2','4_1 h2':'s.l1.x0.x0.y1.u2'}
for nm,w in cases.items():
    J=lp.J(w); j=clib.j_of(J); a2=lp.a2(J)
    print(nm,w,' j =',j,' sigma_B(L_odd)=J\'(1)=',-8*j,' a2=',a2)
    for n in (1,-1,2,-2,3,-3):
        V=clib.V_branch(J,n)
        c=clib.hexp(V,3)
        lam=-c[1]/12 - (-8*j if n%2 else 0)/8      # Mullins in BRIEF convention: lambda = (1/12)V'(-1) - sigma/8, V'(-1) = -c1
        print('    n=%2d  V(L_n)=%s  [%s]  c1=%s c2=%s  Mullins lambda=%s  (Casson n*a2=%s)'%(n,sorted(V.items()),ident(V),c[1],c[2],lam,n*a2))
