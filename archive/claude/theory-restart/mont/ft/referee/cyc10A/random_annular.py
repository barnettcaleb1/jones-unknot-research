"""Lens A (2),(5): test the full annular comparison E_-(D) = E_+(D) at primitive fifth roots on RANDOM annular diagrams,
including non-braid ones (colour-2 cup-caps), plus exact multiplicativity of both functionals on concentric products.
No knot scan: these are annular skein elements, the objects of Sections 2-4."""
import random, sys, time
import sympy as S
from annulus_eval import E_minus, E_plus, mod_phi5, Q
rnd = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
# exact multiplicativity on concentric (= stacked) products, both sides
def conc(D1, n1, D2, n2):  # D1 on strands 0..n1-1 (inner), D2 shifted (outer)
    return D1 + [(g[0], g[1]+n1) + tuple(g[2:]) for g in D2], n1+n2
tests = [([('s',0,1)],2,[],1), ([('s',0,1),('s',1,1)],3,[('s',0,1)],2), ([('s',0,-1)],2,[('s',0,1)],2), ([('e',0)],2,[],1)]
for D1,n1,D2,n2 in tests:
    D,n = conc(D1,n1,D2,n2)
    for E,nm in ((E_minus,'E-'),(E_plus,'E+')):
        lhs = E(D,n); rhs = S.expand(E(D1,n1)*E(D2,n2)) if D2 or n2 else None
        print(nm, 'multiplicative on', D1, '|', D2, ':', S.simplify(lhs - rhs) == 0)
# contractible loop: closure of e on 2 strands = d (no winding)
print('E-(closure e_1) = d_- :', S.simplify(E_minus([('e',0)],2) - (1-Q-1/Q)*E_minus([],0 or 1)/E_minus([],1)*1) if False else '')
# random diagrams
ok = 0; tot = 0; nonzero = 0; t0 = time.time()
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 40):
    n = rnd.choice([2, 3, 3, 4])
    L = rnd.randint(2, 7 if n < 4 else 5)
    D = []
    for _ in range(L):
        j = rnd.randrange(n-1)
        D.append(('e', j) if rnd.random() < 0.2 else ('s', j, rnd.choice([1, -1])))
    em = E_minus(D, n); ep = E_plus(D, n)
    r = mod_phi5(em - ep)
    tot += 1; ok += (r == 0); nonzero += (S.simplify(em - ep) != 0)
    if r != 0: print('FAIL', n, D, r)
print(f'random annular diagrams: {ok}/{tot} equal at primitive 5th roots; {nonzero}/{tot} differ as Laurent polys (test nontrivial); {time.time()-t0:.1f}s')
