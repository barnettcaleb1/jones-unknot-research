# A marked Brunnian band construction and one exact family verdict

2026-11-03. CX-PANTS / CX-BAND3. Geometry and polynomial calculation have
independent internal checks. TRUSTED pending Claude's read; no novelty
claim. The specific family below contains no Jones counterexample.

## The marked surface hypothesis

Let P be an embedded oriented planar surface consisting of a disk and r
bands, with r+1 boundary components. The bands specify a complete cutting
system. For S a subset of the bands let P_S be the disk with just those
bands restored. Assume every proper P_S is ambiently standard, including
its induced framing. This is a condition on the actual surfaces, not on
individual boundary knot types or their polynomials.

Starting with the cut disk boundary, put n_i full twists at the ith cut
box. Call the resulting knot K(n_1,...,n_r). Use V(U)=1, delta=-A^2-A^-2,
t=A^-4, and the handedness with normalized moving eigenvalue A^8.
Let L=boundary(P). Each proper restoration has V=delta^|S|, so the
tensor product of the r local two-state skein identities gives

    V_K - 1 = product_i(1-A^(8n_i)) (V_L/delta^r - 1).       (1)

Indeed all proper sectors agree with the expansion of
product_i(A^(8n_i)+(1-A^(8n_i)))=1; only the full restoration differs.
Thus polynomial cancellation is concentrated in one joint sector, rather
than sought among independently adjustable coefficients.

Let Gamma be the cut unknot and its r specified crossing circles. Deleting
one circle leaves the augmentation of a standard proper surface. Flatten
that surface together with its cut system; its augmentation is an unlink.
The crossing circles without the central knot are also an unlink. Thus
Gamma is a homologically trivial Brunnian link.

The lifted-annuli proof of pants_nontriviality.md works for any r:

    Gamma unlink  =>  Sigma2(L)=#^r(S1 x S2)  =>  L=U_(r+1). (2)

The last implication is the unlink-cover classification, stated in
[Gorchakov Thm2.15](https://arxiv.org/html/2408.12557v1#S2), citing Plotnick.
Consequently any certificate that L is nontrivial certifies Gamma
nontrivial. Mangum--Stanford then shows that K(n) is nontrivial whenever
every n_i is nonzero. If some n_i=0, surgery takes place on a proper unlink
sublink of Gamma, giving an unknot.
[Mangum--Stanford Thm2](https://msp.org/agt/2001/1-1/agt-v1-n1-p07-p.pdf).

If P has zero Seifert form, its rank-r symmetrized Seifert matrix gives
H1(Sigma2(L))=Z^r. The r distance-one smoothing surgeries on the lifted
core link then have zero integral linking matrix, because their cokernel
is Z^r. Full twists give slopes mu+/-2n_i lambda, so numerator-one
surgeries on this algebraically split link yield det K(n)=1. This is the
same argument as the pants case, not an assertion that Delta_K=1.
For nontrivial Gamma, K(1,...,1) has unknotting number exactly one.

For r>=3 the proper-surface hypothesis itself implies zero Seifert form:
each diagonal and off-diagonal entry is visible on a proper one- or
two-band surface. We do not claim that every Brunnian spatial graph
admits this marked surface package.

## One fully specified three-band source

Take three parallel ribbons in a box. Double each strand of the pure
three-braid

    beta = [sigma1^2,sigma2^2]
         = sigma1^2 sigma2^2 sigma1^-2 sigma2^-2

to obtain six boundary strands. A positive sigma_i cables to

    sigma_(2i) sigma_(2i-1) sigma_(2i+1) sigma_(2i),

and a negative generator uses the inverse word. The result has 32 crossings.
Close it by the following exterior arcs (positions are one-based):

    top2--top3, top4--top5,
    bottom2--bottom3, bottom4--bottom5,
    top1--bottom1, top6--bottom6.

This is reduced Markov closure after multiplication by e2 e4 in TL6.
For the surface, join the six ribbon attachment intervals by the exterior
disk on the compactified projection sphere, containing infinity. Its
interior misses the box; choosing the bounded planar disk would be wrong.
The exterior arcs plus attachment intervals form one boundary circle.
Attaching the three identity ribbons gives a standard four-holed sphere.

Deleting any ribbon deletes the corresponding braid strand. Each deletion
of beta is exactly the identity two-strand braid: under deletion, at least
one factor of the displayed commutator disappears. The chosen cabling has
no self-twist on the surviving ribbons. Thus all proper restored surfaces
are standard. At identity the four boundary components traverse strand
sets {1}, {2,3}, {4,5}, {6}. No identification of a boundary sublink with
the ordinary Borromean braid closure is made or needed.

The boundary orientation puts opposite orientations on the two sides of
each ribbon. Each cabled crossing contributes two signs of each kind,
so the diagram has total writhe zero. Its reduced bracket is V_L exactly.
Span would in any event reject a framing-unit ambiguity.

## Exact verdict for every twist triple

The boundary defect is

    V_L-delta^3 = A^-30 (A^4-1)^4 (A^4+1)^3
                 (A^8+A^4+1)(A^8+1)(A^8-A^4+1)^2.          (3)

It is nonzero. The boundary has A-span60; the four-component unlink has
A-span12. Thus L, and by (2) Gamma, are nontrivial.

Substitution in (1), cancelling delta^3=-A^-6(A^4+1)^3, gives the exact
three-parameter formula

    V_K(m,n,p)(t) = 1 - t^-6 (t-1)^4
        (t^2+t+1)(t^2+1)(t^2-t+1)^2
        (1-t^(-2m))(1-t^(-2n))(1-t^(-2p)).                 (4)

Therefore

    V_K(m,n,p)=1  iff  m*n*p=0  iff  K(m,n,p)=U.

This is an all-integer family rejection, not a parameter scan. Every
member with mnp nonzero is a nontrivial determinant-one knot. K111 has
unknotting number one and Jones t-span18.

The first departure from the unknot in the exponential Jones expansion
is especially explicit:

    V_K(m,n,p)(exp(h)) = 1 - 48*m*n*p*h^7 + O(h^8).        (5)

So its Jones-derived finite-type coefficients through degree six vanish.
This statement is about the coefficients of this Jones expansion, not
all finite-type invariants. The exact global factors in (4), rather than
any low-order screen, decide nontriviality of the polynomial.

## Reproducibility and scope

`brunnian_three_band.py/.json` evaluates the one marked closure in the
132-dimensional planar-pairing basis of TL6. Controls: the identity
source gives delta^3, each single cut gives delta^2, and all cuts give1.

`brunnian_three_band_independent.py` uses a distinct 64-dimensional spin
representation and weighted matrix trace, without importing the pairing
tables. It reproduces the full polynomial and the controls, and verifies
(3) by exact integer polynomial multiplication. Geometry has a separate
internal read, including the exterior disk and endpoint matching.

The marked higher-band construction is valid, but its simplest commutator
source fails the required polynomial equality. No other braid, power,
clasper, mutation, or parameter family was searched. A new attempt needs
a specific additional mechanism that kills the joint defect in (1).
