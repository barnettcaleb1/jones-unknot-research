import sys, os, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khtparse import parse_page
root = sys.argv[1]
pages = sorted(glob.glob(root + '/2-bridge_knots/*.html')) + sorted(glob.glob(root + '/*.html'))
pages = [p for p in pages if not p.endswith('2-bridge_knots.html')]
allp = {}
for p in pages:
    name = os.path.basename(p)[:-5]
    try:
        allp[name] = parse_page(p)
    except Exception as e:
        print('FAIL', name, e)
print(len(allp), 'pages parsed')
from collections import Counter
optcount = Counter()
for name, pg in allp.items():
    for sec in ('BNr', 'Khr'):
        opts = [o for o in pg['sections'].get(sec, {}) if o.startswith('-c2')]
        optcount[(sec, tuple(opts))] += 1
        for o in opts:
            blk = pg['sections'][sec][o]
            if blk['unparsed']: print('UNPARSED', name, sec, o, blk['unparsed'][:2])
            if not blk['components']: print('EMPTY', name, sec, o)
for k, v in sorted(optcount.items(), key=lambda kv: -kv[1]): print(v, k)
json.dump(allp, open(sys.argv[2], 'w'), ensure_ascii=False)
