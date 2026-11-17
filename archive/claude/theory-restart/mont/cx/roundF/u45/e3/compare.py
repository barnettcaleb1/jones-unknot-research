"""Compare a rerun's output with engineB's stored output (all original fields; records compared on the original's keys)."""
import sys, json
O = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/'
D = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/out/'
def strip(x, keys):
    return {k: x.get(k) for k in keys}
res = {}
for run in sys.argv[1:]:
    a = json.load(open(O + run + '.json')); b = json.load(open(D + run + '.json'))
    diff = []
    for k, v in a.items():
        if k == 'secs': continue
        w = b.get(k)
        if isinstance(v, list) and v and isinstance(v[0], dict):
            if len(v) != len(w) or any(strip(y, x.keys()) != x for x, y in zip(v, w)): diff.append(k)
        elif v != w: diff.append(k)
    res[run] = 'IDENTICAL' if not diff else 'DIFFER in %s' % diff
    print(run, res[run], '| evals', a['evals'], b['evals'])
