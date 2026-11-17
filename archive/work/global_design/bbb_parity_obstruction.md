# A specialization obstruction to the BBB unequal-count argument

2026-11-03. Independently checked from the coordinated lane's `build-transfer/transfer.md` and `ref-transfer/ref-transfer.md`, and directly against [Bharathram–Birman–Brendle, arXiv:2607.05283v2](https://arxiv.org/html/2607.05283v2). This identifies an incompatible package of proof claims. It does not refute Burau₄ faithfulness.

## The elementary obstruction

For a Moody pairing write its unsimplified polynomial as

    M(t)=Σ_{i=1}^m ε_i t^{k_i},       ε_i∈{−1,1}.

The paper's winding and parity definitions give

    ε_{i+1}/ε_i = (−1)^(k_{i+1}−k_i).

Therefore ε_i(−1)^{k_i} is constant, and

    |M(−1)|=m.

Let X lie in the kernel of the unreduced Burau representation at t=−1. For every Γ the two Moody pairings M_{XΓ} and M_Γ have equal values at −1 up to their lift-normalization signs. This follows from the homological definition; the absolute values agree independently of those choices.

Consequently, whenever both configurations satisfy parity, their intersection counts are equal. This statement holds for every Γ, without assumptions about the geometry of a proposed correcting push.

## A concrete nontrivial Brunnian input

Use the standard pure generators A_{i4}, with [a,b]=aba⁻¹b⁻¹. Set

    T=(σ₁σ₂)⁶,
    Ψ=[[A₁₄,A₂₄],A₃₄],
    Φ=[T,Ψ].

Forgetting any strand kills Ψ, so Ψ is Brunnian; normality gives the same property for Φ.

Take the unreduced Burau block σ_i↦[[1−t,t],[1,0]]. At t=−1 the nontrivial three-dimensional block of σ₁σ₂ is

    C = [[2,−2,1],[1,0,0],[0,1,0]].

Its characteristic polynomial is (x−1)(x²−x+1), a divisor of x⁶−1. Cayley–Hamilton yields C⁶=1, so ρ₄(T)(−1)=1 and ρ₄(Φ)(−1)=1.

Nevertheless Φ is nontrivial. An independent exact evaluation at t=2 over F₅ gives

    ρ₄(Φ) = [[0,3,4,4],
              [4,4,4,4],
              [1,2,3,0],
              [3,1,0,2]],

which is not the identity. The word has 112 letters before free reduction. The generator and inverse matrices, and the adjacent braid relations, were checked in the same calculation. This is a certificate for one specified word, not a search.

Every conjugate of Φ retains membership in the specialized kernel and nontrivial Brunnian subgroup. Standard stabilization retains the specialized identity matrix.

## Consequence for the paper's argument

The paper uses Proposition 6.7 to obtain two parity-satisfying configurations with different intersection counts, after the conjugation/preparation asserted in Theorem 6.9. Applied to the braid above, the combined assertions contradict the elementary obstruction.

At least one part of this package must fail: the claimed preparation of every nontrivial Brunnian braid, the simultaneous parity properties, or the final unequal-count modification. We have not constructed the paper's particular proper-product diagram for Φ, so this is **not** an isolated counterexample to Proposition 6.7's conditional statement. Likewise, it does not refute Corollary 6.8's bare polynomial-inequality conclusion, which could be true by a different argument involving exponents rather than counts.

The precise decision is to stop treating this proof as establishing Burau₄ faithfulness. Any deduction that assumes faithfulness remains explicitly conditional.

## What is not excluded

Parity retains the exponent multiset: M(−t) has contributions of one sign. Equal counts need not mean equal polynomials. A comparison of extreme exponents or higher moments could distinguish braids in the specialized kernel, but no such comparison is established by this count argument. The transfer referee correctly rejects the broader claim that parity itself discards all Torelli information.

No automatic transfer to W(5,1) is justified. Its generic kernel problem remains open in this project.
