import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import sympy as sp
from gtable import tosp
F,K,Dc=pickle.load(open('Kfreq_Sneck.pkl','rb'))
t=sp.symbols('t')
idx={f:k for k,f in enumerate(F)}
def Kx(f,i,j): return tosp(K[i][j][idx[f]]) if K[i][j][idx[f]] else 0
print('K_3^{31} =',sp.factor(Kx(3,1,0)))
print('K_2^{33} =',sp.factor(Kx(2,1,1)),'   K_2^{31} =',sp.factor(Kx(2,1,0)))
print('K_1^{11} =',sp.factor(Kx(1,0,0)),'   K_1^{31} =',sp.factor(Kx(1,1,0)))
print('K_0^{13} =',sp.factor(Kx(0,0,1)),'   K_0^{11}=',sp.factor(Kx(0,0,0)),'  K_0^{33}=',sp.factor(Kx(0,1,1)))
print('edge e1 pole  q~ = -K3^31/K2^33 =',sp.factor(-Kx(3,1,0)/Kx(2,1,1)))
print('edge e2 pole  q  = -K0^13/K2^33 =',sp.factor(-Kx(0,0,1)/Kx(2,1,1)))
eps=-t/(1+t**2)
print('compare X-eigenslopes 1 and eps=-t/(1+t^2)')
