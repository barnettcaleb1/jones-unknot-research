"""affine_reduced_test.py -- the new Alexander-free affine search (reps.affine_rep_reduced, cert/run fix F3) on the suite (b)
nontrivial knots: certify() with EXACT_ALEX_MAX = 0 (so every knot uses the reduced search), default (non-blind) mode.
Every certificate must be accepted by the checker (certify only returns checker-accepted ones); reports the success rate.
usage: affine_reduced_test.py NPROC OUT.json"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import certify
from multiprocessing import Pool
def one(w):
    certify.EXACT_ALEX_MAX = 0
    t0 = time.time()
    st, info = certify.certify(w, write_hits=True, rep_budget=30.0)
    return {'w': w, 'st': st, 'n': info.get('crossings'), 'groups': [c.get('group') for c in info['certificates'] if c['kind'] == 'rep'],
            'secs': round(time.time() - t0, 3)}
if __name__ == '__main__':
    nproc, outp = int(sys.argv[1]), sys.argv[2]
    d = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/out/set_suiteB.json'))
    ws = []
    for k in ('alex_trivial', 'random_V_ne_1', 'random_mirrors'):
        ws += [x[1] if isinstance(x, list) else x for x in d[k]]
    t0 = time.time()
    with Pool(nproc) as P: rows = P.map(one, ws, chunksize=4)
    from collections import Counter
    st = Counter(r['st'] for r in rows); aff = sum(1 for r in rows if any(g and g.startswith('Aff') for g in r['groups']))
    secs = sorted(r['secs'] for r in rows)
    summ = {'knots': len(rows), 'status': dict(st), 'affine_reduced_certs': aff, 'secs_median_max': (secs[len(secs) // 2], secs[-1]),
            'wall': round(time.time() - t0, 1)}
    print(json.dumps(summ)); json.dump({'summary': summ, 'rows': rows}, open(outp, 'w'))
