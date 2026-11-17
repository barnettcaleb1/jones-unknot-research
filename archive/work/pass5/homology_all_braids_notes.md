# Independent audit: every four-strand braid retains the Ren core's degree-two channel

## Statement and scope

Let T be the capped six-strand core specified in `tangle_four_strand.json`, before its two outer top crossings are inserted. For **every** braid β in B₄, including arbitrary negative crossings, its annular closure has bracket

    [Tβ] = aβ(A) z² + bβ(A), with aβ(A) ≠ 0.

In fact, after removal of its monomial factor, aβ has order at most one at A⁴ = −1. Thus no arbitrary four-strand top braid can turn this particular core into a degree-zero annular skein. This statement does not classify the resulting knot closures, exclude Jones-one satellites with nontrivial companions, or resolve Jones unknot detection.

## Framing and trace normalization

Use δ = −A²−A⁻² and braid crossings σᵢ = A I + A⁻¹ eᵢ. In the three-dimensional TL₄ module with two through strands, eᵢ has only row i nonzero: its diagonal entry is δ and its adjacent entries are 1. Set

    x = −A⁻⁴, S = diag(1,A²,A⁴),
    Eᵢ = A⁻² S⁻¹ ρ(eᵢ) S,
    M = A⁻² S⁻¹ ρ(T) S.

The nonzero row of Eᵢ has diagonal x−1, predecessor −x, and successor 1. Therefore

    A⁻¹ S⁻¹ ρ(σᵢ) S = I + Eᵢ,
    A S⁻¹ ρ(σᵢ⁻¹) S = I − x⁻¹ Eᵢ = (I+Eᵢ)⁻¹.

All these matrices are over Z[x,x⁻¹]. If e(β) is the exponent sum, define Uβ by

    S⁻¹ ρ(β) S = A^{e(β)} Uβ(x).

The core has zero identity-basis coefficient. This remains true after multiplication by any TL₄ element because projection onto the four-through quotient is an algebra homomorphism. Consequently its annular degree is at most two. The ordinary trace in the two-through module is the coefficient of z² plus three times the coefficient of z⁴; this equality can be verified on all fourteen TL₄ diagrams. The latter coefficient vanishes here. Hence

    aβ(A) = A^{2+e(β)} tr(M(x) Uβ(x)).

There is no unresolved square-root scalar: the monomial A^{2+e(β)} is a unit, and substituting x=−A⁻⁴ injects Z[x,x⁻¹] into Z[A,A⁻¹]. Negative crossings obey the same formula.

## Exact first jets and the integral quotient

Independent gauging of the raw A-variable core matrix gives

    M(1) = [[−15, 0, 15], [−25, 0, 25], [−15, 0, 15]],
    M′(1) = [[−33, 0, 0], [−40, −8, −15], [−15, 0, −18]].

Thus M(1) is zero modulo 5 and M′(1) is 2I modulo 5. Put u=(1,0,1)ᵀ, e₂=(0,1,0)ᵀ, r=(1,0,−1). Then

    M(1) = (−15u−25e₂)r.

Every generator I+Eᵢ has determinant x, and its value at x=1 fixes u. Accordingly U=Uβ(1) lies in SL₃(Z) and fixes u, for every braid word and its inverses. Its quotient on Z³ / Zu is an integral SL₂(Z) matrix: (u,e₁,e₂) is a unimodular basis, with determinant +1. In the quotient basis ([e₁],[e₂]), its upper-right entry is rUe₂.

Suppose f(x)=tr(M(x)Uβ(x)) vanished identically. At x=1, cyclicity of trace and Uu=u give

    0 = tr(M(1)U) = −25 rUe₂.

The quotient matrix is therefore lower triangular. Its integral diagonal entries have product one, so they are either both +1 or both −1. Including the fixed u-direction, tr(U) is consequently 3 or −1.

Differentiating at x=1 then gives

    f′(1) = tr(M′(1)U + M(1)Uβ′(1))
           ≡ 2 tr(U) (mod 5)
           ∈ {1,3} (mod 5),

contradicting f′(1)=0. More strongly, whenever f(1)=0 this calculation shows f′(1)≠0; f can have at most a simple root at x=1. Since δ=A²(x−1), the corresponding annular coefficient cannot have δ² as a factor.

## What was independently checked

`homology_all_braids_audit.py` reads the independently computed raw A-variable matrix from `braid_core_matrix.json`, performs the gauge and variable change from scratch, and recovers both displayed integer matrices. It separately verifies all TL and braid relations, the inverse formula, determinant x, the primitive fixed vector, the unimodular quotient basis, and the three quotient generators. It does not independently reconstruct the capped six-strand input diagram; that finite diagram expansion and all fourteen trace identities are certified by `tangle_all_braids_obstruction.py`. These complementary checks establish the unbounded braid argument, conditional only on the explicitly documented Ren core diagram.
