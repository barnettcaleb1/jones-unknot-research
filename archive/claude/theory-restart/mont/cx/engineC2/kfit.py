"""Frequency decomposition of the S-necklace form: Ghat(m) = sum_{f=-3..3} t^{f m} K_f (m even). Fit on m in {0,+-2,+-4,+-6},
verify on m = +-8, +-10, +-12.  Stored as Kc_f = Dc * K_f (Laurent polys) with a common denominator Dc."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import sympy as sp
from gtable import tosp, fromsp
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
t=sp.symbols('t')
fit_ms=[0,2,-2,4,-4,6,-6]; F=list(range(-3,4))
S=[[None,None],[None,None]]
for i in range(2):
    for j in range(2):
        xs=sp.symbols('x0:7')
        eqs=[sum(xs[k]*t**(F[k]*m) for k in range(7))-tosp(tab[m][i][j]) for m in fit_ms]
        sol=sp.solve(eqs,xs,dict=True)[0]
        S[i][j]=[sp.factor(sol[xs[k]]) for k in range(7)]
dens=[sp.fraction(sp.together(S[i][j][k]))[1] for i in range(2) for j in range(2) for k in range(7)]
Dc=sp.lcm_list([sp.Poly(d,t).as_expr() for d in dens])
Dc=sp.factor(Dc); print('common denominator',Dc)
K=[[[fromsp(sp.cancel(S[i][j][k]*Dc)) for k in range(7)] for j in range(2)] for i in range(2)]
ok=bad=0
for m in [8,-8,10,-10,12,-12]:
    for i in range(2):
        for j in range(2):
            pred=sp.expand(sum(tosp(K[i][j][k])*t**(F[k]*m) for k in range(7)))
            if sp.expand(pred-sp.expand(Dc*tosp(tab[m][i][j])))==0: ok+=1
            else: bad+=1
print('verification entries ok',ok,'bad',bad)
for k in range(7):
    print('f=%d'%F[k],[[ (min(K[i][j][k]),max(K[i][j][k])) if K[i][j][k] else 0 for j in range(2)] for i in range(2)])
pickle.dump((F,K,fromsp(sp.expand(Dc))),open('Kfreq_Sneck.pkl','wb'))
