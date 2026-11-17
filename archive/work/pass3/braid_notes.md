# Products and commutators of Bigelow-kernel conjugates

This bounded pass found no counterexample to Jones unknot detection and no proof of that conjecture. Two structured searches leave no unresolved candidate. A separate exact calculation proves an infinite-word obstruction for two noncommuting kernel blocks. These are limited results; no novelty claim is made.

## Setup

Let K be the Bigelow-factor commutator defined in `work/pass2/braid_kernel.py`, using `[x,y]=xyx^{-1}y^{-1}`. It is a pure five-strand braid of writhe zero and acts as the identity in the Burau representation. The factors come from page 403 of [Bigelow, *The Burau representation is not faithful for n=5* (1999)](https://doi.org/10.2140/gt.1999.3.397); his commutator convention differs, as documented in the preceding pass.

Let `C=sigma1 sigma2 sigma3 sigma4`. Its closure is the unknot. The five-dimensional residual Temperley–Lieb representation rho satisfies `tr(rho(C))=0`. The preceding pass verified the complete closure-trace decomposition on all 42 TL5 diagram basis elements. Consequently, for any product B of conjugates of K or K inverse,

```
V(closure(B C)) - 1 = A^-12 tr(rho(B) rho(C)).
```

For a different signed Coxeter anchor alpha, the analogous test is `tr(rho(B)rho(alpha))=tr(rho(alpha))`; the right-hand side need not be zero. All these closures are knots because B is pure and the anchor induces a five-cycle.

## A proved obstruction for arbitrary words

Define

```
P = sigma2^-1 K sigma2,
R = sigma2 K sigma2^-1,
Q = P R P.
```

For any nonempty positive word W in the two blocks P,Q, write a for its number of P letters and b for its number of Q letters. Then, with `t=A^-4`,

```
lowest t-degree of V(closure(W C)) = 3 - 37a - 112b,
coefficient at this degree = (-1)^(a+b-1).
```

In particular this polynomial is never 1. This applies to arbitrary order and arbitrary word length, not just to powers of one block. A finite S7 Hurwitz-action calculation in the certificate verifies `[P,Q] != 1`, so the two blocks do not commute.

Here is the full leading-degree argument. In the exact link-state basis used in `tl5_block.py`, let E_ij denote the matrix unit with indices starting at one, and put

```
L = -E_33 + E_35,
M = E_53,
N = E_41 + E_53.
```

Exact Laurent matrix multiplication gives

```
rho(P) = A^148 L + terms of lower degree,
rho(R) = A^152 M + terms of lower degree,
rho(Q) = A^448 L + terms of lower degree,
rho(C) = N + terms of lower degree.
```

The integer matrices satisfy `L M L=L`, `L^2=-L`, and `tr(L N)=1`. Therefore

```
rho(W) = (-1)^(a+b-1) A^(148a+448b) L + lower-degree terms.
```

Taking the trace after multiplication by rho(C) preserves this leading coefficient, and the Jones normalization subtracts 12 from its A-degree. Conversion to `t=A^-4` proves the formula. No assumption about finite samples is used in this induction.

`braid_obstruction.py` verifies the leading matrices, Burau-kernel and purity premises, five full Jones cross-checks, and the noncommutativity witness. `braid_obstruction_certificate.json` saves the exact words and witness. The broader graph of leading rank-one products for 18 signed single-generator conjugates is saved in `braid_leading_results.json`, but is unnecessary for the two-block theorem above.

## Centralizer and commutator search

The first search considered every freely reduced relative conjugator g of length at most six in the eight letters `sigma_i^{+/-1}`. It tested the two proposed kernel mechanisms

```
[rho(K),rho(g)]=0,
[rho(K),rho(g^-1 K g)]=0,
```

and the Jones-one closure tests for `[K,g]` and `[K,g^-1 K g]` with all 16 signed Coxeter anchors.

There were 156,865 freely reduced input words and 18,941 distinct matrices at the filter specialization `A=2 mod 1,000,003`. A failed equality at this specialization rigorously excludes an identity of Laurent polynomials. The only matrix classes passing either centralizer test represented the identity braid. To avoid losing a distinct braid through specialization, all 868 duplicate representatives of potentially surviving classes were compared using the faithful Artin action on the free group: every duplicate was the same actual braid as its representative.

The closure filter left the identity cases, 16 immediate conjugacy tautologies

```
[K,alpha] alpha = K alpha K^-1,
```

and one additional modular survivor. Full exact Jones evaluation rejected that survivor: it had 299 nonzero terms and A-degree range -596 through 596. There is no unresolved candidate in this search.

## Mixed pairs of short conjugates

The second search used `X=c^-1 K c` and `Y=d^-1 K d`, with both c and d of length at most three. It tested `X Y^-1`, `X^-1 Y`, and all four signed commutators `[X^epsilon,Y^eta]`, closing each with every signed Coxeter anchor. There were 259 distinct conjugates and 3,207,456 modular trace tests. This count is not a count of full Jones computations.

The filter left 104 exact geometric tautologies and one other survivor. In each tautological case the faithful Artin action verified `d alpha c^-1=1`, hence `Y=alpha X alpha^-1`. The two balanced-product closures are then explicitly conjugate to alpha:

```
X Y^-1 alpha = X alpha X^-1,
X^-1 Y alpha = X^-1 alpha X.
```

The remaining survivor was the commutator with `c=sigma3 sigma2 sigma4^-1`, `d=sigma2^-1 sigma3^-2`, and anchor `sigma1 sigma2 sigma3^-1 sigma4`. Its exact Jones polynomial had 307 nonzero terms and A-degree range -612 through 612, so it too failed. No nontrivial Jones-one knot was found.

## Reproduction

Run from the workspace root with Python's standard library:

```
python3 work/pass3/braid_obstruction.py
python3 work/pass3/braid_conjugates.py 6
python3 work/pass3/braid_pairs.py
```

The full exact outcomes of the two non-tautological filter survivors are recorded in `braid_filter_survivor_exact.json` and `braid_pairs_exact.json`. Existing code and data from `work/pass2/` and `work/attack_search/` are required. The family obstruction takes a few seconds; each modular search takes roughly 15 seconds on this machine.
