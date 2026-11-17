# ref-transfer: hostile referee report on build-transfer/transfer.md

Lane g2-proof, 2026-11-03. This is a referee pass. Nothing was edited outside this folder.

**Verdict: DAMAGED.** The negative core is correct. The count step of BBB is blind on BI_n, and BBB's proof is invalid on Brun_4 ∩ BI_4. The transfer then goes further and concludes that the BBB method is dead at its core (parity "fails", "no crux inside BBB", and only LT is left). That conclusion does not follow.

## 1. Checked against BBB v2 (arXiv HTML, read this session)

- **The paper.** v2, dated 14 Sep 2026, is the current version. Its comment reads "Minor corrections and improved exposition". There is no v3, and a search found no published critique.
- **Parity, as defined.** A disk Δ in the sequence is sign-changing iff |P(Δ)| is odd. "Sign-changing" means ε_i = -ε_{i+1}.
- **Lemma 3.1 (Bigelow).** W_i = k_{i+1} - k_i, where W_i = ±(number of punctures in Δ_i).
- **Lemma 4.2.** Parity implies no cancellation. The proof is the (-1)^k bookkeeping.
- **Prop 6.7.** It asserts that "both f(Φ)·Γ and Γ satisfy the parity condition". It then adds "Furthermore we may choose Γ so that" the two values of ι(·, α) differ.
- **Cor 6.8.** The proof uses no cancellation on both sides, so each L1 norm equals ι. The step that the two ι differ is introduced as "we can assume".
- **Thm 6.9.** "we may assume that Φ has been conjugated so that it can be written as a proper product". This step is only sketched.
- **Missing topics.** The text and the references never mention t = -1, the double cover, BI_n or BMP.

The Shadow Lemma is therefore correct: under parity, ε_i(-1)^{k_i} is constant, so |M(-1)| = m. Corollary 2 is correct too, since M is Z[t^±]-linear in the class.

**Phi0 re-run.** Phi0 = [(s1 s2)^6, [[y1,y2],y3]] has a 112-letter word. Its Burau image is the identity at t = -1 and not the identity at t = 2 or t = 3/2 (exact arithmetic). It is Brunnian and lies in BI_4, since both subgroups are normal.

So BBB's argument as written would prove ρ_4(Φ)|_{t=-1} ≠ I for every nontrivial Φ in Brun_4. That is false for Phi0. The gap claim survives.

## 2. Localizing the BBB failure (sharpens transfer §2.3)

Take Φ ∈ BI_4 to be a proper product Φ'·Γ_1 with m = ι(Φ). Let Γ be the unmodified push from Prop 6.7 (γ_2 γ_1), which is disjoint from β modulo 4-disks and properly simple modulo 4-disks. Then:
1. Lemmas 6.3 and 6.4 say f(Φ)Γ has Φ's disk sequence with its 4-disks replaced by sign-changing 5-disks. So it satisfies parity and has m points.
2. The Shadow Lemma gives |M_{f(Φ)Γ}(-1)| = m, and since f(Φ) ∈ BI_5, |M_Γ(-1)| = m.
3. Lemma 6.6 says Γ satisfies parity, so ι(Γ) = m = ι(f(Φ)Γ).

So, on BI_4, Lemmas 6.3, 6.4 and 6.6 together with Prop 5.1 force equal counts for the unmodified push. Either one of those lemmas, or the conjugation step, is false, or the failing step is the "Furthermore" modification (Figs. 6.9-6.12, the "we can assume"). This also gives a test that needs no figures: for Φ in BI_4, the identity ι((β*_3)Γ, α) = ι((β*_3)Φ, α) must hold.

## 3. The strongest objection: parity is not what is blind

The Shadow Lemma characterizes the parity condition. It does not say that parity throws information away.

