"""Cube-of-resolutions tools for kht++ Morse words (tangles drawn top to bottom).
Letters: x<i>, y<i> crossings on strands i,i+1; l<i>, r<i> caps creating strands i,i+1; u<i> cup joining i,i+1.
Resolutions (calibrated on kht++ output for Q_1 = l1.y0 and Q_-1 = l1.x0):
   y: 0-resolution = vertical (two strands pass), 1-resolution = horizontal (cup then cap);
   x: 0-resolution = horizontal, 1-resolution = vertical.
A state is a tuple of bits, one per crossing (in word order)."""
import re, itertools, sys
from indcx import reduced_betti, rank_f2

def parse(word):
    word = word.strip()
    if word.startswith('s.'): word = word[2:]
    out = []
    for tok in word.split('.'):
        tok = tok.strip()
        if not tok: continue
        m = re.fullmatch(r'([xylru])(\d+)', tok)
        if not m: raise ValueError(tok)
        out.append((m.group(1), int(m.group(2))))
    return out

def quotient_word(half, orient=True, twists=0):
    """kht++ Tangle::quotient(): half = slices of the symmetric half diagram. twists: number of framing pairs
    (positive: 'x1.x1' pairs, negative: 'y1.y1' pairs); kht++ uses twists = writhe of the symmetric diagram."""
    s = [('r', 1), ('r', 2)] if orient else [('l', 1), ('l', 2)]
    for (c, i) in half:
        if c in 'xy':
            if i == 0: s += [(c, 0), (c, 1), (c, 1), (c, 0)]
            else: s += [(c, 2 * i), (c, 2 * i - 1), (c, 2 * i + 1), (c, 2 * i)]
        elif c in 'lr':
            s += [(c, 2 * i - 1), (c, 2 * i)]
        elif c == 'u':
            s += [(c, 2 * i), (c, 2 * i - 1)]
    s.append(('u', 0))
    t = 'x' if twists > 0 else 'y'
    for _ in range(abs(twists)): s += [(t, 1), (t, 1)]
    return s

def word_str(slices): return '.'.join('%s%d' % s for s in slices)

