"""critic: exact lp.J of the rebuilt engineA unit halfwords (sanity: the halfwords are the units), per-word time limit."""
import sys, json, time
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
from multiprocessing import Pool
def J(w):
    import lp
    t0 = time.time(); j = lp.J(w); return (j == {0: 1}, round(time.time() - t0, 2))
if __name__ == '__main__':
    items = json.load(open(sys.argv[1])); lim = float(sys.argv[2]); out = {}
    with Pool(3) as P:
        fut = [(t, w, P.apply_async(J, (w,))) for t, w in items]
        t0 = time.time()
        for t, w, f in fut:
            try:
                out[t] = f.get(timeout=max(1.0, lim - (time.time() - t0)) if lim > 0 else None)
            except Exception as e:
                out[t] = ('TIMEOUT/ERR', repr(e)[:60])
        P.terminate()
    json.dump(out, open(sys.argv[3], 'w'), indent=0)
    from collections import Counter
    print(Counter(str(v[0]) for v in out.values()))
