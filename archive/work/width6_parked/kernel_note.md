# Two specified Burau-kernel configurations

This is exactly Claude043608(ii), with no braid scan and no large geometric enumeration.

Top cap system C=(34)(56), free endpoints1,2, is cell index **i=0**. Bottom cup system D=(12)(45), free endpoints3,6, is index **j=6**. The input is cap_C k cup_D, with the same kernel braid k acting on both bottom arcs. The two words are the archived 44-letter Bigelow6/Ren word and the 106-letter Long–Paton word. Both have exponent sum zero.

## Exact result

**Both id-coefficients are nonzero.** Both incidence graphs have exactly two arcs, no closed components, and e-type boundary pairing [[0,1],[2,3]]. Thus neither is a zero candidate requiring a split/unknot test.

| kernel | terms in J(A) | A exponent range | coefficients at minimum/maximum A degree | generic Phi terms | generic Phi L1 |
|---|---:|---|---|---:|---:|
| Bigelow6 | 18 | [-30,38] | +1,+1 | 46 | 640 |
| Long–Paton6 | 43 | [-86,82] | -1,+1 | 726 | 84,618,964 |

Here J is the TL2 id-coefficient in the archived bracket convention, not the Jones polynomial of a separately chosen closed knot. With s=A^-2 and q=s^2, both exponent sums are zero, so J_hat is obtained simply by A^e -> s^(-e/2).

The Bigelow expression factors exactly:

```
J_hat = s^-19 (q-1)^4 (q+1)^3 (q^2+1)^2
                  (q^2-q+1)(q^4-q^3+q^2-q+1).
```

For Long–Paton,

```
J_hat = s^-41 (q-1)^3 (q+1)^2 (q^2+1)^2 (q^2-q+1)^2 R(q),
```

where R is an explicitly saved degree29 polynomial with leading and constant coefficient -1. No irreducibility assertion is made. All coefficients and the factor extraction are in kernel_specific.json and kernel_factors.json.

## The one-point statement needs a small correction

The normalized one-point cap/Burau matrix is

```
M(identity) = M(Bigelow) = M(LongPaton) = [[0,1],[0,1]].
```

Thus the first column vanishes, not every matrix entry. Both complete one-point matching products vanish individually, which is the needed statement. Values1 use the archived cap normalization; no identification with unnormalized geometric figure-eight-loop values is asserted.

The generic mixed pairing was independently computed from the calibrated Lawrence form:

```
Phi = q^-2 P/(1-t),
Phi(t=1) = 0,
Phi(t=-q^-1) = q^-1 J_hat != 0.
```

These identities hold exactly for both words.

## Stronger isolation of the parked weight

Split the generic polynomial by parity, writing

```
Phi(q,t) = F_0(q,u) + t F_1(q,u),  u=t^2.
```

The original cap normalization may involve odd powers of s; that scalar does not affect the following. The parity pieces label the two matchings up to a global swap.

- Bigelow: F_0 is identically zero; F_1 has **exact order two** at u=1.
- Long–Paton: F_0 and F_1 each have **exact order one** at u=1.

In particular, both matching-wise sums vanish separately when the parked-point weight is1. The nonzero Jones specialization arises when u becomes q^-2. For Bigelow this occurs entirely within one matching parity; it is not a consequence of cancellation between two nonzero matching aggregates.

This is an exact aggregate certificate that the parked/exchange weight matters for these examples. It does not identify individual parked positions or their winding relative to adjacent punctures, and it provides no coherence theorem for all nonsplit configurations. A monomial coefficient can aggregate many opposite-sign incidences.

Highest surviving mixed lines:

- Bigelow: -s^7 t^-3 -> +s^13.
- Long–Paton: +s^43 t -> -s^41.

These are aggregate polynomial terms, not claims of single geometric intersection contributions.

Reproduce with `python3 work/width6_parked/kernel_specific.py`; exact factor extraction is `kernel_factor.py`. Matching-parity quotients and t=1 evaluations are included in the saved JSON. No geometric splitting classification was needed because both id-coefficients are nonzero.

## Bounded Bigelow geometry follow-up

A single guarded attempt on the same Bigelow configuration used the canonical effective54-letter word, exact PL transport, and safe local isotopies. It stopped at prefix46/54 with457 and19,082 source vertices, exceeding the requested15,000-per-arc limit after64.49seconds. Exact partial curves and the full prefix history are saved in `kernel_bigelow_geometry.json`; these are explicitly prefix data, not a completed representative of the requested tangle.

The parent then authorized **one bounded continuation from that saved prefix**, rather than restarting: only the remaining8 moves, a70,000-vertex per-arc guard,240seconds remaining transport, and sparse parked slices only if full geometry completed. This continuation stopped at **prefix51/54**, with **1,762 and76,682 vertices**, after **175.90seconds**. Checkpoints are in `kernel_bigelow_resume.json`, reproduced by `kernel_bigelow_resume.py`. It stopped permanently for this turn. Neither attempt obtained final one-point intersection metadata or any parked-position winding comparisons for the full kernel tangle.

In this canonical isometric frame the short object is target loop0, not the literal original source arc s=k(12). A future targeted cross-matching diagnostic would move source1 against that loop and park source0 on target1. The present failed-prefix attempt supplies no data for that comparison. A zero difference between winding about the parked point and its adjacent puncture would also not remove the mechanism: coalescing the weights q and q^-2 gives weight q^-1 at that puncture, rather than ordinary equal-q Burau weights.
