"""AUDIT-1 test 2b: power of the hom-count comparison against SYSTEMATIC sign-rule bugs.  For each crossing class
(ty, od, ud) (8 classes) and for the unions 'all od=False', 'all ud=False', 'all y', the signs of replay's Wirtinger
relators in that class are flipped; the comparison with the auditor's plat counts must then FAIL on many knots, while
the unmodified presentation agrees everywhere (t2) and flipping ALL classes (= reflected diagram, mirror) must AGREE.
usage: t2b_sign_classes.py T2_ROWS.json NKNOTS NPROC OUT.json"""
import sys, json, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit1_work')
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import audlib, replay, alex
from multiprocessing import Pool

GS = None
def init():
    global GS
    GS = [g for g in audlib.groups() if g.name in ('S4', 'A4', 'A5', 'F20', 'F42')]

CLASSES = [(t, o, u) for t in 'xy' for o in (True, False) for u in (True, False)]
VARIANTS = [('class', c) for c in CLASSES] + [('od=F', None), ('ud=F', None), ('ty=y', None), ('ALL(mirror)', None)]

def flipped(R, cr, var):
    kind, c = var
    out = []
    for k, (o_, ov, i_, s) in enumerate(R):
        x = cr[k]; key = (x['ty'], x['od'], x['ud'])
        f = ((kind == 'class' and key == c) or (kind == 'od=F' and not x['od']) or (kind == 'ud=F' and not x['ud'])
             or (kind == 'ty=y' and x['ty'] == 'y') or kind == 'ALL(mirror)')
        out.append((o_, ov, i_, -s if f else s))
    return out

def one(w):
    full = alex.symmetrize(alex.parse(w))
    gens, rels = replay.wirtinger_presentation(w)
    cr = replay.knot_crossings(w)
    R = audlib.parse_wirt(gens, rels); n = len(gens)
    caps = 1 + sum(1 for c, i in full if c in 'lr')
    res = {}
    present = set((x['ty'], x['od'], x['ud']) for x in cr)
    for G in GS:
        for C in G.classes:
            if C == [G.e]: continue
            K, reps, sz = audlib.class_K(G, C)
            if len(K) ** (caps - 1) > 20000: continue
            tp = sz * sum(audlib.plat_count(full, G, K, r) for r in reps)
            for var in VARIANTS:
                if var[0] == 'class' and var[1] not in present: continue
                Rv = flipped(R, cr, var)
                tv = sz * sum(audlib.wirt_count(n, Rv, G, K, r) for r in reps)
                key = var[0] if var[1] is None else '%s%s%s' % (var[1][0], 'D' if var[1][1] else 'u', 'D' if var[1][2] else 'u')
                d = res.setdefault(key, [0, 0])
                d[0] += 1; d[1] += (tv != tp)
    return {'w': w, 'n': n, 'res': res}

if __name__ == '__main__':
    rowsf, nk, nproc, outp = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rows = json.load(open(rowsf))['rows']
    ws = [r['w'] for r in rows if r['nonab']][:nk]
    t0 = time.time()
    with Pool(nproc, initializer=init) as P:
        out = P.map(one, ws, chunksize=1)
    agg = {}
    for r in out:
        for k, (c, d) in r['res'].items():
            a = agg.setdefault(k, {'knots_with_class': 0, 'knots_detected': 0})
            a['knots_with_class'] += 1; a['knots_detected'] += (d > 0)
    summ = {'knots': len(out), 'variants': agg, 'secs': round(time.time() - t0, 1),
            'legend': 'class key = ty + od(D=along word,u=against) + ud; ALL(mirror) must have knots_detected = 0'}
    json.dump({'summary': summ, 'rows': out}, open(outp, 'w'))
    print(json.dumps(summ, indent=0))
