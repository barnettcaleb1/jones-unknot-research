#!/usr/bin/env python3
"""Referee script 1 (lens SIGNED SQUARE): exact algebra with sympy.
 (a) E identities, G-unitarity, D-gauge at zeta_8.
 (b) normal form of inner/outer coset tensors at zeta_8 and the ratio det C / C_ij^2 for every nonzero anchor.
 (c) coset preservation under seed moves: S' = bar(P)^-1 S Q.
 (d) A = 1 specialisation: every W in Gamma has a zero entry; consequence for the outer coset.
 (e) EKT tensor identity h = delta^3(delta^2-3)^2 - delta(delta^2-2)(delta^2-4); C(zeta_8) = 0.
"""
import random, itertools
import sympy as sp

A = sp.symbols('A')
d = -A**2 - A**-2
G = sp.Matrix([[d, 1], [1, d]])
M = sp.Matrix([[A, 0], [A**-1, -A**-3]])
J = sp.Matrix([[0, 1], [1, 0]])
E = sp.Matrix([[d, 1], [-1, -d]])
I2 = sp.eye(2)

def bar(X):
    return X.subs(A, 1/A)
def star(X):
    return bar(X).T
def simp(X):
    return X.applyfunc(lambda e: sp.factor(sp.together(e)))
def iszero(X):
    return all(sp.simplify(e) == 0 for e in X)

print("== (a) identities ==")
print("M* G M = G        :", iszero(star(M)*G*M - G))
print("J* G J = G        :", iszero(star(J)*G*J - G))
print("E^2=(d^2-1)I      :", iszero(E*E - (d**2-1)*I2))
print("E* G E=(d^2-1)G   :", iszero(star(E)*G*E - (d**2-1)*G))
print("E J E^-1 = -J     :", iszero(E*J*E.inv() + J))
print("E M E^-1 = -A^-2 J M^-1 J :", iszero(E*M*E.inv() + A**-2*J*M.inv()*J))
print("G E = (d^2-1) diag(1,-1)  :", iszero(G*E - (d**2-1)*sp.diag(1, -1)))
print("bar(M)=M^-1, bar(E)=E     :", iszero(bar(M)-M.inv()), iszero(bar(E)-E))
print("(A J M)^3 = -I            :", iszero((A*J*M)**3 + I2))

z = sp.exp(sp.I*sp.pi/4)
def at_z(X):
    return X.subs(A, z).applyfunc(lambda e: sp.nsimplify(sp.simplify(sp.expand_complex(e))))
D = sp.diag(1, sp.I)
def gauge(X):
    return (D.inv()*at_z(X)*D).applyfunc(lambda e: sp.simplify(sp.expand_complex(e)))
print("D^-1 M D / zeta =", (gauge(M)/z).applyfunc(lambda e: sp.nsimplify(sp.simplify(sp.expand_complex(e)))))
print("D^-1 J D / i    =", (gauge(J)/sp.I).applyfunc(sp.simplify))
print("D^-1 E D / i    =", (gauge(E)/sp.I).applyfunc(sp.simplify))
print("G(zeta)         =", at_z(G))

print("\n== (b) ratio det C / C_ij^2 at zeta_8, random words ==")
random.seed(20261115)
gens = {'M': M, 'm': M.inv(), 'J': J}
def word_matrix(w):
    X = I2
    for c in w:
        X = X*gens[c]
    return X.applyfunc(sp.expand)
def rand_word(L):
    return ''.join(random.choice('MmJ') for _ in range(L))

def ratios(C0):
    """C0: numeric exact 2x2 at zeta. returns dict anchor->ratio"""
    det = sp.simplify(sp.expand_complex(C0.det()))
    out = {}
    for i in range(2):
        for j in range(2):
            c = sp.simplify(sp.expand_complex(C0[i, j]))
            if c != 0:
                out[(i, j)] = sp.nsimplify(sp.simplify(sp.expand_complex(det/c**2)))
    return out

