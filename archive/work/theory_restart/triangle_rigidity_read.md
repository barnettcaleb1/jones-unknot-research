# Triangle-specialization audit and the corrected finite-index theorem

15 November 2026. Independent read for Codex; no pattern-realization claim. The proposed conclusion with only Gamma is false. The extended conclusion has a proof using algebraic convergence, replacing the unsupported bounded-degree-to-bounded-word step.

## 1. Exact omitted normalizer

Use the notation of pattern_symmetry_dichotomy.md and put

    R = [[delta,1],[-1,-delta]],    d=delta^2-1.

Direct multiplication gives

    R^2=d I,       R* G R=d G,
    R J R^-1=-J,
    R M R^-1=-A^-2 J M^-1 J.

Consequently R normalizes the projective group Gamma. If a=[J] and b=[JM] are its order-two and order-three generators, conjugation by R fixes a and takes b to b^-1. This action is nontrivial on the C3 factor of the abelianization C2 x C3. It is therefore outer, so [R] is not in Gamma.

This is a matrix counterexample to the stated finite-index lemma, with intersection the whole group. It is not an actual planar-pattern counterexample: the corresponding C=GR=d diag(1,-1) has zero off-diagonal entries and has not been realized as a pattern. At the triangle specializations, d<0; R reverses the two components of the complement of the invariant circle. Claude invoked the orientation-preserving commensurator and omitted this coset.

## 2. The primary-source inputs

For odd n>30 choose

    A_n=exp(pi i/4-pi i/(2n));    A_n^-4=-exp(2pi i/n).

The projective rational-tangle representation has image the discrete triangle group Delta(2,3,n), and converges on its two generators to the standard modular representation at A_0=exp(pi i/4). Choosing only odd n avoids distinctions between the pure-braid subgroup and the full image in the even-order cases. See Funar--Kohno, *On Burau's representations at roots of unity*, arXiv:0907.0568, especially Proposition3.5 and Lemma3.4 in the author version:
https://www-fourier.ujf-grenoble.fr/~funar/buraufinal.pdf
https://arxiv.org/abs/0907.0568

For n>30, Delta(2,3,n) is nonarithmetic and maximal among orientation-preserving discrete Fuchsian groups; hence its orientation-preserving commensurator is itself. A direct research-paper statement of the combined result is Girondo--Gonzalez-Diez, *On extremal discs inside compact hyperbolic surfaces*, C. R. Acad. Sci. Paris Ser.I329(1999),57--60, Section2, deriving it from Margulis, Takeuchi and Singerman:
https://doi.org/10.1016/S0764-4442(99)80461-3
https://verso.mat.uam.es/~gabino.gonzalez/comptesrendu.pdf
Singerman--Syddall, *The Riemann Surface of a Uniform Dessin*, Beitr.AlgebraGeom.44(2003),413--430, Section9, also carefully distinguishes Comm from Comm+:
https://eudml.org/serve/124695/accessibleLayeredPdf/0

The missing convergence input is Jorgensen--Klein, *Algebraic convergence of finitely generated Kleinian groups*, Q.J.Math.33(1982),325--332, DOI10.1093/qmath/33.3.325. For convergent r-generator non-elementary discrete groups, the limit is non-elementary and discrete, and eventually the generator correspondence from the limit to each approximant extends to an epimorphism. The exact statement was read as Theorem1 of Inoue, *Remarks on algebraic convergence of discrete Mobius groups*, RIMS Kokyuroku1022(1997),113--116; the original publisher's page gives bibliographic data but not its full text:
https://doi.org/10.1093/qmath/33.3.325
https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1022-15.pdf

The conclusion needed below can alternatively be proved from Jorgensen's inequality and uniform isolation of the identity. No quantitative word-length estimate is required.

## 3. Corrected theorem

Let S in GL2(Q(A)) be a G-similitude. If

    H=Gamma intersect [S] Gamma [S]^-1

