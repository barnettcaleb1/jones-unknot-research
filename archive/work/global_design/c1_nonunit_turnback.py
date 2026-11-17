"""REJECTED C1 design with an actual unknot anchor and nonunit EKT turnback.

No Jones, determinant, or parameter search is performed by this module.
Run from any directory; the existing vendored Spherogram is used.
The companion note proves the entire Jones-unit locus is only (0,0), using
turnback torsion divisibility and the one-site skein recurrence.
"""
from pathlib import Path
import sys

WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORK / 'braid_classification' / 'packages'))

from spherogram.links.tangles import (
    IdentityBraid, BraidTangle, IntegerTangle, RationalTangle, ZeroTangle,
)
from spherogram.links.links import Crossing


def braid2_power(k):
    assert isinstance(k, int)
    return BraidTangle([1 if k > 0 else -1] * abs(k), 2)


def omega(T):
    # Literal EKT operation: fraction r -> (3r+8)/(r+3).
    return ((T + IntegerTangle(2)) * IntegerTangle(1)) + IntegerTangle(2)


def seed(n):
    # The ONLY n-box, immediately above the fixed rational tangle.
    # Fraction 25 / (-9 + 50*n); its numerator is the fixed knot J.
    return braid2_power(-2*n) * RationalTangle(25, -9)


def outside(seed_tangle, seam_tangle):
    T = omega(seed_tangle)
    A = IdentityBraid(2) | T.rotate(1)
    B = IntegerTangle(-3).rotate(1) | IdentityBraid(2)
    h = BraidTangle([-2, -3, -1, -2], 4)
    seam = IdentityBraid(1) | seam_tangle | IdentityBraid(1)
    return A * h * seam * h * B


def candidate_tangle(m, n):
    # The m-box is horizontal: rotate the WHOLE two-braid box.
    # At m=0 it is ZeroTangle, the specified seam-band fusion.
    # Do NOT multiply ZeroTangle by a vertical braid: that adds only curls.
    return outside(seed(n), braid2_power(2*m).rotate(1))


def candidate(m, n):
    return candidate_tangle(m, n).braid_closure()


def turnback_link(n):
    # Undo the seam-band fusion. This is the EKT link L_n.
    return outside(seed(n), IdentityBraid(2)).braid_closure()


def corner(epsilon, eta):
    """Actual closures B_epsilon,eta in the LOCAL axes of the two boxes.

    epsilon=0: horizontal through state, i.e. vertical ZeroTangle.
    epsilon=1: horizontal turnback, i.e. vertical IdentityBraid(2).
    eta=0: vertical through state above S0.
    eta=1: vertical turnback above S0.
    """
    assert epsilon in (0, 1) and eta in (0, 1)
    seam = ZeroTangle() if epsilon == 0 else IdentityBraid(2)
    n_state = IdentityBraid(2) if eta == 0 else ZeroTangle()
    S = n_state * RationalTangle(25, -9)
    return outside(S, seam).braid_closure()


def boundary_mates(T):
    """Trace actual strands, including cup/cap connections, not braid guesses."""
    ans = []
    for boundary in range(sum(T.boundary)):
        obj, port = T.adjacent[boundary]
        while obj is not T:
            port = (port + 2) % 4 if isinstance(obj, Crossing) else 1 - port
            obj, port = obj.adjacent[port]
        ans.append(port)
    return ans


def check_anchor_by_isotopy():
    """One fixed diagram only; Spherogram uses Reidemeister/pickup isotopies."""
    K = candidate(0, 0)
    assert len(K.crossings) == 24
    assert len(K.link_components) == 1
    assert K.writhe() == 0
    original_pd = K.PD_code()
    K.simplify('global')
    assert len(K.crossings) == 0
    # The crossed-component list is empty at this point. Do not confuse it
    # with the empty link: the crossing-free component is recorded separately.
    assert K.unlinked_unknot_components == 1
    return original_pd


if __name__ == '__main__':
    print('K(0,0) boundary mates:', boundary_mates(candidate_tangle(0, 0)))
    check_anchor_by_isotopy()
    print('Anchor simplified to exactly one crossing-free unknot.')
    print('No Jones polynomial or nonzero-parameter knot was evaluated.')
