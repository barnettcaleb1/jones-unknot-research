"""line_points.py -- word list of points FAR along engineB's unit-valued lines (beyond the 5 certified points k = -2..2),
to probe whether J = 1 holds along the whole line (exact lp.J on a sample) and whether every point is an unknot.
usage: line_points.py KS(comma) NLINES(0=all) SEED OUT.json"""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import rho2
ks = [int(x) for x in sys.argv[1].split(',')]; nl = int(sys.argv[2]); seed = int(sys.argv[3])
d = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s3b_items.json'))['items']
lines = {}
for W, p in d:
    lines.setdefault((p['V'], p['U'], tuple(p['direction']), tuple(p['offset'])), True)
keys = sorted(lines)
if nl: keys = random.Random(seed).sample(keys, nl)
def blk(letter, k):
    inv = {'x1': 'y1', 'x3': 'y3'}
    return [letter] * (2 * k) if k >= 0 else [inv[letter]] * (-2 * k)
items = []
for V, U, dd, off in keys:
    for k in ks:
        m = off[0] + k * dd[0]; n = off[1] + k * dd[1]
        Wl = [x for x in V.split('.') if x] + blk('x1', m) + blk('x3', n) + [x for x in U.split('.') if x]
        if not rho2.is_knot('l1.l1', Wl, 'u2.u2'): continue
        items.append([{'V': V, 'U': U, 'direction': dd, 'offset': off, 'k': k, 'm': m, 'n': n}, rho2.halfword('l1.l1', Wl, 'u2.u2')])
json.dump(items, open(sys.argv[4], 'w')); print('points', len(items))
