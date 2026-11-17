"""Stage 3 for residues still UNRESOLVED after residue_pd.py: start the validated PD simplifier from many alternative diagrams
of K obtained by random length-preserving word moves (reduce.LP: commutation/braid/type-B, all isotopies) and random
insertion of absorbable end letters (inverse R1 / Hilden moves at caps and cups, also isotopies), from the reduced word.
Each alternative word comes with its move list from the reduced word (replayable: reduce.apply_move / inverse insertions logged).
usage: residue_pd2.py IN.json OUT.json NPROC NALT RESTARTS BUDGET"""
import sys, json, random, time, multiprocessing as mp
from collections import Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import pd as PDm, vk, rules, reduce as R
INS_TOP = [p for p, why in rules.TOPPAT]; INS_BOT = [p for p, why in rules.BOTPAT]
def random_alt(w, rnd, steps):
    """random isotopy walk: length-preserving rewrites + occasional insertion of an absorbable end pattern"""
    w = tuple(w); log = []
    for _ in range(steps):
        r = rnd.random()
        if r < 0.08:
            k = rnd.randrange(len(INS_TOP)); w = INS_TOP[k] + w; log.append(('insT', k))
        elif r < 0.16:
            k = rnd.randrange(len(INS_BOT)); w = w + INS_BOT[k]; log.append(('insB', k))
        else:
            nb = list(R.neighbours(w))
            if not nb: continue
            w, mv = rnd.choice(nb); log.append(mv)
    return w, log
def work(args):
    k, hw_red, nalt, restarts, budget = args
    rnd = random.Random(k)
    w0 = rules.enc(hw_red[len('s.l1.l1.'):-len('.u2.u2')].split('.')) if hw_red != 's.l1.l1.u2.u2' else ()
    best = None
    for a in range(nalt):
        if a == 0: w, wlog = w0, []
        else: w, wlog = random_alt(w0, rnd, rnd.randint(5, 60))
        hw = 's.l1.l1.' + rules.dec(w) + '.u2.u2' if w else 's.l1.l1.u2.u2'
        base = PDm.PD.from_halfword(hw)
        for r in range(restarts):
            q = base.copy(); q.log = []
            b = q.simplify(random.Random(97 * k + 13 * a + r), budget=budget)
            if best is None or b.n() < best[0]:
                best = (b.n(), hw, wlog, b.log, base.n())
            if best[0] == 0: break
        if best[0] == 0: break
    n, hw, wlog, plog, n0 = best
    assert PDm.replay(hw, plog) == n
    out = {'alt_halfword': hw, 'alt_word_log': wlog, 'pd_start_crossings': n0, 'pd_best_crossings': n, 'pd_log': plog}
    if n == 0: out['status'] = 'CERT_c_pd'
    elif n <= 24: out['status'] = 'CERT_a_pd_TS24' if vk.VK(hw) == {0: 1} else 'ALARM_V_ne_1'
    else: out['status'] = 'UNRESOLVED'
    return k, out
if __name__ == '__main__':
    inp, outp = sys.argv[1], sys.argv[2]
    nproc, nalt, restarts, budget = map(int, sys.argv[3:7])
    Rr = json.load(open(inp))
    todo = [k for k, r in enumerate(Rr) if r['status'] == 'UNRESOLVED']
    t0 = time.time()
    ctx = mp.get_context('fork')
    with ctx.Pool(nproc) as pool:
        res = dict(pool.map(work, [(k, Rr[k]['reduced_halfword'], nalt, restarts, budget) for k in todo], chunksize=1))
    for k, out in res.items():
        Rr[k]['stage3'] = out
        Rr[k]['status'] = out['status']
    json.dump(Rr, open(outp, 'w'))
    print('stage3 input', len(todo), 'status', dict(Counter(res[k]['status'] for k in res)), 'overall', dict(Counter(r['status'] for r in Rr)),
          'time', round(time.time() - t0, 1))
