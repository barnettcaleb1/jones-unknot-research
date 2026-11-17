"""S3b regeneration: reproduces engineB/template_screen.py D1 D2 SEED (= 6 6): seven-sector coefficients c_ab of every junction
(V,U) at a generic t (mod P), equal-slope groups for the 16 directions, single-group offsets (|r| <= 24) -> candidate lines;
exact unit test at the representative point (fastJ); for every UNIT line the knots at the 5 points k = -2..2 along the line
are recorded (exactly the points engineB certified with kcert).  Parallel over bottom classes.
usage: s3_lines.py D1 D2 SEED NPROC"""
import sys, random, time, json, multiprocessing as mp
from collections import Counter, defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import mitm, rho2, sectors, fastJ
import template_screen as TS
P = mitm.P
SECT = TS.SECT; E = TS.E; DIRS = TS.DIRS; GROUPS = TS.GROUPS; OFFS = TS.OFFS
G = {}
def setup(D1, D2, seed, R=40):
    rnd = random.Random(seed)
    t = rnd.randrange(2, P - 1); u = t * t % P
    S = sectors.setup(t, P)
    Binv, Bm, blocks = S['Binv'], S['B'], S['blocks']
    MT, VT, PHIT = rho2.normalised()
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}]
    V = [[mitm.evt(x, t) for x in VT['l1.l1']]]
    c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
    PH = [[mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]]
    tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
    def tocoords_v(v): return [sum(Binv[i][j] * v[j] for j in range(9)) % P for i in range(9)]
    def tocoords_w(w): return [sum(w[i] * Bm[i][j] for i in range(9)) % P for j in range(9)]
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[mitm.top_class(w)].append((w, tocoords_v(vecs[0])))
    for w, vecs in bots: BG[mitm.bot_class(w)].append((w, tocoords_w(vecs[0])))
    G.update(dict(TG=TG, BG=BG, bl=[blocks[s] for s in SECT], upow={k: pow(u, k % (P - 1), P) for k in range(-4 * R, 4 * R + 1)}))
def job(args):
    bc, lo, hi = args
    TG, BG, bl, upow = G['TG'], G['BG'], G['bl'], G['upow']
    maskhist = Counter(); cands = []; npairs = 0; poss_cache = {}
    for tc, tl in TG.items():
        if not mitm.knot_ok(tc, bc): continue
        for wb, om in BG[bc][lo:hi]:
            for wt, be in tl:
                cs = []
                for b in bl:
                    s = 0
                    for k in b: s += om[k] * be[k]
                    cs.append(s % P)
                nz = frozenset(SECT[i] for i in range(7) if cs[i])
                maskhist[len(nz)] += 1; npairs += 1
                if len(nz) <= 1: continue
                if nz not in poss_cache: poss_cache[nz] = [d for d in DIRS if TS.possible(nz, d) is True]
                dl = poss_cache[nz]
                if not dl: continue
                cd = dict(zip(SECT, cs))
                for d in dl:
                    gs = [[s for s in g if s in nz] for g in GROUPS[d]]
                    gs = [g for g in gs if g]
                    for (m0, n0) in OFFS[d]:
                        vals = []
                        for g in gs:
                            sm = 0
                            for s in g: sm += cd[s] * upow[E[s[0]] * m0 + E[s[1]] * n0]
                            vals.append(sm % P)
                        if sum(1 for x in vals if x) <= 1:
                            cands.append(('.'.join(wt), '.'.join(wb), d, m0, n0))
    return npairs, dict(maskhist), cands
def W_at(wt, wb, m, n):
    return ([x for x in wt.split('.') if x] + (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m))
            + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n)) + [x for x in wb.split('.') if x])
def exact(c):
    wt, wb, d, m0, n0 = c
    Jn = fastJ.J('l1.l1', W_at(wt, wb, m0, n0), 'u2.u2')
    return c, (Jn is not None and len(Jn) == 1)
if __name__ == '__main__':
    D1, D2, seed, nproc = map(int, sys.argv[1:5])
    t0 = time.time(); setup(D1, D2, seed)
    tasks = []
    for bc, bl in G['BG'].items():
        for lo in range(0, len(bl), 200): tasks.append((bc, lo, lo + 200))
    ctx = mp.get_context('fork')
    npairs = 0; mh = Counter(); cands = []; done = 0
    with ctx.Pool(nproc) as pool:
        for a, b, c in pool.imap_unordered(job, tasks):
            npairs += a; mh.update(b); cands.extend(c); done += 1
            if done % 20 == 0: print('tasks', done, '/', len(tasks), 'pairs', npairs, 'cands', len(cands), round(time.time() - t0, 1), flush=True)
        print('pairs', npairs, 'hist |NZ|', dict(mh), 'single-group lines', len(cands), round(time.time() - t0, 1), flush=True)
        ex = pool.map(exact, cands, chunksize=50)
    unit = [c for c, ok in ex if ok]
    print('unit lines', len(unit), 'non-unit', len(ex) - len(unit), round(time.time() - t0, 1), flush=True)
    json.dump({'D1': D1, 'D2': D2, 'seed': seed, 'pairs': npairs, 'nz_hist': mh, 'ncand': len(cands), 'unit_lines': unit},
              open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s3_lines_%d_%d.json' % (D1, D2), 'w'))
