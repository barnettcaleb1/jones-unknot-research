import itertools, sys
def faces(word, orient):
    """word: cyclic Gauss word; orient[c] in {+1,-1}: local orientation (does 2nd visit cross 1st from right to left).
    Half-edges: at position i the knot arrives (in_i) and leaves (out_i). Vertex = chord c with visits p<q.
    Cyclic order around vertex (counterclockwise): out_p, out_q or in_q..., realised as: for orient=+1:
      [out_p, out_q, in_p, in_q] -> faces traced by rotation; for -1: [out_p, in_q, in_p, out_q]."""
    m = len(word); pos = {}
    for i, c in enumerate(word): pos.setdefault(c, []).append(i)
    rot = {}  # half-edge -> next half-edge counterclockwise at same vertex
    for c, (p, q) in pos.items():
        cyc = [('o', p), ('o', q), ('i', p), ('i', q)] if orient[c] > 0 else [('o', p), ('i', q), ('i', p), ('o', q)]
        for k in range(4): rot[cyc[k]] = cyc[(k + 1) % 4]
    # edge i: from ('o',i) to ('i',(i+1)%m)
    other = {}
    for i in range(m):
        other[('o', i)] = ('i', (i + 1) % m); other[('i', (i + 1) % m)] = ('o', i)
    seen = set(); F = 0
    for h in rot:
        if h in seen: continue
        F += 1; x = h
        while x not in seen:
            seen.add(x); x = rot[other[x]]
    return F
def min_genus(word):
    labs = sorted(set(word)); n = len(labs); best = None
    for o in itertools.product([1, -1], repeat=n):
        F = faces(word, dict(zip(labs, o)))
        g = (2 - (n - 2*n + F)) // 2
        best = g if best is None else min(best, g)
    return best
if __name__ == '__main__':
    for w in sys.argv[1:]:
        print(w, 'min Carter genus', min_genus([int(ch) for ch in w]))
