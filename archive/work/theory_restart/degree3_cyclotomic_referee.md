# Bounded referee: the folded boundary generator and framing

16 November 2026. Follow-up to `degree3_weight_comparison.md`. This checks the folded boundary operator and the framing/projector steps in the proposed cyclotomic proof. It does not supply the annular skein spanning theorem or the original-side generator calculation, which are separate inputs.

## 1. The exact folded operator

Put Q=-t^-1. The ordinary covering-knot Jones variable is t^2=Q^-2, so use the fundamental sl2 braid B at quantum parameter Q. Its eigenvalues are

    Q^(1/2) on the triplet V2,
    -Q^(-3/2) on the singlet V0.

In the bracket pivotal convention let theta_U=-Q^(3/2). The correct folded boundary operator is

    T_fold=theta_U^-1 B=-Q^(-3/2)B.

Its eigenvalues are therefore

    Q^-3 on the singlet,
    -Q^-1 on the triplet.

The quantum trace weights are 1 and [3]_Q=Q²+1+Q^-2. Thus

    L_n^fold=Q^(-3n)+(Q²+1+Q^-2)(-Q^-1)^n.

This is an exact generic fusion calculation, not a root-only spectral fit.

The marked inverse is Y=T^-1. On the original side T acts on the attached i(V1) summand by t^-2 and on the other channel by t; the certificate in `degree3_brauer_mod5.py` checks Ti=t^-2 i. Thus the original point projector is

    P1=(T-t I)/(t^-2-t).

At Q^5=1, t=-Q^-1 gives t^-2=Q²=Q^-3 and t=-Q^-1. Consequently the same polynomial applied to T_fold is exactly the singlet projector P0. Its denominator Q²+Q^-1 is nonzero at a primitive fifth root.

## 2. Why this scalar is a framed pullback correction

It would not be sufficient to choose a Jones-normalized central crossing while leaving every bulk crossing raw. The correction above is instead forced by the pullback framing.

Take the double-cover pullback of framed annular tangles with fixed endpoint framings. The lift respects composition. The local mixed full twist T lifts, as an unframed relative tangle, to one fundamental crossing B: this is exactly the central-crossing rule in the banked symmetric halfword completion. The framed lift must therefore be theta_U^k B for an integer k, since any remaining difference is a relative ribbon twist.

Fix the boundary closure convention by the identity tangle: its lift closes to the two-component zero-framed unlink, so ordinary quantum trace is the compatible closure. The trace closure of T is the annular meridian A1; its lift is the zero-framed unknot. But Tr_q(B)=theta_U dim_q(U). Therefore k=-1. This proves T_fold=theta_U^-1B for an arbitrary outside tangle A by functoriality, not only after evaluating a special closure.

A bulk crossing between two quotient ribbons lifts to the two sheetwise fundamental crossings, with the pulled-back blackboard framings. There is no extra curl there. Thus the raw paired bulk braid and the corrected boundary operator are coherent parts of one framed pullback construction.

An independent check on the standard annular generators is useful. A_n is the closure of the n-strand braid sigma_1...sigma_(n-1), with n-1 crossings. Its lifted diagram has 2(n-1) crossings and is the torus link T(n,2), isotopic to T(2,n). The standard two-strand diagram has n crossings, so the pulled-back ribbon framing differs by n-2. Hence its absolute bracket is

    theta_U^(n-2) Tr_q(B^n)
      =Q^(3(n-1)) Tr_q(T_fold^n).

The equality is literal: the signs (-1)^(n-2) and (-1)^n agree. For n=1 it removes the one kink and gives dim_q(U); for n=2 it gives the raw Hopf-link bracket. This agrees with the annular vector twist r_fold=Q^3.

## 3. Trace comparison and vertices

The original mixed trace, divided by dim_q(V1), has weights 1 and

    [4]_q/[2]_q=t+t^-1=-(Q+Q^-1).

Thus its winding trace is

    L_n^orig=Q^(2n)-(Q+Q^-1)(-Q^-1)^n.

The difference is

    L_n^orig-L_n^fold
      =Q^(-3n)(Q^(5n)-1)
       -Q^-2 Phi_5(Q)(-Q^-1)^n.

