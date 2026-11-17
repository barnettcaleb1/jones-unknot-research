"""second pass on the bases certify_big.py could not reduce: more Whitehead effort (up to 5 generators), 60 s cap per word."""
import sys, json, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
class TO(Exception): pass
def job(words):
    import tietze, signal
    def h(s, f): raise TO()
    signal.signal(signal.SIGALRM, h)
    res = []
    for hw in words:
        t0 = time.time()
        try:
            signal.alarm(20)
            n, rels = tietze.wirtinger(hw); steps = []
            gens, rr = tietze.simplify(n, rels, steps, maxgens_wh=5, max_aut=400, max_total=8000)
            signal.alarm(0)
            ok = (len(gens) <= 1 and not rr)
            rep = tietze.replay(hw, steps) if ok else False
            res.append((hw, ok and rep, len(steps), round(time.time() - t0, 2), None if ok else (len(gens), [len(r) for r in rr][:4])))
        except TO:
            res.append((hw, False, 0, 20, "timeout"))
    return res
if __name__ == '__main__':
    import multiprocessing as mp
    nproc = int(sys.argv[1])
    prev = json.load(open(OUT + 'certify_big.json'))
    words = [x[0] for x in prev if not x[1]]
    print('second pass on', len(words), flush=True)
    chunks = [words[k::nproc * 3] for k in range(nproc * 3)]
    t0 = time.time()
    with mp.get_context('spawn').Pool(nproc) as pool: rr = pool.map(job, chunks)
    res = [x for r in rr for x in r]
    print('certified <a|> (replayed):', sum(1 for x in res if x[1]), 'of', len(res), 'time', round(time.time() - t0, 1), flush=True)
    json.dump(res, open(OUT + 'certify_big2.json', 'w'))
