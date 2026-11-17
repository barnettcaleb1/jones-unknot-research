# Carmi–Cohen obstruction note

Author: Caleb Barnett. Contact: https://barnettcaleb1.github.io.

This is the first complete draft for internal adversarial review. It identifies an incompatibility in the universal, length-independent residual-twist package of Carmi–Cohen, arXiv:2606.22410v1 (21 June 2026). It does **not** assert that their main statement or Jones unknot detection is false. It has not been externally reviewed or sent to the authors.

## Build

From this directory, run twice:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The source is a self-contained amsart document with an inline bibliography; no BibTeX or external figures are required. The compiled output is main.pdf.

## Mathematical certificate

The fixed host is the minimal three-crossing trefoil with the antiparallel seed of its twist-knot diagram marked. The odd-length residual family is the mirror of the rational closure with fraction (2L+1)/2, with chirality fixed by V_1 = x^2 + x^6 - x^8.

The exact degree is 2L+5, and the leading coefficient in the x-coordinate of the basis (1,x) over Z[p], p=x-x^{-1}, is -1. At L=23 this gives b_51=-1 against the asserted uniform cap 22. Proposition 5.12, Theorem 5.6 and Lemma 5.8 are tested as a combined universal package. Their conditional skein identity is not refuted, and no individual geometric submove is isolated as the unique failure.

The manuscript distinguishes the original host's crossing count from the residual diagram's L+2 crossings. The ordinary diagram degree bound 3L+6 remains compatible with the example.

## Exact reproduction

Standard-library arithmetic:

    python3 verify.py

This writes verification.json. It evaluates the closed formula at the five prescribed values L=1,3,5,7,23, extracts basis coefficients through a binomial formula, reconstructs the Laurent polynomial by substitution, and checks the skein identity. It does not search for examples.

Independent actual-diagram check:

    python3 diagram-check.py

This uses Spherogram and Regina. In this workspace the dependencies are available under work/braid_classification/packages; ordinary installations of those packages also work. The recorded run used Python 3.13.7, Spherogram 2.4.1 and Regina 7.4. The script constructs only those same five rational diagrams, takes the same mirror in each case, and compares Regina's exact Jones coefficients to the formula. No framing or monomial correction is applied after the mirror choice.

The diagram-check.json file records the full planar-diagram codes in both indexing conventions, crossing counts, component counts, raw outputs and zero coefficient differences. See diagram-check-notes.md for normalization details.

## Review material

- claim-review.md: fresh read of the source claims, their hypotheses and the scope of the contradiction.
- diagram-check-notes.md: independent reproduction from actual diagrams.
- verification.json and diagram-check.json: exact machine-readable results.

All Carmi–Cohen numbering is pinned to v1. The Garoufalidis–Zagier reference is the 87-page published version in SIGMA 20 (2024), 055; its pages 74 and 79 provide the initial normalization checks.

The author line and AI-collaboration disclosure follow Caleb's approved wording relayed in collab/msgs/20261103-215308-claude.md. No publication or external submission has been made.
