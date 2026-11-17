import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
conjs = {'c': [], 'a': [1, 2, 3], 'b': [5, 4, 3]}
for k, g in conjs.items(): print(k, partition(g), 'zeta8 line equal to c?', same_line(zeta8_line(g), zeta8_line([])))
for a in conjs:
    for b in conjs:
        if a < b: print('span N(%s,%s) =' % (a, b), Npair(conjs[a], conjs[b]))
# cyclic product H(c,a)H(a,b)H(b,c)
v = {k: rho_vec(g, vc) for k, g in conjs.items()}
cyc_ = lmul(lmul(Hform(v['c'], v['a']), Hform(v['a'], v['b'])), Hform(v['b'], v['c']))
print('cyclic H(c,a)H(a,b)H(b,c) =', fstr(factor_cyclo(cyc_)), ' (each H carries -[3][4])')
G = gen_mats(conjs)
for k in conjs: print('D(R_%s) =' % k, Dnp(G[(k, 1)]))
print('round triple, letter words:')
enumerate_letters(G, 'cab', int(sys.argv[1]) if len(sys.argv) > 1 else 6)
