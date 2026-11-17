# Fixed twist templates: exact fibres and binary-input complexity

2026-11-17. Audit of the unrefereed complexity-lens “Theorem S” in Claude's letter 20261117-123654. Theory only; no enumeration. This is a scoped consequence of the existing notes `work/global_design/multitwist_locus.md` and `multitwist_geometry.md`, not a new knot-detection theorem.

## Verdict

**Sound after fixing the input model.** For a fixed finite twist template, Jones equality to a fixed target is a finite union of integer affine flats; allowing half-twist parity and equality up to a monomial gives a finite union of affine sublattice cosets. Membership is decidable in time polynomial in the binary lengths of the twist parameters. Neither result needs the Brownawell–Masser theorem. The exact fibre statement is already D-MULTITWIST from 3 November; the complexity statement is a direct sparse-arithmetic corollary.

This establishes a tractable restriction of Jones-triviality. It does **not** establish unknot recognition in that restriction, classify the topology of a unit flat, or support the unrestricted sentence “twist parameters cannot carry counting.”

## 1. Precise input and prior skein formula

Fix a finite marked diagrammatic contraction with k boxes. At box i insert n_i full twists on a fixed number of strands, for arbitrary n_i in Z. All outside tangles, strand counts, boundary identifications and orientations are fixed. Full twists have identity endpoint permutation, so the component count is fixed. One may restrict to a template whose closures are knots.

The generic Temperley–Lieb spectral expansion of a full twist has finitely many fixed rational projectors and monomial eigenvalues. Expanding each box in the fixed contraction and clearing denominators gives

    F_n(A) = N_n(A)/D(A),
    N_n(A) = sum_(j=1)^s c_j A^(alpha_j + beta_j · n),        (1)

where D is a fixed nonzero integer Laurent polynomial, c_j are fixed integers, and alpha_j and beta_j are fixed integer exponents. F can be the framed bracket, the correctly normalized Jones polynomial expressed in A, or a specified scalar J obtained by a fixed skein contraction and monomial normalization. The denominator includes every fixed normalization factor, including delta if that bracket convention requires it.

For the ordinary two-strand half-twist model, this input is explicit in Champanerkar–Kofman, *On links with cyclotomic Jones polynomials*, Proposition 2.1:

    delta^k <L_n> = A^(sum_i n_i)
                     P(A,(-A^-4)^n_1,...,(-A^-4)^n_k).

