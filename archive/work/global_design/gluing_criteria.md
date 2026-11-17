# What an exact Jones-preserving geometric construction must control

2026-11-03. Theory deductions; no enumeration. These are construction criteria and scoped obstructions, not a solution of Jones detection or a claim of novelty.

## 1. Two-endpoint input balls retain connected-sum factors

Let B_1,...,B_r be disjoint embedded balls in S^3, each meeting an output knot L in one proper arc. Let K_i be that arc's knot closure, and let L_0 be obtained by replacing every input arc by a boundary-parallel arc. Then

    L = L_0 # K_1 # ... # K_r.

Each boundary sphere meets L twice and gives the indicated connected-sum decomposition; apply the disjoint decompositions successively. Thus independent long-knot boxes retain every input's prime factors. If at least two of the displayed factors are nontrivial, the output is composite. If just one is nontrivial, the construction returns that factor.

The scalar Jones multiplication comes from the rank-one skein module of the two-endpoint ball. No converse is claimed: a rank-one formal skein tensor need not exhibit actual decomposing spheres. The geometric ball hypothesis is indispensable.

## 2. When a gluing depends on just one measurement from each input

Let E,F be vector spaces over an infinite field, with nonzero linear functionals ell and m. Let B:E×F→k be bilinear.

**Lemma.** If B is constant, with value c, on {ell=1}×{m=1}, then B(x,y)=c ell(x)m(y) everywhere.

Choose x_0,y_0 with ell(x_0)=m(y_0)=1. Write x=x_0+v, y=y_0+w for v in ker ell and w in ker m. Varying scalar multiples of v,w in the constant identity shows B(v,y_0)=B(x_0,w)=B(v,w)=0. Expanding arbitrary x,y now proves the factorization. The converse is immediate.

Thus a universal independent-input skein identity determined only by two chosen closure values requires a rank-one pairing with the specified factors. An actual-knot-only statement may use additional geometric restrictions on which vectors occur; those restrictions are not supplied by the linear algebra. A restriction to correlated pairs (T,mirror(T)) is also weaker, so unrestricted polarization is not justified there.

For Watson's particular closure matrix

    M = [[X,delta],[delta,delta^2]],
    x=(a,b), y=(c,d), D(x)=a+delta b,

the residual information has an exact form:

    x M y^t = D(x)D(y) + (X-1)ac.

For the original shell X is the square of the figure-eight Jones polynomial, and X-1 is nonzero. With mirror-correlated inputs y=bar(x), the difference from D(x)bar(D(x)) is

    (X-1)a bar(a).

The Laurent ring is a domain, so this difference vanishes only if a=0. Mirror correlation alone does not remove the second bracket coordinate in this shell. Framing units must be matched before using these bracket identities as normalized Jones identities. Source and convention details: `hyperbolic_gate.md`, `relative_double_gate.md`, and [Watson's paper](https://personal.math.ubc.ca/~liam/files/preprint.pdf).

## 3. Closed-surface symmetries invisible to the full skein module

Let S_g be a closed oriented surface of genus g>=1. The kernel of the orientation-preserving mapping-class action on the full Kauffman bracket skein module of S_g×I is

    g=1: {I,-I};
    g=2: {1, the hyperelliptic involution};
    g>=3: {1}.

**Proof.** The module has a free basis given by unoriented essential multicurves on S_g, including the empty multicurve. Mapping classes permute this basis. Acting trivially therefore requires fixing every essential simple-curve isotopy class. For g>=2 the kernel of this curve action is exactly the displayed centre. Equivalently, fixing every curve makes the mapping class commute with every Dehn twist, and the usual centre theorem applies. For the torus, a matrix in SL_2(Z) preserving every unoriented primitive slope is ±I. The listed involutions fix all basis multicurves, proving the converse.

The free-basis argument also works after specialization to any nonzero coefficient ring with A invertible. It concerns the FULL surface skein module, not a finite-level reduced TQFT quotient or one Temperley–Lieb cell module.

The multicurve basis is Przytycki's theorem, explicitly used in the [DGST 2012 erratum](https://nyjm.albany.edu/j/2012/18-5v.pdf). The curve-action kernel is stated in [Luo, Automorphisms of the complex of curves](https://arxiv.org/pdf/math/9904020); the mapping-class centre argument is also standard in Farb–Margalit, Section 3.3. The root and symmetry subagent independently checked the deduction. No priority claim.

**Scope.** This eliminates a higher-genus mutation recipe whose polynomial proof is that the gluing symmetry acts as identity on every skein state. It does NOT say that preserving one specified Jones closure forces trivial action, nor that no new geometric Jones-preserving operation exists. Context-specific cancellation is outside the theorem.

## 4. Universal one-band doubling fails a topological test

Lobb's competing ribbon-resolution mechanism preserves homology and hence Jones under opposite twists when two actual one-band unlink resolutions exist. It is an exact mechanism. But a seed R(K;0,0)=K#mirror(K) cannot have a one-band ribbon presentation for arbitrary K.

If a ribbon knot R has fusion number f, then the first homology of its branched double cover needs at most 2f generators. This follows from the handle presentation of the double cover of a ribbon disk and is recalled in [Sarkar, Ribbon distance and Khovanov homology, Section 3](https://msp.org/agt/2020/20-2/agt-v20-n2-p14-p.pdf).

For K=#^m trefoil,

    H_1(Sigma_2(K#mirror(K))) = (Z/3)^(2m),

so f>=m. Already m=2 prevents the proposed universal one-band seed. More generally no fixed upper fusion bound works for all such doubles.

This obstruction does not decide the Jones-unit input locus: V_K=1 forces determinant one, so the homology group used here vanishes there. Nor does it exclude a genuine many-band construction. Such a construction must supply its seed identification and unlink resolutions; Lobb's theorem does not construct them for arbitrary K.

## Decision

No new global simplification was obtained. The useful outcome is a precise distinction between (a) scalar control that leaves local knot factors untouched, (b) genuine geometric interaction that exposes additional bracket coordinates, and (c) context-specific identities capable of cancelling those coordinates. Watson/Lobb provide real examples of (c), but the inspected forms do not carry arbitrary Jones-unit inputs into a known detection class. A further turn on this construction strategy needs an explicit new geometry, not a replacement scalar or an unmarked band.
