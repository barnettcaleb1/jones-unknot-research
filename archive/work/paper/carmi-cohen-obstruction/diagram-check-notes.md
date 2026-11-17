# Bounded actual-diagram check

Date: 3 November 2026. Requested values only: `L=1,3,5,7,23`.

**Result: PASS for all five prescribed diagrams, with a uniform mirror.**

The family matching the stated base polynomial is

```python
RationalTangle(2*L+1, 2).numerator_closure().mirror()
```

The unmirrored `L=1` diagram gives `x^-2+x^-6-x^-8`, so the mirror is required to obtain `V_1=x^2+x^6-x^8`. That same choice was used at every requested value. No alternative rational fraction or family was searched.

Each original diagram was constructed with Spherogram. Its zero-based PD labels were shifted by `+1` to make the one-based PD accepted by `regina.Link.fromPD`. The mirrored diagram was constructed explicitly using Spherogram's `mirror()` and independently passed to Regina. The code checks that its computed polynomial equals the exponent inversion of the original polynomial.

Regina's installed `Link.jones` documentation specifies that its Laurent variable `x` is the square root of the usual Jones variable `t`: exponents in `t` are doubled. It already returns the normalized Jones polynomial. For the selected mirrored diagrams, the conversion to the target `V_L(x)` is the identity. No extra writhe normalization, overall sign, or monomial shift was applied. The documentation uses Adams's convention; the mirror is fixed here by the explicit base polynomial, so handedness terminology is unnecessary.

| L | Rational fraction before mirror | Diagram crossings | Components | Exact coefficient comparison |
|---|---|---:|---:|---|
| 1 | 3/2 | 3 | 1 | pass |
| 3 | 7/2 | 5 | 1 | pass |
| 5 | 11/2 | 7 | 1 | pass |
| 7 | 15/2 | 9 | 1 | pass |
| 23 | 47/2 | 25 | 1 | pass |

The expected polynomials were computed using integer coefficient dictionaries from

`V_1=x^2+x^6-x^8`,

`V_L=x^4 V_(L-2)+x^2-x^4+x^6-x^8`.

Intermediate recurrence values are formal polynomials only; no diagrams were constructed for other values of `L`. Regina used its exact treewidth algorithm, and every actual-minus-expected coefficient dictionary is empty.

For reference, the first selected PD is

```text
Spherogram, zero-based: [[2,0,3,5],[4,2,5,1],[0,4,1,3]]
Regina, one-based:      [[3,1,4,6],[5,3,6,2],[1,5,2,4]]
```

The JSON is the authoritative record for all five complete PD pairs, raw Regina Jones strings and coefficient dictionaries, writhes, component counts, expected polynomials, and comparison results. The computation used Python 3.13.7, Spherogram 2.4.1, and the local Regina package (`versionString()` reports `7.4`; installed distribution is `7.4.1`).

Files:

- `diagram-check.py`: reproducible bounded computation.
- `diagram-check.json`: complete five-case evidence.

Run from the workspace with `python3.13 work/paper/carmi-cohen-obstruction/diagram-check.py`; the script locates the existing packages under `work/braid_classification/packages` itself.

This is an independent check of the proposed recurrence against the specified actual diagrams. It confirms these five cases and the convention. It does not prove the recurrence for every odd `L`, and does not replace the manuscript's general skein argument or the separate binomial-basis verification.
