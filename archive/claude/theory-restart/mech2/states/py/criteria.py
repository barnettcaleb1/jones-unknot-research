import sys, os, glob, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
from badblocks import bad_blocks, SI
rows = {}
for l in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl'):
    r = json.loads(l); rows[r['name']] = r
names = sorted(os.path.basename(f)[:-4] for f in glob.glob(SI + '/*.kht'))
res = collections.Counter(); lst = collections.defaultdict(list)
for nm in names:
    half, orient, sym = read_kht(os.path.join(SI, nm + '.kht'))
    c = sum(1 for (l, i) in half if l in 'xy')
    wr, _ = half_writhe(half)
    n = 4 * c
    b1, k1 = bad_blocks(half, 1); b0, k0 = bad_blocks(half, 0)
    nb1 = sum(1 for b in b1 if b['nbad']); nb0 = sum(1 for b in b0 if b['nbad'])
    M, m = n + k1, -k0
    d0 = 2 * c - 4 * wr; h0 = 2 * c - 2 * wr
    # sanity versus the DP
    r = rows.get(nm)
    if r and 'err' not in r:
        assert r['top_M'] == M and r['bot_M'] == m, (nm, M, m, r['top_M'], r['bot_M'])
    why = []
    if d0 > M or d0 < m: why.append('A: unit outside the q-range of the cube')
    # B: top degree acyclic when not adequate => N lives in [m+2*[nb0>0], M-2*[nb1>0]]
    Mt = M - (2 if nb1 else 0); mt = m + (2 if nb0 else 0)
    if not why and (d0 > Mt or d0 < mt): why.append('B: unit outside after removing acyclic extreme degrees')
    if nb1 == 0 and d0 != M: why.append('C: adequate at the 1-end and unit not at the top corner')
    if nb0 == 0 and d0 != m: why.append('C: adequate at the 0-end and unit not at the bottom corner')
    key = 'settled' if why else 'open'
    res[key] += 1
    lst[key].append(nm)
    for w in why: res[w] += 1
print('half-diagrams:', len(names))
for k, v in sorted(res.items()): print('%4d  %s' % (v, k))
print('open:', lst['open'])
