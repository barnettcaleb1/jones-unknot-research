# Independent read of the elementary fixed-word argument

15 November 2026. Review of Section6(d) in Claude's Kleinian referee report for TH-FI-EXT. No calculation or search. The proposed tessellation proof is sound. Root supplied the simpler generic-interior-point argument below, which removes even the finite-star bookkeeping. It can replace Jorgensen--Klein as the primary proof of the limit step; the latter remains a separate backup.

## Statement actually needed

After continuous conjugation identify the varying invariant circles and chosen hyperbolic disks. Let Delta_n be the reflection group of a triangle T_n with angles(pi/2,pi/3,pi/n), and let T_0 be its limiting triangle with angles(pi/2,pi/3,0). Assume the three side reflections are fixed words in the marked generators and converge to those of T_0. The triangles converge on compact subsets of the hyperbolic plane. They are strict fundamental chambers for the respective reflection groups.

If g_n belongs to Delta_n and converges to an invertible element g of the extended isometry group of the limiting disk, there is one fixed word W in the marked generators such that g_n=W_n for all sufficiently large n and g=W_0.

This does not assert that polynomial degree bounds word length. It does not presuppose geometric convergence of the whole groups.

## Preferred proof: choose a generic interior point

The limiting reflection tessellation has countably many walls. Since g is an invertible hyperbolic isometry, their inverse images under g are countably many geodesics. Choose

    x in int(T_0) outside g^-1(the union of all limiting walls).

Such a point exists, for example by measure zero of the countable union of geodesics. Then gx lies in the interior of a unique chamber h_0 T_0 for one fixed word h, so y=h_0^-1 gx lies in int(T_0). Both x and y have positive distance from the chamber boundary. Compact convergence of the three sides and convergence h_n^-1 g_n x -> y imply, for all large n,

    x in int(T_n),    h_n^-1 g_n x in int(T_n).

But h_n^-1 g_n belongs to the reflection group. Strict chamber interiors are disjoint under distinct group elements, and the chamber stabilizer is trivial. Therefore h_n^-1 g_n is the identity and g_n=h_n for every sufficiently large n. Taking the limit gives g=h_0.

This chooses x after g is known; there is no need for x to be uniform over all possible limiting isometries. It proves the fixed-word statement without any global local-finiteness or geometric-convergence theorem. For negative similitudes, identify a holomorphic side-swapping map with the orientation-reversing hyperbolic isometry obtained by composing with inversion in the invariant circle. The multiplier's sign is stable near its nonzero limit and that inversion varies continuously, so the same convergence and generic-point proof apply.

## Optional local-star lemma (validates the referee's original choice of x)

Let z be a point of the CLOSED chamber T_0 that lies in the hyperbolic plane. Let F be the finite set of words whose limiting chambers contain z. Then the union of the corresponding chambers k_n T_n, k in F, contains a fixed neighborhood of z for every sufficiently large n.

Here is the explicit justification, avoiding a global local-finiteness assertion.

- If z is in the interior, choose a small closed ball in that interior. Compact convergence of its three boundary geodesics keeps that ball in T_n.
- If z lies in the interior of an edge, take the two chambers on its sides. Their perturbed versions still have that entire common edge, exactly, because the second is obtained by its side reflection. In a sufficiently small ball avoiding both endpoints, these two chambers fill the two sides of the moving geodesic. Their other edges remain outside a smaller fixed ball around z.
- If z is the finite vertex of angle pi/2 or pi/3, take its four or six incident chambers. The same finite words meet at the corresponding moving vertex z_n: the order-two or order-three relation is exact for every n. Their sectors fill the full angle2pi. The other edges of this finite star have positive distance from z in the limit and therefore remain outside a fixed smaller neighborhood for large n. Since z_n tends to z, that neighborhood of z is covered.

There is no ideal-vertex case: the points considered below are images of an interior hyperbolic point under invertible hyperbolic isometries. The finite star may have edges escaping toward the ideal vertex, but the argument takes place in a compact ball about z, away from that ideal vertex.

## Fixed word from the local star

Fix x in the interior of T_0; it is also in the interior of T_n for large n. Select a limiting chamber h_0 T_0 containing gx, with h a fixed word, and put z=h_0^-1 gx. Then

    h_n^-1 g_n x -> z.

By the local-star lemma, h_n^-1 g_n x belongs to k_n T_n for some k in the fixed finite set F. Thus g_n x lies in h_n k_n T_n. Since x is a chamber-interior point and g_n belongs to the reflection group, g_n x is also in the interior of g_n T_n. It cannot lie on a wall. The disjointness of chamber interiors forces

    g_n T_n=h_n k_n T_n.

The reflection group has trivial chamber stabilizer, so g_n=h_n k_n.

The finite candidates h_n k_n have pairwise distinct limits h_0 k_0, since distinct reflection-group elements define distinct chambers. Because g_n has a single limit, exactly one candidate can occur infinitely often and it must occur for every sufficiently large n. The corresponding fixed word W=hk proves the claim.

## Applicability to TH-FI-EXT

The earlier parts of the proof already provide:

1. projectively regular, invertible S_0 at zeta_8, hence S_n -> S_0;
2. S_n in the full holomorphic extended triangle group for all sufficiently large admissible n;
3. E_n as reflection in the side through fix(J_n),fix(J_n M_n), with the other side reflections fixed words in J_n,M_n,E_n;
4. a nondegenerate limiting Hermitian form, allowing continuous disk coordinates;
5. the limiting reflection triangle as a strict chamber for the extended modular group.

Applying the lemma to g_n=S_n yields one fixed word immediately. Vanishing of rational-function projective cross-products at infinitely many distinct A_n then gives [S]=[W] over Q(A), exactly as in the existing proof.

Thus the primary argument may omit BOTH Jorgensen--Klein and the modular coarea bound. Neither conclusion is smuggled into the proof: membership of the limit in the extended modular group is obtained directly from the local chamber star, rather than assumed as geometric convergence. The coarea/Jorgensen--Klein route remains valid as an independently sourced alternative.

## Wording recommendation

Do not merely say “the tessellations converge, hence the word stabilizes.” Use the generic x construction, which reduces the whole argument to compact convergence of two interior points and the strict chamber property. If the referee's arbitrary x is retained instead, supply the local-star argument above. Retain “odd n>30” if that keeps the external triangle-group citation unchanged; enlarging the admissible set is unnecessary for the theorem.
