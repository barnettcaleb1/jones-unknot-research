"""validate_s2.py -- for EVERY S2 word of engineC2's exhaustive |W| <= 7 enumeration (first letters a, B, d; the
enumeration order of engineC2/enum2.py, connectivity rule plat2.is_arc), check
  (1) event-level translation (translate.transfer + events_to_halfword) == closed form s2_halfword_closed;
  (2) lp.J(halfword) == plat2.J(W) exactly (J of the S2 theta-curve, engineC2's own evaluator);
and record which words have J = 1.  usage: validate_s2.py NPROC OUT.json"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import translate as TR
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import enum2, plat2, lp
from multiprocessing import Pool

def one(W):
    try:
        h = TR.s2_halfword(W)
        same = (h == TR.s2_halfword_closed(W))
        Jp = plat2.J(W); Jh = lp.J(h)
        return (W, h, same, Jp == Jh, Jp == {0: 1}, Jh == {0: 1}, None)
    except Exception as e:
        return (W, None, False, False, False, False, repr(e))

if __name__ == '__main__':
    nproc, outp = int(sys.argv[1]), sys.argv[2]
    words = [w for first in 'aBd' for w in enum2.words(first, 7) if plat2.is_arc(w)]
    print('words', len(words), flush=True)
    t0 = time.time()
    with Pool(nproc) as P: res = P.map(one, words, chunksize=64)
    bad = [r for r in res if not (r[2] and r[3])]
    units = [r[0] for r in res if r[4]]
    summ = {'words': len(res), 'event_eq_closed': sum(r[2] for r in res), 'J_equal': sum(r[3] for r in res),
            'J1_plat2': sum(r[4] for r in res), 'J1_lp': sum(r[5] for r in res), 'bad': bad[:50], 'nbad': len(bad),
            'secs': round(time.time() - t0, 1)}
    json.dump(summ, open(outp, 'w'), indent=1)
    json.dump([[r[0], r[1]] for r in res if r[4]], open(os.path.join(os.path.dirname(outp), 's2_unit_halfwords.json'), 'w'))
    json.dump([[r[0], r[1]] for r in res if not r[4]], open(os.path.join(os.path.dirname(outp), 's2_nonunit_halfwords.json'), 'w'))
    print(json.dumps({k: v for k, v in summ.items() if k != 'bad'}), flush=True)
