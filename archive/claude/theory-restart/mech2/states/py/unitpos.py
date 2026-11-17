import sys, os, glob, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/scripts')
from bcube import *
from survey import N_from_chainfile, SI
rows = {}
for l in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl'):
    r = json.loads(l); rows[r['name']] = r
cnt = collections.Counter(); ex = collections.defaultdict(list)
for nm, r in sorted(rows.items()):
    if 'err' in r: continue
    half, orient, sym = read_kht(os.path.join(SI, nm + '.kht'))
    c = sum(1 for (l, i) in half if l in 'xy')
    wr = r['writhe']
    h0, d0 = 2 * c - 2 * wr, 2 * c - 4 * wr
    Npts = N_from_chainfile(os.path.join(SI, nm, 'cxBNr-c2-qs'))
    cube = sorted((h - r['hshift'], q - r['qshift']) for h, q in Npts)
    qs = [q for h, q in cube]
    M, m = r['top_M'], r['bot_M']
    inN = (h0, d0) in cube
    # absolute check: unit position in kht++ coordinates
    if d0 > M: key = 'unit above complex'
    elif d0 < m: key = 'unit below complex'
    elif d0 > max(qs): key = 'unit above N (inside complex range)'
    elif d0 < min(qs): key = 'unit below N (inside complex range)'
    elif d0 == max(qs): key = 'unit at top q of N' + (' (generator there)' if inN else ' (no generator at h0)')
    elif d0 == min(qs): key = 'unit at bottom q of N' + (' (generator there)' if inN else ' (no generator at h0)')
    else: key = 'unit strictly inside q-range of N' + (' (generator there)' if inN else ' (NO generator at unit position)')
    cnt[key] += 1; ex[key].append(nm)
    r['h0'] = h0; r['d0'] = d0
for k, v in sorted(cnt.items()):
    print('%4d  %s   e.g. %s' % (v, k, ex[k][:8]))
