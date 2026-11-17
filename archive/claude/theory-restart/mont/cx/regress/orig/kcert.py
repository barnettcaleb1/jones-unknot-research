"""Fast certification of the covering knot K of a halfword (modular Jones + exact Alexander values).
VK_mod(word, a, p): V_K(t) at A = a mod p (t = A^-4), writhe-normalised; equals 1 for the unknot.
certify(word): returns ('nontrivial', reason) or ('V=1,Delta=1', info)."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex, kauffman
P = (1 << 61) - 1
def bracket_mod(word, a, p=P):
    full = alex.symmetrize(alex.parse(word))
    if full is None: return None
    ai = pow(a, p - 2, p)
    dl = (-(a * a) - ai * ai) % p
    state = {(1, 0): 1}
    for c, i in full:
        new = {}
        for m, v in state.items():
            if c in 'lr':
                k = kauffman.cap(m, i); new[k] = (new.get(k, 0) + v) % p
            elif c == 'u':
                m2, loop = kauffman.cup(m, i)
                new[m2] = (new.get(m2, 0) + (v * dl if loop else v)) % p
            else:
                x, y = (a, ai) if c == 'x' else (ai, a)
                new[m] = (new.get(m, 0) + v * x) % p
                m2, loop = kauffman.cup(m, i)
                q = v * dl % p if loop else v
                k = kauffman.cap(m2, i); new[k] = (new.get(k, 0) + q * y) % p
        state = {m: v for m, v in new.items() if v}
    tot = state.get((), 0)
    # <D> (with the outer loop) / delta
    return tot * pow(dl, p - 2, p) % p
def VK_mod(word, a, p=P):
    b = bracket_mod(word, a, p)
    if b is None: return None
    w = alex.writhe(word)
    f = (-pow(a, 3, p)) % p
    return b * pow(f, w % (p - 1), p) % p   # alex.writhe sign is opposite to the bracket crossing convention (CHECKED)
def certify(word, a=123456789):
    v = VK_mod(word, a)
    if v is None: return ('notknot', None)
    if v != 1: return ('nontrivial', 'V_K(t0) != 1')
    d = alex.alex_eval(word, -1)
    if d != 1: return ('nontrivial', 'det=%s (V=1!)' % d)
    for tt in (2, 3):
        x = alex.alex_eval(word, tt)
        if x != 1: return ('nontrivial', 'Delta(%d)=%s (V=1!)' % (tt, x))
    return ('V=1,Delta=1', None)
if __name__ == '__main__':
    import time
    for w in ['s.l1.l1.u2.u2', 's.l1.y0.y0.x1.u2', 's.l1.l1.x0.x0.x0.x0.x0.x0.y1.u2.u2']:
        t0 = time.time(); print(w, certify(w), round((time.time() - t0) * 1000, 1), 'ms')
