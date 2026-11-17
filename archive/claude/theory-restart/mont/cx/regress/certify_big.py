"""(b)-certify the base knots with > 24 crossings (isotopy-PROVED lines): Wirtinger + Tietze (tietze.py), replayed.
usage: certify_big.py NPROC"""
import sys, pickle, json, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
def job(words):
    import tietze, signal
    res = []
    for W in words:
        hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
        t0 = time.time()
        try:
            n, rels = tietze.wirtinger(hw)
            steps = []
            gens, rr = tietze.simplify(n, rels, steps, maxgens_wh=4)
            ok = (len(gens) <= 1 and not rr)
            rep = tietze.replay(hw, steps) if ok else False
            res.append((hw, ok and rep, len(steps), round(time.time() - t0, 2), None if ok else (len(gens), [len(r) for r in rr][:4])))
        except Exception as e:
            res.append((hw, False, 0, 0, repr(e)))
    return res
if __name__ == '__main__':
    import multiprocessing as mp
    nproc = int(sys.argv[1])
    big = pickle.load(open(OUT + 'big_bases.pkl', 'rb'))
    words = sorted(set(w for D in big for w in big[D]), key=len)
    print('distinct big base words', len(words), flush=True)
    chunks = [words[k::nproc * 4] for k in range(nproc * 4)]
    t0 = time.time()
    with mp.get_context('spawn').Pool(nproc) as pool:
        rr = pool.map(job, chunks)
    res = [x for r in rr for x in r]
    ok = [x for x in res if x[1]]
    print('certified <a|> (replayed):', len(ok), 'of', len(res), 'time', round(time.time() - t0, 1), flush=True)
    json.dump(res, open(OUT + 'certify_big.json', 'w'))
    for x in [x for x in res if not x[1]][:10]: print('NOT certified:', x)
