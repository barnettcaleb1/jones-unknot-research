# Frame check: U = ker e1 ∩ ker e5 in W(6,0) (spin-1 at {1,2} and {5,6}); 2-dim.
# X = T_c0 = (s1 s2)^3 | U, Y = s3^2 | U. Tree data over Q((1/A)): translation lengths, axis overlap.
import sympy as sp
A = sp.symbols('A'); d = -A**2 - A**-2
def ncm(p):
    if not p: return [()]
    a=p[0]; out=[]
    for k in range(1,len(p),2):
        for x in ncm(p[1:k]):
            for y in ncm(p[k+1:]): out.append(((a,p[k]),)+x+y)
    return out
B=[tuple(sorted(m)) for m in ncm(list(range(6)))]; I={m:i for i,m in enumerate(B)}
def E(i):
    M=sp.zeros(5,5)
    for j,m in enumerate(B):
        P={};[P.update({a:b,b:a}) for a,b in m]
        if P[i]==i+1: M[j,j]+=d
        else:
            a,b=P[i],P[i+1]; n=[q for q in m if i not in q and i+1 not in q]+[(i,i+1),tuple(sorted((a,b)))]
            M[I[tuple(sorted(n))],j]+=1
    return M
Es=[E(i) for i in range(5)]; S=[A*sp.eye(5)+Es[i]/A for i in range(5)]
br=sp.simplify(S[0]*S[1]*S[0]-S[1]*S[0]*S[1]); print('braid rel ok:', br==sp.zeros(5,5))
N=Es[0].col_join(Es[4]).nullspace(); print('dim U =',len(N))
Ub=sp.Matrix.hstack(*N)
def restr(M):
    R=(Ub.T*Ub).inv()*Ub.T*(M*Ub); R=sp.simplify(R)
    assert sp.simplify(Ub*R-M*Ub)==sp.zeros(5,2); return R
X=restr((S[0]*S[1])**3); Y=restr(S[2]**2)
def deg(f):
    f=sp.together(sp.simplify(f)); n,dn=sp.fraction(f)
    return sp.degree(sp.expand(n*A**60),A)-sp.degree(sp.expand(dn*A**60),A)
def tau(g): return 2*deg(g.trace())-deg(g.det())
for nm,g in [('X',X),('Y',Y),('XY',X*Y),('XY^-1',X*Y.inv()),('X^-1Y',X.inv()*Y),('X^2Y',X**2*Y),('X^2Y^-1',X**2*Y.inv()),('X^3Y^-2',X**3*Y.inv()**2),('X^3Y^2',X**3*Y**2)]:
    print(nm,'tau =',tau(g))
# eigenlines and cross-ratio
ev=lambda M,lam: (M-lam*sp.eye(2)).nullspace()[0]
l1=ev(X,A**6); l2=ev(X,A**-6); m1=ev(Y,A**2); m0=ev(Y,A**-6)
dt=lambda u,v: sp.simplify(u[0]*v[1]-u[1]*v[0])
cr=sp.factor(sp.simplify(dt(l1,m1)*dt(l2,m0)/(dt(l1,m0)*dt(l2,m1))))
print('cross-ratio [l(3/2),l(1/2); m(1),m(0)] =',cr); print('deg cr =',deg(cr),' deg(1-cr) =',deg(1-cr))
