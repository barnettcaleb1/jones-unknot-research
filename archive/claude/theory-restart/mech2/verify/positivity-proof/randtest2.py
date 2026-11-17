#!/usr/bin/env python3
import random, sys, time
from randtest import *
seed = int(sys.argv[1]); N = int(sys.argv[2]); maxlen = int(sys.argv[3]); maxcr = int(sys.argv[4])
rng = random.Random(seed)
t0 = time.time()
stats = dict(tested=0, homog=0, g0=0, gpos=0, failed=0, maxc=0, maxg=0, general=0, adequate_homog_gpos=0, loops_pos=0)
seen = set(); tries = 0
out = open('randtest2_%d.log' % seed, 'w')
while stats['tested'] < N and tries < 500 * N:
    tries += 1
    shape = random_shape(rng, rng.randrange(3, maxlen), 7)
    mode = rng.choice(['neg', 'pos', 'rand'])
    word = realise(shape, rng, mode)
    if word is None: continue
    ws = wstr(word)
    if ws in seen: continue
    ncr = sum(1 for ch, i in word if ch in 'xy')
    if ncr < 3 or ncr > maxcr: continue
    seen.add(ws)
    try:
        r, fails, extra = check(ws)
    except Exception as e:
        fails = ['EXC ' + repr(e)]; r = dict(c=None, wr=None); extra = {}
    if extra and extra['g'] == 0 and rng.random() < 0.9:
        # keep only a tenth of the unknots in the statistics (they were checked all the same)
        if fails:
            print('FAIL', ws, fails)
        continue
    stats['tested'] += 1
    if extra:
        stats['homog'] += 1
        if extra['g'] == 0: stats['g0'] += 1
        else:
            stats['gpos'] += 1; stats['maxg'] = max(stats['maxg'], extra['g'])
            if extra['nb'] == 0: stats['adequate_homog_gpos'] += 1
            end = 1 if r['wr'] < 0 else 0
            if r['hp%d' % end]['loops'] > 0: stats['loops_pos'] += 1
    else:
        stats['general'] += 1
    if r['c']: stats['maxc'] = max(stats['maxc'], r['c'])
    if fails:
        stats['failed'] += 1
        print('FAIL', ws, fails); sys.stdout.flush()
    out.write('%s c=%s wr=%s %s %s\n' % (ws, r['c'], r['wr'], extra, fails))
out.close()
print('seed', seed, stats, 'time %.1f' % (time.time() - t0))
