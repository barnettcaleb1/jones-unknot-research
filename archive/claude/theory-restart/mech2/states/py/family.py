#!/usr/bin/env python3
"""Run kht++ on half-diagram words (inside states/kht) and print N in cube coordinates of the twist-free band diagram."""
import sys, os, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/scripts')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
from bcube import *
import khtparse, run_words
from badblocks import describe
W = '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/kht'
CACHE = os.path.join(W, 'cache.jsonl')

def load_cache():
    c = {}
    if os.path.exists(CACHE):
        for l in open(CACHE):
            try:
                r = json.loads(l); c[r['word']] = r
            except Exception:
                pass
    return c

def N_points(rec):
    out = []
    for line in rec.get('bnchains', []):
        r = khtparse.parse_line(line)
        if not r:
            continue
        h, q, gens, arrows, rest = r
        gl, cyc, ok = khtparse.gens_with_gradings(h, q, gens, arrows)
        for idem, hh, qq in gl:
            if idem == '⬮':
                out.append((hh, qq))
    return out

def cube_coords(halfword, Npts):
    half = parse_word(halfword)
    word, lab, wr = quotient_word(half, with_twists=False)
    ncr = len(crossings_of(word)); ntw = 2 * abs(wr); xtw = wr > 0
    Pc = b_bracket(word)
    PN = collections.defaultdict(int)
    for h, q in Npts:
        PN[q] += (-1) ** (h % 2)
    PN = {e: c for e, c in PN.items() if c}
    s = max(PN) - max(Pc)
    ok = False
    for eps in (1, -1):
        if len(PN) == len(Pc) and all(PN.get(e + s, 0) == eps * c for e, c in Pc.items()):
            ok = True
    if not ok:
        return None
    base = s - (ntw if xtw else 0)
    nminus = (ncr + ntw - base) // 3
    hshift = (ntw if xtw else 0) - nminus
    return sorted((h - hshift, q - s) for h, q in Npts), ncr

def run(halfword, timeout=200):
    cache = load_cache()
    w = 's.' + halfword
    if w in cache and 'error' not in cache[w]:
        return cache[w]
    rec = run_words.run(W, w, timeout)
    open(CACHE, 'a').write(json.dumps(rec, ensure_ascii=False) + '\n')
    return rec

def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def report(halfword, timeout=200, verbose=True):
    rec = run(halfword, timeout)
    if 'error' in rec:
        print('%-40s ERROR %s' % (halfword, rec['error'])); return None
    Npts = N_points(rec)
    cc = cube_coords(halfword, Npts)
    if cc is None:
        print('%-40s euler mismatch' % halfword); return None
    pts, n = cc
    half = parse_word(halfword)
    word, lab, wr = quotient_word(half, with_twists=False)
    M, st = extreme_states(word, sign=1)
    m, st0 = extreme_states(word, sign=-1)
    qs = [q for h, q in pts]
    top = [(h, q) for h, q in pts if q == max(qs)]
    bot = [(h, q) for h, q in pts if q == min(qs)]
    hv = hull(pts)
    print('%-40s n=%d dimN=%d corners (0,%d)..(%d,%d)  bot %s defect %s | top %s defect %s' % (
        halfword, n, len(pts), m, n, M, bot, [(h, q - m) for h, q in bot], top, [(n - h, M - q) for h, q in top]))
    if verbose:
        print('      hull:', hv)
        print('      top-end blocks:', describe(half, 1)[0], '| bottom-end blocks:', describe(half, 0)[0])
    return pts

if __name__ == '__main__':
    for hw in sys.argv[1:]:
        report(hw)
