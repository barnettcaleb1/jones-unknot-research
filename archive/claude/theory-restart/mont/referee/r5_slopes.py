"""Exhaustive one-box J's by SLOPE: for every slope b/d (d odd, 0<=b<d, gcd=1) build a Gamma_0(2) word w with w(0) = b/d
(Y: s->s+1, X: s->s/(2s+1)), J = normalize(e1^T rho(w) e1) (depends only on b/d mod 1). Compare with vertical words."""
import sys
from math import gcd
from rlib import *
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools'); import alex, kauffman
def inv(p): return {-e: c for e, c in p.items()}
def word_for(b, d):
    # returns word (string over XxYy, leftmost acts last) with M(w)(0,1)^T = +-(b,d)
    w = []
    while b != 0:
        k = round(b / d); b -= k * d
        if k: w.append(('Y' if k > 0 else 'y') * abs(k))
        if b == 0: break
        # now |b| <= |d|/2 ; reduce d by multiples of 2b: (b,d) -> (b, d - 2jb)
        j = round(d / (2 * b)); d -= 2 * j * b
        if j: w.append(('X' if j > 0 else 'x') * abs(j))
        assert d % 2 != 0
    # we applied inverse maps: (b,d) -> Y^-k (b,d) -> X^-j ... ; so original = Y^k X^j ... (0,1)
    return ''.join(w)
def slope_of(w):
    M = [[1, 0], [0, 1]]
    mats = {'Y': [[1, 1], [0, 1]], 'y': [[1, -1], [0, 1]], 'X': [[1, 0], [2, 1]], 'x': [[1, 0], [-2, 1]]}
    for ch in w:
        A = mats[ch]
        M = [[M[0][0]*A[0][0] + M[0][1]*A[1][0], M[0][0]*A[0][1] + M[0][1]*A[1][1]], [M[1][0]*A[0][0] + M[1][1]*A[1][0], M[1][0]*A[0][1] + M[1][1]*A[1][1]]]
    return (M[0][1], M[1][1])
def onebox_Js(d):
    out = {}
    for b in range(0, d):
        if gcd(b, d) != 1: continue
        w = word_for(b, d)
        bb, dd = slope_of(w)
        assert (bb * d - b * dd) == 0 and abs(dd) == d, (b, d, w, bb, dd)
        out[b] = (w, normalize(apply(w)[0]))
    return out
if __name__ == '__main__':
    for p in (5, -3, 7, -5):
        w = 's.l1.y0.' + '.'.join((['x2'] if p > 0 else ['y2']) * abs(p)) + '.u1'
        Jw = J(w); det = alex.alex_eval(w, -1)
        br = kauffman.bracket(w); es = sorted(br)
        print('V_%d(y0): det %d, Jones span %d, Alexander %s' % (p, det, (es[-1] - es[0]) // 4, alex.alex_poly(w)))
        ob = onebox_Js(det)
        hits = [(b, ww) for b, (ww, Jn) in ob.items() if Jn in (Jw, normalize(inv(Jw)))]
        print('   all %d slopes b/%d: one-box J matching J(V_%d(y0)) up to mirror: %s' % (len(ob), det, p, hits))
        # which slopes give the same KNOT (Schubert key) as V_p(y0)? compare Jones of the realised one-box closure
        def key(pp):
            lo = min(pp); s = 1 if pp[lo] > 0 else -1
            return tuple(sorted((e - lo, s * c) for e, c in pp.items()))
        kV = {key(br), key(inv(br))}
        same = []
        for b, (ww, Jn) in ob.items():
            # realise slope word as nested body and compute knot Jones
            s = ''
            for ch in reversed(ww):
                if ch == 'Y': s = ('y0.' + s) if s else 'y0'
                elif ch == 'y': s = ('x0.' + s) if s else 'x0'
                elif ch == 'X': s = 'r2.x1.' + (s + '.' if s else '') + 'u1'
                elif ch == 'x': s = 'r2.y1.' + (s + '.' if s else '') + 'u1'
            if not s: continue
            bw = kauffman.bracket('s.' + s)
            if bw and key(bw) in kV:
                same.append((b, ww, fmt(Jn)))
        print('   slopes whose one-box closure is the same knot (Jones up to mirror):', [(x[0], x[1]) for x in same])
        for x in same: print('      b=%d J=%s' % (x[0], x[2]))
        print('   J(V_%d(y0)) = %s' % (p, fmt(Jw)))
