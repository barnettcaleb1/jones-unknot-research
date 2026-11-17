import sys, os, glob, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/scripts')
from bcube import *
from fullcube import cutpoint_structure, components
from survey import N_from_chainfile, SI
rows = {}
for l in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl'):
    r = json.loads(l); rows[r['name']] = r
def state_graph(half, end):
    word, lab, wr = quotient_word(half, with_twists=False)
    widths, base = cutpoint_structure(word)
    cr = crossings_of(word)
    comp = components(word, {lev: end for lev in cr}, widths, base)
    L = len(word)
    a = comp[0]; b = comp[base[L]]
    star = -1
    def v(x): return star if x in (a, b) else x
    edges = set(); loops = 0
    for lev in cr:
        c, i = word[lev]
        is_e = (end == 1) == one_is_e(c)
        A, B = base[lev], base[lev + 1]
        s = (comp[A + i], comp[B + i]) if is_e else (comp[A + i], comp[A + i + 1])
        x, y = v(s[0]), v(s[1])
        if x == y:
            loops += 1; continue
        edges.add((min(x, y), max(x, y)))
    verts = set(v(x) for x in comp)
    return len(verts), len(edges), loops
ok = 0; bad = []
for nm, r in sorted(rows.items()):
    if 'err' in r: continue
    half, orient, sym = read_kht(os.path.join(SI, nm + '.kht'))
    Npts = N_from_chainfile(os.path.join(SI, nm, 'cxBNr-c2-qs'))
    cube = [(h - r['hshift'], q - r['qshift']) for h, q in Npts]
    n = r['ncr']
    if r['top_gap'] == 0:
        V, E, loops = state_graph(half, 1)
        b1 = E - V + 1
        cnt = cube.count((n - 1, r['top_M'] - 2))
        if cnt == b1: ok += 1
        else: bad.append((nm, 'top', b1, cnt, V, E, loops))
    if r['bot_gap'] == 0:
        V, E, loops = state_graph(half, 0)
        b1 = E - V + 1
        cnt = cube.count((1, r['bot_M'] + 2))
        if cnt == b1: ok += 1
        else: bad.append((nm, 'bot', b1, cnt, V, E, loops))
print('adequate ends where dim N at (corner -+ D) equals b_1 of the reduced state graph:', ok, ' failures:', len(bad))
for b in bad[:20]: print('  ', b)
