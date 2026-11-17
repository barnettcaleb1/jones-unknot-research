#!/usr/bin/env python3
"""Referee: compare the kht++ chain files (b-generators of BN~ with their (h,q)) with the cube predictions.
kht++ bigrading of a cube generator of the full quotient diagram D' (with twists):
   (h,q)_kht = (|s| - n_-, q_cube + n_+ - 2 n_-),  n_+- = signed crossing numbers of D' with the orientation kht++ gives T
   (alpha: top -> b3, beta: b1 -> b2, i.e. the two ends b2, b3 of the extra band parallel)."""
import sys, os, glob, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/scripts')
import khtparse
from ref import *

SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si'

def tangle_signs(bword_with_twists):
    """trace alpha (from the top end, position 0) and beta (from b1 upward) in the tangle word; return (n_plus, n_minus)."""
    full = bword_with_twists
    L = len(full)
    width = [1]
    for (ch, i) in full:
        w = width[-1]
        width.append(w + 2 if ch == 'c' else (w - 2 if ch == 'u' else w))
    assert width[-1] == 3
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
    orient = {}
    def run(node, going_down):
        while True:
            assert node not in orient
            orient[node] = 1 if going_down else -1
            if going_down and node[0] == L: return node
            if (not going_down) and node[0] == 0: return node
            nxt, kind = (down[node] if going_down else up[node])
            if kind == 'cup': going_down = False
            elif kind == 'cap': going_down = True
            node = nxt
    e1 = run((0, 0), True)
    assert e1 == (L, 2), e1          # alpha: top -> b3
    e2 = run((L, 0), False)
    assert e2 == (L, 1), e2          # beta: b1 -> b2
    assert len(orient) == sum(width)
    npl = nmi = 0
    for k, (ch, i) in enumerate(full):
        if ch in 'xy':
            same = orient[(k, i)] == orient[(k, i + 1)]
            pos = same if ch == 'y' else (not same)
            if pos: npl += 1
            else: nmi += 1
    return npl, nmi

def kht_bgens(path):
    out = []
    for line in open(path, encoding='utf-8'):
        r = khtparse.parse_line(line)
        if not r: continue
        h, q, gens, arrows, rest = r
        gl, cyc, ok = khtparse.gens_with_gradings(h, q, gens, arrows)
        assert ok or not cyc
        for idem, hh, qq in gl:
            if idem == '⬮': out.append((hh, qq))
    return out

def predict(wordstr):
    r = analyse(wordstr)
    word = parse_word(wordstr)
    bw, tags = band_word(word)
    wr = r['wr']
    tw = [('x', 1), ('x', 1)] * wr if wr > 0 else [('y', 1), ('y', 1)] * (-wr)
    npl, nmi = tangle_signs(bw + tw)
    tshift = 2 * wr if wr > 0 else 0
    hs = tshift - nmi; qs = tshift + npl - 2 * nmi
    return r, hs, qs

if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(SI, '*.kht')))
    nfile = 0; nok = 0; problems = []
    top1 = 0; bot1 = 0; topdim = {}; botdim = {}
    for f in files:
        name = os.path.basename(f)[:-4]
        chain = os.path.join(SI, name, 'cxBNr-c2-qs')
        if not os.path.exists(chain): continue
        nfile += 1
        wordstr = open(f).read().split('\n')[1].strip()
        r, hs, qs = predict(wordstr)
        pts = kht_bgens(chain)
        # 1. Euler characteristic with the predicted shift (exact, no fitting)
        chi = {}
        for h, q in pts:
            chi[q] = chi.get(q, 0) + (-1) ** (h % 2)
        chi = {e: v for e, v in chi.items() if v}
        pred = {e + qs: v * (-1) ** (hs % 2) for e, v in r['alpha'].items()}
        ok_chi = (chi == pred)
        c = r['c']
        qmax = max(q for h, q in pts); qmin = min(q for h, q in pts)
        topg = [(h, q) for h, q in pts if q == qmax]; botg = [(h, q) for h, q in pts if q == qmin]
        ad1 = (len(r['loop1']) == 0); ad0 = (len(r['loop0']) == 0)
        ok_top = True; ok_bot = True
        if ad1:
            ok_top = (topg == [(4 * c + hs, r['M'] + qs)])
        else:
            ok_top = (qmax < r['M'] + qs)
        if ad0:
            ok_bot = (botg == [(hs, r['m'] + qs)])
        else:
            ok_bot = (qmin > r['m'] + qs)
        # all generators inside the cube range
        ok_range = all(hs <= h <= 4 * c + hs and r['m'] + qs <= q <= r['M'] + qs for h, q in pts)
        topdim[name] = len(topg); botdim[name] = len(botg)
        Ukht = (2 * c - 2 * r['wr'] + hs, r['d0'] + qs)
        flag = ok_chi and ok_top and ok_bot and ok_range
        nok += flag
        if not flag: problems.append((name, ok_chi, ok_top, ok_bot, ok_range))
        print('%-8s dimN=%3d shift=(%d,%d) chi_ok=%s top_ok=%s bot_ok=%s range_ok=%s adequate(1,0)=(%s,%s) topdim=%d botdim=%d U_kht=%s U_in_N=%s'
              % (name, len(pts), hs, qs, ok_chi, ok_top, ok_bot, ok_range, ad1, ad0, len(topg), len(botg), Ukht, Ukht in pts))
    print('chain files', nfile, 'all checks ok', nok, 'problems', problems)
    print('top dimension != 1:', {k: v for k, v in topdim.items() if v != 1})
    print('bottom dimension != 1:', {k: v for k, v in botdim.items() if v != 1})
