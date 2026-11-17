# Joint primitive/Habiro compatibility: an all-order rational diagram lift

2026-11-03. Theory only; no basis enumeration or automated expansion. The all-order construction was proposed by the root agent and independently checked here.

**Result.** The formal Habiro sequence from `colored_propagation.md` admits a group-like lift in the genuine rational Jacobi-diagram completion. Thus its formal polynomial constraints and the actual diagram relations/group-likeness can be satisfied simultaneously. This is NOT realization by a classical knot.

## 1. Vogel insertion and exact normalization

Write \(\mathsf t\) for Vogel's degree-one insertion, reserving q for the Jones variable. It acts on primitive Jacobi diagrams by replacing an internal trivalent vertex; the action is independent of that vertex and preserves the primitive subspace. This action on the unframed primitive space is stated in [Willerton, Section 6](https://arxiv.org/pdf/math/9909151). Degree at least two primitives have connected representatives with internal trivalent vertices, so it applies to every primitive used below.

[Vogel, Theorems 6.1 and 7.2](https://webusers.imj-prg.fr/~pierre.vogel/diagrams.pdf) gives

\[
\Phi_L(\alpha D)=\chi_L(\alpha)\Phi_L(D),
\]

independently of the representation coloring the Wilson loop. For sl(E) with the form Tr_E(xy), Theorem 7.2 sends \(\mathsf t\) to dim(E). Therefore, for sl2 with the trace form in its defining two-dimensional representation, \(\chi_{sl_2}(\mathsf t)=2\). This is the trace-form convention used in the MMR normalization of `fresh_route_a.md`.

Including the grading parameter h, the precise rule is

\[
W_N(\mathsf t D)=2h\,W_N(D).
\tag{1}
\]

In particular, if D4 is the degree-four primitive of that note, with

\[
W_N(D4)=-44(N^2-1)(N^2-4)h^4,
\]

then

\[
\boxed{D6=-\frac1{176}\mathsf t^2D4},\qquad
W_N(D6)=(N^2-1)(N^2-4)h^6.
\tag{2}
\]

This answers the initial question affirmatively with the exact factor. The nonzero N=3 weight proves D6 is nonzero, without any assumption that Vogel insertion is globally injective.

## 2. A triangular family of primitive weights in every degree

Fix the multiplicative rational Kontsevich normalization Z(U)=1, and reduced colored Jones normalization J_{U,N}=1, q=e^h. For a trefoil T define

\[
P_{2m}=(\log Z(T))_{2m},\qquad
W_N(P_{2m})=p_{2m}(N)h^{2m}.
\]

Each P_{2m} is primitive. Weyl symmetry makes p_{2m} even, and p_{2m}(1)=0. The [Melvin–Morton–Rozansky theorem](https://people.mpim-bonn.mpg.de/stavros/publications/printed/5papers.pdf) bounds its degree by 2m and identifies its top coefficient with

\[
c_m=[x^{2m}](-\log\Delta_T(e^x)).
\]

For the trefoil,

\[
\Delta_T(e^x)=2\cosh x-1
=\frac{\cosh(3x/2)}{\cosh(x/2)}.
\]

Consequently the standard Bernoulli expansion of log cosh gives

\[
c_m=\frac{(1-3^{2m})(2^{2m}-1)B_{2m}}
                {2m(2m)!}\ne0\qquad(m\ge1).
\tag{3}
\]

The first two values are c_1=-1 and c_2=5/12, agreeing with the previous hand calculations. Nonvanishing uses B_{2m}!=0. Thus p_{2m} has degree exactly 2m.

Fix d>=2 and put r=floor(d/2). The degree-d primitive elements

\[
Q_{d,m}=\mathsf t^{d-2m}P_{2m},\qquad m=1,\ldots,r,
\]

have weights

\[
W_N(Q_{d,m})=2^{d-2m}p_{2m}(N)h^d.
\tag{4}
\]

The scalar polynomials in (4) have distinct degrees 2,4,...,2r and each vanishes at N=1. They are therefore a basis of

\[
E_d=\{f\in\mathbb Q[N]:f(-N)=f(N),\ \deg f\le d,\ f(1)=0\}.
\tag{5}
\]

Indeed E_d has dimension r, and the distinct nonzero leading coefficients prove linear independence. This is a construction of a spanning weight family; no exhaustive description of the primitive diagram space is needed.

## 3. General formal lifting lemma

**Lemma.** Suppose a family F_N(h) has constant term 1 and

\[
\log F_N(h)=\sum_{d\ge2}f_d(N)h^d,
\qquad f_d\in E_d.
\tag{6}
\]

Then there is a group-like element G of the rational completed Jacobi-diagram algebra such that W_N(G)=F_N(h) simultaneously for every positive integer N.

**Proof.** Expand each f_d uniquely in the basis (4), and let R_d be the corresponding rational linear combination of Q_{d,m}. Then R_d is primitive of degree d and W_N(R_d)=f_d(N)h^d. The completed sum R=sum_{d>=2}R_d is primitive. Define G=exp(R), using the connected-sum product. Weight maps are algebra characters, so

\[
W_N(G)=\exp\left(\sum_{d\ge2}f_d(N)h^d\right)=F_N(h).
\]

Everything is degreewise finite; no convergence or compatibility between choices in different degrees is required. QED.

The lift is not unique in the full diagram algebra because kernels of the weight maps remain. The triangular prescription fixes a particular lift inside the displayed family.

## 4. Application to the earlier formal Habiro sequence

Take

\[
F_N(q)=1+(q+q^{-1}-2)
\prod_{j=1}^{2}(q^N+q^{-N}-q^j-q^{-j}).
\tag{7}
\]

At q=e^h, F_N-1 starts in degree six with coefficient (N^2-1)(N^2-4). Its coefficient of h^d is even in N and has N-degree at most d-2: the prefactor contributes at least h^2 without N, and each remaining exponential contributes N-degree no larger than its h-degree. Every power (F_N-1)^a has N-degree at most d-2a in degree d. Thus every coefficient f_d of log F_N belongs to E_d, and in fact has degree at most d-2. F_1=1 gives f_d(1)=0.

The lemma therefore gives a genuine group-like diagram G whose entire sl2-colored weight sequence is exactly (7), as formal expansions of those Laurent polynomials. Also F_2=1, so its fundamental weight is exactly flat, while F_3 is nontrivial. The first nonzero primitive term can be chosen as D6 in (2).

This combines the previously separate formal properties: the same colored sequence is integral Laurent, has an integral Habiro expansion, the recorded q-holonomic recurrence, MMR diagonal Delta=1 and the recorded loop-rationality shape, AND now arises from a rational group-like diagram series satisfying the actual diagram relations. The h^6 leading term has no diagonal N^6 part; the degree-four Alexander obstruction of exp(D4) is absent here.

## Scope and stopping point

G is not asserted to lie in the image of actual classical knots under Z. Rational diagram lifting does not prove integral clasper realization, realizability at every finite stage by one compatible sequence of knots, convergence of such a sequence to a knot, or simultaneous constraints from every other Lie algebra and geometric quantum invariant. Nor does it supply a counterexample to Jones unknot detection.

Scalar loop rationality is also weaker than the diagram-valued rationality requirement of actual knot integrals. No finite beaded-graph expression at each loop degree has been proved for this lift; see `joint_loop_gate.md`. Thus even the graph-rational formal-image condition remains separate from both the scalar properties established here and actual knot realization.

The joint formal compatibility gap asked about here is closed. A proof route invoking these formal conditions together still needs an additional theorem about the image of classical knots. No further basis computation or instrument is needed for this conclusion.
