#!/usr/bin/env python3
"""Bad blocks of the band diagram at the 1-end and the 0-end, with the component they sit on."""
import sys, os, glob, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
from fullcube import cutpoint_structure, components

SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si'

def bad_blocks(half, end):
    """end = 1 (all-one state) or 0. returns list of dicts per block: kind, letter, halfindex, bad, comp"""
    word, lab, wr = quotient_word(half, with_twists=False)
    widths, base = cutpoint_structure(word)
    cr = crossings_of(word)
    bits = {lev: end for lev in cr}
    comp = components(word, bits, widths, base)
    L = len(word)
    top_pt = 0
    bot = [base[L] + j for j in range(3)]
    assert comp[top_pt] == comp[bot[2]] and comp[bot[0]] == comp[bot[1]], 'extreme state not type b'
    name = {comp[top_pt]: 'a', comp[bot[0]]: 'b'}
    def nm(c):
        if c not in name:
            name[c] = 'c%d' % (len(name) - 1)
        return name[c]
    blocks = []
    # group crossings by label
    groups = collections.OrderedDict()
    for lev in cr:
        groups.setdefault(lab[lev], []).append(lev)
    for (kind, hidx), levs in groups.items():
        chords = []
        for lev in levs:
            c, i = word[lev]
            is_e = (end == 1) == one_is_e(c)
            A, B = base[lev], base[lev + 1]
            if is_e:
                sides = (comp[A + i], comp[B + i])        # upper arc, lower arc
            else:
                sides = (comp[A + i], comp[A + i + 1])    # left line, right line
            chords.append(sides)
        nbad = sum(1 for s in chords if s[0] == s[1])
        badcomp = [nm(s[0]) for s in chords if s[0] == s[1]]
        letter = half[hidx][0]
        is_e = (end == 1) == one_is_e(letter)
        blocks.append(dict(kind=kind, letter=letter, hidx=hidx, state=('cut' if is_e else 'pass') if kind == 'hook' else ('hor' if is_e else 'ver'),
                           nbad=nbad, comp=(badcomp[0] if badcomp else None),
                           sides=[(nm(a), nm(b)) for a, b in chords]))
    ncirc = len(set(comp)) - 2
    return blocks, ncirc

def describe(half, end):
    blocks, ncirc = bad_blocks(half, end)
    s = []
    for b in blocks:
        tag = ('H' if b['kind'] == 'hook' else 'B') + b['letter'] + ('!' + b['comp'] if b['nbad'] else '')
        s.append(tag)
    return ' '.join(s), sum(1 for b in blocks if b['nbad']), ncirc

if __name__ == '__main__':
    rows = {}
    for l in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl'):
        r = json.loads(l)
        rows[r['name']] = r
    names = sys.argv[1:] or sorted(os.path.basename(f)[:-4] for f in glob.glob(SI + '/*.kht'))
    for nm_ in names:
        half, orient, sym = read_kht(os.path.join(SI, nm_ + '.kht'))
        r = rows.get(nm_, {})
        for end, tag in ((1, 'top'), (0, 'bot')):
            d, nb, nc = describe(half, end)
            if 'err' in r or not r:
                defect = None
            else:
                n = r['ncr']
                defect = (n - r['N_top'][0], r['top_gap']) if end == 1 else (r['N_bot'][0], r['bot_gap'])
            print('%-8s %s nbad=%d defect=%s  | %s' % (nm_, tag, nb, defect, d))
