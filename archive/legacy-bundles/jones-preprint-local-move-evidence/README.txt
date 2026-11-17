This archive supports the local-move audit of Carmi–Cohen arXiv:2606.22410v1.
Start with outputs/jones-preprint-local-move-audit.txt.

The main certificate is reproducible using standard Python only:
  python3 work/research36/verify_g2_certificate.py
It exhaustively evaluates 128 smoothing states for each of three 7-crossing
closed diagrams and checks bracket spans 20, 4, 20 respectively.

The independent operator arithmetic can be reproduced with:
  python3 work/research36/verify_operator_growth.py
It uses the included outputs/verify_twist_obstruction.py.

source_machine.py records the port-level reconstruction, using the external
Spherogram and Regina packages if installed. It is not needed to run the
standalone exhaustive certificate. The remaining visual input is the map
from the source figures to the listed planar diagrams; machine_geometry.txt
explains this map explicitly. Agreement of arithmetic engines does not by
itself certify a visual transcription.

The two source images are audit excerpts from the arXiv source of the
cited preprint, included to permit that visual check. Source record:
https://arxiv.org/abs/2606.22410v1

These files identify a flaw in the proposed proof, not a solution of the
Jones unknot-detection problem. No priority or expert endorsement is claimed.
