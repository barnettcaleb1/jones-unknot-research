# Sikora rational-solution uniqueness manuscript

First complete internal-review draft, 3 November 2026.
Author: Caleb Barnett. No affiliation supplied.

## Files and build

- main.tex: self-contained amsart source with an embedded bibliography.
- main.pdf: compiled manuscript.
- surgery-review.md, floer-review.md, extension-and-sources-review.md:
  internal checks used in preparing this draft; not part of the paper.

Run from this directory:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

TeX Live 2022 compiles it with standard AMS, geometry, microtype, hyperref,
enumitem and array packages. No shell escape, external figures, bibliography
processor or private project dependencies are required. The source alone
is sufficient to reproduce the paper with these standard packages.

## Scope and review status

This is a draft deduction of the framed rational-solution conjecture,
with the unframed three-probe and arithmetic extensions. It is not a proof
of Jones unknot detection. The underlying argument has internal audits;
Claude's adversarial review of this complete manuscript is requested next.
There is no external specialist review or certified priority claim.
Nothing has been posted, submitted or sent outside the collaboration.

The author line, website and AI statement follow Caleb's instruction relayed
in collab/msgs/20261103-215308-claude.md. No affiliation or acknowledgments
have been invented.

## Source hierarchy and corrections

The audited proof in outputs/rational-tangle-uniqueness-audited-proof.txt
governs the mathematical argument; the subsequent corrective audit governs
where it identifies a specific error. In particular:

1. No step uses Sikora Proposition 10(1). The explicit counterexample is
   included only as a stress test; the longitudinal proof uses RR 7.8.
2. Stoimenow Proposition 6.5 is used for odd determinant iff knot, which is
   sufficient. The older attribution of a stronger divisibility theorem
   to that proposition is not repeated.
3. The Goeritz presentation including determinant zero is cited precisely
   to Lickorish's book Theorems 9.3–9.4 and Corollary 9.5.
4. The Casson–Walker formula is cited to the checked Ni–Wu restatement.
   No unchecked original Boyer–Lines theorem number is asserted.
5. Buck–Mauricio's journal title differs from its arXiv title. The bibliography
   records both and pins result numbers to the checked preprint.
6. The two-probe calibration is the mirror/reparametrization of
   Ernst–Sumners 1999 Example 3, not a new example or the 1990 calculus paper.
7. The surgery coefficient is a marked lifted-slope coordinate; it is not
   silently identified with the Conway fraction of the closing tangle.
8. RR and Sikora numbering is pinned to the specified arXiv versions.

The methods section credits Gainullin's surgery–Alexander strategy,
Rasmussen–Rasmussen's machinery, and classical special cases. The recent
IPAM abstract is evidence of that abstract's wording, not a priority proof.
