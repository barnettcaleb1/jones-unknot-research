"""Kill-robust task runner (written after the 04:33 incident in which another lane's `pkill -f multiprocessing.spawn` killed
all workers of rg_q4_boxes.py, rg_q5_closures.py, rg_q5_second.py; Pool.imap silently loses the tasks of dead workers).
 * ProcessPoolExecutor: a killed worker raises BrokenProcessPool instead of hanging; we restart on the REMAINING tasks.
 * every result is written atomically to its own file  <outdir>/<kind>_<key>.pkl  as soon as it completes;
 * on (re)start, tasks that already have a result file are skipped;  counts are taken ONLY from result files.
Task kinds:
   q4vec <x>    : box x of gen2_res.pkl: vector from two raw lp.J closures (rg_vecJ) == vc.vec(tree) up to a unit
   q5 <seed>    : rg_q5_closures.job_lpJ2((seed, fam)), fam = V if (seed-70000) even else H  (deterministic per seed)
Usage:  python rg_robust.py run <nworkers>       |   python rg_robust.py status"""
import sys, os, pickle, time, random
import concurrent.futures as cf
from concurrent.futures.process import BrokenProcessPool
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
C1 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1'
EA = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'
OUT = RG + 'rg_results/'
sys.path.insert(0, RG)

def q4_pick():
    """the SAME 200 boxes as rg_q4_boxes.py (seed 20261117)"""
    Gr = pickle.load(open(C1 + '/gen2_res.pkl', 'rb'))
    sigs = Gr['sigs']; resV = Gr['resV']; resH = Gr['resH']
    both = [k for k in sigs if resV[k][0] and all(not v for v in resH[k].values())]
    pool_x = [(x, k) for k in both for x in sigs[k]]
    assert len(pool_x) == 46771, len(pool_x)
    random.seed(20261117)
    return random.sample(pool_x, 200), Gr
def q5_fam(seed): return 'V' if (seed - 70000) % 2 == 0 else 'H'
def all_tasks():
    pick, Gr = q4_pick()
    return [('q4vec', x) for x, k in pick] + [('q5', s) for s in range(70000, 72000)]

_G = {}
def _gr():
    if 'Gr' not in _G: _G['Gr'] = pickle.load(open(C1 + '/gen2_res.pkl', 'rb'))
    return _G['Gr']
def t_q4vec(x):
    sys.path.insert(1, EA)
    import vc, rg_vecJ as VJ
    T = _gr()['trees'][x]
    t0 = time.time()
    v = vc.vec(T)
    w = VJ.vec_from_J(vc.word(T))
    return dict(x=x, vecJ=(w is not None and VJ.same_up_to_unit(v, w)), wNone=(w is None), t=time.time() - t0)
def t_q5(seed):
    import rg_q5_closures as Q
    return Q.job_lpJ2((seed, q5_fam(seed)))
def run_task(task):
    kind, key = task
    if kind == 'q4vec': return t_q4vec(key)
    if kind == 'q5': return t_q5(key)
    raise ValueError(kind)

def fname(task): return OUT + '%s_%s.pkl' % task
def save(task, res):
    tmp = fname(task) + '.tmp%d' % os.getpid()
    with open(tmp, 'wb') as f:
        pickle.dump((task, res), f)
    os.replace(tmp, fname(task))          # atomic
def load_all():
    out = {}
    for fn in os.listdir(OUT):
        if not fn.endswith('.pkl'): continue
        try:
            task, res = pickle.load(open(OUT + fn, 'rb'))
        except Exception:
            continue                      # unreadable -> treated as missing
        out[tuple(task)] = res
    return out

def import_old():
    """results saved by the killed runs (complete results, deterministic per seed)"""
    n = 0
    for fn in ('rg_q5_lpJ.pkl', 'rg_q5_lpJ_b.pkl'):
        if not os.path.exists(RG + fn): continue
        for r in pickle.load(open(RG + fn, 'rb')):
            task = ('q5', r['seed'])
            if not os.path.exists(fname(task)):
                r = dict(r); r['source'] = fn
                save(task, r); n += 1
    return n

def run(nworkers):
    os.makedirs(OUT, exist_ok=True)
    print('imported from killed runs:', import_old(), flush=True)
    tasks = all_tasks()
    restarts = 0; t0 = time.time()
    while True:
        done = load_all()
        rem = [t for t in tasks if t not in done]
        print('%s: %d/%d tasks have results, %d remaining (restarts %d)' % (
            time.strftime('%H:%M:%S'), len(tasks) - len(rem), len(tasks), len(rem), restarts), flush=True)
        if not rem: break
        try:
            with cf.ProcessPoolExecutor(max_workers=nworkers) as ex:
                futs = {ex.submit(run_task, t): t for t in rem}
                k = 0
                for f in cf.as_completed(futs):
                    t = futs[f]
                    res = f.result()          # raises BrokenProcessPool if a worker was killed
                    save(t, res); k += 1
                    if k % 50 == 0:
                        print('  +%d results this round, %.0fs' % (k, time.time() - t0), flush=True)
        except BrokenProcessPool as e:
            restarts += 1
            print('BrokenProcessPool (a worker died): %s -- restarting on remaining tasks' % e, flush=True)
            if restarts > 50: raise
            time.sleep(5)
    status()

def status():
    tasks = all_tasks()
    done = load_all()
    q4 = [done[t] for t in tasks if t[0] == 'q4vec' and t in done]
    q5 = [done[t] for t in tasks if t[0] == 'q5' and t in done]
    print('q4vec: %d/200 results; vector from lp.J closures == vc.vec up to unit: %d; lp.J returned None: %d' % (
        len(q4), sum(1 for r in q4 if r['vecJ'] is True), sum(1 for r in q4 if r.get('wNone'))))
    if q5:
        sj = [r['spanJ'] for r in q5 if r['spanJ'] is not None]
        print('q5: %d/2000 distinct closures; lp.J units %d; lp.J == vector calculus %d; J None %d; forced Lemma-W N %d; '
              'H %d; V %d; min span J %s' % (len(q5), sum(r['J_unit'] for r in q5), sum(r['agree'] for r in q5),
              sum(r['J_none'] for r in q5), sum(r['forced'] for r in q5), sum(r['fam'] == 'H' for r in q5),
              sum(r['fam'] == 'V' for r in q5), min(sj) if sj else None))
    missing = [t for t in tasks if t not in done]
    print('missing tasks:', len(missing), missing[:10])

if __name__ == '__main__':
    if sys.argv[1] == 'run': run(int(sys.argv[2]) if len(sys.argv) > 2 else 8)
    else: status()
