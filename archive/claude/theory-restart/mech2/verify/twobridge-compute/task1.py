#!/usr/bin/env python3
"""TASK 1: J from the saved kht++ data versus the matrix formula of Theorem A, for every record whose half-diagram
word is  s.<l1|r1>.<letters in y0,x0,x1,y1>.u2 .  Also: J from my own Kauffman-bracket evaluation of the kht++
quotient tangle (third, independent leg)."""
import json, os, sys, collections
from reflib import *
base = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
DICT = {'y0': 'Y', 'x0': 'y', 'x1': 'X', 'y1': 'x'}     # dictionary letter -> generator (worked out on 3_1, 4_1-1, 4_1-2)
def load():
    out = []
    for l in open(base + 'k138/k138.jsonl'):
        r = json.loads(l)
        fn = base + 'k138/examples/si/' + r['file'].replace('^', '-') + '.kht'
        out.append(('k138', r['file'], fn, r))
    for l in open(base + 'tilt/run_3_45.jsonl'):
        r = json.loads(l)
        f = r['file']
        fn = base + 'tilt/' + f if f.endswith('.kht') else base + 'tilt/examples/strong_inversions/2-bridge_knots/' + f + '.kht'
        out.append(('tilt', os.path.basename(f).replace('.kht', ''), fn, r))
    return out
def word_of(fn):
    if not os.path.exists(fn): return None
    lines = open(fn).read().split('\n')
    return lines[1].strip()
def twoletter(word):
    toks = word.split('.')
    if toks[0] != 's' or toks[1] not in ('l1', 'r1') or toks[-1] != 'u2': return None
    mid = toks[2:-1]
    if any(t not in DICT for t in mid): return None
    return ''.join(DICT[t] for t in mid)
rows = []; stats = collections.Counter(); mism = []; seenwords = {}
other_checked = 0; other_bad = []
for (src, name, fn, r) in load():
    word = word_of(fn)
    if word is None: stats['no file'] += 1; continue
    khr = r.get('khr')
    w = twoletter(word)
    if w is None:
        stats['not a two-letter word'] += 1
        # sanity leg only: data J against my bracket J (small diagrams only)
        if khr:
            jd = J_from_khr(khr)
            if jd is not None:
                try:
                    L = half_letters(word)
                    if len(L) <= 14:
                        jb = A_to_t(J_bracket(L)[0])
                        other_checked += 1
                        if pnorm(jb) != pnorm(jd[2]): other_bad.append((src, name, word, pnorm(jb), pnorm(jd[2])))
                except Exception as e:
                    other_bad.append((src, name, word, 'ERR', repr(e)))
        continue
    stats['two-letter word'] += 1
    if not khr:
        stats['two-letter word, no saved Kh~ (timeout)'] += 1
        continue
    jd = J_from_khr(khr)
    if jd is None:
        stats['two-letter word, khr not standard'] += 1
        mism.append((src, name, word, w, 'khr not of the standard shape')); continue
    k, j, Jd, pts = jd
    Jm = J_matrix(w)
    Jb = A_to_t(J_bracket(half_letters(word))[0])
    nd, nm, nb = pnorm(Jd), pnorm(Jm), pnorm(Jb)
    nmf = pnorm(pflip(Jm))
    exact = (nd == nm); mirror = (nd == nmf)
    brk_data = (nb == nd); brk_mat = (nb == nm)
    stats['compared'] += 1
    stats['data == matrix (up to unit, no mirror)'] += exact
    stats['data == matrix only after t<->1/t'] += (mirror and not exact)
    stats['data == my bracket (up to unit)'] += brk_data
    stats['my bracket == matrix (up to unit)'] += brk_mat
    stats['J is a unit (trivial tangle)'] += (len(nd) == 1)
    mixed = len(set(c.isupper() for c in w)) == 2
    stats['mixed-sign words'] += mixed
    stats['dim N = %s' % ('1' if len(pts) == 1 else '>1')] += 1
    if not exact or not brk_data or not brk_mat:
        mism.append((src, name, word, w, 'data', nd, 'matrix', nm, 'bracket', nb, 'mirror ok' if mirror else 'mirror also fails'))
    seenwords.setdefault(w, []).append((src, name))
    rows.append((src, name, word, w, len(pts), nd))
print('records:', dict(stats))
print('distinct two-letter words compared:', len(seenwords), '; distinct normalised J:', len(set(r[5] for r in rows)))
print('non-trivial (J not a unit):', sum(1 for r in rows if len(r[5]) > 1), ' distinct words among them:',
      len(set(r[3] for r in rows if len(r[5]) > 1)))
print('MISMATCHES (%d):' % len(mism))
for m in mism: print('   ', m)
print('other (not two-letter) records: data J vs my bracket J checked on', other_checked, 'records; disagreements:', len(other_bad))
for m in other_bad: print('   ', m)
json.dump([list(r[:5]) + [list(r[5])] for r in rows], open('task1_rows.json', 'w'))
