#!/usr/bin/env python3
"""Referee: random half-diagram words (general and homogeneous), all checks of the sweep plus Theorem 2.4 checks."""
import random, sys, json, time
from ref import *
from symm import sym_info

def random_shape(rng, maxlen, maxw):
    """random sequence of letters ('X' = crossing of unspecified type) ending with width 1."""
    w = 1; out = []
    for step in range(maxlen):
        opts = []
        opts += [('X', 0)] * 3
        for i in range(1, w): opts += [('X', i)] * 2
        if w + 2 <= maxw:
            for i in range(1, w + 2): opts.append(('l', i))
        if w >= 3:
            for i in range(1, w): opts += [('u', i)] * 2
        ch, i = rng.choice(opts)
        out.append((ch, i))
        if ch == 'l': w += 2
        elif ch == 'u': w -= 2
    # close up: cups until width 1
    while w > 1:
        i = rng.randrange(1, w)
        out.append(('u', i)); w -= 2
    return out

def realise(shape, rng, mode):
    """mode 'neg'/'pos': choose x/y so that every crossing is negative/positive; 'rand': random letters."""
    word = [(('y' if ch == 'X' else ch), i) for ch, i in shape]
    try:
        info = half_info(word)
    except AssertionError:
        return None
    out = []
    for (ch, i), (ch0, _), s in zip(word, shape, info['signs']):
        if ch0 != 'X':
            out.append((ch, i)); continue
        # with letter y the sign is s; with x it is -s
        if mode == 'rand':
            out.append((rng.choice('xy'), i))
        else:
            want = -1 if mode == 'neg' else 1
            out.append(('y' if s == want else 'x', i))
    return out

def wstr(word):
    return 's.' + '.'.join('%s%d' % (ch, i) for ch, i in word)

def check(wordstr):
    r = analyse(wordstr)
    c = r['c']
    word = parse_word(wordstr)
    fails = []
    if not (r['t1'] == 'b' and r['t0'] == 'b'): fails.append('type')
    if r['M'] != 4 * c + r['k1']: fails.append('M')
    if r['m'] != -r['k0']: fails.append('m')
    if r['closure'] != {2 * c: 1}: fails.append('closure')
    v, d = r['Jcong']
    if not (abs(v - 1) < 1e-7 and abs(d) < 1e-7): fails.append('Jcong')
    for end in (1, 0):
        loop = r['loop%d' % end]; hp = r['hp%d' % end]
        for blk, places in loop.items():
            ch, i = word[blk]
            is_e = (ch == 'y') if end == 1 else (ch == 'x')
            exp = [0, 3] if (i == 0 or not is_e) else [1, 2]
            if i == 0 and is_e: fails.append('cut-loop')
            if sorted(places) != exp: fails.append('twins')
        if sorted(loop.keys()) != sorted(hp['bad']): fails.append('hp_bad%d' % end)
        if hp['k_pred'] != (r['k1'] if end == 1 else r['k0']): fails.append('hp_k%d' % end)
        if not hp['alpha_beta_ok']: fails.append('ab%d' % end)
        if (r['E1'] if end == 1 else r['E0']) != 4 ** len(loop): fails.append('E%d' % end)
        if not (hp['regions'] == hp['arcs'] + hp['loops'] + 1 and hp['curves'] == hp['arcs'] + 2 * hp['loops'] + 1): fails.append('regions%d' % end)
    si = sym_info(wordstr)
    if si['ncomp'] != 1: fails.append('sym-not-knot')
    homog = (abs(r['wr']) == c)
    extra = {}
    if homog and c > 0:
        end = 1 if r['wr'] < 0 else 0
        hp = r['hp%d' % end]
        l = hp['loops']; ca, co = r['c_axis'], r['c_o']
        k = r['k1'] if end == 1 else r['k0']
        exps = sorted(r['alpha'])
        if k != 2 * ca + 2 * l: fails.append('k=2ca+2l')
        if si['genus_can'] != co - l: fails.append('genus')
        if abs(si['writhe']) != si['n']: fails.append('sym-not-homog')
        g = co - l
        if end == 1:
            if r['d0'] - r['M'] != 2 * g: fails.append('gap')
            if exps[-1] > r['d0'] - 2 * g: fails.append('support')
        else:
            if r['m'] - r['d0'] != 2 * g: fails.append('gap')
            if exps[0] < r['d0'] + 2 * g: fails.append('support')
        nb = len(r['loop%d' % end])
        extra = dict(g=g, nb=nb, flat=(r['alpha'] == {r['d0']: 1}))
        if g == 0:
            if not extra['flat']: fails.append('genus0-not-flat')
            if nb != 0: fails.append('genus0-not-adequate')
        else:
            if extra['flat']: fails.append('FLAT-with-g>0')
    return r, fails, extra

if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    rng = random.Random(seed)
    t0 = time.time()
    stats = dict(tested=0, homog=0, g0=0, failed=0, maxc=0)
    seen = set()
    out = open('randtest_%d.log' % seed, 'w')
    tries = 0
    while stats['tested'] < N and tries < 200 * N:
        tries += 1
        shape = random_shape(rng, rng.randrange(1, 10), 7)
        mode = rng.choice(['neg', 'pos', 'rand', 'neg'])
        word = realise(shape, rng, mode)
        if word is None: continue
        ws = wstr(word)
        if ws in seen: continue
        ncr = sum(1 for ch, i in word if ch in 'xy')
        if ncr == 0 or ncr > 9: continue
        seen.add(ws)
        try:
            r, fails, extra = check(ws)
        except Exception as e:
            fails = ['EXC ' + repr(e)]; r = dict(c=None, wr=None); extra = {}
        stats['tested'] += 1
        if extra:
            stats['homog'] += 1
            if extra['g'] == 0: stats['g0'] += 1
        if r['c']: stats['maxc'] = max(stats['maxc'], r['c'])
        if fails:
            stats['failed'] += 1
            print('FAIL', ws, fails); sys.stdout.flush()
        out.write('%s c=%s wr=%s %s %s\n' % (ws, r['c'], r['wr'], extra, fails))
    out.close()
    print('seed', seed, stats, 'time %.1f' % (time.time() - t0))
