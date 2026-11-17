#!/usr/bin/env python3
"""Compare the Alexander polynomials of my two components of T(0) (computed from the tangle word) with the lens's table of constituent
knots of the theta-curve (twobridge/table_const.txt, computed there from the half-diagram: a different route)."""
import re, json
from morse import parse
from alexander import alexander
info = json.load(open('split_info.json'))
def parse_poly(s):
    s = s.strip().replace(' ', '')
    if s in ('None', ''): return None
    terms = re.findall(r'[+-]?[^+-]+', s)
    d = {}
    for tm in terms:
        m = re.fullmatch(r'([+-]?)(\d*)\*?(t?)(?:\*\*(\d+))?', tm)
        assert m, (s, tm)
        sg = -1 if m.group(1) == '-' else 1
        c = int(m.group(2)) if m.group(2) else 1
        e = (int(m.group(4)) if m.group(4) else 1) if m.group(3) else 0
        d[e] = d.get(e, 0) + sg * c
    lo, hi = min(d), max(d)
    c = [d.get(e, 0) for e in range(lo, hi + 1)]
    if sum(c) < 0: c = [-x for x in c]
    return c
def sym(c):   # Alexander polynomials are symmetric; normalise anyway
    return tuple(c)
theirs = {}
for line in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/twobridge/table_const.txt'):
    m = re.match(r'(\S+)\s+dimN=\s*(\d+).*?detK=(\S+)\s+detKu=(\S+)\s+detKl=(\S+)\s+Ku=(.*?)\s+Kl=(.*?)(?:\s+\[.*)?$', line.rstrip())
    if not m:
        print('unparsed line:', line.strip()); continue
    theirs[m.group(1)] = (parse_poly(m.group(6)), parse_poly(m.group(7)), int(m.group(2)))
agree = 0; dis = []; missing = []
mine = {}
for nm, r in sorted(info.items()):
    ao = alexander(parse(r['open'])); ac = alexander(parse(r['closed']))
    mine[nm] = (ao, ac)
    if nm not in theirs:
        missing.append(nm); continue
    u, l, dimN = theirs[nm]
    if sorted([sym(ao), sym(ac)]) == sorted([sym(u), sym(l)]):
        agree += 1
    else:
        dis.append((nm, ao, ac, u, l))
json.dump(mine, open('alex_components.json', 'w'))
print('agree (unordered pair of Alexander polynomials):', agree, ' disagree:', dis, ' not in their table:', missing)
# which of (open, closed) is their K_u ?
role = {'open=Ku': 0, 'closed=Ku': 0, 'ambiguous': 0}
for nm in mine:
    if nm not in theirs: continue
    ao, ac = mine[nm]; u, l, _ = theirs[nm]
    if ao == ac: role['ambiguous'] += 1
    elif sym(ao) == sym(u): role['open=Ku'] += 1
    else: role['closed=Ku'] += 1
print(role)
for nm in ['3_1', '4_1-1', '8_19', '9_42', '9_46-1', '9_46-2', '7_4-2', '7_7-2', '9_23-2']:
    print(nm, 'Alexander open', mine[nm][0], 'closed', mine[nm][1])
