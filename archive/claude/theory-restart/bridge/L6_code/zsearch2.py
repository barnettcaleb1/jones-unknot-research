"""Iterative deepening on # of increasing (R2+) moves; between them, closure under R1-, R2-, R3."""
import sys
from zbfs import canon, neighbors
def closure(states, maxn):
    seen = set(states); stack = list(states)
    while stack:
        w, s = stack.pop()
        sg = {i: s[i] for i in range(len(s))}
        for w2, sg2 in neighbors(list(w), sg, 0):   # maxn=0 disables R2+
            k = canon(w2, sg2)
            if len(k[0]) <= len(w) and k not in seen:
                seen.add(k); stack.append(k)
    return seen
def search(word, sg, maxinc, maxn):
    level = closure({canon(word, sg)}, maxn)
    for inc in range(maxinc + 1):
        if ((), ()) in level: return inc, len(level)
        if inc == maxinc: break
        nxt = set()
        for w, s in level:
            if len(w)//2 + 2 > maxn: continue
            sgd = {i: s[i] for i in range(len(s))}
            for w2, sg2 in neighbors(list(w), sgd, len(w)//2 + 2):
                if len(w2) > len(w): nxt.add(canon(w2, sg2))
        level = closure(nxt | level, maxn)
    return None, len(level)
if __name__ == '__main__':
    for line in open(sys.argv[1]):
        f = dict(kv.split('=') for kv in line.split())
        n = int(f['n']); w = [int(ch) for ch in f['word']]
        sg = {i: (1 if s == '+' else -1) for i, s in enumerate(f['eps'])}
        r, sz = search(w, sg, int(sys.argv[2]), n + 2)
        print(f"n={n} word={f['word']} eps={f['eps']} parity={f['parity']} {'TRIVIAL with %d R2+ moves' % r if r is not None else 'NOT-FOUND'} (states {sz})", flush=True)
