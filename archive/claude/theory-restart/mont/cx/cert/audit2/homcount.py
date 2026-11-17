"""homcount.py -- count homomorphisms of a Wirtinger presentation into a finite permutation group (own code)."""
import sys, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
import a2lib
pmul, pinv = a2lib.pmul, a2lib.pinv


def closure(gens):
    d = len(gens[0]); e = tuple(range(d))
    seen = {e}; frontier = [e]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = pmul(g, x)
                if y not in seen: seen.add(y); nf.append(y)
        frontier = nf
    return seen


def psl2(p):
    pts = list(range(p)) + ['inf']
    idx = {x: i for i, x in enumerate(pts)}
    def mob(a, b, c, d):
        out = []
        for z in pts:
            if z == 'inf': w = 'inf' if c == 0 else a * pow(c, -1, p) % p
            else:
                den = (c * z + d) % p
                w = 'inf' if den == 0 else (a * z + b) * pow(den, -1, p) % p
            out.append(idx[w])
        return tuple(out)
    return closure([mob(1, 1, 0, 1), mob(0, p - 1, 1, 0)])


def sym(n):
    return closure([tuple([1, 0] + list(range(2, n))), tuple(list(range(1, n)) + [0])])


def alt(n):
    gens = [tuple([1, 2, 0] + list(range(3, n)))]
    if n > 3:
        if n % 2: gens.append(tuple(list(range(1, n)) + [0]))
        else: gens.append(tuple([0] + list(range(2, n)) + [1]))
    return closure(gens)


def count_homs(gens, rels, G):
    """number of homomorphisms (all, including abelian) of <gens|rels> (Wirtinger: rel = (-out, o^s, i, -o^s)) into G."""
    G = list(G)
    # conjugacy classes
    Gs = set(G); classes = []; seen = set()
    for g in G:
        if g in seen: continue
        cl = set(pmul(pmul(h, g), pinv(h)) for h in G)
        seen |= cl; classes.append(sorted(cl))
    rinfo = []
    for r in rels:
        out = -r[0]; s = 1 if r[1] > 0 else -1; o = abs(r[1]); i = r[2]
        rinfo.append((out, o, i, s))
    total = 0
    for cl in classes:
        c0 = cl[0]
        cnt = _count_fixed(gens, rinfo, c0, cl)
        total += cnt * len(cl)
    return total


def _count_fixed(gens, rinfo, c0, cl):
    clset = set(cl)
    first = gens[0]
    def propagate(asg):
        changed = True
        while changed:
            changed = False
            for (out, o, i, s) in rinfo:
                if o in asg and i in asg:
                    xo = asg[o]
                    v = pmul(pmul(xo, asg[i]), pinv(xo)) if s > 0 else pmul(pmul(pinv(xo), asg[i]), xo)
                    if out in asg:
                        if asg[out] != v: return False
                    else:
                        asg[out] = v; changed = True
                elif o in asg and out in asg:
                    xo = asg[o]
                    v = pmul(pmul(pinv(xo), asg[out]), xo) if s > 0 else pmul(pmul(xo, asg[out]), pinv(xo))
                    asg[i] = v; changed = True
        return True
    def rec(asg):
        if not propagate(asg): return 0
        un = [g for g in gens if g not in asg]
        if not un:
            return 1
        # branch on the unassigned generator occurring most often as an over arc
        g = un[0]
        tot = 0
        for c in cl:
            a2 = dict(asg); a2[g] = c
            tot += rec(a2)
        return tot
    return rec({first: c0})
