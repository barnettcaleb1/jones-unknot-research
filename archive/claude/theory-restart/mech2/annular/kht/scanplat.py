#!/usr/bin/env python3
"""Random search over width-5 long-knot plats (top: open strand 0, caps (1,2), (3,4); a braid word on 5 strands; bottom: cups (0,1), (2,3),
open strand 4) for knots whose reduced Khovanov homology (F_2) has an extreme quantum degree supported in more than one homological degree."""
import sys, os, re, subprocess, random, json
from collections import defaultdict
KHT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
HERE = os.path.dirname(os.path.abspath(__file__))
def word(br): return 'r1.r3.' + '.'.join(br) + '.u0.u0'
def components(br):
    # union-find on strand segments: track connectivity through caps/cups
    # positions 0..4; identity of the arc at each position
    par = {}
    def f(a):
        while par.get(a, a) != a: a = par[a]
        return a
    def u(a, b): par[f(a)] = f(b)
    ids = ['top', 'c1', 'c1', 'c2', 'c2']
    for l in br:
        i = int(l[1:]); ids[i], ids[i+1] = ids[i+1], ids[i]
    u(ids[0], ids[1]); u(ids[2], ids[3]); u(ids[4], 'bot')
    roots = set(f(x) for x in ['top', 'c1', 'c2', 'bot'])
    return len(roots), f('top') == f('bot')
def khr(br, name, tl=30):
    d = os.path.join(HERE, 'examples', 'plat'); os.makedirs(d, exist_ok=True)
    fn = os.path.join(d, name + '.kht')
    open(fn, 'w').write('%% plat %s\n%s\n,1\n' % (' '.join(br), word(br)))
    out = os.path.join(d, name, 'cxCKh-c2')
    if os.path.exists(out): os.remove(out)
    try:
        subprocess.run(['perl', '-e', 'alarm %d; exec @ARGV' % tl, KHT, '-c2', 'examples/plat/%s.kht' % name], cwd=HERE, stdin=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=tl + 5)
    except Exception: return None
    if not os.path.exists(out): return None
    gens = []
    for line in open(out, encoding='utf-8'):
        m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)', line)
        if not m: continue
        h, q, chain = int(m.group(1)), int(m.group(2)), m.group(4)
        gens.append((h, q))
        if '>' in chain:
            mm = re.search(r'H(?:\^(\d+))?', chain); n_ = int(mm.group(1) or 1) if mm else 1
            gens.append((h + 1, q + 2 * n_))
    return gens
def extremes(gens):
    byq = defaultdict(list)
    for h, q in gens: byq[q].append(h)
    top, bot = max(byq), min(byq)
    e = lambda v: sum((-1) ** (x % 2) for x in v)
    return dict(rank=len(gens), top=(top, sorted(byq[top]), e(byq[top])), bot=(bot, sorted(byq[bot]), e(byq[bot])))
if __name__ == '__main__':
    N = int(sys.argv[1]); L = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    random.seed(seed)
    letters = [c + str(i) for c in 'xy' for i in range(4)]
    seen = set(); found = 0; ran = 0
    out = open(os.path.join(HERE, 'plat_found_L%d_s%d.jsonl' % (L, seed)), 'a')
    while ran < N:
        br = [random.choice(letters) for _ in range(L)]
        # no immediately cancelling pairs
        if any(br[i][1:] == br[i+1][1:] and br[i][0] != br[i+1][0] for i in range(L - 1)): continue
        nc, ok = components(br)
        if nc != 1 or not ok: continue
        g = khr(br, 's%d' % seed)
        ran += 1
        if not g: continue
        key = tuple(sorted(g))
        if key in seen: continue
        seen.add(key)
        ex = extremes(g)
        if len(set(ex['top'][1])) > 1 or len(set(ex['bot'][1])) > 1:
            found += 1
            rec = dict(word=word(br), rank=ex['rank'], top=ex['top'], bot=ex['bot'])
            out.write(json.dumps(rec) + '\n'); out.flush()
            print('IMPURE', rec, flush=True)
    print('ran', ran, 'distinct', len(seen), 'impure', found)
