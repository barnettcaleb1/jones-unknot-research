"""run_batch.py CASES.json OUT.jsonl [NPROC] -- run halfword test cases through certify() in parallel; verify."""
import sys, json, time, multiprocessing as mp
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
import harness

def work(case):
    try:
        if 'hw' in case:
            return harness.run_hw(case['hw'], case.get('label', ''), case.get('expect'), case.get('blind', False),
                                  case.get('tietze_budget'), case.get('rep_budget', 30.0), case.get('seed', 0))
        else:
            r = harness.run_pd([tuple(x) for x in case['X']], case['sign'], case.get('label', ''), case.get('expect'),
                               case.get('blind', True), case.get('tietze_budget', 3.0), case.get('rep_budget', 30.0),
                               case.get('seed', 0), case.get('do_rep', True), None, case.get('skip_j24', False))
            return r
    except Exception as e:
        import traceback
        return {'case': case.get('label'), 'status': 'HARNESS_EXCEPTION', 'err': traceback.format_exc()[-800:], 'bad': ['HARNESS_EXCEPTION']}

if __name__ == '__main__':
    cases = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    nproc = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    t0 = time.time()
    with mp.Pool(nproc) as pool, open(out, 'w') as f:
        for k, r in enumerate(pool.imap_unordered(work, cases, chunksize=1)):
            f.write(json.dumps(r, default=str) + '\n'); f.flush()
            if r.get('bad'):
                print('BAD', r.get('label'), r.get('hw', '')[:80], r.get('status'), r.get('bad'), flush=True)
    print('done', len(cases), 'cases in', round(time.time() - t0, 1), 's', flush=True)
