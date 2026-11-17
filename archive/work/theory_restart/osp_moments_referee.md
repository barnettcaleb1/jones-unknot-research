# OSP and the third moment: bounded referee report

16 November 2026. Referee of Claude `210856`, items 5–6. This report does not decide FT; the integral-model referee handles that statement. No scan was performed. The new Claude OSP and literature reports were skeletons when read.

## 1. Exact calibration, and its limit

For a superspace of dimension `1|2`, the super permutation on its tensor square has positive eigenspace of ordinary dimension

    dim Sym²(V_even) + dim Λ²(V_odd) + dim(V_even⊗V_odd) = 1+1+2=4,

and negative eigenspace of dimension `3+2=5`. Its superdimension is `1−2=−1`. Thus BOTH numerical checks in the proposed color-2 interpretation work: the `(+1,+1,−1)` fusion spectrum with dimensions `(1,3,5)`, and `Delta_2=−1` at the chosen root. This is an exact calibration, not a construction of the requisite mixed ribbon category. A regular integral matrix realization specializing to this super permutation would be materially stronger than matching eigenvalues. The FT referee reports such a ramified lattice calculation; that calculation, rather than an appeal to generic spectral projectors, should carry the proof.

The axis needs additional structure. An ordinary finite-dimensional representation of the classical Lie superalgebra osp(1|2) is completely reducible and its simple summands have odd ordinary dimensions. Therefore an ordinary rank-two axis specialization is a sum of two trivial one-dimensional modules. More basically, in the classical symmetric super category, double braiding is the identity for every pair of objects. It cannot give the nonconstant `(+1,−1)` mixed full-monodromy spectrum claimed for our axis. This refutes only the naive interpretation using an ordinary classical osp module for every strand. It does not refute a defect sector, a quantum covering specialization, or the FT referee's concrete root model.

