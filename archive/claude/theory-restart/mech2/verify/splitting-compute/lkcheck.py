#!/usr/bin/env python3
"""Sign of the l-shift c against the linking number of T(0) computed with the orientation that kht++ itself uses
(top end up, cap letters l/r of the simplified word)."""
import json, collections
from morse import parse, Trace
from words import header_word
rows = json.load(open('analysis.json'))
def kht_orientation(events, tr):
    """orientation of every monotone strand as kht++ reads the word: top ends up; cap 'l' = (down, up), 'r' = (up, down).
    Returns None if the letters are inconsistent (kht++ would auto-correct)."""
    o = [0] * tr.nstrands
    for s in range(tr.ntop): o[s] = 1
    for a, b, kind, k in tr.links:
        if kind == 'cap':
            c = events[k][0]
            o[a], o[b] = (-1, 1) if c == 'l' else (1, -1)
    for a, b, kind, k in tr.links:
        if kind == 'cup' and o[a] == o[b]:
            return None
    return o
res = collections.Counter(); detail = {}
for nm, r in sorted(rows.items()):
    ev = parse(header_word(nm)) + [('u', 0)]
    tr = Trace(ev, 1, close11=True)
    o = kht_orientation(ev, tr)
    if o is None:
        res['inconsistent letters'] += 1; print('inconsistent cap letters', nm); continue
    # closure consistency: bottom strand must be up (same as top)
    assert o[tr.bottom[0]] == 1, nm
    tr.orient = o
    c_open = tr.comp[0]; c_closed = [c for c in tr.components() if c != c_open][0]
    lk2 = tr.linking2(c_open, c_closed)
    detail[nm] = lk2
    if 'dimN' in r:
        c = r['good_c'][0]
        res[('c + 2lk_kht', c + lk2)] += 1
print(sorted(res.items(), key=str))
json.dump(detail, open('lk_kht.json', 'w'))
print('2lk_kht distribution', sorted(collections.Counter(detail.values()).items()))
