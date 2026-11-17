"""suites.py -- validation suites (a) unknots, (b) nontrivial knots, (c) timing.
usage: suites.py SET.json KEY LABEL NPROC OUTPREFIX [tietze_budget] [rep_budget] [blind]
  SET.json: a JSON list of halfwords, or a dict whose entry KEY is such a list (or a list of [m, word] pairs).
Writes OUTPREFIX.jsonl (one record per word, full certificate) and OUTPREFIX.summary.json."""
import sys, json, time, os
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/code')
import certify
from multiprocessing import Pool

ARGS = {}

def run_one(w):
    t0 = time.time()
    try:
        st, cert = certify.certify(w, tietze_budget=ARGS.get('tb'), rep_budget=ARGS.get('rb', 30.0), blind=ARGS.get('blind', False))
    except Exception as e:
        return {'w': w, 'status': 'ERROR', 'err': repr(e)}
    kinds = [c['kind'] for c in cert['certificates']]
    rec = {'w': w, 'status': st, 'kinds': kinds, 'n': cert.get('crossings'), 'V1': cert.get('V_K') == [(0, 1)],
           'A1': cert.get('Delta') == [(0, 1)], 'secs': round(time.time() - t0, 3), 'tietze': cert.get('tietze'),
           'groups': [c.get('group') for c in cert['certificates'] if c['kind'] == 'rep'], 'notes': cert.get('notes'),
           'cert': cert}
    return rec

def init(a):
    ARGS.update(a)

if __name__ == '__main__':
    setf, key, label, nproc, outp = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
    tb = float(sys.argv[6]) if len(sys.argv) > 6 and sys.argv[6] != 'None' else None
    rb = float(sys.argv[7]) if len(sys.argv) > 7 else 30.0
    blind = len(sys.argv) > 8 and sys.argv[8] == 'blind'
    d = json.load(open(setf))
    ws = d if isinstance(d, list) else d[key]
    ws = [w[1] if isinstance(w, list) else w for w in ws]
    t0 = time.time()
    with Pool(nproc, initializer=init, initargs=({'tb': tb, 'rb': rb, 'blind': blind},)) as P:
        recs = P.map(run_one, ws, chunksize=2)
    with open(outp + '.jsonl', 'w') as f:
        for r in recs: f.write(json.dumps(r) + '\n')
    from collections import Counter
    st = Counter(r['status'] for r in recs)
    kinds = Counter(k for r in recs for k in r.get('kinds', []))
    groups = Counter(g for r in recs for g in r.get('groups', []))
    ns = [r['n'] for r in recs if r.get('n') is not None]
    secs = sorted(r['secs'] for r in recs if 'secs' in r)
    by_n = {}
    for r in recs:
        if r.get('n') is None: continue
        b = (r['n'] // 4) * 4
        e = by_n.setdefault(b, {'count': 0, 'unknot': 0, 'nontrivial': 0, 'unresolved': 0, 'secs': []})
        e['count'] += 1; e['secs'].append(r['secs'])
        if r['status'] == 'CERTIFIED_UNKNOT': e['unknot'] += 1
        elif r['status'] in ('CERTIFIED_NONTRIVIAL', 'COUNTEREXAMPLE'): e['nontrivial'] += 1
        else: e['unresolved'] += 1
    for b, e in by_n.items():
        s = sorted(e['secs']); e['median_s'] = s[len(s) // 2]; e['max_s'] = s[-1]; del e['secs']
    summ = {'label': label, 'count': len(recs), 'status': dict(st), 'certificate_kinds': dict(kinds),
            'tietze_success': sum(1 for r in recs if r.get('tietze') and r['tietze'].get('success')),
            'V_K=1': sum(1 for r in recs if r.get('V1')), 'Delta=1': sum(1 for r in recs if r.get('A1')),
            'rep_groups': dict(groups), 'crossings_min_max': (min(ns), max(ns)) if ns else None,
            'secs_median_max_total': (secs[len(secs) // 2], secs[-1], round(sum(secs), 1)) if secs else None,
            'by_crossings_bucket4': dict(sorted(by_n.items())), 'wall': round(time.time() - t0, 1),
            'params': {'tietze_budget': tb, 'rep_budget': rb, 'blind': blind}}
    json.dump(summ, open(outp + '.summary.json', 'w'), indent=1)
    print(json.dumps(summ))
