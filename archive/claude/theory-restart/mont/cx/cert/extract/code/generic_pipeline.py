"""Generic stage-1 pipeline: list of (W, provenance) -> dedupe by W -> exact V_K of the original diagram -> word reduction +
certification (certify_lib) -> residue JSON + certificates.  usage: generic_pipeline.py IN.json TAG NPROC
IN.json: {'items': [[W, prov], ...]}"""
import sys, json, time, gzip, multiprocessing as mp
from collections import Counter, defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import rules, certify_lib as C, vk
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/'
def work(W):
    w = rules.enc(W.split('.') if W else [])
    res = C.certify_word(w, budget=2000)
    hw0 = C.halfword(w)
    res['V_original_exact_is_1'] = (vk.VK(hw0) == {0: 1})
    res['ncross_original'] = vk.ncross(hw0)
    return W, res
if __name__ == '__main__':
    inp, tag, nproc = sys.argv[1], sys.argv[2], int(sys.argv[3])
    items = json.load(open(inp))['items']
    prov = defaultdict(list)
    for W, p in items: prov[W].append(p)
    print(tag, 'items', len(items), 'distinct words', len(prov), flush=True)
    t0 = time.time()
    ctx = mp.get_context('fork')
    with ctx.Pool(nproc) as pool: results = pool.map(work, list(prov), chunksize=200)
    stats = Counter(); resid = []
    with gzip.open(OUT + tag + '_certificates.jsonl.gz', 'wt') as f:
        for W, res in results:
            st = res['status']; stats[st] += 1
            if not res['V_original_exact_is_1']: stats['ALARM_original_V_ne_1'] += 1
            f.write(json.dumps({'word': W, 'status': st, 'reduced': res['reduced'], 'moves': res['moves'],
                                'ncross_original': res['ncross_original'], 'ncross_reduced': res.get('ncross_reduced'),
                                'prov': prov[W]}) + '\n')
            if st not in ('CERT_c_empty', 'CERT_a_TS24'):
                resid.append({'halfword': 's.l1.l1.' + (W + '.' if W else '') + 'u2.u2',
                              'reduced_halfword': C.halfword(rules.enc(res['reduced'])),
                              'ncross_original': res['ncross_original'], 'ncross_reduced': res.get('ncross_reduced'),
                              'status': st, 'V_K_exact_original_is_1': res['V_original_exact_is_1'], 'provenance': prov[W]})
    json.dump(resid, open(OUT + tag + '_stage1_residue.json', 'w'))
    json.dump({'items': len(items), 'distinct_words': len(prov), 'status': dict(stats)}, open(OUT + tag + '_stage1_counts.json', 'w'), indent=1)
    print(tag, 'status', dict(stats), 'time', round(time.time() - t0, 1), flush=True)
