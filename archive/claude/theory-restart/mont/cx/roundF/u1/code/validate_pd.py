"""validate_pd.py -- step (1)+(2) validation.
For random halfwords (flat_search.gen grammar + width-two words with all prefixes/suffixes):
  * PD code passes check_pd (labels, orientation, planar Euler characteristic F = n + 2);
  * V_K from the PD code (diagram.jones) == ident3-normalised V_K from kauffman.bracket (refs.VK_ref), EXACTLY;
  * Alexander polynomial from Fox calculus on the Wirtinger presentation of the PD code == alex.alex_poly (sympy);
  * Alexander polynomial from Fox calculus on the PLAT presentation (Artin action) == alex.alex_poly.
usage: validate_pd.py SEED COUNT NPROC OUT.json"""
import sys, json, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u1/code')
import diagram, wirtinger, refs
from multiprocessing import Pool


def plat_alex(word):
    full = diagram.morse_word(word)
    gens, rels = wirtinger.plat(full)
    ab = wirtinger.abelianisation(gens, rels)
    if ab is None: return 'ab-fail'
    rels2 = rels[:-1]                      # the last cup relator is a consequence of the others
    M = diagram.fox_matrix(gens, rels2, ab)
    m = [row[:-1] for row in M]
    return diagram.normalize_alex(diagram.poly_det(m)), max(len(r) for r in rels), sorted(set(abs(v) for v in ab.values()))


def one(w):
    t0 = time.time()
    pd = diagram.pd_from_halfword(w)
    if pd is None: return (w, 'pd-none')
    res = {'w': w, 'n': pd.n, 'check': diagram.check_pd(pd)}
    V = diagram.jones(pd); Vr = refs.VK_ref(w)
    res['V_ok'] = (V == Vr)
    A = diagram.alexander(pd); Ar = refs.alex_ref_fast(w)
    if pd.n <= 12: res["A_sympy_ok"] = (refs.alex_ref(w) == Ar)
    res['A_ok'] = (A == Ar)
    try:
        Ap, maxlen, absv = plat_alex(w)
        res['Aplat_ok'] = (Ap == Ar); res['plat_maxrel'] = maxlen; res['plat_ab'] = absv
    except Exception as e:
        res['Aplat_ok'] = 'err %s' % e
    res['V_is_1'] = (V == {0: 1}); res['A_is_1'] = (Ar == ((0, 1),))
    res['sec'] = round(time.time() - t0, 3)
    return res


if __name__ == '__main__':
    seed, count, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    ws = refs.random_halfwords(seed, count, minlen=4, maxlen=18, width2_frac=0.5, w2len=(1, 16))
    t0 = time.time()
    with Pool(nproc) as P:
        rows = P.map(one, ws, chunksize=4)
    bad = [r for r in rows if not isinstance(r, dict) or not (r['check'] and r['V_ok'] and r['A_ok'] and r['Aplat_ok'] is True)]
    ns = [r['n'] for r in rows if isinstance(r, dict)]
    summ = {'count': len(rows), 'bad': len(bad), 'check_ok': sum(1 for r in rows if isinstance(r, dict) and r['check']),
            'V_ok': sum(1 for r in rows if isinstance(r, dict) and r['V_ok']),
            'A_ok': sum(1 for r in rows if isinstance(r, dict) and r['A_ok']),
            'Aplat_ok': sum(1 for r in rows if isinstance(r, dict) and r['Aplat_ok'] is True),
            'V_is_1': sum(1 for r in rows if isinstance(r, dict) and r['V_is_1']),
            'A_sympy_checked': sum(1 for r in rows if isinstance(r, dict) and 'A_sympy_ok' in r),
            'A_sympy_ok': sum(1 for r in rows if isinstance(r, dict) and r.get('A_sympy_ok') is True),
            'crossings_min_max_mean': (min(ns), max(ns), round(sum(ns) / len(ns), 2)),
            'plat_ab_values': sorted(set(tuple(r.get('plat_ab', ())) for r in rows if isinstance(r, dict))),
            'secs': round(time.time() - t0, 1)}
    json.dump({'summary': summ, 'bad': bad[:50], 'rows': rows}, open(outp, 'w'))
    print(json.dumps(summ))
    for b in bad[:10]: print('BAD', b)
