"""Artin action of the type-B_4 Artin group (inside B_5: puncture 0 = axis, punctures 1..4 = legs 0..3) on F_5 = <g0..g4>.
Words in F_5 are tuples of nonzero ints: +(j+1) = g_j, -(j+1) = g_j^-1.
Letter map (consistent with rho2 letters): x_i -> sigma_i (i=1..3, exchanging punctures i, i+1), y_i -> sigma_i^-1,
x0 -> sigma_0^2 (full twist of the axis puncture with leg 0), y0 -> sigma_0^-2.  (A global mirror would be harmless:
the stabiliser of the straight cap arcs is mirror invariant.)"""
def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)
def inv(w): return tuple(-a for a in reversed(w))
def sigma_images(i, sign):
    """images of generators under sigma_i^sign (i = 0..3 exchanging punctures i and i+1); returns dict gen_index -> word"""
    a, b = i + 1, i + 2      # symbols for g_i, g_{i+1}
    if sign > 0:
        return {i: (a, b, -a), i + 1: (a,)}
    else:
        return {i: (b,), i + 1: (-b, a, b)}
def apply_aut(images, w):
    """apply the automorphism given by images (dict j -> word for g_j; others fixed) to the word w"""
    out = []
    for s in w:
        j = abs(s) - 1
        if j in images:
            img = images[j]
            out.extend(img if s > 0 else inv(img))
        else:
            out.append(s)
    return red(out)
def compose(*ims):
    """automorphism = first ims[0] then ims[1] ... as images dict of all 5 generators"""
    cur = {j: (j + 1,) for j in range(5)}
    for im in ims:
        cur = {j: apply_aut(im, w) for j, w in cur.items()}
    return cur
S = {}
for i in range(1, 4):
    S['x%d' % i] = sigma_images(i, +1)
    S['y%d' % i] = sigma_images(i, -1)
s0p = sigma_images(0, +1); s0m = sigma_images(0, -1)
def _sq(im):
    full = {j: apply_aut(im, (j + 1,)) for j in range(5)}
    return {j: apply_aut(im, w) for j, w in full.items()}
# sigma_0^2 : apply sigma_0 twice: first image then image again (substitution composition)
def _twice(im):
    first = {j: apply_aut(im, (j + 1,)) for j in range(5)}
    return {j: apply_aut(im, w) for j, w in first.items()}
S['x0'] = {j: w for j, w in _twice(s0p).items() if w != (j + 1,)}
S['y0'] = {j: w for j, w in _twice(s0m).items() if w != (j + 1,)}
def act(L, w):
    return apply_aut(S[L], w)
def cyc_red(w):
    w = list(w)
    while len(w) >= 2 and w[0] == -w[-1]:
        w = w[1:-1]
    return tuple(w)
def booth(s):
    """least rotation index (Booth's algorithm)"""
    S2 = s + s
    f = [-1] * len(S2)
    k = 0
    for j in range(1, len(S2)):
        sj = S2[j]
        i = f[j - k - 1]
        while i != -1 and sj != S2[k + i + 1]:
            if sj < S2[k + i + 1]: k = j - i - 1
            i = f[i]
        if sj != S2[k + i + 1]:
            if sj < S2[k]: k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k
def canon_cyc(w):
    w = cyc_red(w)
    if not w: return ()
    k = booth(w)
    return w[k:] + w[:k]
def group_key(word_letters):
    """exact group element key: images of all generators"""
    cur = tuple((j + 1,) for j in range(5))
    for L in word_letters:
        cur = tuple(act(L, w) for w in cur)
    return cur
if __name__ == '__main__':
    # sanity: relations hold as automorphisms
    def gk(ws): return group_key(ws)
    print('x1 y1 = 1', gk(['x1','y1']) == gk([]), 'x0 y0 = 1', gk(['x0','y0']) == gk([]))
    print('braid 121=212', gk(['x1','x2','x1']) == gk(['x2','x1','x2']), '232', gk(['x2','x3','x2']) == gk(['x3','x2','x3']))
    print('13=31', gk(['x1','x3']) == gk(['x3','x1']), '0 2 comm', gk(['x0','x2']) == gk(['x2','x0']))
    print('typeB 0101=1010', gk(['x0','x1','x0','x1']) == gk(['x1','x0','x1','x0']))
    print('0 1 not comm', gk(['x0','x1']) != gk(['x1','x0']))
    # product g0 g1 g2 g3 g4 preserved
    w = (1, 2, 3, 4, 5)
    for L in ['x0','y0','x1','y1','x2','y2','x3','y3']:
        assert act(L, w) == w, L
    print('boundary word fixed by all letters: OK')
