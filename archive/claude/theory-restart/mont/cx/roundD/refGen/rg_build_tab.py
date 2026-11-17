"""precompute the certificate-search tables for the 7 fixed 3-row coefficient matrices (B-independent)"""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_gen as G
from fractions import Fraction as Fr
Z = (Fr(0),) * 4
for nm, rows, off0 in G.cases((Fr(0), Fr(0)), (Fr(0), Fr(0)), Z, Fr(1)):
    coeffs = tuple(tuple(Fr(x) for x in r[:4]) for r in rows)
    G.gtable(coeffs)
print('tables', len(G._gtab), {k: len(v) for k, v in G._gtab.items()})
G.dump_gtab('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/rg_gtab.pkl')
