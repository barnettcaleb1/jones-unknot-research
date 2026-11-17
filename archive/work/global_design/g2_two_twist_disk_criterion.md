# A disk criterion and unlink detection on two-twist orbits

2026-11-03. Node G2-ORBIT; constructive refinement of G2-DEEP.

Status: TRUSTED written deduction from G2-PAIR/G2-PAIR-COMM and the exact cap-module formulas, with independent internal checks. Main collaborator read and novelty assessment pending. No numerical search is used.

## 1. Statement with a geometric seed condition

Let S be a trivial three-strand tangle, V_S its genus-two double branched cover, and a a reducing 3|3 curve on its boundary sphere. Thus a bounds a disk meeting S once; its lift bounds a separating disk in V_S. Write T_a for the upstairs separating twist, represented downstairs by the square of the full twist about a.

Choose a second 3|3 curve d with
\[
H(S,v_d)\ne0.
\tag{1}
\]
Here H is the generic invariant Hermitian form on W(6,0), and v_d spans the spin-3/2 line associated to d.

There is a purely topological sufficient condition for (1). Let L_S be the meridian Lagrangian in H_1(boundary V_S;Q), and let P_d^hom be either symplectic plane of d's lifted homological splitting. Then
\[
L_S\cap P_d^{hom}=0
\tag{2}
\]
implies (1). Indeed, the regular endpoint curve-cap pairing is a nonzero constant times the determinant of a basis of P_d^hom and a basis of L_S. This is the lane's curve-cap shadow formula. Condition (2) says d is not even homologically reducing.

Put G=<T_a,T_d>. The hypotheses imply that the seed spin lines differ, so G2-PAIR makes G a free group on these two twists and its projective Jones action is faithful.

**Theorem 1 (disk criterion on the orbit).** For every f in G,
\[
H(S,v_{f(a)})=0
\quad\Longleftrightarrow\quad
f\in\langle T_a\rangle
\quad\Longleftrightarrow\quad
f(a)=a
\quad\Longleftrightarrow\quad
f(a)\text{ is reducing for }S.
\tag{3}
\]
Equality of curves means isotopy class. In particular G2-TWIST is true on this entire orbit, including its curves with a's unchanged homological splitting.

**Theorem 2 (cap and handlebody stabilizers).** Within G,
\[
\operatorname{Stab}_G([S])
=G\cap\operatorname{HandlebodyGroup}(V_S)
=\langle T_a\rangle.
\tag{4}
\]
For the tangle version, use the equivariant boundary action and its Hilden subgroup.

**Corollary 3 (Jones detects the unlink in these plat families).** Let L_f be the three-bridge plat obtained by using S as both the upper and lower cap system and a pure braid lift of f in G between them. Then
\[
V(L_f)\doteq V(U_3)
\quad\Longleftrightarrow\quad
f\in\langle T_a\rangle
\quad\Longleftrightarrow\quad
L_f=U_3.
\tag{5}
\]
The symbol \(\doteq\) allows a Jones framing/orientation monomial unit; exact equality is included. These pure lifts give three components. This is a class of links, not a proof of unknot detection.

## 2. From one zero coefficient to a line stabilizer

Let P,Q be the projectors onto the spin lines of a,d, respectively. The two-plane
\[
U=\operatorname{span}(v_a,v_d)
\]
is nondegenerate by G2-PAIR. The functional l=H(S,.) vanishes at v_a because a is reducing, and is nonzero at v_d by (1). Consequently
\[
\ker(l|_U)=K v_a.
\tag{6}
\]
Every element of G preserves U. Choose the representative v_{f(a)}=rho(f)v_a; changing it by a nonzero scalar does not change the zero condition. By (6), its zero pairing is equivalent to rho(f) preserving K v_a.

The raw TL braid operators preserve H. An H-isometry preserving a nonisotropic line also preserves its orthogonal complement, hence commutes with the orthogonal projector onto that line and with its twist operator. Thus a zero pairing gives
\[
[\rho(f),\rho(T_a)]=I.
\]
The faithful projective action of the free group G gives [f,T_a]=1. The centralizer of a free generator in a free group is precisely its cyclic subgroup, so f belongs to <T_a>.

