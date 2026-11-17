import sys, os, json, collections
from fractions import Fraction as Fr
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/scripts')
from bcube import *
from survey import N_from_chainfile, SI
rows = {}
for l in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl'):
    r = json.loads(l); rows[r['name']] = r
viol = []; slopes = collections.Counter(); h0pts = collections.Counter()
tot = 0; nt = 0
allrel = {}
for nm, r in sorted(rows.items()):
    if 'err' in r: continue
    half, orient, sym = read_kht(os.path.join(SI, nm + '.kht'))
    c = sum(1 for (l, i) in half if l in 'xy'); wr = r['writhe']
    U = (2 * c - 2 * wr, 2 * c - 4 * wr)
    Npts = N_from_chainfile(os.path.join(SI, nm, 'cxBNr-c2-qs'))
    rel = sorted((h - r['hshift'] - U[0], q - r['qshift'] - U[1]) for h, q in Npts)
    allrel[nm] = rel
    nt += 1
    for h, q in rel:
        tot += 1
        if h == 0:
            h0pts[q] += 1
            if q != 0: viol.append((nm, h, q))
        else:
            s = Fr(q, h); slopes[s] += 1
            if not (1 <= s <= 2): viol.append((nm, h, q))
print('tangles', nt, 'generators', tot)
print('generators with h = 0 by q:', dict(h0pts))
print('slope q/h distribution (h != 0): min', min(slopes), 'max', max(slopes))
print('  slopes < 4/3:', sorted((str(s), n) for s, n in slopes.items() if s < Fr(4, 3)))
print('violations of the cone 1 <= q/h <= 2:', viol[:20], len(viol))
json.dump(allrel, open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/N_rel_unit.json', 'w'))
