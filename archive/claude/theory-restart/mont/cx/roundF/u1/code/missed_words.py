"""missed_words.py -- the theta-curves engineB's (7,7) MITM never examined because of NON-GEOMETRIC bottom deduplication:
for every missed bottom class U' (geo_bfs.py: same projective rho_2 class as the MITM representative b, different tangle)
and every top class t with (t, b) a zeta_7 & zeta_10 survivor (cert/extract/data/s2_survivors_7_7.json = engineB's list),
the knot s.l1.l1.t.U'.u2.u2 has J(t.U') = unit * J(t.b) (exact projective equality, checked in geo_bfs.py), so it is a
J = 1 configuration whenever (t, b) is.  Writes the word list [[tag, halfword], ...] for cert_words.py; exact J is computed
there for every non-unknot result (an unknot needs no J); a sample is checked for J = 1 separately (j_sample.py).
usage: missed_words.py GEO_BFS.json OUT_WORDS.json"""
import sys, os, json
from collections import defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import rho2, lp
g = json.load(open(sys.argv[1]))
missed = [m for m in g['bottom']['missed'] if 'missed_word' in m]
by_rep = defaultdict(list)
for m in missed: by_rep[m['mitm_rep']].append(m['missed_word'])
surv = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s2_survivors_7_7.json'))['survivors']
tops_of = defaultdict(list)
for v, u in surv: tops_of[u].append(v)
items = []; stats = {'missed_classes': len(missed), 'reps_with_missed': len(by_rep), 'pairs': 0, 'not_knot': 0, 'J1': 0, 'J_not_1': 0}
jn1 = []
for b, Us in by_rep.items():
    for v in tops_of.get(b, []):
        for U in Us:
            W = [x for x in v.split('.') if x] + [x for x in U.split('.') if x]
            stats['pairs'] += 1
            if not rho2.is_knot('l1.l1', W, 'u2.u2'): stats['not_knot'] += 1; continue
            hw = rho2.halfword('l1.l1', W, 'u2.u2')
            items.append([{'top': v, 'missed_bottom': U, 'mitm_bottom': b}, hw])   # J computed by cert_words for non-unknots
stats['J_not_1_examples'] = jn1[:10]
json.dump(items, open(sys.argv[2], 'w'))
print(json.dumps(stats))
