import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
conjs = {0: [], 1: [3], 7: [3, 3], 10: [2, -3]}
G = gen_mats(conjs)
for B in ([(0, 1), (1, 1), (7, 1), (1, -1), (0, -1), (10, 1)], [(0, 1), (1, 1), (7, -1), (1, -1), (0, -1), (10, 1)]):
    X = None; out = []
    for n in range(1, 9):
        for ke in B:
            X = G[ke] if X is None else mul(X, G[ke])
        out.append(Dnp(X))
    print('B =', B)
    print('  D(B^n), n=1..8:', out, ' increments:', [b - a for a, b in zip(out, out[1:])], ' TSI(B^n)=48n+16')
