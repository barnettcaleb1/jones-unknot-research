import cmath
# Laurent polys as dict exp->coef
def ev(p,z): return sum(c*z**e for e,c in p.items())
def mul(p,q):
    r={}
    for a,x in p.items():
        for b,y in q.items(): r[a+b]=r.get(a+b,0)+x*y
    return {e:c for e,c in r.items() if c}
def add(p,q):
    r=dict(p)
    for e,c in q.items(): r[e]=r.get(e,0)+c
    return {e:c for e,c in r.items() if c}
T4m1={4:1,0:-1}
ex={ # name: (J_pref, k, P)
 'trefoil':({-7:1,-4:1,-3:-1},-4,{-7:-1}),
 '4_1':({-6:1,-3:1,-2:-1,0:1,1:-1},0,{-6:-1,-3:-1}),
 'l_bXXYa':(mul({-8:1},{-3:1,-2:-1,0:1,1:-1,2:1}),-8,{-10:1,-11:-1}),
}
z6=cmath.exp(1j*cmath.pi/3); om=cmath.exp(2j*cmath.pi/3)
for n,(J,k,P) in ex.items():
    rec=add({k:1},mul(T4m1,P))
    ok=(rec==J)
    vals=[abs(ev(J,z)-1)<1e-12 for z in (1,-1,1j,z6,z6.conjugate())]
    # (t+1)^2 | J-1 : derivative at -1
    d=sum(c*e*(-1)**(e-1) for e,c in J.items())
    pred={0:0,1:-1,2:om}[(k//4)%3]
    print(n,'decomp',ok,'J(1,-1,i,z6,z6b)=1',vals,'J\'(-1)',round(d,9),'P(-1)',ev(P,-1),'-k/4',-k/4,'P(z6)',complex(round(ev(P,z6).real,9),round(ev(P,z6).imag,9)),'pred',complex(round(pred.real,9),round(pred.imag,9)) if isinstance(pred,complex) else pred)
# Phi10 check trefoil: J(t) - V_RH(t^2) divisible by Phi10 : evaluate at primitive 10th roots
VRH={1:1,3:1,4:-1}
J=ex['trefoil'][0]
for kk in (1,3,7,9):
    z=cmath.exp(2j*cmath.pi*kk/10)
    print('Phi10 root',kk, abs(ev(J,z)-ev(VRH,z**2))<1e-12, abs(ev(J,z)-ev(VRH,z**-2))<1e-12)
