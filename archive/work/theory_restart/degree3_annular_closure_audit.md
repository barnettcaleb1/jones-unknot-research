# Bounded audit: annular closure and the theta projector

16 November 2026. Scope: the annular/topological part of the proposed comparison modulo \(\Phi _5(Q)\), \(Q=-t^{-1}\). No new evaluation search was performed. The folded ribbon normalization is assigned separately.

## Result

The annular and theta closure steps have a coherent proof. They do not require the quotient theta curve to be a necklace or a rational box. The key is to use the **scalar by which a closed annular diagram acts on the simple axis color**, rather than asserting multiplicativity of ordinary link polynomials.

The resulting conditional statement is: if the two framed theories have equal bulk Dubrovnik parameters modulo \(\Phi _5(Q)\), the stated mixed-power eigenvalues and reduced weights, and coherently normalized vertex projectors, then their reduced evaluation on every marked theta diagram agrees modulo \(\Phi _5(Q)\). Passing from those framed evaluations to preferred \(J\) and \(V_K(t^2)\) still requires the separate framing check.

## 1. Arbitrary theta diagrams reduce to closed annular diagrams

The quotient theta graph has an unknotted axis cycle of color 1 and an arc of color 2 joining its two vertices. Take a regular-neighborhood ball of one complete color-1 edge, including its two endpoint vertices and only short initial segments of the other incident edges. Its boundary meets the graph at four points with colors \(1,2,1,2\). The regular neighborhood of this edge is a ball regardless of its apparent diagram complexity.

With the bending and boundary marking fixed, the inside tangle is the channel projector

\[
P_1=i p,\qquad p i=\mathrm{Id}_{V_1}.
\]

The complement is an arbitrary colored tangle \(A\) on \(V_1\otimes V_2\). Cyclicity of the generic pivotal trace gives

\[
\operatorname{tr}_{V_1}(pAi)
=\operatorname{tr}_{V_1\otimes V_2}(AP_1).
\]

Both expressions are reduced by the same axis normalization. This is initially an identity away from vanishing quantum dimensions; it is then used as an identity of the regular scalar functions furnished by the integral model. Division by the specialized quantum dimension at the root is not part of the argument.

For the proposed original mixed eigenvalues \(Q^2,-Q^{-1}\),

\[
P_1=\frac{T+Q^{-1}}{Q^2+Q^{-1}}.
\]

Substitution expresses the theta value as a linear combination of two actual closed colored links. In each link the color-1 component is still an unknot. The identity term reconnects the original axis edge; the \(T\) term inserts a local full twist between this edge and the color-2 edge, which does not knot the color-1 component considered alone. Hence both terms are legitimate diagrams in the complement of an unknot axis, i.e. annular skein elements.

The denominator is harmless near \(Q=1\) modulo 5 (its value is 2), and also in the cyclotomic integer quotient: \(Q^2+Q^{-1}=Q^{-1}(Q^3+1)\), and \(1+\zeta_5^3\) is a cyclotomic unit. The folded projector has denominator \(Q^{-3}+Q^{-1}\); these denominators and the projector formulas agree modulo \(\Phi_5\).

## 2. The correct multiplicativity statement

On the original side a closed annular diagram acts on a straight color-1 axis as a scalar endomorphism. Write this endomorphism as \(z(A)\). The annular skein product corresponds to nesting annular operators and therefore

\[
z(AB)=z(A)z(B).
\]

Generically the axis representation is simple, so \(z(A)=L(A)\mathrm{Id}\), and

\[
L(AB)=L(A)L(B).
\]

This scalar identity extends to the integral local model when its evaluations are regular. It is emphatically not a claim that an arbitrary unpointed link evaluation is multiplicative. No division by the vanishing axis dimension is required after extension.

The folded axis is a branch defect, so Schur's lemma for the original color-1 representation must not simply be imported for that side. There is a direct topological verification on the required basis monomials. The product \(A_{n_1}\cdots A_{n_k}\) is represented as the annular closure of a braid with disjoint consecutive blocks

\[
\beta=\beta_1\cdots\beta_k,\qquad
\beta_i=\sigma_1\cdots\sigma_{n_i-1}
\]

