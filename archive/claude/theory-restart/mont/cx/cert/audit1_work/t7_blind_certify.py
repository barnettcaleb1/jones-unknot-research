"""AUDIT-1 test 7: certify() on the AUDITOR's own random knots (own grammar walker, incl. mid-word caps/cups, axis
crossings), blind mode (Tietze forced on every knot).  A CERTIFIED_UNKNOT on a knot with V_K != 1 (project bracket) would be
a false certification; every CERTIFIED_* must carry checker-accepted certificates; rep certificates are re-checked with
the strict pair condition (F1).  usage: t7_blind_certify.py SEED COUNT NPROC OUT.json"""
import sys, json, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit1_work')
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import audlib, certify, replay
from multiprocessing import Pool

def one(w):
    t0 = time.time()
    st, c = certify.certify(w, tietze_budget=3.0, rep_budget=15.0, blind=True, write_hits=False)
    V = replay.VK_project(w)
    rec = {'w': w, 'st': st, 'n': c.get('crossings'), 'V1': V == {0: 1}, 'kinds': [x['kind'] for x in c['certificates']],
           'secs': round(time.time() - t0, 2)}
    rec['recheck'] = all(replay.check(x)[0] for x in c['certificates'])
    for x in c['certificates']:
        if x['kind'] == 'rep':
            gens = replay.wirtinger_presentation(w)[0]
            rec['strict'] = (x['noncommuting'][0] in gens and x['noncommuting'][1] in gens)
    rec['FALSE_UNKNOT'] = (st == 'CERTIFIED_UNKNOT' and not rec['V1'])
    return rec

if __name__ == '__main__':
    seed, count, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); ws = []; seen = set()
    while len(ws) < count:
        w = audlib.rand_halfword(rnd, rnd.randint(4, 16), maxhw=rnd.choice([5, 7]))
        if w in seen or not audlib.is_knot(w) or not (8 <= audlib.ncross(w) <= 40): continue
        seen.add(w); ws.append(w)
        mw = w.replace('x', 'X').replace('y', 'x').replace('X', 'y')          # mirror image
        if mw not in seen and len(ws) < count: seen.add(mw); ws.append(mw)
    t0 = time.time()
    with Pool(nproc) as P:
        rows = P.map(one, ws, chunksize=1)
    from collections import Counter
    summ = {'knots': len(rows), 'status': dict(Counter(r['st'] for r in rows)),
            'status_V1': dict(Counter(r['st'] for r in rows if r['V1'])),
            'status_Vne1': dict(Counter(r['st'] for r in rows if not r['V1'])),
            'FALSE_UNKNOT': [r for r in rows if r['FALSE_UNKNOT']], 'recheck_all': all(r['recheck'] for r in rows),
            'rep_strict': dict(Counter(r.get('strict') for r in rows if 'strict' in r)),
            'n_range': (min(r['n'] for r in rows), max(r['n'] for r in rows)), 'wall': round(time.time() - t0, 1)}
    json.dump({'summary': summ, 'rows': rows}, open(outp, 'w'))
    print(json.dumps(summ))