Primary source for the classical statement: M. Yousofzadeh, *Extended Affine Lie Superalgebras*, Publ. RIMS Kyoto Univ. 52 (2016), 309–333, Corollary 2.5 and Theorem 2.6, [publisher PDF](https://ems.press/content/serial-article-files/41278).

## 2. What the quantum correspondence actually supplies

Blumen's Theorem 1.1 identifies the vector-representation invariants with two Kauffman-polynomial specializations. His discussion of Zhang's correspondence explicitly restricts the SO side to tensorial representations at generic parameter. This alone does not transport our spinorial color-1 axis, and it is not a theorem about integral lattices at the exceptional root. See S. C. Blumen, *On the U_q(osp(1|2n)) and U_{−q}(so(2n+1)) Uncoloured Quantum Link Invariants*, arXiv:0901.3232, Sections 1–2, [primary PDF](https://www.maths.usyd.edu.au/u/pubs/publist/preprints/2009/blumen-3.pdf).

The more relevant source is S. Clark, *Quantum osp(1|2n) knot invariants are the same as quantum so(2n+1) knot invariants*, Algebr. Geom. Topol. 17 (2017), 2961–3005, arXiv:1509.03533. Theorem 3.8 and Corollary 3.9 give the generic multicolored tangle functor; Theorem 4.24 gives, for a same-colored oriented knot,

    osp J_K^lambda(q) = i^{star(K,lambda)} so J_K^lambda(i^{-1}q).

The phase and parameter convention matter. Neither theorem asserts the proposed classical defect model or identifies our mixed trivalent graph with it. [Primary text](https://arxiv.org/html/1509.03533v1).

One must not overstate the rank-two obstruction: the quantum covering theory DOES contain a rank-two module. Ebert's account displays `V(1)`, with one even and one odd basis vector, and the relations

    EF − pi FE = (JK−K^{-1})/(pi q−q^{-1}),
    J|V(m) = pi^m.

At `pi=−1,q=1` this presentation is not automatically the ordinary enveloping algebra of classical osp(1|2). In particular its denominator is `−2`, and its central `J` distinguishes the weight sectors. Thus “the parameter is now 1” does not by itself establish the claimed classical limit. See M. Ebert, *A new presentation of the osp(1|2)-polynomial link invariant and categorification*, arXiv:2210.09583, Sections 3.2–3.5 and Theorem 3.6, [primary text](https://arxiv.org/html/2210.09583v1).

For the root-local proof, cutting the axis is the clean normalization. Generically the open diagram is an intertwiner `V_1→V_1`, hence a scalar by Schur's lemma. Compute this scalar as a matrix entry in a regular lattice and then specialize. The closed quantum trace is `delta` times that scalar, but no division by the vanishing specialized dimension is required. This is an ordinary reduced-scalar construction; a modified trace need not be introduced unless invariance under a different cut or a genuinely nonsemisimple closed-category formulation is required. The graph's trivalent coupon still needs an explicitly regular intertwiner.

**Verdict:** the super permutation is a valid and useful description of the local root model. An osp/parity-defect *weight-system identification* remains open. The new finite target would be an explicit module/defect object and coupon reproducing both local crossing operators and the axis reduction, with the parameter and phases fixed. A generic quantum correspondence is not a substitute for this check.

## 3. The observed denominator 36 follows from ROOTS

Assume the ROOTS factorization established in the separate referee pass and put

    D(t)=(t+1)^2(t−1)(t^2+1)(t^2−t+1),
    H(t)=(J(t)−1)/D(t) in Z[t,t^{-1}].

Write `D=(t+1)^2 f`. Direct differentiation gives

    f(−1)=−12,    f'(−1)=30,
    J''(−1)=−24 H(−1),
    J'''(−1)=180 H(−1)−72 H'(−1).

Since the banked second-moment identity is `J''(−1)=−24 a_2(K)`, this proves

    H(−1)=a_2(K),
    M_3=−J'''(−1)+3J''(−1)
       =72 H'(−1)−252 a_2(K)
       =36(2H'(−1)−7a_2(K)).

Consequences, unconditional given ROOTS and the banked second-moment identity:

* `36 | M_3` for every inversion;
* `M_3/36 = a_2(K) mod 2`;
* on the target core `a_2(K)=0`, the stronger divisibility `72 | M_3` holds;
* the first residual third-order datum on that core is exactly `H'(−1)`.

This explains the denominator 36 in the sample without an osp identification or a finite-type theorem. It also identifies precisely the unproved part of the proposed `iota`:

    iota = [2H'(−1)−7a_2(K)−7v_3(K)]/5.

Its integrality is a MODULO-FIVE CONGRUENCE not implied by the displayed root factorization. It remains data, unless another argument supplies this congruence. Naming the quotient does not identify it with a constituent-knot or eta invariant.

If FT holds, `M_3` is order at most three for the stated equivariant moves. The ordinary `v_3` restricted to these moves is also of order at most three: each simultaneous-pair difference expands into ordinary differences involving at least one crossing at that site. Thus the rational-valued displayed `iota` inherits that bound. It is primitive under compatible equivariant connected sum: `J` is multiplicative, while `M_1=0`, so `M_3` is additive, and `v_3` is additive. These are useful necessary conditions on any proposed geometric identification; they are not an identification.

One scope correction: the supplied example with `v_3(K)=0` and `iota=1` rules out a universal scalar-multiple formula in `v_3`. By itself it does NOT prove that `iota` is not determined by the underlying knot. That requires an identified knot with two inversions giving different values, or a separate structural argument. Before trying eta/constituent formulas, request that fixed two-inversion certificate.

### Fixed calibration subsequently completed

At the parent's request, I computed exactly the TWO published figure-eight inversion inputs, without sampling other knots. The archived KWZ table records

    4_1^1: s.l1.y0.y0.x1.u2,
    4_1^2: s.l1.x0.x0.y1.u2.

The preferred plain-bracket computation gives

    J_1=t^-6+t^-3−t^-2+1−t,
    J_2=J_1(t^-1),
    (M_0,M_1,M_2,M_3,M_4)=(1,0,24,−180,1200)

for the first, and `(1,0,24,180,1200)` for the second. The figure-eight has `v_3=0` and `a_2=−1`, so the displayed candidate `iota` equals `−1,+1`. Thus the needed same-knot certificate exists, and the claim that M_3 depends on the inversion is now checked on a fixed identified pair. The earlier logical caution applies to the supplied one-example argument, not to this new certificate.

Reproducer and exact output: `referee_checks/figure_eight_inversion_moments.py` and `.json`. They use the existing exact Laurent bracket evaluator and the two archived table halfwords. This identifies genuinely equivariant information already at third order; it does not prove the universal modulo-five congruence.

## 4. What this gives the theory program

The moment expansion already determines the Laurent polynomial J, regardless of FT. The proposed FT theorem upgrades it to a structured equivariant finite-type system, but nonvanishing of that system for every nontrivial inversion remains exactly the hard separation assertion. The concrete new simplification here is to remove the universal factor D and work with H: on the a_2-zero core, `H(−1)=0`, and its first derivative controls M_3 with the explicit factor 72. No finite list of these tests has been shown sufficient, and no new class-free detection theorem follows from the correspondence alone.
