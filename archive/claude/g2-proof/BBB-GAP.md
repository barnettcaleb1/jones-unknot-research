# A gap in the n = 4 Burau faithfulness proof

Bharathram, Birman, Brendle, "The Burau representation of the braid group is faithful for n = 4", arXiv:2607.05283v2. Checked against the PDF text on 3 November 2026. Notation follows the paper:
- ρ_n is the unreduced Burau representation;
- f : B_4 → B_5 is the stabilization;
- K_n = π_1(D_{n-1}, p_n) is the point-pushing subgroup;
- M_Φ is the Moody polynomial of (β*_3)Φ against α, defined up to a unit ±t^k.

**Claim.** The argument of Section 6 can only certify braids whose stabilization is nontrivial under ρ_5 at t = -1. Every element of ker ρ_4 is trivial there. An explicit nontrivial Brunnian 4-braid that is trivial at t = -1 meets every hypothesis of Prop. 6.7 and Cor. 6.8, so the argument fails on it. This does not show that ρ_4 is unfaithful. It shows that the question is open again.

**Status.** Three independent hostile referees, one each for §1, §2 and §§4-5, found no refutation. Their corrections are folded in. Details are at the end.

## 1. Parity forces a single sign at t = -1

**Lemma 1.** Let φ satisfy the parity condition. Write M_φ = Σ ε_i t^{k_i} over the intersection points q_1, ..., q_m of α with a transverse representative of β = (β*_3)φ, in order along β. Then ε_i (-1)^{k_i} does not depend on i. Hence |M_φ(-1)| = m = Σ|coefficients|, and m = ι(α, β).

*Proof.* Section 3 defines W_i = ±k, where Δ_i is the k-punctured disk bounded by α_i and β_i. So |W_i| = |P(Δ_i)|, and Lemma 3.1 gives W_i = k_{i+1} - k_i (eq. (1)). Under parity, ε_{i+1} = -ε_i exactly when |P(Δ_i)| is odd, that is, exactly when (-1)^{W_i} = -1. So ε_{i+1}(-1)^{k_{i+1}} = ε_i(-1)^{k_i}.

For the last claim: |M_φ(-1)| does not depend on the representative, and a minimal representative has ι points. So m = |M_φ(-1)| ≤ ι ≤ m. ∎

So a parity representative is automatically in minimal position. "No cancellation" (Lemma 4.2) is the special case that equal exponents carry equal signs.

The paper's Section 7 data agree. The two parity polynomials there have M(-1) = 8 and M(-1) = -20, which are plus or minus their numbers of terms. The non-parity polynomial has M(-1) = 2 with 8 terms.

## 2. The value at t = -1 sees only ρ at t = -1

**Lemma 2.** If ρ_n(Y) = I at t = -1, then M_{YX}(-1) = ±M_X(-1) for every X ∈ B_n.

*Proof.* By the proof of Thm. 2.3, M_X is determined by a class in H_1(D̃_n, {p̃*}), the free Z[t^{±1}]-module on which ρ_n acts. The class enters through the equivariant intersection pairing with the lift of α, which is Z[t^{±1}]-sesquilinear and has no denominators.

The paper takes the class of the boundary loop of a neighbourhood of the arc. Its pairing is (1 - t^{±1}) times the arc polynomial, and that factor equals 2 at t = -1.

If ρ_n(Y) = I at t = -1, then ρ_n(Y) - I maps the module into (t + 1) times itself, and ρ_n(X) preserves that submodule. So the classes for YX and X differ by an element of (t + 1)H, whose pairing with α vanishes at t = -1.

This holds in either composition convention, because the hypothesis is invariant under transpose, inverse and t ↦ 1/t. The ± comes from normalising M only up to ±t^k. ∎

## 3. What Cor. 6.8 actually proves

