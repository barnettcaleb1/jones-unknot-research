"""Classify every unit line of the fixed census (D1,D2) by mechanism, re-check unit-ness exactly, and certify base knots.
REP level (rho_2): top-scalar = Sv in one d-slope class (g = X1^(2p) X3^(2q) scalar on V v); bot-scalar = Sw in one class;
  pairing-only = neither (only the pairing support nz lies in one class) ; offset = engineB's offset-specific lines.
GEOMETRIC level (geo.py, exact free groups):
  TOP-STAB : g fixes the top half  [(1,0): c01 dies in pi_1(top); (0,1): c23 dies; (1,-1): kernel test T_V = T_{V.x1.x1.y3.y3}]
  BOT-STAB : g fixes the bottom    [(1,0): c01 dies in pi_1(bottom); (0,1): c23 dies; (1,-1): c01 and c23 both die]
  SPLIT    : (1,-1) with X1^2 fixing one half and X3^2 the other
  NONE     : no half stabiliser found.
BASE KNOT: the point of the line with the fewest crossings (free-reduced word, k in [-40,40]); if <= 24 crossings, V_K exact
  (kauffman.bracket, ident3 normalisation); V_K = 1 there => CERTIFIED_UNKNOT (Tuzun-Sikora), and for a geometric line every
  knot on the line is isotopic to it.
usage: classify.py D1 D2 NPROC [EXACT_SAMPLE]"""
import sys, pickle, glob, json, random, time
from collections import Counter, defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
E = {0: 0, 2: 1, 4: 3}
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
def slope(s, d): return E[s[0]] * d[0] + E[s[1]] * d[1]
def one_class(S, d): return len(set(slope(s, d) for s in S)) <= 1
def twist(m, n): return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def freered(W):
    out = []
    for L in W:
        if out and out[-1] == INV[L]: out.pop()
        else: out.append(L)
    return out
def ncross(W): return sum(1 if L[1] == '0' else 2 for L in W)
def base_point(V, U, d, m0, n0):
    best = None
    for k in range(-40, 41):
        m, n = m0 + k * d[0], n0 + k * d[1]
        W = freered(V + twist(m, n) + U)
        key = (ncross(W), len(W), abs(m) + abs(n))
        if best is None or key < best[0]: best = (key, (m, n), W)
    return best
_gt, _gb = {}, {}
def top_geo(V):
    import geo
    k = tuple(V)
    if k not in _gt:
        r = geo.top_tests(V)
        r['stab_1m1'] = geo.top_same(V, V + ['x1', 'x1', 'y3', 'y3'])
        _gt[k] = r
    return _gt[k]
def bot_geo(U):
    import geo
    k = tuple(U)
    if k not in _gb: _gb[k] = geo.bot_tests(U)
    return _gb[k]
_vk = {}
def VK1(W):
    """exact V_K == 1 for the halfword s.l1.l1.W.u2.u2 (ident3 normalisation); None if not a knot diagram"""
    k = tuple(W)
    if k not in _vk:
        import kauffman
        hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
        kb = kauffman.bracket(hw)
        if not kb: _vk[k] = None
        else:
            kb = {e: c for e, c in kb.items() if c}
            _vk[k] = (len(kb) == 1)
    return _vk[k]
def classify_one(x):
    kind, wt, wb, d, m0, n0, nz, Sv, Sw = x
    V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
    rep_top = one_class(Sv, d); rep_bot = one_class(Sw, d)
    rep = 'offset' if kind == 'offset' else ('both' if rep_top and rep_bot else 'top-scalar' if rep_top else 'bot-scalar' if rep_bot else 'pairing-only')
    tg = top_geo(V); bg = bot_geo(U)
    if d == (1, 0): topst, botst, split = tg['c01'], bg['c01'], False
    elif d == (0, 1): topst, botst, split = tg['c23'], bg['c23'], False
    elif d == (1, -1):
        topst = tg['stab_1m1'] or (tg['c01'] and tg['c23'])
        botst = bg['c01'] and bg['c23']
        split = (tg['c01'] and bg['c23']) or (tg['c23'] and bg['c01'])
    else: topst = botst = split = False
    geo_t = 'TOP-STAB' if topst else 'BOT-STAB' if botst else 'SPLIT' if split else 'NONE'
    sub = ''
    if geo_t == 'TOP-STAB' and d == (1, -1): sub = 'axis-split' if tg['c0123'] else ('both-caps' if (tg['c01'] and tg['c23']) else 'band-clasp')
    (nc, ln, _), (mb, nb), Wb = base_point(V, U, d, m0, n0)
    return (kind, d, rep, geo_t, sub, nc, (mb, nb), Wb)
