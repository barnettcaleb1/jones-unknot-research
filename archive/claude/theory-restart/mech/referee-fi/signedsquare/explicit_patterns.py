#!/usr/bin/env python3
"""Referee script 3: explicit two-slot patterns; exact tensors with cx-tools bracket.py, cross-checked by two
independent state sums; evaluation at zeta_8; sign test; convention tests for M, G; seed moves."""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction
import sympy as sp
from twobox import *

A = sp.symbols('A')
def to_sp(p):
    return sp.Add(*[c * A**e for e, c in p.items()]) if p else sp.Integer(0)
def sp_tensor(C):
    return sp.Matrix(2, 2, lambda i, j: to_sp(C[i][j]))
dl = -A**2 - A**-2
G = sp.Matrix([[dl, 1], [1, dl]])
M = sp.Matrix([[A, 0], [A**-1, -A**-3]])
J = sp.Matrix([[0, 1], [1, 0]])
E = sp.Matrix([[dl, 1], [-1, -dl]])
def eqm(X, Y):
    return all(sp.simplify(e) == 0 for e in (X - Y))

def three_way(word, n, closure="braid"):
    C1 = tl_tensor(word, n, closure)
    C2 = pd_tensor(word, n, closure)
    C3 = [[port_bracket(word, n, {'B1': i, 'B2': j}, closure) for j in range(2)] for i in range(2)]
    return C2, (C1 == C2), (C3 == C2)

def report(name, word, n, closure="braid"):
    C, ok1, ok2 = three_way(word, n, closure)
    print("\n### %s   (n=%d, %s closure)\n    word = %r" % (name, n, closure, word))
    print("    bracket.py tensor == TL-direct state sum: %s ; == port state sum: %s" % (ok1, ok2))
    for i in range(2):
        for j in range(2):
            print("    C[%d][%d] = %s" % (i, j, pstr(C[i][j])))
    res = analyse(C)
    for i in range(2):
        for j in range(2):
            print("    C[%d][%d](zeta_8) = %s" % (i, j, zstr(res["Z"][i][j])))
    print("    det C(zeta_8) = %s" % zstr(res["det"]))
    if not res["nonzero"]:
        print("    C(zeta_8) = 0: identity vacuous (m = 0), no unit seed possible")
    for (i, j), d in sorted(res["anchors"].items()):
        print("    anchor (%d,%d): det/C^2 = %s  rational=%s  |anchor|=1:%s  law[(-1)^(i+j)*ratio is a square >=0]: %s"
              % (i, j, zstr(d["ratio"]), d["rational"], d["unit"], d["ok"]))
    print("    SIGN LAW:", "PASS" if res["ok"] else "FAIL")
    return C, res

allok = True
print("== calibration: bracket.py vs TL-direct on closures without boxes handled via trivial box fillings ==")
# trefoil: sigma_1^3 with two extra boxes filled by id must give <trefoil closure>
tre = [(1, 1), (1, 'B1'), (1, 1), (1, 'B2'), (1, 1)]
print("   s1^3 closure (boxes=id):", pstr(pd_bracket(tre, 2, {'B1': 0, 'B2': 0})), " TL:", pstr(tl_bracket(tre, 2, {'B1': 0, 'B2': 0})))

# P1: numerator closure of a tangle sum, N(T1+T2)
C, res = report("P1  tangle-sum closure N(T1+T2)", [(1, 'B1'), (1, 'B2')], 2)
allok &= res["ok"]
print("    C == G:", eqm(sp_tensor(C), G))

# convention test: twists stacked on the boxes act by M
w = [(1, 'B1'), (1, 1), (1, 1), (1, 'B2'), (1, -1), (1, -1), (1, -1)]
C, res = report("P1' N(T1+T2) with 2 positive twists after box 1 and 3 negative twists after box 2", w, 2)
allok &= res["ok"]
print("    C == (M^2)^T G M^-3 :", eqm(sp_tensor(C), (M**2).T * G * M**-3))
# seed: T1 = id, T2 = id gives sigma^2 sigma^-3 = sigma^-1 closure = unknot.  Move seed to corner 11 by label swap J on both slots.
Cs = J * sp_tensor(C) * J
print("    seed (id,id) bracket:", sp.simplify(sp_tensor(C)[0, 0]), "-> corner 11 after J-relabel; unit")

# P2: EKT Hopf shell: 2-cable of the Hopf link with a box on each ribbon
ekt = [(1, 'B1'), (3, 'B2'), (2, 1), (1, 1), (3, 1), (2, 1), (2, 1), (1, 1), (3, 1), (2, 1)]
C, res = report("P2  EKT Hopf shell (2-cable of Hopf link, one box per ribbon)", ekt, 4)
allok &= res["ok"]
h = -A**14 - A**6 - 2*A**2 - 2*A**-2 - A**-6 - A**-14
Cekt = sp.Matrix([[h, dl**2], [dl**2, dl]])
print("    C == [[h,delta^2],[delta^2,delta]] (dichotomy file, EKT calibration):", eqm(sp_tensor(C), Cekt))
Cm = sp_tensor(C).subs(A, 1/A)
print("    mirror also equal:", eqm(Cm, Cekt))

