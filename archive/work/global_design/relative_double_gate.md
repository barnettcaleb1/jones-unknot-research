# Relative doubling: what can retain ordinary Jones data?

Date: 2026-11-03. Bounded theory/literature pass. No scans or new matrix computations.

Update 12:59: the one-band Jones-unit-only loophole below is CLOSED by `band_transfer.md`. Bleiler–Eudave-Muñoz force every composite determinant-one ribbon knot to have fusion number at least two. Lobb's many-twist-site extension still has a one-band unlink resolution, so is not a higher-fusion escape. The originally proposed unrestricted two-resolution lemma remains impossible; a genuinely higher-fusion construction needs a different theorem.

## Answer to the concrete Kinoshita--Terasaka question

A one-twist-region symmetric-union presentation of the Kinoshita--Terasaka knot **already exists**, with the unknot as partial knot. Consequently, the Lamm--Tanaka statement that every partial knot of such a presentation has trivial Jones polynomial does not supply a counterexample or a currently missing presentation.

Primary evidence independent of the inaccessible full 2025 article:

- [Moore, Symmetric unions without cosmetic crossing changes, arXiv:1507.07996v2](https://arxiv.org/pdf/1507.07996), Section 2 and Figure 3. Her terminology in that section means one tangle replacement; multiple replacements are explicitly called generalized symmetric unions. Figure 3 gives KT and U as two different symmetric unions having partial knot U.
- [Eisermann--Lamm, A refined Jones polynomial for symmetric unions](https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/publications/symjones.pdf), Example 6.7 and Figure 16(b). Their family D_k has trivial partial knots, D_0=U, and D_2=KT. They compute

      W_k(s,t) = 1 + ((-s)^k - 1) f(t),
      f(t) = t^-4 (t^2+1)(t-1)^2(t^2+t+1)(t^2-t+1) != 0.

  Thus at s=t the output Jones polynomial depends on marked tangle information beyond the partial knot, even when the partial knot is the actual unknot. This example is a direct obstruction to treating arbitrary symmetric unions as a function of V_partial alone.

The [2025 Lamm--Tanaka abstract](https://www.sciencedirect.com/science/article/pii/S0166864125003918) supplies the claim about Jones-trivial partial knots. I could verify the abstract and section summaries, but not retrieve the full proof or proposition number. The potentially interesting new geometric problem would be: **does KT have a one-region symmetric-union presentation with a nontrivial partial knot?** A positive answer, together with their theorem, would refute Jones unknot detection. The existence of a one-region presentation alone does not do so, and no source retrieved here settles existence of a nontrivial partial knot.

## 1. A real positive mechanism: two competing ribbon resolutions

The strongest nearby construction is Kanenobu--Watson--Lobb, not a formal replacement of a colored cable by a product. [Lobb, arXiv:1105.3985](https://arxiv.org/pdf/1105.3985), Theorem 1.4, treats a knot with a specified one-ribbon presentation. Twisting that ribbon shifts the non-unknot summand of its sl(N) homology uniformly. If a knot admits two such ribbon resolutions, twists can be transferred between them in opposite directions without changing the homology. His Theorem 3.2 extends the transfer to knots K_T(p_1,...,p_n) built from a ribbon tangle T: fixed sum of twist parameters and fixed individual parities give the same indicated homologies.

This has the correct kind of mechanism: actual unlink resolutions make a local skein/exact-sequence defect independent of the rest of the diagram, so the defects at two sites cancel. It is stronger than ordinary Jones preservation and does not invoke J_2 => J_3.

What it does **not** say is that every K#mirror(K) admits the needed two-resolution presentation, or that arbitrary such transfers produce prime strongly invertible or low-tunnel-number knots. Ribbon fusion number one is a substantial geometric condition, not a consequence of being ribbon. I did not identify a universal construction with these properties in this pass.

The archived project has already checked the smallest Watson shell. In that six-strand shell its seed is J_beta#mirror(J_beta), where J_beta is two-bridge, and its closure matrix is

      [[X, delta], [delta, delta^2]],   X=V_J(A^-4)V_J(A^4).

The determinant-one locus forces J_beta=U and the particular shell degenerates to a connected sum. See `work/research26/watson_geometric_inputs.txt` and `work/research21/watson_topology_audit.txt`. Those are existing results, not recomputed here. The higher-ribbon-tangle theorem is a genuine extension in available geometry; it does not automatically identify its zero-twist seed with arbitrary K#mirror(K).

There is also an exact obstruction to rescuing this particular matrix by mirror correlation. Write D(T)=a+delta*b and D(U)=c+delta*d for the two denominator closures. Then

    B(T,U)=D(T)D(U)+(X-1)ac.

For U=mirror(T), the residual is `(X-1)a*bar(a)`. Since the Laurent ring is a domain, it cannot vanish by cancellation between mirrored inputs: it requires X=1 or a=0. This argument is specific to this matrix; it is not a theorem about every correlated-input shell.

## 2. The minimal relative-skein obstruction

There are two different ways to insert arbitrary input K, and they must stay distinct.

**One-strand input boxes.** A long knot in a ball with two boundary endpoints has a rank-one bracket skein class, so inserting K and mirror(K) in two such boxes automatically multiplies the output by V_K V_mirror(K), up to the framing correction. But the boundary sphere of either box is a decomposing sphere meeting the output twice. As long as the operation leaves these boxes intact, the inserted local knots remain connected-sum factors. No exterior band or braid that misses the boxes can turn this into primeification.

**Cutting K at two or more arcs.** This can eliminate the visible decomposing spheres and permits genuine primeification. Its relative skein state has more than one coordinate. The ordinary Jones polynomial supplies one closure functional on that state; the other coordinates are marked-tangle information. A fixed outside gluing then sees a bilinear form in the state of the input and its mirror, rather than automatically the product of the two ordinary closures.

There is a precise algebraic design criterion. Let H be the relevant finite-dimensional relative skein space over Q(A), and let ell:H->Q(A) be the closure defining V_K. A proposed double shell gives a bilinear pairing B:H x H->Q(A). A **universal independent-input** identity

      B(x,y) = ell(x) ell(y)

is exactly the statement that B has rank one and factors through the two closure functionals. It is enough to verify this on crossingless basis tangles, which are actual diagrams. Achieving it geometrically without preserving decomposing spheres is the construction problem.

Do not overstate this obstruction: an identity only on pairs (T, mirror(T)) is weaker than the independent-input identity. One cannot polarize using arbitrary linear combinations of knots and conclude that the full matrix has rank one. Likewise, a skein rank-one matrix does not by itself imply a topologically split shell. Those would be additional theorems, with the same danger encountered in earlier rank-one tangle claims.

## 3. The concrete next lemma worth seeking

The constructive route I would keep is a **two-resolution primeification lemma**:

> Given a diagram of K, construct a ribbon knot R(K;p,q), two specified bands, and a seed identification R(K;0,0)=K#mirror(K). Require that either band's designated resolution is an actual two-component unlink for all relevant p,q; opposite twist transfer preserves the normalized Jones polynomial; and for some p=-q the output is prime (plus a separately proved strong inversion if that is the desired target).

The payoff would be immediate: R(K;p,-p) has the product Jones polynomial and preserves nontriviality once primeification/nontriviality is established. The actual unlink resolutions are the mechanism; they are the missing data to draw, not a conjectural scalar identity to fit.

**However, the unrestricted version of this lemma is impossible.** Its seed would have ribbon fusion number at most one. The double branched cover of a ribbon knot of fusion number b has first homology generated by at most 2b elements. Take K to be a connected sum of m trefoils. The double branched cover of K#mirror(K) has H_1=(Z/3)^(2m), requiring fusion number at least m. Thus no one-ribbon seed construction covers arbitrary K. The generator bound is recalled in [Sarkar, Ribbon distance and Khovanov homology](https://msp.org/agt/2020/20-2/agt-v20-n2-p14-p.pdf), Section 3. This homology bound alone did not exclude determinant-one inputs. The later Bleiler–Eudave-Muñoz argument in band_transfer.md DOES exclude the one-band seed for every nontrivial Jones-unit K. A genuinely higher-fusion construction is still outside these obstructions.

There are two cheap theory gates before doing computations:

1. Specify either a restriction on K compatible with one-ribbon seeds, or a multi-band replacement. The arbitrary-input, one-ribbon version has already failed the branched-cover rank gate above.
2. Make the primeification proof independent of Jones. Lobb's polynomial/homology transfer only compares invariants; it does not certify distinct knot types, and his paper explicitly says a separate distinction argument is required.

An alternative would need a genuinely higher-fusion theorem, beyond Lobb's published many-twist-site construction, which still has fusion number at most one. The exact seed and intermediate closure data must be written down. Saying “put a braid beside its inverse” is insufficient: cancellation occurs only after the specific caps or bands have joined their strands. Other closures can retain the full braid matrix.

## Judgement

No global prime/strongly-invertible/low-tunnel-number transformation depending only on ordinary Jones was established. The two-resolution mechanism is real, but its naive arbitrary-input one-ribbon version is obstructed by branched-cover rank. The fixed KT target is concrete but its known presentation has partial unknot, and it also supplies an explicit warning: even one-region symmetric unions retain marked information invisible to V_partial.
