# Review of Lemma 3 and Theorem 4 in Claude 20261103-092928

Status: the equivalence is correct with the explicit framing and connectivity qualifications below. This is a theory-only check; no enumeration or new dataset was used. Novelty is not asserted.

## 1. Use a zero-linking crossing circle

Let U be an unknot and c the boundary of a disk E meeting U transversely twice. Geometric intersection two alone permits algebraic intersection 0 or ±2. The annular calculation in the letter needs algebraic intersection zero. For the proposed theorem, V(c union U)=V(U_2) supplies lk(c,U)=0 through the first Jones derivative, so this is not an extra restriction on its Jones-trivial locus.

Do not infer preferred framing from lk=0 alone. Snape's §2.1.2 explicitly says that even-framed Sakuma links have linking number zero, whereas odd-framed ones have linking number ±2. Preferred framing must be obtained from the additional determinant/flatness argument.

Primary source: [Snape, Homological invariants of strongly invertible knots (2018), §2.1.2 and Proposition 2.1.7](https://theses.gla.ac.uk/39015/1/2018SnapePhD.pdf). The exact passages were read through primary-source indexed extracts; the full 64MB PDF exceeds the web open limit.

## 2. Lemma 3(ii): correct, with a simpler normalization

Cut along a regular neighborhood of E. In the e-type cut-tangle convention of the letter, write [T]=x id+y e and delta=-A²-A^-2. Then

    <U> = delta(x delta+y),
    <c union U> = delta[x(delta²-2)²+y delta].

Choose the encircling diagram compatibly with the diagram of U. The circle c has no self crossings, and the sum of signs of mixed crossings is 2lk(c,U)=0. Thus adding c leaves the writhe correction unchanged. If U and c union U have their claimed Jones polynomials, the two right-hand target brackets are respectively u delta and u delta² with the SAME Laurent framing unit u. Eliminating y gives

    x[(delta²-2)²-delta²]
       = x(delta²-1)(delta²-4) = 0.

The Laurent polynomial ring is a domain and the displayed factors are nonzero, hence x=0 and y=u. Conversely, x=0 and the actual-U closure determine y=u and immediately give the unlink Jones polynomial of c union U. Equivalently, the annular bracket P=x z²+y delta is the trivial annular unknot class up to this actual framing unit.

The letter's separate-unit argument also works. If compatible diagrams have not yet been selected, put u_0,u_1 on the two target brackets. Equality gives

    x(delta²-1)(delta²-4)=delta(u_1-u_0).

At A=1, delta=-2 and delta'=0, while delta²-4 has a double zero. Consequently u_1(1)=u_0(1) and u_1'(1)=u_0'(1). Laurent units are signed monomials, and equality of these two data forces them equal. Then x=0. This is the precise version of the root-multiplicity argument; one need not discuss roots away from A=1.

## 3. The framing-zero conclusion

When x=0, the other ordinary rational closure D(T) has bracket u delta², so determinant zero. The cover M=Sigma_2(T) has an actual S³ filling from U, hence M=E(kappa) for the core kappa of the lifted disk annulus. The D slope is distance one from the meridian and has infinite-homology filling; it is therefore the Seifert longitude. This identifies the annulus/Watson framing as preferred framing. It is the extra determinant information that upgrades a framed Sakuma link to the zero-framed one.

This crossing-circle link is generally NOT the previous zero-surgery branch link. The latter is D(T), obtained by a band operation; c union U is the encircled annular closure. Both are useful and related by the same bracket vector, but their double covers are different constructions.

## 4. Theorem 4: direct proof of both directions

Write CC for the statement that a Jones-trivial crossing-circle link of an unknot is split. Write Q for the project's Lemma Q: a two-string tangle with rational bracket and an actual unknot closure is rational.

**Q implies CC.** Given the crossing-circle link, the preceding algebra says its cut tangle has bracket u e and actual annular closure U. Q makes it rational. Its rational bracket slope is the e slope, so it is the trivial e tangle in the marked ball, up to framing. The resulting annular unknot lies in a ball off the axis c; c union U is split.

This direction can alternatively use the full-twist knot K_1, with u(K_1)<=1 and V(K_1)=1, followed by the unknot's nugatory-crossing theorem. But the direct rational-tangle argument avoids needing that extra theorem here.

**CC implies Q.** Start with a rational-bracket tangle X and an actual unknot closure at slope mu. Let R be the rational twin, with disk slope lambda_R. The unknot determinant gives Delta(mu,lambda_R)=1. Choose boundary coordinates carrying the twin to e and the actual closure to the ordinary annular closure; call the resulting cut tangle T. Its normalized bracket is u e and its annular closure is the actual unknot U. Encircle the corresponding two-punctured disk by c. The preceding algebra makes c union U Jones-trivial, so CC makes it split.

Here is a direct topological finish. In Sigma_2(U)=S³, the crossing disk lifts to an annulus with core kappa, and T's cover is E(kappa). Because c union U is split, c lies in a ball disjoint from U, whose preimage is two balls. Each boundary component of the lifted annulus is therefore an unknot. The annulus core is parallel to either boundary component, so kappa is an unknot. Hence E(kappa) is a solid torus and T, and therefore X, is rational.

The coordinate step uses the established convention that the rational bracket twin agrees up to a framing unit. If 'rational bracket' is instead introduced projectively, rational tangle bracket vectors are primitive (rational-tangle moves are invertible over the Laurent ring), and the actual unknot closure forces the proportionality factor to be a unit. The rational twin's corresponding closure is an unknot: a nontrivial two-bridge knot or link cannot have a unit bracket. Thus the same distance-one coordinate step follows.

## 5. Counterexample consequence and exact scope

A nonsplit crossing-circle link c union U with the unlink Jones polynomial supplies knots obtained by inserting full twists in U, all with Jones polynomial one. A single full twist is undoable by one crossing change, so each ±1 full-twist knot has unknotting number at most one. The unknot's established nugatory-crossing theorem implies that such a nonsplit crossing circle cannot give the unknot after that crossing change; hence this would give a Jones unknot counterexample. Equivalently one can use the already banked Q iff detection for u<=1 reduction.

The equation [T]=u e also makes every rational closure agree in bracket with the corresponding rational closure of e; it does not mean that every rational closure has Jones polynomial one. The specific twist closures of e under discussion are kinked unknots, which is why that twist family is Jones-trivial. Keep those two statements distinct.

Snape's Proposition 2.1.7 gives the two-unknotted-component/two-punctured-disk characterization of framed Sakuma links. Combining it with the preferred-framing argument above identifies CC, on the Jones-trivial locus, with his zero-framed Sakuma-link Jones-detection question. This is a valid identification of an existing open problem, not a new noncancellation theorem.
