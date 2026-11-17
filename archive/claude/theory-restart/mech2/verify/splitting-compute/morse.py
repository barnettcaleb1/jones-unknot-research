#!/usr/bin/env python3
"""Referee's own Morse-word tools (written from scratch for verify/splitting-compute; nothing imported from the lenses).

Morse word (kht++ convention, top to bottom): x<i> crossing, over-strand from top-left to bottom-right;
y<i> crossing, over-strand from top-right to bottom-left; l<i>/r<i> cap inserting two new strands at positions i,i+1
(l: left leg oriented down, right leg up; r: left leg up, right leg down); u<i> cup joining strands i,i+1.
"""
import re, collections

def parse(word):
    out = []
    for tok in word.strip().strip('.').split('.'):
        tok = tok.strip()
        if not tok:
            continue
        m = re.fullmatch(r'([xylru])(\d+)', tok)
        if not m:
            raise ValueError('bad token %r' % tok)
        out.append((m.group(1), int(m.group(2))))
    return out

def unparse(events):
    return '.'.join('%s%d' % e for e in events)

class Trace:
    """Trace the monotone strands of a Morse word with ntop top ends.
    Strand ids: 0..ntop-1 = top ends; each cap creates two new ids (left leg, right leg)."""
    def __init__(self, events, ntop=1, close11=False):
        self.events = list(events)
        self.ntop = ntop
        cur = list(range(ntop)); nxt = ntop
        self.cuts = [list(cur)]
        self.links = []       # (a, b, kind, event index): a,b joined at a cap or cup => opposite vertical orientation
        self.crossings = []   # (event index, letter, strand at top-left, strand at top-right)
        for k, (c, i) in enumerate(self.events):
            if c in 'xy':
                if not (0 <= i < len(cur) - 1):
                    raise ValueError('crossing index out of range at event %d (%s%d), width %d' % (k, c, i, len(cur)))
                self.crossings.append((k, c, cur[i], cur[i + 1]))
                cur[i], cur[i + 1] = cur[i + 1], cur[i]
            elif c in 'lr':
                if not (0 <= i <= len(cur)):
                    raise ValueError('cap index out of range at event %d' % k)
                a, b = nxt, nxt + 1; nxt += 2
                cur[i:i] = [a, b]
                self.links.append((a, b, 'cap', k))
            else:
                if not (0 <= i < len(cur) - 1):
                    raise ValueError('cup index out of range at event %d' % k)
                a, b = cur[i], cur[i + 1]
                self.links.append((a, b, 'cup', k))
                del cur[i:i + 2]
            self.cuts.append(list(cur))
        self.nstrands = nxt
        self.bottom = list(cur)
        # components (union-find over monotone strands)
        par = list(range(nxt))
        def find(a):
            while par[a] != a:
                par[a] = par[par[a]]; a = par[a]
            return a
        for a, b, kind, k in self.links:
            par[find(a)] = find(b)
        self.closed11 = False
        if close11:
            if not (ntop == 1 and len(self.bottom) == 1):
                raise ValueError('close11 needs a 1-1 tangle')
            par[find(0)] = find(self.bottom[0]); self.closed11 = True
        self.comp = [find(a) for a in range(nxt)]
        # orientation: +1 up, -1 down; top ends up; links force opposite orientation; closure forces equal orientation
        adj = collections.defaultdict(list)
        for a, b, kind, k in self.links:
            adj[a].append((b, -1)); adj[b].append((a, -1))
        if close11 and self.bottom[0] != 0:
            adj[0].append((self.bottom[0], 1)); adj[self.bottom[0]].append((0, 1))
        o = [0] * nxt
        order = list(range(nxt))
        for s in order:
            if o[s] != 0:
                continue
            o[s] = 1   # top ends, and the first (left) leg of the first cap of a closed component: up
            st = [s]
            while st:
                a = st.pop()
                for b, sg in adj[a]:
                    if o[b] == 0:
                        o[b] = o[a] * sg; st.append(b)
                    elif o[b] != o[a] * sg:
                        raise ValueError('inconsistent orientation')
        self.orient = o

    def components(self):
        d = collections.OrderedDict()
        for s in range(self.nstrands):
            d.setdefault(self.comp[s], []).append(s)
        return d

    def sign(self, cr):
        k, c, a, b = cr
        parallel = (self.orient[a] == self.orient[b])
        return 1 if ((c == 'y') == parallel) else -1

    def writhe(self, comp=None):
        w = 0
        for cr in self.crossings:
            k, c, a, b = cr
            if comp is None or (self.comp[a] == comp and self.comp[b] == comp):
                w += self.sign(cr)
        return w

    def linking2(self, c1, c2):
        """twice the linking number (sum of signs of mixed crossings)"""
        s = 0
        for cr in self.crossings:
            k, c, a, b = cr
            if {self.comp[a], self.comp[b]} == {c1, c2} and c1 != c2:
                s += self.sign(cr)
        return s

    def ncross(self, c1, c2=None):
        if c2 is None: c2 = c1
        return sum(1 for (k, c, a, b) in self.crossings if {self.comp[a], self.comp[b]} == {c1, c2})

    def subword(self, target):
        """Morse word of the sub-diagram formed by the component `target` alone, cap letters from self.orient."""
        cur = list(range(self.ntop)); nxt = self.ntop
        out = []
        cnt = lambda i: sum(1 for s in cur[:i] if self.comp[s] == target)
        for (c, i) in self.events:
            if c in 'xy':
                a, b = cur[i], cur[i + 1]
                if self.comp[a] == target and self.comp[b] == target:
                    out.append((c, cnt(i)))
                cur[i], cur[i + 1] = b, a
            elif c in 'lr':
                a, b = nxt, nxt + 1; nxt += 2
                if self.comp[a] == target:
                    out.append(('l' if self.orient[a] == -1 else 'r', cnt(i)))
                cur[i:i] = [a, b]
            else:
                a, b = cur[i], cur[i + 1]
                if self.comp[a] == target:
                    assert self.comp[b] == target
                    out.append(('u', cnt(i)))
                del cur[i:i + 2]
        return out

