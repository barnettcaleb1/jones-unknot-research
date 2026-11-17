import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
conjs = {'c': [], 'x': [3], 'y': [4, 3, 2, 3]}
for k, g in conjs.items(): print(k, partition(g))
for a in conjs:
    for b in conjs:
        if a < b: print('span N(%s,%s) =' % (a, b), Npair(conjs[a], conjs[b]))
G = gen_mats(conjs)
for k in conjs: print('D(R_%s) =' % k, Dnp(G[(k, 1)]), Dnp(G[(k, -1)]))
print('first-lemma triple, letter words:')
enumerate_letters(G, 'cxy', int(sys.argv[1]) if len(sys.argv) > 1 else 5)
