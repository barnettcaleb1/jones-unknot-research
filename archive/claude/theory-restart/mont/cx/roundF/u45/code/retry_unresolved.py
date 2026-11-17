"""retry_unresolved.py -- step (3) of the task for every UNRESOLVED word found in the given result files:
  (i)   Tietze with more seeds and longer budgets (10 seeds x 120 s);
  (ii)  the MIRROR word (x <-> y in every letter = the reflected diagram; its Wirtinger presentation is a different
        presentation of an isomorphic group): CERTIFIED_UNKNOT for the mirror certifies K (mirror of the unknot is the unknot);
        a rep certificate for the mirror certifies K nontrivial (isomorphic group);
  (iii) larger representation searches (extra groups: PSL(2,p), SL(2,p) up to p = 13, A8, S8 on the reduced presentation,
        120 s), and the Alexander-free affine search mod p up to p = 400.
Anything still not certified is RETAINED in OUT.json (never called an unknot).
usage: retry_unresolved.py OUT.json FILE.jsonl.gz [...]"""
import sys, os, json, gzip, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import certify, reps, replay
def mirror(w):
    toks = w.split('.')
    return '.'.join(('y' + t[1:]) if t.startswith('x') else ('x' + t[1:]) if t.startswith('y') else t for t in toks)
EXTRA = None
def extra_groups():
    global EXTRA
    if EXTRA is None:
        G = list(reps.target_groups())
        G += [('PSL(2,17)', reps.psl2_group(17)), ('PSL(2,19)', reps.psl2_group(19)), ('SL(2,11)', reps.sl2_group(11)),
              ('SL(2,13)', reps.sl2_group(13)), ('A8', reps.alt_group(8)), ('S8', reps.sym_group(8))]
        EXTRA = G
    return EXTRA
def retry(w):
    out = {'w': w, 'steps': []}
    st, info = certify.certify(w, tietze_budget=120.0, rep_budget=120.0, seed=100, n_seeds=10, groups=extra_groups())
    out['steps'].append(('long', st, [c['kind'] for c in info['certificates']]))
    if st not in ('UNRESOLVED',):
        out['status'] = st; out['certificates'] = info['certificates']; return out
    m = mirror(w)
    st2, info2 = certify.certify(m, tietze_budget=120.0, rep_budget=120.0, seed=200, n_seeds=5, groups=extra_groups())
    out['steps'].append(('mirror', st2, [c['kind'] for c in info2['certificates']]))
    if st2 == 'CERTIFIED_UNKNOT':
        out['status'] = 'CERTIFIED_UNKNOT'; out['via'] = 'mirror word ' + m; out['certificates'] = info2['certificates']; return out
    if st2 in ('CERTIFIED_NONTRIVIAL', 'COUNTEREXAMPLE'):
        out['status'] = 'CERTIFIED_NONTRIVIAL'; out['via'] = 'mirror word ' + m; out['certificates'] = info2['certificates']; return out
    out['status'] = 'UNRESOLVED'; out['V_K'] = info.get('V_K'); out['V_K_project'] = info.get('V_K_project'); out['n'] = info.get('crossings')
    return out
if __name__ == '__main__':
    outp = sys.argv[1]; words = []
    for f in sys.argv[2:]:
        with gzip.open(f, 'rt') as fh:
            for line in fh:
                r = json.loads(line)
                if r['status'] in ('UNRESOLVED', 'ERROR'): words.append(r['w'])
    print('UNRESOLVED words to retry:', len(words), flush=True)
    res = [retry(w) for w in words]
    json.dump(res, open(outp, 'w'), indent=1)
    from collections import Counter
    print(json.dumps(dict(Counter(r['status'] for r in res))))
