"""certcheck.py MODE RESULTS.jsonl N -- explicit cross-check of saved certificates (fresh process).
MODE rep:    N rep certificates: my Wirtinger presentation (own Morse sweep), bijectivity, every relator, noncommuting
             pair among generators, order of the image group (own closure), replay.check verdict for comparison.
MODE tietze: N tietze certificates: replay.check (the project's independent checker) AND my replay (README spec, own
             canonical form) on my presentation; plus a transplant test: the same moves on a crossing-switched halfword
             (one letter x <-> y) must be rejected."""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import a2lib, homcount, replay
mode, path, N = sys.argv[1], sys.argv[2], int(sys.argv[3])
rows = [json.loads(l) for l in open(path)]
certs = []
for r in rows:
    for c in (r.get('info_certs') or []):
        if c['kind'] == mode: certs.append(c)
rng = random.Random(1)
rng.shuffle(certs)
certs = certs[:N]
ok_all = 0; out = []
for c in certs:
    hw = c['halfword']
    g, rels = a2lib.wirtinger_from_halfword(hw)
    if mode == 'rep':
        imgs = {int(k): tuple(v) for k, v in c['images'].items()}
        extra = sorted(set(imgs) - set(g))
        ok, msg = a2lib.check_rep(g, rels, imgs, c['degree'], tuple(c['noncommuting']))
        G = homcount.closure([imgs[x] for x in g])
        rp = replay.check(c)
        good = ok and rp[0] and len(G) > 1 and not extra and all(x in g for x in c['noncommuting'])
        ok_all += good
        out.append((hw[:50], len(g), c.get('group'), c['degree'], len(G), ok, rp[0], extra[:3]))
    else:
        mv = [tuple(m) for m in c['moves']]
        mine = a2lib.my_replay(g, rels, mv)
        rp = replay.check(c)
        # transplant: switch one random crossing letter
        toks = hw.split('.')
        idx = [i for i, t in enumerate(toks) if t and t[0] in 'xy']
        i = rng.choice(idx)
        toks[i] = ('y' if toks[i][0] == 'x' else 'x') + toks[i][1:]
        hw2 = '.'.join(toks)
        rp2 = replay.check(dict(c, halfword=hw2))
        good = mine[0] and rp[0] and not rp2[0]
        ok_all += good
        out.append((hw[:50], len(g), len(mv), mine[0], rp[0], 'transplant rejected' if not rp2[0] else 'TRANSPLANT ACCEPTED: ' + rp2[1]))
for o in out: print(o)
print('MODE', mode, 'checked', len(certs), 'all-good', ok_all)