- **What parity gives.** Under parity, M(-t) = c · Σ_i t^{k_i} with c = ±1. The whole exponent multiset is still there, with no cancellation.
- **What two-sided parity decides.** Suppose both ψΓ and Γ satisfy parity. Then M_{ψΓ} = M_Γ (up to a unit) iff their exponent multisets agree up to translation. This is decided by the power sums p_j = Σ k_i^j.
- **Equal sizes.** For two multisets of the same size m, Newton's identities show that p_1..p_m decide equality.
- **Graded blindness.** If ψ ∈ F_k (ρ(ψ) ≡ I mod (t+1)^k, which is Kasahara's h-adic filtration for genus two), the moments of order < k agree. So a coherent comparison of size m is blind exactly on F_{m+1}, and not on BI = F_1.
- **Where the count sits.** The count statistic is the order-0 case. It is the only statistic that the Shadow Lemma kills.
- **An example.** Equal low moments with different extremes do occur: Prouhet-Tarry-Escott multisets. So comparing spans is not blind on BI_n by this argument.

**Consequences for transfer.md.**
- Step 5 ("parity fails as a method, blind on Torelli") is wrong. Parity transfers as a no-cancellation device, modulo NL1 and NL3.
- The last sentence of §4.4(b) is false: "everything that could distinguish psi from 1 lies in the cancelling, parity-violating part". When both sides are coherent there is no cancelling part.
- §5 ("BBB contributes nothing to the core") and the crux field ("No crux exists inside BBB's method") are wrong. A non-blind criterion exists inside BBB's architecture: two-sided parity plus an inequality between the exponent multisets or spans. BBB's own proof of Cor 6.8 names the extreme exponents M- and M+ and then uses only the L1 norm.
- LT is not the only non-blind replacement. Under two-sided coherence, extremal sign coherence holds automatically.

## 4. Repair

**Restated obstruction.** The count (L1) comparison is the q = -1 value, and it is blind on BI_n. A size-m coherent comparison is blind on F_{m+1}. Steps 5-9 should be relabelled as follows:

| Step | Relabelled as |
|---|---|
| 5 | transfers (needs NL1, NL3) |
| 6 | open (NL2) |
| 7, 8 | open: BBB's own multi-push problem. This is not a necessary failure. |
| 9 | fails as stated. Replace the ι-inequality by an inequality of exponent multisets or spans. |

**Crux inside BBB at n = 4 (new, open).** Only Brun_4 ∩ BI_4 needs any argument, because ker ρ_4 ⊂ BI_4, and off BI_4 nonmembership in the kernel is already visible at t = -1. For every nontrivial proper product Φ in Brun_4 ∩ BI_4, the unmodified push Γ should give different exponent multisets:
- for f(Φ)Γ, the exponents are k_i + s_i, where s_i is the signed number of 4-disks before position i;
- for Γ, the exponents are read off Γ's own disk sequence (1-, 2-, 3- and 5-disks).

These are explicit from the disk sequences by Lemma 3.1, and no cancellation control is needed. Strength: this implies Burau_4 is faithful on Brun_4, so the statement is faithfulness-strength. Constraint: it must fail if the depth of Φ exceeds ι(Φ).

**W(5,1).** The same criterion needs two more things, so the real obstacles are steps 7-8 and the stabilization, not blindness:
1. Two-sided two-point coherence. This needs at least two pushes and the sector condition NL3, and it is open.
2. A genuinely new point. In W(6,0) the pushes of p6 already lie in B_5/Z, so step 3 is only formal. The stabilization has to go through W(6,2) = W(5,1) + Burau_5 (restricted to B_5), together with ker Burau_5 (Bigelow) and Long.

## 5. Dependencies and minor errors

- **F2.** The transfer uses it only as Long 1986, which is published. That is fine.
- **F3, not flagged.**
  - The step "every kernel element lies in BI_5" goes through Kasahara Thm 5.1 transported to B_5, and so uses F3. F3 is essentially Kasahara 2008 / Bigelow 2002.
  - §0.3 misstates the conclusion: the coset over -I in Sp(4,Z) is omitted there, although §4.4 has it.
  - The obstruction itself does not need F3. BI_5 lying in the projective kernel at A^4 = -1 is checked, and BMP plus Long finish the argument. In fact TL_5 at δ = 0 is semisimple, so W(5,1) stays irreducible there.
- **F6.** Only the twist formula is used, and it was checked independently.
- **The chain from LT to faithfulness.** LT => KL(3|C) => faithful rests on read-model Thm D. In Thm D, Lemma C is only sketched and the normalization of (E3) is not fixed. The crux field does not flag this.
- **Strength chain.** "W(5,1) faithful => Burau_4 faithful" is correct. It follows from the branching W(4,0) + W(4,2), the fact that W(4,0) factors through B_3, and Long (Kasahara Rem 5.6).
- **Minor errors.**
  - Step 7: the "three non-nested types" are read-bbb's reformulation, not BBB's own remark.
  - §4.5: the roots-of-unity clause is ill-posed, since real signs cannot equal non-real character values.
  - §4.4(c): "order 1 = tau_2" is untagged.
