# Sanity check (LIT lane): colour-2 (spin-1) Jones of T(2,n) via 2-strand recoupling, expanded at t = -1.
# Claim to test: J3(K; -e^h) = 1 - 24 a2(K) h^2 + O(h^3)  (knot-level analogue of F2 / osp(1|2) mechanism).
import sympy as sp
t,h=sp.symbols('t h')
def qint(n):  # [n] in q=A^2, expressed in t=A^-4 (n odd): sum_{k} A^{2k} for k=-(n-1)..(n-1) step 2 -> t^{-k/2}
    return sum(t**sp.Rational(-k,2) for k in range(-(n-1),n,2))
def J3_T2(n):
    # half-twist eigenvalues for two colour-2 strands, channels c=0,2,4: A^-8, -A^-4, A^4  ->  t^2, -t, t^-1
    lam={0:t**2,2:-t,4:t**-1}
    Delta={c:qint(c+1) for c in (0,2,4)}   # (-1)^c [c+1], c even
    framed=sum(Delta[c]*lam[c]**n for c in (0,2,4))
    theta2=t**-2   # colour-2 twist (-1)^2 A^{8} = t^-2
    return sp.simplify(framed/(theta2**n)/Delta[2])
for n in (3,5,7,-3,9):
    J=sp.factor(sp.simplify(J3_T2(n)))
    ser=sp.series(J.subs(t,-sp.exp(h)),h,0,4).removeO()
    a2=sp.Rational(n*n-1,8)
    print('T(2,%d)'%n,'a2=',a2,' J3(-e^h)=',sp.expand(ser),'  coeff h^2/(-24 a2)=',sp.simplify(ser.coeff(h,2)/(-24*a2)))
    # divisibility of J3-1 by (t^2-1)(t^4-1)
    num=sp.numer(sp.together(J-1)); print('   (J3-1) divisible by (t^2-1)(t^4-1):', sp.rem(sp.expand(num), sp.expand((t**2-1)*(t**4-1)), t)==0)
