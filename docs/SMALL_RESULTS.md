# Small results, with proofs and limits

[Start here](START_HERE.md) · [Research map](RESEARCH_MAP.md) · [Failures](FAILURES.md)

These short proofs expose reusable parts of the project without requiring the correspondence. They are selected entry points; the [complete early result ledger](../archive/outputs/claude-handoff/RESULT_LEDGER.json) and [later scaffold](../archive/collab/SCAFFOLD.md) contain many additional results and evidence paths. No novelty claim is implied by inclusion here. “Internally checked” does not mean externally peer reviewed.

Conventions are local to each item. For the Kauffman bracket, $\delta=-A^2-A^{-2}$; a monomial unit means $\pm A^k$, not an arbitrary rational factor. Ordinary Jones polynomials have $V_U=1$. Full notes govern all geometric markings.

## 1. Three homology measurements determine the peripheral functional

**Status:** internally checked elementary lemma, RB-HOM3.

Let $M$ be a compact connected oriented 3-manifold with one torus boundary and a rational-homology-sphere filling. Let $V$ be a marked solid torus. Define $h(Y)=|H_1(Y;\mathbb Z)|$ when finite and $h(Y)=0$ otherwise. If $h(M(\alpha))=h(V(\alpha))$ at three distinct slopes, then $H_1(M)=\mathbb Z$, its boundary map onto free homology is primitive, and its homological longitude agrees with that of $V$.

**Proof.** A finite filling gives $b_1(M)=1$. Write $H_1(M)=\mathbb Z\oplus T$, and let $\ell_M:H_1(\partial M)\to\mathbb Z$ be the free part of inclusion. Filling kills the slope class, so $h(M(\alpha))=|T|\,|\ell_M(\alpha)|$. Put $m=|T|\ell_M$, and let $l$ be the primitive integral functional for $V$. Then $m^2-l^2=(m-l)(m+l)$ vanishes on three distinct projective directions. A nonzero product of two linear forms has at most two such directions, so $m=\pm l$. Primitivity forces $|T|=1$ and $\ell_M$ primitive. Their kernels agree. ∎

**Limit:** this is homology interpolation, not a solid-torus recognition theorem. The later topological conclusion needs the separate surgery argument. [Full proof and application](../archive/work/big_reductions/surgery.md).

## 2. Two homology probes leave one explicit arithmetic alternative

**Status:** internally checked algebra within RB-ARITH; the final tangle theorem has additional candidate-proof dependencies.

Choose slope coordinates $\alpha=(1,0)$, $\beta=(a,d)$, with $d>0$ and $\gcd(a,d)=1$. Let $l=(u,v)$. If an integral functional $m$ has the same absolute values as $l$ on both slopes, choose its global sign so $m(\alpha)=u$. Then either

$$
m=l,\qquad\text{or}\qquad m=(u,-v-2au/d).
$$

**Proof.** Its first coordinate is $u$. Equality at $\beta$ says $au+dm_2=\pm(au+dv)$, giving the two expressions. The second is integral only if $d\mid2au$, equivalently $d\mid2u$. Thus $d\nmid2u$ rules out the alternative. ∎

**Limit:** absolute determinants do not supply orientation-preserving homeomorphisms of fillings. This test does not eliminate the distance-two, determinant-one case central to the crossing-change problem. [Proof, signed surgery hypotheses and Ernst–Sumners calibration](../archive/work/big_reductions/surgery.md).

## 3. The alternating Alexander form has a positive second derivative

**Status:** elementary deduction used in the internally audited rational-tangle argument.

Suppose

$$
\Delta(t)=(-1)^k+\sum_{j=1}^k(-1)^{k-j}(t^{n_j}+t^{-n_j}),
\qquad 0<n_1<\cdots<n_k.
$$

Then $\Delta''(1)>0$ if $k>0$.

**Proof.** Differentiating a symmetric pair gives $2n_j^2$, hence $\Delta''(1)=2\sum_j(-1)^{k-j}n_j^2$. Group consecutive terms from the largest end. Every pair is $n_j^2-n_{j-1}^2>0$; if one term remains, it is positive. ∎

The important imported input is that the relevant Alexander polynomial actually has this form. That requires the Floer-simple hypotheses audited against Rasmussen–Rasmussen, rather than an assumption that every knot's Alexander coefficients alternate. [Source and hypothesis audit](../archive/work/big_reductions/surgery.md); [Rasmussen–Rasmussen](https://arxiv.org/abs/1508.05900).

