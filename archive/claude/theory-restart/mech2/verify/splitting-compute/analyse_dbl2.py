#!/usr/bin/env python3
"""Part 2 for doubles: all doubles with stored data.  N from stored cxBNr-c2-d (my parser), cross-checked with gtilde jset on doubles.jsonl;
Kh~(K) from my own kht++ run of the knot word (examples/dblk/); writhe/lk from my own doubled word."""
import json, os, sys, collections, subprocess
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import gtilde
from chain import b_generators, kh_of_knot
from analyse import poly_l, pmulc, refinement, jones_from_kh
from doubles import read_kht, double_word, kht_orient
from morse import parse, unparse, Trace, jones_11
DBL = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots'
KHT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
os.makedirs('examples/dblk', exist_ok=True)
recs = [json.loads(l) for l in open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/doubles.jsonl')]
n_ok = 0
for r in recs:
    nm = r['knot']
    if 'khr' not in r:
        print('  %-7s no data (%s)' % (nm, r.get('error'))); continue
    path = os.path.join(DBL, nm, 'cxBNr-c2-d')
    n = b_generators(path)
    js = gtilde.jset(r['khr']) if gtilde.valid(r['khr']) else None
    jmatch = (js is not None and sorted((q // 2 - d, q) for q, d in js[2]) == n)
    word, top = read_kht(os.path.join(DBL, nm + '.kht'))
    fn = 'examples/dblk/%s.kht' % nm
    if not os.path.exists('examples/dblk/%s/cxCKh-c2' % nm):
        open(fn, 'w').write('%% knot %s\n%s\n,%d\n' % (nm, word, top[0]))
        subprocess.run(['perl', '-e', 'alarm 120; exec @ARGV', KHT, '-c2', fn], stdin=subprocess.DEVNULL, stdout=open(fn[:-4] + '.log', 'w'), stderr=subprocess.STDOUT)
    kk = kh_of_knot('examples/dblk/%s/cxCKh-c2' % nm)
    jk, wk = jones_11(parse(word))
    assert jones_from_kh(kk) == sorted(jk.items()), nm
    # linking number of T_K(0) from my doubled word
    dw, w = double_word(word, top)
    ev = dw + [('u', 0)]
    tr = Trace(ev, 1, close11=True); tr.orient = kht_orient(ev, tr, top)
    c_open = tr.comp[0]; c_closed = [c for c in tr.components() if c != c_open][0]
    lk2 = tr.linking2(c_open, c_closed)
    PN = poly_l(n); W = pmulc(poly_l(kk), poly_l(kk))
    good, divisible = refinement(PN, W)
    ok = (len(n) >= len(kk) ** 2 and len(good) == 1 and good[0][0] == -lk2)
    n_ok += ok
    print('  %-7s dim N = %3d (gtilde jset agrees: %s)  rk Kh~(K) = %2d  square = %3d  admissible c = %s  2lk = %d  R = %s  %s'
          % (nm, len(n), jmatch, len(kk), len(kk) ** 2, [c for c, R in good], lk2, [sorted(R.items()) for c, R in good], 'OK' if ok else 'PROBLEM'))
print('doubles with data passing all checks:', n_ok)
