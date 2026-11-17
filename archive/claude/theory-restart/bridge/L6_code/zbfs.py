"""BFS over signed chord diagrams (virtual knots mod Z-move) with Reidemeister moves R1-, R2+-, R3.
R3 rule (arrows free): three chords a,b,c whose endpoints sit in three cyclically-adjacent pairs, each chord using
both its endpoints; strands = the three adjacent pairs.  Let a=P12 (strands 1,2), b=P13, c=P23, s1=+1 iff a before b
on strand 1, s2=+1 iff a before c on strand 2, s3=+1 iff b before c on strand 3; o_a=s1s2, o_b=s1s3, o_c=s2s3.
Move is valid unless eps_a*o_a == eps_c*o_c == -eps_b*o_b (cyclic heights).  Move = swap within each pair."""
import sys, itertools
from collections import deque

def canon(word, sg):
    m = len(word); best = None
    if m == 0: return ((), ())
    for s in range(m):
        r = word[s:] + word[:s]
        for v in (r, r[::-1]):
            mp = {}; out = []
            for c in v:
                if c not in mp: mp[c] = len(mp)
                out.append(mp[c])
            sig = [0]*len(mp)
            for c, k in mp.items(): sig[k] = sg[c]
            key = (tuple(out), tuple(sig))
            if best is None or key < best: best = key
    return best

def positions(word):
    pos = {}
    for i, c in enumerate(word): pos.setdefault(c, []).append(i)
    return pos

def neighbors(word, sg, maxn):
    m = len(word); n = m // 2; pos = positions(word)
    res = []
    adj = lambda i, j: (j - i) % m == 1
    # R1-
    for c, (p, q) in pos.items():
        if adj(p, q) or adj(q, p):
            w2 = [x for x in word if x != c]; res.append((w2, sg))
    # R2-
    for c, d in itertools.combinations(pos, 2):
        if sg[c] == sg[d]: continue
        P = pos[c] + pos[d]
        (p1, p2), (q1, q2) = pos[c], pos[d]
        ok = False
        for (x1, y1, x2, y2) in ((p1, q1, p2, q2), (p1, q2, p2, q1)):
            if (adj(x1, y1) or adj(y1, x1)) and (adj(x2, y2) or adj(y2, x2)): ok = True
        if ok:
            w2 = [x for x in word if x not in (c, d)]; res.append((w2, sg))
    # R3
    pairs = [(i, (i + 1) % m) for i in range(m) if word[i] != word[(i + 1) % m]]
    for (i1, j1), (i2, j2), (i3, j3) in itertools.combinations(pairs, 3):
        used = {i1, j1, i2, j2, i3, j3}
        if len(used) != 6: continue
        segs = [(i1, j1), (i2, j2), (i3, j3)]
        labs = [frozenset((word[i], word[j])) for i, j in segs]
        chords = set().union(*labs)
        if len(chords) != 3 or len(set(labs)) != 3: continue
        # strand k = seg k ; chord shared by seg k and seg l is P_kl
        def shared(k, l): return next(iter(labs[k] & labs[l]))
        a, b, c = shared(0, 1), shared(0, 2), shared(1, 2)
        def before(seg, x, y):
            i, j = seg
            return 1 if word[i] == x else -1
        s1 = before(segs[0], a, b); s2 = before(segs[1], a, c); s3 = before(segs[2], b, c)
        oa, ob, oc = s1*s2, s1*s3, s2*s3
        if sg[a]*oa == sg[c]*oc == -sg[b]*ob: continue
        w2 = list(word)
        for i, j in segs: w2[i], w2[j] = w2[j], w2[i]
        res.append((w2, sg))
    # R2+ (only if room)
    if n + 2 <= maxn:
        new1, new2 = max(pos, default=-1) + 1, max(pos, default=-1) + 2
        for g1 in range(m + 1):
            for g2 in range(g1, m + 1):
                for order in (0, 1):
                    for s in (1, -1):
                        w2 = list(word)
                        ins2 = [new1, new2] if order == 0 else [new2, new1]
                        w2 = w2[:g2] + ins2 + w2[g2:]
                        w2 = w2[:g1] + [new1, new2] + w2[g1:]
                        sg2 = dict(sg); sg2[new1] = s; sg2[new2] = -s
                        res.append((w2, sg2))
    return res

def bfs(word, sg, maxn, limit=2000000):
    start = canon(word, sg)
    seen = {start: None}; dq = deque([start])
    while dq:
        cur = dq.popleft()
        w, s = cur
        if len(w) == 0: 
            path = []; x = cur
            while x is not None: path.append(x); x = seen[x]
            return path[::-1], len(seen)
        sgd = {i: s[i] for i in range(len(s))}
        for w2, sg2 in neighbors(list(w), sgd, maxn):
            k = canon(w2, sg2)
            if k not in seen:
                seen[k] = cur; dq.append(k)
                if len(seen) > limit: return None, len(seen)
    return None, len(seen)

if __name__ == '__main__':
    word = [int(ch) for ch in sys.argv[1]]; eps = sys.argv[2]; maxn = int(sys.argv[3])
    sg = {i: (1 if ch == '+' else -1) for i, ch in enumerate(eps)}
    path, nseen = bfs(word, sg, maxn, limit=int(sys.argv[4]) if len(sys.argv) > 4 else 300000)
    print('explored', nseen, 'states;', 'TRIVIAL path length %d' % (len(path)-1) if path else 'no path found')
    if path:
        for st in path: print('  ', ''.join(map(str, st[0])), ''.join('+' if x > 0 else '-' for x in st[1]))
