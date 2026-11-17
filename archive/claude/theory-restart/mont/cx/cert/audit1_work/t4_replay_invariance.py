"""AUDIT-1 test 4: does the CHECKER's move replay (replay.replay_moves) preserve the group?
Random VALID move sequences (elim / mult with random rotations and exponents / nielsen, indices read off the checker's
own canonical list) are replayed by replay.replay_moves on the checker's Wirtinger presentation; at the end
|Hom(<G|R>, H)| is computed by brute force over H^|G| and compared with |Hom(pi_1, H)| computed independently from the
auditor's plat sweep (exact Artin action).  H in {S3, A4, F20}.  Also: any sequence ending at <a | > on a knot with
V_K != 1 would be a false certificate (reported).
usage: t4_replay_invariance.py SEED COUNT NPROC OUT.json"""
import sys, json, random, time, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit1_work')
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import audlib, replay, alex
from multiprocessing import Pool

HS = None
def init():
    global HS
    HS = [g for g in audlib.groups() if g.name in ('S3', 'A4', 'F20')]

def hom_plat_total(full, H):
    return sum(audlib.plat_count(full, H, list(range(H.N)), c) for c in range(H.N))

def hom_brute(G, R, H):
    k = len(G); pos = {g: t for t, g in enumerate(G)}
    m = H.mul; iv = H.inv; e = H.e
    cnt = 0
    for tup in itertools.product(range(H.N), repeat=k):
        ok = True
        for r in R:
            acc = e
            for a in r:
                x = tup[pos[abs(a)]]
                acc = m[acc][x if a > 0 else iv[x]]
            if acc != e: ok = False; break
        if ok: cnt += 1
    return cnt

def random_move(rnd, G, R, allow_elim=True):
    opts = []
    if allow_elim:
        for j, r in enumerate(R):
            for g in G:
                if sum(1 for a in r if abs(a) == g) == 1: opts.append(('elim', g, j))
    mv = None
    if opts and rnd.random() < 0.45:
        return rnd.choice(opts)
    if len(R) >= 2 and rnd.random() < 0.5:
        i, j = rnd.sample(range(len(R)), 2)
        return ('mult', i, j, rnd.choice((1, -1)), rnd.randrange(len(R[j])), rnd.randrange(len(R[i])))
    if len(G) >= 2:
        x, a = rnd.sample(G, 2)
        return ('nielsen', x, a, rnd.choice((1, -1)), rnd.choice('RL'))
    if opts: return rnd.choice(opts)
    return None

def one(arg):
    w, seed = arg
    rnd = random.Random(seed)
    full = alex.symmetrize(alex.parse(w))
    gens, rels = replay.wirtinger_presentation(w)
    targets = {H.name: hom_plat_total(full, H) for H in HS}
    moves = []; G, R = replay.normal_form(gens, rels)
    steps = rnd.randint(5, 60); maxlen = 400
    for s in range(steps):
        mv = random_move(rnd, G, R, allow_elim=(len(G) > 1))
        if mv is None: break
        res, msg = replay.replay_moves(gens, rels, moves + [mv])
        if res is None: return {'w': w, 'err': 'own valid move rejected: %s %r' % (msg, mv)}
        if sum(len(r) for r in res[1]) > maxlen: continue
        moves.append(mv); G, R = res
    # finish: eliminate while possible to get few generators
    for _ in range(40):
        if len(G) <= 3: break
        opts = [(len(r), g, j) for j, r in enumerate(R) for g in G if sum(1 for a in r if abs(a) == g) == 1]
        if not opts: break
        _, g, j = min(opts)
        res, msg = replay.replay_moves(gens, rels, moves + [('elim', g, j)])
        if res is None: return {'w': w, 'err': 'elim rejected %s' % msg}
        moves.append(('elim', g, j)); G, R = res
    out = {'w': w, 'n': len(gens), 'moves': len(moves), 'kinds': sorted(set(m[0] for m in moves)), 'final_gens': len(G),
           'final_rels': len(R), 'reached_Z': (len(G) == 1 and not R)}
    if len(G) <= 3:
        out['hom'] = {H.name: (targets[H.name], hom_brute(G, R, H)) for H in HS if H.N ** len(G) <= 9000}
        out['ok'] = all(a == b for a, b in out['hom'].values())
    return out

if __name__ == '__main__':
    seed, count, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); ws = []; seen = set()
    while len(ws) < count:
        w = audlib.rand_halfword(rnd, rnd.randint(1, 5), maxhw=5, pcap=0.08, pcup=0.08)
        if w in seen or not audlib.is_knot(w) or audlib.ncross(w) > 10 or audlib.ncaps(w) > 3: continue
        seen.add(w); ws.append((w, rnd.randrange(10 ** 9)))
    t0 = time.time()
    with Pool(nproc, initializer=init) as P:
        rows = P.map(one, ws, chunksize=2)
    errs = [r for r in rows if 'err' in r]
    cmp_rows = [r for r in rows if 'ok' in r]
    summ = {'knots': len(rows), 'errors': errs[:10], 'compared': len(cmp_rows), 'hom_invariant': sum(1 for r in cmp_rows if r['ok']),
            'hom_comparisons': sum(len(r['hom']) for r in cmp_rows),
            'nontrivial_targets': sum(1 for r in cmp_rows for H, (a, b) in r['hom'].items() if a > {'S3': 6, 'A4': 12, 'F20': 20}[H]),
            'mismatch': [r for r in cmp_rows if not r['ok']][:10], 'reached_Z': sum(1 for r in rows if r.get('reached_Z')),
            'move_kinds': sorted(set(k for r in rows for k in r.get('kinds', []))), 'secs': round(time.time() - t0, 1)}
    json.dump({'summary': summ, 'rows': rows}, open(outp, 'w'))
    print(json.dumps(summ))
