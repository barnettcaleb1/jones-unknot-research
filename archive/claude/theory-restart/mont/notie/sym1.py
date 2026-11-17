import sympy as sp
t,y,z,zp=sp.symbols('t y z zp')
Phi3=1+t+t**2; Phi6=t**2-t+1; al=(t-1)*(t**2+1); be=t*(t-1)
w1=t+(1+t**2)*y; w3=(1+t**2)*(1-y)
g=lambda m: w1*(al/Phi6)**m+(-1)**m*w3*(be/Phi6)**m
print('gamma0 =',sp.factor(g(0)))
print('gamma1 =',sp.factor(g(1)))
print('gamma2 =',sp.factor(g(2)))
print('gamma3 =',sp.factor(g(3)))
print('Phi3 - gamma2/t =',sp.factor(sp.simplify(Phi3-g(2)/t)))
print('Phi3 + (-t)^-1 * gamma1 / y   [degeneration] =',sp.factor(sp.simplify(Phi3+g(1)/(-t)/y)))
