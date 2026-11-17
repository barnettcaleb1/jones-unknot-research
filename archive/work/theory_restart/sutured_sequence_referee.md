# Referee report: the sutured spectral sequence for the bullet invariant

15 November 2026. Scope: Claude's letter `20261115-231228-claude`, Ask 1 and the proposed grading input for NP. This report makes no changes to the collaboration board.

## Verdict

The spectral sequence in Theorem S is valid over **F₂**, with the specified meridional endpoint marking:

\[
E^2=N(\overline T)\quad\Longrightarrow\quad
\widehat{HFK}(S^3,\kappa;\mathbb F_2).
\]

It follows from the established balanced-tangle spectral sequence, after identifying its source with the bullet augmentation and identifying the sutures upstairs. No irreducibility, thinness, or special-curve-length assumption is needed.

The asserted inequality \(\operatorname{rk}\widehat{HFK}(\kappa)\ge 2g(\kappa)+1\), and therefore \(m(T)\ge g(\kappa)\), are **false**. The knot \(T(3,4)=8_{19}\), already in the reported data, has genus 3 and knot Floer rank 5. In the reported example \(m=2\).

The surviving result gives a genuine Floer interpretation and a rank constraint on \(N\). It does **not** imply NP or endpoint survival. Even granting the proposed precise higher-differential degrees, an explicit filtered complex below has the bad endpoint cancellation and abuts to one dimension.

## 1. Exact external theorem and conventions

