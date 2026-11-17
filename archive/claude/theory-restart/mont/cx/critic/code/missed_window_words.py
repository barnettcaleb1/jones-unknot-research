"""missed_window_words.py -- window (S3a, (4,4) junctions, |m|,|n| <= 6) and unit-line (S3b, (6,6) junctions, 5 points per line)
configurations that engineB never examined because their bottom U' was merged (non-geometrically) into the class of the
representative U: for every S3a / S3b item (V, U, m, n) [cert/extract/data/s3{a,b}_items.json] whose U has missed classes U'
of depth <= 4 (S3a) / <= 6 (S3b) (geo_bfs.py), the theta-curve V.(x1x1)^m.(x3x3)^n.U' (same J up to a unit) is listed (J for non-unknots is computed by cert_words.py).  usage: missed_window_words.py GEO_BFS.json OUT_WORDS.json"""
import sys, json
from collections import defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import rho2, lp
g = json.load(open(sys.argv[1]))
missed = [m for m in g['bottom']['missed'] if 'missed_word' in m]
D = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/'
items = []; stats = {}
def twist(m, n):
    a = (['x1', 'x1'] * m) if m >= 0 else (['y1', 'y1'] * (-m))
    b = (['x3', 'x3'] * n) if n >= 0 else (['y3', 'y3'] * (-n))
    return a + b
for name, f, dmax in (('S3a', 's3a_items.json', 4), ('S3b', 's3b_items.json', 6)):
    by_rep = defaultdict(list)
    for m in missed:
        if m['depth'] <= dmax: by_rep[m['mitm_rep']].append(m['missed_word'])
    st = {'missed_classes_used': sum(len(v) for v in by_rep.values()), 'items_with_rep': 0, 'theta': 0, 'not_knot': 0, 'J1': 0, 'J_not_1': 0}
    seen = set()
    for W, prov in json.load(open(D + f))['items']:
        U = prov.get('U', '')
        if U not in by_rep: continue
        st['items_with_rep'] += 1
        V = [x for x in prov.get('V', '').split('.') if x]
        mid = twist(prov['m'], prov['n'])
        for U2 in by_rep[U]:
            Wl = V + mid + [x for x in U2.split('.') if x]
            key = '.'.join(Wl)
            if key in seen: continue
            seen.add(key); st['theta'] += 1
            if not rho2.is_knot('l1.l1', Wl, 'u2.u2'): st['not_knot'] += 1; continue
            hw = rho2.halfword('l1.l1', Wl, 'u2.u2')
            items.append([{'set': name, 'V': prov.get('V', ''), 'U_rep': U, 'U_missed': U2, 'm': prov['m'], 'n': prov['n']}, hw])
    stats[name] = st
json.dump(items, open(sys.argv[2], 'w'))
print(json.dumps(stats))
