# Bounded Jones unknot search — October 31, 2026

This is a small, reproducible exploratory search, not an exhaustive knot census.
No counterexample was established. No proof of the unknot-detection conjecture
was obtained. The lengths below count letters in sampled braid words; they do
not establish the minimal crossing number of the represented knot.

## Sample and result

The generator uses C++ `mt19937_64` with seed **20261031**. It generates words
in the six signed generators of the four-strand braid group, rejecting an
immediate inverse of the preceding letter. The closed braid is retained only
if its permutation is a four-cycle. A four-cycle has odd parity, so the sampled
word lengths are odd.

| Word length | Generated words | Knot closures | Exact Jones=1 hits |
|---|---:|---:|---:|
| 27 | 10,000 | 4,949 | 45 |
| 31 | 10,000 | 4,982 | 26 |
| 35 | 10,000 | 4,936 | 13 |
| 39 | 10,000 | 4,982 | 9 |
| Total | 40,000 | 19,849 | 93 |

Of these 93 hits, **91 have explicit, replay-verified reductions to the empty
one-strand braid**, certifying they are unknots. The remaining **two were not
classified within the simplification budget**. All 93 also have Alexander
polynomial 1. This additional invariant does not establish that the unresolved
two are unknots, and nothing here establishes that they are nontrivial.

The full words and results are in `exact_hits.json`; the primitive certificates
and unresolved words are in `unknot_certificates.json`. The unresolved entries
have zero-based indices 82 and 86. Their complete signed words are:

```
82: 1 3 2 1 2 2 3 -2 3 1 -3 2 1 3 -2 -1 -1 2 1 -2 -3 -3 1 2 -3 -2 -2 3 -1 -1 -3 2 -1 -3 -2
86: 2 -1 -1 2 -1 3 1 -2 3 -1 3 2 1 2 -3 -2 -2 3 1 -3 -1 2 2 2 -1 -1 -2 -1 -1 2 -1 -3 1 3 -1 -1 3 1 -2
```

## Exact arithmetic and validation

`search.py` constructs the 14 crossingless matching diagrams for the
Temperley–Lieb algebra on four strands. It uses

```
sigma_i = A*identity + A^(-1)*e_i
loop d = -A^2 - A^(-2)
V = (-A)^(-3*writhe) * closure_bracket
```

The bracket of one closed circle is 1. Therefore Jones=1 is exactly the
condition that the bracket is the single term
`(-1)^writhe * A^(3*writhe)`. Integer Laurent-polynomial arithmetic verifies
every hit. There is no floating-point polynomial arithmetic.

The C++ search uses the exact evaluation A=2 modulo the prime 1,000,003 as a
cheap rejection filter. A polynomial equal to 1 necessarily passes this
filter. Passing it alone is not evidence that the polynomial is identically 1;
all 93 survivors were subsequently recomputed as full Laurent polynomials.

Validation includes the unknot, trefoil, figure-eight, mirror symmetry, braid
relations, inverse cancellation, positive and negative stabilization, and
93 exact-polynomial comparisons against the C++ finite-field implementation.
The number 93 in this comparison is coincidental: those are early sampled
words, not necessarily the 93 Jones=1 hits. The independent reduced Burau
implementation in `alexander.py` checks the Alexander polynomial, with known
unknot, trefoil, and figure-eight tests.

Each unknot certificate consists of explicit inverse cancellations, cyclic
rotations (conjugations), commuting distant generators, braid relations,
and Markov destabilizations. `certify.py` also supports standard exchange
moves preserving braid closures, but the saved 91 successful certificates
do not need them. The verifier checks each operation's prerequisites and
requires the final result to be exactly the empty one-strand braid.
For the exchange-move convention see Birman–Menasco,
[Studying links via closed braids V: The unlink](https://www.math.columbia.edu/~jb/slvcb-v.pdf).

The first simplification pass was limited to roughly 30,000 states per hit.
A deeper 500,000-state attempt on entry 82 also failed; a subsequent search
including exchange moves was limited to 200,000 states and 45 seconds per
unresolved entry. The saved `states` values refer to each entry's last saved
attempt, rather than total work over all attempts. Failure means that this
particular bounded search did not find a certificate; it is not a mathematical
obstruction to simplifying the knot.

## Reproduce or verify

Only Python 3's standard library is required for verification. From this folder:

```
python3 replay.py
```

This recomputes all 93 Jones and Alexander polynomials, replays all 91 unknot
certificates, and repeats the saved modular cross-checks. It does not rerun
the costly simplification searches.

To regenerate the random sample (requires a C++17 compiler):

```
python3 search.py
clang++ -O3 -std=c++17 search.cpp -o search
./search 10000
python3 search.py modular_hits.txt
```

Running `python3 certify.py` starts a new bounded simplification pass and
overwrites `unknot_certificates.json`; it is unnecessary for checking the
saved evidence. C++ random-generator behavior and modulo sampling are fixed
explicitly in the source, without implementation-dependent distribution classes.

## Limits

The sample is neither uniform over knot types nor over isotopy classes of
braid closures. It contains many presentations of ordinary unknots and may
repeat knot types. A long word can represent a knot of small crossing number.
The search covers only this small sample of closed four-strand braids. It
does not test general knots or supply meaningful statistical confidence for
the conjecture. The two unresolved words are ordinary classification tasks
left by the bounded simplifier, not established counterexamples or evidence
of novel behavior.