Their proof diagonalizes the two-strand crossing as A p_0 - A^-3 p_1. The paper also identifies its twist-bracket with the earlier general central-idempotent construction. [Primary source, Proposition 2.1](https://www.math.csi.cuny.edu/~abhijit/papers/cjp_AGT.pdf).

There is no need for the operators in different positions of the contraction to commute: expanding each of a fixed number of independently parameterized boxes suffices. Geometric disk twists with disjoint support are an important instance, not a necessary extra algebraic hypothesis.

**Framing.** In an oriented m-strand full-twist box with algebraic winding w, one full twist changes writhe by w^2-m. This is even, since w and m have the same parity. The Jones writhe correction is therefore a monomial with exponent linear in n and no varying sign. It is absorbed into alpha and beta in (1). A fixed initial sign is absorbed into c_j. For any additional preferred normalization used for J, its exponent must likewise be established as affine on the parameter class; it must not be inferred separately at each sample.

**Half twists.** First divide the parameters into their finitely many parity classes. On each class the signs and endpoint permutations are fixed, n=2m+r, and the same model applies in m. Discard classes whose closures are not knots if the question is restricted to knots. More general fixed periodic endpoint phases can be handled by a finite residue-class split. Arbitrary parameter-dependent connectivity or moving sites are outside this model.

## 2. Fixed target: balanced partitions give the complete fibre

For a fixed Laurent target Q, expand N_n-DQ as

    sum_(j=1)^M d_j A^(a_j+b_j·n),                       (2)

with integer d_j. A partition of {1,...,M} is balanced when each block has coefficient sum zero. For every balanced partition, require equality of all affine exponents within each block. These are integer linear equations Bn=v.

Their integer solution sets give the fibre exactly. If (2) vanishes, grouping its terms by their actual exponents supplies such a partition, because distinct Laurent monomials are linearly independent. Conversely, each balanced block cancels, even when two blocks collide. There are finitely many partitions, so the fibre is a finite union of nonempty sets n_0+ker_Z B. These kernels are saturated. Points are the rank-zero cases; a separate “finite exceptional set” is unnecessary.

After a parity split these become affine sublattice cosets in the original parameters, which need not be saturated. This proof is elementary and constructive. General function-field S-unit results are not needed and do not improve this conclusion for the present model. The balanced-partition construction may have very large preprocessing cost; the membership algorithm below does not enumerate partitions.

## 3. Unknown monomial: exact locus and exact decision

For units of Z[A,A^-1], the question is

    F_n(A) = epsilon A^m,       epsilon in {+1,-1}, m in Z.

For each sign apply the preceding argument to N_n-epsilon A^m D, now treating (n,m) as the variables. This is again a finite union of affine integer solution sets. Projecting each solution coset to n gives an affine sublattice coset: the projection of a lattice is a lattice. For half twists, include the parity split first.

On each such coset the value is a monomial with a possibly **varying** exponent m. This is the meaning of “identically a monomial”; it need not be one fixed monomial. The exponent is unique whenever a solution exists, because D is nonzero. On the lattice directions of a projected coset it is an integer-valued affine homomorphism. Projection need not preserve saturation, so the more cautious “affine sublattice coset” formulation is appropriate here.

For membership no search over m is needed. Group the equal exponents of N_n and remove zero coefficients. If N_n is zero, reject. Otherwise let nu and deg denote its least and greatest surviving exponents, and let d_min,d_max be those of D. A possible unit must have

    m = nu-d_min,
    deg-nu = d_max-d_min.                              (3)

If (3) fails, reject. Determine epsilon by comparing the coefficient at nu with epsilon times the coefficient of D at d_min; if neither sign works, reject. Finally compare the two sparse Laurent polynomials N_n and epsilon A^m D exactly. This criterion is necessary and sufficient even without assuming in advance that N_n/D is Laurent. Merely testing span zero of a Laurent quotient would miss a nonunit constant coefficient.

Testing F_n=1 is simpler: compare N_n directly with D. If the desired unit is only A^(4m), or t^m with t=A^-4, also test the resulting exponent congruence. A normalization that proves “every possible unit J equals 1” may of course remove the unit search entirely, but is not needed for this algorithm.

## 4. Bit complexity

Encode n_i as signed binary integers and put

    L = sum_i (1 + ceil(log_2(2+|n_i|))).

For a fixed template, k,s,c_j,alpha_j,beta_j,D and Q are constants independent of L. Each affine exponent in (1) is computable with O(L)-bit integer arithmetic. Sorting a fixed number of such exponents, summing the fixed integer coefficients at collisions, and comparing against a fixed number of shifted denominator or target terms take O_T(L) elementary bit operations with ordinary fixed-constant arithmetic; the weaker polynomial bound is more than sufficient. The constant depends on the entire template, not only k. There is no expansion into an array indexed by every exponent up to max |alpha_j+beta_j·n|.

For a uniformly supplied **explicit sparse model** (1), the same method is polynomial in its description size plus L: use binary integer arithmetic for dot products, exponent comparisons, and coefficient sums. This is distinct from being given a diagram and constructing that sparse model.

An expanded diagram has crossing count comparable to sum_i |n_i| up to template constants. It may be exponentially larger than the binary parameter list. Accordingly “polynomial in log |n|” describes a succinctly represented, fixed-template problem, not a uniform polynomial-time algorithm for Jones-triviality of arbitrary diagrams. The sparse numerator can have bounded support while division by fixed D produces a Laurent polynomial with unboundedly many terms; deciding equality does not require printing that polynomial.

## 5. What does not follow

1. **A fixed number of slots is not a fixed template.** If the outside diagram, strand counts, or gluing complexity is input, extracting the coefficients and projectors can dominate the work. The number of channels or expanded coefficient terms can grow exponentially. The proof supplies no polynomial preprocessing bound from that diagram input.

2. **Arbitrary braid powers are not automatically twist slots.** A fixed crossing, full twist, or other operator already proved semisimple with monomial eigenvalues satisfies the same argument. A general braid matrix can have nonmonomial eigenvalues; a nonsemisimple operator can produce polynomial factors in n. Neither has the constant-coefficient affine-exponent model (1) merely because its matrix dimension is fixed. Fixed matrices may still be amenable to other algorithms, but that requires a separate theorem.

   The distinction is mathematically essential for broad matrix-power claims. With U(n)=I+nE_12 and V(m)=I+mE_23 in dimension three, the (1,3) coefficient of U(n)V(m)(I-lE_13) is nm-l. Its integer zero locus is not a finite union of affine lattice cosets. Each matrix is a power of a fixed unipotent matrix. This is an algebraic counterexample to an unrestricted matrix-power version, **not** an assertion that these matrices arise from an actual braid or tangle.

3. **The result does not classify unit knots.** An infinite parameter coset may contain one knot type, or many. Whether a Jones-unit coset admits a nontrivial knot remains the geometric question in `multitwist_geometry.md`. Isolated unit points also remain.

4. **“Twists cannot carry counting” needs a complexity hypothesis and an input restriction.** What is proved is that binary twist parameters in one fixed model give a language in deterministic polynomial time. Any claimed polynomial-time hardness reduction into that same fixed model would therefore imply the corresponding complexity collapse. No unconditional prohibition follows. Growing templates, variable numbers of sites, and reductions that encode information in the fixed part are not covered. Nor does an easy equality test imply that every numerical statistic of the family is uninformative.

## Recommendation

Bank **FIXED-TWIST-P** as an elementary algorithmic corollary of D-MULTITWIST, with a link to the established twist-bracket construction. It is a useful negative control for proposed complexity gadgets: enormous binary twist exponents alone, in one fixed finite template, do not escape the sparse comparison algorithm. Do not present it as a new Brownawell–Masser reduction or as new leverage toward Jones unknot detection. The worthwhile open bridge is uniform complexity when the template itself grows, together with which connectivity-preserving gadgets can realize that growth.


## Referee closure

Claude124955 accepts the fixed-template algorithmic corollary with D-MULTITWIST credited. FIXED-TWIST-P is PROVED under the collaboration protocol (Codex125018); external review and novelty remain unassessed. All input-model restrictions above remain part of the statement.
