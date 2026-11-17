"""Mechanism classification of every unit line / unit plane of the fixed census, with RE-CUTS: a twist site may be slid
through letters it commutes with (X1: x1,y1,x3,y3;  X3: x0,y0,x1,y1,x3,y3;  joint X1^2X3^-2: x1,y1,x3,y3), including the
offset twists of the line, and the disc criteria (geo.py) are tested at every reachable cut.
  SITE-STAB (1,0)/(0,1):  the moving site's curve (c01 / c23) dies in the top or bottom complement at some cut
  JOINT-STAB (1,-1):      X1^2X3^-2 fixes the top at some cut (exact kernel test; sub-type axis-split / band-clasp / both-caps)
  PLANE-GEO:              planes with BOTH sites explained (each at some cut, top or bottom)
  NONE:                   no half stabiliser at any cut; sub-label 'end-segments' if at the junction cut the site's two legs
                          run (through U and the closure) to v_bot and to c/v_top, i.e. the site twists the two END segments of
                          the quotient arc around each other.
Also: exact fastJ re-check of unit-ness (all or a sample), base point (fewest crossings on the line), exact V_K at the base
when <= 24 crossings.   usage: classify2.py D1 D2 NPROC [EXACT_SAMPLE]"""
import sys, pickle, glob, json, random, time
from collections import Counter, defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
from classify import one_class, twist, freered, ncross, base_point, VK1, E, INV
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
COMM = {'X1': {'x1', 'y1', 'x3', 'y3'}, 'X3': {'x0', 'y0', 'x1', 'y1', 'x3', 'y3'}, 'J': {'x1', 'y1', 'x3', 'y3'}}
_t, _b, _j = {}, {}, {}
def ttest(W):
    import geo
    k = tuple(W)
    if k not in _t: _t[k] = geo.top_tests(list(W))
    return _t[k]
def btest(W):
    import geo
    k = tuple(W)
    if k not in _b: _b[k] = geo.bot_tests(list(W))
    return _b[k]
def jtest(W):
    import geo
    k = tuple(W)
    if k not in _j: _j[k] = geo.top_same(list(W), list(W) + ['x1', 'x1', 'y3', 'y3'])
    return _j[k]
def cuts(W, j0, site):
    c = COMM[site]; lo = j0; hi = j0
    while lo > 0 and W[lo - 1] in c: lo -= 1
    while hi < len(W) and W[hi] in c: hi += 1
    return range(lo, hi + 1)
def site_expl(W, j0, site):
    curve = 'c01' if site == 'X1' else 'c23'
    for i in cuts(W, j0, site):
        if ttest(W[:i])[curve]: return ('top' if i == j0 else 'top-recut')
        if btest(W[i:])[curve]: return ('bottom' if i == j0 else 'bottom-recut')
    return None
def joint_expl(W, j0):
    for i in cuts(W, j0, 'J'):
        T = W[:i]; tt = ttest(T)
        if tt['c01'] and tt['c23']: return 'both-caps' + ('' if i == j0 else '-recut')
        if jtest(T): return ('axis-split' if tt['c0123'] else 'band-clasp') + ('' if i == j0 else '-recut')
    return None
def roles(U, legs):
    """closure roles ('v' = to v_bot, 'c' = to v_top via c, 'u' = cup) of junction legs after U"""
    import rho2
    pos = rho2.perm_of(list(U))
    R = {0: 'v', 1: 'u', 2: 'u', 3: 'c'}
    return tuple(sorted(R[pos[p]] for p in legs))
