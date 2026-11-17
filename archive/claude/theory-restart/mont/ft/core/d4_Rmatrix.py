# Integral R-matrix of U_q(sl2) on V(2) x V(2) (Weyl module, divided-power basis), check R(q=i)^2 = id.
import sympy as sp
q=sp.symbols('q')
def qint(n): return sum(q**(n-1-2*k) for k in range(n)) if n>0 else 0
def qfact(n):
    r=1
    for k in range(1,n+1): r*=qint(k)
    return r
lam=2; d=3
# basis v_k = F^(k) v_0 (divided powers), weight lam-2k. E v_k = [lam-k+1] v_{k-1}; F v_k = [k+1] v_{k+1}
E=sp.zeros(d); Fm=sp.zeros(d); Kd=sp.zeros(d)
for k in range(d):
    if k>0: E[k-1,k]=qint(lam-k+1)
    if k<d-1: Fm[k+1,k]=qint(k+1)
    Kd[k,k]=q**(lam-2*k)
wt=[lam-2*k for k in range(d)]
def kron(A,B): return sp.kronecker_product(A,B)
# R = q^{H(x)H/2} sum_n q^{n(n-1)/2} (q-q^-1)^n/[n]! E^n (x) F^n
R=sp.zeros(d*d)
for n in range(0,d):
    term=q**sp.Rational(n*(n-1),2)*(q-1/q)**n/qfact(n)*kron(E**n,Fm**n)
    R+=term
Hq=sp.diag(*[q**sp.Rational(wt[a]*wt[b],2) for a in range(d) for b in range(d)])
R=sp.simplify(Hq*R)
P=sp.zeros(d*d)
for a in range(d):
    for b in range(d): P[b*d+a,a*d+b]=1
Rc=sp.simplify(P*R)            # braiding R-check
Ri=Rc.subs(q,sp.I)
print('entries integral (Laurent in q)?', all(sp.simplify(sp.together(x)).is_polynomial(q) or sp.simplify(x*q**8).is_polynomial(q) for x in Rc))
M2=sp.simplify(Ri*Ri)
print('R(i)^2 == id ?', M2==sp.eye(d*d))
ev=sp.simplify(Rc).eigenvals() if False else None
# minimal polynomial check at q=i
I9=sp.eye(d*d)
print('(R(i)-1)(R(i)+1) == 0 ?', sp.simplify((Ri-I9)*(Ri+I9))==sp.zeros(d*d))
print('(R(i)-1)^2(R(i)+1) == 0 ?', sp.simplify((Ri-I9)**2*(Ri+I9))==sp.zeros(d*d))
# generic eigenvalues on channels (as a check): characteristic polynomial factor
x=sp.symbols('x')
cp=sp.factor(sp.simplify((Rc-x*I9).det()))
print('char poly of R-check (generic q):',cp)