Conversely a power of T_a fixes a. The curve a is reducing. Finally every reducing curve has zero pairing, by the easy Jones-Wenzl cap relation. These implications prove all of (3).

Only the initial reducing curve and one nonzero seed pairing are used. If d is also geometrically reducing instead, both twists extend over V_S, so every curve in this orbit is reducing and has zero pairing. This complementary observation does NOT resolve the case of a nonreducing d whose pairing is zero: that is precisely a counterexample to the general target.

## 3. Rational-line stabilizers and the cap vector

The proof of G2-PAIR-COMM establishes a fact about all rational lines, not just spin lines:

> Every nonidentity element of [G,G] has all of its Q(A)-rational invariant lines in U-perp.

The reason is that its rational eigenvalues are Laurent units, the second-order identity at zeta forces them to equal1, and eigenvalue1 is absent on U. Over an algebraic closure there ARE eigenlines on U; the rationality qualification is essential.

It follows that the stabilizer in G of any rational projective line outside U-perp is cyclic. Otherwise two noncommuting stabilizers would have a nonidentity commutator fixing that same line. This contradicts the displayed fact. The stabilizer is therefore abelian, and abelian subgroups of a free group are cyclic.

In the present setting S is outside U-perp because H(S,v_d) is nonzero. Its projective stabilizer contains T_a, since a is reducing. More directly, if f stabilizes [S], then [T_a,f] also does; the rational-line fact forces this commutator to be the identity, whence f lies in <T_a>. This proves the first equality in (4).

Every boundary mapping class extending over the marked handlebody/tangle preserves its vacuum cap line. Conversely every power of T_a extends by twisting the reducing disk. The resulting inclusions give the second equality in (4). No converse to the general cap-stabilizer problem has been assumed.

## 4. The link conclusion

For a cap vector S, H(S,S)=delta^3, where delta=-A^2-A^-2. On a unit-circle arc near A=1, the cap Gram form is definite (negative definite before multiplying by -1) and braid operators are unitary. The plat bracket is H(S,rho(f)S).

If the normalized Jones polynomial has the unlink value up to a monomial unit, then throughout that arc
\[
|H(S,\rho(f)S)|=|\delta|^3
=\|S\|\,\|\rho(f)S\|.
\]
Equality in Cauchy-Schwarz gives rho(f)S proportional to S at every regular point of the arc. Its rational two-by-two coordinate minors therefore vanish identically, so f stabilizes [S] over Q(A). Theorem 2 gives f in <T_a>, whose plat is actually U_3.

Conversely powers of T_a extend over the tangle and give U_3. An actual U_3 of course has its Jones polynomial. This proves (5), without invoking uniqueness of a bridge sphere of the unlink.

## 5. A canonical explicit family with every finite vanishing order

Use the standard cap basis from g2_two_twist_freeness.md. Take
\[
a=\partial\{1,2,3\},\qquad
S=D_4=(16)(23)(45),\qquad
d=\sigma_3(a).
\]
The seed a is reducing. With v_a the standard Jones-Wenzl rainbow and Delta_3=delta^3-2delta, the local identity e_3D_4=D_5 and rainbow duality give
\[
H(S,v_a)=0,\qquad
H(S,v_d)=A^{-1}\Delta_3.
\tag{7}
\]
Thus (1) holds, and after dividing out the universal Gram zero delta,
\[
\widehat H(S,v_d)(\zeta)=-2\zeta^{-1}\ne0,
\qquad \zeta=e^{i\pi/4}.
\]
The seed also meets the topological condition (2): d partitions the endpoints into {1,2,4} and {3,5,6}, so each cap of S crosses that partition; equivalently the determinant in the curve-cap shadow is nonzero by (7).

Define explicit words
\[
f_1=T_d,\qquad
f_{r+1}=[T_a,f_r],
\quad [x,y]=xyx^{-1}y^{-1}.
\tag{8}
\]
In braid words one may take T_a=(sigma_1 sigma_2)^6 and T_d=sigma_3 T_a sigma_3^-1.

