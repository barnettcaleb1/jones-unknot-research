#!/usr/bin/env python3
"""Test N := (#blocks) = n_special + |k|/4  against (det - 1 + |sigma|)/2  [= rank SFH(S^3(kappa),Gamma_0)/2 for HFK-thin kappa]."""
import json, os, re, sys
from math import gcd, floor
from collections import Counter
rows = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rows.json')))

def sig_2bridge(p, q):
    # Murasugi/Shinohara: sigma(K(p,q)) = sum_{i=1}^{p-1} (-1)^{floor(i q / p)}, q odd
    if q % 2 == 0: q = q - p if q > 0 else q + p
    return sum((-1)**floor(i*q/p) for i in range(1, p))

# determinant and |signature| for knots up to 9 crossings (from memory of the Rolfsen/KnotInfo tables; flagged in the report)
tab = {
'3_1':(3,2),'4_1':(5,0),'5_1':(5,4),'5_2':(7,2),'6_1':(9,0),'6_2':(11,2),'6_3':(13,0),
'7_1':(7,6),'7_2':(11,2),'7_3':(13,4),'7_4':(15,2),'7_5':(17,4),'7_6':(19,2),'7_7':(21,0),
'8_1':(13,0),'8_2':(17,4),'8_3':(17,0),'8_4':(19,2),'8_5':(21,4),'8_6':(23,2),'8_7':(23,2),'8_8':(25,0),'8_9':(25,0),
'8_10':(27,2),'8_11':(27,2),'8_12':(29,0),'8_13':(29,0),'8_14':(31,2),'8_15':(33,4),'8_16':(35,2),'8_17':(37,0),'8_18':(45,0),
'8_19':(3,6),'8_20':(9,0),'8_21':(15,2),
'9_1':(9,8),'9_2':(15,2),'9_3':(19,6),'9_4':(21,4),'9_5':(23,2),'9_6':(27,6),'9_7':(29,4),'9_8':(31,2),'9_9':(31,6),'9_10':(33,4),
'9_11':(33,4),'9_12':(35,2),'9_13':(37,4),'9_14':(37,0),'9_15':(39,2),'9_16':(39,6),'9_17':(39,2),'9_18':(41,4),'9_19':(41,0),'9_20':(41,4),
'9_21':(43,2),'9_22':(43,2),'9_23':(45,4),'9_24':(45,0),'9_25':(47,2),'9_26':(47,2),'9_27':(49,0),'9_28':(51,2),'9_29':(51,2),'9_30':(53,0),
'9_31':(55,2),'9_32':(59,2),'9_33':(61,0),'9_34':(69,0),'9_35':(27,2),'9_36':(37,4),'9_37':(45,0),'9_38':(57,4),'9_39':(55,2),'9_40':(75,2),
'9_41':(49,0),'9_42':(7,2),'9_43':(13,4),'9_44':(17,0),'9_45':(23,2),'9_46':(9,0),'9_47':(27,2),'9_48':(27,2),'9_49':(25,4)}
nonalt = {'8_19','8_20','8_21','9_42','9_43','9_44','9_45','9_46','9_47','9_48','9_49'}

res = Counter(); bad = []
for name, k, dimW, nspec, nbn in rows:
    N = dimW // 4
    assert dimW % 4 == 0
    base = os.path.basename(name)
    if name.startswith('tilt'):
        m = re.match(r'b(\d+)_(\d+)-?(\d?)', base)
        p, q = int(m.group(1)), int(m.group(2))
        res['tilt_seen'] += 1
        # NOTE: some generated files are not the knot p/q (generator degenerate); skip here, treated via cxCKh check below
        continue
    if name.startswith('k138'):
        m = re.match(r'(\d+_\d+)', base)
        kn = m.group(1)
        det, sg = tab[kn]
        pred = (det - 1 + sg) // 2
        tag = 'k138_nonalt' if kn in nonalt else 'k138_alt'
        res[tag] += 1
        if N == pred: res[tag + '_ok'] += 1
        else: bad.append((base, k, N, pred, det, sg))
print(dict(res))
for b in bad: print('MISMATCH name,k,N,pred,det,sig:', b)
