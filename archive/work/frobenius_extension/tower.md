# Higher cyclic Sakuma lifts: a graph tower, not a colored-knot tower

Theory-only pass, 2026-11-03. No numerical search. These are direct covering-space deductions and a consequence of hyperbolic Dehn filling; novelty is unassessed. The conclusions do not depend on assuming an unknown Jones-trivial example exists.

## 1. Exact topology of the lifted crossing disk

Let S=U union c be a winding-zero crossing-circle link, with U unknotted and c=boundary D, where the disk D meets U transversely twice with opposite signs. Let pi_p:S^3->S^3 be the p-fold cyclic cover branched along U, and put

    F_p=pi_p^-1(D),       L_p=boundary F_p=pi_p^-1(c).

Then F_p is a CONNECTED genus-zero surface with p boundary components.

Proof. The two puncture meridians of D map to +1 and -1 in Z/p. Either generates the cover, so the punctured-disk cover is connected. The total boundary monodromy is zero, so boundary D has p separate degree-one lifts. Riemann-Hurwitz gives chi(F_p)=p-2(p-1)=2-p. With p boundary components, 2-2g-p=2-p forces g=0. This includes the actual cyclic branched neighborhoods at both punctures, so it describes the embedded surface, not merely an abstract unbranched cover.

Choose an arc alpha in D joining the two branch points. Its lift is a spatial theta_p graph: two vertices joined by p edges. F_p retracts onto this graph, and its 3-dimensional regular neighborhood is a handlebody of genus p-1. At p=2, theta_2 is a circle and F_2 an annulus; its core is the covering knot kappa. For p>2 the natural object is a handlebody/spatial-graph embedding. There is no distinguished knot core supplied by this construction.

This establishes the precise missing identification in an attempted color tower. A planar surface having p boundary components does not identify its boundary with a p-parallel of the p=2 core.

## 2. The exact Frobenius congruences that do survive

Use P(A,z), the annular bracket of c in the complement of U, with the downstairs framing fixed as in U5-FROB5. If the preferred Sakuma link has unlink Jones, the existing two-measurement argument gives

    P(A,z)-delta(A)
       =(z²-delta(A)²)(z²-lambda(A)²) R(A,z²),
    delta=-A²-A^-2,       lambda=-A^4-A^-4.

For p=2^r, the state-orbit proof works under the full cyclic deck group: every non-fixed orbit has even size. Hence, with the INDUCED lifted framing,

    <L_p>(A)=P(A^p,delta(A)) modulo 2.

The essential-circle lift stays one circle; a contractible circle lifts p times; delta(A^p)=delta(A)^p in characteristic two. Therefore

    <L_p>-delta^p
      =(delta²-delta^(2p))(delta²-delta^(4p)) R(A^p,delta²)
        modulo 2.                                            (T)

Thus the higher tower does provide graph-link congruences with increasingly large cyclotomic factors. It does NOT give the colored Jones polynomials of kappa without a new topological relation. At p=2 the annulus and preferred framing supply exactly that relation. For higher p, individual zero framings also cannot be inferred merely by repeating the p=2 argument: linking transfer gives self-framing plus a SUM of mutual linkings equal to zero, not termwise vanishing.

The algebra in (T) is a substitution in the same two-measurement factorization. At the formal annular-skein level it introduces no further equation on P. Its potential additional strength would have to come from actual topology of the theta_p embeddings or their linked boundaries.

## 3. A rigorous obstruction to replacing higher lifts by ordinary cables

**Proposition.** If the exterior of S=U union c is hyperbolic, then the exterior of L_p is hyperbolic for all sufficiently large p. Consequently those L_p are not ordinary parallel cables of kappa (or of any knot).

Proof. On the U cusp of E(S), use generalized meridional filling coefficient (p,0), leaving the c cusp complete. For sufficiently large p, hyperbolic Dehn filling gives the orbifold with underlying space S^3 minus c and singular locus U of order p. Equivalently its cone angle at U is 2pi/p. Its cyclic p-fold manifold cover is exactly S^3 minus L_p; pulling back the orbifold metric removes the cone singularity and gives a complete finite-volume hyperbolic metric. In contrast a parallel link with at least two components has a nonhyperbolic exterior: for a nontrivial companion it has an essential companion torus/parallel annulus; for the unknot it is an unlink or a torus-link-type parallel, likewise nonhyperbolic.

The primary reference for the small-cone-angle filling statement is [Cooper-Hodgson-Kerckhoff, Three-dimensional Orbifolds and Cone-Manifolds, section 5.6, Theorem 5.12](https://web.math.ucsb.edu/~cooper/37.pdf#page=109). The Dehn-surgery parameter satisfies x*mu+y*lambda=2pi*i; (p,0) therefore has meridional angle 2pi/p. Their section 7.2, printed p.122, explicitly leaves unfilled boundary tori as cusps throughout the small-angle deformation. This is the standard multicusped version, not a claim that the primitive slope (1,0) varies with p.

The hyperbolic hypothesis is conditional and essential to this argument. I have not proved it for every preferred Sakuma link, and no hypothetical flat Sakuma example is asserted to exist. The proposition nevertheless prevents a GENERAL theorem identifying all higher cyclic lifts with the ordinary parallel cable tower.

## 4. Decision for U5-FROB5

The twofold construction is exceptional for a topological reason: its ribbon surface has a knot core. Raising the cyclic degree moves from knots to embedded theta graphs, and in the hyperbolic case eventually produces hyperbolic links rather than satellites. The existing finite-root obstruction therefore does not automatically bootstrap to infinitely many colors of the same kappa by this operation.

A legitimate future mechanism would need either (i) a relation between these actual theta_p quantum invariants and the colored invariants of theta_2, with its hypotheses proved, or (ii) a detection theorem for the whole equivariant graph tower using the band/cover structure. Neither is established here. This is a boundary on an amplification method, not a new attack on those larger detection problems.