def work(args):
    chunk, exact_idx = args
    import fastJ
    out = []
    for i, x in chunk:
        c = classify_one(x)
        kind, wt, wb, d, m0, n0 = x[:6]
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        ex = None
        if i in exact_idx:
            J = fastJ.J('l1.l1', V + twist(m0, n0) + U, 'u2.u2')
            ex = (J == {0: 1})
        cert = None
        if c[5] <= 24: cert = VK1(c[7])
        out.append((i, c, ex, cert))
    return out
if __name__ == '__main__':
    import multiprocessing as mp
    D1, D2, nproc = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    nex = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9
    U_all = []; PL = []
    for f in sorted(glob.glob(OUT + 'census_%d_%d_w*.pkl' % (D1, D2))):
        r, u, pl = pickle.load(open(f, 'rb')); U_all.extend(u); PL.extend(pl)
    # planes become 'plane' lines in direction (1,0) only for classification purposes (one representative per plane)
    lines = list(U_all)
    for wt, wb, nz, Sv, Sw, unit in PL:
        if unit: lines.append(('plane', wt, wb, (1, 0), 0, 0, nz, Sv, Sw))
    rnd = random.Random(7)
    idx = list(range(len(lines)))
    exact_idx = set(idx) if nex >= len(idx) else set(rnd.sample(idx, nex))
    chunks = [[] for _ in range(nproc * 8)]
    for i in idx: chunks[i % len(chunks)].append((i, lines[i]))
    t0 = time.time()
    with mp.get_context('spawn').Pool(nproc) as pool:
        res = pool.map(work, [(ch, exact_idx) for ch in chunks])
    allr = sorted([y for r in res for y in r])
    print('classified', len(allr), 'lines in', round(time.time() - t0, 1), 's', flush=True)
    tab = Counter(); certtab = Counter(); exacttab = Counter(); examples = defaultdict(list)
    for (i, c, ex, cert) in allr:
        kind, d, rep, geo_t, sub, nc, pt, Wb = c
        key = (kind, d, rep, geo_t, sub)
        tab[key] += 1
        certtab[(kind, d, geo_t, 'base<=24:V=1' if cert is True else 'base<=24:V!=1' if cert is False else 'base>24' if nc > 24 else 'notknot?')] += 1
        if ex is not None: exacttab[(kind, ex)] += 1
        if len(examples[key]) < 6: examples[key].append((lines[i][1], lines[i][2], lines[i][4], lines[i][5], pt, nc, '.'.join(Wb)))
    print('EXACT unit re-check (fastJ at the representative point):', dict(exacttab))
    print('TYPES (kind, direction, rep-level, geometric, sub):')
    for k in sorted(tab, key=str): print('   ', k, tab[k])
    print('BASE-KNOT certification (kind, direction, geometric, status):')
    for k in sorted(certtab, key=str): print('   ', k, certtab[k])
    print('EXAMPLES:')
    for k in sorted(examples, key=str):
        print('  ', k)
        for e in examples[k]: print('      V=%s U=%s offset=(%d,%d) base=%s crossings=%d word=%s' % e)
    pickle.dump({'lines': lines, 'res': allr}, open(OUT + 'classify_%d_%d.pkl' % (D1, D2), 'wb'))
    json.dump({'types': {str(k): v for k, v in tab.items()}, 'cert': {str(k): v for k, v in certtab.items()},
               'exact': {str(k): v for k, v in exacttab.items()}}, open(OUT + 'classify_%d_%d.json' % (D1, D2), 'w'), indent=1)
