"""S2 regeneration: reproduces engineB/mitm.py + mitm_gated.py with (D1,D2) = (7,7): every width-two theta-curve
s.l1.l1.V.U.u2.u2 with V a top representative (|V| <= 7, projective dedup of rho(V) f0) and U a bottom representative
(|U| <= 7, projective dedup of PHI rho(U)), knot pairs only (mitm.knot_ok); filter J_raw(zeta_7) in +-zeta_7^Z AND
J_raw(zeta_10) in zeta_10^Z (both necessary for J = 1), mod mitm.P.  Records every survivor with its lengths.
Parallel over bottom chunks (fork).  usage: s2_regen.py D1 D2 SEED NPROC"""
import sys, random, time, json, multiprocessing as mp
from collections import defaultdict, Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import mitm, rho2
P = mitm.P
G = {}
def setup(D1, D2, seed):
    rnd = random.Random(seed)
    tg = rnd.randrange(2, P - 1); z7 = mitm.root_of_unity(7); z10 = mitm.root_of_unity(10)
    MT, VT, PHIT = rho2.normalised()
    ts = [tg, z7, z10]
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()} for t in ts]
    V = [[mitm.evt(x, t) for x in VT['l1.l1']] for t in ts]
    PH = []
    for t in ts:
        c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
        PH.append([mitm.evt(x, t) * c % P for x in PHIT['u2.u2']])
    tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[mitm.top_class(w)].append((w, vecs[1], vecs[2]))
    for w, vecs in bots: BG[mitm.bot_class(w)].append((w, vecs[1], vecs[2]))
    G.update(dict(TG=TG, BG=BG, ntops=len(tops), nbots=len(bots),
                  U7=set(pow(z7, k, P) for k in range(7)) | set((-pow(z7, k, P)) % P for k in range(7)),
                  U10=set(pow(z10, k, P) for k in range(10))))
def job(args):
    bc, lo, hi = args
    TG, BG, U7, U10 = G['TG'], G['BG'], G['U7'], G['U10']
    bl = BG[bc][lo:hi]; npairs = 0; n7 = 0; n710 = 0; out = []; bylen = Counter()
    for tc, tl in TG.items():
        if not mitm.knot_ok(tc, bc): continue
        for (wb, b7, b10) in bl:
            b0, b1, b2, b3, b4, b5, b6, b7_, b8 = b7
            lb = len(wb)
            for (wt, u7, u10) in tl:
                s = (b0 * u7[0] + b1 * u7[1] + b2 * u7[2] + b3 * u7[3] + b4 * u7[4] + b5 * u7[5] + b6 * u7[6] + b7_ * u7[7] + b8 * u7[8]) % P
                if s in U7:
                    n7 += 1
                    s10 = sum(x * y for x, y in zip(b10, u10)) % P
                    if s10 in U10:
                        n710 += 1; L = len(wt) + lb; bylen[L] += 1
                        out.append(('.'.join(wt), '.'.join(wb)))
            npairs += len(tl)
    return npairs, n7, n710, dict(bylen), out
if __name__ == '__main__':
    D1, D2, seed, nproc = map(int, sys.argv[1:5])
    t0 = time.time(); setup(D1, D2, seed)
    print('tops', G['ntops'], 'bottoms', G['nbots'], 'setup', round(time.time() - t0, 1), flush=True)
    tasks = []
    for bc, bl in G['BG'].items():
        for lo in range(0, len(bl), 400): tasks.append((bc, lo, lo + 400))
    ctx = mp.get_context('fork')
    tot = [0, 0, 0]; bylen = Counter(); surv = []
    with ctx.Pool(nproc) as pool:
        for npairs, n7, n710, bl, out in pool.imap_unordered(job, tasks):
            tot[0] += npairs; tot[1] += n7; tot[2] += n710; bylen.update(bl); surv.extend(out)
    print('knots', tot[0], 'pass zeta7', tot[1], 'pass zeta7 & zeta10', tot[2], 'by length', dict(sorted(bylen.items())),
          'time', round(time.time() - t0, 1), flush=True)
    json.dump({'D1': D1, 'D2': D2, 'seed': seed, 'P': P, 'tops': G['ntops'], 'bottoms': G['nbots'], 'knots': tot[0],
               'pass7': tot[1], 'pass7_10': tot[2], 'by_length': bylen, 'survivors': surv},
              open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s2_survivors_%d_%d.json' % (D1, D2), 'w'))
