"""Per-run table for U4: reproduction status, stored J = 1 words, certification and two-checker verification counts."""
import sys, json, gzip, os, glob
from collections import Counter
D = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/'
O = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/'
RUNS = ['e3_n12_s1', 'e3_n12_s112', 'e3_n16_s116', 'e3_n20_s120', 'e3_n24_s124', 'e3_n30_s130', 'e3_n40_s140',
        'e3b_n12_s7', 'e3b_n12_s212', 'e3b_n16_s216', 'e3b_n20_s220', 'e3b_n24_s224', 'e3b_n30_s230', 'e3b_n40_s240',
        'e3w3_n14_s1', 'e3w3_n14_s314', 'e3w3_n18_s318', 'e3w3_n24_s324', 'e3w3_n30_s330',
        'e3d_n20_s420', 'e3d_n30_s430', 'e3d_n40_s440']
def strip(x, keys): return {k: x.get(k) for k in keys}
def repro(run):
    a = json.load(open(O + run + '.json')); b = json.load(open(D + 'e3/out/' + run + '.json'))
    diff = []
    for k, v in a.items():
        if k == 'secs': continue
        w = b.get(k)
        if isinstance(v, list) and v and isinstance(v[0], dict):
            if len(v) != len(w) or any(strip(y, x.keys()) != x for x, y in zip(v, w)): diff.append(k)
        elif v != w: diff.append(k)
    return 'IDENTICAL' if not diff else 'DIFF:' + ','.join(diff), a['evals'], b['evals'], b
verif = {}
for f in glob.glob(D + 'cert/verify_u4_*.json'):
    v = json.load(open(f))
    allpass = (v['fraction'] == 1.0 and v['records_pass'] == v['sampled'] == v['records_total'])
    for fn in v['files']:
        nf = sum(1 for _ in gzip.open(os.path.join(D, fn) if not fn.startswith('/') else fn, 'rt'))
        if len(v['files']) == 1: verif[os.path.basename(fn)] = (v['records_total'], v['sampled'], v['records_pass'], v['fraction'])
        elif allpass: verif[os.path.basename(fn)] = (nf, nf, nf, 1.0)   # multi-file verify with every record passing
        else: verif[os.path.basename(fn)] = ('see', os.path.basename(f))
rows = []; tot = Counter()
for run in RUNS:
    if not os.path.exists(D + 'e3/out/' + run + '.json'): rows.append((run, 'not finished')); continue
    st, eo, er, b = repro(run)
    J1 = b['j1_words']
    where = Counter(e['where'] for e in J1.values()); kc = Counter(e['kcert'][0] for e in J1.values())
    cf = D + 'cert/u4_%s.jsonl.gz' % run
    cs = Counter(); kinds = Counter(); ncr = []; nrec = 0; vk = Counter()
    if os.path.exists(cf):
        for line in gzip.open(cf, 'rt'):
            r = json.loads(line); nrec += 1; cs[r['status']] += 1; kinds.update(r['kinds']); ncr.append(r['n'] or 0)
            vk[(r.get('V_K') == [[0, 1]], r.get('V_K_project') == [[0, 1]])] += 1
    vv = verif.get('u4_%s.jsonl.gz' % run)
    rows.append((run, st, eo, er, b['u45']['n_j1_probes'], len(J1), dict(where), dict(kc), nrec, dict(cs), dict(kinds),
                 (min(ncr), max(ncr)) if ncr else None, sum(1 for x in ncr if x <= 24), vv, {str(k): v for k, v in vk.items()}))
    tot['probes'] += b['u45']['n_j1_probes']; tot['distinct'] += len(J1); tot['certified_records'] += nrec
    tot['evals'] += er; tot['repro_identical'] += (st == 'IDENTICAL'); tot['runs'] += 1
    tot['gt24'] += sum(1 for x in ncr if x > 24); tot['vk_both_one'] += vk[(True, True)]
    for k, v in where.items(): tot['where:' + k] += v
    for k, v in kc.items(): tot['kcert:' + k] += v
    for k, v in cs.items(): tot['status:' + k] += v
    if vv and isinstance(vv[2], int): tot['verified_pass'] += vv[2]; tot['verified_sampled'] += vv[1]
json.dump({'rows': rows, 'totals': dict(tot)}, open(D + 'e3/u4_table.json', 'w'), indent=1)
for r in rows: print(r)
print('TOTALS', dict(tot))
