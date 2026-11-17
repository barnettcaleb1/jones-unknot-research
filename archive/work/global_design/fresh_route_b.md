# Fresh route B: sutured cutting and local-to-global reconstruction

Theory pass, 2026-11-03. Verdict: no qualified new detection mechanism emerged. The useful output is a precise first-lemma requirement and an actual tangle family showing why a single closure cannot supply it. This is a design stop, not a claimed new partial result on the Jones conjecture.

## 1. The candidate and its genuine attraction

One might cut a knot complement along a taut sutured hierarchy, retaining stated skein data on every new boundary, and hope to reconstruct the knot from local pieces. This has a legitimate categorical model: surface stated-skein algebras admit triangular decompositions, and their gluings retain boundary states rather than immediately taking scalar traces. See [Lê, Triangular decomposition of skein algebras](https://arxiv.org/abs/1609.04987) and [Costantino–Lê, Stated skein algebras of surfaces](https://arxiv.org/abs/1907.11400).

But a theorem about decomposing a *known state* is not a theorem about recovering that state from one closed evaluation. In addition, the injectivity statements for surface splitting must not be silently promoted to arbitrary taut surface cuts in three-manifolds. The distinction is substantive in [Lê's stated SL(n) construction](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/topo.12350): it constructs disk-splitting maps for marked three-manifolds, while the stated injectivity theorem in the abstract is for surfaces with boundary.

The original Jones polynomial provides the fully contracted scalar. Cutting exposes boundary coordinates that this scalar has already forgotten.

## 2. The exact finite-dimensional reconstruction lemma

Let H be a finite-dimensional relative skein space over Q(A), and let B:H x H' -> Q(A) be a nondegenerate gluing pairing. If y_1,...,y_d give a basis of H*, via x -> B(x,y_i), then the d closure values B(x,y_i) determine x uniquely. If the closure values of x and a reference x_0 agree on that basis, then x=x_0.

This elementary statement is the actual local-to-global mechanism available from nondegeneracy. The missing input is a *spanning family of measurements*, not further formal properties of the pairing. A single equality B(x,y)=B(x_0,y) places x-x_0 in one hyperplane whenever dim H>1.

The required new geometric lemma would therefore have to produce independent exterior probes whose values are forced by V_K=1, or prove that the realizable boundary state lies in a set separated by the one available probe. Tautness supplies a geometric restriction, but no argument was found that makes either conclusion follow from it.

## 3. Actual unknot closures already show the missing coordinates

The issue is visible with genuine classical tangles, without a formal unrealizable countermodel.

Use TL_2 with basis id,e, relation e^2=delta e, and delta=-A^2-A^{-2}. A braid crossing acts as

    sigma = A id + A^{-1} e.

Close its two top endpoints together and its two bottom endpoints together. The resulting 2-plat of sigma^n is an unknot for every integer n. Its reduced bracket closure functional is

    ell(a id+b e)=a+delta b,

and ell(sigma^n)=(-A^{-3})^n. Remove that framing scalar and put

    x_n = (-A^{-3})^{-n} sigma^n
        = q^n id + (1-q^n)/delta · e,     q=-A^4.             (1)

The quotient in (1) is a Laurent polynomial: 1-q is divisible by delta, and the same holds for 1-q^n. These are normalized states of actual rational tangles. They satisfy

    ell(x_n)=1                                              (2)

for every n, yet are pairwise distinct, even projectively. Indeed their id coefficients q^n differ, and (2) fixes the projective scalar.

The other elementary closure is

    ell'(a id+b e)=delta a+b,

so

    ell'(x_n) = delta q^n + (1-q^n)/delta,

which varies with n. The two closure functionals have matrix

    [[1, delta], [delta, 1]],

whose determinant 1-delta^2 is nonzero. Thus two measurements recover the relative state; the actual unknotted first closure does not supply the second.

These rational pieces do not refute a theorem restricted to essential cuts of prime knot exteriors. They establish the narrower point that geometric realizability, actual unknot closure, and an exact skein gluing law do not by themselves constitute the desired reconstruction principle.

## 4. Why this is not yet a new route

A proposed hierarchy argument needs both of the following bridges:

1. A geometry-dependent source of independent closure constraints, or an equally concrete restriction on allowable relative states.
2. A topological rigidity theorem turning the recovered local skein state into the relevant product or disk certificate.

The first is not supplied by ordinary Jones equality; the second resembles the rational-tangle detection problems already on the board. Declaring either bridge to be a general “local-to-global principle” would conceal the old difficulty rather than create a mechanism.

I do not recommend a scan, a hierarchy implementation, or a new scaffold node from this pass. A future proposal should first name one essential cut and derive one additional independent closure identity from the original Jones equality. That would be a concrete advance worth developing. No such identity was found here.
