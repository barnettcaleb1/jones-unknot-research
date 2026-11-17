import sys, re
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/fukaya/scratch')
from khtio import *
from collections import Counter, defaultdict
ROWW = 'b-S>c-D>c-S2>c-D>c-S>b'
ROWR = 'b<S-c<D-c<S2-c<D-c<S-b'

def parse_arc(c):
    """Decompose an arc into pieces. Returns dict: k (tail slope), rows: list of (q,h) of row sources, tail_b: (q,h),
    junction powers, family ('E' tail emits D, 'V' tail receives D, '0' no rows), ends (h of BL-end, h of BR-end)."""
    n = len(c.idem)
    # generators that are b
    bs = [i for i in range(n) if c.idem[i] == 0]
    # D arrows between b's are junctions
    junc = [(x, y, p) for (x, y, kind, p) in c.arrows if kind == 'D' and c.idem[x] == 0]
    # cut the chain at junctions: pieces are maximal runs of consecutive generators without a b-b D arrow between them
    cuts = set()
    for (x, y, p) in junc:
        assert abs(x - y) == 1
        cuts.add(min(x, y))
    pieces = []; start = 0
    for i in range(n):
        if i in cuts or i == n - 1:
            pieces.append((start, i)); start = i + 1
    rows = []; tail = None
    for (s, e) in pieces:
        idems = c.idem[s:e + 1]
        if len(idems) == 6 and idems == [0, 1, 1, 1, 1, 0]:
            # a row: its source is the b with outgoing S
            outS = {x for (x, y, kind, p) in c.arrows if kind == 'S' and s <= x <= e and s <= y <= e}
            src = s if s in outS else e
            snk = e if src == s else s
            rows.append((src, snk))
        else:
            assert tail is None, 'two tails?'
            tail = (s, e)
    if tail is None: return None
    s, e = tail
    tb = s if c.idem[s] == 0 else e
    assert c.idem[tb] == 0 and all(c.idem[i] == 1 for i in range(s, e + 1) if i != tb), 'tail not a(k)'
    ncirc = e - s
    # sign of k: k<0 if b has outgoing S inside tail
    k = 0
    if ncirc:
        outS = any(kind == 'S' and x == tb and s <= y <= e for (x, y, kind, p) in c.arrows)
        k = -ncirc if outS else ncirc
        # check shape
    fam = '0'
    for (x, y, p) in junc:
        if x == tb: fam = 'E'
        if y == tb: fam = 'V'
    far = (e if tb == s else s)   # BR end generator (tail end)
    # BL end: the end of the chain that is not in the tail
    blend = 0 if not (s <= 0 <= e) else n - 1
    if not rows: blend = tb
    return dict(k=k, rows=[(c.q[r], c.h[r]) for r, _ in rows], tail_b=(c.q[tb], c.h[tb]), jpow=sorted(p for _, _, p in junc),
                fam=fam, hBL=c.h[blend], hBR=c.h[far], qBR=c.q[far], w=len(rows))

if __name__ == '__main__':
    stats = Counter(); bad = []
    Atab = defaultdict(set)
    for name, bn, kh in all_tangles():
        arc = [c for c in bn if not c.cyclic][0]
        cps = [c for c in bn if c.cyclic]
        A = parse_arc(arc)
        r = [parse_label(c.label) for c in kh if parse_label(c.label)[0] == 'r'][0]
        k = int(r[2]); qr = r[3]
        j = (qr - Fraction(k * (abs(k) + 2), abs(k) + 1)) / 24
        assert j.denominator == 1, (name, j)
        j = int(j)
        ok_k = (A['k'] == k)
        wsigned = 2 * j + k // 4
        ok_w = (A['w'] == abs(wsigned))
        ok_fam = (A['fam'] == ('0' if wsigned == 0 else ('E' if wsigned > 0 else 'V')))
        ok_h = (A['hBR'] - A['hBL'] == 8 * j)
        # e_0 coefficient exponent: tail b at q_b, k<=0: q_b + 2|k| ; k>0: q_b  -> should equal 24 j
        qb = A['tail_b'][0]
        N = qb + 2 * abs(k) if k <= 0 else qb
        ok_N = (N == 24 * j)
        # arc specials predicted from rows: (c,d) = (q+4, q/2-h)
        pred = sorted((q + 4, Fraction(q, 2) - h) for (q, h) in A['rows'])
        cs = sorted([(c.q[0] + 4, Fraction(c.q[0], 2) - c.h[0]) for c in cps] + [(c.q[0] + 6, Fraction(c.q[0], 2) - c.h[0]) for c in cps] + pred)
        actual = sorted((int(L[3]), L[4]) for L in (parse_label(c.label) for c in kh) if L[0] == 's')
        ok_sp = (cs == actual)
        std = (set(A['jpow']) <= {1})
        stats[(ok_k, ok_w, ok_fam, ok_h, ok_N, ok_sp, std)] += 1
        if not all((ok_k, ok_w, ok_fam, ok_h, ok_N, ok_sp, std)): bad.append((name, k, j, A, ok_k, ok_w, ok_fam, ok_h, ok_N, ok_sp, std))
        # arc polynomial P_arc
        P = Counter()
        for (cc, dd) in pred: P[cc] += (-1) ** int(Fraction(cc, 2) - dd)
        Atab[(k, j)].add(tuple(sorted((c_, v) for c_, v in P.items() if v)))
    print('checks (k matches, w=|2j+k/4|, family by sign, hBR-hBL=8j, e0-exponent=24j, specials = rows + compact pairs, all junctions D^1): counts')
    for kk, v in stats.items(): print('  ', kk, v)
    for b in bad: print('  EXCEPTION', b)
    print('distinct (k,j):', len(Atab), ' with more than one arc polynomial:', [(kj, v) for kj, v in Atab.items() if len(v) > 1])
    import json
    json.dump({f"{k},{j}": sorted(list(v))[0] for (k, j), v in Atab.items()}, open('/Users/calebbarnett/jones-lanes/theory-restart/mech/fukaya/scratch/arc_poly_data.json', 'w'))
