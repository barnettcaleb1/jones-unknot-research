"""enum4.py -- realisable 4-ended brackets from plat-type tangles.
T = cup_{2,3} o beta o cap_{2,3} on 4 strands (2 free strands), beta a word in x_i, y_i (i = 0,1,2), length <= L.
Records br(T) = (f, g) in basis (e = 0-tangle '=' , id = inf-tangle '||'), i.e. br = f*e + g*id.
Also tangles from 3-strand braids with a cap/cup (N = 4) and 2-strand rational words."""
import sys, pickle, itertools, cmath
from tl import *
E0 = (1, 0, 3, 2)   # pairs (0,1),(2,3): bottom pair, top pair  = e  = 0-tangle
EI = (3, 2, 1, 0)   # pairs (0,3),(1,2): identity            = inf-tangle
def fg(br):
    assert set(br) <= {E0, EI}, br
    return (br.get(E0, {}), br.get(EI, {}))
def words(L, gens):
    """reduced words (no g g^-1)"""
    inv = {}
    for (k, i) in gens: inv[(k, i)] = ('y' if k == 'x' else 'x', i)
    out = [()]
    frontier = [()]
    for l in range(1, L + 1):
        nf = []
        for w in frontier:
            for g in gens:
                if w and inv[w[-1]] == g: continue
                nf.append(w + (g,))
        out += nf; frontier = nf
    return out
if __name__ == '__main__':
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    gens = [(k, i) for k in 'xy' for i in range(3)]
    seen = {}
    cnt = 0
    for w in words(L, gens):
        word = [('cap', 2)] + list(w) + [('cup', 2)]
        br = evaluate_tangle(word, 2, 2)
        f, g = fg(br)
        key = (tuple(sorted(f.items())), tuple(sorted(g.items())))
        cnt += 1
        if key not in seen: seen[key] = w
    print('words', cnt, 'distinct brackets', len(seen))
    pickle.dump(seen, open('enum4_L%d.pkl' % L, 'wb'))