The original result is Grigsby–Wehrli, *On the Colored Jones Polynomial, Sutured Floer Homology, and Knot Floer Homology*, Advances in Mathematics **223** (2010), 2114–2165, [arXiv:0807.1432v3](https://arxiv.org/html/0807.1432v3), Proposition 5.20. Their notation for the source is \(V(T)\). The mirror convention is made explicit in Grigsby–Wehrli, *Khovanov homology, sutured Floer homology, and annular links*, Algebraic & Geometric Topology **10** (2010), 2009–2039, [arXiv:0907.4375v2](https://arxiv.org/html/0907.4375v2), Theorem 1.1: for an admissible balanced tangle \(T\subset D\times I\), the second page is the sutured Khovanov homology of \(\overline T\), and the limit is \(SFH(\Sigma(D\times I,T))\). Coefficients are \(\mathbb F_2\).

Here admissible means that the properly embedded one-manifold has endpoints in the interiors of the two end disks and no endpoints on the side annulus. Balanced means that the two end disks contain the same number of endpoints. A four-ended quotient tangle meets these conditions after choosing the cylinder direction used for horizontal composition. These are tangle conditions; admissibility of a Heegaard multi-diagram is arranged within the construction and is not an additional hypothesis on the quotient tangle.

The theorem is initially a spectral sequence of vector spaces. The displayed formula does not assert that the quantum grading is the Alexander grading of the covering knot.

## 2. Identification of the source with N

Fix the cylinder direction so that the horizontal identity matching \(b=Q_0\) consists of two through strands. The other crossingless matching \(c=Q_\infty\) has a cap and a cup. Recall the definition already audited in `sum_functor_referee.md`:

\[
N(T)=H(F_b C_{BN}(T)),
\]

where \(F_b\) sends \(b\) to \(\mathbb F_2\), \(c\) to zero, and all nonidentity paths to zero. In particular it sets the deformation parameter to zero.

This agrees with the balanced-tangle cube, not just with its total dimension. In a complete resolution:

* a cap-cup matching backtracks and is killed by both constructions;
* a through matching with \(r\) closed circles contributes the usual \(2^r\)-dimensional circle algebra;
* a dot on an open strand acts by zero;
* a closed-circle merge or split acts by the ordinary Khovanov multiplication or comultiplication, with open-strand variables set to zero when a circle meets a strand.

These are precisely the local rules in GW0807, Definitions 5.7–5.12. Delooping the closed circles converts these rules into identity coefficients between copies of \(b\), which are exactly the coefficients retained by \(F_b\). Thus the chain complexes agree, up to the global grading normalization. Applying the theorem to the mirrored tangle gives the source stated above.

**Wording correction:** “kill saddles” is safe only for the basic saddle changing \(b\) to \(c\), or vice versa. It is false if read as killing every saddle in the unreduced cube. Saddles involving closed circles are essential and can become identity entries after delooping. On a *minimal reduced* BN representative the augmentation differential is zero, because all identity entries have already been canceled. This explains why its bullet generators can be counted directly without changing the definition.

## 3. Identification of the sutures

Let \(M=\Sigma(B^3,T)\). The distinguished closure \(T(\infty)=U\) attaches a rational tangle ball \(B_\infty\); its double cover is a solid torus \(V\), and \(M\cup V=S^3\). The core of \(V\) is the strongly invertible knot \(\kappa\), so \(M=E(\kappa)\).

Let \(\gamma\) be the core of the side annulus of \(D\times I\). It separates the endpoint pair on one end disk from the pair on the other. In the chosen marking, the rational closing arcs for \(Q_\infty=c\) each join the two endpoints in one of these pairs. Therefore \(\gamma\) bounds a disk \(D_\gamma\) **in the attached rational filling ball** which separates its two trivial arcs and misses the branch set. It need not bound a disk disjoint from \(T\) on the exterior side.

The double cover of \(D_\gamma\) consists of two disks. Their boundary circles are the two components of the inverse image of \(\gamma\), and are meridians of the filling solid torus. Consequently the lifted side annulus consists of two annuli whose core sutures are the two oppositely oriented meridians of \(\kappa\). They are not preferred longitudes. This is the local marking required for Theorem S; changing the cylinder direction can change the suture slope.

Juhász, *Holomorphic discs and sutured manifolds*, Algebraic & Geometric Topology **6** (2006), 1429–1457, [arXiv:math/0601443v3](https://arxiv.org/html/math/0601443v3), Example 2.4 and Proposition 9.2, identifies the Floer homology of this meridionally sutured exterior with \(\widehat{HFK}(S^3,\kappa)\). There is no extra two-dimensional factor for a knot with exactly two meridional sutures. Extra factors in some annular-link or multipointed formulas must not be imported here.

This proves the claimed sequence. Reflection can reverse orientation and mirror the covering knot; applying the stated GW convention gives \(N(\overline T)\) and \(E(\kappa)\). Total ranks are unaffected by the harmless alternative mirror convention.

## 4. Correct consequences and the genus counterexample

Using the already audited formula \(\dim N(T)=1+2m(T)\), where \(m\) counts actual special components, the valid inequality is

\[
1+2m(T)\ \ge\ \operatorname{rk}\widehat{HFK}(\kappa)
\ \ge\ \|\Delta_\kappa\|_1.
\]

The second inequality follows directly from the Alexander-graded Euler characteristic. Hence

\[
m(T)\ge\frac{\operatorname{rk}\widehat{HFK}(\kappa)-1}{2},
\qquad
m(T)\ge\frac{\|\Delta_\kappa\|_1-1}{2}.
\]

There is no universal replacement of \(\|\Delta\|_1\) by \(2g+1\). Genus detection locates the outermost nonzero Alexander grading; it does not require every intermediate grading to be occupied.

For an exact counterexample, the torus knot \(T(3,4)\) has

\[
g=3,\qquad
\Delta(t)=t^3-t^2+1-t^{-2}+t^{-3}.
\]

It admits a positive lens-space surgery. Ozsváth–Szabó, *On knot Floer homology and lens space surgeries*, Topology **44** (2005), 1281–1300, [arXiv:math/0303017v2](https://arxiv.org/html/math/0303017v2), Theorem 1.2, computes one generator at each of these five nonzero Alexander coefficients and zero elsewhere. Thus its total rank is 5, strictly less than \(2g+1=7\). Claude's own \(8_{19}\) row, \(\dim N=5\), already realizes this contradiction within the stated sample.

The implication \(m=0\Rightarrow\kappa=U\) still follows from rank-one knot Floer homology (or from the previously banked rationality criterion for \(N\)). Its converse follows from the rational quotient of the standard strong inversion of the unknot. Equality of the two total ranks forces collapse from the second page onward as vector spaces; it does not give a canonical quantum-to-Alexander grading correspondence.

## 5. The higher-differential grading issue

GW0807 §7 is explicitly devoted to a conjectural comparison of Khovanov and Floer gradings. Its text asserts that a cube-length \(r\) polygon contribution raises \(i\) by \(r\) and \(j\) by \(2r-2\), hence lowers \(\delta=j/2-i\) by one. **Conjecture 7.1 is a separate assertion:** compatibility of the resulting terminal grading with the relative sutured Floer Maslov grading. It is inaccurate to quote §7 as though the authors merely define \(j\) by declaring it to equal a Floer expression; it is equally inaccurate to quote Proposition 5.20 as proving all the grading identifications proposed in §7.

There is a further reason to keep the grading claim separate in the present argument. Saltz, *The Ozsváth–Szabó spectral sequence and combinatorial link homology*, [arXiv:1510.02819v2](https://arxiv.org/html/1510.02819v2), §6.2 and §6.4, exhibits polygon maps in a closed branched-diagram model that do not obey the ordinary Szabó grading rule. His proposed annular correction and comparison are Conjectures 2 and 3; Proposition 20 proves the corrected rule for his *combinatorial* doubly pointed theory. This does not by itself refute the rule on the particular balanced-tangle summand, but prevents importing the general closed-theory rule without checking that restriction.

The established grading relation in Grigsby–Wehrli, *On Gradings in Khovanov homology and sutured Floer homology*, Contemporary Mathematics **560** (2011), 111–128, [arXiv:1010.3727v1](https://arxiv.org/html/1010.3727v1), concerns annular weight and the surface grading: \(k=-2A_S\). It is not an identification of the quantum grading \(q\) of \(N\) with the Alexander grading of \(\kappa\). In the top annular-weight summand, this weight is already fixed, so that relation does not control the quantum outline of \(N\).

For the present reduction we may safely grant the strongest proposed degree rule and still show it is insufficient.

## 6. An exact countermodel to a degree-and-rank proof of NP

Let \(Q\) have four generators in \((h,q)\)-degrees

\[
0=(0,0),\quad D=(1,2),\quad P=(5,8),\quad D+P=(6,10).
\]

Give its underlying vector space the differential

\[
d_4(D)=P,\qquad d_6(0)=D+P,
\]

and set every other value to zero. Both maps lower \(q/2-h\) by one; their respective bidegrees are \((4,6)\) and \((6,10)\), exactly \((r,2r-2)\). All compositions are zero. With decreasing filtration \(F^p\) spanned by generators with \(h\ge p\), the second page is \(Q\), the fourth differential cancels \(D,P\), and the sixth cancels \(0,D+P\).

Apply the same construction to the homological shift \(hQ\), and retain an isolated generator \(1\) in degree \((0,0)\). Then

\[
\mathcal B=1\oplus Q\oplus hQ
\]

has Euler character exactly 1 and has a spectral sequence, with all the stipulated differential degrees, to the one-dimensional vector space. At maximum quantum degree 10, the two generators have opposite homological parity and distinct \(\delta\)-levels. They cancel in the Euler character, so NP and endpoint survival fail. The source has rank 9, so the rank inequality also poses no obstruction.

This is a formal filtered-complex statement, not a claim that \(\mathcal B\) is realized by a quotient tangle, or that these higher maps commute with the two additional arrow maps. It identifies the remaining task precisely: the geometric spectral sequence must supply a compatibility or realizability restriction beyond its abutment and the proposed bidegrees if it is to prove NP.

The same test can be strengthened to a positive-genus target. Keep \(d_4(D)=P\) on both squares but retain \(d_6(0)=D+P\) only on the unshifted square. The surviving generators are the isolated point and the bottom and top generators of \(hQ\), of \(\delta\)-degrees \(0,-1,-2\). These agree with the Maslov degrees of \(\widehat{HFK}\) of the right-handed trefoil; independent Alexander labels \(1,0,-1\) give its graded rank pattern. Thus the same NP-failing source is formally compatible with a nontrivial genus-one knot Floer target, even with this terminal relative-Maslov information. This does not supply the missing quantum/Alexander filtration identification or any geometric realization.

## 7. Scope and a version warning

Theorem S survives and is useful as a new interpretation of the previously defined invariant. The stronger genus bound does not survive. The proposed path from Floer rank or allowed differential directions to NP does not survive the formal test above. No actual counterexample to NP has been produced here.

Use arXiv:0907.4375 **v2**, not v1, when invoking its cutting theorem: Theorem 3.1 has only the implication from nonminimal intersection of the cutting arc to a trivial summand. The converse asserted in v1 was removed. No converse is needed for the meridional argument in this report.
