# Ren cable channel and independent Jones-locus audit

This pass supplies two exact checks. It does not prove Jones unknot detection or produce a counterexample.

## The cable channel survives every two-site top twist

Let J be Ren's capped six-strand pattern, with braid word

```
w = sigma2^-1 sigma1^3 sigma2^-1 sigma4 sigma5^-3 sigma4.
```

Cap positions 3–4 at both ends, and annularly close the other four strands. Let K(p,q) additionally have top crossings `sigma1^p sigma5^q` before those partial closures. Equivalently, these are the two disjoint top twist sites on the remaining four strands. Ren's original knot is K(1,1).

Independently computing the highest annular channel of the blackboard 2-cable gives

```
[z^8] bracket(cable2(J)) = h(A),
h(A) = -A^-24 (A^4-1)^4 (A^4+1)^2
       * (1+A^4+A^8+A^12+A^16+A^20+A^24).
```

In particular h is not zero. Each original top crossing cables to four braid crossings on the eight remaining through strands. Its highest-channel action is the scalar A^4, with inverse A^-4 for a negative crossing. Therefore, for every pair of integers p,q,

```
[z^8] bracket(cable2(K(p,q))) = A^(4(p+q)) h(A) != 0.
```

It follows that **wrap(K(p,q))=4 for every integer p,q**. The diagram gives an upper bound of four, whereas the cable's degree eight is at most twice the original wrapping number. This statement includes link parameter values as well as the odd-odd knot family. It is a geometric essentiality certificate, independent of whether the ordinary closure is an unknot.

The computation uses the TL12 cell module with eight through strands. Its basis consists of 54 noncrossing partial matchings with two cups; the doubled cap/cup is the nested matching `(5,8),(6,7)`, with one-based indexing. A cabled positive generator sigma_i is the four-letter block `(sigma_(2i),sigma_(2i-1),sigma_(2i+1),sigma_(2i))`; negatives use its inverse. Thus 40 crossings act on a 54-component Laurent vector, avoiding an exponential state expansion.

`braid_ren_cable.py` checks every Temperley–Lieb relation on this module, both cap normalizations, the original five-dimensional zero channel, mirror symmetry, and the displayed factorization. Its exact output is `braid_ren_cable.json`.

Ren's paper already reports that the original knot's two-cable has degree eight; the coefficient above is an independent calculation. Primary source: [Qiuyu Ren, *A counterexample to the wrapping number conjecture*, arXiv:2609.11084v2](https://arxiv.org/abs/2609.11084v2), particularly the two annular-degree proofs and the cable remark. No novelty claim is made.

## Independent audit of the complete three-parameter locus

The root calculation parameterizes odd top twists by `p=1+2m`, `q=1+2l` and uses integer meridional twist n. Let delta=-A^2-A^-2 and Delta2=delta^2-1. If Fa,Fb are the denominator-cleared coefficients from the four top-smoothing blocks, then

```
bracket(K(p,q)) = A^(p+q)/delta^2 * (Fa z^2 + Fb).
```

In the colored annular basis `S2=z^2-1`, `S0=1`, a normalized meridional twist multiplies S2 by A^8 and S0 by 1. Evaluating in S^3 and applying the Jones framing normalization gives the exact Jones-one condition

```
(A^(8n) Delta2 + 1) Fa + Fb - delta^3 A^(2(p+q)) = 0.
```

This agrees with `ren_jones_locus.py`. The parity signs and all denominator factors in that file are correct. The nonzero Laurent denominators do not alter an identity over Q(A).

I independently checked its 48-term affine-exponent formula against direct TL2 powers at 125 parameter triples. More importantly, I implemented a different exhaustive solution algorithm, using highest-degree ties instead of its positive/negative coefficient branching:

1. Restrict every affine exponent to the current affine parameter subspace and collect identical terms.
2. Group surviving terms by their variable exponent vector; retain each group's highest constant exponent.
3. At a zero, at least two of those group-leading exponents must agree. Branch on every such equality.
4. Each equality increases the constraint rank by one. With three variables the recursion has depth at most three. A zero restricted polynomial gives an entire solution locus; a nonzero polynomial at full rank rejects that point.

This separate implementation uses its own exact rational row reduction and no integrality pruning. It examines 294 affine loci and finds exactly one solution:

```
(m,l,n)=(-1,0,0), equivalently (p,q,n)=(-1,1,0).
```

There are no positive-dimensional solution loci. The result agrees with the original solver. The original solver's termination and completeness also survive direct code review: any coefficient group must cancel with an opposite-sign group, and every chosen unequal slope imposes a new independent constraint.

The separate geometry check identifies the surviving ordinary closure as an actual unknot. The cable result above shows that its annular pattern nevertheless has wrapping four. The polynomial calculation therefore excludes every nontrivial Jones-one ordinary closure in this fixed three-parameter knot family; it does not exclude all possible companions or all patterns.

Files: `braid_locus_audit.py` and `braid_locus_audit.json`. Run either verification script with standard-library Python from the workspace root.

## Why this does not automatically descend to annular degree zero

Satellite composition is not substitution of ordinary uncolored annular polynomials. The satellite map sends z^2 to the actual framed two-cable of the inner pattern. Here that cable has degree eight, even though the original pattern has degree two. Composing the degree-two Ren pattern with itself therefore raises this degree to eight instead of eliminating the surviving channel.

For an essential annular pattern P of degree two whose ordinary closure is the unknot, write its bracket as `a S2+b S0`, with a nonzero. After fixed framing normalization, substituting a zero-framed companion C gives

```
V(P(C))-1 = nonzero scalar * (J_(C,color 2)-Delta2).
```

Here color 2 denotes the second Jones–Wenzl idempotent, or the three-dimensional representation. Thus a Jones-one satellite from this remaining pattern would require a companion with trivial colored invariant in that channel. The essential unknot anchor by itself does not supply such a companion.