(with strand indices shifted for the successive blocks). Its two-fold lift branched over the braid axis is the closure of \(\beta^2\). The disjoint blocks stay disjoint, so that closure is the split union of the closures of \(\beta_i^2\). The absolute framed Jones evaluation therefore factors, with the individual framing corrections retained. A contractible circle away from the axis lifts to two split contractible circles and supplies \(d_+\). Thus the folded values on all basis monomials are the products of the stated generator values without any irreducibility assumption about the branch defect.

Consequently equality on the positive-winding annular generators, together with equality of the contractible loop value and bulk skein parameters, extends to all annular skein elements. Only integral generation by the positive cycle closures is needed; one need not invert quantum integers or use a semisimple idempotent basis. A crossing-change/descending-diagram proof of generation uses skein relations and framing units, rather than division by the crossing parameter.

## 3. Generator topology and framing

Let \(U_n\cup C_n\) be the standard two-component link \(T(2,2n)\), with \(U_n\) designated the axis. Its two components are annular parallels. On the boundary of the axis exterior the second component has slope

\[
\lambda_{U_n}+n\mu_{U_n}.
\]

In the solid-torus coordinates of that exterior this is the \((n,1)\) torus curve. It is therefore the positive cycle-braid annular generator \(A_n\). The mixed-link presentation gives the moving component zero blackboard self-framing; the standard cycle braid has \(n-1\) positive self-crossings. Thus its annular framed value differs by the moving-color twist \(r^{n-1}\), with the sign fixed by the common positive-crossing convention.

For \(r_-=Q^{-2}\) and \(r_+=Q^3\), the quotient of these framing factors is \(Q^{5(n-1)}\), so it is 1 modulo \(\Phi_5(Q)\).

The proposed reduced mixed-power evaluations are

\[
L_n^-=Q^{2n}-(Q+Q^{-1})(-Q^{-1})^n,
\]
\[
L_n^+=Q^{-3n}+(Q^2+1+Q^{-2})(-Q^{-1})^n.
\]

They agree modulo \(\Phi_5(Q)\) for every integer \(n\): use \(Q^5=1\) and \(Q^2+Q+1+Q^{-1}+Q^{-2}=0\). The same last identity gives equality of the two contractible loop values. Thus the generator trace comparison, with the ribbon correction retained, is exactly the comparison needed in Section 2.

## 4. Remaining scope

No annular-topological obstruction was found. The argument becomes a full preferred-polynomial congruence only after verifying that the folded ribbon evaluation is the ordinary covering-knot Jones evaluation at \(t^2\), and that the preferred normalization on the original theta side introduces the same residual unit modulo \(\Phi_5\). That check cannot be replaced by agreement on a few named knots. Likewise the bulk parameter agreement must refer to the actual chosen ribbon operators, not just their eigenvalue sets.

## 5. Hostile reread of the completed comparison

The subsequently supplied `degree3_cyclotomic_comparison.md`, Sections 2, 3 and 5, survives this audit. The delicate topology has no restriction to unknotted-looking axis edges: a regular neighborhood of the selected edge together with the short vertex stubs is a regular neighborhood of a tree, hence a ball. Its boundary marking is inherited from the actual embedding. Straightening that marked neighborhood puts all outside complexity into \(A\); it does not assert that the edge was trivial relative to some previously prescribed ball.

In the identity resolution the axis is the original unknot. In the mixed-twist resolution, deleting the color-2 strand makes the remaining color-1 local braid strand isotopic relative to its endpoints to the original strand. Thus that resolution also has an unknotted axis. The two ordinary annular evaluations are consequently applicable exactly where the proof uses them.

The covering projector is the cup-cap normalized by the fundamental unknot value; taking its trace produces the covering-knot evaluation divided by precisely that value. The normalization \(pi=\mathrm{Id}\) fixes the bending scalar, so no independently chosen closure normalization has entered. With the separately supplied local lift identity \(T_{\rm fold}=\theta_U^{-1}B\), the completed proof supplies the framing input left open in Section 4 above.

Verdict on the assigned closure portion: **accepted**. The annular closure argument is complete, rather than merely an agreement on examples or on principal symbols. This audit does not claim a second independent computation of every quantum-group matrix or a literature priority check.
