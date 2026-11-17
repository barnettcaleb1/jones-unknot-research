"""Stage 3 for residues still UNRESOLVED after stage 2 (PD): for each, try in order
  (T) pi_1 Tietze reduction (tietze.certify_multi: plat presentation read top-down and bottom-up, greedy + randomised) on the
      reduced halfword, then on the original halfword;
  (A) alternative diagrams of K (random isotopy walks from the reduced word: group rules + insertion of absorbable end patterns;
      residue_pd2.random_alt) with Tietze and the PD simplifier on each.
CERT_b_tietze: presentation reduced to <a | > (replayable: direction + elimination log, tietze.replay_dir).
usage: residue_stage3.py IN.json OUT.json NPROC NALT"""
import sys, json, random, time, multiprocessing as mp
from collections import Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import pd as PDm, vk, rules, tietze, tietze2
from residue_pd2 import random_alt
def word_of(hw):
    s = hw[len('s.l1.l1.'):-len('.u2.u2')] if hw != 's.l1.l1.u2.u2' else ''
    return rules.enc(s.split('.')) if s else ()
def hw_of(w): return 's.l1.l1.' + rules.dec(w) + '.u2.u2' if w else 's.l1.l1.u2.u2'
def work(args):
    k, r, nalt = args
    rnd = random.Random(k)
    for src in ('reduced_halfword', 'halfword'):
        ok, info = tietze2.certify2(r[src])
        if ok:
            g, rest = tietze2.replay2(r[src], info['direction'], info['log'])
            assert len(g) == 1 and not rest
            return k, {'status': 'CERT_b_tietze', 'tietze_version': 2, 'tietze_word': r[src], 'tietze_direction': info['direction'], 'tietze_log': info['log']}
    for src in ('reduced_halfword', 'halfword'):
        ok, info = tietze.certify_multi(r[src], tries=10, seed=k)
        if ok:
            g, rest = tietze.replay_dir(r[src], info['direction'], info['log'])
            assert len(g) == 1 and not rest
            return k, {'status': 'CERT_b_tietze', 'tietze_version': 1, 'tietze_word': r[src], 'tietze_direction': info['direction'], 'tietze_log': info['log']}
    w0 = word_of(r['reduced_halfword']); bestpd = None
    for a in range(nalt):
        w, wlog = random_alt(w0, rnd, rnd.randint(5, 60))
        hw = hw_of(w)
        ok, info = tietze2.certify2(hw)
        if ok:
            g, rest = tietze2.replay2(hw, info['direction'], info['log'])
            assert len(g) == 1 and not rest
            return k, {'status': 'CERT_b_tietze', 'tietze_version': 2, 'alt_word_log': wlog, 'tietze_word': hw, 'tietze_direction': info['direction'], 'tietze_log': info['log']}
        base = PDm.PD.from_halfword(hw)
        q = base.copy(); q.log = []
        b = q.simplify(random.Random(a), budget=300)
        if bestpd is None or b.n() < bestpd[0]: bestpd = (b.n(), hw, wlog, b.log)
        if b.n() <= 24:
            assert PDm.replay(hw, b.log) == b.n()
            if b.n() == 0: st = 'CERT_c_pd'
            else: st = 'CERT_a_pd_TS24' if vk.VK(hw) == {0: 1} else 'ALARM_V_ne_1'
            return k, {'status': st, 'alt_halfword': hw, 'alt_word_log': wlog, 'pd_best_crossings': b.n(), 'pd_log': b.log}
    return k, {'status': 'UNRESOLVED', 'best_pd_crossings_seen': bestpd[0] if bestpd else None}
if __name__ == '__main__':
    inp, outp, nproc, nalt = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    Rr = json.load(open(inp))
    todo = [k for k, r in enumerate(Rr) if r['status'] == 'UNRESOLVED']
    t0 = time.time()
    ctx = mp.get_context('fork')
    with ctx.Pool(nproc) as pool:
        res = dict(pool.map(work, [(k, Rr[k], nalt) for k in todo], chunksize=8))
    for k, out in res.items():
        Rr[k]['stage3'] = out; Rr[k]['status'] = out['status']
    json.dump(Rr, open(outp, 'w'))
    print('stage3 input', len(todo), 'status', dict(Counter(res[k]['status'] for k in res)), 'overall', dict(Counter(r['status'] for r in Rr)),
          'time', round(time.time() - t0, 1), flush=True)