bad = 0
ntest = 0
for trial in range(60):
    w = rand_word(random.randint(0, 9))
    W = word_matrix(w)
    for coset, X in (("inner", G*W), ("outer", G*E*W)):
        C0 = at_z(X)
        r = ratios(C0)
        for (i, j), val in r.items():
            ntest += 1
            want = (-1)**(i+j) * (1 if coset == "inner" else -1)
            ok = val.is_rational and sp.sign(val) == want and sp.sqrt(abs(val)).is_rational
            if not ok:
                bad += 1
                print("UNEXPECTED", coset, w, (i, j), val)
print("tests:", ntest, "violations of [sign = (-1)^(i+j) inner, -(-1)^(i+j) outer; |ratio| rational square]:", bad)

# explicit symbolic normal form: outer coset C = v G D L D^-1 with L real, det L = -1
a_, b_, c_, d_, v_ = sp.symbols('a b c d v')
L = sp.Matrix([[a_, b_], [c_, d_]])
Cn = v_*at_z(G)*D*L*D.inv()
Cn = Cn.applyfunc(sp.simplify)
print("C(zeta) for S(zeta)=v D L D^-1:", Cn)
print("det C =", sp.factor(Cn.det()), " C_22^2 =", sp.factor(Cn[1, 1]**2), " C_11^2 =", sp.factor(Cn[0, 0]**2),
      " C_12^2 =", sp.factor(Cn[0, 1]**2), " C_21^2 =", sp.factor(Cn[1, 0]**2))
detL = a_*d_ - b_*c_
for name, ent, sgn in (("lower-right (corner 11 in 0/1 labels)", Cn[1, 1], 1), ("upper-left (corner 00)", Cn[0, 0], 1),
                       ("upper-right (corner 01)", Cn[0, 1], -1), ("lower-left (corner 10)", Cn[1, 0], -1)):
    print("  ratio det/C^2 at", name, "=", sp.simplify(Cn.det()/ent**2), "   [= det(L)/x^2 on the diagonal, -det(L)/x^2 off the diagonal]")

print("\n== (c) seed move: C' = P^T C Q  =>  S' = bar(P)^-1 S Q ==")
ok = True
for trial in range(8):
    P = word_matrix(rand_word(random.randint(1, 5)))
    Q = word_matrix(rand_word(random.randint(1, 5)))
    # check G^-1 P^T G = bar(P)^-1
    ok = ok and iszero(G.inv()*P.T*G - bar(P).inv())
print("G^-1 P^T G = bar(P)^-1 for random P in Gamma:", ok)
# E normalises Gamma => Gamma E Gamma = E Gamma: bar(P)^-1 (E W) Q = E (E^-1 bar(P)^-1 E) W Q with E^-1 Gamma E = Gamma projectively.
print("E^-1 J E prop J:", iszero(E.inv()*J*E + J), "  E^-1 M E prop J M^-1 J:", iszero(E.inv()*M*E + A**-2*J*M.inv()*J))

print("\n== (d) A = 1: the image of Gamma and the outer coset ==")
M1, J1, E1, G1 = (X.subs(A, 1) for X in (M, J, E, G))
grp = {tuple(I2)}
frontier = [I2]
while frontier:
    X = frontier.pop()
    for g in (M1, J1):
        Y = X*g
        if tuple(Y) not in grp:
            grp.add(tuple(Y)); frontier.append(Y)
print("order of <M(1),J(1)> :", len(grp))
print("every element has a zero entry:", all(0 in t for t in grp))
print("G(1)E(1) =", G1*E1, " so outer-coset tensors at A=1 are scalar*diag(1,-1)*W(1): always have a zero entry")
print("inner coset G(1)W(1) has NO zero entry for all W:", all(0 not in tuple(G1*sp.Matrix(2, 2, t)) for t in grp))
print("E(1) =", E1, " (no zero entry => [E] not in Gamma projectively)")

print("\n== (e) EKT tensor ==")
h = -A**14 - A**6 - 2*A**2 - 2*A**-2 - A**-6 - A**-14
print("h = d^3(d^2-3)^2 - d(d^2-2)(d^2-4):", sp.simplify(h - (d**3*(d**2-3)**2 - d*(d**2-2)*(d**2-4))) == 0)
print("h(zeta_8) =", sp.simplify(sp.expand_complex(h.subs(A, z))), " h/delta polynomial? ", sp.simplify(sp.cancel(h/d)))