## 4. Specialization at A=1 remembers connectivity

**Status:** boundary lemma internally checked; its specialization-only formulation is recorded with the later gadget audit.

If two actual $2n$-ended tangles have relative brackets equal up to sign at $A=1$, they have the same endpoint matching and the same number of closed components.

**Proof.** Let their matchings be $\pi,\sigma$, their closed-component counts $r,s$, and let $\ell$ count the cycles of $\pi\cup\sigma$. Close both by the same actual tangle with matching $\pi$, and then by one with matching $\sigma$. Crossingful closing tangles are allowed. The bracket's absolute value at $A=1$ is $2^{c-1}$, where $c$ is the resulting link's component count. The two comparisons give $r+n=s+\ell$ and $r+\ell=s+n$. Thus $r=s$ and $\ell=n$. A union of two perfect matchings on $2n$ points has $n$ cycles only when each cycle has length two, so $\pi=\sigma$. ∎

**Limit:** matching is not isotopy. This does prevent silently changing component structure by replacing a full skein signature. [Full proof](../archive/work/theory_restart/jt2_difference_algebra.md).

The component specialization is classical [Jones](REFERENCES.md#jones85), and its use to preserve connectivity in skein replacements has a prior appearance in [Champanerkar–Kofman, Proposition 2.2](REFERENCES.md#ck06). The proof above records the boundary-marking form needed by this project; it is not a priority claim.

## 5. Fixed twist-template fibers are finite unions of integer affine flats

**Status:** internally checked elementary consequence of twist spectral expansion; no novelty claim for the underlying twist-bracket technology.

For a fixed diagrammatic template with finitely many full-twist boxes, clear its fixed denominators and subtract a fixed target. The exact defect has the form

$$
F_n(A)=\sum_{i=1}^M c_i A^{a_i+b_i\cdot n},\qquad n\in\mathbb Z^s.
$$

Its zero set is a finite union of solution sets to integral linear equations.

**Proof.** At a zero, group terms having the same exponent. Every group's coefficient sum is zero. Conversely, any partition into zero-sum blocks gives zeros wherever the exponents within each block coincide. There are finitely many partitions, and every coincidence is an integral affine equation in $n$. Their integer solutions are affine lattice cosets. ∎

Half twists require a finite parity split. Equality up to a unit can include its exponent as an extra variable. None of this says which knot types occupy a unit flat. [Full-twist proof](../archive/work/global_design/multitwist_locus.md); [input-model audit and credit to Champanerkar–Kofman](../archive/work/theory_restart/fixed_twist_bridge_audit.md).

## 6. Enormous binary twist parameters do not defeat sparse comparison

**Status:** FIXED-TWIST-P, internally checked algorithmic corollary.

For the fixed model in item 5, exact equality is decidable in time polynomial in the bit lengths of $n_1,\ldots,n_s$.

**Proof.** Compute the fixed number of integer exponents $a_i+b_i\cdot n$, sort them, sum the coefficients in each collision class, and test whether every sum is zero. Work with sparse exponents in binary; do not expand an array reaching the largest exponent. ∎

**Limit:** “fixed template” includes the outside diagram, number of boxes, strand counts and normalization. It does not mean merely a fixed number of variables in an arbitrary input diagram. General braid powers may also have nonmonomial eigenvalues. [Full scope](../archive/work/theory_restart/fixed_twist_bridge_audit.md).

## 7. A fixed two-channel body has at most two candidate unit twists

**Status:** internally checked, ARB-RESONANCE-BUDGET.

Let $A(t),B(t)$ be nonzero Laurent polynomials and $f_m(t)=A(t)-(-t)^{-m}B(t)$. A monomial value can occur only at an alignment of their top support exponents or an alignment of their bottom support exponents. There are at most two such integers $m$.

**Proof.** If neither endpoint aligns, the extreme terms of the union of the two shifted support intervals are unique and cannot cancel. A monomial cannot have those two distinct surviving extremes. Endpoint equality is a linear equation in $m$, one for the top and one for the bottom. At either candidate the full Laurent identity must still be checked. ∎

For the actual normalized states in the application, where every closure value is nonzero, the minimum span also occurs at one of these alignments: away from them it is at least the longer interval's length; alignment contains the shorter interval in the longer before cancellation. [Proof, normalization and exceptional cases](../archive/work/theory_restart/arborescent_pair_and_deficit.md).

## 8. A proper coordinate ideal cannot be repaired by the allowed box grammar

**Status:** ARB-IDEAL, internally checked.

Let $\Lambda=\mathbb Z[t,t^{-1}]$, $d=1-t^3$, and let a box have integral coordinates $v=(a,c)$. Its star product is

$$
(a,c)*(a',c')=(aa',ac'+ca'+dcc').
$$

Put $I(v)=(a,c)$. The permitted invertible twist matrices preserve this ideal, and

$$
I(v*w)\subseteq I(v)I(w)\subseteq I(v)\cap I(w).
$$

**Proof.** An invertible matrix over $\Lambda$ changes generators of the same ideal. Both product coordinates are sums of products of one coordinate from each input. Integral closure functionals take their value in the resulting ideal. Thus a proper ideal at any node prevents a later closure in this grammar from being a Laurent unit. ∎

**Limit:** coordinates with no common polynomial factor need not generate the unit ideal. A finite-field common zero can give a stronger obstruction. The integrality of the permitted vertical closure is a separate verified part of the dictionary. [Full proof](../archive/work/theory_restart/arborescent_resonance_divisor.md).

## 9. Pairwise compatibility characterizes unimodular star products

**Status:** ARB-PAIR-IDEAL, internally checked.

Over any commutative ring $R$, suppose $(a_i,c_i)=R$, and put $b_i=a_i+dc_i$. Then

$$
I(v_1*\cdots*v_n)=R
\iff (a_i,b_j)=R\quad\text{for every ordered }i\ne j.
$$

**Proof.** Reduce modulo a maximal ideal to a field $k$. If $d\ne0$, the algebra $k[s]/(s(s-d))\cong k\times k$; the factors have coordinates $(a_i,b_i)$. Their product is zero exactly when some $a_i$ and some $b_j$ vanish, necessarily with different indices. If $d=0$, the algebra is $k[\epsilon]/(\epsilon^2)$. Every factor is nonzero: it is either a unit or a nonzero multiple of $\epsilon$. The product vanishes exactly when two factors are multiples of $\epsilon$, the same cross-pair condition because $b_i=a_i$. A proper ideal lies in a maximal ideal, finishing both implications. ∎

The corresponding bad-prime loci agree **after taking radicals**. Equality of multiplicities is not asserted. [Proof and deficit counterexample](../archive/work/theory_restart/arborescent_pair_and_deficit.md).

## 10. Repeating one box has a third-root norm test

**Status:** REPEAT-GATE, internally checked.

For unimodular $v=(a,c)$, a star power with at least two copies remains unimodular exactly when $(a,d)=\Lambda$. For an actual preferred body with $a(1)=1$, this is equivalent to

$$
a(\omega)a(\omega^2)=1,\qquad \omega^2+\omega+1=0.
$$

**Proof.** Item 9 reduces repetition to $(a,b)=\Lambda$. Since $b=a+dc$, this ideal is $(a,dc)$. A Bezout identity for $(a,c)$ gives $(a,dc)=(a,d)$. The factor $1-t$ of $d=(1-t)\Phi_3$ is harmless because $a(1)=1$. Modulo $\Phi_3$, the ring is $\mathbb Z[\omega]$, whose units have norm one; conversely a norm-one element has its conjugate as inverse. ∎

For $a=1+t^{-3}-t$, one has $a(\omega)=2-\omega$ and norm $7$. Repeated products are therefore excluded without checking twist parameters. This is a primitive **third** root, distinct from sixth-root conditions elsewhere. [Full derivation](../archive/work/theory_restart/arborescent_pair_and_deficit.md).

## 11. The augmented tangle homology is multiplicative under compatible sums

**Status:** TH-BULLET-SUM, internally checked using published planar functoriality.

Let $b$ be the crossingless matching that is the horizontal-sum unit and $c$ the other matching. The augmentation sends $b\mapsto\mathbb F$, $c\mapsto0$, and every nonidentity path to zero. If $N(T)$ is the augmented complex's homology, then

$$
N(T_1*T_2)\cong N(T_1)\otimes_{\mathbb F}N(T_2).
$$

**Proof.** Before reductions, a $b$-generator in the product comes only from a pair of $b$-generators. Delooping $c*c$ produces only $c$-summands. The augmented differential is the tensor differential. The augmentation is additive and preserves chain homotopies, so subsequent cancellations do not change its homology. Apply Künneth over a field. ∎

The proof uses Bar–Natan planar functoriality and the KWZ algebra model, not a count of unreduced generators. It also holds for formal complexes, so it supplies no realization obstruction by itself. [Full proof and exact citations](../archive/work/theory_restart/sum_functor_referee.md).

## 12. Extremal parity coherence factors exactly under these sums

**Status:** internally checked consequence of item 11; not a universal tangle law.

Call a nonzero finite bigraded vector space extremally coherent if its highest and lowest quantum degrees each have only one homological parity. A tensor product is extremally coherent if and only if both factors are.

**Proof.** The top quantum space is the tensor product of its factors' top spaces, and likewise at the bottom. A tensor product of nonzero parity-graded spaces has one parity exactly when both factors do. If either has both, tensor its two nonzero parity pieces with any nonzero homogeneous piece of the other factor; both parities remain. ∎

This is a reduction for the specified equivariant-sum operation, not a reduction to ordinary prime knots. Later actual examples refuted the expectation that all quotient tangles have coherent ends. [Proof and scope](../archive/work/theory_restart/sum_functor_referee.md).

## 13. Universal coefficients separate torsion from genuine Euler cancellation

**Status:** TH-FIELD-END, internally checked.

For a finite free integral bigraded cochain complex, write $b_{h,q}$ for rational homology rank and $t_p(h,q)$ for the number of $p$-primary cyclic summands. Then

$$
\dim_{\mathbb F_p}H^{h,q}=b_{h,q}+t_p(h,q)+t_p(h+1,q).
$$

**Proof.** This is the universal-coefficient exact sequence. Each torsion summand contributes adjacent homological degrees, whose Euler signs cancel. Rational support is contained in every mod-$p$ support, and the integer Euler polynomial is common to all fields. ∎

A nonzero endpoint Euler coefficient at a mod-$p$ endpoint is therefore also a rational endpoint. Away from finitely many torsion primes the entire dimension profile agrees. But an adjacent equal-quantum pair does **not** itself diagnose torsion: two free summands can have the same profile. [Argument and signed formal control](../archive/work/theory_restart/characteristic_zero_ladder_referee.md).

## 14. A natural higher differential can hide a formal ladder at every closure

**Status:** exact formal countermodel, internally checked; no actual tangle realization.

Let $Q$ be the specified nonzero compact Bar–Natan complex. Set $Q'=h^{-8}q^{-14}Q$ and

$$
L=a(0)\oplus Q\oplus hQ\oplus Q'\oplus hQ'.
$$

Its Euler class is that of $a(0)$, since each opposite-parity pair cancels. Define a higher differential by the underlying identities $Q'\to Q$ and $hQ'\to hQ$, of bidegree $(8,14)$, and zero otherwise.

**Proof of the control.** Sources and targets are disjoint, so the higher map squares to zero. It commutes with the original differential because it is an identity between shifted copies. Over $\mathbb F_2$, their sum is a differential. Its page-eight cancellation removes all four extra summands. Every additive graded closure functor preserves shifts, identities and these equations, so the cancellation works naturally after every such closure. ∎

The existence of compatible additive collapse sequences is thus insufficient for Euler detection. This does not identify the map with any geometric Floer differential. [Full construction and surviving geometric question](../archive/work/theory_restart/surgery_ladder_referee.md).

## 15. Fixed Jones Taylor jets are polynomial-time computable

**Status:** recorded proof with complexity quantifiers accepted in the collaboration.

Fixed-order computability is part of the classical finite-type theory; see [Bar-Natan, Theorem 1](REFERENCES.md#barnatan95). The direct recursion below fixes this ledger's input model. It is distinct from the uniform-in-order bound in item 16.

For every fixed $r$, the first $r$ Taylor coefficients of the normalized Jones polynomial of an explicit link diagram are exactly computable in polynomial time.

**Proof.** Change crossings until the diagram becomes a descending unlink, telescoping the skein relation. Each smoothing branch brings $t^{1/2}-t^{-1/2}$, of order one at $t=e^h=1$. Modulo $h^{r+1}$, only smoothing depth at most $r$ matters. With $n$ crossings there are $O(1+n+\cdots+n^r)$ relevant nodes; each requires polynomial-size diagram operations and truncated exact rational arithmetic. ∎

A promised family whose nonzero defects have uniformly bounded Taylor order therefore has a polynomial-time identity test. Under $\mathrm P\ne\mathrm{NP}$, the NO-image of a coNP-hard many-one reduction cannot have that promise. Depths must be unbounded somewhere in that image, not along every input sequence. [Full input model](../archive/work/theory_restart/jt2_scope_audit.md).

## 16. An integral counting encoding needs quantitatively deep vanishing

**Status:** uniform knot estimate and integral-depth deduction internally checked; link extension recorded separately.

For an $n$-crossing knot, $n\ge1$,

$$
|[h^r]V_K(e^h)|\le2(16n)^r.
$$

**Proof outline with the uniform constant.** At smoothing depth $s$, the descending skein recursion has at most $n^s$ terminal terms. Bounding smoothing factors, accumulated monomials and unlink factors on $|h|\le R$ gives

$$
|V_K(e^h)|\le e^{4nR}\sum_{s\ge0}(2nR e^{4nR})^s.
$$

At $R=1/(16n)$ the ratio is $e^{1/4}/8<1/6$, and the total is less than two. Cauchy's estimate yields the coefficient bound. The full note supplies the diagram and exponent bookkeeping. ∎

If $V_K-1=ND\ne0$, where $N\in\mathbb Z$ and $D$ is **integral** of order $r$ at one, write $D=(t-1)^rE$. Its first $h$-coefficient is $NE(1)$, a nonzero integer multiple of $N$. Hence

$$
r\ge\frac{\log(|N|/2)}{\log(16n)}.
$$

Polynomial diagram size and exponentially large $|N|$ force $r=\Omega(m/\log m)$. The upper bound $|N|\le2^m$ alone is insufficient. For the two-component defect $\Delta_L(q)=V_L(q^2)+q+q^{-1}$, the corresponding bound is $8(32n)^r$. [Knot proof](../archive/work/theory_restart/depth_uniform_audit.md); [link extension](../archive/work/theory_restart/jt2_scope_audit.md).

## 17. Increasing modular divisibility need not increase Taylor depth

**Status:** EF-DEPTH, internally checked arithmetic and primary-source normalization; no novelty claim.

The Eliahou–Fromentin family has Jones polynomial congruent to one modulo $2^r$, yet

$$
V_{K_r}(e^h)=1+96\,2^{r-1}h^4+O(h^5).
$$

**Proof.** Their printed seed, in bracket variable $A=e^x$, gives $f_1=1+16384x^4+O(x^6)$, $g_1=8192x^4+O(x^6)$. Horizontal doubling obeys $f_{r+1}=f_r^2$, $g_{r+1}=2f_rg_r+\delta g_r^2$, so both fourth-order coefficients double. The marked closure has normalized bracket $f_r+A^{-6}g_r$. Substitute $x=-h/4$, obtaining $24576/256=96$. The coefficient never vanishes. ∎

The displayed crossing count is exponential in $r$, so this respects item 16. [Full calculation](../archive/work/theory_restart/eliahou_fromentin_bridge_audit.md); [portable exact certificate](../archive/work/theory_restart/referee_checks/ef_depth.py); [Eliahou–Fromentin, Lemma 4.2 and Proposition 5.2](https://arxiv.org/pdf/1610.05560v2).

## 18. Exact two-component Jones-triviality belongs to C_=P

**Status:** elementary recorded complexity deduction; no hardness theorem.

JT₂ consists of oriented two-component diagrams with $V_L(q^2)=-q-q^{-1}$. It belongs to $\mathrm C_{=}\mathrm P$, the class of zero sets of GapP functions.

**Proof.** Each normalized bracket coefficient is a signed count of polynomial-size witnesses: choose smoothings, then monomials from loop factors. Their signs and exponents are efficiently computable. Thus each target-subtracted coefficient $g_e(D)$ is GapP. Only polynomially many exponents occur. The function $G(D)=\sum_e g_e(D)^2$ is GapP by closure under products and polynomial sums, and over the integers vanishes exactly when every coefficient difference vanishes. Invalid inputs may be assigned value one. ∎

There is a reduction from knot Jones-triviality: $K\mapsto K\sqcup U$, whose polynomial is $-(q+q^{-1})V_K(q^2)$. Neither statement proves a reverse reduction or hardness. [Full scope and literature comparison](../archive/work/theory_restart/jt2_scope_audit.md).

The conditional connection between Jones unknot detection and exact counting has a [Welsh antecedent quoted by Hass–Lagarias–Pippenger](REFERENCES.md#welsh93). The GapP argument here records the precise whole-polynomial two-component language; no novelty claim is made for this routine membership refinement.

## 19. A scalar binary gate need not be reusable multiplication

**Status:** SERIAL-TL2, TRUSTED; independent referee pending at the pause.

Work in $TL_2=K[I,e]/(e^2=\delta e)$, $K=\mathbb Q(A)$. For a scalar functional $\ell$, let $\alpha=\ell(I)\ne0$, $\beta=\ell(e)$, $Z=\beta I-\alpha e$. Then

$$
\ell((I+xZ)(I+yZ))=\alpha+xy\alpha\beta(\alpha\delta-\beta).
$$

This looks like a binary product, but no analogous nonzero pure all-variable product exists in this serial architecture for three or more independent inputs.

**Proof.** Vanishing singletons put every defect in the one-dimensional kernel $KZ$. Vanishing proper pair terms then forces $\ell(Z^2)=0$. Apply $\ell$ to

$$
Z^2-(2\beta-\alpha\delta)Z+\beta(\beta-\alpha\delta)I=0.
$$

Because $\alpha\ne0$, this gives $\beta(\beta-\alpha\delta)=0$. Hence every positive power of $Z$ has zero evaluation, contradicting the nonzero full product. ∎

Before closure, the binary output still contains $(x+y)Z$. The functional killed those terms; it did not remove them from the reusable state. Larger spaces, different wiring and noninvertible backgrounds remain outside the theorem. [Full proof](../archive/work/theory_restart/jt2_difference_algebra.md).

## 20. The simplest projector accumulator pays in components

**Status:** PROJECTOR-COST, TRUSTED; independent referee pending at the pause.

Formal orthogonal projectors $p_0=e/\delta$, $p_1=I-e/\delta$ satisfy

$$
\prod_i(p_0+z_i p_1)=p_0+\left(\prod_i z_i\right)p_1.
$$

Clear denominators with $C(z)=e+z(\delta I-e)$. If actual two-string tangles realize each $C(z_i(A))$ up to monomial units and $z_i(1)=0$, every closure of $m$ serial carriers has at least $m$ components.

**Proof.** At $A=1$, each carrier specializes to $\pm e$. Item 4 forces cup-cap matching and no closed component. Composing $m$ matchings creates $m-1$ closed components at the interfaces. Closing the remaining arcs adds at least one. An outside context cannot fuse components already closed inside the composite. ∎

They need not be split or unknotted. Internal cuts and extra boundary legs change the architecture and are not excluded. This is one scoped obstruction to a JT₂ compiler, not a universal no-go. [Full proof and mixed-corner criterion](../archive/work/theory_restart/jt2_difference_algebra.md).

## 21. From V3 non-flatness to knot-level Jones detection

**Status:** a corollary of the internally refereed V3 algebra and marked skein dictionary, with the internally checked ODD-CLOSURE-REPAIR. No external specialist review or priority determination is claimed.

Let $(K,h)$ be the marked strong inversion of a V3 vertical construction

$$
\texttt{s.l1.}(Y^N B_1\cdots B_r)\texttt{.}(x_2)^a\texttt{.u1},
$$

where $N\in\mathbb Z$, each $B_i$ is a non-integral rational box in the fixed dictionary, $a$ is odd, and $r\ge1$ if $|a|\ge3$ or $r\ge2$ if $a=\pm1$. These are hypotheses on the marked construction, not a classification of all inversions of the resulting covering knot. V3 gives $J\ne1$. Put $L_n=T(1/n)$, so $L_0=U$, and let $a_2(K)$ denote the second Conway coefficient.

* If $a_2(K)=0$, then $V(L_n)\ne1$ for every integer $n\ne0$.
* If $a_2(K)\ne0$, all nonzero even $n$ are excluded, and at most one odd $n$ can have $V(L_n)=1$. In the convention below, that parameter must satisfy $j=n a_2(K)$, where $j$ is fixed by the inversion. This is a necessary condition, not an assertion that the exceptional knot exists.

**Proof.** In the fixed preferred convention set $G=(J-1)/(1+t)^2$, $\Phi_3=1+t+t^2$, and $\epsilon_n=0$ or $1$ according to the parity of $n$. The marked closure identity is

$$
V(L_n)=t^{12j\epsilon_n}\bigl[1+(1-(-t)^{-n})\Phi_3G\bigr].
$$

For even nonzero $n$, the prefactor is one and $(1-(-t)^{-n})\Phi_3$ is nonzero. The Laurent polynomial ring is a domain, so $V(L_n)=1$ would imply $G=0$, contrary to $J\ne1$.

For the odd parameters one must keep the prefactor. Each $\Sigma_2(L_n)$ is an integral homology sphere obtained by $1/n$ surgery, so $\det L_n=1$. The symmetrized Seifert form is even unimodular, and its signature lies in $8\mathbb Z$. The knots $L_{n+2}$ and $L_n$ differ by one crossing change, which changes signature by at most two. Hence signatures are constant on each parity class. In this convention they are zero on the even class and $-8j$ on the odd class.

Use the ordinary Casson normalization of Mullins's formula,

$$
\lambda(\Sigma_2L)=-\frac{V'_L(-1)}{12V_L(-1)}+\frac{\sigma(L)}8.
$$

The orientation agreeing with the displayed closure formula gives $\lambda(\Sigma_2L_n)=-n a_2(K)$. An odd Jones-unit closure therefore satisfies $-n a_2(K)=-j$. If $a_2(K)\ne0$, at most one nonzero odd integer solves this equation. If $a_2(K)=0$, it forces $j=0$, removing the prefactor; the same domain argument as for even $n$ then contradicts $J\ne1$. A consistent reversal of orientations changes the signed identification, not the zero or uniqueness conclusions. ∎

The proof imports [Mullins, Theorem 5.1, with the Casson normalization and orientation check recorded here](../archive/work/theory_restart/roots_odd_referee.md); that audit also gives a [primary source for the branched-cover formula and normalization comparison](https://arxiv.org/abs/math/9811021). The non-flatness input is the [V3 proof audit](../archive/collab/data/roundD/refV3_REPORT.md), completed topologically by the [arbitrary-box dictionary](../archive/work/theory_restart/skein_dictionary_arbitrary_boxes.md) and its [three-referee report](../archive/collab/msgs/20261117-061728-claude.md). The formal odd-closure target from the earlier letter explains why simply deleting the prefactor is invalid.

**Concrete recorded family.** E6 has $a=-3$, $N=-2$, boxes of slopes $1/9,5/13,-4/13$, and recorded $a_2(K)=0$. Its saved two-channel calculation gives span $V(L_n)=n+28$ and both extreme coefficients of modulus two for every $n\ge1$. Thus the corollary supplies ordinary Jones non-triviality uniformly in $n$, including a family outside the semi-adequate and Turaev-genus-one tests and above the 24-crossing range. The [saved input and polynomial data](../archive/claude/theory-restart/mont/cx/roundD/lit/examples_E6.json) and [internal literature/geometry report](../archive/collab/data/roundD/LIT_RESULT.md) are separate evidence from the uniform V3 proof. Their broader topology and novelty claims are internally reported, not externally certified; see the [scope and prior-work comparison](RESEARCH_MAP.md#6-exact-transfer-systems-two-bridge-necklaces-and-arborescent-boxes).

## Further proof collections

* [Two-slot pattern symmetry](../archive/work/theory_restart/pattern_symmetry_dichotomy.md): a nonscalar relative Hermitian operator forces the projected universal symmetry group to be cyclic; the similitude case needs a different argument.
* [Finite-index rigidity](../archive/work/theory_restart/finite_index_pattern_rigidity.md): the missing outer coset and its exclusion for actual pattern tensors. This classifies tensors, not geometry.
* [Two-box signed-square identity](../archive/work/global_design/two_box_signed_square.md): a square constraint on determinant specializations of four marked corners.
* [Arbitrary-box skein dictionary](../archive/work/theory_restart/skein_dictionary_arbitrary_boxes.md): the bridge from actual marked tangles to transfer formulas.
* [Generic constant-braid restrictions](../archive/work/theory_restart/jt2_clause_gate_scope.md): finite projective image under a common invariant-code hypothesis and the separate rational-Hadamard valuation obstruction; TRUSTED at pause.

For results not summarized here, follow the ledger identifier to the full proof and correction history. This guide deliberately does not promote every archived “PROVED” heading into an externally established theorem.

