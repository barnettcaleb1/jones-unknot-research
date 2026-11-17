"""verify_sample.py -- FRESH-PROCESS re-check of a random sample of stored certificates.
For every sampled record and every certificate in it:
  (1) replay.check  (the FIXED independent checker, run/code/replay.py: own Wirtinger presentation from alex.diagram);
  (2) audit-2's independent library (copied to run/code/a2lib_indep.py; imports only alex for the definition of K):
      tietze  -> a2lib.my_replay on a2lib's OWN Wirtinger presentation (own Morse sweep, own canonical form);
      jones24 -> a2lib's own crossing count (<= 24) and own Morse-sweep bracket (monomial <=> V_K = 1);
      unknot0 -> a2lib's own diagram has 0 crossings;
      rep     -> a2lib.check_rep on its own presentation + image keys exactly the generators + pair in generators.
A record passes iff its status is backed by a certificate that passes BOTH checks.
usage: verify_sample.py FRACTION SEED NPROC OUT.json FILE.jsonl.gz [...]"""
import sys, os, json, gzip, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import replay, a2lib_indep as A
from multiprocessing import Pool

def a2_check(c):
    w = c['halfword']; k = c['kind']
    full = A.full_of(w)
    if k == 'tietze':
        P = A.wirtinger_from_halfword(w)
        if P is None: return False, 'a2: no presentation'
        ok, msg, fin = A.my_replay(P[0], P[1], [tuple(m) for m in c['moves']])
        return ok, 'a2: ' + msg
    if k == 'jones24':
        D = A.morse_diagram(full)
        if D is None: return False, 'a2: not a knot'
        if D['n'] > 24: return False, 'a2: > 24 crossings'
        return A.jones_unit_test(A.bracket_full(full)), 'a2: %d crossings, bracket monomial' % D['n']
    if k == 'unknot0':
        D = A.morse_diagram(full)
        return (D is not None and D['n'] == 0), 'a2: crossing-free'
    if k == 'rep':
        P = A.wirtinger_from_halfword(w)
        if P is None: return False, 'a2: no presentation'
        imgs = {int(kk): tuple(v) for kk, v in c['images'].items()}
        if sorted(imgs) != sorted(P[0]): return False, 'a2: image keys != generators'
        pair = tuple(c['noncommuting'])
        if any(x not in P[0] for x in pair): return False, 'a2: pair not generators'
        return A.check_rep(P[0], P[1], imgs, c['degree'], pair)
    return False, 'a2: unknown kind'

def check_rec(rec):
    out = {'w': rec['w'], 'status': rec['status'], 'certs': []}
    good_unknot = False; good_rep = False
    for c in rec.get('certificates') or []:
        r1 = replay.check(c)
        try: r2 = a2_check(c)
        except Exception as e: r2 = (False, 'a2 exception %r' % (e,))
        out['certs'].append({'kind': c['kind'], 'replay': r1[0], 'a2': bool(r2[0]), 'msg': (r1[1][:80], str(r2[1])[:80])})
        if r1[0] and r2[0]:
            if c['kind'] in ('tietze', 'jones24', 'unknot0'): good_unknot = True
            if c['kind'] == 'rep': good_rep = True
    st = rec['status']
    out['pass'] = (good_unknot if st == 'CERTIFIED_UNKNOT' else good_rep if st in ('CERTIFIED_NONTRIVIAL', 'COUNTEREXAMPLE') else True)
    return out

if __name__ == '__main__':
    frac, seed, nproc, outp = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = random.Random(seed)
    sample = []; total = 0
    for f in sys.argv[5:]:
        with gzip.open(f, 'rt') as fh:
            for line in fh:
                total += 1
                if rng.random() < frac: sample.append(json.loads(line))
    t0 = time.time()
    with Pool(nproc) as P: res = P.map(check_rec, sample, chunksize=4)
    from collections import Counter
    kinds = Counter((c['kind'], c['replay'], c['a2']) for r in res for c in r['certs'])
    summ = {'files': sys.argv[5:], 'records_total': total, 'sampled': len(res), 'fraction': frac, 'seed': seed,
            'records_pass': sum(1 for r in res if r['pass']), 'records_FAIL': [r for r in res if not r['pass']][:20],
            'certs_by_kind_replay_a2': {'%s|replay=%s|a2=%s' % k: v for k, v in kinds.items()},
            'status': dict(Counter(r['status'] for r in res)), 'secs': round(time.time() - t0, 1)}
    json.dump(summ, open(outp, 'w'), indent=1)
    print(json.dumps({k: v for k, v in summ.items() if k != 'records_FAIL'}), 'FAILS:', len([r for r in res if not r['pass']]))
