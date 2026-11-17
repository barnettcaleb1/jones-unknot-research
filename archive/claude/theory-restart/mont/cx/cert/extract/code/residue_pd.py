"""Knot-level fallback for residues: PD of the REDUCED halfword (a diagram of K by the word-level isotopies), then validated
Reidemeister simplification (R1/R2 removals + random R3), several restarts.  0 crossings -> CERT_c_pd; <= 24 -> CERT_a
(exact V_K of the reduced diagram = 1).  Logs are replayable with pd.replay.  usage: residue_pd.py IN.json OUT.json NPROC RESTARTS BUDGET"""
import sys, json, random, time, multiprocessing as mp
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import pd as PDm, vk
def work(args):
    k, hw, restarts, budget = args
    base = PDm.PD.from_halfword(hw)
    if base is None: return k, {'status': 'ALARM_not_knot'}
    best = None
    for r in range(restarts):
        q = base.copy(); q.log = []
        b = q.simplify(random.Random(1000 * k + r), budget=budget)
        if best is None or b.n() < best.n(): best = b
        if best.n() == 0: break
    n = best.n()
    assert PDm.replay(hw, best.log) == n
    out = {'pd_start_crossings': base.n(), 'pd_best_crossings': n, 'pd_log': best.log}
    if n == 0: out['status'] = 'CERT_c_pd'
    elif n <= 24:
        V = vk.VK(hw)
        out['status'] = 'CERT_a_pd_TS24' if V == {0: 1} else 'ALARM_V_ne_1'
    else: out['status'] = 'UNRESOLVED'
    return k, out
if __name__ == '__main__':
    inp, outp, nproc, restarts, budget = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    R = json.load(open(inp))
    t0 = time.time()
    tasks = [(k, r['reduced_halfword'], restarts, budget) for k, r in enumerate(R)]
    ctx = mp.get_context('fork')
    with ctx.Pool(nproc) as pool: res = dict(pool.map(work, tasks, chunksize=4))
    from collections import Counter
    st = Counter()
    for k, r in enumerate(R):
        r.update(res[k]); st[r['status']] += 1
    json.dump(R, open(outp, 'w'))
    print('input', len(R), 'status', dict(st), 'time', round(time.time() - t0, 1))