def classify_line(x):
    kind, wt, wb, d, m0, n0, nz, Sv, Sw = x
    V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
    W = V + twist(m0, n0) + U; j0 = len(V)
    rep_top = one_class(Sv, d); rep_bot = one_class(Sw, d)
    rep = 'offset' if kind == 'offset' else ('both' if rep_top and rep_bot else 'top' if rep_top else 'bottom' if rep_bot else 'pairing-only')
    if kind == 'plane':
        e1 = site_expl(W, j0, 'X1'); e3 = site_expl(W, j0, 'X3')
        geo_t = 'PLANE-GEO' if (e1 and e3) else 'PLANE-PARTIAL' if (e1 or e3) else 'NONE'
        sub = '%s|%s' % (e1, e3)
        if geo_t != 'PLANE-GEO':
            miss = [s for s, e in (('X1', e1), ('X3', e3)) if not e]
            sub += ' miss:' + ','.join('%s%s' % (s, roles(W[j0:], (0, 1) if s == 'X1' else (2, 3))) for s in miss)
    elif d in ((1, 0), (0, 1)):
        site = 'X1' if d == (1, 0) else 'X3'
        e = site_expl(W, j0, site)
        geo_t = 'SITE-STAB' if e else 'NONE'
        sub = e if e else 'legs->%s' % (roles(W[j0:], (0, 1) if site == 'X1' else (2, 3)),)
    elif d == (1, -1):
        e = joint_expl(W, j0)
        geo_t = 'JOINT-STAB' if e else 'NONE'
        sub = e if e else ''
    else:
        geo_t, sub = 'NONE', 'other-direction'
    return (kind, d, rep, geo_t, sub)
def work(args):
    chunk, exact_idx = args
    import fastJ
    out = []
    for i, x in chunk:
        c = classify_line(x)
        kind, wt, wb, d, m0, n0 = x[:6]
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        ex = None
        if i in exact_idx:
            J = fastJ.J('l1.l1', V + twist(m0, n0) + U, 'u2.u2'); ex = (J == {0: 1})
        (nc, ln, _), pt, Wb = base_point(V, U, d, m0, n0)
        cert = VK1(Wb) if nc <= 24 else None
        out.append((i, c, ex, nc, pt, tuple(Wb), cert))
    return out
if __name__ == '__main__':
    import multiprocessing as mp
    D1, D2, nproc = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    nex = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9
    lines = []
    for f in sorted(glob.glob(OUT + 'census_%d_%d_w*.pkl' % (D1, D2))):
        r, u, pl = pickle.load(open(f, 'rb')); lines.extend(u)
        for wt, wb, nz, Sv, Sw, unit in pl:
            if unit: lines.append(('plane', wt, wb, (1, 0), 0, 0, nz, Sv, Sw))
    rnd = random.Random(7); idx = list(range(len(lines)))
    exact_idx = set(idx) if nex >= len(idx) else set(rnd.sample(idx, nex))
    chunks = [[] for _ in range(nproc * 8)]
    for i in idx: chunks[i % len(chunks)].append((i, lines[i]))
    t0 = time.time()
    with mp.get_context('spawn').Pool(nproc) as pool:
        res = pool.map(work, [(ch, exact_idx) for ch in chunks])
    allr = sorted([y for r in res for y in r])
    print('classified', len(allr), 'lines/planes in', round(time.time() - t0, 1), 's', flush=True)
    tab = Counter(); certtab = Counter(); exacttab = Counter(); examples = defaultdict(list); ncr = Counter()
    for (i, c, ex, nc, pt, Wb, cert) in allr:
        kind, d, rep, geo_t, sub = c
        tab[c] += 1
        st = 'base<=24,V=1' if cert is True else 'base<=24,V!=1' if cert is False else ('base>24' if nc > 24 else 'base<=24,notknot?')
        certtab[(kind, d, geo_t, st)] += 1
        if ex is not None: exacttab[(kind, ex)] += 1
        if len(examples[c]) < 5: examples[c].append((lines[i][1], lines[i][2], lines[i][4], lines[i][5], pt, nc, '.'.join(Wb)))
    print('EXACT unit re-check (fastJ, representative point):', dict(exacttab))
    print('TYPES (kind, direction, rep-level support, geometric mechanism, detail): count')
    for k in sorted(tab, key=str): print('   ', k, tab[k])
    print('BASE-KNOT status (kind, direction, mechanism, base):')
    for k in sorted(certtab, key=str): print('   ', k, certtab[k])
    print('EXAMPLES:')
    for k in sorted(examples, key=str):
        print('  ', k)
        for e in examples[k]: print('      V=%s U=%s offset=(%d,%d) base=%s crossings=%d word=%s' % e)
    pickle.dump({'lines': lines, 'res': allr}, open(OUT + 'classify2_%d_%d.pkl' % (D1, D2), 'wb'))
    json.dump({'types': {str(k): v for k, v in tab.items()}, 'cert': {str(k): v for k, v in certtab.items()},
               'exact': {str(k): v for k, v in exacttab.items()}}, open(OUT + 'classify2_%d_%d.json' % (D1, D2), 'w'), indent=1)
