# Exact Jones fibers in fixed multi-twist families

2026-11-03. Elementary relative-skein derivation; no knot computation or novelty claim.

## The family and its finite Laurent model

Fix a diagrammatic tangle construction with s designated boxes. Box i contains m_i strands and is replaced by n_i full twists, where n=(n_1,...,n_s) ranges over Z^s. All outside tangles and all gluing maps are fixed. Assume the closure is a knot; full twists have identity endpoint permutation, so the component structure is then fixed for every n. Fix its orientation once. Let w_i be the algebraic number of oriented strands through box i.

This includes simultaneous twisting about disjoint crossing disks or disjoint meridional disks. More generally it includes any fixed finite planar-algebra contraction of such full-twist operators. It does not include moving later twist sites in a parameter-dependent way that changes their strand counts or the fixed outside contraction.

Over Q(A), TL_(m_i) is generically semisimple. Its full twist has distinct scalar eigenvalues

    lambda_(i,j)=A^(j(j+2)-3m_i),
    j=m_i,m_i-2,...,0 or 1.

Its spectral projectors are fixed rational functions of A and the full-twist operator. For example they follow by Lagrange interpolation in its distinct eigenvalues. Thus for every positive or negative integer n_i,

    FullTwist_i^(n_i)=sum_j E_(i,j) lambda_(i,j)^(n_i).

Substituting these decompositions into the fixed multilinear contraction gives finitely many monomial exponent channels with coefficients in Q(A).

The framing normalization stays linear in all parameters. A full twist of m_i strands changes the oriented writhe by

    sum_(a != b) epsilon_a epsilon_b = w_i^2-m_i.

This number is even, because w_i congruent to m_i modulo 2. Hence the factor (-A^3)^(-n_i(w_i^2-m_i)) introduces no parameter-dependent sign. The normalized exponent of the j-channel is

    b_(i,j)=j(j+2)-3w_i^2.                              (1)

The same correction follows from surgery framings: a meridional ribbon twist changes self-linking by n_i w_i^2. The boxes are fixed, so there are no mixed n_i n_k writhe terms.

Therefore there is a nonzero D(A) in Z[A,A^-1], independent of n, such that

    D(A) delta(A) V_(K_n)(A^-4)
       = sum_(a,b) c_(a,b) A^(a+b dot n),                (2)

where the sum is finite, a is an integer, b is an integer s-vector, and c_(a,b) are integers. One obtains D by clearing all projector/contraction denominators and then expanding the remaining Laurent coefficients. An initial framing unit is absorbed into the intercept a. D is a formal nonzero polynomial; no specialization at its roots is being used.

## Exact affine-lattice theorem

Fix any Laurent polynomial target F(A^-4), in particular F=1. Subtract D delta F from (2), combine identical exponent pairs (a,b), and write the resulting formal defect as

    Phi(A,z)=sum_(i=1)^M c_i A^(a_i) z^(b_i),
    c_i in Z\{0},
    z^b=z_1^(b_1)...z_s^(b_s).                          (3)

Then

    V_(K_n)=F  iff  Phi(A,A^(n_1),...,A^(n_s))=0

as a Laurent polynomial in A.

**Theorem.** The parameter set `{n in Z^s : V_(K_n)=F}` is exactly a finite union of sets

    {n in Z^s : M_P n=v_P},                             (4)

with integral matrices and integral right-hand sides. Each nonempty set is an affine lattice coset n_0+ker_Z(M_P), equivalently the intersection of a rational affine flat with Z^s. The kernel lattice is saturated. The union may overlap and may include points or the entire parameter space.

**Proof.** Call a set partition P of {1,...,M} balanced if every block B satisfies sum_(i in B)c_i=0. For each such partition impose, within every block, equality of the affine exponents:

    a_i+b_i dot n = a_(i_B)+b_(i_B) dot n
    for i in B,

where i_B is a chosen reference index. These are precisely integral linear equations of form (4).

Every solution gives cancellation within each block, hence a zero of the defect. No inequality between different blocks is needed: if two blocks acquire the same exponent, their already-zero coefficient sums still add to zero.

Conversely, at any parameter where the defect vanishes, group its monomials according to their actual exponent of A. Each group has coefficient sum zero, because distinct Laurent monomials are linearly independent. These groups form a balanced partition whose equations the parameter satisfies. There are finitely many partitions, proving the exact finite-union assertion.

