import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
vc = [{2: 1, -2: 1}, {0: 1}, {0: 1}, {2: 1, -2: 1}, {4: 1, 0: 1, -4: 1}]
g = {'c': [], 'x': [3], 'y': [4, 3, 2, 3]}
v = {k: rho_vec(w, vc) for k, w in g.items()}
t34 = lmul({4: 1, 0: 1, -4: 1}, {6: 1, 2: 1, -2: 1, -6: 1})   # [3][4]
for a, b in (('c', 'x'), ('c', 'y'), ('x', 'y')):
    h = Hform(v[a], v[b]); s = max(h) - min(h)
    print(a, b, 'span H =', s, ' span N =', s - 20, ' H =', lstr(h))
# cyclic invariant H(c,x)H(x,y)H(y,c): normalization-free up to units
cyc_ = lmul(lmul(Hform(v['c'], v['x']), Hform(v['x'], v['y'])), Hform(v['y'], v['c']))
print('cyclic H(c,x)H(x,y)H(y,c) span =', max(cyc_) - min(cyc_), ' =', fstr(factor_cyclo(cyc_)))
