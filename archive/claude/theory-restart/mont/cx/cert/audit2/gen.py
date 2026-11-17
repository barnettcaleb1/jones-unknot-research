"""gen.py -- AUDIT-2 random halfword generator (own code) and halfword manipulations."""
import random


def rand_halfword(rng, nletters, maxhw=5, p_axis=0.25, p_cap=0.10, p_cup=0.10, prefix=None):
    """General halfword grammar: s . tokens ; hw = strands per side (starts at 1, must end at 1; always odd).
    l_s/r_s: 1 <= s <= hw+1 ; x_s/y_s: 0 <= s <= hw-1 ; u_s: 1 <= s <= hw-1 (needs hw >= 3)."""
    toks = ['s']; hw = 1
    for t in (prefix or []):
        toks.append(t)
        if t[0] in 'lr': hw += 2
        elif t[0] == 'u': hw -= 2
    steps = 0
    while True:
        if steps >= nletters:
            if hw == 1: break
            s = rng.randint(1, hw - 1); toks.append('u' + str(s)); hw -= 2; continue
        steps += 1
        r = rng.random()
        if hw == 1 and r < 0.8:
            s = rng.randint(1, 2); toks.append(rng.choice('lr') + str(s)); hw += 2; continue
        if r < p_cap and hw + 2 <= maxhw:
            s = rng.randint(1, hw + 1); toks.append(rng.choice('lr') + str(s)); hw += 2; continue
        if r < p_cap + p_cup and hw >= 3:
            s = rng.randint(1, hw - 1); toks.append('u' + str(s)); hw -= 2; continue
        if hw == 1 or rng.random() < p_axis:
            toks.append(rng.choice('xy') + '0')
        else:
            toks.append(rng.choice('xy') + str(rng.randint(1, hw - 1)))
    return '.'.join(toks)


def hw_tokens(hw):
    return hw.split('.')


def halfwidths(toks):
    """half-width before each token (index aligned with toks; toks[0] == 's')."""
    out = []; h = 1
    for t in toks:
        out.append(h)
        if t == 's': continue
        if t[0] in 'lr': h += 2
        elif t[0] == 'u': h -= 2
    out.append(h)
    return out


def inverse_letters(ws):
    return [('y' if t[0] == 'x' else 'x') + t[1:] for t in reversed(ws)]


def insert_cancelling(hw, rng, nins=3, wlen=6):
    """Insert W . W^-1 (W random in x_s/y_s with valid s) at random positions; isotopic knot, longer diagram."""
    toks = hw_tokens(hw)
    for _ in range(nins):
        H = halfwidths(toks)
        cand = [j for j in range(1, len(toks) + 1)]       # insert before toks[j] (j = len -> at the end)
        j = rng.choice(cand)
        h = H[j]
        letters = [rng.choice('xy') + str(rng.randint(0, h - 1)) for _ in range(wlen)]
        toks = toks[:j] + letters + inverse_letters(letters) + toks[j:]
    return '.'.join(toks)


def conjugate_insert(hw, rng, wlen=6, inner=None):
    """Insert W . inner . W^-1 where inner is a cancelling R2 pair; another cancelling pattern."""
    toks = hw_tokens(hw)
    H = halfwidths(toks)
    j = rng.randint(1, len(toks))
    h = H[j]
    letters = [rng.choice('xy') + str(rng.randint(0, h - 1)) for _ in range(wlen)]
    s = rng.randint(0, h - 1)
    mid = ['x' + str(s), 'x' + str(s), 'y' + str(s), 'y' + str(s)]
    toks = toks[:j] + letters + mid + inverse_letters(letters) + toks[j:]
    return '.'.join(toks)


def reduce_hw(hw):
    toks = hw_tokens(hw); out = []
    for t in toks:
        if out and t[0] in 'xy' and out[-1][0] in 'xy' and out[-1][1:] == t[1:] and out[-1][0] != t[0]:
            out.pop()
        else:
            out.append(t)
    return '.'.join(out)


def swap_sum_halfword(full):
    """K' given by a Morse word (initial cap implicit, final ('u',0)) -> halfword of K' # rK' (swap sum):
    s.l1.<K' ops on the right side>.u2 ; the new right cap of l1 is K''s initial cap, the strand from s runs
    outside on the right and is joined to K''s strand 1 by the final u2 (K' opened at its last cup)."""
    assert full[-1] == ('u', 0)
    toks = ['s', 'l1']
    for c, i in full[:-1]:
        toks.append(c + str(i + 1))
    toks.append('u2')
    return '.'.join(toks)
