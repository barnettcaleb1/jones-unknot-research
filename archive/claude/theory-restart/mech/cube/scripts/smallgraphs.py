from indcx import reduced_betti, euler_reduced
def mk(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    return adj
def cycle(names): return [(names[i], names[(i + 1) % len(names)]) for i in range(len(names))]
def two_cycles(a, b):
    c1 = ['v'] + ['a%d' % i for i in range(a - 1)]
    c2 = ['v'] + ['b%d' % i for i in range(b - 1)]
    return mk(cycle(c1) + cycle(c2))
for a in (4, 6, 8, 10):
    for b in (4, 6, 8, 10):
        if a <= b:
            g = two_cycles(a, b); print('C%d v C%d  (|V|=%d):' % (a, b, len(g)), reduced_betti(g))
# cycle with pendant path
def cyc_pend(n, k):
    c = ['c%d' % i for i in range(n)]
    e = cycle(c); prev = 'c0'
    for i in range(k):
        e.append((prev, 'p%d' % i)); prev = 'p%d' % i
    return mk(e)
for n in (4, 6, 8):
    for k in range(0, 5):
        print('C%d + pendant path %d:' % (n, k), reduced_betti(cyc_pend(n, k)))
# two cycles joined by a path of length k (k edges)
def two_cyc_path(a, b, k):
    c1 = ['a%d' % i for i in range(a)]; c2 = ['b%d' % i for i in range(b)]
    e = cycle(c1) + cycle(c2)
    path = ['a0'] + ['p%d' % i for i in range(k - 1)] + ['b0']
    e += [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    return mk(e)
for a, b in ((6, 6), (4, 6), (4, 4)):
    for k in range(1, 5):
        g = two_cyc_path(a, b, k); print('C%d -path%d- C%d (|V|=%d):' % (a, k, b, len(g)), reduced_betti(g))
# theta graphs: two vertices joined by three paths with i,j,k internal vertices
def theta(i, j, k):
    e = []
    for nm, l in (('x', i), ('y', j), ('z', k)):
        path = ['s'] + ['%s%d' % (nm, t) for t in range(l)] + ['t']
        e += [(path[t], path[t + 1]) for t in range(len(path) - 1)]
    return mk(e)
for i in range(1, 6):
    for j in range(i, 6):
        for k in range(j, 6):
            if (i + j) % 2 == 0 and (j + k) % 2 == 0:
                b = reduced_betti(theta(i, j, k))
                if len(b) > 1 or sum(b.values()) > 1: print('theta', i, j, k, b)
