#!/usr/bin/env python3
"""
twist.py -- builders for PD codes (same convention as bracket.py):

  braid_closure_pd(word, n_strands=None)   closure of a braid word
  plat_closure_pd(word, n_strands)         plat closure (n_strands even)
  insert_full_twists(pd, e1, e2, n, ...)   replace the identity 2-tangle
                                           formed by two edges e1, e2 that
                                           bound a common face by 2n crossings
  clasp_unknot_pd()                        2-crossing clasp diagram of the
                                           unknot (band edges 2 and 4)
  parallel_edge_pairs(pd)                  all (e1, e2, face) twist sites

Braid words are lists of nonzero ints: +i = sigma_i, -i = sigma_i^-1.
Strands run UPWARD.  sigma_i: the strand at position i (left) passes OVER
the strand at position i+1 while they swap.  With all strands oriented
upward sigma_i is a POSITIVE crossing (right-handed), sigma_i^-1 negative.

Twist handedness in insert_full_twists: n > 0 inserts crossings of the
sigma type (the strand entering the twist box at its bottom-left passes
over), n < 0 the sigma^-1 type.  Whether these are positive or negative
crossings depends on the relative orientation of the two strands (parallel:
sigma type is positive; antiparallel: sigma type is negative).

All emitted PD codes have labels 1..2n, consecutive along the orientation
of each component (so both the a->c under-strand rule and the numbering
rule of bracket.py agree).
"""

from bracket import Diagram

# slot geometry used for every crossing created here: the crossing sits in a
# box with strands entering at bottom-left (BL), bottom-right (BR) and
# leaving at top-left (TL), top-right (TR).  Slots are listed COUNTER-
# CLOCKWISE and slots 0, 2 are the UNDER strand.
#   sigma   type:  under BR -> TL   ccw from BR: [BR, TR, TL, BL]
#   sigma^-1 type: under BL -> TR   ccw from BL: [BL, BR, TR, TL]
_SIGMA = {"BR": 0, "TR": 1, "TL": 2, "BL": 3}
_SIGMA_INV = {"BL": 0, "BR": 1, "TR": 2, "TL": 3}


class Builder:
    """Unoriented 4-valent planar diagram with over/under data.
    Crossing slots are in counterclockwise order; slots 0 and 2 carry the
    under strand.  conn maps (crossing, slot) -> (crossing, slot)."""

    def __init__(self):
        self.ncross = 0
        self.conn = {}

    def new_crossing(self):
        self.ncross += 1
        return self.ncross - 1

    def connect(self, p, q):
        if p in self.conn or q in self.conn:
            raise ValueError("port already connected: %r / %r" % (p, q))
        self.conn[p] = q
        self.conn[q] = p

    def disconnect(self, p):
        q = self.conn.pop(p)
        self.conn.pop(q)
        return q

    @classmethod
    def from_pd(cls, pd):
        """Builder from a PD code; crossing i's slot s is the s-th entry."""
        b = cls()
        D = Diagram(pd)
        b.ncross = D.n
        for e, (p, q) in D.occ.items():
            b.connect(p, q)
        return b

    def pd_code(self, starts=None):
        """Emit a PD code.  `starts` is an optional list of darts
        (crossing, slot) meaning 'enter this crossing at this slot'; the
        traversal from a start fixes the orientation of that component.
        Components without a start get an arbitrary orientation."""
        for i in range(self.ncross):
            for s in range(4):
                if (i, s) not in self.conn:
                    raise ValueError("port (%d,%d) not connected" % (i, s))
        label = {}
        under_entry = {}
        visited = set()
        darts = list(starts or []) + [(i, s) for i in range(self.ncross) for s in range(4)]
        nxt = 1
        for d0 in darts:
            if d0 in visited:
                continue
            cur = d0
            while cur not in visited:
                visited.add(cur)
                i, s = cur
                if s in (0, 2):
                    under_entry[i] = s
                out = (i, (s + 2) % 4)
                visited.add(out)
                nxt_dart = self.conn[out]
                label[out] = nxt
                label[nxt_dart] = nxt
                nxt += 1
                cur = nxt_dart
        pd = []
        for i in range(self.ncross):
            u = under_entry[i]
            pd.append([label[(i, (u + k) % 4)] for k in range(4)])
        return pd


