# EKT and the proposed wrapping-two axis: the components themselves are knotted

Date: 2026-11-03. Conceptual archive/primary-source pass only; no new diagram computation or enumeration.

## Answer to Q1

**The standard nontrivial LL1 and LL2 families are not an unknotted component encircling a pattern. Both actual components are nontrivial knots.** Their description as Hopf satellites involves two auxiliary companion solid tori, with both components patterned inside them. The wrapping-two statement for those auxiliary tori is not wrapping two about either actual link component: the complement of either actual component is not a solid torus.

In fact the same conclusion holds for every nonzero member of the archived EKT opposite-omega construction starting from any unknot-numerator seed. The short proof below uses existing primitive peripheral data, not new calculations.

## Primary-source geometry

EKT, *Infinite families of links with trivial Jones polynomial*, Topology 42 (2003), §2 identifies the sublinks of H(T,U) as the numerator closures T^N and U^N, lying in companion solid tori V_T and V_U whose cores form a Hopf link. It gives a meridional disk meeting each numerator in two points and proves geometric essentiality when the corresponding tangle has no NS-separating disk. Thus the essential component patterns have geometric index exactly two **in the companion tori**.

In §4.1, LL2(n)=H(T_n,-T_n), with T_1=3, T_2=5·1·2, and subsequent rational tangles. In §4.2, LL1(m,n)=H(T,-3). These descriptions already identify the relevant components. [Primary paper](https://homepages.math.uic.edu/~kauffman/ekt.pdf), pp.159–160 and 165–166.

## Uniform component-determinant lemma

Let S have numerator U, and consider the EKT family

    L_j = H(S^(omega^j), (infinity+2)^(omega^(-j))).

Normalize S's primitive Fox/peripheral pair as (1,d), with d an integer. The validity of this integral pair for a possibly nonrational S follows from the actual S3 filling of its double cover; it is explained and audited in `work/band_obstructions.md`, §3 and §7.

Write

    Omega^j = [[a,8b],[b,a]],   a>0,   a²-8b²=1.

The two component numerator determinants are

    det K_T = |a+8bd|,       det K_U = a.

For j nonzero, b is nonzero, a>=3, and a<=3|b|, the last inequality following immediately from a²=8b²+1<=9b². If d=0, the first determinant is a>=3. If d is nonzero,

    |a+8bd| >= 8|b|-a >= 5|b| >=5.

Thus both component determinants exceed one. In particular neither component is an unknot. The numerator determinants are odd; since these tangles have two arcs and no closed components, their numerator closures are knots, as also follows from the construction.

This proves the assertion for the entire archived unknot-seed family, including all nonzero positive and negative iterates. It says nothing about arbitrary other choices of H(T,U), a different Jones-trivial seed, or a different Jones-preserving construction.

## Explicit standard families

For LL2, the archived recurrence gives

    (p_(n+1),q_(n+1))=(3p_n+8q_n,p_n+3q_n),  (p_0,q_0)=(1,0).

The components are a two-bridge knot of determinant p_n and its mirror. For n=1 these are the trefoil and mirror trefoil; for n=2 their determinants are 17. All n>0 have p_n>1. Strict unlink Jones occurs for even n; odd n has the orientation-dependent monomial factor described in EKT Theorem 4.1. Thus the exact Jones-trivial even subfamily still has both components knotted.

For LL1(m,n), the second component is the numerator of -3, hence a trefoil. The first determinant is

    |p_T| = |(8A-1)/3|,   A=4^m(3n+2).

Here A is an integer congruent to 2 modulo 3. Its allowed values give |p_T|>=3, so the other component is nontrivial too. This component need not be two-bridge for m>0; no rationality assumption is used to infer its nontriviality from the determinant.

The published/source indexing has a minor LL1/LL2 coincidence typo noted in `work/ekt_homology_notes.md`; no argument here uses that coincidence.

## Independent obstruction from the marked band

The existing archive also proves

    H1(Sigma_2(L_j)) = Z + Z/|1+12b(b+ad)|,

with nonzero finite torsion for every j nonzero. Therefore none of these links admits a band to any determinant-one knot, in particular to U. This is independent of the absence of an unknotted component. For LL2(n), the finite order is 1+12q_n²; for LL1 it is |12·4^m(3n+2)-1|.

## Implication for Claude's dichotomy

The proposed alternatives “EKT is wrapping two around an unknot” versus “EKT needs higher wrapping around an unknot” do not cover these standard families. They have **no actual unknot axis at all**. The two index-two companion patterns should not be merged into a single annular pattern around an actual component.

Consequently these examples do not, by themselves, decide whether the desired wrapping-two/unknotted-axis statement is true or false. Their absence from that class is not evidence that the class satisfies Jones detection. The unknown geometric statement must still be proved for the actual marked-band locus.

The full EKT template permits more inputs than the standard unknot-seed orbit. No classification of all inputs yielding an unknotted component and unlink Jones was established in this pass, and no numerical wrapping bound about an actual unknotted component is claimed for such unclassified inputs.
