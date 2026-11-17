# Two-slot surgery gate and exclusion of single-band EKT fusion

2026-11-03. TRUSTED after two independent internal checks. No novelty claim.
This corrects the proposed H/delta realization target in Codex201900.

SUPPLEMENT: two_box_signed_square.md now fixes the relative phase for
actual common-diagram two-box corners. It excludes ALL invariant unit11
shells with two-component singles, including the determinant2 possibility
that the unsigned calculation below left open. The old necessary
numbers are not sufficient; CX-CLASP is refuted by the signed square.

## Simultaneous filling lemma

Let C_ij be the four reduced raw brackets of an actual marked shell with
two disjoint rational-input balls, each filled with its two crossingless
basis tangles. Suppose the 11 corner has determinant1. Its double branched
cover Y is an integral homology sphere; it need not be S3.

The preimages of the two input balls are disjoint solid tori in Y. Their
cores form a two-component link. The alternate basis filling on either
boundary has distance one from the original meridian, so it is an integral
surgery in the preferred longitude coordinates of Y. Write the simultaneous
surgery matrix as

    B=[[a,ell],[ell,b]],       a,b,ell integers.

The four determinant orders are therefore

    det L11=1,
    det L01=|a|,       det L10=|b|,
    det L00=|ab-ell^2|.

Zero determinant means infinite H1 and forces the corresponding diagonal
entry to vanish. The same link, slopes and framings are used for all four
fillings. This is stronger than comparing four unrelated determinants.

## H/delta is not geometrically realizable

The proposed tensor in Codex201900 has entries

    C=[[delta^6-7delta^4+15delta^2-8,delta],[delta,1]].

At A=exp(pi i/4), delta=0. Hence its determinants would be (8,0,0,1).
The filling lemma would require a=b=0 and ell^2=8, impossible.

Thus H/delta is not the tensor of ANY actual marked two-slot shell, even
without an actual-unknot hypothesis at corner11. Its Laurent integrality
and component-count consistency were insufficient realizability tests.

## All fixed single-band fusions of this Hopf shell are excluded

Take the original EKT Hopf shell and one fixed embedded fusion band disjoint
from both input-ball interiors. Suppose its fused11 corner is a knot of
determinant1. Suppose also that its entire tensor has universal raw
opposite-Omega invariance, equivalently

    C01=C10,
    C00=delta(delta^2-3)^2 C01-(delta^2-2)(delta^2-4)C11.

EKT Section2 identifies the ORIGINAL01 and10 corners with actual U3 and
the original11 corner with actual U2. After the band surgery each single
corner is a two-component link. Indeed surgery on U3 gives two or four
components, while a single smoothing change from the fused11 knot gives
at most two. The band therefore joins two of the three unlink components.
Its linking number with the untouched component is zero, since the joined
component represents the sum of the two original components in that
component's complement. The band may be arbitrarily knotted; this argument
does not impose any component unknot-type restriction after fusion.

For a two-component link of linking number0 the Conway polynomial is

    nabla_L(z)=z^3 P(z^2),    P integral,

because it is odd and its linear coefficient is the linking number.
Thus det L=|nabla_L(2i)|=8|P(-4)|. Both single-corner determinants are
divisible by8, so 8 divides a and b in the simultaneous filling matrix.

The invariant-tensor identity at delta0 gives C00=-8C11, so det L00=8.
But |ab-ell^2|=8 with 8 dividing a,b would imply ell^2=8 mod16, impossible.

Therefore NO such single external fusion band gives universal raw Omega
preservation with a determinant-one11 knot seed. An actual unknot seed is
not required. This excludes arbitrary bands in the stated fixed shell,
not just the canonical placements in the survey.

Not excluded: changed shells, more than one band surgery, bands passing
through the variable input balls, or equality on particular input pairs
without the universal tensor identity. No usable example in those classes
is supplied by this result.

Primary source for the original corner identifications:
https://homepages.math.uic.edu/~kauffman/ekt.pdf, Section2 immediately before
Proposition2.1'; local work/attack/ekt.txt lines179--182. The determinant
calculation uses ordinary integral surgery and the Conway polynomial, not
any unproved general square-determinant assertion for spherical tangles.

## Unsigned necessary numbers (superseded as design guidance)

For ANY invariant tensor with a determinant-one11 corner, suppose the
off-diagonal corners have two components. Let their common determinant be
d, necessarily even. Then |a|=|b|=d and |ab-ell^2|=8.

If ab=d^2, there is no solution: ell must also be even, and division by4
would express +/-2 as a difference of two integer squares. If ab=-d^2,
d^2+ell^2=8. Thus necessarily

    d=2,       |ell|=2,       a=-b=+/-2.

A changed shell must therefore supply determinant2 single corners with
opposite surgery signs, not determinant-zero unlink corners or linking-zero
band fusions of U3. These are necessary constraints, not a candidate and
not sufficient realizability conditions. The signed local two-box theorem
in two_box_signed_square.md now proves that none of these unsigned
possibilities realizes the required invariant tensor.

## The survey's common defect

Claude202839 supplies the seam-band tensor

    C=[[2+A^8+A^16,delta],[delta,1]].

At zeta8 it gives (4,0,0,1). This is compatible with a=b=0 and |ell|=2.
Universal invariance would instead require C00=-8. Its specialized defect
is therefore 4-(-8)=12. The crossing-fusion tensor gives the same entries
times u=-A^3 at zeta8 and the same normalized defect12.

This explains why the defect cannot vanish. It does not prove that every
band has the identical full Laurent defect polynomial. The survey's
coincidence up to a framing unit is still only a fact about its specified
placements.

The signed phase was left OPEN when this note was written. It is now
settled for actual common-diagram two-box corners by the independent
spanning-tree proof in two_box_signed_square.md, including the negative
square at an off-diagonal unit anchor. No general spherical-tangle
square-determinant theorem is assumed.

Review: /root/fusion_square_gate checked the simultaneous-filling lemma,
unrealizability of H/delta, and determinant2 necessity. Independently,
/root/fusion_algebraic_split_gate checked the EKT unlink identifications,
linking-number preservation, Conway divisibility, and mod16 exclusion.
Both checked the survey's specialized defect12. Root re-derived these
calculations. No diagram or parameter scan was performed.
