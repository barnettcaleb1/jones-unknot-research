"""platcheck.py -- AUDIT-2: |Hom(pi, G)| from MY Wirtinger presentation vs from MY plat presentation (Artin action on
the Morse sweep: no arcs, no signs).  Independent validation that my (= the checker's) Wirtinger presentation presents
the right group."""
import sys, random, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
import a2lib, gen, homcount
pmul, pinv = a2lib.pmul, a2lib.pinv

def plat(full):
    g = 1; pos = [(g,), (-g,)]; gens = [g]; rels = []
    for c, i in full:
        if c in 'lr':
            g += 1; gens.append(g); pos[i:i] = [(g,), (-g,)]
        elif c == 'u':
            rels.append(a2lib.red(pos[i] + pos[i + 1])); del pos[i:i + 2]
        elif c == 'x':
            a, b = pos[i], pos[i + 1]; pos[i], pos[i + 1] = a2lib.red(a + b + a2lib.inv(a)), a
        elif c == 'y':
            a, b = pos[i], pos[i + 1]; pos[i], pos[i + 1] = b, a2lib.red(a2lib.inv(b) + a + b)
    return gens, rels

def ev(w, img, d):
    acc = tuple(range(d))
    for a in w: acc = pmul(acc, img[a] if a > 0 else pinv(img[-a]))
    return acc

def count_plat(gens, rels, G):
    G = list(G); d = len(G[0]); e = tuple(range(d))
    seen = set(); total = 0
    for x in G:
        if x in seen: continue
        cl = sorted(set(pmul(pmul(h, x), pinv(h)) for h in G)); seen |= set(cl)
        cnt = 0
        for rest in itertools.product(cl, repeat=len(gens) - 1):
            img = {gens[0]: cl[0]}
            for gg, v in zip(gens[1:], rest): img[gg] = v
            if all(ev(r, img, d) == e for r in rels): cnt += 1
        total += cnt * len(cl)
    return total

rng = random.Random(31337)
groups = {'S3': homcount.sym(3), 'S4': homcount.sym(4)}
A5 = homcount.alt(5)
agree = 0; disagree = 0; tested = 0; a5t = 0
while tested < 80:
    hw = gen.rand_halfword(rng, rng.randint(3, 14), maxhw=3)
    full = a2lib.full_of(hw); D = a2lib.morse_diagram(full)
    if D is None or D['n'] < 3: continue
    pg, pr = plat(full)
    if len(pg) > 5: continue
    wg, wr = a2lib.wirtinger_from_full(full)
    tested += 1
    row = []
    gl = list(groups.items()) + ([('A5', A5)] if (len(pg) <= 3 and a5t < 25) else [])
    if len(pg) <= 3 and a5t < 25: a5t += 1
    ok = True
    for name, G in gl:
        a = homcount.count_homs(wg, wr, G); b = count_plat(pg, pr, G)
        row.append((name, a, b))
        if a != b: ok = False
    agree += ok; disagree += (not ok)
    if not ok: print('DISAGREE', hw, row)
print('knots', tested, 'agree', agree, 'disagree', disagree, '(A5 included for', a5t, 'knots)')