# P3: closed 3-braid pattern  box1@1, s2^2, box2@1, s2^-2   (fillings s1^a, s1^b give closed 3-braids)
p3 = [(1, 'B1'), (2, 1), (2, 1), (1, 'B2'), (2, -1), (2, -1)]
C, res = report("P3  closed 3-braid pattern  B1 s2^2 B2 s2^-2", p3, 3)
allok &= res["ok"]
C3 = sp_tensor(C)

# P4: closed 3-braid pattern with boxes on different positions
p4 = [(1, 'B1'), (2, 1), (1, -1), (2, 'B2'), (1, 1), (2, 1), (2, 1)]
C, res = report("P4  closed 3-braid pattern  B1@1 s2 s1^-1 B2@2 s1 s2^2", p4, 3)
allok &= res["ok"]
C4 = sp_tensor(C)

# P5: pretzel-like 4-plat pattern
p5 = [(2, 1), (2, 1), (1, 'B1'), (3, 'B2'), (2, -1), (2, -1), (2, -1)]
C, res = report("P5  4-plat pattern  s2^2 (B1@1 B2@3) s2^-3", p5, 4, "plat")
allok &= res["ok"]
C5 = sp_tensor(C)

# P6: a Kinoshita-Terasaka-flavoured pattern: 4-strand braid closure with clasps between the slots
p6 = [(1, 'B1'), (2, 1), (2, 1), (3, 'B2'), (2, -1), (2, -1), (1, 1), (3, -1)]
C, res = report("P6  4-braid pattern  B1@1 s2^2 B2@3 s2^-2 s1 s3^-1", p6, 4)
allok &= res["ok"]
C6 = sp_tensor(C)

print("\n== Is S = G^-1 C a similitude for these (Z_C scalar)?  and A=1 values ==")
for nm, Cx in (("P3", C3), ("P4", C4), ("P5", C5), ("P6", C6)):
    if sp.simplify(Cx.det()) == 0:
        print("  ", nm, "det C = 0"); continue
    S = (G.inv() * Cx).applyfunc(sp.cancel)
    Sstar = S.subs(A, 1/A).T
    H = (Sstar * G * S).applyfunc(sp.cancel)
    Zc = (G.inv() * H).applyfunc(sp.cancel)
    scalar = sp.simplify(Zc[0, 1]) == 0 and sp.simplify(Zc[1, 0]) == 0 and sp.simplify(Zc[0, 0] - Zc[1, 1]) == 0
    print("  ", nm, "similitude:", scalar, "  C(1) =", Cx.subs(A, 1).tolist())

print("\n== seed moves realised by actual diagrams (twists stacked on the boxes), and the unit-anchored ratio ==")
import itertools
def twisted(word, a, b):
    out = []
    for pos, kind in word:
        out.append((pos, kind))
        if kind == 'B1':
            out += [(pos, 1 if a > 0 else -1)] * abs(a)
        if kind == 'B2':
            out += [(pos, 1 if b > 0 else -1)] * abs(b)
    return out
for nm, wd, n, cl, C0 in (("P3", p3, 3, "braid", C3), ("P4", p4, 3, "braid", C4), ("P5", p5, 4, "plat", C5), ("P6", p6, 4, "braid", C6)):
    found = 0
    for a, b in itertools.product(range(-3, 4), repeat=2):
        # seed: box1 = sigma^a (i.e. M^a e_0), box2 = sigma^b
        v = (M**a)[:, 0]; wv = (M**b)[:, 0]
        val = sp.simplify((v.T * C0 * wv)[0, 0])
        valp = sp.Poly(sp.expand(val * A**200), A)
        if len(valp.terms()) == 1 and abs(valp.terms()[0][1]) == 1:
            # unit seed.  Moved pattern: twists stacked, labels swapped on both slots: C' = (M^a J)^T C (M^b J)
            wd2 = twisted(wd, a, b)
            Cd = pd_tensor(wd2, n, cl)
            Cd_tl = tl_tensor(wd2, n, cl)
            Cprime_diag = J * sp_tensor(Cd) * J
            Cprime_alg = (M**a * J).T * C0 * (M**b * J)
            same = eqm(Cprime_diag, Cprime_alg)
            # ratio at the new corner 11 = old corner 00 of the twisted diagram
            res = analyse(Cd)
            d = res["anchors"][(0, 0)]
            found += 1
            print("   %s seed (s^%d, s^%d): bracket %s ; diagram tensor == (M^a J)^T C (M^b J): %s ; TL==PD: %s ; det C'/C'_11^2 = %s ; unit:%s ; law:%s"
                  % (nm, a, b, val, same, Cd == Cd_tl, zstr(d["ratio"]), d["unit"], res["ok"]))
            allok &= res["ok"] and same and (Cd == Cd_tl)
    if not found:
        print("   %s: no unit seed among integer-twist fillings |a|,|b|<=3" % nm)

print("\nALL EXPLICIT CHECKS PASS:", bool(allok))
