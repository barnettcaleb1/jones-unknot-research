# Referee: claim 11. Braiding of U_q(sl2) on V_2 x V_2 in (a) the divided-power (Lusztig) lattice, (b) Astra's s-lattice
# (E w1 = s w0, E w2 = s w1, F w0 = s w1, F w1 = s w2, s^2 = [2]). Check involutivity at q = i (t = q^2 = -1).
import sympy as sp
q,s=sp.symbols('q s')
def qi(n): return sum(q**(n-1-2*k) for k in range(n))
def braid(E,F,wts):
    d=3; R=sp.zeros(9)
    for n in range(3):
        c=q**sp.Rational(n*(n-1),2)*(q-1/q)**n/sp.prod([qi(k) for k in range(1,n+1)])
        R+=c*sp.kronecker_product(E**n,F**n)
    H=sp.diag(*[q**sp.Rational(wts[a]*wts[b],2) for a in range(3) for b in range(3)])
    P=sp.zeros(9)
    for a in range(3):
        for b in range(3): P[b*3+a,a*3+b]=1
    return P*H*R
wts=[2,0,-2]
# (a) divided powers: E v1=[2]v0, E v2=v1, F v0=v1, F v1=[2]v2
E=sp.zeros(3); F=sp.zeros(3); E[0,1]=qi(2); E[1,2]=1; F[1,0]=1; F[2,1]=qi(2)
B=sp.simplify(braid(E,F,wts)); Bi=B.subs(q,sp.I); I9=sp.eye(9)
print('(a) divided-power lattice: entries Laurent in q:',all(sp.simplify(x*q**8).is_polynomial(q) for x in B))
print('    (B-1)(B+1)=0 at q=i?',sp.simplify((Bi-I9)*(Bi+I9))==sp.zeros(9),'  (B-1)^2(B+1)=0?',sp.simplify((Bi-I9)**2*(Bi+I9))==sp.zeros(9))
# (b) Astra lattice
E=sp.zeros(3); F=sp.zeros(3); E[0,1]=s; E[1,2]=s; F[1,0]=s; F[2,1]=s
B=braid(E,F,wts)
B=B.applyfunc(lambda x: sp.expand(sp.simplify(x)))
# replace s^2 by [2] where it occurs (entries are polynomials in s^2 after simplification)
B=B.applyfunc(lambda x: sp.simplify(sp.expand(x).subs(s**4,qi(2)**2).subs(s**2,qi(2))))
print('(b) s-lattice entries:',sorted(set(str(sp.factor(x)) for x in B if x!=0))[:12])
B0=B.subs(q,sp.I).subs(s,0)
print('    B at root (q=i, s=0) involution?',sp.simplify(B0*B0)==I9,'  = super flip (w1 even, w0,w2 odd)?')
SF=sp.zeros(9)
for a in range(3):
    for b in range(3):
        sign=-1 if (a!=1 and b!=1) else 1
        SF[b*3+a,a*3+b]=sign
print('   ',sp.simplify(B0-SF)==sp.zeros(9))
