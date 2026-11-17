#!/usr/bin/env python3
"""Check Theorem A against the saved chain files: for every component of every cxBNr-c2* file, classify the moves between consecutive
b-generators, test unit arrows, count composable junctions, and confirm: unit arrows => unit square (compact) or zigzag (arc)."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khparse import parse_file
from collections import Counter
ROOT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out'
B, C = '⬮', '⬯'
def moves(comp):
    """walk along the chain; return list of (kind, direction) between consecutive b-generators, kind = 'D^a' or 'P_n' or 'other', plus tails"""
    gens = comp['gens']; n = len(gens)
    arr = {}
    for (s, t, kind, p) in comp['arrows']:
        arr[(s, t)] = (kind, p, +1); arr[(t, s)] = (kind, p, -1)
    order = list(range(n)) + ([0] if comp['cyclic'] else [])
    bpos = [i for i in range(len(order)) if gens[order[i]][0] == B]
    out = []
    for a, b in zip(bpos, bpos[1:]):
        seg = [arr[(order[i], order[i + 1])] for i in range(a, b)]
        dirs = set(d for (_, _, d) in seg)
        labels = [(k, p) for (k, p, _) in seg]
        if len(seg) == 1 and labels[0][0] == 'D': out.append(('D^%d' % labels[0][1], seg[0][2]))
        elif len(seg) >= 3 and len(dirs) == 1 and labels[0] == ('S', 1) and labels[-1] == ('S', 1) and \
                all(l == (('D', 1) if i % 2 == 0 else ('S', 2)) for i, l in enumerate(labels[1:-1])):
            out.append(('P_%d' % ((len(seg) - 1) // 2), seg[0][2]))
        else: out.append(('other:' + str(labels), 0))
    return out
SUBS = sys.argv[1:] or ['k138', 'dbl', 'comp', 'tilt', 'alex1']
tot = Counter(); bad = []
files = []
for sub in SUBS:
    for dp, dn, fns in os.walk(os.path.join(ROOT, sub)):
        files += glob.glob(os.path.join(dp, 'cxBNr-c2*'))
for fn in sorted(set(files)):
    try: comps = parse_file(fn)
    except Exception as e: continue
    for comp in comps:
        if len(comp['gens']) == 1: continue
        mv = moves(comp)
        kinds = Counter(k for k, d in mv)
        unit = all(k in ('D^1', 'P_2') for k, d in mv)
        m = mv + ([mv[0]] if comp['cyclic'] else [])
        composable = sum(1 for (k1, d1), (k2, d2) in zip(m, m[1:]) if d1 == d2 and d1 != 0)
        typ = 'compact' if comp['cyclic'] else 'arc'
        tot[typ] += 1
        tot[typ + (' unit' if unit else ' nonunit')] += 1
        if unit:
            if comp['cyclic']:
                ok = (len(mv) == 4 and composable == 2 and sorted(k for k, d in mv) == ['D^1', 'D^1', 'P_2', 'P_2'])
            else:
                ok = (composable == 0)
            tot[typ + (' unit, as Theorem A' if ok else ' unit, VIOLATES Theorem A')] += 1
            if not ok: bad.append((fn, mv))
        else:
            tot[typ + ' nonunit: ' + ','.join(sorted(set(k for k, d in mv if k not in ('D^1', 'P_2'))))[:60]] += 1
            tot[typ + ' nonunit, composable junctions=%d' % composable] += 1
for k, v in sorted(tot.items()): print('%6d  %s' % (v, k))
print('violations:', bad[:5])
