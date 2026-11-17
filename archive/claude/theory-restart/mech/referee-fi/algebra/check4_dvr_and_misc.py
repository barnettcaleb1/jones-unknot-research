# (1) Outer tensor diag(1,-1): explicit universal symmetries for P=J and P=M (index-one sanity).
# (2) Modular-group facts used in the DVR step, in the D-gauge: centralizer of S0 in PSL2(Z) is {1,S0};
#     T'^N and S0 T'^N S0^-1 have distinct unique invariant lines.
# (3) bar preserves the prime (Phi_8); G, bare words, E invertible mod Phi_8.
# (4) Gauge form: D^* G0 D = i*Omega, so every real L is a similitude with multiplier det L (sign of multiplier = sign det L).
# (5) S -> bar(P)^-1 S Q under C -> P^T C Q.
import sympy as sp
A = sp.symbols('A'); d = -A**2 - A**-2
bar = lambda X: X.subs(A, 1/A)
simp = lambda X: X.applyfunc(lambda e: sp.simplify(sp.together(e)))
G = sp.Matrix([[d,1],[1,d]]); M = sp.Matrix([[A,0],[1/A,-A**-3]]); J = sp.Matrix([[0,1],[1,0]]); E = sp.Matrix([[d,1],[-1,-d]])
C = sp.diag(1,-1)
print('(1) J^T C J =', J.T*C*J, '(= -C);  M^T C (J M J) + A^-2 C =', simp(M.T*C*(J*M*J) + A**-2*C))
# general: Q = u S^-1 bar(P) S with S=E
for P,name in [(M,'M'),(J,'J'),(M*J*M,'MJM')]:
    Q = simp(E.inv()*bar(P)*E)
    print('    P=%s: E^-1 bar(P) E =' % name, Q, ' G-unitary:', simp(bar(Q).T*G*Q - G) == sp.zeros(2,2))
print('(2) centralizer of S0: g=[[a,b],[c,e]], g S0 = +-S0 g')
a,b,c,e = sp.symbols('a b c e')
g = sp.Matrix([[a,b],[c,e]]); S0 = sp.Matrix([[0,1],[-1,0]])
for sgn in (1,-1):
    sol = sp.solve(list(g*S0 - sgn*S0*g), [a,b,c,e], dict=True)
    print('    sign %+d:' % sgn, [ (g.subs(s), sp.factor(g.subs(s).det())) for s in sol])
N = sp.symbols('N', positive=True)
Tp = sp.Matrix([[1,0],[-N,1]]); U = simp(S0*Tp*S0.inv())
print('    T\'^N =', Tp, 'eigvecs', [v[2] for v in Tp.eigenvects()], '; S0 T\'^N S0^-1 =', U, 'eigvecs', [v[2] for v in U.eigenvects()])
print('(3) Phi_8(1/A)*A^4 - Phi_8(A) =', sp.expand((A**-4+1)*A**4 - (A**4+1)))
z = sp.exp(sp.I*sp.pi/4)
for X,name in [(G,'G'),(M,'M'),(J,'J'),(E,'E')]:
    print('    det %s at zeta_8 =' % name, sp.simplify(sp.expand_complex(X.det().subs(A,z))))
print('(4) D^* G0 D =', sp.diag(1,-sp.I)*sp.Matrix([[0,1],[1,0]])*sp.diag(1,sp.I))
P_ = M*J*M; Q_ = J*M
Cc = sp.Matrix(2,2,sp.symbols('c1:5'))
S = G.inv()*Cc
print('(5) G^-1 P^T C Q - bar(P)^-1 S Q =', simp(G.inv()*P_.T*Cc*Q_ - bar(P_).inv()*S*Q_))
