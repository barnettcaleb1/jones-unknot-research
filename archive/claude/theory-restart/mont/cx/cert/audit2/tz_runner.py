"""tz_runner.py CASES.json OUT.jsonl NPROC SEEDS BUDGET -- blind Tietze stress (soundness): for every case (halfword or
PD), run the certifier's simplifier tietze.simplify with each seed and the given wall-clock budget; any success is
re-checked by replay (replay.check for halfwords / replay.replay_moves for PDs) AND by a2lib.my_replay."""
import sys, json, time, multiprocessing as mp
A2 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2'
CERT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert'
sys.path.insert(0, A2); sys.path.insert(0, CERT)

def work(args):
    case, seeds, budget = args
    import a2lib, diagram, wirtinger, tietze, replay
    out = {'label': case.get('label'), 'expect': case.get('expect'), 'hw': case.get('hw'), 'runs': []}
    if 'hw' in case:
        pd = diagram.pd_from_halfword(case['hw'])
        mg, mr = a2lib.wirtinger_from_halfword(case['hw'])
    else:
        pd = diagram.PD([tuple(x) for x in case['X']], case['sign'])
        mg, mr = a2lib.wirtinger_from_pd([tuple(x) for x in case['X']], case['sign'])
    gens, rels = wirtinger.wirtinger(pd)
    out['n'] = pd.n
    for s in seeds:
        t0 = time.time()
        ok, moves, fin, st = tietze.simplify(gens, rels, seed=s, time_budget=budget)
        run = {'seed': s, 'success': ok, 'final_gens': len(fin[0]) if fin else None,
               'final_rels': len(fin[1]) if fin else None, 'secs': round(time.time() - t0, 2), 'attempts': st.get('attempts')}
        if ok:
            mv = [list(m) for m in moves]
            if 'hw' in case:
                run['replay'] = replay.check({'kind': 'tietze', 'halfword': case['hw'], 'moves': mv})
            else:
                pres, msg = replay.replay_moves(gens, rels, [tuple(m) for m in mv])
                run['replay'] = (pres is not None and len(pres[0]) == 1 and not pres[1], msg)
            run['mine'] = a2lib.my_replay(mg, mr, [tuple(m) for m in mv])[:2]
            run['nmoves'] = len(mv)
            if case.get('expect') == 'nontrivial':
                run['ALERT'] = 'SIMPLIFIER CLAIMS <a|> FOR A NONTRIVIAL KNOT'
                run['moves'] = mv
        out['runs'].append(run)
        if ok and case.get('expect') == 'unknot' and not case.get('all_seeds'): break
    return out

if __name__ == '__main__':
    cases = json.load(open(sys.argv[1])); outp = sys.argv[2]
    nproc = int(sys.argv[3]); seeds = [int(x) for x in sys.argv[4].split(',')]; budget = float(sys.argv[5])
    t0 = time.time()
    with mp.Pool(nproc) as pool, open(outp, 'w') as f:
        for r in pool.imap_unordered(work, [(c, seeds, budget) for c in cases], chunksize=1):
            f.write(json.dumps(r, default=str) + '\n'); f.flush()
            for run in r['runs']:
                if run.get('ALERT') or (run.get('success') and not (run['replay'][0] and run['mine'][0])):
                    print('ALERT', r['label'], r.get('hw', '')[:80], run, flush=True)
    print('done', len(cases), round(time.time() - t0, 1), 's', flush=True)
