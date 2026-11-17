"""Trace strands of a kht++ Morse word (1-3 tangle: one top end) and classify each crossing as
self-crossing of the special strand (containing the top end), self-crossing of the other strand, or mixed."""
import sys, re
def trace(word):
    letters = word.split('.')
    parent = {}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[a] = b
    cur = [0]; parent[0] = 0; nid = 1
    crossings = []
    for pos, L in enumerate(letters):
        m = re.match(r'([xylru])(\d+)$', L); t, i = m.group(1), int(m.group(2))
        if t in 'lr':
            parent[nid] = nid
            cur[i:i] = [nid, nid]; nid += 1
        elif t == 'u':
            union(cur[i], cur[i + 1]); del cur[i:i + 2]
        else:
            crossings.append((pos, L, cur[i], cur[i + 1]))
            cur[i], cur[i + 1] = cur[i + 1], cur[i]
    special = find(0)
    out = []
    for pos, L, a, b in crossings:
        a, b = find(a), find(b)
        kind = 'mixed' if a != b else ('self-special' if a == special else 'self-other')
        out.append((pos, L, kind))
    return out, [find(x) for x in cur], special
if __name__ == '__main__':
    w = sys.argv[1]
    out, ends, sp = trace(w)
    print('bottom ends strands:', ends, 'special:', sp)
    for o in out: print(o)
