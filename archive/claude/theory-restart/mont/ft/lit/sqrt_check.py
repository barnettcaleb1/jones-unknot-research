# LIT-lane curiosity check: compare J(K,h) products with the colour-2 Jones J3(K) (both normalised, variable t = A^-4).
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/lit')
import lp, sympy as sp
t,h=sp.symbols('t h')
def tosym(p): return sum(c*t**e for e,c in p.items())
def J3_T2(n):
    qint=lambda m: sum(t**sp.Rational(-k,2) for k in range(-(m-1),m,2))
    lam={0:t**2,2:-t,4:t**-1}; D={c:qint(c+1) for c in (0,2,4)}
    return sp.simplify(sum(D[c]*lam[c]**n for c in (0,2,4))/(t**-2)**n/D[2])
for w in ['s.y0.y0.y0','s.x0.x0.x0']:
    Jw=lp.J(w); print(w,'J =',Jw)
    if Jw:
        Js=tosym(Jw)
        for n in (3,-3):
            print('   J^2 - J3(T(2,%d)) ='%n, sp.factor(sp.expand(Js**2-J3_T2(n))))
# figure-eight: two inversions, J3(4_1) from Habiro: 1 + {4}{2}(1+{5}{1}), q=t
q=t
J341=sp.expand(1+(q**2-q**-2)*(q-q**-1)*(1+q**3-q**2-q**-2+q**-3))
J1=lp.J('s.l1.y0.y0.x1.u2'); J2=lp.J('s.l1.x0.x0.y1.u2'); print('fig8 J1',J1,' J2',J2)
print('   J1*J2 - J3(4_1) =', sp.factor(sp.expand(tosym(J1)*tosym(J2)-J341)))
print('   series J1(-e^h)=',sp.series(tosym(J1).subs(t,-sp.exp(h)),h,0,4))
print('   series J3(4_1)(-e^h)=',sp.series(J341.subs(t,-sp.exp(h)),h,0,4))
