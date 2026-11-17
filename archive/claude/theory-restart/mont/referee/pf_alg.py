"""Referee (PROOF lane): recompute the algebraic identities of REPORT sections 1-2 with sympy (exact)."""
import sympy as sp
t=sp.symbols('t')
X=sp.Matrix([[1,1-t**4],[0,-t]]); Y=sp.Matrix([[1,0],[t**-3,t**-3]])
e1=sp.Matrix([1,0]); s=1-t**3
def simp(e): return sp.simplify(sp.factor(e))
out=[]
# 1. eigen-data of rho(Y)
h1=sp.Matrix([1,1/(t**3-1)]); h3=sp.Matrix([0,1/(1-t**3)])
out.append(('Y h1 = h1', simp((Y*h1-h1).norm())==0 if False else all(simp(x)==0 for x in (Y*h1-h1))))
out.append(('Y h3 = t^-3 h3', all(simp(x)==0 for x in (Y*h3-t**-3*h3))))
out.append(('h1+h3 = e1', all(simp(x)==0 for x in (h1+h3-e1))))
out.append(('e1^T h3 = 0', simp(h3[0])==0))
# left eigenvector: e1^T Y = e1^T
out.append(('e1^T Y = e1^T', all(simp(x)==0 for x in (e1.T*Y-e1.T))))
# 2. coordinates a,b: v = a h1 + b h3  <=>  a = v1, b = v1 + (1-t^3) v2
a,b,v1,v2,w1,w2=sp.symbols('a b v1 v2 w1 w2')
v=a*h1+b*h3
out.append(('v1 = a', simp(v[0]-a)==0))
out.append(('v1+(1-t^3)v2 = b', simp(v[0]+s*v[1]-b)==0))
# 3. star product = channelwise product
def star(v,w): return sp.Matrix([v[0]*w[0], v[0]*w[1]+v[1]*w[0]+s*v[1]*w[1]])
A_=lambda v: v[0]; B_=lambda v: v[0]+s*v[1]
V=sp.Matrix([v1,v2]); W=sp.Matrix([w1,w2]); P=star(V,W)
out.append(('a(v*w)=a(v)a(w)', simp(A_(P)-A_(V)*A_(W))==0))
out.append(('b(v*w)=b(v)b(w)', simp(B_(P)-B_(V)*B_(W))==0))
out.append(('e1 unit', all(simp(x)==0 for x in (star(e1,V)-V))))
# 4. rho(Y) diagonal in (a,b): a(Yv)=a(v), b(Yv)=t^-3 b(v)
YV=Y*V
out.append(('a(Yv)=a(v)', simp(A_(YV)-A_(V))==0))
out.append(('b(Yv)=t^-3 b(v)', simp(B_(YV)-t**-3*B_(V))==0))
# Y acting on vector = star with Y e1 (box operator)
out.append(('Y v = (Y e1)*v', all(simp(x)==0 for x in (Y*V-star(Y*e1,V)))))
# X is NOT a box operator: X v != (X e1)*v in general
out.append(('X v == (X e1)*v ? (expect False)', all(simp(x)==0 for x in (X*V-star(X*e1,V)))))
# 5. e1^T X^mu closed form, mu in [-6,6]
ok=True
for mu in range(-6,7):
    M=X**mu if mu>=0 else (X.inv())**(-mu)
    row=e1.T*M
    if simp(row[0]-1)!=0 or simp(row[1]-(1-t)*(1+t**2)*(1-(-t)**mu))!=0: ok=False; print('closed form fails',mu)
out.append(('e1^T X^mu = (1,(1-t)(1+t^2)(1-(-t)^mu)), mu=-6..6', ok))
# 6. Theorem 2.3 channel functional: e1^T X^mu h_c = w_c/Phi3
Phi3=1+t+t**2
ok=True
for mu in range(-6,7):
    M=X**mu if mu>=0 else (X.inv())**(-mu)
    w1_=t+(1+t**2)*(-t)**mu; w3_=(1+t**2)*(1-(-t)**mu)
    if simp((e1.T*M*h1)[0]-w1_/Phi3)!=0 or simp((e1.T*M*h3)[0]-w3_/Phi3)!=0: ok=False; print('channel fn fails',mu)
out.append(('e1^T X^mu h1 = w1/Phi3, e1^T X^mu h3 = w3/Phi3, mu=-6..6', ok))
# 7. Corollary 5.1: P + Q(-t)^mu
ok=True
for mu in range(-5,6):
    M=X**mu if mu>=0 else (X.inv())**(-mu)
    J=(e1.T*M*V)[0]
    Pp=v1+(1-t)*(1+t**2)*v2; Qq=-(1-t)*(1+t**2)*v2
    if simp(J-(Pp+Qq*(-t)**mu))!=0: ok=False
    # P,Q in channel form
    Aa=v1; Bb=v1+s*v2
    if simp(Pp-(t*Aa+(1+t**2)*Bb)/Phi3)!=0 or simp(Qq-(1+t**2)*(Aa-Bb)/Phi3)!=0: ok=False
out.append(('Cor 5.1: J_mu = P + Q(-t)^mu with P,Q channel forms', ok))
# 8. eigenvalues of X: e1 is eigvec (1), left: e1^T X has (1, ..)  ; X acts on H: E1 eigenvalue 1
out.append(('X e1 = e1', all(simp(x)==0 for x in (X*e1-e1))))
# 9. twist rows: X^j Y e1, a_r, b_r closed forms
ok=True
for j in range(0,7):
    vv=X**j*Y*e1
    ar=1+t**-3*(1-t)*(1+t**2)*(1-(-t)**j)
    br=t**-3-t**-2+t**-1+(-1)**j*(t**(j-2)-t**(j-1))
    if simp(A_(vv)-(e1.T*X**j*Y*e1)[0])!=0: ok=False
    if simp(A_(vv)-ar)!=0: ok=False; print('a_r fails',j, sp.expand(A_(vv)))
    if j>=1 and simp(sp.expand(B_(vv))-br)!=0: ok=False; print('b_r fails',j, sp.expand(B_(vv)), br)
    if simp(vv[1]-(-t)**j*t**-3)!=0: ok=False; print('second coord fails',j)
out.append(('twist rows: a_r, b_r closed forms (j=0..6; b_r for j>=1)', ok))
# mirror rows: X^-j Y^-1 e1 vs t->1/t of X^j Y e1 (brief: 'mirror rows: t -> 1/t (no unit shift)')
ok=True
for j in range(1,6):
    vv=(X.inv())**j*Y.inv()*e1; ww=X**j*Y*e1
    if simp(A_(vv)-A_(ww).subs(t,1/t))!=0: ok=False; print('mirror a fails',j)
    if simp(B_(vv)-B_(ww).subs(t,1/t))!=0: ok=False; print('mirror b fails',j, sp.expand(B_(vv)), sp.expand(B_(ww).subs(t,1/t)))
out.append(('mirror rows: (a,b) of X^-j Y^-1 e1 = (a,b)(1/t) of X^j Y e1', ok))
for k,vv in out: print(('OK  ' if vv else 'FAIL'),k) if not k.endswith('(expect False)') else print(('OK  ' if not vv else 'FAIL'),k)