It vanishes at primitive fifth roots. The original vector framing is t²=Q^-2, while the folded vector framing is Q³; these agree there as well. Thus the corrected framed values on A_n agree, provided the original annular-generator formula stated by the other lane is used.

Products of annular generators can be placed in balls separated by spheres meeting the branch axis twice. Their double covers are separating spheres, so the lifted links are split. Absolute bracket evaluation is therefore multiplicative. On the original side, each annular pattern acts as a scalar on the simple axis color, and normalized axis trace is likewise multiplicative. This explains why equality on a spanning set of products of the A_n would give equality of the two annular evaluation functionals.

For the original theta, opening the two vertices gives A:V1 tensor V2 -> V1 tensor V2 and

    p A i = Tr_q(A P1)/dim_q(V1).

The corresponding folded projector is P0 at the fifth root. Since P0 is the singlet cup-cap divided by dim_q(U), its folded trace is the reduced bracket of the lifted knot, not an unnormalized extra loop. Thus the projector formula supplies the vertex comparison; the trace weights alone would not have done so.

## 4. Preferred framing can be fixed after a raw Laurent congruence

Suppose the annular argument establishes a raw congruence F(Q)=G(Q) modulo Phi_5(Q), with F,G integral Laurent polynomials and F(1)=G(1)=1. Write F-G=Phi_5 R. Then R(1)=0, and

    F'(1)-G'(1)=5R'(1) in 5Z.

The preferred normalizations are Q^(-F'(1))F and Q^(-G'(1))G, since they remove the linear term while keeping value one. Their correcting exponents differ by a multiple of five, so they remain congruent modulo Phi_5. This avoids comparing separate geometric writhe formulas at every closure.

The integrality hypothesis here is important. A root-field congruence between rational functions whose denominators may vanish at Q=1 does not by itself justify this derivative argument. In the intended application the closed raw scalars are known to be Laurent polynomials up to ribbon monomials, from the generic identification with J and the ordinary knot bracket; that fact must be stated explicitly.

## Scope

The folded generator, its trace weights, the boundary framing correction, the projector match, and the preferred-unit lemma pass this audit. To complete the proposed cyclotomic theorem one still has to state and justify the common annular skein parameters/spanning input and the original-side A_n framing formula. No extrapolation from the root Casimir identity alone proves that global statement.

## 5. Verdict on the completed comparison

The subsequently completed `degree3_cyclotomic_comparison.md`, especially Sections 4–6, supplies these remaining inputs and **passes this bounded audit**. This verdict supersedes the pending status in the preceding paragraph.

The crucial local statement is now explicit: the mixed full twist lifts to one fundamental crossing, with a relative ribbon curl fixed independently of the outside tangle. The identity closure fixes the closure gauge; the meridian closure forces that curl to be negative. Consequently `T_fold=theta_U^-1 B` is the operator used in the arbitrary-outside projector comparison, not just a formula inferred for a family of closed traces. It is coherent with the raw paired-crossing bulk evaluation. The separate `A_n` framing calculation agrees with it, including the negative curl at `n=1` and the raw Hopf case `n=2`.

The completed normalization argument also retains the raw signs. The closed raw evaluations lie in `Q(Q)` and are known ribbon monomials times the integral preferred polynomials, so their monomial exponents are integers and the raw evaluations are integral Laurent polynomials. Gauss's lemma supplies `F-G=Phi_5 R` integrally. Since `F(1)=1` and `G(1)` is initially only `+1` or `-1`, evaluation gives `1-G(1)=5R(1)` and forces `G(1)=1`. Differentiation then makes the framing exponents agree modulo five. No independent sign normalization is made after the raw congruence.

Thus, using the stated integral annular generation theorem and the banked generic theta/cover identifications, the proof establishes the exact preferred cyclotomic congruence `J(t)=V_K(t^2) mod Phi_10(t)`. Its consequence is the full cubic jet and `M_3/36=7v_3(K) mod 5`, including the lower-order residual. The conclusion is stronger than the principal-symbol theorem in `degree3_weight_comparison.md`; it does not identify the integer invariant `iota` geometrically or prove nonvanishing of `J`. This audit does not constitute an independent literature priority check or a rederivation of every previously banked quantum-group tensor.
