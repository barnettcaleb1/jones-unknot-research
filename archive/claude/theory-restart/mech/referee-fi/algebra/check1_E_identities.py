# Exact check of the E identities, generator relations, and specialization at zeta_8.
import sympy as sp
A = sp.symbols('A')
d = -A**2 - A**-2
def bar(X):
    return X.subs(A, 1/A)
def star(X):
    return bar(X).T
def Z(X):
    return X.applyfunc(lambda e: sp.simplify(sp.together(e)))
G = sp.Matrix([[d,1],[1,d]])
M = sp.Matrix([[A,0],[1/A,-A**-3]])
J = sp.Matrix([[0,1],[1,0]])
E = sp.Matrix([[d,1],[-1,-d]])
I2 = sp.eye(2)
zero = sp.zeros(2,2)
res = {}
res['M unitary'] = Z(star(M)*G*M - G) == zero
res['J unitary'] = Z(star(J)*G*J - G) == zero
res['bar(M)=M^-1'] = Z(bar(M) - M.inv()) == zero
res['J^2=I'] = J*J == I2
res['(A J M)^3=-I'] = Z((A*J*M)**3 + I2) == zero
res['detM=-A^-2'] = sp.simplify(M.det() + A**-2) == 0
res['E^2=(d^2-1)I'] = Z(E*E - (d**2-1)*I2) == zero
res['E*GE=(d^2-1)G'] = Z(star(E)*G*E - (d**2-1)*G) == zero
res['EJE^-1=-J'] = Z(E*J*E.inv() + J) == zero
res['EME^-1=-A^-2 J M^-1 J'] = Z(E*M*E.inv() + A**-2*J*M.inv()*J) == zero
res['E(JM)E^-1=A^-2 (JM)^-1'] = Z(E*J*M*E.inv() - A**-2*(J*M).inv()) == zero
res['GE=(d^2-1)diag(1,-1)'] = Z(G*E - (d**2-1)*sp.diag(1,-1)) == zero
res['detE=1-d^2'] = sp.simplify(E.det() - (1-d**2)) == 0
for k,v in res.items(): print(k, v)
# det E modulo squares
num = sp.factor(sp.together(E.det()))
print('det E factored:', num)
print('factor list of A^4*detE:', sp.factor_list(sp.expand(A**4*E.det())))
# is E proportional to I or J ?
print('E prop to I?', Z(E - E[0,0]*I2) == zero, ' E prop to J?', Z(E - E[0,1]*J) == zero)

# specialization at zeta_8
z = sp.exp(sp.I*sp.pi/4)
D = sp.diag(1, sp.I)
def spec(X):
    return (D.inv()*X.subs(A, z)*D).applyfunc(lambda e: sp.nsimplify(sp.simplify(sp.expand_complex(e))))
Ms = spec(M); Js = spec(J); Es = spec(E); Gs = G.subs(A,z).applyfunc(lambda e: sp.simplify(sp.expand_complex(e)))
print('D^-1 M D / A0 =', (Ms/z).applyfunc(lambda e: sp.simplify(sp.expand_complex(e))))
print('D^-1 J D / i  =', (Js/sp.I).applyfunc(sp.simplify))
print('D^-1 E D / i  =', (Es/sp.I).applyfunc(sp.simplify), ' det =', sp.simplify((Es/sp.I).det()))
print('G(zeta) =', Gs)
print('delta(zeta)=', sp.simplify(sp.expand_complex(d.subs(A,z))))
# induced automorphism at zeta in SL2(Z) terms: conjugation by X=[[0,1],[1,0]]
X = sp.Matrix([[0,1],[1,0]])
S0 = sp.Matrix([[0,1],[-1,0]]); T0 = sp.Matrix([[1,0],[-1,1]])
print('X S0 X^-1 =', X*S0*X.inv(), ' (=-S0:', X*S0*X.inv() == -S0, ')')
print('X T0 X^-1 =', X*T0*X.inv(), ' ;  S0 T0^-1 S0^-1 =', S0*T0.inv()*S0.inv())
# compare: E M E^-1 ~ J M^-1 J  specializes to  S0 T0^-1 S0^-1 projectively
# triangle specialization delta(A_n) = -2 sin(pi/n)
n = sp.symbols('n', positive=True)
An = sp.exp(sp.I*sp.pi/4 - sp.I*sp.pi/(2*n))
print('delta(A_n)+2 sin(pi/n) =', sp.simplify(sp.expand_complex(d.subs(A,An)) + 2*sp.sin(sp.pi/n)))
# eigenvalue ratio of M at A_n: -A^4 -> exp(-2 pi i/n)
print('-A_n^4 / exp(-2 pi i /n) =', sp.simplify(-An**4/sp.exp(-2*sp.pi*sp.I/n)))
