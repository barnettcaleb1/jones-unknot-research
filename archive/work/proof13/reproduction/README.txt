Proof13 evidence, 2026-10-31. No generic proof or actual Jones-one knot.
Run from this archive's extracted root with Python3:
 python3 work/proof13/generic/cabling_bootstrap_check.py
 python3 work/proof13/homology/check_extension.py
 python3 work/proof13/homology/check_integral_extension.py
 python3 work/proof13/tangle/sign_certificate.py
 python3 work/proof13/tangle/whitehead_bridge_verify.py
These five entry points require only the standard library. Some rewrite
their JSON certificates; hashes describe the initial archived files.

Full proofs and audits are in work/proof13/{generic,homology,tangle}.
Optional actual-diagram regeneration requires Spherogram2.4.1 and Regina7.4.1;
packages are not bundled. See tangle/findings.txt. Stored PDs and exact Jones
coefficients are included. The earlier color3 R-matrix JSON is included as
an input to the independent Whitehead identity check; its original full
R-matrix reproduction is in the preceding proof12 evidence archive.
Source papers are linked in the notes and are not bundled.