class Diagram:
    def __init__(self, slices, ntop=1):
        self.slices = list(slices); self.ntop = ntop
        self.cross = [k for k, (c, i) in enumerate(self.slices) if c in 'xy']
        self.n = len(self.cross)
        self.cidx = {k: j for j, k in enumerate(self.cross)}
        # width check
        w = ntop
        for (c, i) in self.slices:
            if c in 'xy':
                if i + 1 >= w: raise ValueError('crossing out of range')
            elif c in 'lr':
                if i > w: raise ValueError('cap out of range')
                w += 2
            else:
                if i + 1 >= w: raise ValueError('cup out of range')
                w -= 2
        self.nbot = w

    def components_through_crossings(self):
        """number of closed components of the actual tangle (crossings as crossings) and the pairing of ends."""
        parent = {}
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            return a
        cnt = [0]
        def new():
            cnt[0] += 1; parent[cnt[0]] = cnt[0]; return cnt[0]
        cur = [new() for _ in range(self.ntop)]
        tops = list(cur); loops = 0
        for (c, i) in self.slices:
            if c in 'xy':
                cur[i], cur[i + 1] = cur[i + 1], cur[i]
            elif c in 'lr':
                a = new(); cur[i:i] = [a, a]
            else:
                a, b = find(cur[i]), find(cur[i + 1])
                if a == b: loops += 1
                else: parent[a] = b
                del cur[i:i + 2]
        return loops, [find(t) for t in tops], [find(b) for b in cur]

    def state(self, bits):
        """returns (nloops, conn) for the state with resolution bits (tuple/list of 0/1 per crossing).
        conn = tuple of pairs of end labels ('T',i)/('B',i) matched, sorted."""
        parent = [0]
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            return a
        def new():
            parent.append(len(parent)); return len(parent) - 1
        cur = [new() for _ in range(self.ntop)]
        tops = list(cur); loops = 0; j = 0
        for (c, i) in self.slices:
            if c in 'xy':
                b = bits[j]; j += 1
                horizontal = (b == 1) if c == 'y' else (b == 0)
                if horizontal:
                    a, bb = find(cur[i]), find(cur[i + 1])
                    if a == bb: loops += 1
                    else: parent[a] = bb
                    a = new(); cur[i] = a; cur[i + 1] = a
            elif c in 'lr':
                a = new(); cur[i:i] = [a, a]
            else:
                a, bb = find(cur[i]), find(cur[i + 1])
                if a == bb: loops += 1
                else: parent[a] = bb
                del cur[i:i + 2]
        ends = [('T', k, find(t)) for k, t in enumerate(tops)] + [('B', k, find(b)) for k, b in enumerate(cur)]
        byc = {}
        for (s, k, r) in ends: byc.setdefault(r, []).append((s, k))
        conn = tuple(sorted(tuple(sorted(v)) for v in byc.values()))
        return loops, conn

    def extreme_bits(self, which):
        """which = 'B' (all 1-resolutions) or 'A' (all 0)."""
        return [1] * self.n if which == 'B' else [0] * self.n

    def lando(self, which, close=None):
        """Lando data of the all-B or all-A state. close: optional extra slices appended (a closure), e.g. [('u',0)].
        Returns dict with loops, conn, self-chords (crossings whose flip creates one more loop without changing conn),
        essential chords (flip changes conn, loops unchanged), graph on self chords (adjacency = interlaced)."""
        D = self if close is None else Diagram(self.slices + list(close), self.ntop)
        bits = D.extreme_bits(which)
        l0, c0 = D.state(bits)
        selfc = []; ess = []; merge = []
        for j in range(D.n):
            bits[j] ^= 1
            l1, c1 = D.state(bits)
            bits[j] ^= 1
            if c1 != c0: ess.append(j); assert l1 == l0
            elif l1 == l0 + 1: selfc.append(j)
            else:
                assert l1 == l0 - 1, (l0, l1); merge.append(j)
        adj = {j: set() for j in selfc}
        for a, b in itertools.combinations(selfc, 2):
            bits[a] ^= 1; bits[b] ^= 1
            l2, c2 = D.state(bits)
            bits[a] ^= 1; bits[b] ^= 1
            if not (l2 == l0 + 2 and c2 == c0):
                adj[a].add(b); adj[b].add(a)
        return dict(loops=l0, conn=c0, selfc=selfc, ess=ess, merge=merge, adj=adj, n=D.n)

CONN_H = (( ('B', 0), ('B', 1) ), (('B', 2), ('T', 0)))   # 1-3 tangle 'l0' : T-b3, b1-b2  (idempotent of Q_0, kht symbol B/⬮)
CONN_V = (( ('B', 0), ('T', 0) ), (('B', 1), ('B', 2)))   # 1-3 tangle 'l1' : T-b1, b2-b3  (idempotent of Q_inf, ⬯)

def conn_name(conn):
    if conn == CONN_H: return 'H'
    if conn == CONN_V: return 'V'
    return str(conn)

if __name__ == '__main__':
    # sanity: rational tangles
    for w in ['l0', 'l1', 'l1.y0', 'l1.x0', 'l1.y0.y0', 'l0.x1.x1']:
        D = Diagram(parse(w), 1)
        print(w, [(bits, D.state(bits)[0], conn_name(D.state(bits)[1])) for bits in itertools.product((0, 1), repeat=D.n)])
    half = parse('l1.y0.y0.y1.u2')
    q = quotient_word(half, True, 0)
    print(word_str(q))
    D = Diagram(q, 1); print('crossings', D.n, 'closed comps', D.components_through_crossings())
    for which in 'AB':
        L = D.lando(which)
        print(which, 'loops', L['loops'], conn_name(L['conn']), 'self', len(L['selfc']), 'ess', len(L['ess']), 'merge', len(L['merge']),
              'betti Ind(G0):', reduced_betti(L['adj']))
