# Referee: swap sums (claim 9). Own Habiro-formula colour-2 coloured Jones J_3 (standard variable: J_2 = V, V(RHT)=t+t^3-t^4)
# for 4_1 (c_n = 1) and trefoils (c_n = (-1)^n q^{+-n(n+3)/2}); compare with lp.J of swap words found by search.
import itertools, random, sympy as sp
import rlib, lp
sys_path='/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/core'
import sys; sys.path.insert(0,sys_path)
q=sp.symbols('q')
def habiro_J(N,c):
    tot=0
    for n in range(0,N):
        term=c(n)
        for k in range(1,n+1):
            term*=(q**sp.Rational(N+k,2)-q**sp.Rational(-(N+k),2))*(q**sp.Rational(N-k,2)-q**sp.Rational(-(N-k),2))
        tot+=term
    P=sp.Poly(sp.expand(tot*q**40),q)
    return {m[0]-40:int(cf) for m,cf in zip(P.monoms(),P.coeffs())}
J3={'4_1':habiro_J(3,lambda n:1),'RHT':habiro_J(3,lambda n:(-1)**n*q**sp.Rational(n*(n+3),2)),
    'LHT':habiro_J(3,lambda n:(-1)**n*q**sp.Rational(-n*(n+3),2))}
V2={'4_1':habiro_J(2,lambda n:1),'RHT':habiro_J(2,lambda n:(-1)**n*q**sp.Rational(n*(n+3),2))}
print('check J_2: 4_1',sorted(V2['4_1'].items()),' RHT',sorted(V2['RHT'].items()))
for k,v in J3.items(): print('J_3',k,sorted(v.items()), ' value at -1:',sum(c*(-1)**(e%2) for e,c in v.items()),' deriv at -1:',rlib.deriv_at(v,1,-1))
Vt={'4_1':{-2:1,-1:-1,0:1,1:-1,2:1},'RHT':{1:1,3:1,4:-1},'LHT':{-1:1,-3:1,-4:-1}}
# search swap words (no axis letters) whose half-arc K' has V = target; K' built as the closed long knot (closing strand at position 0)
from c1_constituents import constituents
found={k:[] for k in Vt}
letters=['x1','y1','x2','y2','x3','y3']
rnd=random.Random(8)
tries=0
while any(len(v)<3 for v in found.values()) and tries<60000:
    tries+=1
    body=[rnd.choice(letters[:4] if rnd.random()<0.6 else letters) for _ in range(rnd.randint(3,8))]
    w='s.'+rnd.choice(['l1','r1','l2','r2'])+'.'+'.'.join(body)+'.'+rnd.choice(['u1','u2','u3'])
    J=lp.J(w)
    if J is None or J=={0:1}: continue
    Vi,Vo=constituents(w)
    for k,v in Vt.items():
        if Vo==v and len(found[k])<3 and w not in [x[0] for x in found[k]]:
            VK=rlib.VK(w)
            found[k].append((w,J,VK==rlib.pmul(v,v)))
for k,lst in found.items():
    for w,J,vsq in lst:
        Jinv={-e:c for e,c in J3[k].items()}
        print(k,w,' V_K=V_K\'^2:',vsq,' J==J_3(K\';t):',J==J3[k],' J==J_3(K\';1/t):',J==Jinv)
# the 10th-root statement in standard convention
import cmath
for k in ('RHT','LHT'):
    for m in (1,3,7,9):
        xi=cmath.exp(2j*cmath.pi*m/10)
        a=sum(c*xi**e for e,c in J3[k].items()); b=sum(c*xi**(2*e) for e,c in Vt[k].items())**2; bb=sum(c*xi**(-2*e) for e,c in Vt[k].items())**2
        print(k,'xi=e^(2pi i %d/10): J_3(xi)=V(xi^2)^2 ?'%m,abs(a-b)<1e-9,'   J_3(xi)=V(xi^-2)^2 ?',abs(a-bb)<1e-9)
