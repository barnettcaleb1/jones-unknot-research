# Projection averaging: exact endpoints and a concentration lemma

Bounded theory pass, 2026-11-03. No enumeration. The concentration and optimization statements below are elementary deductions; novelty is not claimed. They give a structural test for the proposed integral-geometric route.

## 1. What Jones-flatness actually forces at the potential ends

Use the reduced bracket convention <U> = 1, delta = -A^2-A^{-2}, and

    V_K(t) = (-A)^(-3w(D)) <D>,    t = A^(-4).

For a connected knot diagram D write c=c(D), a=|s_A(D)|, b=|s_B(D)|, and w=w(D). Its bracket state sum is

    <D> = sum_s A^(c-2|s_B|) delta^(|s|-1).

The potential largest and smallest A-degrees are

    M_A = c+2a-2,       m_A = -c-2b+2.

After normalization and changing variables, the potential Jones interval is [ell,h], where

    ell = (3w-c-2a+2)/4,
    h   = (3w+c+2b-2)/4.                                      (1)

All Jones exponents lie in this interval. Its width and midpoint satisfy

    h-ell = (c+a+b-2)/2 = c-g_T(D),
    (h+ell)/2 = (3w+b-a)/4,

using g_T(D)=(2+c-a-b)/2.

Let I_A = sum over independent sets S in the all-A Lando graph of (-1)^|S|, including the empty set; define I_B similarly. Directly collecting the states attaining the potential degrees gives

    alpha(D) := [t^ell]V_K = (-1)^(w+a-1) I_A,
    beta(D)  := [t^h]V_K   = (-1)^(w+b-1) I_B.                 (2)

With the usual reduced Euler convention, I_A=-chi_tilde(Ind(G_A)); the formula also handles the empty graph. This is the state-sum form of the Bae–Morton/Lando correspondence, categorified in [Gonzalez-Meneses–Manchon–Silvero, Sections 3–4 and Theorem 4](https://arxiv.org/pdf/1511.05845).

If V_K=1, the exact consequences are:

- ell <= 0 <= h.
- If ell<0, then alpha=0; if ell=0, then alpha=1.
- If h>0, then beta=0; if h=0, then beta=1.

Thus “both Lando Euler characteristics vanish in every projection” is false without the endpoint qualification. The crossingless unknot already has ell=h=0 and both potential coefficients equal to 1. A nonnegative statistic genuinely forced to vanish by Jones-flatness is

    F_out(D) = 1_(ell<0) |alpha(D)|^2 + 1_(h>0) |beta(D)|^2.  (3)

Squaring removes cancellation between viewing directions. It does not establish that this statistic detects knotting.

## 2. Proposition: flattening concentrates the projection distribution on any diagram

Let F be a real-valued statistic of signed combinatorial knot diagrams, invariant under planar isotopy and viewing the diagram from its opposite side. Assume F is bounded on diagrams with any fixed upper bound on crossing number. Define for a polygonal embedding C

    Average_F(C) = (1/(4 pi)) integral_(v in S^2) F(D_v(C)) dOmega(v),

ignoring the measure-zero exceptional directions.

**Concentration lemma.** Given any regular polygonal diagram D of a knot K, there exist embeddings C_epsilon of K such that

    lim_(epsilon -> 0+) Average_F(C_epsilon) = F(D).          (4)

Proof. Choose a polygonal realization C_1 whose vertical projection is D. Let

    T_epsilon(x,y,z)=(x,y,epsilon z),   C_epsilon=T_epsilon C_1.

All epsilon>0 give ambient-isotopic embeddings. Projecting C_epsilon along v has the same signed diagram type as projecting C_1 along T_epsilon^{-1}v, after the induced invertible linear change of coordinates on the projection plane. For every v with v_z not zero, the latter direction tends to one of the two vertical directions. Since D is regular, its signed diagram type is locally constant there. The two sides give the same value of F. Thus F(D_v(C_epsilon)) tends pointwise almost everywhere to F(D).

The number N of polygon edges is fixed. Every regular projection has at most N(N-3)/2 crossings, so the assumed boundedness supplies a uniform integrable bound. Dominated convergence proves (4).

The lemma applies to c,w,a,b, the potential endpoint coefficients, their squared magnitudes, and bounded combinations or threshold indicators of these data. It also applies to averages against any fixed absolutely continuous probability distribution on directions. It does not apply without further argument to a measure that changes with the embedding or becomes singular under flattening.

## 3. Corollary: optimizing the average adds no new diagram-level information

For each knot type K,

    inf_(polygonal C of type K) Average_F(C)
        = inf_(diagrams D of K) F(D),                         (5)

and likewise for the supremum, interpreted in the extended real numbers.

Proof. Every regular projection of every C is a diagram of K, so every average lies between the diagram infimum and supremum. Flatten each particular D as in (4) to obtain the opposite inequalities.

In particular, if Average_F(C) were invariant under ambient isotopy of C, then F(D) itself would already be invariant under Reidemeister moves. Averaging cannot convert a genuinely presentation-dependent, purely combinatorial diagram statistic into an isotopy invariant.

This is a useful restriction on a proposed mechanism, not a rejection of integral geometry. Milnor averages the number of maxima of a height function; that quantity retains geometric turning information and is not a function of the signed crossing diagram up to planar isotopy. His total-curvature functional is itself geometric, with a topological lower bound. [Milnor, On the Total Curvature of Knots](https://people.reed.edu/~ormsbyk/milnor-total-curvature.pdf). The distinction explains why that argument is not a direct template for averaging Lando data.

## 4. Two curls defeat a uniform extremal-Euler lower bound for every knot

With the conventions of (1), adding a positive Reidemeister-I curl changes

    (c,w,a,b) -> (c+1,w+1,a+1,b),
    (ell,h)   -> (ell,h+1).

It preserves V, so the new potential upper coefficient is zero. A negative curl changes

    (c,w,a,b) -> (c+1,w-1,a,b+1),
    (ell,h)   -> (ell-1,h),

and makes the new potential lower coefficient zero. Adding one curl of each sign to any D therefore yields a diagram D' of the same knot with

    alpha(D')=beta(D')=0.

Apply (5) to F_ends=|alpha|^2+|beta|^2, or to F_out from (3). For EVERY knot type K,

    inf_C Average_(F_ends)(C) = inf_C Average_(F_out)(C) = 0.  (6)

Hence neither unweighted statistic can have a positive, knot-type-dependent lower bound analogous to the curvature gap. This obstruction needs no special nontrivial knot with intrinsically cancelling Khovanov extremes: the two local unknotted perturbations and flattening suffice for every knot type.

Equation (6) does not say that the average is exactly zero for every embedding, nor that zero is attained for each knot. An arbitrarily small positive number and an identically zero function are different claims. If curls are removed by a prescribed reduction before evaluation, the general optimization theorem (5) still applies to that new combinatorial statistic; the particular two-curl argument may then cease to apply.

## 5. A precise remaining opening

An integral-geometric proposal needs information outside this theorem's domain: for example, a controlled geometric density that compensates for flattening, or a curvature/length-constrained class of embeddings with a proved canonical relation to Jones data. The difficulty then becomes proving that V=1 annihilates the weighted quantity while topology forces it positive. No such identity has been supplied here.

The new lemma worth retaining is (4)–(5): unweighted projection averaging, even followed by optimization over embeddings, cannot be stronger than optimizing its underlying diagram statistic. It converts the proposed averaging route into a sharply testable question about which extra geometric data are indispensable.