Let Γ be as in Prop. 6.7 for Φ. The proof of Cor. 6.8 deduces M_{f(Φ)Γ} ≠ M_Γ from the inequality of the coefficient sums alone: "By Proposition 6.7 we can assume that ι ≠ ι. The result follows." By Lemma 1 those sums are |M_{f(Φ)Γ}(-1)| and |M_Γ(-1)|. So Prop. 6.7 yields M_{f(Φ)Γ}(-1) ≠ ±M_Γ(-1), and Lemma 2 then gives ρ_5(f(Φ)) ≠ I at t = -1.

If Φ ∈ ker ρ_4, then f(Φ) ∈ ker ρ_5 by Obs. 2.1, so f(Φ) is trivial at t = -1. The chain Prop. 6.7 → Cor. 6.8 → Thm. 2.3 therefore never reaches a kernel element. Any braid that meets its hypotheses and is trivial at t = -1 is a counterexample to it.

## 4. An explicit braid on which the chain fails

Let A_{14}, A_{24}, A_{34} be the standard pure braid generators, write [x, y] = x y x^{-1} y^{-1}, and set

  Φ0 = [(σ1σ2)^6, [[A_{14}, A_{24}], A_{34}]].

- **Pure and Brunnian.** (σ1σ2)^6 = Δ_3^4 and the A_{ij} are pure, so Φ0 is pure, and strand deletion acts on it as a homomorphism. Deleting strand 4 kills every A_{i4}. Deleting strand i ≤ 3 kills A_{i4}, and with it the inner commutator.
- **Nontrivial, and trivial at t = -1.** ρ_4(Φ0) = I and ρ_5(f(Φ0)) = I at t = -1, while ρ_4(Φ0) ≠ I at t = 2 and at t = 3. This is exact rational arithmetic in bbb-gap/phi0_check.py, with output in bbb-gap/phi0_check.out.
  - Why it holds: (σ1σ2)^6 is the square of the twist about a curve around three punctures. By the 2-chain relation it lifts to a Dehn twist about a separating curve in the double branched cover. So it lies in the braid Torelli group, and so does any commutator with it.
- **In [K_4, K_4].** Δ_4² is central, so conjugation by Δ_3² acts on K_4 as conjugation by δ^{-1}, where δ = Δ_3^{-2}Δ_4² ∈ K_4. So Φ0 = [δ^{-2}, b] with b = [[A_{14}, A_{24}], A_{34}].

Let y1, y2, y3 be the free basis of K_4 in Fig. 6.13. The proof of Thm. 6.9 notes that Γ_1, as a reduced word, begins with y2^{-1}. Take m larger than the length of the reduced word of Φ0, and set

  Φ′ = Γ_1^{-1} y1^m Φ0 y1^{-m},  Φ = Φ′ · Γ_1 = g Φ0 g^{-1} with g = Γ_1^{-1} y1^m.

**Free reduction.**
- Φ0 is nontrivial with exponent sum zero, so it is not a power of y1. Hence the reduced form of y1^m Φ0 y1^{-m} begins with y1 and ends with y1^{-1}.
- Γ_1^{-1} ends with y2, so Φ′ is freely reduced.
- Φ′ ends with y1^{-1} and Γ_1 begins with y2^{-1}, so the juxtaposition Φ′·Γ_1 is freely reduced too.

**Proper product.** The paper's definition (Section 5) is geometric. Condition 1 forbids bigon-forming polygons among α, β and Γ. Condition 2 concerns how Γ_I and Γ_F meet β′.

The proof of Thm. 6.9 asserts a shortcut for Γ_1, without proof:
- Condition 1 always holds. Only trigons and rectangles could occur, trigons are removed by isotopy, and rectangles are excluded by the alternation of signs along α.
- A freely reduced juxtaposition gives Condition 2.

By that criterion Φ = Φ′·Γ_1 is a proper product. We could not check Conditions 1 and 2 directly, because the figures are not in our text.

**Conclusion.** Φ is a conjugate of Φ0. So it is a nontrivial Brunnian braid in K_4, hence pseudo-Anosov with ι(α, (β*_3)Φ) > 0, and ρ_5(f(Φ)) = I at t = -1. It therefore meets every hypothesis of Lemma 6.3, Prop. 6.7 and Cor. 6.8, and by §3 no Γ can have all the properties Prop. 6.7 asserts for it.

