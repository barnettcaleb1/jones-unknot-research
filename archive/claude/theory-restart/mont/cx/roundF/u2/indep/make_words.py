"""u2/indep/make_words.py -- member halfwords of every U2 family for the audited certifier:
lines: the points k = -2..2 of the line (unreduced words, the actual diagrams) + regress's base word (fewest crossings);
planes: the 3x3 grid (m,n) in {-1,0,1}^2 + the base word.  Output: [tag, halfword] list (tag = family id + point)."""
import json
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
def tw(m, n): return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def sp(s): return [a for a in s.split('.') if a]
def hw(W): return 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
fams = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/families.json'))
out = []; seen = set()
def add(tag, w):
    out.append([tag, w])
for f in fams:
    if not f['u2_target']: continue
    V, U = sp(f['V']), sp(f['U'])
    if f['kind'] == 'line':
        d = f['d']
        for k in range(-2, 3): add('%s|k=%d' % (f['fid'], k), hw(V + tw(f['m0'] + k * d[0], f['n0'] + k * d[1]) + U))
    else:
        for m in (-1, 0, 1):
            for n in (-1, 0, 1): add('%s|m=%d,n=%d' % (f['fid'], m, n), hw(V + tw(m, n) + U))
    add('%s|base' % f['fid'], f.get('base_hw') or hw(f['base_word']))
words = {}
for tag, w in out: words.setdefault(w, tag)
print('member points', len(out), 'distinct words', len(words))
json.dump([[t, w] for w, t in words.items()], open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/member_words.json', 'w'))
json.dump(out, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/member_points.json', 'w'))