**Theorem 4 (exact order).** The coefficients
\[
F_r(A)=\widehat H(S,\rho(f_r)v_a)
\]
are nonzero and satisfy
\[
\operatorname{ord}_\zeta F_r=r
\quad\text{for every }r\ge1.
\tag{9}
\]
The curves f_r(a) are nonreducing, all have a's integral homological splitting, and f_r belongs to gamma_r(I_2).

**Proof.** Put h=(A-zeta)/zeta and write P_0=P(zeta), Q_0=Q(zeta). The projectors are regular at zeta. The raw squared-twist formula gives
\[
-\rho(T_i)=I+hB_i+O(h^2),
\quad B_a=24P_0-12I,\quad B_d=24Q_0-12I.
\tag{10}
\]
Projector derivatives cancel at first order because the two raw eigenvalues coincide at zeta. For r>=2, ordinary commutator expansion yields
\[
\rho(f_r)=I+h^r\operatorname{ad}_{B_a}^{\,r-1}(B_d)+O(h^{r+1}).
\tag{11}
\]
Let l_0=\widehat H(S,.)|_zeta and v_0=v_a(zeta). We have l_0P_0=0 and P_0v_0=v_0. For every matrix X,
\[
l_0[B_a,X]v_0=-24\,l_0Xv_0.
\tag{12}
\]
Moreover
\[
C:=l_0Q_0v_0\ne0.
\]
Indeed Q_0v_0 is a nonzero multiple of v_d(zeta) by G2-ORTH, and (7) gives nonzero pairing with that vector. For r>=2, equations (11)-(12) therefore give
\[
F_r(A)=24(-24)^{r-1}C\,h^r+O(h^{r+1}),
\tag{13}
\]
whose leading coefficient is nonzero. For r=1 the raw scalar minus gives F_1=-24C h+O(h^2). Variations of the covector and v_a cannot alter these leading terms: their unperturbed pairing is identically zero, and rho(f_r)-I starts in order r. This proves (9).

The free-group recurrence gives f_r outside <T_a>: f_1 is the other generator; thereafter a commutator with T_a could be trivial only if the previous word centralizes T_a, and a nontrivial commutator cannot be a nonzero power of T_a by abelianization. Theorem 1 proves nonreducibility. All generators are upstairs separating twists, hence lie in I_2, and (8) gives the stated lower-central depth. QED.

This replaces the density-based existence argument by an explicit family with EXACT, rather than merely unbounded, finite orders. It is not evidence for a kernel: every coefficient is proved nonzero.

## 6. The remaining global gap

The mechanism is the conjunction of a two-dimensional span, a one-dimensional kernel of the cap functional on that span, and the cyclic centralizer of a free generator. With three independent spin lines, that functional already has a two-dimensional kernel on their span. Its vanishing no longer forces preservation of a particular line. We have no replacement for that step.

Nor is there a topological normal form placing every homologically reducing curve into these certified orbits with a known reducing anchor and a known nonzero transverse seed. After leaving the disk set, the resulting curve cannot simply be used as the reducing anchor for the next induction step.

Thus this is a proved orbit-class version of G2-TWIST and of three-component unlink detection, not the general disk criterion, full W(5,1) faithfulness, or Jones unknot detection.

The component hypothesis matters in the link argument: the three-component unlink in three-bridge position saturates the definite-form bound. An unknot in three-bridge position has bracket magnitude only |delta|, below that bound |delta|^3, so its Jones equality does not give the same cap-line preservation. No Euler-characteristic-to-homology-rank claim is imported.

## 7. Evidence

- G2-PAIR and G2-PAIR-COMM: complete proofs in g2_two_twist_freeness.md, independently read by Claude154307.
- Exact cap, projector, and endpoint formulas: the coordinated lane's read-model/model.md and build-kernel/kernel.md; the definite-arc argument is written out above and in build-heegaard/heegaard.md.
- An independent internal reader checked the seeded orbit theorem, rational-line and handlebody stabilizers, and the canonical exact-order expansion. No enumeration was performed.