For a nonempty component choose one integer solution n_0. All other solutions are exactly n_0+ker_Z M_P. Saturation follows directly from M_P(kv)=0 implying M_Pv=0 for a nonzero integer k. QED.

This is stronger and more specific than calling the set “semilinear”: no congruence holes or one-sided arithmetic rays occur inside a component. Such features could arise for half-twist models with changing endpoint permutation or extra parity phases; those are not the fixed full-twist model above.

## Two parameters: infinite fibers are binomial directions

Suppose s=2 and Phi is nonzero. Every positive-dimensional component of its zero locus must be a line: a full two-dimensional flat would force Phi itself to be zero by the same distinct-exponent argument. Thus an infinite parameter fiber contains a full integer affine line

    n=n_0+k v,    k in Z,

with primitive nonzero v=(v_1,v_2). There is an equivalent factor certificate.

**Corollary.** That full line is contained in the fiber if and only if Phi is divisible in Z[A^+/-1,z_1^+/-1,z_2^+/-1] by

    z_1^(v_2) z_2^(-v_1)
       - A^(n_(0,1)v_2-n_(0,2)v_1).                    (5)

Indeed the substitution z_i=A^(n_(0,i))t^(v_i) defines a map to Z[A^+/-1,t^+/-1]. Because v is primitive, its kernel is the principal ideal generated by (5), as follows by an integral unimodular change of the two z-coordinates. If all integer k lie in the fiber, the substituted Laurent polynomial vanishes at t=A^k for all k; distinct exponent slopes force that two-variable polynomial to vanish identically. The reverse implication is direct substitution.

Consequently a nonzero Phi has infinitely many Jones-target parameters if and only if it has at least one binomial factor of the form (5). If it has no such factor, the exact finite-union theorem leaves only finitely many parameter points. No bound on the number of those isolated points is asserted here.

## Explicit certificates in any number of parameters

A balanced block B gives the identity

    sum_(i in B)c_i A^(a_i)z^(b_i)
      = sum_(i in B, i != i_B)c_i
          [A^(a_i)z^(b_i)-A^(a_(i_B))z^(b_(i_B))].

Thus each affine component comes with an explicit binomial-ideal certificate for Phi, using the block equalities. This does not assert that the displayed ideal is already saturated or prime; the integer solution set is exactly the linear system above regardless.

The result controls the algebraic shape of a fixed twisting family's Jones fiber. It does not identify the knot types on a component, show that a Jones-unit component consists of unknots, or give a reduction from arbitrary knots to one fixed family.

## Concrete two-site corollary: two algebraic-winding-zero crossing disks

Suppose both boxes contain exactly two strands and have w_1=w_2=0. Their normalized sector exponents are 0 and 8, so the exact Jones family has the form

    V_(K_(n_1,n_2))=a+b x+c y+d xy,
    x=A^(8n_1),   y=A^(8n_2),
    a,b,c,d in Q(A).                                    (6)

Assume the entire template is not Jones-unit, meaning that (a,b,c,d) is not (1,0,0,0). Any infinite Jones-unit affine line whose two coordinates both vary has primitive direction (1,1) or (1,-1), up to overall sign. Indeed, along a direction v=(v_1,v_2), the four possible exponent slopes are 0,v_1,v_2,v_1+v_2. With both coordinates nonzero these are distinct unless v_1=v_2 or v_1=-v_2. In the distinct case, infinitely many unit values would force a=1 and b=c=d=0, contrary to the assumption. Primitivity then gives the two stated directions.

The exact conditions are:

* **Opposite-direction line n_1+n_2=m:** it is entirely Jones-unit if and only if

      b=c=0,        a+d A^(8m)=1.

  Substitute n_1=k,n_2=m-k in (6); the three slopes are 1,0,-1, so the two nonconstant coefficients must vanish.

* **Same-direction line n_1-n_2=m:** it is entirely Jones-unit if and only if

      a=1,          d=0,          b A^(8m)+c=0.

  Substitute n_1=k+m,n_2=k in (6); the resulting polynomial in A^(8k) has coefficients a, b A^(8m)+c, and d A^(8m).

In each case infinitely many unit parameters on the stated line already force these identities, and the identities conversely give every integer parameter on the line. This classifies only lines with both coordinates active; it makes no claim that a geometric knot template realizing either coefficient pattern exists.
