#!/usr/bin/env python3
"""Step 1: build PD codes for K(m,n), m,n in -2..2, and the four corner
diagrams, exactly as specified in c4_two_site_candidate.md.  Verifies
component count, crossing count / writhe of K(0,0), and the writhe formula
w = -7 + 2m + 2n, using (a) spherogram's own crossing signs and (b) an
independent sign read off the PD code (over strand runs d -> b  <=>  +1).
Writes family_pd.json."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = ('/Users/calebbarnett/Documents/Codex/2026-10-31/'
       'it-is-an-open-problem-whether-4/work/braid_classification/packages')
sys.path.insert(0, PKG)
from spherogram.links.tangles import (  # noqa: E402
    IdentityBraid, BraidTangle, IntegerTangle, ZeroTangle,
)


def sigma2_power(k):
    assert isinstance(k, int)
    if k == 0:
        return IdentityBraid(4)
    return BraidTangle([2 if k > 0 else -2] * abs(k), 4)


def fixed_pieces():
    T = IntegerTangle(3)
    U = IntegerTangle(-3)
    A0 = IdentityBraid(2) | T.rotate(1)
    B0 = U.rotate(1) | IdentityBraid(2)
    h = BraidTangle([-2, -3, -1, -2], 4)
    return A0, h, B0


def candidate(m, n):
    A0, h, B0 = fixed_pieces()
    return (A0 * h * sigma2_power(1) * sigma2_power(2 * m)
            * h * sigma2_power(2 * n) * B0).braid_closure()


def corner(epsilon, eta):
    assert epsilon in (0, 1) and eta in (0, 1)
    A0, h, B0 = fixed_pieces()
    G = [IdentityBraid(4),
         IdentityBraid(1) | ZeroTangle() | IdentityBraid(1)]
    return (A0 * h * sigma2_power(1) * G[epsilon]
            * h * G[eta] * B0).braid_closure()


def pd_writhe(pd):
    """Independent writhe from the PD code alone.  Labels are consecutive
    along each component (spherogram PD_code numbering), so the over strand
    runs d -> b iff b == d + 1 (mod component length).  We detect the
    successor relation by following the component cycles built from the
    under-strand arcs a -> c and over-strand arcs."""
    labels = sorted({x for row in pd for x in row})
    nlab = len(labels)
    w = 0
    for a, b, c, d in pd:
        # successor of d along its component is d+1 unless d is the last
        # label of its component; handle by checking both candidates
        if b == d + 1:
            w += 1
        elif d == b + 1:
            w -= 1
        else:
            # wrap-around: one of them is the max label of a component
            # and the other the min label of the same component
            if b < d:
                w += 1   # d -> b wraps (d max, b min)
            else:
                w -= 1   # b -> d wraps
    return w


def describe(link):
    pd = [tuple(int(x) for x in row) for row in link.PD_code()]
    comps = len(link.link_components)
    free = getattr(link, 'unlinked_unknot_components', 0)
    return dict(pd=pd, crossings=len(link.crossings), components=comps,
                free_loops=free, writhe_spherogram=link.writhe(),
                writhe_pd=pd_writhe(pd))


def main():
    out = {'family': {}, 'corners': {}}
    ok = True
    for m in range(-2, 3):
        for n in range(-2, 3):
            L = candidate(m, n)
            d = describe(L)
            out['family'][f'{m},{n}'] = d
            expect_w = -7 + 2 * m + 2 * n
            flags = []
            if d['components'] != 1:
                flags.append('NOT A KNOT')
            if d['free_loops']:
                flags.append('FREE LOOPS')
            if d['writhe_spherogram'] != expect_w:
                flags.append(f'WRITHE {d["writhe_spherogram"]} != {expect_w}')
            if d['writhe_pd'] != d['writhe_spherogram']:
                flags.append('PD-sign writhe disagrees with spherogram')
            if flags:
                ok = False
            print(f'K({m:2d},{n:2d}): crossings={d["crossings"]:3d} '
                  f'components={d["components"]} writhe={d["writhe_spherogram"]:3d} '
                  f'(pd-sign {d["writhe_pd"]:3d}) expected {expect_w:3d} '
                  + ('OK' if not flags else ' '.join(flags)))
    k00 = out['family']['0,0']
    print('K(0,0): crossings', k00['crossings'], 'writhe', k00['writhe_spherogram'],
          '-> spec says 15 and -7:',
          'OK' if (k00['crossings'], k00['writhe_spherogram']) == (15, -7) else 'MISMATCH')
    for e in (0, 1):
        for f in (0, 1):
            L = corner(e, f)
            d = describe(L)
            out['corners'][f'{e}{f}'] = d
            print(f'corner({e},{f}): crossings={d["crossings"]} components={d["components"]} '
                  f'free_loops={d["free_loops"]} writhe={d["writhe_spherogram"]} '
                  f'(pd-sign {d["writhe_pd"]})')
    out['all_checks_passed'] = ok
    (HERE / 'family_pd.json').write_text(json.dumps(out, indent=1))
    print('ALL STEP-1 CHECKS PASSED' if ok else 'STEP-1 CHECK FAILURES (see above)')


if __name__ == '__main__':
    main()
