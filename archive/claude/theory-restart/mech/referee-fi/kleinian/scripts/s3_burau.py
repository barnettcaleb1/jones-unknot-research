# Identify the projective rational-tangle group <[M],[J]> with the projective reduced Burau image of B_3.
# Reduced Burau (Birman / Funar-Kohno / McMullen convention up to duality): s1 -> [[-t,1],[0,1]], s2 -> [[1,0],[t,-t]].
import sympy as sp
A, t = sp.symbols('A t')
M = sp.Matrix([[A,0],[1/A,-A**-3]]); J = sp.Matrix([[0,1],[1,0]])
N = J*M*J
simp = lambda X: X.applyfunc(sp.cancel)
# braid relation (linear, not only projective)
print('M N M - N M N =', simp(M*N*M - N*M*N))
B1 = sp.Matrix([[-t,1],[0,1]]); B2 = sp.Matrix([[1,0],[t,-t]])
assert simp(B1*B2*B1 - B2*B1*B2) == sp.zeros(2,2)
# eigenvalues: M ~ (A, -A^-3) = -A^-3 * (-A^4, 1); Burau s_i ~ (-t, 1).  So t = A^4 after rescaling by -A^-3.
for tval, name in ((A**4,'t=A^4'), (A**-4,'t=A^-4')):
    for (X1,X2,lab) in ((M,N,'s1->M,s2->JMJ'),(N,M,'s1->JMJ,s2->M')):
        for scal in (-A**-3, A):
            p = sp.symbols('p0:4'); P = sp.Matrix(2,2,p)
            eqs = list(P*X1 - scal*B1.subs(t,tval)*P) + list(P*X2 - scal*B2.subs(t,tval)*P)
            sol = sp.solve(eqs, p, dict=True)
            Ps = [P.subs(s) for s in sol]
            good = [simp(Q) for Q in Ps if sp.cancel(Q.det()) != 0]
            if good:
                print(name, lab, 'scalar', scal, ' intertwiner P =', good[0].subs({p[3]:1, p[2]:1, p[1]:1, p[0]:1}) if good[0].free_symbols - {A} else good[0])
# Conclusion printed by the run: projectively, [M] and [JMJ] are the reduced Burau generators at t = A^4 (or dual at A^-4).
# At A_n: t = A_n^4 = -exp(-2 pi i/n) = -q with q = exp(-2 pi i/n)  (Funar-Kohno beta_{-q}; McMullen A_2(-zeta_n)).