has finite index in Gamma, then

    [S] belongs to Gamma^ext = <Gamma,[R]> = Gamma semidirect C2.

In particular S normalizes Gamma, so the intersection is actually Gamma. Requiring positive similitude multiplier on the indefinite arc near A_0 removes the R-coset and recovers the proposed orientation-preserving conclusion.

### Step1: specialization at A_0 is projectively nonsingular

Multiply S by a scalar rational function so its entries are regular at the irreducible divisor A^4+1 and at least one entry is nonzero there. For generators h_i of H choose words k_i in Gamma with

    h_i S = alpha_i S k_i.

All Gamma-word determinants are signed monomials. Taking determinants shows alpha_i^2 is a signed monomial, so the rational function alpha_i has neither zero nor pole at A_0. If S_0 had rank one, its image would be a common invariant line of the specialized H. The specialization Gamma -> Gamma_0 is faithful, so H_0 is a finite-index modular subgroup and has no invariant complex line. Thus S_0 is invertible. Since G_0 is nonsingular, the specialized similitude multiplier is also nonzero.

### Step2: the one-sided finite-index hypothesis suffices after specialization

Outside finitely many exceptional A_n, the identities above specialize. The image H_n has index at most [Gamma:H] in Gamma_n. Its conjugate S_n^-1 H_n S_n lies in Gamma_n and has finite hyperbolic covolume, hence has finite index there as well. The two covolumes agree because a positive or negative similitude induces an isometry of the hyperbolic plane (the latter after exchanging the disk sides). Thus S_n is in the full commensurator of Gamma_n. By the primary result above and the explicit normalizing reflection R_n,

    S_n belongs to Gamma_n^ext=<Gamma_n,R_n>.

### Step3: the algebraic limit is the extended modular group

Take the four marked generators J_n,M_n,R_n,S_n. Their group is Gamma_n^ext, a discrete non-elementary group of complex Mobius transformations. All four generators converge. The Jorgensen--Klein theorem makes the limit

    L=<J_0,M_0,R_0,S_0>

discrete. It contains the extended modular group and preserves its generalized circle, by the nondegenerate specialized similitude identity.

Its orientation-preserving subgroup contains PSL2(Z). A discrete supergroup of this lattice has finite index and finite covolume; it is noncompact because it contains a parabolic. The minimal area of an oriented finite-area noncompact hyperbolic orbifold is pi/3, as follows immediately from the signature formula 2pi(2g-2+s+sum(1-1/m_i)); equality occurs for signature(0;2,3;1 cusp). PSL2(Z) already has this area. Therefore there is no proper discrete orientation-preserving supergroup. Since L already contains R_0, it is exactly the extended modular group.

### Step4: one fixed word, by eventual preservation of relations

Write S_0=w(J_0,M_0) R_0^epsilon, epsilon in{0,1}. Apply the eventual epimorphism in Jorgensen--Klein to the four marked generators. The relation expressing S_0 by this fixed word holds for S_n for all sufficiently large n. Hence

    [S(A_n)]=[w(J(A_n),M(A_n)) R(A_n)^epsilon]

at infinitely many A_n. The relevant rational-function cross-products vanish identically, proving the generic statement.

This repairs, rather than invokes, the original argument's assertion that bounded degree forces the representing word to become constant. The repair requires the nondegenerate limit in Step1; without it, a rational family could escape every compact subset of PGL2(C).

## 4. What is not settled

Nothing here classifies infinite-index intersections, proves that every exceptional similitude tensor is an actual planar pattern, or upgrades an algebraic symmetry to isotopy. The explicit R-coset must be kept in the algebraic classification even if a separate geometric positivity or signed-square theorem later excludes it from the particular actual-pattern class with an unknot seed.

The finite-index theorem uses only finitely generated subgroup identities plus established discrete-group results, not a root-of-unity computation or a scan. Its conclusion is strictly stronger than finite index: in this setting every finite-index intersection is the full group.
