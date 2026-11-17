import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
def Aij(i, j):  # pure braid generator, 1<=i<j<=6
    w = list(range(j - 1, i, -1))
    return w + [i, i] + [-g for g in reversed(w)]
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
ell0 = zeta8_line([])
cands = []
while len(cands) < 6:
    k = random.randint(1, 3)
    phi = []
    for _ in range(k):
        i = random.randint(1, 5); j = random.randint(i + 1, 6)
        g = Aij(i, j)
        if random.random() < 0.5: g = inv_word(g)
        phi += g
    if same_line(zeta8_line(phi), ell0): continue      # same splitting -> skip
    cands.append(phi)
for phi in cands:
    print('phi =', phi, ' partition', partition(phi), ' spanN(c,c\')=', Npair([], phi),
          ' spanN(c\',x)=', Npair(phi, [3]), ' spanN(c\',y)=', Npair(phi, [4, 3, 2, 3]))
sel = cands[:int(sys.argv[2]) if len(sys.argv) > 2 else 3]
for phi in sel:
    conjs = {'c': [], 'd': phi, 'x': [3]}
    G = gen_mats(conjs)
    print('system {c, c\'=phi(c) [same partition, new splitting], x}: D(R_d)=%d' % Dnp(G[('d', 1)]))
    enumerate_letters(G, 'cdx', 5)
