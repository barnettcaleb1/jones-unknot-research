# Exact identities for the generic group and E, and the modular specialization.
import sympy as sp
A = sp.symbols('A')
bar = lambda X: X.subs(A, 1/A) if not isinstance(X, sp.MatrixBase) else X.applyfunc(lambda e: e.subs(A, 1/A))
star = lambda X: bar(X).T
simp = lambda X: X.applyfunc(sp.cancel)
d = -A**2 - A**-2
G = sp.Matrix([[d,1],[1,d]])
M = sp.Matrix([[A,0],[1/A,-A**-3]])
J = sp.Matrix([[0,1],[1,0]])
E = sp.Matrix([[d,1],[-1,-d]])
I2 = sp.eye(2)
Z = sp.zeros(2,2)
chk = {}
chk['M*GM=G'] = simp(star(M)*G*M - G) == Z
chk['J*GJ=G'] = simp(star(J)*G*J - G) == Z
chk['(AJM)^3=-I'] = simp((A*J*M)**3 + I2) == Z
chk['E^2=(d^2-1)I'] = simp(E*E - (d**2-1)*I2) == Z
chk['E*GE=(d^2-1)G'] = simp(star(E)*G*E - (d**2-1)*G) == Z
chk['EJE^-1=-J'] = simp(E*J*E.inv() + J) == Z
chk['EME^-1=-A^-2 J M^-1 J'] = simp(E*M*E.inv() + A**-2*J*M.inv()*J) == Z
chk['E(JM)E^-1 = A^-2 (JM)^-1'] = simp(E*J*M*E.inv() - A**-2*(J*M).inv()) == Z
chk['detM=-A^-2'] = sp.cancel(M.det() + A**-2) == 0
chk['detE=1-d^2'] = sp.cancel(E.det() - (1-d**2)) == 0
# eigenvalues of M: A and -A^-3, ratio -A^4
chk['M eig ratio'] = sp.cancel((A)/(-A**-3) + A**4) == 0
# modular point
A0 = sp.exp(sp.I*sp.pi/4)
D = sp.diag(1, sp.I)
sub0 = lambda X: X.applyfunc(lambda e: sp.simplify(e.subs(A, A0)))
M0 = sub0(M); J0 = J; E0 = sub0(E); G0 = sub0(G)
chk['D^-1 M0 D = A0 [[1,0],[-1,1]]'] = (D.inv()*M0*D - A0*sp.Matrix([[1,0],[-1,1]])).applyfunc(sp.simplify) == Z
chk['D^-1 J D = i[[0,1],[-1,0]]'] = (D.inv()*J0*D - sp.I*sp.Matrix([[0,1],[-1,0]])).applyfunc(sp.simplify) == Z
print('E0 =', E0, ' G0 =', G0, ' D^-1 E0 D =', (D.inv()*E0*D).applyfunc(sp.simplify))
print('delta(A0) =', sp.simplify(d.subs(A, A0)), ' delta^2-1 at A0 =', sp.simplify((d**2-1).subs(A,A0)))
# A_n : delta = -2 sin(pi/n), A_n^4 = -exp(-2 pi i/n)
n = sp.symbols('n', positive=True)
An = sp.exp(sp.I*sp.pi/4 - sp.I*sp.pi/(2*n))
chk['delta(A_n) = -2 sin(pi/n)'] = sp.simplify(sp.expand(d.subs(A, An).rewrite(sp.cos), complex=True) + 2*sp.sin(sp.pi/n)) == 0
chk['-A_n^4 = exp(-2 pi i/n)'] = sp.simplify(-An**4 - sp.exp(-2*sp.I*sp.pi/n)) == 0
for k,v in chk.items(): print(('OK   ' if v else 'FAIL ')+k)
assert all(chk.values())
