#!/usr/bin/env python3
"""Random half-diagram words (strongly invertible knots, generator of tools/alex_search.py): compute the reduced Khovanov homology of the
knot itself (kht++ -c2 -s) and record the words whose knot has an impure extreme quantum degree."""
import sys, os, re, subprocess, random, json, hashlib
from collections import defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
from alex_search import gen
KHT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
HERE = os.path.dirname(os.path.abspath(__file__))
def knot_kh(word, name, tl=20):
    d = os.path.join(HERE, 'examples', 'sik'); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, name + '.kht'), 'w').write('%% %s\n%s\n,1\n' % (word, word))
    outdir = os.path.join(d, name)
    for f in (os.listdir(outdir) if os.path.isdir(outdir) else []):
        if f.startswith('cx'): os.remove(os.path.join(outdir, f))
    try:
        subprocess.run(['perl', '-e', 'alarm %d; exec @ARGV' % tl, KHT, '-c2', '-s', 'examples/sik/%s.kht' % name], cwd=HERE,
                       stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=tl + 5)
    except Exception: return None
    fs = [f for f in (os.listdir(outdir) if os.path.isdir(outdir) else []) if f.startswith('cxCKh')]
    if not fs: return None
    gens = []; towers = 0
    for line in open(os.path.join(outdir, fs[0]), encoding='utf-8'):
        m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)', line)
        if not m: continue
        h, q, chain = int(m.group(1)), int(m.group(2)), m.group(4)
        gens.append((h, q))
        if '>' in chain:
            mm = re.search(r'H(?:\^(\d+))?', chain); n_ = int(mm.group(1) or 1) if mm else 1
            gens.append((h + 1, q + 2 * n_))
        else: towers += 1
    return gens, towers
def extremes(gens):
    byq = defaultdict(list)
    for h, q in gens: byq[q].append(h)
    top, bot = max(byq), min(byq)
    e = lambda v: sum((-1) ** (x % 2) for x in v)
    return dict(rank=len(gens), top=(top, sorted(byq[top]), e(byq[top])), bot=(bot, sorted(byq[bot]), e(byq[bot])))
if __name__ == '__main__':
    seed, count, maxlen = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rnd = random.Random(seed); seen = set(); kinds = set(); ran = 0
    out = open(os.path.join(HERE, 'si_found_s%d.jsonl' % seed), 'a')
    while ran < count:
        w = gen(rnd, rnd.randint(4, maxlen))
        if not w or w in seen: continue
        seen.add(w)
        r = knot_kh(w, 's%d' % seed)
        ran += 1
        if not r: continue
        g, towers = r
        if towers != 1 or len(g) < 5: continue
        key = tuple(sorted(g))
        if key in kinds: continue
        kinds.add(key)
        ex = extremes(g)
        if len(set(ex['top'][1])) > 1 or len(set(ex['bot'][1])) > 1:
            ncross = sum(1 for tok in w[2:].split('.') if tok[0] in 'xy')
            rec = dict(word=w, halfcross=ncross, rank=ex['rank'], top=ex['top'], bot=ex['bot'])
            out.write(json.dumps(rec) + '\n'); out.flush()
            print('IMPURE', rec, flush=True)
    print('ran', ran, 'distinct knot types (by Kh~)', len(kinds))
