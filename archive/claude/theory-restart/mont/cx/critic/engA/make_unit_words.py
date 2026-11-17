"""critic: rebuild every unit stored by engineA (e1_L0.pkl: R(8) single-child roots; e2_test.pkl: two-child test run)
as explicit halfwords (engineA's own tree->halfword dictionary vc.hw / vc.vert_word, imported read-only), recompute the
exact J with lp.J, and write [tag, halfword] pairs for the certifier.  Nothing in engineA is written."""
import sys, pickle, json
sys.dont_write_bytecode = True
EA = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'
sys.path.insert(0, EA); sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import vc, lp
from collections import Counter

def e1_word(u):
    kind, par, N, T = u[0], u[1], u[2], u[3]
    if kind == 'H':
        kids = [T] + ([('w', ('Y' if N > 0 else 'y') * abs(N))] if N else [])
        return vc.hw(('n', -par, kids))
    body = vc.word(('p', [T] + ([('w', ('Y' if N > 0 else 'y') * abs(N))] if N else [])))
    return vc.vert_word(par, body)

def e2_word(u):
    mu, N, T1, T2 = u[:4]
    kids = [T1, T2] + ([('w', ('Y' if N > 0 else 'y') * abs(N))] if N else [])
    return vc.hw(('n', -mu, kids))

out = []; stats = Counter()
r1 = pickle.load(open(EA + '/e1_L0.pkl', 'rb'))
for i, u in enumerate(r1['units']):
    w = e1_word(u)
    stats[('e1_L0', u[0])] += 1
    out.append(['e1_L0:%d:%s:%s:%s' % (i, u[0], u[1], u[2]), w])
r2 = pickle.load(open(EA + '/e2_test.pkl', 'rb'))
for i, u in enumerate(r2['units']):
    w = e2_word(u)
    stats[('e2_test', 'H')] += 1
    out.append(['e2_test:%d:mu=%s:N=%s:%s/%s' % (i, u[0], u[1], u[4], u[5]), w])
json.dump(out, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/engA/unit_words.json', 'w'))
print(dict(stats)); print('words', len(out), 'distinct', len(set(w for _, w in out)))
lens = [len(w.split('.')) for _, w in out]; print('letters min/max', min(lens), max(lens))
for t, w in out[:3] + out[142:146]: print(t, w)
