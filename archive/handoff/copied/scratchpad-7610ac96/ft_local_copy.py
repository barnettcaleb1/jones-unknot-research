import sympy as S
q=S.symbols('q',nonzero=True)
s=S.symbols('s',nonzero=True)
def red(x):
 x=S.cancel(x)
 n,d=S.fraction(x)
 n=S.rem(n,S.Poly(s*s-q-q**-1,s).as_expr(),s)
 d=S.rem(d,S.Poly(s*s-q-q**-1,s).as_expr(),s)
 return S.cancel(n/d)
def matred(M):return M.applyfunc(red)
E1=S.Matrix([[0,1],[0,0]]); F1=E1.T; K1=S.diag(q,q**-1)
E2=S.Matrix([[0,s,0],[0,0,s],[0,0,0]]);F2=E2.T;K2=S.diag(q*q,1,q**-2)
wt1=[1,-1];wt2=[2,0,-2]
def R(Ea,Fb,wa,wb):
 dim=len(wa)*len(wb)
 D=S.diag(*[q**S.Rational(a*b,2) for a in wa for b in wb])
 out=S.eye(dim)
 fact=1
 for n in range(1,min(len(wa),len(wb))):
  fact*= (q**n-q**-n)/(q-q**-1)
  out+=q**S.Rational(n*(n-1),2)*(q-q**-1)**n/fact*S.kronecker_product(Ea**n,Fb**n)
 return matred(D*out)
def swap(a,b):
 P=S.zeros(a*b)
 for i in range(a):
  for j in range(b):P[j*a+i,i*b+j]=1
 return P
R22=R(E2,F2,wt2,wt2)
DeltaE22=S.kronecker_product(E2,K2)+S.kronecker_product(S.eye(3),E2)
DeltaEop22=S.kronecker_product(K2,E2)+S.kronecker_product(E2,S.eye(3))
print('R intertwines E22',matred(R22*DeltaE22-DeltaEop22*R22)==S.zeros(9))
B22=swap(3,3)*R22
print('B22 eigenpoly',S.factor(B22.charpoly().as_expr()))
B0=B22.subs(s,0).subs(q,S.I).applyfunc(S.simplify)
print('B22(0)^2=I',B0**2==S.eye(9))
print('B0',B0)
d=q*q+1+q**-2
i=S.zeros(6,2);i[1,0]=q*q;i[3,0]=-s;i[4,1]=-1;i[2,1]=q*s
p=S.zeros(2,6);p[0,1]=1/d;p[0,3]=-q**-1*s/d;p[1,4]=-q**-2/d;p[1,2]=s/d
DE=S.kronecker_product(E1,K2)+S.kronecker_product(S.eye(2),E2)
DF=S.kronecker_product(F1,S.eye(3))+S.kronecker_product(K1**-1,F2)
print('pi',matred(p*i)==S.eye(2))
print('i E,F',matred(DE*i-i*E1)==S.zeros(6,2),matred(DF*i-i*F1)==S.zeros(6,2))
print('p E,F',matred(p*DE-E1*p)==S.zeros(2,6),matred(p*DF-F1*p)==S.zeros(2,6))
B12=swap(2,3)*R(E1,F2,wt1,wt2)
B21=swap(3,2)*R(E2,F1,wt2,wt1)
T=matred(B21*B12)
print('T satisfies CH',matred((T-q**-4*S.eye(6))*(T-q**2*S.eye(6)))==S.zeros(6))
print('T eigenpoly',S.factor(T.charpoly().as_expr()))
# coevaluation and evaluation; column order 00,01,02,10,11,12,20,21,22
co=S.zeros(9,1);co[2]=q*q;co[4]=-q*q;co[6]=1
A=S.Matrix(3,3,list(co))
ev=A.inv().reshape(1,9)
print('co E,F',matred(DeltaE22*co)==S.zeros(9,1),matred((S.kronecker_product(F2,S.eye(3))+S.kronecker_product(K2**-1,F2))*co)==S.zeros(9,1))
print('ev E,F',matred(ev*DeltaE22)==S.zeros(1,9),matred(ev*(S.kronecker_product(F2,S.eye(3))+S.kronecker_product(K2**-1,F2)))==S.zeros(1,9))
print('evco',matred(ev*co))
