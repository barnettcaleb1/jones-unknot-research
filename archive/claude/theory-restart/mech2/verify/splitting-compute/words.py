#!/usr/bin/env python3
"""Read the simplified quotient-tangle words from the .kht headers; trace T and T(0) = T.u0; basic topology checks."""
import os, re, json, sys
from morse import parse, unparse, Trace, bracket, pstr
SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si'

def header_word(name):
    txt = open(os.path.join(SI, name + '.kht'), encoding='utf-8').read()
    m = re.search(r"Simplifies with options '-qs' to\s+(\S+)", txt)
    return m.group(1) if m else None

def names():
    return sorted(f[:-4] for f in os.listdir(SI) if f.endswith('.kht'))

if __name__ == '__main__':
    rows = {}
    for nm in names():
        w = header_word(nm)
        if w is None:
            print(nm, 'NO SIMPLIFIED WORD'); continue
        ev = parse(w)
        tr = Trace(ev, 1)
        nb = len(tr.bottom)
        # connectivity of the 1-3 tangle: which bottom position carries the top strand's component
        comp_top = tr.comp[0]
        pos = [i for i, s in enumerate(tr.bottom) if tr.comp[s] == comp_top]
        ncr = len(tr.crossings)
        rows[nm] = dict(word=w, nbottom=nb, top_at=pos, ncross=ncr, ncomp=len(tr.components()))
        flag = '' if (nb == 3 and pos == [2] and len(tr.components()) == 2) else '   <-- NOT of connectivity b'
        print('%-8s crossings %2d bottom ends %d  top strand ends at bottom position %s  components %d%s' % (nm, ncr, nb, pos, len(tr.components()), flag))
    json.dump(rows, open('words.json', 'w'), indent=0)
