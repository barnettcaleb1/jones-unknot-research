"""translate.py (roundF/u1) -- engineC2 theta-curves (circle model, theta.py event lists) -> kht++ halfwords.

The S2 / E4 theta-curves have rings of k around BOTH axis lines: A_l (position 0) and A_r (the last position).
A halfword (theta.from_halfword) has rings only around A_l = A_in, with A_r = A_out bare and both vertices on A_l.
Two isotopies of Theta (proofs in REPORT.md section 2):
 (V)  bottom vertex: ... cup(1), mergeL(1), cup(0)  ->  ... cup(1), mergeR(0), cup(0)   (planar slide of v_bot along the
      bottom cup of A; below cup(1) only A_l, one k strand, A_r exist).
 (R)  ring transfer (rotation of the lower half-space ball B = {z < z0} about the unknotted arc B n A by 2 pi; collar
      Dehn twist along a latitude separating A_l(z0) from A_r(z0), chosen through infinity between k_{m-1} and k_m):
      a full twist of (k_m, A_r) at a level with k strands k_1..k_m (positions 1..m, A_r at m+1) is replaced by the full
      twist of the same handedness of positions 0..m-1 (A_l, k_1..k_{m-1}):
          Delta^2(0..m-1) = prod_{j=1}^{m-1} s_{j-1}...s_1 s_0^2 s_1...s_{j-1},   s_i = X(i) (or Y(i) for the other sign).
After (V) and (R) the event list is exactly theta.from_halfword(h) of a halfword h, read off by events_to_halfword."""
import sys
for p in ('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2',
          '/Users/calebbarnett/jones-lanes/theory-restart/mont',
          '/Users/calebbarnett/jones-lanes/theory-restart/tools'):
    if p not in sys.path: sys.path.insert(0, p)
import plat2, theta, sym, lp

def full_twist_events(m, typ):
    """Delta^2 on undoubled positions 0..m-1 (m strands), all crossings of type typ ('X' or 'Y')."""
    ev = []
    for j in range(1, m):
        ev += [(typ, i) for i in range(j - 1, 0, -1)] + [(typ, 0), (typ, 0)] + [(typ, i) for i in range(1, j)]
    return ev

def transfer(events):
    """apply (R) to every ring on the last axis strand and (V) to the bottom vertex; returns new event list.
    Asserts the shapes it relies on (rings come as two consecutive equal crossings of the strand next to A_r)."""
    cols = []; out = []; i = 0; nring = 0
    while i < len(events):
        ev = events[i]; typ = ev[0]
        if typ in ('X', 'Y'):
            p = ev[1]
            if p + 1 == len(cols) - 1 and cols[p + 1] == 'a':          # crossing with the last strand = A_r
                assert cols[p] == 'k', ('A_r crossing with non-k strand', ev, cols)
                nxt = events[i + 1]
                assert nxt == ev, ('A_r crossing not part of a ring', ev, nxt)
                m = p                                                   # k strands at positions 1..m
                assert all(c == 'k' for c in cols[1:m + 1]) and cols[0] == 'a'
                out += full_twist_events(m, typ); nring += 1
                i += 2; continue
            cols[p], cols[p + 1] = cols[p + 1], cols[p]
            out.append(ev); i += 1; continue
        if typ == 'mergeL':
            p = ev[1]
            # bottom vertex on A_r: allowed only when the level is [a, k, a] and the axis cup follows
            assert cols == ['a', 'k', 'a'] and p == 1 and events[i + 1:] == [('cup', 0)], ('vertex shape', cols, events[i:])
            out += [('mergeR', 0), ('cup', 0)]
            return out, nring
        # other events: update colours as theta.expand does
        if typ in ('capA', 'capK'):
            p = ev[1]; c = 'a' if typ == 'capA' else 'k'; cols[p:p] = [c, c]
        elif typ == 'cup':
            p = ev[1]; del cols[p:p + 2]
        elif typ == 'splitR':
            cols[ev[1] + 1:ev[1] + 1] = ['k']
        elif typ == 'splitL':
            cols[ev[1]:ev[1]] = ['k']
        elif typ == 'mergeR':
            del cols[ev[1] + 1]
        out.append(ev); i += 1
    raise AssertionError('no bottom vertex mergeL found')

def events_to_halfword(ev):
    """inverse of theta.from_halfword on its image; raises if the list is not of that shape."""
    assert ev[:3] == [('capA', 0), ('splitR', 0), ('proj', 1)], ev[:3]
    assert ev[-2:] == [('mergeR', 0), ('cup', 0)], ev[-2:]
    toks = ['s']; body = ev[3:-2]; i = 0
    while i < len(body):
        typ, p = body[i]
        if typ in ('X', 'Y'):
            if p == 0:
                assert body[i + 1] == (typ, 0), ('lone axis crossing', body[i:i + 2])
                toks.append(typ.lower() + '0'); i += 2; continue
            toks.append(typ.lower() + str(p))
        elif typ == 'capK':
            assert p >= 1; toks.append('l%d' % p)
        elif typ == 'cup':
            assert p >= 1; toks.append('u%d' % p)
        else:
            raise AssertionError(('unexpected event', body[i]))
        i += 1
    h = '.'.join(toks)
    assert theta.from_halfword(h) == ev, 'round trip failed'
    return h

def s2_events(W):
    return sym.symmetric(plat2.top_events(W))

def s2_halfword(W):
    ev, nr = transfer(s2_events(W))
    return events_to_halfword(ev)

# closed form for S2 (equivalent to the event-level translation; asserted equal in validate_s2.py)
T = {'a': 'y1', 'A': 'x1', 'b': 'x2', 'B': 'y2', 'c': 'y0', 'C': 'x0', 'd': 'x0.x1.x0.x1', 'D': 'y0.y1.y0.y1'}
def fword(W): return ''.join(plat2.FL[ch] for ch in reversed(W))
def s2_halfword_closed(W):
    return '.'.join(['s', 'l2'] + [T[ch] for ch in W + fword(W)] + ['u1'])

if __name__ == '__main__':
    for W in sys.argv[1:]:
        h = s2_halfword(W)
        print(W, h, h == s2_halfword_closed(W))
        print('  J plat2 ', plat2.J(W))
        print('  J events', theta.J_events(s2_events(W)))
        print('  J transl', theta.J_events(transfer(s2_events(W))[0]))
        print('  lp.J    ', lp.J(h))
