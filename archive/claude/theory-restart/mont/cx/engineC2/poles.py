import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,"/Users/calebbarnett/jones-lanes/theory-restart/mont"); sys.path.insert(0,"/Users/calebbarnett/jones-lanes/theory-restart/tools"); import lp
from lp import add, mul, sub, top, bot
import sympy as sp
t=sp.symbols('t')
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
def tosp(p): return sum(c*t**e for e,c in p.items())
for m in [2,4,6,-2,-4]:
    G=tab[m]
    det=sub(mul(G[0][0],G[1][1]),mul(G[0][1],G[1][0]))
    print('m',m,'det Ghat =',sp.factor(tosp(det)))
    # bottom pole of q: q ~ -G13/G33 at t->0 ; top pole: q ~ -G31/G33... print series at t->0
    pole=-tosp(G[0][1])/tosp(G[1][1])
    s=sp.series(pole,t,0,8).removeO()
    print('   -G13/G33 at t->0:',sp.expand(s))
    pole2=-tosp(G[1][0])/tosp(G[1][1])
    s2=sp.series(pole2.subs(t,1/t),t,0,8).removeO()   # top expansion in u=1/t
    print('   -G31/G33 at t->inf (in u=1/t):',sp.expand(s2))
