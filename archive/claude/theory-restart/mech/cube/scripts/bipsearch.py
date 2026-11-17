"""All bipartite graphs with parts (a,b), a+b <= N: find those whose independence complex has F_2 homology
in more than one degree. Canonicalise by sorted rows/cols crude key to cut duplicates."""
import itertools, sys, collections
from indcx import reduced_betti, fold_reduce
N = int(sys.argv[1])
found = collections.OrderedDict()
for a in range(1, N):
    for b in range(a, N - a + 1):
        seen = set()
        for mask in range(1 << (a * b)):
            rows = [(mask >> (i * b)) & ((1 << b) - 1) for i in range(a)]
            if any(r == 0 for r in rows): continue
            if rows != sorted(rows): continue          # rows sorted (partial canonical form)
            cols = [sum(((rows[i] >> j) & 1) << i for i in range(a)) for j in range(b)]
            if any(c == 0 for c in cols): continue
            if cols != sorted(cols): continue
            adj = {('r', i): set() for i in range(a)}; adj.update({('c', j): set() for j in range(b)})
            for i in range(a):
                for j in range(b):
                    if (rows[i] >> j) & 1:
                        adj[('r', i)].add(('c', j)); adj[('c', j)].add(('r', i))
            red, contr = fold_reduce(adj)
            if contr or len(red) != len(adj): continue  # only fold-irreducible graphs
            bt = reduced_betti(adj, reduce=False)
            if len(bt) > 1:
                key = (a, b, tuple(sorted(sorted(len(adj[v]) for v in adj))), tuple(sorted(bt.items())))
                if key not in found:
                    found[key] = (rows, bt)
for k, (rows, bt) in found.items():
    print(k[0], k[1], 'degrees', k[2], 'betti', bt, 'rows', [bin(r) for r in rows])
print(len(found))
