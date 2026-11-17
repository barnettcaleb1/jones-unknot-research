#!/usr/bin/env python3
"""Doubled tangles T_K: rebuild the doubled 1-3 tangle word myself from the knot word (recipe = definition of kht++ -d:
cap l0/r0 on the left, every strand doubled, w = writhe full twists on (b2,b3) to make the linking number 0), write
 (a) the doubled word as a plain 1-3 tangle (to be rerun with kht++ and compared with the stored cxBNr-c2-d),
 (b) the two components of T_K(0) = T_K.u0 as 1-1 tangles."""
import os, re, json, sys
from morse import parse, unparse, Trace, closed_to_11, jones_11
DBL = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots'

def read_kht(path):
    lines = [l.split('%')[0].strip() for l in open(path, encoding='utf-8')]
    txt = ''.join(lines)
    word, _, orient = txt.partition(',')
    return word.strip('.'), [int(x) for x in orient.split(',') if x != '']

def kht_orient(events, tr, top):
    o = [0] * tr.nstrands
    for s in range(tr.ntop): o[s] = 1 if top[s] == 1 else -1
    for a, b, kind, k in tr.links:
        if kind == 'cap':
            o[a], o[b] = (-1, 1) if events[k][0] == 'l' else (1, -1)
    for a, b, kind, k in tr.links:
        if kind == 'cup' and o[a] == o[b]:
            raise ValueError('inconsistent orientation letters')
    return o

def double_word(word, top):
    ev = parse(word)
    tr = Trace(ev, 1, close11=True)
    tr.orient = kht_orient(ev, tr, top)
    w = tr.writhe()
    out = [('l' if top[0] == 1 else 'r', 0)]
    for c, i in ev:
        p = 1 + 2 * i
        if c in 'xy':
            out += [(c, p + 1), (c, p), (c, p + 2), (c, p + 1)]
        elif c in 'lr':
            out += [(c, p), (c, p + 1)]
        else:
            out += [('u', p + 1), ('u', p)]
    tw = ('x', 1) if w >= 0 else ('y', 1)
    out += [tw, tw] * abs(w)
    return out, w

if __name__ == '__main__':
    names = sys.argv[1:]
    os.makedirs('examples/dbl', exist_ok=True)
    info = {}
    for nm in names:
        word, top = read_kht(os.path.join(DBL, nm + '.kht'))
        dw, w = double_word(word, top)
        # (a) doubled tangle as a plain 1-3 tangle
        with open('examples/dbl/%s_T.kht' % nm, 'w') as f:
            f.write('%% doubled tangle of %s, rebuilt by the referee\n%s\n,%d\n' % (nm, unparse(dw), top[0]))
        # the knot itself
        with open('examples/dbl/%s_K.kht' % nm, 'w') as f:
            f.write('%% knot %s\n%s\n,%d\n' % (nm, word, top[0]))
        # (b) components of T_K(0)
        ev = dw + [('u', 0)]
        tr = Trace(ev, 1, close11=True)
        o = kht_orient(ev, tr, top)
        comps = tr.components(); assert len(comps) == 2
        c_open = tr.comp[0]; c_closed = [c for c in comps if c != c_open][0]
        # linking number with the kht orientation
        tr_k = Trace(ev, 1, close11=True); tr_k.orient = o
        lk2 = tr_k.linking2(c_open, c_closed)
        sub_o = tr.subword(c_open); sub_c = closed_to_11(tr.subword(c_closed))
        jo, wo = jones_11(sub_o); jc, wc = jones_11(sub_c); jk, wk = jones_11(parse(word))
        for tag, sw in (('o', sub_o), ('c', sub_c)):
            with open('examples/dbl/%s_%s.kht' % (nm, tag), 'w') as f:
                f.write('%% component %s of T_K(0), K = %s\n%s\n,1\n' % (tag, nm, unparse(sw)))
        info[nm] = dict(word=word, top=top, writhe=w, doubled=unparse(dw), lk2=lk2, ncross=len([e for e in dw if e[0] in 'xy']),
                        jones_K=sorted(jk.items()), jones_o=sorted(jo.items()), jones_c=sorted(jc.items()))
        print(nm, 'writhe', w, 'crossings of T_K', info[nm]['ncross'], '2lk', lk2,
              ' Jones(open)==Jones(K):', jo == jk, ' Jones(closed)==Jones(K):', jc == jk)
    old = json.load(open('dbl_info.json')) if os.path.exists('dbl_info.json') else {}
    old.update(info)
    json.dump(old, open('dbl_info.json', 'w'), indent=0)