def _braid_builder(word, n_strands):
    """Lay out the braid; returns (builder, bottom_darts, top_darts), where
    bottom_darts[k] is the entry port of the first crossing met by the strand
    starting at position k (None if the strand meets no crossing) and
    top_darts[k] the exit port of the last crossing at position k."""
    b = Builder()
    top = [None] * (n_strands + 1)
    bottom = [None] * (n_strands + 1)
    for g in word:
        if g == 0 or abs(g) >= n_strands:
            raise ValueError("generator %d invalid for %d strands" % (g, n_strands))
        i = abs(g)
        c = b.new_crossing()
        slot = _SIGMA if g > 0 else _SIGMA_INV
        for pos, port in ((i, "BL"), (i + 1, "BR")):
            entry = (c, slot[port])
            if top[pos] is None:
                bottom[pos] = entry
            else:
                b.connect(top[pos], entry)
        top[i] = (c, slot["TL"])
        top[i + 1] = (c, slot["TR"])
    return b, bottom, top


def braid_closure_pd(word, n_strands=None):
    """PD code of the closure of a braid word.  Every strand must meet at
    least one crossing (a PD code cannot hold a crossingless component)."""
    word = list(word)
    if n_strands is None:
        n_strands = max(abs(g) for g in word) + 1
    b, bottom, top = _braid_builder(word, n_strands)
    for k in range(1, n_strands + 1):
        if top[k] is None:
            raise ValueError("strand %d meets no crossing; PD codes cannot represent it" % k)
        b.connect(top[k], bottom[k])
    starts = [bottom[k] for k in range(1, n_strands + 1)]
    return b.pd_code(starts=starts)


def plat_closure_pd(word, n_strands):
    """PD code of the plat closure: strands 2k-1, 2k are joined by a cup at
    the bottom and a cap at the top.  n_strands must be even."""
    if n_strands % 2:
        raise ValueError("plat closure needs an even number of strands")
    b, bottom, top = _braid_builder(list(word), n_strands)
    for k in range(1, n_strands + 1, 2):
        if top[k] is None and top[k + 1] is None:
            raise ValueError("strands %d,%d meet no crossing: crossingless component" % (k, k + 1))
        if top[k] is None:            # cup -> strand k -> cap, no crossing on k
            b.connect(bottom[k + 1], top[k + 1])
        elif top[k + 1] is None:
            b.connect(bottom[k], top[k])
        else:
            b.connect(bottom[k], bottom[k + 1])
            b.connect(top[k], top[k + 1])
    return b.pd_code()


def faces_with_edges(pd):
    """List of faces; each face is a list of (edge, from_dart, to_dart) in
    the face-on-the-left walk (see bracket.Diagram.faces)."""
    return Diagram(pd).faces()


def parallel_edge_pairs(pd):
    """All twist sites: (e1, e2, face_index) for distinct edges e1 != e2
    bounding the same face."""
    out = []
    for fi, face in enumerate(faces_with_edges(pd)):
        edges = [e for e, _, _ in face]
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                if edges[i] != edges[j]:
                    out.append((edges[i], edges[j], fi))
    return out


