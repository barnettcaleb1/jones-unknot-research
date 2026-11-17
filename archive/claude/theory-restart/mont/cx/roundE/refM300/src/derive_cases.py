"""refM300: INDEPENDENT symbolic derivation (sympy) of the weak-end case conditions.
Unit <=> F = S1 + S2 = c t^e Phi_3 <=> normalised expansion of F at each end = 1 + u + u^2 + 0 u^3 + 0 ...
Weak end, offset d = (degree of S1) - (degree of S2) toward the expansion, e = lc S2 / lc S1 in {+1,-1}.
s1 = exp(A1 u + A2 u^2 + A3 u^3), s2 = exp(B1 u + B2 u^2 + B3 u^3) (normalised S1, S2 at that end).
  d > 0 : F_norm = s1 + e u^d s2;   d < 0 : F_norm = s2 + e u^|d| s1;
  d = 0, e = +1 : F_norm = (s1 + s2)/2;   d = 0, e = -1 : F = (s1 - s2) = c1 u + c2 u^2 + c3 u^3, r = 1 iff c1 != 0:
                  F_norm = 1 + (c2/c1) u + (c3/c1) u^2  -> first condition c2 = c1.
Substitution (LP variables): A1 = p1 + RA + al, A2 = p2 + LA + La, B1 = q1 + RB + al + P, B2 = q2 + LB + La + Lam,
and the weak-end mismatch B1 - A1 = mB (strong end r >= 2 + sigma-law)  [the 'P0' row].
Output: for each case a list of affine equations  sum coef[v] v + const = 0  over v in (al,P,La,Lam,RA,LA,RB,LB,mB,p1,p2,q1,q2)."""
import sympy as sp, pickle
u=sp.symbols('u')
A1,A2,A3,B1,B2,B3,m=sp.symbols('A1 A2 A3 B1 B2 B3 m')
al,P,La,Lam,RA,LA,RB,LB,mB,p1,p2,q1,q2=sp.symbols('al P La Lam RA LA RB LB mB p1 p2 q1 q2')
def ser(a1,a2,a3,K=4):
    return sp.series(sp.exp(a1*u+a2*u**2+a3*u**3),u,0,K).removeO()
s1=ser(A1,A2,A3); s2=ser(B1,B2,B3)
def coef(expr,k): return sp.expand(expr).coeff(u,k)
SUB={A1:p1+RA+al, A2:p2+LA+La, B1:q1+RB+al+P, B2:q2+LB+La+Lam}
P0=sp.Eq(q1+RB+al+P-(p1+RA+al), mB)       # mismatch row
out={}
def record(name,conds,extra=()):
    eqs=[sp.expand(c.subs(SUB)) for c in conds]
    out[name]=dict(eqs=[sp.srepr(e) for e in eqs]+[sp.srepr(sp.expand(P0.lhs-P0.rhs))],
                   raw=[str(c) for c in conds],extra=list(extra))
for d in (1,2,3,4,5):
    for e in (1,-1):
        F=s1+e*u**d*s2
        conds=[coef(F,1)-1, coef(F,2)-1]
        # for d >= 3 the eps does not enter at order <= 2
        record('d=%d e=%d'%(d,e),conds)
        F=s2+e*u**d*s1
        conds=[coef(F,1)-1, coef(F,2)-1]
        record('d=-%d e=%d'%(d,e),conds)
# d = 0, e = +1 (no cancellation):  (s1+s2)/2
F=(s1+s2)/2
record('d=0 r=0',[coef(F,1)-1, coef(F,2)-1])
# d = 0, e = -1, r = 1 : c1 = coef(s1-s2,1) != 0, first condition c2 = c1
G=s1-s2
c1=coef(G,1); c2=coef(G,2)
record('d=0 r=1',[c2-c1],extra=['c1 = A1-B1 = -mB != 0'])
pickle.dump(out,open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/derived_cases.pkl','wb'))
for k,v in out.items(): print(k,v['raw'])
# order-3 F1 lemma ('d=-1 e=-1'): u^3 coefficient with X2 = l1(s2) = 2 and l2(s2) = X1 - 1
F=s2-u*s1
c3=sp.expand(coef(F,3))
sol=sp.expand(c3.subs({B1:2, B2:A1-1}))
print('F1 order-3 coefficient (B1=2, B2=A1-1):', sol, ' -> condition B3 - A2 =', sp.simplify(sp.solve(sp.Eq(sol,0),B3)[0]-A2))
print('   with A1 = 2 - mB :', sp.expand((sp.solve(sp.Eq(sol,0),B3)[0]-A2).subs(A1,2-mB)))
# mirror F1' ('d=1 e=-1'): F = s1 - u s2 with X1 = l1(s1) = 2, l2(s1) = X2 - 1
F=s1-u*s2
c3=sp.expand(coef(F,3))
sol=sp.expand(c3.subs({A1:2, A2:B1-1}))
print("F1' order-3 coefficient:", sol, ' -> A3 - B2 =', sp.expand(sp.solve(sp.Eq(sol,0),A3)[0]-B2), ' with B1 = 2 + mB:', sp.expand((sp.solve(sp.Eq(sol,0),A3)[0]-B2).subs(B1,2+mB)))
# tie T2 condition: d=0, e=-1, A1 = B1 (r >= 2), D2 = A2 - B2 != 0: F_norm = 1 + (c3/c2) u + ... ; need c3 = c2
G=s1-s2
c2=sp.expand(coef(G,2).subs(B1,A1)); c3=sp.expand(coef(G,3).subs(B1,A1))
print('tie r=2: c2 =',sp.factor(c2),' c3 =',sp.factor(c3),' c3 - c2 =',sp.factor(sp.expand(c3-c2)))
