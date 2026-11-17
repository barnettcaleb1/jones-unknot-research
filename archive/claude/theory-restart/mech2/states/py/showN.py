import sys, os, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/scripts')
from bcube import *
from survey import N_from_chainfile, SI
from badblocks import describe
from family import hull
rows = {}
for l in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl'):
    r = json.loads(l); rows[r['name']] = r
for nm in sys.argv[1:]:
    r = rows[nm]
    half, orient, sym = read_kht(os.path.join(SI, nm + '.kht'))
    c = sum(1 for (l, i) in half if l in 'xy'); wr = r['writhe']
    U = (2 * c - 2 * wr, 2 * c - 4 * wr)
    Npts = N_from_chainfile(os.path.join(SI, nm, 'cxBNr-c2-qs'))
    rel = sorted((h - r['hshift'] - U[0], q - r['qshift'] - U[1]) for h, q in Npts)
    print('==', nm, r['half'], 'c=%d wr=%d' % (c, wr), 'U(cube)=', U, 'corners rel U: bottom (%d,%d) top (%d,%d)' % (-U[0], r['bot_M'] - U[1], r['ncr'] - U[0], r['top_M'] - U[1]))
    print('   N - U:', rel)
    print('   hull :', hull(rel))
    byq = collections.defaultdict(list)
    for h, q in rel: byq[q].append(h)
    print('   by q :', ' '.join('%d:%s' % (q, sorted(byq[q])) for q in sorted(byq)))
    print('   1-end:', describe(half, 1)[0]); print('   0-end:', describe(half, 0)[0])
