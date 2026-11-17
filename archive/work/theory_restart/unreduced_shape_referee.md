# Referee report on SHAPE and the unreduced lift

15 November 2026. Codex independent read of Claude231228 and the primary-source material. Coefficients are \(\mathbb F_2\). No knot search or geometric construction was performed.

## Verdict

**SHAPE remains an open assertion about actual tangles. The proposed unreduced-lift mechanism does not prove it and does not exclude the formal object \(B=a(0)\oplus S\oplus hS\).**

There is an explicit lift of every reduced formal Bar-Natan complex to the usual unreduced dotted Bar-Natan category. The reduced dot \(D\) lifts to the *difference of the two absolute dots* (their sum in characteristic two), not to the unmodified dot on one strand. Its product with a saddle remains zero. Thus the anticipated restoration of a nonzero \(DP\) product is not what unreduction does.

Moreover, \(B\)'s bullet part already has the proposed SHAPE: a point plus two squares. Each square is acyclic for either of its edge differentials, so the two one-dimensional collapse conditions also hold. These premises do not constrain the relative placement of the squares at the quantum extremes.

## 1. What the reduced dot actually denotes

In the ordinary dotted Bar-Natan theory over \(R=\mathbb F_2[H]\), let \(x\) denote a dot on the component adjacent to the distinguished endpoint, and \(y_i\) a dot on the other component of the crossingless object \(i\in\{b,c\}\). The relations are
\[
x^2=Hx,\qquad y_i^2=Hy_i.
\]
Dots slide on connected components. If \(S:i\to j\) is a saddle, its surface connects the two strands, so
\[
y_jS=xS,\qquad Sy_i=Sx.
\tag{1}
\]
Neck cutting gives, for the two consecutive saddles returning to \(i\),
\[
S^2_i=x+y_i+H.
\tag{2}
\]
Signs disappear over \(\mathbb F_2\).

Put
\[
D_i=x+y_i.
\tag{3}
\]
Then (1) implies
\[
D_jS=0,\qquad SD_i=0,
\tag{4}
\]
and (2) becomes
\[
H=D_i+S_i^2.
\tag{5}
\]
These are precisely the KWZ reduced quiver relations. They hold **before setting \(x=0\)**. Thus \(DS=0\) is not repaired merely by allowing the distinguished-component dot.

The difference is substantive: sending reduced \(D_i\) to the raw dot \(y_i\) would give \(y_jS=xS\), generally nonzero. That assignment is not a lift of the reduced algebra. Sending it to \(x+y_i\) is.

## 2. An algebraic section of reduction

Let \(\mathcal B\) be the reduced two-idempotent algebra, with central parameter \(H=D+S^2\), and set
\[
R'=\mathbb F_2[H,x]/(x^2+Hx).
\]
The two-object unreduced dotted algebra is obtained by
\[
\mathcal A\cong \mathcal B\otimes_{\mathbb F_2[H]}R',
\tag{6}
\]
with the identifications in (3). The inverse sends the physical second dot to
\[
y_i\longmapsto D_i+x.
\]
For example,
\[
(D_i+x)^2=D_i^2+x^2=HD_i+Hx=H(D_i+x);
\]
here \(D_i^2=HD_i\) follows from (5) and \(D_iS^2=0\).
The saddle relations and saddle-square relation are verified by (4)–(5). Hence the two presentations agree. Equivalently, neck cutting gives the expected normal forms: the endomorphism space of each crossingless matching has basis \(1,x,y_i,xy_i\) over \(R\), and the saddle space has basis \(S,xS\); replacing \(y_i\) by \(D_i+x\) is an invertible change of basis.

The reduction homomorphism sends \(x\) to zero. Its section sends \(D_i\) to (3) and preserves the saddles. Therefore any bounded graded complex over \(\mathcal B\) lifts by applying this section to every differential entry. Its squared differential remains zero, and setting \(x=0\) recovers the original complex. Gradings are preserved: \(x,y_i,D_i,H\) all have quantum degree \(-2\).

