"""Word-level reduction of halfwords s.l1.l1.W.u2.u2 by valid isotopies (rules.py), with a replayable move log.
Moves:  ('F', i)            free cancellation of W[i], W[i+1]  (R2)
        ('L', i, rule_idx)  length-preserving group rule rules.LP[rule_idx] (lhs -> rhs) applied at position i
        ('Ld', i, rule_idx) the same rule used right-to-left (rhs -> lhs)
        ('T', rule_idx)     delete the prefix rules.TOPPAT[rule_idx][0]
        ('B', rule_idx)     delete the suffix rules.BOTPAT[rule_idx][0]
reduce_word(w, budget) -> (best_word, moves) ; replay(w, moves) re-applies and checks every move."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import rules
from collections import deque
LP = rules.LP
# lookup: tuple -> list of (replacement, move_tag)
LOOK = {}
for k, (nm, l, r) in enumerate(LP):
    LOOK.setdefault(l, []).append((r, ('L', k)))
    LOOK.setdefault(r, []).append((l, ('Ld', k)))
LENS = sorted(set(len(k) for k in LOOK))
TOPS = [(p, k) for k, (p, why) in enumerate(rules.TOPPAT)]
BOTS = [(p, k) for k, (p, why) in enumerate(rules.BOTPAT)]
USE = {'top': True, 'bot': True}
def shorten_once(w):
    """one shortening move (free cancellation, top/bottom absorption) or None"""
    for i in range(len(w) - 1):
        if w[i] == -w[i + 1]: return w[:i] + w[i + 2:], ('F', i)
    if USE['top']:
        for p, k in TOPS:
            if w[:len(p)] == p: return w[len(p):], ('T', k)
    if USE['bot']:
        for p, k in BOTS:
            if len(w) >= len(p) and w[len(w) - len(p):] == p: return w[:len(w) - len(p)], ('B', k)
    return None
def greedy(w, moves):
    while True:
        r = shorten_once(w)
        if r is None: return w
        w, m = r; moves.append(m)
def neighbours(w):
    n = len(w)
    for L in LENS:
        for i in range(n - L + 1):
            seg = w[i:i + L]
            if seg in LOOK:
                for rep, tag in LOOK[seg]:
                    yield w[:i] + rep + w[i + L:], (tag[0], i, tag[1])
def reduce_word(w, budget=3000, target=0):
    """returns (reduced word, list of moves).  BFS over length-preserving rewrites until a shortening move applies."""
    w = tuple(w); moves = []
    w = greedy(w, moves)
    spent = 0
    while w and spent < budget and rules.crossings(w) > target:
        # BFS from w
        parent = {w: None}
        q = deque([w]); found = None
        while q and spent < budget:
            u = q.popleft(); spent += 1
            for v, mv in neighbours(u):
                if v in parent: continue
                parent[v] = (u, mv)
                if shorten_once(v) is not None: found = v; break
                q.append(v)
            if found is not None: break
        if found is None: break
        # reconstruct path
        path = []; x = found
        while parent[x] is not None:
            u, mv = parent[x]; path.append(mv); x = u
        moves.extend(reversed(path))
        w = greedy(found, moves)
    return w, moves
def apply_move(w, mv):
    if mv[0] == 'F':
        i = mv[1]; assert w[i] == -w[i + 1], ('bad F', w, mv); return w[:i] + w[i + 2:]
    if mv[0] in ('L', 'Ld'):
        i, k = mv[1], mv[2]; nm, l, r = LP[k]
        if mv[0] == 'Ld': l, r = r, l
        assert w[i:i + len(l)] == l, ('bad L', w, mv); return w[:i] + r + w[i + len(l):]
    if mv[0] == 'T':
        p = rules.TOPPAT[mv[1]][0]; assert w[:len(p)] == p, ('bad T', w, mv); return w[len(p):]
    if mv[0] == 'B':
        p = rules.BOTPAT[mv[1]][0]; assert w[len(w) - len(p):] == p, ('bad B', w, mv); return w[:len(w) - len(p)]
    raise ValueError(mv)
def replay(w, moves):
    w = tuple(w)
    for mv in moves: w = apply_move(w, mv)
    return w
if __name__ == '__main__':
    import random, time
    for s in ['x2.x1.x3.x2', 'y1.x0.x1.x0.x2', 'x0.x2.y0.y2', 'x2.x0.x1.y2.y0.x3.x2.x2.x3']:
        w = rules.enc(s); r, m = reduce_word(w)
        print(s, '->', rules.dec(r), len(m), replay(w, m) == r)
