# Extra checks for the verify-defence lens, using the independent tool arcs_indep.py.
#  (a) Lemma 2 of the note on planar data: Y = [Delta_3^4, A_34] is trivial at t=-1, so |M_{YX}(-1)| = |M_X(-1)|
#      and |M_{XY}(-1)| = |M_X(-1)| for pure X.
#  (b) the note's Phi0 as a y-word equals the note's sigma-word as a mapping class (exact Artin action),
#      and the free-reduction claims of note section 4 (only the first letter y2^-1 of Gamma_1 is used).
#  (c) the defence's "discriminating" observation: does Lemma 6.3's list also hold for products that FAIL the
#      word criterion?  (If yes, the 400-product test does not discriminate the criterion.)
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from arcs_indep import (red, inv, comm, push_word, automorphism, summary, W_GAMMA1, Y_S, is_identity,
                        fox_matrix_at, LEMMA63)

random.seed(5)
Ysig = comm([1, 2] * 6, [3, 3])
fails = tested = 0
for _ in range(40):
    X = push_word(red([random.choice([1, 2, 3, -1, -2, -3]) for _ in range(random.randint(1, 4))]))
    if not X:
        continue
    mx = abs(summary('X', X)[0]['M_at_minus1'])
    myx = abs(summary('YX', Ysig + X)[0]['M_at_minus1'])
    mxy = abs(summary('XY', X + Ysig)[0]['M_at_minus1'])
    tested += 1
    fails += (mx != myx) + (mx != mxy)
print(f"(a) Lemma 2 planar test with Y=[Delta3^4,A34]: {tested} random X, mismatches: {fails}")

# (b)
def A(i, j):
    up = list(range(j - 1, i, -1)); return up + [i, i] + inv(up)
phi0_sigma = comm([1, 2] * 6, comm(comm(A(1, 4), A(2, 4)), A(3, 4)))
g = {1: [3, -2], 2: [2, -1], 3: [1]}          # A14 = y3 y2^-1, A24 = y2 y1^-1, A34 = y1
def g2y(w):
    out = []
    for x in w:
        out += g[abs(x)] if x > 0 else inv(g[abs(x)])
    return red(out)
b_y = g2y(comm(comm([1], [2]), [3]))
phi0_y = red(comm([-3, -3], b_y))
same = automorphism(push_word(phi0_y)) == automorphism(phi0_sigma)
print(f"(b) Phi0 y-word (length {len(phi0_y)}) equals the note's sigma-word as a mapping class: {same}")
print("    rho(Phi0) = I at t=-1 (homological Burau):", is_identity(fox_matrix_at(phi0_sigma, 4, -1)),
      "; at t=2:", is_identity(fox_matrix_at(phi0_sigma, 4, 2)))
L = len(phi0_y)
m = L + 1
core = red([1] * m + phi0_y + [-1] * m)
Wi = inv(W_GAMMA1)
PhiP = Wi + core
print("    y1^m Phi0 y1^-m reduced begins with y1, ends with y1^-1:", core[0] == 1 and core[-1] == -1)
print("    Phi' = Gamma1^-1 y1^m Phi0 y1^-m is freely reduced:", red(PhiP) == PhiP)
print("    Gamma1 begins with y2^-1:", W_GAMMA1[0] == -2, "; Phi' ends with y1^-1:", PhiP[-1] == -1,
      "; juxtaposition Phi'.Gamma1 reduced:", red(PhiP + W_GAMMA1) == PhiP + W_GAMMA1)

# (c)
def lemma63_ok(braid):
    o, R = summary('c', braid)
    return o['bad63'] == 0, o['has3']
res = {'criterion holds': [0, 0], 'criterion fails (Phi ends in y2)': [0, 0]}
for _ in range(60):
    V = red([random.choice([1, 2, 3, -1, -2, -3]) for _ in range(random.randint(1, 4))])
    if not V:
        continue
    key = 'criterion fails (Phi ends in y2)' if V[-1] == 2 else 'criterion holds'
    ok, has3 = lemma63_ok(push_word(V + W_GAMMA1))
    res[key][0] += 1; res[key][1] += (not ok)
for _ in range(30):
    V = red([random.choice([1, 2, 3, -1, -2, -3]) for _ in range(random.randint(0, 3))] + [2])
    if not V or V[-1] != 2:
        continue
    ok, has3 = lemma63_ok(push_word(V + W_GAMMA1))
    res['criterion fails (Phi ends in y2)'][0] += 1; res['criterion fails (Phi ends in y2)'][1] += (not ok)
print("(c) Lemma 6.3 list violations [tested, violating]:", res)