## 5. Where the failure can be

At least one of the following is false:
- the shortcut criterion for Γ_1 in the proof of Thm. 6.9 (if it fails, Φ′·Γ_1 need not be a proper product);
- Prop. 6.7, through its parity claims (Lemmas 6.2 to 6.6) or through its "Furthermore" inequality.

Prop. 5.1 is not a suspect, because Lemma 1 gives minimal position from parity alone. If the parity lemmas hold, the "Furthermore" clause of Prop. 6.7 is what fails.

Two further remarks:
- **The reduction in Thm. 6.9.** As written, that proof shows only that Φ·Γ_1 is reduced and then asserts Φ = Φ′·Γ_1. Given the shortcut criterion, the step is repairable: conjugation by g as above puts any nontrivial element of [K_4, K_4] into the form Φ′·Γ_1.
- **"Proper product" for f(Φ)·Γ.** Prop. 6.7 applies the notion to f(Φ)·Γ in B_5, although the definition and Prop. 5.1 require the first factor to lie in K_5, and f(Φ) does not. That is a misapplication inside Prop. 6.7, not a separate failure.

## 6. What a repair would need

By Lemma 1, under parity M_Φ(t) = ±p(-t), where p(s) = Σ_i s^{k_i} has nonnegative coefficients and records the exponent multiset. BBB compare only p(1) = ι.

Since M^{(j)}(-1) = ±(-1)^j p^{(j)}(1), comparing the first m factorial moments p^{(j)}(1), j < m, cannot separate braids with ρ ≡ I mod (t + 1)^m. A repaired Prop. 6.7 would therefore have to separate f(Φ)Γ from Γ using the full multiset, or moments of unbounded order. We have not checked whether such a version holds.

For Φ0 itself the (t + 1)-adic depth is exactly 1, so the first moment p′(1) may already separate f(Φ0)Γ from Γ. Elements of ker ρ_4 have infinite depth, though, and nontrivial Brunnian braids occur at every depth. So no comparison of moments of bounded order can work. A repair needs a statistic that finitely many moments at t = -1 do not determine. The natural candidate, suggested by the breakthrough chat, is the span max k_i - min k_i of the exponents under parity. A span inequality between f(Φ)Γ and Γ would be the first lemma of a repair, and it looks hard.

## Verification

Three hostile referees, one per lens, read the paper text and this note. None found a refutation:
- **Parity (§1).** Checked the definitions of W_i and the disk sequence, embeddedness of the disks, Lemma 4.2, Cor. 6.8, and the Section 7 polynomials. Script: bbb-gap/check-parity/sec7.py.
- **t = -1 (§2 and the facts about Φ0).** Wrote its own exact code in four conventions: unreduced and reduced Burau, each also with its transpose. Checked that Φ0 is Brunnian via the Artin action on F_4. Scripts: bbb-gap/check-tminus1/chk.py and brunn.py.
- **Construction (§§4-5).** Checked the proper-product definition, the hypothesis lists of Lemma 6.3, Prop. 6.7 and Cor. 6.8, and the free reductions at both junctions.

Corrections from the referees, now folded in:
- the source of |W_i| = |P(Δ_i)|;
- the ± in Lemma 2;
- the boundary-loop normalisation;
- the purity of Φ0;
- the conditional status of the proper-product shortcut;
- the removal of Prop. 5.1 from the suspects;
- the misapplication of "proper product" to f(Φ)·Γ.

A separate chat independently recomputed Φ0. Its unreduced Burau matrix is I at t = -1, and it is not I as a Laurent matrix or at t = 2. Its (t + 1)-adic depth is exactly 1. That chat agreed with the logic of §3.

Not checked: Conditions 1 and 2 of a proper product directly from the figures, and the internal case analyses of Lemmas 6.3 and 6.6.
