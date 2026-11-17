"""gen_sets.py -- test sets for the validation suites.
  unknots LMIN LMAX COUNT SEED OUT    J = 1 width-two configurations s.P.W.S, |W| in [LMIN, LMAX] (random reduced W, all
                                      prefixes l1.l1/l1.l2 and suffixes u1.u2/u2.u2/u3.u2), knots only, deduplicated
  nontrivial LMIN LMAX COUNT SEED OUT random knots with V_K != 1 (half flat_search.gen grammar, half width-two words)
  alextriv SECONDS SEED OUT           annealing for Alexander-trivial knots (Delta = 1) with V_K != 1 (cf. engineB E3d)
"""
import sys, json, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/code')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import refs, diagram, lp
from multiprocessing import Pool

PRE = ['l1.l1', 'l1.l2']; SUF = ['u1.u2', 'u2.u2', 'u3.u2']


def _unk_worker(args):
    seed, lmin, lmax, n_try = args
    rnd = random.Random(seed); out = []
    for _ in range(n_try):
        w = refs.rand_width2(rnd, rnd.randint(lmin, lmax), rnd.choice(PRE), rnd.choice(SUF))
        if not refs.is_knot(w): continue
        if lp.J(w) == {0: 1}: out.append(w)
    return out


def _nt_worker(args):
    seed, lmin, lmax, n = args
    rnd = random.Random(seed); out = []
    while len(out) < n:
        if rnd.random() < 0.5:
            w = refs.rand_width2(rnd, rnd.randint(lmin, lmax), rnd.choice(PRE), rnd.choice(SUF))
        else:
            w = refs.fs.gen(rnd, rnd.randint(max(4, lmin), lmax + 4))
            if not w: continue
        if not refs.is_knot(w): continue
        pd = diagram.pd_from_halfword(w)
        if diagram.jones(pd) != {0: 1}: out.append(w)
    return out


def mirror(w):
    toks = w.split('.')
    out = []
    for t in toks:
        if t and t[0] == 'x': out.append('y' + t[1:])
        elif t and t[0] == 'y': out.append('x' + t[1:])
        else: out.append(t)
    return '.'.join(out)


def _alex_worker(args):
    seed, secs, n = args
    rnd = random.Random(seed); t_end = time.time() + secs
    LET = refs.LET2; found = {}
    import alex
    def score(W):
        w = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
        if not refs.is_knot(w): return None, w
        d1 = alex.alex_eval(w, -1); d2 = alex.alex_eval(w, 2)
        if d1 is None or d2 is None: return None, w
        import math
        return math.log2(max(1, d1)) + math.log2(max(1, d2)), w
    while time.time() < t_end:
        W = [rnd.choice(LET) for _ in range(n)]
        f, w = score(W)
        if f is None: continue
        for step in range(3000):
            if time.time() > t_end: break
            W2 = W[:]
            mv = rnd.random()
            if mv < 0.5: W2[rnd.randrange(n)] = rnd.choice(LET)
            elif mv < 0.8:
                i = rnd.randrange(n - 1); W2[i], W2[i + 1] = W2[i + 1], W2[i]
            else:
                i = rnd.randrange(n); del W2[i]; W2.insert(rnd.randrange(n), rnd.choice(LET))
            f2, w2 = score(W2)
            if f2 is None: continue
            T = 2.0 * (1 - step / 3000) + 0.05
            import math
            if f2 <= f or rnd.random() < math.exp(-(f2 - f) / T):
                W, f, w = W2, f2, w2
            if f == 0:
                pd = diagram.pd_from_halfword(w)
                if diagram.alexander(pd) == ((0, 1),) and diagram.jones(pd) != {0: 1}:
                    found[w] = True
    return list(found)


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'unknots':
        lmin, lmax, count, seed, outp = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
        res = []; seen = set(); s = seed
        with Pool(6) as P:
            while len(res) < count:
                chunks = P.map(_unk_worker, [(s + i, lmin, lmax, 3000) for i in range(6)])
                s += 6
                for ch in chunks:
                    for w in ch:
                        if w not in seen: seen.add(w); res.append(w)
                print('unknots so far', len(res), flush=True)
        json.dump(res[:count], open(outp, 'w'))
    elif mode == 'nontrivial':
        lmin, lmax, count, seed, outp = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
        with Pool(6) as P:
            chunks = P.map(_nt_worker, [(seed + i, lmin, lmax, count // 6 + 1) for i in range(6)])
        res = []; seen = set()
        for ch in chunks:
            for w in ch:
                if w not in seen: seen.add(w); res.append(w)
        json.dump(res[:count], open(outp, 'w'))
        print('nontrivial', len(res[:count]))
    elif mode == 'alextriv':
        secs, seed, outp = float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        with Pool(6) as P:
            chunks = P.map(_alex_worker, [(seed + i, secs, n) for i, n in enumerate([16, 20, 24, 18, 22, 26])])
        res = sorted(set(w for ch in chunks for w in ch))
        json.dump(res, open(outp, 'w'))
        print('alexander-trivial V!=1 found', len(res))
