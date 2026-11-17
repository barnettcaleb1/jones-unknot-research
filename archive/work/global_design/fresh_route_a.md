# Primitive deformation gate: a genuine diagrammatic kernel already in degree four

2026-11-03. Bounded theory pass, with all expansions below by hand. No knot search, no automated expansion, no novelty claim.

## Candidate and verdict

A distinct proposed mechanism was to exploit the group-like property of the universal Kontsevich integral: perhaps compatibility with connected-sum composition and the actual Jacobi-diagram relations forbids a nontrivial deformation whose fundamental sl2 weight is trivial. This would be stronger than the polynomial constraints tested in `colored_propagation.md`.

The first lemma this mechanism would need is false. There is an explicit nonzero primitive element D in degree four of the genuine Jacobi-diagram Hopf algebra with

\[
W_N(D)=-44(N^2-1)(N^2-4)h^4.
\tag{1}
\]

In particular W_2(D)=0, while W_3(D)=-1760h^4. Therefore exp(D) is a nontrivial group-like diagram series with fundamental weight identically 1. This is a countermodel inside the diagram algebra, not merely an invented sequence of colored polynomials. It is NOT asserted to be the Kontsevich integral of a knot.

## Normalization and construction

Use the multiplicative Kontsevich normalization Z(U)=1 and Z(K#L)=Z(K)Z(L), with the connected-sum product of diagrams. Z(K) is group-like; thus log Z(K) is primitive, as is each homogeneous part. These conventions and properties are explicit in [Willerton, Sections 1 and 3](https://arxiv.org/pdf/math/9909151). Use zero framing and the sl2 weight normalized so that

\[
W_N(Z(K))=J_{K,N}(e^h),\qquad J_{U,N}=1,\quad J_{K,2}=V_K.
\]

Here W_N includes the h-degree bookkeeping, so a degree-four diagram maps to h^4 times its scalar weight. Let

\[
P_4(K)=(\log Z(K))_{\text{degree }4}.
\]

Let T be the trefoil with V_T(t)=t+t^3-t^4, let bar(T) be its mirror, and let F be the figure-eight knot. Define the ACTUAL element of the diagram algebra

\[
D=13\big(P_4(T)+P_4(\bar T)\big)-94P_4(F).
\tag{2}
\]

This definition uses existing knot integrals, their logarithms and homogeneous projection; consequently every STU/AS/IHX relation is already respected. D is primitive without any realizability assumption about (2) as a new knot.

## Exact hand calculation of its weight

Write p_K(N)=[h^4]log J_{K,N}(e^h). The sl2 Weyl symmetry N -> -N makes p_K even. The Melvin–Morton–Rozansky theorem bounds its degree by four and identifies its N^4 coefficient as [x^4](-log Delta_K(e^x)). Also p_K(1)=0. The diagonal statement passes to logarithms because taking the diagonal is multiplicative for series with no terms above the diagonal. See [Bar-Natan–Garoufalidis, Theorem 1](https://people.mpim-bonn.mpg.de/stavros/publications/printed/5papers.pdf).

The needed ordinary Jones expansions are

\[
V_T(e^h)=1-3h^2-6h^3-\frac{29}{4}h^4+O(h^5),
\qquad [h^4]\log V_T(e^h)=-\frac{47}{4};
\]

\[
V_F(e^h)=1+3h^2+\frac54h^4+O(h^6),
\qquad [h^4]\log V_F(e^h)=-\frac{13}{4}.
\]

Mirroring replaces h by -h and leaves the fourth-order coefficient unchanged. Therefore the fundamental weight of (2) is

\[
13\left(-\frac{47}{2}\right)-94\left(-\frac{13}{4}\right)=0.
\tag{3}
\]

The Alexander polynomials give

\[
\Delta_T(e^x)=e^x-1+e^{-x}=1+x^2+\frac{x^4}{12}+O(x^6),
\]
\[
[x^4](-\log\Delta_T(e^x))=\frac5{12};
\]

\[
\Delta_F(e^x)=3-e^x-e^{-x}=1-x^2-\frac{x^4}{12}+O(x^6),
\]
\[
[x^4](-\log\Delta_F(e^x))=\frac7{12}.
\]

Thus the N^4 coefficient of W_N(D)/h^4 is

\[
13\frac{10}{12}-94\frac7{12}=-44.
\tag{4}
\]

This even polynomial has degree at most four, vanishes at N=1 and N=2, and has leading coefficient -44. Hence it is exactly -44(N^2-1)(N^2-4), proving (1). Nonvanishing at N=3 certifies that D is nonzero in the diagram quotient itself.

## What group-likeness does not repair

Since D is primitive, G=exp(D) is group-like and satisfies

\[
W_2(G)=1,\qquad
W_N(G)=\exp\big(-44(N^2-1)(N^2-4)h^4\big).
\]

This is an exact identity in the degree/h-adic completion, not merely a finite-jet assertion. It defeats the implication “actual diagram relations plus group-likeness plus fundamental flatness force triviality or higher-color flatness.”

It does NOT certify the Laurent-polynomial, integral, Habiro, MMR/Alexander, or geometric realizability conditions for G. Indeed its diagonal is exp(-44x^4), which would require an Alexander polynomial with Taylor expansion exp(44x^4), not a Laurent polynomial. This particular G is therefore excluded by full Alexander realizability. The earlier `colored_propagation.md` countermodel passed those polynomial/rationality constraints but did not supply a group-like diagram lift; the present example supplies such a lift but fails that separate condition. The two countermodels must not be combined into an unproved joint countermodel.

## Decision

No viable new full proof route was obtained. A deformation argument would need a geometric/integrality constraint on the IMAGE of actual knots inside the group-like completion, not the Hopf-algebra axioms alone. Constructing that constraint could be substantive, but neither “primitive,” “group-like,” nor “universal” provides it. No further computation is recommended from this note.

**Subsequent extension, 2026-11-03 12:33 (Q-JOINT).** The joint compatibility question is now settled by a DIFFERENT lift: `joint_primitive_gate.md` constructs a rational group-like series with the exact integral Habiro/MMR-compatible colored sequence of `colored_propagation.md`. Its first primitive term is -mathsf-t² D/176 in degree6, followed by a triangular all-order correction. The present exp(D) still fails Alexander realizability; its failure is not being erased or attributed to the new series. Graph-level rationality and actual knot realization remain unproved.
