# Matching parity in the canonical mixed pairing

This note uses only the three saved fixed-cap Long–Paton polynomials. No braid scan, geometric enumeration, or minimization was performed.

## Exact observation

Label the two source arcs and the two target loops. Each complete configuration intersection has a matching `m in {0,1}`. Choose a base intersection with matching `m0`. The loop used to define its local-system monomial returns the two labeled configuration points in their original order precisely when `m=m0`. Consequently

```
b mod 2 = m XOR m0.
```

This is the parity of the number of half-exchanges. It does not require any extremal-monomial hypothesis.

The archived canonical Phi differs from an instrument base-lift normalization by one unit `epsilon*s^u*t^v`. Hence the matching of a canonical monomial is

```
m = (b + v + m0) mod 2.
```

Thus **canonical even and odd powers of t are the two complete matchings, up to one global swap**. The s normalization of the original cap classes does not affect that assertion. The parity pieces are exactly `(Phi(t)+Phi(-t))/2` and `(Phi(t)-Phi(-t))/2`; these are integral polynomials because their monomial supports are disjoint.

This recovers matching-wise SIGNED contributions. It does not recover the unsigned products of one-point intersection counts, because arbitrary same-monomial opposite-sign cancellations may already have occurred.

## The tau = sigma1^-2 leading line

The saved canonical mixed polynomial has surviving collapsed s-degree 27, with terms

```
-11*s^27 - 10*s^29*t.
```

At `t=-s^-2`, the matching-wise contributions are therefore **-11*s^27 and +10*s^27**. Their sum is `-s^27`.

Claude's structural guess is correct in this precise sense: the `11` and `10` come from the two different complete matchings, up to swapping their labels. The two matchings contribute at least 11 and 10 actual incidences on this line. Their unsigned counts have the form `11+2r` and `10+2s`, with `r,s>=0`, allowing also any hidden canceling monomials on that line. These are lower bounds and parity statements, not an assertion of exactly 21 incidences.

The higher generic collapsed line has `s^29+s^31*t`. Its contributions from the two matchings are `+1` and `-1`, so its vanishing is explicitly cancellation between matchings.

For the other two completions, the highest surviving line is `s^39`: the matching-wise signed contributions are `+1` and `0`. The second matching need not have zero actual incidences there.

## Whole-lift incidence lower bounds

Each actual incidence contributes one signed monomial. For each parity class separately, its actual number of incidences is at least the sum of the absolute values of its generic Phi coefficients.

| tau | even-b class lower bound | odd-b class lower bound | total lower bound |
|---|---:|---:|---:|
| identity | 74,173,998 | 42,374,176 | 116,548,174 |
| sigma1^2 | 153,090,112 | 82,220,788 | 235,310,900 |
| sigma1^-2 | 5,869,720 | 3,197,952 | 9,067,672 |

The named matchings may be swapped by the base-lift choice. These bounds hold for the fixed generic lifts under ordinary arc isotopy and deck-unit shifts. They are not cap-slide invariant and do not bound slide-minimal tangle complexity. Large incidence lower bounds do not, by themselves, preclude an efficient algorithm for counting unsigned products without enumerating every configuration.

Exact calculations and both matching-resolved specialized polynomials are saved in `parity_counts.json`, reproduced by `parity_counts.py`.
