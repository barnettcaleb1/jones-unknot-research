# Remark 6(3): Penner example. Conventions of phi0_check.py (right Artin action, words applied left to right).
# x3 is the loop around p3 along beta*_3; z = x1 x2 is the loop around the disk containing alpha (fixed by s1).
import sys
sys.path.insert(0, sys.argv[1])
from lib import inv, red, artin, pure, trivial
n = 4
Eu = [3, 2, 2, -3]        # candidate twist about a curve around {p2,p4}
Ed = [-3, 2, 2, 3]        # the other candidate
img = lambda w: artin(w, n)
# The curve on the far side of p3 from p* is disjoint from beta*: its twist fixes x3 exactly.
for name, E in (("s3 s2^2 s3^-1", Eu), ("s3^-1 s2^2 s3", Ed)):
    print(f"twist {name}: fixes x3? {img(E)[3] == [3]}")
E_far = Eu if img(Eu)[3] == [3] else Ed
E_near = Ed if E_far is Eu else Eu
c1, c2 = [1, 1], [3, 3]   # twists about round curves around {p1,p2} and {p3,p4}
def to_z_basis(word):     # rewrite in free basis {x1, z=x1x2, x3, x4}: x2 = x1^-1 z, z encoded as 5
    out = []
    for a in word:
        if abs(a) == 2: out += [-1, 5] if a > 0 else [-5, 1]
        else: out.append(a)
    return red(out)
def report(label, Phi):
    w3 = img(Phi)[3]
    zb = to_z_basis(w3)
    fixed_by_s1sq = artin([1, 1], n, start={3: w3})[3] == w3
    print(f"{label}: pure {pure(Phi, n)}, nontrivial {not trivial(Phi, n)}; image of x3 has length {len(w3)};"
          f" in <x1x2,x3,x4>: {all(abs(a) != 1 for a in zb)}; fixed by s1^2: {fixed_by_s1sq}")
    return w3
w = report("Phi = Tc1 . Te^-1 . Tc2 (e on far side of p3)", c1 + inv(E_far) + c2)
print("   image of x3 =", w, "  ( = image of x3 under Tc2 alone:", w == img(c2)[3], ")")
report("control: e on the p*-side of p3     ", c1 + inv(E_near) + c2)
report("control: beta* crossing alpha (s2 s1^2 s2^-1 ... )", [2, 1, 1, -2])
# growth rate of word lengths under iteration vs Penner matrix PF root
Phi = c1 + inv(E_far) + c2
cur = {j: [j] for j in range(1, n + 1)}
lens = []
for k in range(1, 6):
    cur = artin(Phi, n, start=cur)
    lens.append(sum(len(v) for v in cur.values()))
print("total word lengths of Phi^k(x_i), k=1..5:", lens)
print("successive ratios:", [round(lens[i + 1] / lens[i], 4) for i in range(len(lens) - 1)])
# Penner matrices on weights (mu_c1, mu_c2, mu_e), i(c1,e)=i(c2,e)=2
import itertools
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
M1 = [[1, 0, 2], [0, 1, 0], [0, 0, 1]]
M2 = [[1, 0, 0], [0, 1, 2], [0, 0, 1]]
Me = [[1, 0, 0], [0, 1, 0], [2, 2, 1]]
M = mm(M2, mm(Me, M1))
v = [1.0, 1.0, 1.0]
for _ in range(200):
    v2 = [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]
    lam = max(v2); v = [x / lam for x in v2]
print("Penner matrix", M, " PF eigenvalue ~", round(lam, 6))
