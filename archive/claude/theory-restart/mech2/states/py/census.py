import sys, os, glob, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
from badblocks import bad_blocks, SI
rows = {}
for l in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl'):
    r = json.loads(l); rows[r['name']] = r
names = sorted(os.path.basename(f)[:-4] for f in glob.glob(SI + '/*.kht'))
cnt = collections.Counter(); lists = collections.defaultdict(list)
dist = collections.Counter()
viol = []
for nm in names:
    half, orient, sym = read_kht(os.path.join(SI, nm + '.kht'))
    nb = {}
    for end in (1, 0):
        blocks, nc = bad_blocks(half, end)
        nb[end] = sum(1 for b in blocks if b['nbad'])
        # twin structure check: every bad block has exactly 2 bad chords
        for b in blocks:
            if b['nbad'] not in (0, 2):
                viol.append((nm, end, b))
    dist[(nb[1], nb[0])] += 1
    key = ('T' if nb[1] == 0 else '-') + ('B' if nb[0] == 0 else '-')
    cnt[key] += 1; lists[key].append(nm)
    r = rows.get(nm)
    if r and 'err' not in r:
        # cross-check with kht++: adequate <=> gap 0 and N top one-dimensional at h = n
        if (nb[1] == 0) != (r['top_gap'] == 0) or (nb[0] == 0) != (r['bot_gap'] == 0):
            print('MISMATCH', nm, nb, r['top_gap'], r['bot_gap'])
        if nb[1] == 0 and r['N_top'] != [r['ncr']]: print('TOP not at corner', nm, r['N_top'])
        if nb[0] == 0 and r['N_bot'] != [0]: print('BOT not at corner', nm, r['N_bot'])
        # |E| = 4^nbad
        if r['top_nE'] != 4 ** nb[1] or r['bot_nE'] != 4 ** nb[0]:
            print('nE mismatch', nm, nb, r['top_nE'], r['bot_nE'])
print('total', len(names))
print('adequate at top and bottom:', cnt['TB'], lists['TB'])
print('adequate at top only:', cnt['T-'], lists['T-'])
print('adequate at bottom only:', cnt['-B'], lists['-B'])
print('adequate at neither end:', cnt['--'])
print('violations of twin structure:', viol[:5])
print('distribution of (bad blocks at 1-end, at 0-end):', sorted(dist.items()))
