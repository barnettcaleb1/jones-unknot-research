"""cert_words.py -- certify a list of halfwords with the FIXED certifier (run/code/certify.py), multiprocessing, resumable.
Every record (status, crossings, V_K by both brackets, ALL certificates with full move lists, Tietze stats, notes, time) is
appended to OUT.jsonl.gz as it arrives; a word already present in OUT.jsonl.gz is skipped on restart.  COUNTEREXAMPLE ->
certify() writes the HIT file at once (write_hits=True) and this driver also prints a loud line.
usage: cert_words.py WORDS.json NPROC OUTPREFIX [tietze_budget] [rep_budget]
  WORDS.json: a JSON list of halfwords (or of [tag, halfword] pairs; the tag is stored)."""
import sys, os, json, gzip, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import certify
from multiprocessing import Pool
ARGS = {}

def init(a): ARGS.update(a)

def one(item):
    tag, w = item
    t0 = time.time()
    try:
        st, info = certify.certify(w, tietze_budget=ARGS.get('tb'), rep_budget=ARGS.get('rb', 30.0), write_hits=True)
    except Exception as e:
        return {'w': w, 'tag': tag, 'status': 'ERROR', 'err': repr(e), 'secs': round(time.time() - t0, 3)}
    J = None
    if st in ('CERTIFIED_NONTRIVIAL', 'UNRESOLVED', 'COUNTEREXAMPLE'):
        # BRIEF section 0/5: a NONTRIVIAL K with J = 1 is a Lemma Q counterexample (hence a JUC counterexample via L_n),
        # whatever V_K is.  J is computed exactly (lp.J) for every non-unknot result.
        try:
            if '/Users/calebbarnett/jones-lanes/theory-restart/mont' not in sys.path:
                sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
            import lp
            J = lp.J(w)
        except Exception as e:
            J = 'error %r' % (e,)
        if st == 'CERTIFIED_NONTRIVIAL' and J == {0: 1}:
            rep = next(c for c in info['certificates'] if c['kind'] == 'rep')
            info['hit_file'] = certify.write_hit(w, dict(info.get('V_K') or []), dict(info.get('V_K_project') or []),
                                                 None, info.get('Delta'), rep,
                                                 'LEMMA Q COUNTEREXAMPLE: J = 1 (lp.J exact) and K CERTIFIED_NONTRIVIAL (cert_words.py)')
            st = 'LEMMA_Q_HIT'
    return {'w': w, 'tag': tag, 'status': st, 'J': (sorted(J.items()) if isinstance(J, dict) else J), 'n': info.get('crossings'), 'V_K': info.get('V_K'),
            'V_K_project': info.get('V_K_project'), 'Delta': info.get('Delta'),
            'kinds': [c['kind'] for c in info['certificates']], 'certificates': info['certificates'],
            'tietze': info.get('tietze'), 'notes': info.get('notes'), 'hit_file': info.get('hit_file'),
            'secs': round(time.time() - t0, 3)}

if __name__ == '__main__':
    src, nproc, outp = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    tb = float(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != 'None' else None
    rb = float(sys.argv[5]) if len(sys.argv) > 5 else 30.0
    d = json.load(open(src))
    items = [(x[0], x[1]) if isinstance(x, list) else (None, x) for x in d]
    done = set()
    if os.path.exists(outp + '.jsonl.gz'):
        try:
            with gzip.open(outp + '.jsonl.gz', 'rt') as f:
                for line in f:
                    try: done.add(json.loads(line)['w'])
                    except Exception: break
        except (EOFError, OSError):
            pass
    todo = [it for it in items if it[1] not in done]
    print('words', len(items), 'already done', len(done), 'todo', len(todo), flush=True)
    from collections import Counter
    st = Counter(); t0 = time.time()
    with Pool(nproc, initializer=init, initargs=({'tb': tb, 'rb': rb},)) as P, gzip.open(outp + '.jsonl.gz', 'at') as f:
        for i, rec in enumerate(P.imap_unordered(one, todo, chunksize=8)):
            st[rec['status']] += 1
            f.write(json.dumps(rec) + '\n')
            if rec['status'] in ('COUNTEREXAMPLE', 'LEMMA_Q_HIT'):
                print('!!!!! COUNTEREXAMPLE', rec['w'], rec.get('hit_file'), flush=True)
            if rec['status'] not in ('CERTIFIED_UNKNOT',):
                print('non-unknot:', rec['status'], rec['w'], rec.get('n'), rec.get('notes'), flush=True)
            if (i + 1) % 2000 == 0:
                f.flush()
                print('progress', i + 1, dict(st), round(time.time() - t0, 1), flush=True)
    print('DONE', dict(st), round(time.time() - t0, 1), flush=True)
