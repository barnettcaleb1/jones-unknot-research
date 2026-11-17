#!/usr/bin/env python3
"""Random half-diagram words whose strongly invertible knot has the Alexander polynomial of 5_1 / 10_132 (filter by |Delta(-1)| = 5,
|Delta(2)| = 11 * 2^k, |Delta(3)| = 61 * 3^k); candidates are then checked with kht++ (-c2 -s): reduced Khovanov rank 11 = 10_132 type."""
import sys, os, random, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
from alex_search import gen
from scansi import knot_kh, extremes
def strip_pow(v, p):
    v = abs(v)
    from fractions import Fraction
    v = Fraction(v).limit_denominator(10**9)
    n, d = v.numerator, v.denominator
    while n % p == 0 and n: n //= p
    while d % p == 0: d //= p
    return n, d
seed, count, maxlen = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rnd = random.Random(seed); seen = set(); cand = 0; hits = 0
out = open('find132_s%d.jsonl' % seed, 'a')
for it in range(count):
    w = gen(rnd, rnd.randint(5, maxlen))
    if not w or w in seen: continue
    seen.add(w)
    try:
        if alex.alex_eval(w, -1) != 5: continue
        if strip_pow(alex.alex_eval(w, 2), 2) != (11, 1): continue
        if strip_pow(alex.alex_eval(w, 3), 3) != (61, 1): continue
    except Exception: continue
    cand += 1
    r = knot_kh(w, 'f%d' % seed, tl=30)
    if not r: continue
    g, towers = r
    ex = extremes(g)
    rec = dict(word=w, rank=ex['rank'], top=ex['top'], bot=ex['bot'])
    if ex['rank'] != 5:
        hits += 1; out.write(json.dumps(rec) + '\n'); out.flush(); print('HIT', rec, flush=True)
print('tried', len(seen), 'alexander candidates', cand, 'non-5_1 hits', hits)
