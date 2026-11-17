#!/usr/bin/env python3
"""Scan closures of 3-braids (knots) for reduced Khovanov homology (F_2) whose top or bottom quantum degree is not pure
(supported in more than one homological degree) or has zero Euler characteristic.  Uses kht++ (time limit per call)."""
import sys, os, re, subprocess, itertools, json
from collections import defaultdict
KHT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
HERE = os.path.dirname(os.path.abspath(__file__))
def word(braid, n):
    w = ['r%d' % i for i in range(1, n)]
    for g in braid: w.append(('y' if g > 0 else 'x') + str(abs(g) - 1))
    for i in range(n - 1, 0, -1): w.append('u%d' % i)
    return '.'.join(w)
def is_knot(braid, n):
    p = list(range(n))
    for g in braid:
        i = abs(g) - 1; p[i], p[i+1] = p[i+1], p[i]
    seen = set(); c = 0
    for s in range(n):
        if s in seen: continue
        c += 1; t = s
        while t not in seen: seen.add(t); t = p[t]
    return c == 1
def khr(braid, n, name='scan', tl=60):
    d = os.path.join(HERE, 'examples', 'scan'); os.makedirs(d, exist_ok=True)
    fn = os.path.join(d, name + '.kht')
    open(fn, 'w').write('%% %s\n%s\n,1\n' % (braid, word(braid, n)))
    out = os.path.join(d, name, 'cxCKh-c2')
    if os.path.exists(out): os.remove(out)
    try:
        subprocess.run(['perl', '-e', 'alarm %d; exec @ARGV' % tl, KHT, '-c2', 'examples/scan/%s.kht' % name], cwd=HERE, stdin=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=tl + 5)
    except Exception as e:
        return None
    if not os.path.exists(out): return None
    gens = []
    for line in open(out, encoding='utf-8'):
        m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)', line)
        if not m: continue
        h, q, chain = int(m.group(1)), int(m.group(2)), m.group(4)
        gens.append((h, q))
        mm = re.search(r'H(?:\^(\d+))?', chain)
        if '—>' in chain or mm:
            n_ = int(mm.group(1) or 1) if mm else 1
            gens.append((h + 1, q + 2 * n_))
    return gens
def extremes(gens):
    byq = defaultdict(list)
    for h, q in gens: byq[q].append(h)
    top, bot = max(byq), min(byq)
    e = lambda v: sum((-1) ** (x % 2) for x in v)
    return dict(rank=len(gens), top=(top, sorted(byq[top]), e(byq[top])), bot=(bot, sorted(byq[bot]), e(byq[bot])))
if __name__ == '__main__':
    maxlen = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    seen = set(); found = []
    cnt = 0
    for L in range(3, maxlen + 1):
        for w in itertools.product((1, -1, 2, -2), repeat=L):
            # reduce: no cancelling adjacent letters (cyclically), canonical rotation, first letter 1 or -1
            if any(w[i] == -w[(i + 1) % L] for i in range(L)): continue
            rots = [w[i:] + w[:i] for i in range(L)]
            if w != min(rots): continue
            if not is_knot(w, 3): continue
            # skip words using only one generator sign pattern trivially alternating? keep all
            g = khr(list(w), 3)
            cnt += 1
            if g is None: continue
            ex = extremes(g)
            key = tuple(sorted(g))
            if key in seen: continue
            seen.add(key)
            imp = (len(set(ex['top'][1])) > 1) or (len(set(ex['bot'][1])) > 1)
            if imp:
                found.append((w, ex)); print('IMPURE', w, ex, flush=True)
    print('words run', cnt, 'distinct Kh', len(seen), 'impure', len(found))
