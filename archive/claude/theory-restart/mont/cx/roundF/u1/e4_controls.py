"""e4_controls.py -- discriminating check of the translation on E4 configurations (rings at levels m = 3, 5, 7) and E4
NONTRIVIAL CONTROLS.  For special words W_s of E4 forms, engineC2's own machinery gives J of the 2-slot closure with any
box: G = gtable.Ghat(top_fn) (fitted exactly from 4 direct evaluations, as e4_gen.py does), J = fastS.J_of(G, (a, b t^-3N)).
Pick non-unit (box, N) pairs (same nested-box family as the 65 units + rational boxes), build the body word exactly as
cert_e4.py does, translate, compare lp.J(halfword) with engineC2's J; write the halfwords (J != 1, hence K nontrivial) for
certification as controls.  usage: e4_controls.py NPER OUT.json"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import translate as TR
C2 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2'
sys.path.insert(0, C2); sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import gtable, plat2, sym, fastS, lp, vc, lib
from lp import shift
from multiprocessing import Pool
NPER = int(sys.argv[1]); OUTP = sys.argv[2]
def build_boxes():
    R = lib.rational(4)
    NL = []; seen = set()
    for u in lib.rational(3):
        for kk in [-2, -1, 1, 2]:
            for NN in [-1, 0, 1]:
                try: nd = lib.node(kk, NN, [u])
                except AssertionError: continue
                if nd is None or nd[0] in seen: continue
                seen.add(nd[0]); NL.append(nd)
    return [(b[1], b[2]) for b in R] + [(b[1], b[2]) for b in NL]
def job(Ws):
    rng = random.Random(hash(Ws) % 1000)
    G = gtable.Ghat(lambda B: plat2.top_events(Ws) + sym.body(B, 0))
    if G is None or isinstance(G, tuple): return []
    boxes = build_boxes(); out = []; tries = 0
    while len(out) < NPER and tries < 200:
        tries += 1
        v, Tr = rng.choice(boxes); N = rng.randint(-1, 1)
        a, b = v
        Je = fastS.J_of(G, (a, shift(b, -3 * N)))
        if Je is None or Je == {0: 1}: continue
        T = ('p', [Tr, ('w', ('Y' if N > 0 else 'y') * abs(N))]) if N else Tr
        body = vc.word(T)
        ev = sym.symmetric(plat2.top_events(Ws) + sym.body(body, 0))
        try:
            ev2, nr = TR.transfer(ev); h = TR.events_to_halfword(ev2)
        except AssertionError as e:
            continue
        if len(h.split('.')) > 120: continue
        Jh = lp.J(h)
        ms = sorted(set(p for (p) in []))
        out.append({'W_s': Ws, 'body': body, 'N': N, 'halfword': h, 'J_engineC2': sorted(Je.items()),
                    'J_lp': sorted(Jh.items()) if Jh else None, 'equal': Jh == Je, 'rings': nr})
    return out
if __name__ == '__main__':
    forms = ['abba', 'abCa', 'BABA', 'dbab', 'aDB', 'Baba']
    t0 = time.time()
    with Pool(3) as P: res = P.map(job, forms)
    rows = [r for rr in res for r in rr]
    json.dump(rows, open(OUTP, 'w'), indent=1)
    json.dump([['E4ctl:%s|%s|N=%d' % (r['W_s'], r['body'], r['N']), r['halfword']] for r in rows],
              open(os.path.join(os.path.dirname(OUTP), 'words_e4_controls.json'), 'w'))
    print('E4 non-unit configurations', len(rows), 'lp.J(translated) == engineC2 J:', sum(r['equal'] for r in rows),
          'secs', round(time.time() - t0, 1))
