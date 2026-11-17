"""Geometric intersection numbers of simple closed curves in S_{0,6} via the free group.

S_{0,6} minus a disk around puncture 6 = D_5, pi_1 = F_5 = <x1..x5>, with x6 = (x1...x5)^-1.
Curves: conjugacy classes; c_{123} = [x1 x2 x3]. Braids act by the Artin automorphisms of F_6
(sigma_i: x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i), then x6 is eliminated.
Intersection count: linked pairs of axes in the Cayley tree of the rose, using the ribbon
(planar) cyclic order at the vertex; each linked pair counted once at the first vertex of the
shared segment (Cohen-Lustig / Birman-Series style).  Letters: +k = x_k, -k = x_k^-1.
"""
import sys

def reduce_word(w):
    out = []
    for a in w:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return out
def cyc_reduce(w):
    w = reduce_word(w)
    while len(w) >= 2 and w[0] == -w[-1]:
        w = w[1:-1]
    return w
def inv(w):
    return [-a for a in reversed(w)]

def artin(g, w):
    i = abs(g); out = []
    for a in w:
        k, s = abs(a), (1 if a > 0 else -1)
        if g > 0:
            if k == i:
                img = [i, i + 1, -i]
            elif k == i + 1:
                img = [i]
            else:
                img = [k]
        else:
            if k == i:
                img = [i + 1]
            elif k == i + 1:
                img = [-(i + 1), i, i + 1]
            else:
                img = [k]
        out += img if s > 0 else inv(img)
    return reduce_word(out)
def act(word, w):
    for g in reversed(word):
        w = artin(g, w)
    return w
def kill6(w, n=6):
    out = []
    for a in w:
        if abs(a) == n:
            rep = inv(list(range(1, n)))        # x6 = (x1...x5)^-1
            out += rep if a > 0 else inv(rep)
        else:
            out.append(a)
    return cyc_reduce(out)

def make_order(n, option):
    # linear (left-to-right) order of half-edge labels at the base vertex; boundary gap closes it
    order = []
    for k in range(1, n + 1):
        order += ([k, -k] if option == 0 else [-k, k])
    return order

class Ribbon:
    def __init__(self, n, option):
        self.order = make_order(n, option)
        self.pos = {lab: t for t, lab in enumerate(self.order)}
        self.m = len(self.order)
    def side(self, h_in, h_out, h):
        """cyclic order: is h strictly between h_out and h_in going 'counterclockwise' (+1) or other (-1)"""
        a, b, c = self.pos[h_out], self.pos[h_in], self.pos[h]
        # going from a upward (mod m) do we hit c before b?
        da = (c - a) % self.m; db = (b - a) % self.m
        return 1 if da < db else -1

def letter_at(w, k):
    return w[k % len(w)]

def count_crossings(u, v, R, maxwalk=None):
    """number of linked axis pairs of cyclic words u, v (both cyclically reduced, primitive)"""
    L = maxwalk or 4 * (len(u) + len(v)) + 10
    total = 0
    nu, nv = len(u), len(v)
    for i in range(nu):
        Up = lambda k: letter_at(u, i + k)            # forward letters from vertex i
        Um = lambda k: -letter_at(u, i - 1 - k)       # backward letters from vertex i
        for j in range(nv):
            Vp = lambda k: letter_at(v, j + k)
            Vm = lambda k: -letter_at(v, j - 1 - k)
            if Um(0) in (Vp(0), Vm(0)):
                continue  # not the start of the shared segment
            # follow the shared segment along U+
            if Up(0) == Vp(0):
                k = 0
                while k < L and Up(k) == Vp(k):
                    k += 1
                if k >= L:
                    continue  # same axis (self-pairing)
                vx = Vm(0)                      # v's other half-edge at start vertex
                vy = Vp(k)                      # v's continuing half-edge at end vertex
                uy_in, uy_out = -Up(k - 1), Up(k)
            elif Up(0) == Vm(0):
                k = 0
                while k < L and Up(k) == Vm(k):
                    k += 1
                if k >= L:
                    continue
                vx = Vp(0)
                vy = Vm(k)
                uy_in, uy_out = -Up(k - 1), Up(k)
            else:
                # single shared vertex: v's two half-edges must lie on opposite sides of u
                s1 = R.side(Um(0), Up(0), Vp(0))
                s2 = R.side(Um(0), Up(0), Vm(0))
                if s1 != s2:
                    total += 1
                continue
            sx = R.side(Um(0), Up(0), vx)
            sy = R.side(uy_in, uy_out, vy)
            # at the start vertex u comes in via Um(0) and leaves via Up(0);
            # at the end vertex u comes in via -Up(k-1), leaves via Up(k)
            if sx != sy:
                total += 1
    return total

def curve(word, base=(1, 2, 3)):
    w = act(word, list(base))
    return kill6(w)

if __name__ == '__main__':
    n = 5
    for option in (0, 1):
        R = Ribbon(n, option)
        tests = {
            'self2(x1x2)': count_crossings([1, 2], [1, 2], R),
            'self2(x1x2x3)': count_crossings([1, 2, 3], [1, 2, 3], R),
            'self2(x1^2x2)': count_crossings([1, 1, 2], [1, 1, 2], R),
            'i(bdry,x2x3)': count_crossings([1, 2, 3, 4, 5], [2, 3], R),
            'i(x1x2x3, x2x3x4)': count_crossings([1, 2, 3], [2, 3, 4], R),
            'i(x2x3, x1x3)': count_crossings([2, 3], [1, 3], R),
            'i(x1x2,x2x3)': count_crossings([1, 2], [2, 3], R),
            'i(x1x2,x3x4)': count_crossings([1, 2], [3, 4], R),
            'i(x1x2x3,x2x3x4)': count_crossings([1, 2, 3], [2, 3, 4], R),
        }
        print('option', option, tests)
