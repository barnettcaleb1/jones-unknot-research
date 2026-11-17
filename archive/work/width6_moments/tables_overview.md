# Exact parked-position moment tables

## Authorized restoration addendum (20261103-080944)

The original summary-based tables below record the evidence available before restoration. Caleb subsequently authorized replaying only the same six-letter control. The restored `../width6_instrument/arc_noncancellation_exact_full.json` contains all 4,005 records and matches all 22 non-runtime summary fields. `nonzero_restored_check.json` supplies every parked row's exact counts: matching 0 has 7 positive/6 negative at degree -1, at all 24 positions; matching 1 has 3 positive/4 negative at degree -2, at all 23 positions. Thus all 47 positions have mixed extrema. The original metadata-only tables are preserved as historical outputs; the new check resolves their explicitly missing counts. The broader research remains paused.

Scope: Claude 20261103-045944. Existing exact incidence records and saved independently checked anchor metadata only. No new braid search, geometric transport, intersection generation, or winding computation.

## Main findings

1. **P1 fails on the saved nonzero control.** Every one of its 23 matching-1 parked positions has a lowest nonzero moment `mu_0 = -q^-2` whose unique surviving degree receives both positive and negative individual record contributions. This also holds for all three parked positions contributing at the total surviving degree `q^-4` (indices 8, 12, 22). The archived summary suffices to prove mixed signs, although the exact raw count is only narrowed to 3 or 7.
2. **P2 has no eligible parked position in the full witness.** All 1,585 full-witness positions have `mu_0 != 0`. Its implication about positions with `mu_0 = 0` is therefore vacuous on these data.
3. The split witness has mixed-sign extrema at every full-representative parked position, and pure extrema after reduction to four incidences. This is a statement about representatives. No slide-minimality has been certified for the nonzero control, so P1's failure does **not** by itself refute the version of Conjecture M restricted to slide-reduced representatives.
4. All sampled lowest nonzero moments have index 0. These data do not test a moment ladder beginning with a vanishing ordinary Burau fiber. Kernel matching sums with positive vanishing order are not interchangeable with per-parked-position moments.

## Polynomial profiles

Here `S = sum eta_x q^A_x u^W_x`, `mu_k = partial_u^k S(q,1)`. Every entry below has `mu_2 = 0`; in fact all moments of index at least 2 vanish because the aggregated S is affine in u. A zero moment can still contain cancelling individual nonzero-weight records, retained in the full tables.

| Case | Matching | Positions | S(q,u) | mu_0 | mu_1 |
|---|---:|---:|---|---|---|
| Reduced witness | 0 | 2 | 1 | 1 | 0 |
| Reduced witness | 1 | 1 | 1 - q^-1 | 1 - q^-1 | 0 |
| Full witness | 0 | 192 | q^-1 | q^-1 | 0 |
| Full witness | 0 | 114 | q^-1 u | q^-1 | q^-1 |
| Full witness | 0 | 24 | q^-1 - 1 + u | q^-1 | 1 |
| Full witness | 1 | 1255 | 1 - q | 1 - q | 0 |
| Nonzero control | 0 | 24 | q^-1 | q^-1 | 0 |
| Nonzero control | 1 | 23 | -q^-2 | -q^-2 | 0 |

The nonzero control's polynomial rows follow exactly from the saved geometric range `W_x = 0` at all 47 parked positions, together with the saved inner specializations. No missing raw records were reconstructed.

## Individual record signs at actual extrema of the lowest nonzero moment

All lowest moments are `mu_0`, so raw and weighted signs coincide here. Counts exclude zero falling-factorial weights when a higher moment is tabulated. The JSON distinguishes the highest/lowest *potential* degree before cancellations from the highest/lowest *surviving* polynomial degree.

| Case/matching | Extremal degree | Positive records | Negative records | Total |
|---|---:|---:|---:|---:|
| Reduced witness / 0 | 0 | 1 | 0 | 1 |
| Reduced witness / 1, highest | 0 | 1 | 0 | 1 |
| Reduced witness / 1, lowest | -1 | 0 | 1 | 1 |
| Full witness / 0 | -1 | 93 | 92 | 185 |
| Full witness / 1, highest | 1 | 9 | 10 | 19 |
| Full witness / 1, lowest | 0 | 36 | 35 | 71 |
| Nonzero control / 0 | -1 | unknown | unknown | unknown |
| Nonzero control / 1 | -2 | 1 or 3 | 2 or 4 | 3 or 7 |

Each row applies to every parked position of that matching. For the nonzero control, the two alternatives are correlated: `(positive,negative,total) = (1,2,3)` or `(3,4,7)`.

## Exact P1 certificate without the omitted 4,005 raw records

For matching 1, all W are zero and `mu_0 = -q^-2`. Let `n_j` count individual first-point records with `A_x = j`. The saved parked `A_y` multiplicities are `0:2, -1:18, -2:3`. The saved surviving collapsed line is degree -4 and contains exactly 21 records, all in matching 1. Therefore

```
2*n_-4 + 18*n_-3 + 3*n_-2 = 21.
```

Since the signed coefficients at -4 and -3 in mu_0 vanish, `n_-4,n_-3` are even. Since the coefficient at -2 is -1, `n_-2` is odd. Nonnegative solutions give `(n_-4,n_-3,n_-2) = (6,0,3)` or `(0,0,7)`. Consequently the extremal coefficient -1 receives respectively `1 positive + 2 negative`, or `3 positive + 4 negative`, records. P1 fails under either possibility.

The total `q^-4` receives nonzero contributions only from matching-1 parked indices `8,12,22`: respectively `+q^-4,-q^-4,+q^-4`. Thus restricting P1 to positions contributing at a degree that survives the outer sum does not remove the failure.

## Outer cancellation

| Case | Matching 0 sum | Matching 1 sum | Total |
|---|---|---|---|
| Reduced witness | 1 - q^-1 | -1 + q^-1 | 0 |
| Full witness | q^-2 - q^-3 | -q^-2 + q^-3 | 0 |
| Nonzero control | 0 | q^-4 | q^-4 |

These sums include the saved anchor units. In both split representatives all individual inner sums are nonzero; splitness is realized by cancellation in the outer sum.

## Files and reproduction

Run `python3 work/width6_moments/tables_compute.py` to regenerate all three tables from the existing saved inputs.

- `tables_witness_reduced.json`: all four reconstructed `(x,A,W,eta)` incidences, all three parked-position polynomials and full extremal counts.
- `tables_witness_full.json`: all 340,350 reconstructed incidences, all 1,585 parked-position polynomials and full extremal counts.
- `tables_nonzero_control.json`: all 47 exact polynomial rows, saved W-range evidence, and partial sign certificate; explicitly records that raw incidences are missing.
- Corresponding `tables_*_summary.json` files contain compact statistics and witnesses.
- `tables_*_compact.json` omit raw incidence lists but retain every parked-position polynomial and extremal count summary.

Reconstruction for a saved record `[m,x,y,a,b,raw_sign]` uses

```
A = a - a_m - A_y
W = (b - b_m)/2 - w0_geometric(y)
eta = raw_sign / raw_sign_at_x0_same_y.
```

The parity is checked, the x=0 reference is checked, and the reconstructed specialization `sum eta q^(A-2W)` is compared exactly with every saved inner pairing. This is reuse of a previously independently checked formula, not a new geometric verification. Full S, rather than only the first three moments, is used to determine exact lowest nonzero order. No kernel fiber records were available, so no kernel per-position moment claims are made.
