"""[cert/run copy of audit1_work/t5_saved_certs.py: uses the FIXED checker run/code/replay.py] AUDIT-1 test 5: re-check the SAVED certificates in cert/out with replay.check, plus the auditor's extra condition for
'rep' certificates (finding F1): the noncommuting pair must consist of Wirtinger generators and the image keys must be
exactly the generators.  Tietze certificates: all of them in the suites, a random sample from the bulk files.
usage: t5_saved_certs.py NPROC SAMPLE_PER_BULK OUT.json"""
import sys, json, gzip, glob, random, time, os
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/code')
import replay
from multiprocessing import Pool
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/out'

def certs_of(rec):
    """yield (status, cert) pairs from a stored record of any of the formats"""
    if 'kind' in rec and 'halfword' in rec:                  # bare certificate (mitm77 tietze file)
        yield ('CERTIFIED_UNKNOT', rec); return
    if 'certificates' in rec:                                 # certify() info dict (mitm77 FULL path)
        for c in rec['certificates']: yield (None, c)
        return
    st = rec.get('status')
    c = rec.get('cert')
    if isinstance(c, dict):
        if 'certificates' in c:
            for cc in c['certificates']: yield (st, cc)
        elif 'kind' in c:
            yield (st, c)

def strict_rep(c):
    P = replay.wirtinger_presentation(c['halfword'])
    if P is None: return False, 'no presentation'
    gens = P[0]
    g, h = c['noncommuting']
    keys = sorted(int(k) for k in c['images'])
    return (g in gens and h in gens and g != h and keys == sorted(gens)), (g, h, len(keys), len(gens))

def check_one(item):
    src, st, c = item
    ok, msg = replay.check(c)
    out = {'src': src, 'st': st, 'kind': c.get('kind'), 'ok': ok}
    if c.get('kind') == 'rep':
        s, info = strict_rep(c); out['strict'] = s
    if not ok: out['msg'] = msg; out['w'] = c.get('halfword')
    return out

if __name__ == '__main__':
    nproc, samp, outp = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rnd = random.Random(5)
    items = []; counts = {}
    files = sorted(glob.glob(OUT + '/v3/*.jsonl')) + sorted(glob.glob(OUT + '/*.jsonl'))
    gzs = sorted(glob.glob(OUT + '/*.jsonl.gz'))
    for f in files:
        for line in open(f):
            rec = json.loads(line)
            for st, c in certs_of(rec):
                counts[(os.path.basename(f), c.get('kind'))] = counts.get((os.path.basename(f), c.get('kind')), 0) + 1
                items.append((os.path.basename(f), st, c))
    for f in gzs:
        allc = []
        with gzip.open(f, 'rt') as fh:
            for line in fh:
                rec = json.loads(line)
                for st, c in certs_of(rec):
                    counts[(os.path.basename(f), c.get('kind'))] = counts.get((os.path.basename(f), c.get('kind')), 0) + 1
                    allc.append((os.path.basename(f), st, c))
        reps = [x for x in allc if x[2].get('kind') == 'rep']
        others = [x for x in allc if x[2].get('kind') != 'rep']
        items += reps + (rnd.sample(others, samp) if len(others) > samp else others)
    for f in [OUT + '/mitm77_recert_37.json', OUT + '/bulk_top_d8_recert_1.json']:
        d = json.load(open(f))
        recs = d if isinstance(d, list) else d.get('rows', d.get('records', [d]))
        for rec in recs:
            if isinstance(rec, dict):
                for st, c in certs_of(rec): items.append((os.path.basename(f), st, c))
    t0 = time.time()
    with Pool(nproc) as P:
        res = P.map(check_one, items, chunksize=16)
    from collections import Counter
    acc = Counter((r['kind'], r['ok']) for r in res)
    rep_strict = Counter(r.get('strict') for r in res if r['kind'] == 'rep')
    summ = {'items_checked': len(res), 'accepted_by_kind': {'%s:%s' % k: v for k, v in acc.items()},
            'rep_strict_pair_in_gens': {str(k): v for k, v in rep_strict.items()},
            'rejected': [r for r in res if not r['ok']][:20],
            'stored_counts': {'%s|%s' % k: v for k, v in sorted(counts.items())}, 'secs': round(time.time() - t0, 1)}
    json.dump(summ, open(outp, 'w'), indent=1)
    print(json.dumps({k: summ[k] for k in ('items_checked', 'accepted_by_kind', 'rep_strict_pair_in_gens', 'secs')}))
    print('rejected:', summ['rejected'][:5])