def insert_full_twists(pd, e1, e2, n, face=None):
    """Replace the identity 2-tangle formed by edges e1 and e2 (which must
    bound a common face) by 2n crossings (n full twists; sign of n picks the
    handedness, see module docstring).  Returns a new PD code with labels
    1..2(n_old+2|n|).  If e1, e2 share several faces, `face` (an index into
    faces_with_edges(pd)) selects one; default: the first shared face."""
    pd = [list(x) for x in pd]
    if n == 0:
        return pd
    D = Diagram(pd)
    faces = D.faces()
    chosen = None
    for fi, f in enumerate(faces):
        if face is not None and fi != face:
            continue
        d1 = [(fr, to) for e, fr, to in f if e == e1]
        d2 = [(fr, to) for e, fr, to in f if e == e2]
        if d1 and d2:
            chosen = (d1[0], d2[0])
            break
    if chosen is None:
        raise ValueError("edges %r and %r do not bound a common face" % (e1, e2))
    (P1, Q1), (P2, Q2) = chosen
    # Face on the left of both walks: e1 runs 'up' on the right of the face
    # (P1 bottom, Q1 top), e2 runs 'down' on the left (P2 top, Q2 bottom).
    b = Builder.from_pd(pd)
    b.disconnect(P1)
    b.disconnect(P2)
    slot = _SIGMA if n > 0 else _SIGMA_INV
    k = 2 * abs(n)
    prev_left, prev_right = Q2, P1        # bottom ends of the box
    for _ in range(k):
        c = b.new_crossing()
        b.connect(prev_left, (c, slot["BL"]))
        b.connect(prev_right, (c, slot["BR"]))
        prev_left, prev_right = (c, slot["TL"]), (c, slot["TR"])
    b.connect(prev_left, P2)
    b.connect(prev_right, Q1)
    # keep the orientation of the original components where possible:
    starts = [D.head[e] for comp in D.components for e in comp[:1]]
    return b.pd_code(starts=starts)


def clasp_unknot_pd():
    """The 2-crossing 'clasp' diagram of the unknot: an untwisted band whose
    two folds hook each other.  Edges 2 and 4 are the two parallel band
    strands (they bound a common face); inserting n full twists there with
    insert_full_twists(pd, 2, 4, n) gives twist knots.  Both crossings are
    positive (writhe +2)."""
    return [[1, 3, 2, 2], [3, 1, 4, 4]]


def connected_sum_pd(pd1, pd2):
    """Connected sum: cut edge max-label of pd1 and label 1 of pd2 and splice.
    Only sensible for knots; the result is independent of the choice of
    edges up to isotopy."""
    D1 = Diagram(pd1)
    D2 = Diagram(pd2)
    if D1.num_components() != 1 or D2.num_components() != 1:
        raise ValueError("connected_sum_pd is only implemented for knots")
    n1 = len(pd1)
    # relabel pd2 to avoid collisions
    off = 10 ** 6
    pd2r = [[e + off for e in x] for x in pd2]
    b = Builder()
    b.ncross = n1 + len(pd2)
    for e, (p, q) in D1.occ.items():
        b.connect(p, q)
    for e, (p, q) in D2.occ.items():
        b.connect((p[0] + n1, p[1]), (q[0] + n1, q[1]))
    e1 = D1.components[0][0]
    e2 = D2.components[0][0]
    t1, h1 = D1.tail[e1], D1.head[e1]
    t2, h2 = (D2.tail[e2][0] + n1, D2.tail[e2][1]), (D2.head[e2][0] + n1, D2.head[e2][1])
    b.disconnect(t1)
    b.disconnect(t2)
    b.connect(t1, h2)
    b.connect(t2, h1)
    return b.pd_code(starts=[h1])


if __name__ == "__main__":
    import sys, json
    from bracket import jones_from_pd, jones_str
    if len(sys.argv) >= 3 and sys.argv[1] == "--braid":
        pd = braid_closure_pd(json.loads(sys.argv[2]))
    elif len(sys.argv) >= 4 and sys.argv[1] == "--plat":
        pd = plat_closure_pd(json.loads(sys.argv[2]), int(sys.argv[3]))
    else:
        print("usage: twist.py --braid '[1,1,1]'   |   twist.py --plat '[2,1,1]' 4")
        sys.exit(1)
    print("PD:", pd)
    print("V :", jones_str(jones_from_pd(pd)))
