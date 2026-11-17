#!/usr/bin/env python3
"""Random 2-string tangles (1-3 Morse words, connectivity b: top-b3, b1-b2, no closed components) to test Theorem A outside the lens data.
Writes examples/rand/r<k>_T.kht (the tangle), r<k>_o.kht, r<k>_c.kht (the two components of T(0) = T.u0) and rand_info.json."""
import random, json, os, sys
from morse import parse, unparse, Trace, closed_to_11, jones_11, bracket

def random_word(rng, target, wmax):
    ev = []; w = 1; nc = 0
    for _ in range(400):
        if nc >= target and w == 3:
            return ev
        opts = []
        if w + 2 <= wmax: opts += ['cap'] * (3 if w == 1 else 1)
        if w >= 3 and nc >= 2: opts += ['cup'] * (2 if (nc >= target or w > 3) else 1)
        if w >= 2 and nc < target + 4: opts += ['cr'] * 8
        m = rng.choice(opts)
        if m == 'cap':
            ev.append(('l', rng.randint(0, w))); w += 2
        elif m == 'cup':
            ev.append(('u', rng.randint(0, w - 2))); w -= 2
        else:
            ev.append((rng.choice('xy'), rng.randint(0, w - 2))); nc += 1
    return None

def good_tangle(ev):
    tr = Trace(ev, 1)
    if len(tr.bottom) != 3: return None
    comps = tr.components()
    if len(comps) != 2: return None
    if tr.comp[tr.bottom[2]] != tr.comp[0]: return None
    if tr.comp[tr.bottom[0]] == tr.comp[0] or tr.comp[tr.bottom[1]] == tr.comp[0]: return None
    return tr

def with_letters(ev, tr):
    """rewrite cap letters according to tr.orient (so that kht++ reads exactly this orientation)"""
    out = []; k_cap = {k: a for a, b, kind, k in tr.links if kind == 'cap'}
    for k, (c, i) in enumerate(ev):
        if c in 'lr':
            a = k_cap[k]
            out.append(('l' if tr.orient[a] == -1 else 'r', i))
        else:
            out.append((c, i))
    return out

if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    want_both = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    want_one = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    rng = random.Random(seed)
    os.makedirs('examples/rand', exist_ok=True)
    info = {}; n_both = n_one = 0; tries = 0; seen = set()
    while (n_both < want_both or n_one < want_one) and tries < 2000000:
        tries += 1
        ev = random_word(rng, rng.randint(8, 18), rng.choice([5, 5, 7]))
        if ev is None: continue
        tr = good_tangle(ev)
        if tr is None: continue
        ev = with_letters(ev, tr)
        key = unparse(ev)
        if key in seen: continue
        ev0 = ev + [('u', 0)]
        t0 = Trace(ev0, 1, close11=True)
        if len(t0.components()) != 2: continue
        c_open = t0.comp[0]; c_closed = [c for c in t0.components() if c != c_open][0]
        # orientation of T(0) as kht++ reads the letters of ev: identical to tr.orient on the strands of T
        t0.orient = list(tr.orient)
        so = t0.subword(c_open); sc = closed_to_11(Trace(ev0, 1, close11=True).subword(c_closed))
        jo, wo = jones_11(so); jc, wc = jones_11(sc)
        ko = (jo != {0: 1}); kc = (jc != {0: 1})
        if ko and kc:
            if n_both >= want_both: continue
            n_both += 1
        elif ko or kc:
            if n_one >= want_one: continue
            n_one += 1
        else:
            continue
        seen.add(key)
        nm = 'r%03d' % len(info)
        lk2 = t0.linking2(c_open, c_closed)
        info[nm] = dict(word=key, open=unparse(so), closed=unparse(sc), lk2=lk2, ncross=len(t0.crossings), n_mixed=t0.ncross(c_open, c_closed),
                        jones_o=sorted(jo.items()), jones_c=sorted(jc.items()), both=(ko and kc))
        for tag, w in (('T', key), ('o', unparse(so)), ('c', unparse(sc))):
            open('examples/rand/%s_%s.kht' % (nm, tag), 'w').write('%% random tangle %s part %s (referee)\n%s\n,1\n' % (nm, tag, w))
    json.dump(info, open('rand_info.json', 'w'), indent=0)
    print('generated', len(info), 'tangles (both knotted: %d, one knotted: %d) in %d tries' % (n_both, n_one, tries))
    import collections
    print('crossing numbers:', sorted(collections.Counter(v['ncross'] for v in info.values()).items()))
    print('2lk values:', sorted(collections.Counter(v['lk2'] for v in info.values()).items()))
