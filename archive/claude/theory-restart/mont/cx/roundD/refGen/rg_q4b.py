"""Q4 restart, incremental: 200 random BOTH boxes (same seed as rg_q4_boxes.py).
 mode 'wit':  own B-data from vc.vec == C1 key; own generator verdict; C1 witnesses regenerated + exact re-check (fast)
 mode 'vec':  independent vector from two raw lp.J closures == vc.vec up to a unit (slow)"""
import sys, pickle, random, time, os
from multiprocessing import Pool
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_gen as G
import rg_q4_boxes as Q4
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
C1 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1'
def pick200():
    Gr = pickle.load(open(C1 + '/gen2_res.pkl', 'rb'))
    sigs = Gr['sigs']; resV = Gr['resV']; resH = Gr['resH']
    both = [k for k in sigs if resV[k][0] and all(not v for v in resH[k].values())]
    pool_x = [(x, k) for k in both for x in sigs[k]]
    random.seed(20261117)
    pick = random.sample(pool_x, 200)
    return [(x, Gr['trees'][x], k, Gr['tags'][x]) for x, k in pick]
def wjob(arg):
    x, T, key, tag = arg
    sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
    import vc
    a, b = vc.vec(T)
    Bd, sg, dl, lcok, spa = G.bdata_from_vec(a, b)
    r = dict(x=x, tag=tag, key_match=((Bd['top'], Bd['bot'], sg, dl) == key) and lcok and spa >= 1)
    r.update(Q4.verify_sig(Bd, sg, dl, 1))
    return r
def vjob(arg):
    x, T, key, tag = arg
    sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
    import vc, rg_vecJ as VJ
    t0 = time.time()
    v = vc.vec(T); w = VJ.vec_from_J(vc.word(T))
    return dict(x=x, tag=tag, ok=(w is not None and VJ.same_up_to_unit(v, w)), t=time.time() - t0)
def init(): G.load_gtab(RG + 'rg_gtab.pkl')
if __name__ == '__main__':
    mode = sys.argv[1]; nj = int(sys.argv[2])
    items = pick200()
    fn = RG + ('rg_q4b_wit.pkl' if mode == 'wit' else 'rg_q4b_vec.pkl')
    done = pickle.load(open(fn, 'rb')) if os.path.exists(fn) else []
    seen = set(r['x'] for r in done)
    todo = [it for it in items if it[0] not in seen]
    t0 = time.time()
    with Pool(nj, initializer=init) as P:
        for i, r in enumerate(P.imap_unordered(wjob if mode == 'wit' else vjob, todo)):
            done.append(r)
            pickle.dump(done, open(fn, 'wb'))
            if (i + 1) % 10 == 0: print('  %d/%d (%.0fs)' % (len(done), len(items), time.time() - t0), flush=True)
    if mode == 'wit':
        print('boxes', len(done), '| own key == C1 key', sum(r['key_match'] for r in done),
              '| own generator proves all classes', sum(1 for r in done if not r['mine_open']),
              '| C1 witnesses', sum(r['nwit'] for r in done), 'exact OK', sum(r['wit_ok'] for r in done),
              'FAILED', sum(r['nbad'] for r in done), '| rows differ', sum(r['rows_diff'] for r in done),
              '| C1 none', sum(r['c1_none'] for r in done))
    else:
        print('boxes', len(done), '| lp.J-closure vector == vc.vec up to unit:', sum(r['ok'] for r in done),
              '| by tag', {t: sum(1 for r in done if r['tag'] == t) for t in set(r['tag'] for r in done)})
