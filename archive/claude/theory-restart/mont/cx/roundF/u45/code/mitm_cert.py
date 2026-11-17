"""mitm_cert.py -- re-run engineB's exhaustive width-two screen (mitm.py, imported READ-ONLY) and CERTIFY every survivor.
Screen (identical to engineB mitm.main): tops = projective classes of rho_2(G1) v (|G1| <= D1), bottoms = projective classes
of phi rho_2(G2) (|G2| <= D2), all class-compatible pairs (knot_ok), filter J_raw(zeta_7) in +-zeta_7^Z (J = 1 forces
it).  Every survivor s.l1.l1.G1.G2.u2.u2 is then classified HERE:
  V_K != 1 (PD bracket)                    -> 'V!=1' (not a J = 1 unknot candidate; engineB's near misses)
  V_K = 1, crossings <= 24                 -> jones24 certificate (replay.check: project bracket + crossing count)
  V_K = 1, crossings > 24                  -> Tietze certificate (replay.check); if that fails: full certify.certify
                                              (long Tietze, reps; COUNTEREXAMPLE writes the HIT file)
Outputs OUT.summary.json, OUT.unresolved.json (every survivor not certified, retained), OUT.tietze.jsonl.gz (certificates
of all > 24-crossing survivors).
usage: mitm_cert.py D1 D2 SEED NPROC OUTPREFIX"""
import sys, json, time, random, gzip
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/code')
import mitm, rho2
import diagram, wirtinger, tietze, replay, certify
from multiprocessing import Pool
P = mitm.P


def survivors(D1, D2, seed):
    rnd = random.Random(seed)
    tg = rnd.randrange(2, P - 1)
    z7 = mitm.root_of_unity(7)
    MT, VT, PHIT = rho2.normalised()
    ts = [tg, z7]
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()} for t in ts]
    V = [[mitm.evt(x, t) for x in VT['l1.l1']] for t in ts]
    PH = []
    for t in ts:
        c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
        PH.append([mitm.evt(x, t) * c % P for x in PHIT['u2.u2']])
    tops = mitm.bfs(Ms, V, D1, 'top')
    bots = mitm.bfs(Ms, PH, D2, 'bot')
    U7 = set(pow(z7, k, P) for k in range(7)) | set((-pow(z7, k, P)) % P for k in range(7))
    from collections import defaultdict
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[mitm.top_class(w)].append((w, vecs[1]))
    for w, vecs in bots: BG[mitm.bot_class(w)].append((w, vecs[1]))
    out = []; npairs = 0
    for tc, tl in TG.items():
        for bc, bl in BG.items():
            if not mitm.knot_ok(tc, bc): continue
            for (wb, b7) in bl:
                b0, b1, b2, b3, b4, b5, b6, b7_, b8 = b7
                for (wt, u7) in tl:
                    s = (b0 * u7[0] + b1 * u7[1] + b2 * u7[2] + b3 * u7[3] + b4 * u7[4] + b5 * u7[5] + b6 * u7[6] + b7_ * u7[7] + b8 * u7[8]) % P
                    if s in U7: out.append((wt, wb))
                npairs += len(tl)
    return len(tops), len(bots), npairs, out


def classify(pair):
    wt, wb = pair
    hw = rho2.halfword('l1.l1', list(wt) + list(wb), 'u2.u2')
    pd = diagram.pd_from_halfword(hw)
    if pd is None: return {'w': hw, 'cls': 'NOT_A_KNOT'}
    # [cert/run fix F3 audit-1] 'V!=1' only if BOTH brackets say so (PD bracket and project bracket kauffman.py)
    if diagram.jones(pd) != {0: 1} and replay.VK_project(hw) != {0: 1}: return {'w': hw, 'cls': 'V!=1', 'n': pd.n}
    if pd.n <= 24:
        ok, msg = replay.check({'kind': 'jones24', 'halfword': hw})
        if ok: return {'w': hw, 'cls': 'UNKNOT_jones24', 'n': pd.n, 'cert': {'kind': 'jones24', 'halfword': hw, 'checker': msg}}
    if pd.n == 0:
        return {'w': hw, 'cls': 'UNKNOT_0', 'n': 0}
    g, r = wirtinger.wirtinger(pd)
    ok, moves, fin, st = tietze.simplify(g, r, seed=0, time_budget=5.0)
    if ok:
        cert = {'kind': 'tietze', 'halfword': hw, 'moves': [list(m) for m in moves]}
        c_ok, msg = replay.check(cert)
        if c_ok: return {'w': hw, 'cls': 'UNKNOT_tietze', 'n': pd.n, 'cert': cert}
    stt, cert = certify.certify(hw, tietze_budget=60.0, rep_budget=60.0, seed=1)
    return {'w': hw, 'cls': 'FULL_' + stt, 'n': pd.n, 'cert': cert}


if __name__ == '__main__':
    D1, D2, seed, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    t0 = time.time()
    ntop, nbot, npairs, surv = survivors(D1, D2, seed)
    print('tops', ntop, 'bottoms', nbot, 'knot pairs', npairs, 'zeta7 survivors', len(surv), 'time', round(time.time() - t0, 1), flush=True)
    from collections import Counter
    cls = Counter(); unres = []; byn = Counter()
    t1 = time.time()
    with Pool(nproc) as Pl, gzip.open(outp + '.tietze.jsonl.gz', 'wt') as f:
        for i, rec in enumerate(Pl.imap_unordered(classify, surv, chunksize=64)):
            cls[rec['cls']] += 1
            if rec.get('n') is not None and rec['cls'] != 'V!=1': byn[rec['n']] += 1
            if rec['cls'] in ('UNKNOT_tietze', 'UNKNOT_jones24'): f.write(json.dumps(rec['cert']) + '\n')   # [cert/run] jones24 words stored too
            elif rec['cls'].startswith('FULL_') or rec['cls'] == 'NOT_A_KNOT':
                unres.append({k: v for k, v in rec.items()})
                if rec['cls'] == 'FULL_CERTIFIED_UNKNOT':
                    f.write(json.dumps(rec['cert']) + '\n')
            if (i + 1) % 20000 == 0:
                print('progress', i + 1, dict(cls), round(time.time() - t1, 1), flush=True)
                json.dump({'partial': True, 'done': i + 1, 'classes': dict(cls)}, open(outp + '.summary.json', 'w'))
    summ = {'D1': D1, 'D2': D2, 'tops': ntop, 'bottoms': nbot, 'knot_pairs': npairs, 'zeta7_survivors': len(surv),
            'classes': dict(cls), 'V=1_crossings_hist': dict(sorted(byn.items())),
            'unresolved_or_full_path': len(unres), 'secs_screen': round(t1 - t0, 1), 'secs_certify': round(time.time() - t1, 1)}
    json.dump(unres, open(outp + '.unresolved.json', 'w'))
    json.dump(summ, open(outp + '.summary.json', 'w'), indent=1)
    print(json.dumps(summ), flush=True)
