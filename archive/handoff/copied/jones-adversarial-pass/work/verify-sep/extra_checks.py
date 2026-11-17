import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
def is_scalar(M):
    d = M[0][0]
    return all((M[i][j] == (d if i == j else {})) for i in range(DIM) for j in range(DIM)), d
sphere = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
full = [1, 2, 3, 4, 5] * 6
print("sphere relation element scalar on W(6,0):", is_scalar(rho_mat(sphere)))
print("full twist Delta_6^2 scalar:", is_scalar(rho_mat(full)))
# trace identity: gamma = [tr(l_c l_c') - 2 l1 l3 - 3 l1^2]/(l3-l1)^2 ; report tr(l_c l_c') for i=2 pair
# l_c = l1 + (l3 - l1) P_c ; with P_c = v H(v,.)/H(v,v)
import json
o = json.load(open(__file__.rsplit('/', 1)[0] + '/run_sep_out.json'))
l1 = {4: -1, -4: -1}; l3 = {8: -1, -8: -1}
# tr(l_c l_c') = 5 l1^2 + 2 l1 (l3-l1) + (l3-l1)^2 gamma ; compute for gamma = 1/[3]^2 : (l3-l1)^2/[3]^2 must be a Laurent poly
d = ladd(l3, l1, -1)
d2 = lmul(d, d)
s3sq = lmul({4: 1, 0: 1, -4: 1}, {4: 1, 0: 1, -4: 1})
sh, a = to_poly(d2); sh2, b = to_poly(s3sq)
q = poly_exact_div(a, b)
ratio = {sh - sh2 + k: c for k, c in enumerate(q) if c}
tr = ladd(ladd(lscale(lmul(l1, l1), 5), lscale(lmul(l1, d), 2)), ratio)
print("tr_W(l_c l_c') for i=2 pair:", lstr(tr))
print("tr_W(l_c l_c) = l3^2+4 l1^2:", lstr(ladd(lmul(l3, l3), lscale(lmul(l1, l1), 4))))
