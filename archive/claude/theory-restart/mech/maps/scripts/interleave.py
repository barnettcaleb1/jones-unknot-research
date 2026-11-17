import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from itertools import product

def all_classes(M):
    """all nonzero homology classes of MorSpace M as sets of basis morphisms (representatives)."""
    hb = M.homology_basis()
    out = []
    for bits in range(1, 1 << len(hb)):
        v = 0
        for i, c in enumerate(hb):
            if (bits >> i) & 1: v ^= c
        out.append(M.unvec(v))
    return out

def interleavings(X, Y, degs=((0, 0), (0, -2)), names=('H', 'S2', 'Db', 'Dc')):
    """search for F: X->Y of bidegree d1, G: Y->X of bidegree d2, {d1,d2}=degs in either order,
    with G F ~ c id_X and F G ~ c id_Y. Returns list of (c, deg F, deg G)."""
    res = []
    EX = MorSpace(X, X, 0, -2); EY = MorSpace(Y, Y, 0, -2)
    for (d1, d2) in (degs, degs[::-1]):
        MF = MorSpace(X, Y, *d1); MG = MorSpace(Y, X, *d2)
        cf = all_classes(MF); cg = all_classes(MG)
        for name in names:
            cX = central(X, name); cY = central(Y, name)
            found = False
            for F in cf:
                for G in cg:
                    gf = compose(X, Y, X, G, F); fg = compose(Y, X, Y, F, G)
                    if EX.is_boundary(gf ^ cX) and EY.is_boundary(fg ^ cY):
                        found = True; break
                if found: break
            res.append((name, d1, d2, found, len(cf), len(cg)))
    return res

def report(tag, X, Y):
    print(tag)
    for name in ('H', 'S2', 'Db', 'Dc'):
        print('    %s id null-homotopic on X: %s, on Y: %s' % (name, MorSpace(X, X, 0, -2).is_boundary(central(X, name)), MorSpace(Y, Y, 0, -2).is_boundary(central(Y, name))))
    for r in interleavings(X, Y):
        print('    composite %-3s  deg F=%s deg G=%s : exists=%s   (#classes F %d, G %d)' % r)

if __name__ == '__main__':
    # 4_1-1 quotient: framed (r(0)) versus the same word without the two framing twists y1.y1 (r(2));
    # they differ by changing the last crossing y1 -> x1 (then y1.x1 cancels): a mixed crossing change at the ends BR, TR.
    X = parse_chain(0, 12, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮')
    Y = parse_chain(0, 10, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮<~⬯<—⬯')
    report('4_1-1 quotient, framing 0 (X) vs framing +2 (Y): one mixed crossing change y1->x1 at the right ends', X, Y)
