"""Independence complexes of graphs over F_2: reduced Betti numbers, with fold reductions.
Graph = dict v -> set of neighbours (symmetric)."""
import itertools, sys
from functools import lru_cache

def fold_reduce(adj):
    """Repeatedly remove a vertex v when some u != v has N(u) subset of N(v) (Ind unchanged up to homotopy).
    Returns (adj, contractible_flag). An isolated vertex makes Ind a cone (contractible)."""
    adj = {v: set(n) for v, n in adj.items()}
    changed = True
    while changed:
        changed = False
        vs = list(adj)
        for u in vs:
            if not adj[u]:
                return adj, True
        for u in vs:
            if u not in adj: continue
            for v in vs:
                if v == u or v not in adj or u not in adj: continue
                if v in adj[u]: continue
                if adj[u] <= adj[v]:
                    for w in adj[v]: adj[w].discard(v)
                    del adj[v]
                    changed = True
    return adj, False

def indep_sets(adj):
    vs = sorted(adj)
    idx = {v: i for i, v in enumerate(vs)}
    nb = [sum(1 << idx[w] for w in adj[v]) for v in vs]
    out = []
    def rec(i, cur, forb):
        if i == len(vs):
            out.append(cur); return
        rec(i + 1, cur, forb)
        if not (forb >> i) & 1:
            rec(i + 1, cur | (1 << i), forb | nb[i])
    rec(0, 0, 0)
    return out, len(vs)

def rank_f2(rows):
    """rows: list of python ints (bit vectors). Returns rank over F_2."""
    piv = {}
    r = 0
    for x in rows:
        while x:
            h = x.bit_length() - 1
            if h in piv:
                x ^= piv[h]
            else:
                piv[h] = x; r += 1; break
    return r

def reduced_betti(adj, reduce=True, maxsets=400000):
    """Reduced F_2 Betti numbers of Ind(G) as dict dim -> rank (dim = |I|-1, so dim -1 is the empty set).
    Returns {} if acyclic."""
    if reduce:
        adj, contr = fold_reduce(adj)
        if contr: return {}
    if not adj:
        return {-1: 1}
    sets, n = indep_sets(adj)
    if len(sets) > maxsets:
        raise RuntimeError("too many independent sets: %d" % len(sets))
    bydim = {}
    for s in sets:
        bydim.setdefault(bin(s).count('1') - 1, []).append(s)
    dims = sorted(bydim)
    index = {d: {s: i for i, s in enumerate(bydim[d])} for d in dims}
    ranks = {}
    for d in dims:
        if d == -1: ranks[d] = 0; continue
        rows = []
        for s in bydim[d]:
            row = 0; t = s
            while t:
                b = t & -t; t ^= b
                row |= 1 << index[d - 1][s ^ b]
            rows.append(row)
        ranks[d] = rank_f2(rows)
    betti = {}
    for d in dims:
        b = len(bydim[d]) - ranks[d] - ranks.get(d + 1, 0)
        if b: betti[d] = b
    return betti

def euler_reduced(adj):
    """sum over independent sets of (-1)^{|I|-1} = -I(G;-1)."""
    vs = sorted(adj); idx = {v: i for i, v in enumerate(vs)}
    nb = tuple(sum(1 << idx[w] for w in adj[v]) for v in vs)
    @lru_cache(maxsize=None)
    def I(mask):
        if mask == 0: return 1
        i = mask.bit_length() - 1
        return I(mask & ~(1 << i)) - I(mask & ~(1 << i) & ~nb[i])
    return -I((1 << len(vs)) - 1)

if __name__ == '__main__':
    # tests: cycles
    def cyc(n): return {i: {(i - 1) % n, (i + 1) % n} for i in range(n)}
    for n in range(3, 10): print('C%d' % n, reduced_betti(cyc(n)), euler_reduced(cyc(n)))
    # two hexagons sharing a vertex (GMS example)
    adj = {i: set() for i in range(1, 12)}
    def e(a, b): adj[a].add(b); adj[b].add(a)
    for a, b in [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1),(1,7),(7,8),(8,9),(9,10),(10,11),(11,1)]: e(a, b)
    print('two hexagons sharing a vertex:', reduced_betti(adj), reduced_betti(adj, reduce=False), euler_reduced(adj))
