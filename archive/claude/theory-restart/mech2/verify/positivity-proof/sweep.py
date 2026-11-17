#!/usr/bin/env python3
"""Sweep the 138 half-diagrams (lit/kht/out/k138/examples/si/*.kht) with the referee code."""
import os, sys, glob, json, time
from ref import *

SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si'
files = sorted(glob.glob(os.path.join(SI, '*.kht')))
rows = []
fail = []
t00 = time.time()
for f in files:
    name = os.path.basename(f)[:-4]
    with open(f) as fh:
        lines = fh.read().split('\n')
    wordstr = lines[1].strip()
    try:
        r = analyse(wordstr)
    except Exception as e:
        fail.append((name, repr(e)))
        print('FAIL', name, wordstr, repr(e)); sys.stdout.flush()
        continue
    c = r['c']
    checks = {}
    checks['type_b_ends'] = (r['t1'] == 'b' and r['t0'] == 'b')
    checks['M=4c+k1'] = (r['M'] == 4 * c + r['k1'])
    checks['m=-k0'] = (r['m'] == -r['k0'])
    checks['closure=q^2c'] = (r['closure'] == {2 * c: 1})
    v, d = r['Jcong']
    checks['Jcong'] = (abs(v - 1) < 1e-9 and abs(d) < 1e-9)
    for end in (1, 0):
        loop = r['loop%d' % end]; hp = r['hp%d' % end]
        word = parse_word(wordstr)
        okplaces = True
        for blk, places in loop.items():
            ch, i = word[blk]
            is_e = (ch == 'y') if end == 1 else (ch == 'x')
            if i == 0:
                exp = [0, 3]            # pass-by hook: twin chords are the two letters at position 0
                if is_e: okplaces = False   # a cut hook must have no loop chord
            else:
                exp = [1, 2] if is_e else [0, 3]
            if sorted(places) != exp:
                okplaces = False
        checks['twin_places_%d' % end] = okplaces
        checks['hp_bad=direct_%d' % end] = (sorted(loop.keys()) == sorted(hp['bad']))
        checks['hp_k_%d' % end] = (hp['k_pred'] == (r['k1'] if end == 1 else r['k0']))
        checks['alpha_beta_%d' % end] = hp['alpha_beta_ok']
        nb = len(loop)
        checks['E=4^bad_%d' % end] = ((r['E1'] if end == 1 else r['E0']) == 4 ** nb)
        checks['regions_%d' % end] = (hp['regions'] == hp['arcs'] + hp['loops'] + 1 and hp['curves'] == hp['arcs'] + 2 * hp['loops'] + 1)
    row = dict(name=name, word=wordstr, c=c, c_axis=r['c_axis'], c_o=r['c_o'], wr=r['wr'], k1=r['k1'], k0=r['k0'], M=r['M'], m=r['m'],
               d0=r['d0'], E1=r['E1'], E0=r['E0'], bad1=sorted(r['loop1'].keys()), bad0=sorted(r['loop0'].keys()),
               loops1=r['hp1']['loops'], loops0=r['hp0']['loops'], arcs1=r['hp1']['arcs'], arcs0=r['hp0']['arcs'],
               cut1=r['hp1']['cut'], cut0=r['hp0']['cut'],
               alpha={str(k): v for k, v in r['alpha'].items()}, checks=checks)
    rows.append(row)
    bad = [k for k, v in checks.items() if not v]
    print('%-8s c=%d wr=%+d k1=%d k0=%d M=%d m=%d d0=%d E1=%d E0=%d  %s' % (name, c, r['wr'], r['k1'], r['k0'], r['M'], r['m'], r['d0'], r['E1'], r['E0'],
          'ALL OK' if not bad else 'FAILED: ' + ','.join(bad)))
    sys.stdout.flush()
with open('sweep.json', 'w') as fh:
    json.dump(rows, fh)
print('files', len(files), 'analysed', len(rows), 'exceptions', len(fail), 'time %.1f s' % (time.time() - t00))
allbad = [(r['name'], [k for k, v in r['checks'].items() if not v]) for r in rows if not all(r['checks'].values())]
print('rows with failed checks:', allbad)
