"""Exact lp.J of every U5 unit halfword (independent of engineA's vector calculus), per-word time limit."""
import sys, json, signal, time
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp
from multiprocessing import Pool
LIM = int(sys.argv[3]) if len(sys.argv) > 3 else 20
class TO(Exception): pass
def h(s, f): raise TO()
def one(item):
    tag, w = item
    signal.signal(signal.SIGALRM, h); signal.alarm(LIM)
    t0 = time.time()
    try:
        J = lp.J(w); r = 'J=1' if J == {0: 1} else 'J!=1 %r' % (sorted(J.items()) if J else J)
    except TO: r = 'timeout'
    except Exception as e: r = 'error %r' % (e,)
    finally: signal.alarm(0)
    return {'tag': tag, 'w': w, 'r': r, 'secs': round(time.time() - t0, 2)}
if __name__ == '__main__':
    L = json.load(open(sys.argv[1]))
    with Pool(2) as P: res = P.map(one, L, chunksize=4)
    from collections import Counter
    c = Counter(x['r'] if not x['r'].startswith('J!=1') else 'J!=1' for x in res)
    json.dump({'counts': dict(c), 'nonone': [x for x in res if x['r'].startswith('J!=1')], 'records': res}, open(sys.argv[2], 'w'))
    print(sys.argv[1], dict(c))
