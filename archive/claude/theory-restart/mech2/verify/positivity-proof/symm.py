#!/usr/bin/env python3
"""Referee: the symmetric diagram D_sym of a half-diagram (my reading of Tangle::complete_symmetry), its crossing signs,
Seifert circles and canonical genus, computed by a generic tracer (independent of the half-plane model in ref.py)."""
from ref import parse_word, half_info, half_plane

def complete_symmetry(word):
    hw = 1
    out = []
    for (ch, s) in word:
        if s == 0:
            assert ch in 'xy'
            out.append((ch, hw - 1))
        elif ch in 'xy':
            out.append((ch, hw + s - 1)); out.append((ch, hw - s - 1))
        elif ch in 'lr':
            out.append(('c', hw + s - 1)); out.append(('c', hw - s + 1)); hw += 2
        elif ch == 'u':
            out.append(('u', hw + s - 1)); out.append(('u', hw - s - 1)); hw -= 2
    out.append(('u', 0))
    return out

def trace_closed(full):
    """full: word with two top ends (positions 0,1) and no bottom ends; the two top ends are joined (fixed point at infinity).
    Returns (signs per crossing letter in order, number of Seifert circles, n_components)."""
    L = len(full)
    width = [2]
    for (ch, i) in full:
        w = width[-1]
        if ch in 'xy':
            assert 0 <= i and i + 1 < w, (ch, i, w)
            width.append(w)
        elif ch == 'c':
            assert 0 <= i <= w
            width.append(w + 2)
        else:
            assert 0 <= i and i + 1 < w
            width.append(w - 2)
    assert width[-1] == 0
    down = {}; up = {}
    for k, (ch, i) in enumerate(full):
        w = width[k]
        if ch in 'xy':
            for p in range(w):
                q = i + 1 if p == i else (i if p == i + 1 else p)
                down[(k, p)] = ((k + 1, q), 'v'); up[(k + 1, q)] = ((k, p), 'v')
        elif ch == 'c':
            for p in range(w):
                q = p if p < i else p + 2
                down[(k, p)] = ((k + 1, q), 'v'); up[(k + 1, q)] = ((k, p), 'v')
            up[(k + 1, i)] = ((k + 1, i + 1), 'cap'); up[(k + 1, i + 1)] = ((k + 1, i), 'cap')
        else:
            for p in range(w):
                if p in (i, i + 1): continue
                q = p if p < i else p - 2
                down[(k, p)] = ((k + 1, q), 'v'); up[(k + 1, q)] = ((k, p), 'v')
            down[(k, i)] = ((k, i + 1), 'cup'); down[(k, i + 1)] = ((k, i), 'cup')
    up[(0, 0)] = ((0, 1), 'cap'); up[(0, 1)] = ((0, 0), 'cap')
    orient = {}
    node = (0, 0); going_down = True
    total = sum(width)
    while node not in orient:
        orient[node] = 1 if going_down else -1
        nxt, kind = (down[node] if going_down else up[node])
        if kind == 'cup': going_down = False
        elif kind == 'cap': going_down = True
        node = nxt
    ncomp = 1 if len(orient) == total else 2   # 2 = "more than one"
    signs = []
    # Seifert smoothing with a label list
    pos = [0, 0]; nxtlab = 1; circles = 0
    def cup(i):
        nonlocal circles, pos
        a, b = pos[i], pos[i + 1]
        del pos[i:i + 2]
        if a == b: circles += 1
        else: pos = [a if z == b else z for z in pos]
    def cap(i):
        nonlocal nxtlab
        pos.insert(i, nxtlab); pos.insert(i, nxtlab); nxtlab += 1
    for k, (ch, i) in enumerate(full):
        if ch == 'c': cap(i)
        elif ch == 'u': cup(i)
        else:
            if ncomp != 1:
                signs.append(None); continue
            same = orient[(k, i)] == orient[(k, i + 1)]
            if ch == 'y': s = 1 if same else -1
            else: s = -1 if same else 1
            signs.append(s)
            if not same:      # antiparallel vertical strands: Seifert smoothing = turnback
                cup(i); cap(i)
    assert pos == []
    return signs, circles, ncomp

def sym_info(wordstr):
    word = parse_word(wordstr)
    full = complete_symmetry(word)
    signs, circles, ncomp = trace_closed(full)
    n = len(signs)
    return dict(n=n, signs=signs, seifert=circles, ncomp=ncomp, writhe=sum(signs) if ncomp == 1 else None,
                genus_can=(n - circles + 1) // 2 if ncomp == 1 else None, parity_ok=((n - circles + 1) % 2 == 0))

if __name__ == '__main__':
    import sys, json
    rows = json.load(open('sweep.json'))
    bad = 0
    for r in rows:
        w = parse_word(r['word']); hi = half_info(w); si = sym_info(r['word'])
        # per-letter comparison of signs: an off-axis crossing gives two crossings upstairs, an axis crossing one
        exp = []
        for (ch, i), s in zip(w, hi['signs']):
            if ch in 'xy':
                exp += [s] if i == 0 else [s, s]
        ok = (si['ncomp'] == 1 and si['signs'] == exp and si['n'] == 2 * hi['c_o'] + hi['c_axis'])
        homog = abs(hi['wr']) == hi['c']
        if homog:
            end = 1 if hi['wr'] < 0 else 0
            hp = half_plane(w, end)
            ok = ok and (si['genus_can'] == hi['c_o'] - hp['loops']) and (si['seifert'] == hi['c_axis'] + 1 + 2 * hp['loops'])
            ok = ok and (abs(si['writhe']) == si['n'])
        if not ok:
            bad += 1; print('MISMATCH', r['name'], r['word'], si, hi)
    print('checked', len(rows), 'mismatches', bad)
