# Referee: concrete instance of claim 10 at N = 3 using the identity J(swap K') = J_3(K'; 1/t) (checked in r6_swap.py)
# and multiplicativity of J_3 under connected sum. K' = RHT # LHT # 4_1 # 4_1 has a_2 = v_3 = 0 (C_4-trivial), K' nontrivial.
import sympy as sp, rlib
q=sp.symbols('q')
def habiro_J(N,c):
    tot=0
    for n in range(0,N):
        term=c(n)
        for k in range(1,n+1):
            term*=(q**sp.Rational(N+k,2)-q**sp.Rational(-(N+k),2))*(q**sp.Rational(N-k,2)-q**sp.Rational(-(N-k),2))
        tot+=term
    P=sp.Poly(sp.expand(tot*q**60),q)
    return {m[0]-60:int(cf) for m,cf in zip(P.monoms(),P.coeffs())}
J3={'4_1':habiro_J(3,lambda n:1),'RHT':habiro_J(3,lambda n:(-1)**n*q**sp.Rational(n*(n+3),2)),
    'LHT':habiro_J(3,lambda n:(-1)**n*q**sp.Rational(-n*(n+3),2))}
inv=lambda p:{-e:c for e,c in p.items()}
Jsw={k:inv(v) for k,v in J3.items()}       # J of the swap sum, J-variable
for k,v in Jsw.items(): print(k,'swap-J moments M0..M4:',[rlib.mom(v,i) for i in range(5)])
Kp=rlib.pmul(rlib.pmul(Jsw['RHT'],Jsw['LHT']),rlib.pmul(Jsw['4_1'],Jsw['4_1']))
print("K' = RHT#LHT#4_1#4_1 (a2 = 1+1-1-1 = 0, v3 = 1-1+0+0 = 0): swap-J moments M0..M5:",[rlib.mom(Kp,i) for i in range(6)],' J==1?',Kp=={0:1})
