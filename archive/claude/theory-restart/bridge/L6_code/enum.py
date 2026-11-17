import sys, itertools, numpy as np, time
from scd import interlace, nullity_table, jones_x, parity, show_t

def matchings(m):
    """all perfect matchings of range(m) as list of pairs"""
    if m == 0:
        yield []; return
    pts = list(range(m))
    def rec(rem):
        if not rem:
            yield []; return
        a = rem[0]
        for i in range(1, len(rem)):
            b = rem[i]
            rest = rem[1:i] + rem[i+1:]
            for r in rec(rest):
                yield [(a, b)] + r
    yield from rec(pts)

def word_of(match, m):
    w = [None]*m
    for k, (a, b) in enumerate(match):
        w[a] = k; w[b] = k
    return w

def relabel(w):
    mp = {}; out = []
    for c in w:
        if c not in mp: mp[c] = len(mp)
        out.append(mp[c])
    return tuple(out)

def canon(w):
    m = len(w); best = None
    for s in range(m):
        r = w[s:] + w[:s]
        for v in (r, r[::-1]):
            t = relabel(v)
            if best is None or t < best: best = t
    return best

def even_quick(match, m):
    # degree parity of each chord
    for (a, b) in match:
        deg = 0
        for (c, d) in match:
            if (a < c < b) != (a < d < b): deg += 1
        if deg % 2: return False
    return True

def r1r2_irreducible(w, eps):
    m = len(w); pos = {}
    for i, c in enumerate(w): pos.setdefault(c, []).append(i)
    adj = lambda i, j: (abs(i - j) == 1) or {i, j} == {0, m - 1}
    for c, (p, q) in pos.items():
        if adj(p, q): return False
    labs = list(pos)
    for c, d in itertools.combinations(labs, 2):
        if eps[c] == eps[d]: continue
        (p1, p2), (q1, q2) = pos[c], pos[d]
        if (adj(p1, q1) and adj(p2, q2)) or (adj(p1, q2) and adj(p2, q1)):
            return False
    return True

P1, P2 = 1000003, 998244353 % 1000033
def screen_tables(n, x0, p):
    nb = 1 << n
    pc = np.array([bin(i).count('1') for i in range(nb)])
    inter = np.array([[bin(b & R).count('1') for R in range(nb)] for b in range(nb)])
    E = 2*inter - pc[None, :]           # eps(R) for sign vector b (bit=1 => +1)
    xinv = pow(x0, p - 2, p)
    def powtab(e):
        return np.vectorize(lambda k: pow(x0, int(k), p) if k >= 0 else pow(xinv, int(-k), p))(e)
    PX = powtab(E).astype(np.int64)
    w = 2*pc - n
    T = np.array([((-1)**(int(wi) % 2)) * pow(xinv, int(wi), p) % p if wi >= 0 else ((-1)**(int(-wi) % 2)) * pow(x0, int(-wi), p) % p for wi in w]) % p
    d0 = (-(x0 + xinv)) % p
    return PX, T, d0

def run(n, only_even=False, out=None):
    t0 = time.time(); m = 2*n
    seen = set(); reps = []
    for match in matchings(m):
        if only_even and not even_quick(match, m): continue
        c = canon(word_of(match, m))
        if c not in seen:
            seen.add(c); reps.append(c)
    print(f'n={n} only_even={only_even}: {len(reps)} diagrams up to dihedral symmetry ({time.time()-t0:.1f}s)', flush=True)
    tabs = [screen_tables(n, 7, 1000003), screen_tables(n, 11, 999983)]
    stats = dict(hits=0, irred=0, irred_even=0, irred_odd=0)
    cores = []
    for w in reps:
        labs, rows = interlace(list(w))
        N = nullity_table(rows)
        ok = None
        for (PX, T, d0), p in zip(tabs, (1000003, 999983)):
            C = np.array([pow(int(d0), k, p) for k in N], dtype=np.int64)
            S = (PX % p * 1) @ C % p if False else (PX.dot(C)) % p
            cand = (S % p) == (T % p)
            ok = cand if ok is None else (ok & cand)
        par = parity(rows)
        for b in np.nonzero(ok)[0]:
            eps = [1 if (b >> i) & 1 else -1 for i in range(n)]
            if eps[0] == -1: continue      # mirror symmetry
            V = jones_x(rows, eps, N)
            if V != {0: 1}: continue
            stats['hits'] += 1
            if r1r2_irreducible(list(w), eps):
                stats['irred'] += 1
                ev = not any(par)
                stats['irred_even' if ev else 'irred_odd'] += 1
                oddw = sum(e for e, q in zip(eps, par) if q)
                cores.append((w, tuple(eps), tuple(par), oddw))
    print(f'  V=1 signed diagrams (eps0=+1): {stats}  ({time.time()-t0:.1f}s)', flush=True)
    if out:
        with open(out, 'a') as f:
            for w, eps, par, oddw in cores:
                f.write(f'n={n} word={"".join(map(str,w))} eps={"".join("+" if e>0 else "-" for e in eps)} parity={"".join(map(str,par))} oddwrithe={oddw}\n')
    return cores

if __name__ == '__main__':
    nmax = int(sys.argv[1]); out = sys.argv[2] if len(sys.argv) > 2 else None
    for n in range(1, nmax + 1):
        run(n, out=out)
