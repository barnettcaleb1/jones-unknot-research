"""critic: 3x3 det grid {-1,0,1}^2 for every 2-parameter axis-free plane without a Lemma-K site (all 572 PLANE-with-R)."""
import sys, json
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
from multiprocessing import Pool
def tw(m, n): return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def job(x):
    import alex
    t, wt, wb = x
    V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]; ok = True
    for m in (-1, 0, 1):
        for n in (-1, 0, 1):
            W = V + tw(m, n) + U; hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
            v = alex.alex_eval(hw, -1); ok = ok and v is not None and abs(v) == 1
    return ok
if __name__ == '__main__':
    items = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/planes_need_grid.json'))
    with Pool(3) as P: res = P.map(job, items, chunksize=8)
    print('planes', len(items), 'det = 1 on the whole 3x3 grid:', sum(res))
