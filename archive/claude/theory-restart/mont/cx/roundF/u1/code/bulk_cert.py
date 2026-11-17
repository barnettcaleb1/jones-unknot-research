"""bulk_cert.py -- certify large families of expected unknots.
Lean path per word: PD -> Wirtinger -> tietze.simplify -> replay.check (independent).  Any word not certified this way
goes through the full certify.certify (Tietze with a long budget, jones24, representation search; COUNTEREXAMPLE ->
HIT file).  Every certificate is stored (gzip JSONL); unresolved words are retained in OUT.unresolved.json.
usage: bulk_cert.py SET.json KEY NPROC OUTPREFIX [tietze_budget]"""
import sys, json, time, gzip
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u1/code')
import diagram, wirtinger, tietze, replay, certify
from multiprocessing import Pool

TB = [5.0]

def one(w):
    t0 = time.time()
    pd = diagram.pd_from_halfword(w)
    if pd is None: return {'w': w, 'status': 'NOT_A_KNOT'}
    if pd.n == 0:       # [cert/run fix F4 audit-1] unknot0 accepted only through the checker
        cert = {'kind': 'unknot0', 'halfword': w}
        c_ok, msg = replay.check(cert)
        if c_ok:
            cert['checker'] = msg
            return {'w': w, 'status': 'CERTIFIED_UNKNOT', 'kind': 'unknot0', 'n': 0, 'secs': 0.0, 'cert': cert}
    g, r = wirtinger.wirtinger(pd)
    ok, moves, fin, st = tietze.simplify(g, r, seed=0, time_budget=TB[0])
    if ok:
        cert = {'kind': 'tietze', 'halfword': w, 'moves': [list(m) for m in moves]}
        c_ok, msg = replay.check(cert)
        if c_ok:
            return {'w': w, 'status': 'CERTIFIED_UNKNOT', 'kind': 'tietze', 'n': pd.n, 'nmoves': len(moves),
                    'secs': round(time.time() - t0, 3), 'cert': cert}
    stt, cert = certify.certify(w, tietze_budget=60.0, rep_budget=60.0, seed=1)
    return {'w': w, 'status': stt, 'kind': [c['kind'] for c in cert['certificates']], 'n': pd.n,
            'secs': round(time.time() - t0, 3), 'cert': cert, 'full': True}

def init(tb): TB[0] = tb

if __name__ == '__main__':
    setf, key, nproc, outp = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    tb = float(sys.argv[5]) if len(sys.argv) > 5 else 5.0
    d = json.load(open(setf))
    ws = d if isinstance(d, list) else d[key]
    ws = [x[1] if isinstance(x, list) else x for x in ws]
    t0 = time.time()
    from collections import Counter
    st = Counter(); unres = []; ns = Counter(); secs = []
    with Pool(nproc, initializer=init, initargs=(tb,)) as P, gzip.open(outp + '.jsonl.gz', 'wt') as f:
        for i, rec in enumerate(P.imap(one, ws, chunksize=8)):
            st[rec['status']] += 1
            if rec.get('n') is not None: ns[rec['n']] += 1
            if 'secs' in rec: secs.append(rec['secs'])
            if rec['status'] != 'CERTIFIED_UNKNOT': unres.append({k: v for k, v in rec.items() if k != 'cert'})
            f.write(json.dumps(rec) + '\n')
            if (i + 1) % 5000 == 0:
                print('progress', i + 1, dict(st), round(time.time() - t0, 1), flush=True)
    secs.sort()
    summ = {'set': setf, 'key': key, 'count': len(ws), 'status': dict(st), 'crossings': dict(sorted(ns.items())),
            'secs_median_max_total': (secs[len(secs) // 2], secs[-1], round(sum(secs), 1)) if secs else None,
            'wall': round(time.time() - t0, 1), 'full_path_used': len(unres)}
    json.dump(unres, open(outp + '.unresolved.json', 'w'))
    json.dump(summ, open(outp + '.summary.json', 'w'), indent=1)
    print(json.dumps(summ), flush=True)