Since \(R'\) is free of rank two over \(R\), the corresponding scalar extension also preserves chain homotopies and direct sums. In particular the established null-homotopies of \(H\), \(D_b\), \(D_c\) and \(S^2\) on the short special lift as well.

**Consequence.** The formal \(B=a(0)\oplus S\oplus hS\) has an unreduced lift with a distinguished-dot action and the other strand's dot action satisfying the usual dotted relations. Requiring the existence of such a lift cannot distinguish \(B\) from an actual tangle complex.

This does not claim that the lifted formal complex is the cube of an actual tangle diagram. That much stronger realization condition remains precisely the issue.

## 3. This is consistent with the universal cobordism interpretation

The terminology “reduced” can hide a useful point. KWZ's 2019 construction first defines Bar-Natan's abstract undotted cobordism category with the sphere, torus and four-tube relations and **nonempty boundary**. It then introduces \(H\) using a handle on a distinguished component and introduces the relative dot using a tube to that component. The special-dot-zero identity is derived from this notation. Theorem 4.21 identifies the quiver algebra with the full endomorphism category of the two basic crossingless objects.

Thus a formal \(\mathcal B\)-complex already corresponds to a formal complex of universal cobordisms. It is not merely an object known to exist after forgetting an obstruction to those cobordisms. Applying an unreduced Frobenius functor is possible for such formal complexes; being the image of an actual *crossing cube* is additional information.

Sources inspected:

- [Kotelskiy–Watson–Zibrowius, arXiv:1910.14584v2](https://arxiv.org/abs/1910.14584v2), Section 4: definitions labelled def:Cobl and def:NotationDotsAndH, Proposition prop:CobRH, and Theorem 4.21. The locally archived primary TeX was read.
- [Kotelskiy–Watson–Zibrowius, arXiv:2602.23442](https://arxiv.org/abs/2602.23442), Section 2.1 and the quiver/cobordism identification; its \(G=-H\) convention agrees in characteristic two.
- [Bar-Natan, Khovanov's homology for tangles and cobordisms](https://arxiv.org/html/math/0410495v2), Sections 9 and 11.2, for dotted cobordisms and the distinction between abstract complexes and tangle cubes.
- [Khovanov, Link homology and Frobenius extensions](https://arxiv.org/html/math/0411447v2), for the rank-two Frobenius and base-change framework.

The presentation (6) is the direct calculation above, not a claim that these sources state the exact no-go conclusion in this wording.

## 4. Why the proposed square-completion analogy does not follow

The word
\[
P_n=S(DS^2)^{n-1}DS
\]
records a sequence of arrows through the other idempotent. Interpreted as an ordinary product in \(\mathcal B\), it is already zero because it contains \(DS\) or \(SD\). It is not an ordinary second polynomial variable that can simply be multiplied with \(D\). A derived quotient or a transferred higher operation may encode such runs, but its multiplication and higher structure must be specified and proved.

Likewise, the maps called \(d_D,d_P\) on the bullet generators are not supplied automatically by the augmentation functor: that functor kills the original \(D\)- and \(S\)-labelled maps. Extracting edge operators from a particular reduced curve normal form is a useful description of the observed shapes, but functoriality and the asserted universal relations are separate claims.

The comparison with a complex over \(\mathbb F[U,V]\), where an uncancelled \(UV\) term violates \(\partial^2=0\), would require an actual lift to that specific algebra together with an identification of \(U,V\) and the transferred differential. Adjoining the second dot as in (6) does not produce it.

## 5. SHAPE and both collapses permit the bad placement

In the \((h,q)\) coordinates of the letter let
\[
D=(1,2),\qquad P=(5,8).
\]
A square has vertices \(0,D,P,D+P\). The operator along its two \(D\)-edges is acyclic, and the operator along its two \(P\)-edges is acyclic. Therefore
\[
\text{point}\ \oplus\ \text{square}\ \oplus\ h\,\text{square}
\]
has one-dimensional homology under either operator. It is the bullet support of the formal countermodel, up to a global shift.

Its two squares have opposite Euler signs and identical quantum supports. The upper quantum extreme is occupied in adjacent homological degrees, so NP and END fail. Nevertheless its component shapes are exactly the allowed point/staircase and squares.

Consequently neither SHAPE nor SHAPE plus the two one-dimensional collapses controls the global outline. The unreduced lift from Section 2 does not change this conclusion.

A further standalone formal check, communicated by the root agent and checked here, is useful for the spectral-sequence analogy. On one square set
\[
\partial_4(D)=P,\qquad \partial_6(0)=D+P,
\]
with all other values zero. These have degrees \((4,6)\) and \((6,10)\), respectively, lower \(\delta=q/2-h\) by one, and their sum squares to zero. Filtering by \(h\) realizes successive fourth- and sixth-page cancellations, making the square acyclic. Applying this to both squares leaves the point. Thus merely postulating some filtered differential with the listed “Szabó-type” degrees also permits the bad object.

No compatibility between this artificial differential and \(d_D,d_P\), no actual geometric spectral sequence, and no actual tangle realization is asserted. Such additional compatibility could still contain information.

## 6. Remaining status and small corrections

- **Actual SHAPE law:** OPEN. This report neither proves it nor produces an actual tangle violating it.
- **Unreduced-lift existence as an obstruction to \(B\):** refuted over the stated coefficient field by the explicit lift.
- **SHAPE plus the two collapse ranks as a proof of NP:** refuted as an abstract algebraic implication by the same formal support.
- For \(D^a\) with \((h,q)=(1,2a)\), the change in \(\delta\) is \(a-1\), not zero unless \(a=1\). The recorded \(D^2\) exceptional arrow changes the diagonal grading by \(+1\).
- The statement that arbitrary Alexander-polynomial-one knots have knot Floer complexes of “point plus boxes” type is not supplied by the thin-knot structure theorem. Euler cancellation is automatic; that chain-level classification needs its own hypotheses.

What would revive the proposed route is a constraint on actual crossing cubes or on a specified compatible geometric structure that is stronger than the existence of the unreduced dot lift and the separate collapse maps. The missing condition must control the relative placement of the whole configuration, since the formal model already has the desired individual shapes.
