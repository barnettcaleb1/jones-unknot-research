"""Brute-force generator space E_iota(D) = H(C_iota(D), d_id) of a tangle diagram (F_2).
C_iota(D): states of connectivity iota with +/- labels on closed loops; d_id = the part of the Khovanov/Bar-Natan
edge maps whose algebra coefficient is an idempotent (identity part after delooping).
Gradings: r = number of 1-resolutions, qq = r + sum of loop signs (unnormalised)."""
import itertools, sys, collections
from cube import Diagram, parse, quotient_word, word_str, conn_name
from indcx import rank_f2

def state_full(D, bits):
    parent = [0]
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def new():
        parent.append(len(parent)); return len(parent) - 1
    cur = [new() for _ in range(D.ntop)]
    tops = list(cur); j = 0
    corners = []   # per crossing: 4 node ids (TL, TR, BL, BR)
    freeloops = 0
    for (c, i) in D.slices:
        if c in 'xy':
            b = bits[j]; j += 1
            horizontal = (b == 1) if c == 'y' else (b == 0)
            tl, tr = cur[i], cur[i + 1]
            if horizontal:
                a, bb = find(tl), find(tr)
                if a != bb: parent[a] = bb
                nn = new(); cur[i] = nn; cur[i + 1] = nn
            corners.append((tl, tr, cur[i], cur[i + 1]))
        elif c in 'lr':
            a = new(); cur[i:i] = [a, a]
        else:
            a, bb = find(cur[i]), find(cur[i + 1])
            if a != bb: parent[a] = bb
            del cur[i:i + 2]
    ends = [('T', k, find(t)) for k, t in enumerate(tops)] + [('B', k, find(b)) for k, b in enumerate(cur)]
    strandroots = set(r for (_, _, r) in ends)
    byc = {}
    for (s, k, r) in ends: byc.setdefault(r, []).append((s, k))
    conn = tuple(sorted(tuple(sorted(v)) for v in byc.values()))
    # component key of each corner: min corner id in the component (corner id = 4*j + t)
    comp_corners = collections.defaultdict(list)
    croot = []
    for jx, cs in enumerate(corners):
        rr = tuple(find(x) for x in cs); croot.append(rr)
        for t, r in enumerate(rr): comp_corners[r].append(4 * jx + t)
    key = {r: min(v) for r, v in comp_corners.items()}
    loops = sorted(key[r] for r in comp_corners if r not in strandroots)
    isstrand = {key[r]: (r in strandroots) for r in comp_corners}
    ckeys = [tuple(sorted(set(key[r] for r in rr))) for rr in croot]   # comps through crossing j (keys)
    return conn, loops, isstrand, ckeys

def E_space(D, verbose=False):
    n = D.n
    info = {}
    for bits in itertools.product((0, 1), repeat=n):
        info[bits] = state_full(D, bits)
    # generators
    gens = collections.defaultdict(list)   # (conn, qq, r) -> list of (bits, frozenset of minus-loops)
    for bits, (conn, loops, isstrand, ckeys) in info.items():
        r = sum(bits)
        for signs in itertools.product((1, -1), repeat=len(loops)):
            minus = frozenset(l for l, s in zip(loops, signs) if s < 0)
            gens[(conn, r + sum(signs), r)].append((bits, minus))
    index = {k: {g: i for i, g in enumerate(v)} for k, v in gens.items()}
    ranks = {}
    for (conn, qq, r), glist in gens.items():
        tgt = index.get((conn, qq, r + 1))
        if not tgt: ranks[(conn, qq, r)] = 0; continue
        rows = []
        for (bits, minus) in glist:
            row = 0
            cinfo = info[bits]
            for c in range(n):
                if bits[c]: continue
                b2 = bits[:c] + (1,) + bits[c + 1:]
                c2info = info[b2]
                if c2info[0] != conn: continue
                A = cinfo[3][c]; B = c2info[3][c]
                sA = [cinfo[2][a] for a in A]; sB = [c2info[2][b] for b in B]
                rest = set(minus) - set(A)
                outs = []
                if len(A) == 2 and len(B) == 1:
                    z = B[0]
                    if not sA[0] and not sA[1]:
                        m0 = A[0] in minus; m1 = A[1] in minus
                        if not m0 and not m1: outs.append(rest)
                        elif m0 != m1: outs.append(rest | {z})
                    else:
                        loop = A[0] if not sA[0] else A[1]
                        assert sA[0] != sA[1]
                        if loop not in minus: outs.append(rest)
                elif len(A) == 1 and len(B) == 2:
                    x = A[0]
                    if not sA[0]:
                        if x in minus: outs.append(rest | {B[0], B[1]})
                        else: outs.append(rest | {B[0]}); outs.append(rest | {B[1]})
                    else:
                        loop = B[0] if not sB[0] else B[1]
                        assert sB[0] != sB[1]
                        outs.append(rest | {loop})
                else:
                    raise RuntimeError('unexpected edge type %s %s' % (A, B))
                for o in outs:
                    g2 = (b2, frozenset(o))
                    row ^= 1 << tgt[g2]
            rows.append(row)
        ranks[(conn, qq, r)] = rank_f2(rows)
    E = {}
    for (conn, qq, r), glist in gens.items():
        b = len(glist) - ranks[(conn, qq, r)] - ranks.get((conn, qq, r - 1), 0)
        if b: E[(conn_name(conn), r, qq)] = b
    return E

def show(E):
    out = collections.defaultdict(list)
    for (cn, r, qq), b in sorted(E.items()): out[cn].append((r, qq, b))
    return dict(out)

if __name__ == '__main__':
    for w, ntop in [('l1.y0', 1), ('l1.y0.y0', 1), ('l1.x2.y0.x2.y0.x2.u1', 2)]:
        D = Diagram(parse(w), ntop); print(w, show(E_space(D)))
    q = quotient_word(parse('l1.y0.y0.y1.u2'), True, 0)
    D = Diagram(q, 1); print(word_str(q), show(E_space(D)))
