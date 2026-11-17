"""AUDIT-1 test 3: the project bracket kauffman.bracket (trusted input of the jones24 route) and the certifier's PD
bracket diagram.jones (routing V_K = 1 and HIT detection) against the AUDITOR's brute-force state sum (all 2^n states,
own Morse-word edge graph, A-smoothing derived from first principles: 'x' (over SW->NE in the upward picture) -> A =
vertical TL-BL/TR-BR; 'y' -> A = horizontal TL-TR/BL-BR), n <= NMAX.  For n > NMAX: kauffman vs diagram.jones only.
Also: NOT_A_KNOT consistency (diagram.pd_from_halfword is None  <=>  alex.diagram is None).
usage: t3_bracket.py SEED COUNT NPROC NMAX OUT.json"""
import sys, json, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit1_work')
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import audlib, alex, kauffman, replay, diagram
from multiprocessing import Pool

NMAX = [14]

def brute_bracket(full):
    """<D> with <O> = 1 as dict A-exp -> coeff, by summing over all states."""
    # slots: ('c', k, s) for crossing k, s in TL TR BL BR; plus edge ids; build adjacency of slot-ends via caps/cups
    nid = [0]
    def new():
        nid[0] += 1; return nid[0]
    par = {}
    def f(a):
        par.setdefault(a, a)
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    def u(a, b): par[f(a)] = f(b)
    e0 = new(); pos = [e0, e0]; cr = []
    for c, i in full:
        if c in 'xy':
            a, b = pos[i], pos[i + 1]; bl, br = new(), new()
            cr.append((c, a, b, bl, br)); pos[i], pos[i + 1] = bl, br
        elif c in 'lr':
            e = new(); pos[i:i] = [e, e]
        elif c == 'u':
            u(pos[i], pos[i + 1]); del pos[i:i + 2]
    assert not pos
    n = len(cr)
    # edges: classes f(e); each crossing slot is attached to an edge class. A state joins slots inside crossings.
    base = {}
    for k, (c, a, b, bl, br) in enumerate(cr):
        base[(k, 'TL')] = f(a); base[(k, 'TR')] = f(b); base[(k, 'BL')] = f(bl); base[(k, 'BR')] = f(br)
    allcls = set(f(x) for x in list(par))
    for x in range(1, nid[0] + 1): allcls.add(f(x))
    out = {}
    for st in range(1 << n):
        p2 = {c: c for c in allcls}
        def g(a):
            while p2[a] != a:
                p2[a] = p2[p2[a]]; a = p2[a]
            return a
        def j(a, b):
            ra, rb = g(a), g(b)
            if ra != rb: p2[ra] = rb
        nA = 0
        for k, (c, a, b, bl, br) in enumerate(cr):
            useA = not (st >> k) & 1
            vertical = (useA if c == 'x' else not useA)
            if useA: nA += 1
            if vertical:
                j(base[(k, 'TL')], base[(k, 'BL')]); j(base[(k, 'TR')], base[(k, 'BR')])
            else:
                j(base[(k, 'TL')], base[(k, 'TR')]); j(base[(k, 'BL')], base[(k, 'BR')])
        loops = len(set(g(c) for c in allcls))
        ex = nA - (n - nA)
        # delta^(loops-1), delta = -A^2 - A^-2
        poly = {ex: 1}
        for _ in range(loops - 1):
            q = {}
            for e, v in poly.items():
                q[e + 2] = q.get(e + 2, 0) - v; q[e - 2] = q.get(e - 2, 0) - v
            poly = q
        for e, v in poly.items():
            out[e] = out.get(e, 0) + v
    return {e: v for e, v in out.items() if v}

def one(w):
    full = alex.symmetrize(alex.parse(w))
    a_none = full is None or alex.diagram(full) is None
    pd = diagram.pd_from_halfword(w)
    rec = {'w': w, 'nak_consistent': (pd is None) == a_none}
    if a_none or pd is None: return rec
    n = pd.n; rec['n'] = n
    kb = kauffman.bracket(w); kb = {e: v for e, v in kb.items() if v}
    if n <= NMAX[0]:
        bb = brute_bracket(full)
        rec['kauffman_eq_brute'] = (kb == bb)
    Vp = replay.VK_project(w); Vd = diagram.jones(pd)
    rec['VK_eq'] = (Vp == Vd)
    rec['V1'] = (Vd == {0: 1})
    return rec

def init(nm): NMAX[0] = nm

if __name__ == '__main__':
    seed, count, nproc, nmax, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    rnd = random.Random(seed); ws = []; seen = set()
    while len(ws) < count:
        w = audlib.rand_halfword(rnd, rnd.randint(1, 13), maxhw=rnd.choice([3, 5, 7, 9]))
        if rnd.random() < 0.1:       # deliberately broken / exotic words for the NOT_A_KNOT consistency check
            toks = w.split('.'); i = rnd.randrange(1, len(toks)); toks[i] = rnd.choice(['x9', 'u7', 'l0', 'y0', 'u1', 'r5'])
            w = '.'.join(toks)
        if w in seen: continue
        seen.add(w); ws.append(w)
    t0 = time.time()
    with Pool(nproc, initializer=init, initargs=(nmax,)) as P:
        rows = P.map(one, ws, chunksize=4)
    knots = [r for r in rows if 'n' in r]
    summ = {'words': len(rows), 'nak_consistent': sum(r['nak_consistent'] for r in rows), 'knots': len(knots),
            'brute_compared': sum(1 for r in knots if 'kauffman_eq_brute' in r),
            'brute_agree': sum(1 for r in knots if r.get('kauffman_eq_brute')),
            'VK_agree': sum(1 for r in knots if r['VK_eq']), 'V1_knots': sum(1 for r in knots if r['V1']),
            'n_range': (min(r['n'] for r in knots), max(r['n'] for r in knots)),
            'bad': [r for r in rows if not r['nak_consistent'] or r.get('kauffman_eq_brute') is False or r.get('VK_eq') is False][:20],
            'secs': round(time.time() - t0, 1)}
    json.dump({'summary': summ, 'rows': rows}, open(outp, 'w'))
    print(json.dumps(summ))
