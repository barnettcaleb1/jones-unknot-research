"""critic falsification test of the SWAP-SUM LEMMA: for an axis-free width-two word W (no x0/y0), the axis bounds a disc
disjoint from the arc, so K = K' # rK' (K' = closure of the arc along the axis, a 4-plat); then V_K = V(K')^2 must be a
PERFECT SQUARE.  Control: words with axis letters (expected: usually not squares)."""
import sys, random
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/code')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import replay, rho2
import sympy as sp
t = sp.symbols('t')
def is_square(V):
    e0 = min(V); P = sum(c * t**(e - e0) for e, c in V.items())
    if (max(V) - e0) % 2: return False
    f = sp.factor_list(sp.Poly(P, t))
    return all(m % 2 == 0 for _, m in f[1]) and f[0] in (1, -1) or (f[0] == 1 and all(m % 2 == 0 for _, m in f[1]))
rnd = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
for label, alpha in (('axis-free', ['x1', 'x2', 'x3', 'y1', 'y2', 'y3']), ('with-axis', ['x0', 'y0', 'x1', 'x2', 'x3', 'y1', 'y2', 'y3'])):
    sq = nsq = triv = 0; ex = []
    tries = 0
    while sq + nsq < 150 and tries < 5000:
        tries += 1
        W = [rnd.choice(alpha) for _ in range(rnd.randint(4, 11))]
        if label == 'with-axis' and not any(a[1] == '0' for a in W): continue
        if not rho2.is_knot('l1.l1', W, 'u2.u2'): continue
        hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
        V = replay.VK_project(hw)
        if V is None: continue
        if V == {0: 1}: triv += 1; continue
        if is_square(V): sq += 1
        else:
            nsq += 1
            if len(ex) < 3: ex.append((hw, V))
    print(label, 'nontrivial V: square', sq, 'NOT square', nsq, '| V=1:', triv, '| examples of non-squares:', ex[:2])
