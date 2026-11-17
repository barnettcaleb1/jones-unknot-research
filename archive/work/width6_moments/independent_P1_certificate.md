# Independent check: P1 is false in the archived nonzero representative

This uses only saved records and summaries. No geometric model was constructed or replayed. Reproduce with `python work/width6_moments/independent_check.py`; the machine-readable result is `independent_results.json` in this directory.

## The moment values

For the nonzero six-letter control, all 47 parked positions have saved winding range (W_x=[0,0]). Therefore (S(q,u)) is independent of (u), and the archived colored inner pairing is exactly μ₀:

- Matching 0: all 24 positions have μ₀ = q⁻¹.
- Matching 1: all 23 positions have μ₀ = −q⁻².
- Every position has μ₁ = μ₂ = 0 and, in fact, every higher moment zero.

The underlying 4005 individual records were not saved in `arc_noncancellation_exact.json`. Its saved extremal record count nevertheless suffices to prove that the matching-1 extremal term has mixed signs.

## Exact parity certificate

In matching 1 the reference exponents satisfy (a_m=b_m=1), and all (w_0,W_x) vanish. Hence the collapsed record degree is (A_x+A_y). The saved parked data give the following multiplicities of (A_y):

| (A_y) | 0 | −1 | −2 |
|---|---:|---:|---:|
| Number of positions | 2 | 18 | 3 |

Let (n_j) be the number of first-point intersections with (A_x=j). These numbers do not depend on the parked position: both (A_x) and the normalized local sign ηₓ are first-point data. The archived surviving collapsed line of degree −4 contains exactly 21 records, all with exchange exponent 1. Thus

\[
2n_{-4}+18n_{-3}+3n_{-2}=21.
\]

Since the signed inner sum is −q⁻², the counts (n_{-4},n_{-3}) are even and (n_{-2}) is odd. Nonnegativity leaves exactly two possibilities:

| (n_{-4}) | (n_{-3}) | (n_{-2}) | Positive records at −2 | Negative records at −2 |
|---:|---:|---:|---:|---:|
| 0 | 0 | 7 | 3 | 4 |
| 6 | 0 | 3 | 1 | 2 |

Either possibility proves that **every matching-1 parked position has both signs at the unique extremal degree of its lowest nonzero moment**. These are the positions in the surviving matching: matching 0 sums to zero, whereas matching 1 gives the nonzero total q⁻⁴.

Therefore prediction P1 fails for this saved representative. This does not refute an existential claim about a slide-reduced representative: the current data do not certify that this representative is slide-reduced. The exact extremal record count is not recoverable from these summaries alone, but mixed signs are forced independently of that ambiguity.

## Reduced split witness

The four saved raw records reconstruct the three parked inner sums as 1, 1, and (1-q^{-1}), all independent of (u). Every lowest nonzero moment is μ₀. At each of its nonzero extremal degrees there is exactly one signed record. There is no parked position with μ₀ = 0, so P2's conditional hypothesis is never met in this reduced witness.

These results also show why the moment hierarchy must not be inferred from a whole matching polynomial's vanishing order: an outer sum can cancel even when every inner μ₀ is nonzero.
