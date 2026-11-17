"""Search band diagrams (kht++ quotient construction, no framing twists) of symmetric half-words for
chain-level extreme parts of E_H (H = connectivity of Q_0) that are nonzero in more than one degree."""
import itertools, sys, collections, random, time
from cube import Diagram, parse, quotient_word, word_str, conn_name, CONN_H, CONN_V
from indcx import reduced_betti, fold_reduce, euler_reduced

def extreme_EH(D, which):
    """chain-level extreme part of E_H at the 'which' end. Returns (kind, betti dict) where betti is indexed by
    |J| (number of crossings flipped from the extreme state), or None if not determined."""
    L = D.lando(which)
    if L['conn'] == CONN_H:
        b = reduced_betti(L['adj'])
        return ('H', {d + 1: v for d, v in b.items()}, L)
    elif L['conn'] == CONN_V:
        b0 = reduced_betti(L['adj'])
        L2 = D.lando(which, close=[('u', 0)])
        b2 = reduced_betti(L2['adj'])
        if b0:
            return ('V-nonacyclic', {'X0': b0, 'Xp': b2}, L)
        return ('V', {d + 1: v for d, v in b2.items()}, L)
    return ('?', {}, L)

def gen_words(maxcross, caps=1):
    """half words: l1, then letters among x0,y0,x1,y1,x2,y2 (3 strands), then u1 or u2."""
    letters = [('x', 0), ('y', 0), ('x', 1), ('y', 1), ('x', 2), ('y', 2)]
    inv = {('x', i): ('y', i) for i in range(3)}; inv.update({('y', i): ('x', i) for i in range(3)})
    def rec(w):
        if w: yield list(w)
        if len(w) == maxcross: return
        for a in letters:
            if w and inv[w[-1]] == a: continue
            if w and w[-1][1] == 2 and a[1] == 0: continue   # commuting letters: index 0 before index 2
            w.append(a)
            yield from rec(w)
            w.pop()
    for w in rec([]):
        for cup in (1, 2):
            yield [('l', 1)] + w + [('u', cup)]

if __name__ == '__main__':
    maxc = int(sys.argv[1]); limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9
    t0 = time.time(); cnt = 0; good = 0; stats = collections.Counter(); hits = []
    for half in gen_words(maxc):
        try:
            q = quotient_word(half, True, 0); D = Diagram(q, 1)
        except ValueError:
            continue
        loops, tops, bots = D.components_through_crossings()
        if loops: continue
        cnt += 1
        if cnt > limit: break
        for which in 'AB':
            kind, b, L = extreme_EH(D, which)
            key = (kind, tuple(sorted(b.items())) if kind in ('H', 'V') else 'x')
            stats[(kind, len(b) if kind in 'HV' else -1)] += 1
            if kind in ('H', 'V') and len(b) > 1:
                hits.append((word_str(half), which, kind, b, D.n))
    print('diagrams', cnt, 'time %.1f' % (time.time() - t0))
    print('stats (kind, number of nonzero degrees):', sorted(stats.items()))
    for h in hits[:60]: print(h)
    print('hits', len(hits))
