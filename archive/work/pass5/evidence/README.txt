REN CORE: ALL FOUR-STRAND BRAIDS
31 October 2026

Result: for the explicit capped ten-crossing core T, every attached braid
beta in B4 gives annular bracket a(A) z^2+b(A) with a(A) nonzero.
The proof has no word-length or component-count restriction.
This does not prove general Jones unknot detection or exclude ordinary
Jones-one closures after substituting z=delta. No novelty claim is made.

Read tangle_all_braids_proof.txt or compile proof.tex for the full argument.

Reproduce the exact proof data (Python 3, standard library only):
  python3 -S tangle_all_braids_obstruction.py
This rebuilds the core from ten crossings; it reads no saved JSON data.
It uses tangle_core_stdlib.py and search.py in this directory.

Additional independent algebra checks:
  python3 -S braid_first_jet_audit.py
  python3 -S homology_all_braids_audit.py
The first rebuilds the raw 3x3 matrix from the saved TL4 element; the second
independently gauges that raw matrix. Their input is checked against the
from-crossings reconstruction by validate_search.py.

Validate the optional finite search (C++ compiler required):
  c++ -O3 -std=c++17 top_braid_search.cpp -o top_braid_search
  python3 -S validate_search.py
  ./top_braid_search 12
The last command regenerates top_braid_counts.json and top_braid_hits.txt.
It checks all 366210937 freely reduced words of length at most 12, of which
183771832 have knot closures. There were zero modular vanishing hits.
Words and knot-closure instances can describe the same knot; these are not
counts of distinct knots. The all-braid proof does not rely on this search.
The finite modulus is 1000000007 and A=2. A truly zero Laurent coefficient
would vanish at this modular specialization. The 128-word comparison is
an implementation check, not a replacement for the all-braid proof.

Internal algebra audits are not external peer review.
Source of the original construction:
https://arxiv.org/html/2609.11084v2

SHA256SUMS lists the original bytes of all files other than itself.
Reproduction scripts may rewrite their JSON output files.
