"""critic: run regress's OWN line classifier (classify2.classify_line + classify3.global_expl, imported read-only) on the
unit lines / unit planes that the (6,6) census never saw because their bottom class hides a different tangle (cert/run
geo_bfs missed classes, depth <= 6).  For each: mechanism type, base point (fewest crossings), base halfword.
Writes critic/missed/missed66_classified.json and the distinct base halfwords for the certifier."""
import sys, json, pickle, glob, time
sys.dont_write_bytecode = True
for p in ('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress', '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig',
          '/Users/calebbarnett/jones-lanes/theory-restart/mont', '/Users/calebbarnett/jones-lanes/theory-restart/tools'):
    sys.path.insert(0, p)
from collections import Counter, defaultdict
OUTD = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/missed/'

def work(chunk):
    sys.dont_write_bytecode = True
    import classify2 as C2, classify3 as C3
    from classify import twist, base_point
    out = []
    for x, rep in chunk:
        kind, wt, wb, d, m0, n0 = x[:6]
        c = C2.classify_line(x)
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        W = V + twist(m0, n0) + U; j0 = len(V)
        g = {}
        if c[3] in ('NONE', 'PLANE-PARTIAL'):
            if kind == 'plane':
                for site in ('X1', 'X3'):
                    e = C2.site_expl(W, j0, site)
                    if e: g[site] = 'half:' + e
                    else:
                        r, seen = C3.global_expl(W, j0, site); g[site] = ('global:' + r) if r else 'NONE'
            elif d in ((1, 0), (0, 1)):
                site = 'X1' if d == (1, 0) else 'X3'
                r, seen = C3.global_expl(W, j0, site); g[site] = ('global:' + r) if r else 'NONE'
        (nc, ln, _), pt, Wb = base_point(V, U, d, m0, n0)
        hw = 's.l1.l1.' + '.'.join(Wb) + '.u2.u2' if Wb else 's.l1.l1.u2.u2'
        out.append({'kind': kind, 'V': wt, 'U_missed': wb, 'U_rep': rep, 'd': list(d), 'm0': m0, 'n0': n0,
                    'type': list(c), 'global': g, 'base_pt': list(pt), 'base_cross': nc, 'base_hw': hw})
    return out

if __name__ == '__main__':
    import multiprocessing as mp
    D = int(sys.argv[1]); nproc = int(sys.argv[2])
    gb = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/out/dedup/geo_bfs_d7.json'))
    by_rep = defaultdict(list)
    for m in gb['bottom']['missed']:
        if 'missed_word' in m and m['depth'] <= D: by_rep[m['mitm_rep']].append(m['missed_word'])
    items = []
    for f in sorted(glob.glob('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/census_%d_%d_w*.pkl' % (D, D))):
        st, units, pls = pickle.load(open(f, 'rb'))
        for u in units:
            if u[2] in by_rep:
                for Um in by_rep[u[2]]: items.append(((u[0], u[1], Um) + tuple(u[3:]), u[2]))
        for wt, wb, nz, Sv, Sw, unit in pls:
            if unit and wb in by_rep:
                for Um in by_rep[wb]: items.append((('plane', wt, Um, (1, 0), 0, 0, nz, Sv, Sw), wb))
    print('missed items', len(items), flush=True)
    chunks = [items[k::nproc * 6] for k in range(nproc * 6)]
    t0 = time.time()
    with mp.get_context('spawn').Pool(nproc) as pool:
        rr = pool.map(work, chunks)
    allr = [y for r in rr for y in r]
    print('classified', len(allr), 'in', round(time.time() - t0, 1), 's', flush=True)
    tab = Counter()
    for r in allr:
        t = r['type']; g = r['global']
        lab = t[3] if t[3] not in ('NONE', 'PLANE-PARTIAL') else ('%s|%s' % (t[3], ','.join('%s=%s' % kv for kv in sorted(g.items()))))
        tab[(r['kind'], tuple(r['d']) if r['kind'] != 'plane' else 'plane', lab, 'base<=24' if r['base_cross'] <= 24 else 'base>24')] += 1
    for k in sorted(tab, key=str): print('   ', k, tab[k])
    json.dump(allr, open(OUTD + 'missed%d%d_classified.json' % (D, D), 'w'))
    bases = sorted(set(r['base_hw'] for r in allr))
    json.dump([['base', b] for b in bases], open(OUTD + 'missed%d%d_bases.json' % (D, D), 'w'))
    print('distinct base halfwords', len(bases))
