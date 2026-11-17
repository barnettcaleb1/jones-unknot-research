# The actual unknot locus in fixed rational twist templates

2026-11-03. Theory-only reduction, with no enumeration or Jones-detection assumption. No novelty claim.

## Statement

Use additive continued fractions

    [x_1,...,x_m]=x_1+1/(x_2+1/(...+1/x_m)).

Allow zero entries by using the matrix convention

    M(x)=[[x,1],[1,0]],
    M(x_1)...M(x_m)=[[p,*],[q,*]].

The first column is primitive because the matrix determinant is +/-1; it represents p/q, including q=0. The empty list has p=1. The numerator closure of the corresponding rational tangle is the unknot exactly when |p|=1, the standard rational-knot classification criterion. For primary background see [Kauffman–Lambropoulou, On the Classification of Rational Knots](https://arxiv.org/abs/math/0212011); their [Hard Unknots and Collapsing Tangles](https://homepages.math.uic.edu/~kauffman/IntellUnKnot.pdf), Sections 4–5, also uses the matrix calculus and the unit-numerator unknot criterion.

**Theorem.** Let x_i=L_i(n) be integer-affine functions of n in Z^s, with the list length m fixed. Then

    {n : |p(L_1(n),...,L_m(n))|=1}

is a finite union of rational affine flats intersected with Z^s. Each nonempty component has the form n_0+ker_Z B for an integral matrix B, so its lattice is saturated.

In particular, this proves the proposed shape statement for the **actual unknot locus** of any fixed rational/2-bridge full-twist template with entries a_i+2n_i. It proves no statement about general knot templates.

## First lemma: a unit numerator forces a small entry

Let p_k be the numerator of the prefix of length k, with p_0=1 and p_1=x_1. The continuant recurrence is

    p_k=x_k p_(k-1)+p_(k-2).

If every |x_i|>=2, then

    |p_1|>=2>|p_0|,
    |p_k|>=2|p_(k-1)|-|p_(k-2)|>|p_(k-1)|.

Since the quantities are integral, |p_m|>=m+1. Therefore a nonempty continued fraction with |p_m|=1 has an entry in {0,1,-1}.

This argument allows arbitrary signs. No positivity assumption on the continued fraction is needed.

## Affine shortening moves

Every small entry can be removed by a shortening move that preserves the absolute numerator and keeps all remaining entries integer-affine in the original parameters.

1. **Internal zero:** replace

       (...,a,0,b,...) -> (...,a+b,...).

   This follows from M(a)M(0)M(b)=M(a+b).

2. **Terminal zero, length at least two:** delete the last two entries (...,a,0). The numerator is unchanged by the recurrence p_m=p_(m-2). If the zero is at the first end, reverse the list first. Reversal preserves the numerator because each M(x) is symmetric, so the reversed product is the transpose of the original product.

3. **Internal epsilon=+/-1:** replace

       (...,a,epsilon,b,c_1,...,c_t)
         -> (...,a+epsilon,-b-epsilon,-c_1,...,-c_t).

   The fraction itself is unchanged, and the numerator changes at most by sign. For a direct matrix verification, put D=diag(-1,1). Then

       M(a)M(epsilon)M(b)
          = epsilon M(a+epsilon)M(-b-epsilon)D,
       D M(c)=-M(-c)D.

   Moving D through the tail changes only an overall sign on the first column. Thus the claim also holds at singular-looking continued-fraction values without dividing by an intermediate denominator.

4. **Terminal epsilon=+/-1, length at least two:** replace (...,a,epsilon) by (...,a+epsilon). The first column changes by the factor epsilon. A small entry at the first end can again be moved to the last end by reversal.

For a list of length one, entries +/-1 succeed and entry 0 fails. The empty list succeeds. These handle all endpoint exceptions.

## Finite affine reduction tree

At a node, the current entries are affine functions of the original n and the current branch has imposed finitely many affine equations.

Branch over every possible choice of a small entry and its value: impose

    current_entry_i(n)=epsilon,
    epsilon in {0,1,-1},

then apply the appropriate shortening move. Each move strictly decreases the list length. Branches reaching the empty list succeed; length-one branches succeed exactly at +/-1. Inconsistent systems may be discarded.

Every successful leaf gives a finite integral linear system Bn=b, and every parameter satisfying it has |p|=1, because all shortening moves preserve |p|. Conversely, every unit-numerator parameter has a small entry by the first lemma; following one such branch repeatedly reaches a successful leaf. The tree is finite because its depth is bounded by m and its branching is finite.

Therefore the original unit-numerator locus is exactly the union of the successful leaf systems. A nonempty solution set of Bn=b is n_0+ker_Z B. The kernel is saturated, since B(kv)=0 implies Bv=0 for every nonzero integer k. This proves the theorem.

No inequalities or congruence conditions are introduced. There is no need to choose the first small entry or make the branches disjoint; overlapping branches are what allow the description to use affine equalities only. The tree need not be computationally efficient.

## Knot parity and scope

For entries a_i+2n_i, the numerator modulo 2 is independent of the parameters. If one member has odd numerator, all members do, so the template stays in the knot rather than two-component-link locus. The reduction proves the actual unknot locus within this fixed knot family; it does not silently change components by deleting a half-twist in the original diagram.

The shortening formulas are algebraic operations on a rational continued-fraction description. They are not claimed to decrease crossing number in every displayed knot diagram. Their role is to bound the depth of the parameter reduction.

Thus no nonlinear integer unknot locus can occur in this fixed-length rational-template setting. A proposed failure of the affine-flat shape statement must use a more general tangle construction or leave the fixed finite affine continued-fraction model. This conclusion is independent of the global Jones unknot conjecture.
