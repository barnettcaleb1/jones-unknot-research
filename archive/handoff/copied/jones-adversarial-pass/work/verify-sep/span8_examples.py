import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
vc = [{2: 1, -2: 1}, {0: 1}, {0: 1}, {2: 1, -2: 1}, {4: 1, 0: 1, -4: 1}]
nH = Hform(vc, vc)
M0 = 4  # index of (16)(25)(34)
for w in ([-4, -4, -3, 5, -3, -2, -1, -4, 2, -3], [1, 4, 3, -2, -4, -4, 5, 1, 4, 1, -3, -1, -3], [5, -4, -1, -3, 4, -4, 1, -2, 4, -3, 5], [3], [3, 3]):
    wv = rho_vec(w, vc)
    N = wv[M0]
    h = Hform(vc, wv)
    # check H(v_c, w) = -[3][4] * w_{m0} up to unit: compare h with N * [3][4]
    t34 = lmul({4: 1, 0: 1, -4: 1}, {6: 1, 2: 1, -2: 1, -6: 1})
    ratio_ok = (ladd(h, lmul(t34, N), 1) == {})   # h == -[3][4] N
    one_minus = ladd(lmul({4: 1, 0: 1, -4: 1}, {4: 1, 0: 1, -4: 1}), lmul(N, lbar(N)), -1)
    print(w, "\n   N = (rho(phi)v_c)_(16)(25)(34) =", lstr(N), " span", max(N) - min(N),
          "\n   H = -[3][4] N ?", ratio_ok, " lead*trail of N =", N[max(N)] * N[min(N)],
          "\n   [3]^2 - N Nbar =", lstr(one_minus))
