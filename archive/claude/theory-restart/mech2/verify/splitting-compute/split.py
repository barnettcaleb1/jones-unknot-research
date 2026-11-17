#!/usr/bin/env python3
"""For each table inversion: T(0) = (simplified word).u0, trace the two components, write a 1-1 tangle .kht file for each
component (sub-diagram of that component alone), and record my own Jones polynomial, writhes, linking number."""
import json, os, sys
from morse import parse, unparse, Trace, closed_to_11, jones_11
from words import header_word, names
OUT = 'examples/comp'
os.makedirs(OUT, exist_ok=True)
info = {}
for nm in names():
    w = header_word(nm)
    ev = parse(w) + [('u', 0)]
    tr = Trace(ev, 1, close11=True)
    comps = tr.components()
    assert len(comps) == 2, (nm, len(comps))
    c_open = tr.comp[0]
    c_closed = [c for c in comps if c != c_open][0]
    sub_o = tr.subword(c_open)
    sub_c0 = tr.subword(c_closed)
    sub_c = closed_to_11(sub_c0)
    # sanity: the sub-words are knots (1 component each, 1-1 tangles)
    for sw in (sub_o, sub_c):
        t2 = Trace(sw, 1, close11=True)
        assert len(t2.components()) == 1 and len(t2.bottom) == 1
    jo, wo = jones_11(sub_o); jc, wc = jones_11(sub_c)
    lk2 = tr.linking2(c_open, c_closed)
    rec = dict(word=w, open=unparse(sub_o), closed=unparse(sub_c),
               n_self_open=tr.ncross(c_open), n_self_closed=tr.ncross(c_closed), n_mixed=tr.ncross(c_open, c_closed),
               writhe_open=wo, writhe_closed=wc, lk2=lk2,
               jones_open=sorted(jo.items()), jones_closed=sorted(jc.items()))
    info[nm] = rec
    for tag, sw in (('o', sub_o), ('c', sub_c)):
        fn = os.path.join(OUT, '%s_%s.kht' % (nm, tag))
        with open(fn, 'w') as f:
            f.write('%% component %s of T(0) for %s (referee)\n%s\n,1\n' % (tag, nm, unparse(sw)))
json.dump(info, open('split_info.json', 'w'), indent=0)
for nm in ['3_1', '8_19', '9_42', '9_46-1', '9_46-2', '7_4-2', '7_7-2', '9_23-2']:
    r = info[nm]
    print(nm, 'self-crossings open/closed/mixed', r['n_self_open'], r['n_self_closed'], r['n_mixed'], '2lk', r['lk2'])
    print('   open  :', r['open']); print('     Jones', r['jones_open'])
    print('   closed:', r['closed']); print('     Jones', r['jones_closed'])