def closed_to_11(events):
    """A closed knot diagram (0 top, 0 bottom ends) whose first event is a cap at index 0 with left leg up ('r0'):
    cut it open at the top of that cap.  New word: top end = old left leg; 'l1' creates the old right leg (down) and an extra
    strand (up) which runs down on the far right to the bottom end."""
    c, i = events[0]
    if not (c in 'lr' and i == 0):
        raise ValueError('first event must be a cap at 0')
    if c != 'r':
        raise ValueError('expected left leg up (r0); got %s' % c)
    return [('l', 1)] + list(events[1:])

# ---------------- Laurent polynomials in one variable: dict exponent -> int ----------------
def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        v = r.get(e, 0) + c
        if v: r[e] = v
        elif e in r: del r[e]
    return r
def pmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = e1 + e2; v = r.get(e, 0) + c1 * c2
            if v: r[e] = v
            elif e in r: del r[e]
    return r
def pshift(p, s, c=1):
    return {e + s: v * c for e, v in p.items()}
DELTA = {2: -1, -2: -1}
def pstr(p, var='A'):
    if not p: return '0'
    return ' + '.join('%d*%s^%d' % (p[e], var, e) for e in sorted(p))

# ---------------- Kauffman bracket by sweeping the Morse word ----------------
def bracket(events, ntop=1):
    """Returns dict: matching (tuple of partner indices over the points [top ends..., bottom strands...]) -> polynomial in A.
    <x> = A <cup-cap> + A^-1 <identity>,  <y> = A <identity> + A^-1 <cup-cap>,  circle = -A^2 - A^-2."""
    if ntop % 2 == 0 and ntop > 0:
        raise NotImplementedError
    # initial state: ntop top points each matched to the strand below it
    w = ntop
    m0 = tuple(list(range(ntop, 2 * ntop)) + list(range(0, ntop)))
    state = {m0: {0: 1}}
    def add(st, m, p):
        if m in st:
            r = padd(st[m], p)
            if r: st[m] = r
            else: del st[m]
        elif p:
            st[m] = p
    for (c, i) in events:
        new = {}
        p_ = ntop + i
        if c in 'lr':
            for m, pol in state.items():
                mm = [x + 2 if x >= p_ else x for x in m]
                mm[p_:p_] = [p_ + 1, p_]
                add(new, tuple(mm), pol)
            w += 2
        elif c == 'u':
            q_ = p_ + 1
            for m, pol in state.items():
                mm = list(m)
                if mm[p_] == q_:
                    pol2 = pmul(pol, DELTA)
                else:
                    a, b = mm[p_], mm[q_]
                    mm[a] = b; mm[b] = a
                    pol2 = pol
                del mm[p_:q_ + 1]
                mm = [x - 2 if x > q_ else x for x in mm]
                add(new, tuple(mm), pol2)
            w -= 2
        else:
            q_ = p_ + 1
            cid = -1 if c == 'x' else 1      # exponent of A on the identity smoothing
            for m, pol in state.items():
                add(new, m, pshift(pol, cid))
                mm = list(m)
                if mm[p_] == q_:
                    pol2 = pmul(pol, DELTA)
                else:
                    a, b = mm[p_], mm[q_]
                    mm[a] = b; mm[b] = a
                    mm[p_] = q_; mm[q_] = p_
                    pol2 = pol
                add(new, tuple(mm), pshift(pol2, -cid))
            state = new
            continue
        state = new
    return state

def jones_11(events):
    """Normalised Jones polynomial (unknot = 1) of the closure of a 1-1 tangle that is a KNOT, as dict: exponent of q (= 2*exponent of t) -> coeff,
    in the convention V = sum (-1)^h q^q of kht++ (right-handed trefoil q^2 + q^6 - q^8)."""
    tr = Trace(events, 1, close11=True)
    st = bracket(events, 1)
    assert list(st.keys()) == [(1, 0)], st.keys()
    pol = st[(1, 0)]
    w = tr.writhe()
    # V = (-A^3)^(-w) <D>,  t = A^-4, q = t^(1/2)  => A^e -> q^(-e/2)
    out = {}
    for e, c in pol.items():
        e2 = e - 3 * w
        assert e2 % 2 == 0
        out[-e2 // 2] = out.get(-e2 // 2, 0) + c * (-1) ** (w % 2)
    return {k: v for k, v in out.items() if v}, w

if __name__ == '__main__':
    # self tests
    ev = parse('r1.y0.y0.y0.u1')
    print('rh trefoil:', jones_11(ev))
    ev = parse('r1.x0.x0.x0.u1')
    print('lh trefoil:', jones_11(ev))
    ev = parse('r1.y0.x0.u1')
    print('unknot (R2):', jones_11(ev))
    ev = parse('r1.x0.u1')
    print('unknot (R1):', jones_11(ev))
    ev = parse('r1.y0.y0.y0.y0.y0.u1')
    print('T(2,5):', jones_11(ev))
    ev = parse('r1.r3.x2.y1.x2.y1.u0.u1')   # some closure
    try:
        print('test:', jones_11(ev))
    except Exception as ex:
        print('test raised', ex)
