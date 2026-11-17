"""Finite diagram checks of the still-unproved central-power absorption.
These checks are NOT used in the determinant-factorization proof.
"""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'pass2'))
from watson_model import *
T=(RationalTangle(1,2)+RationalTangle(1,3)).rotate(1)
U=-T
rows=[]
for alpha in ([1],[1,2]*3+[1],[2,2,1,2,2],[1,2]*6+[2,2,1,2,2]):
    for n in (0,1):
        L=watson(alpha,T+RationalTangle(n),U+RationalTangle(-n))
        before=L.PD_code()
        L.simplify('global')
        pieces=L.deconnect_sum()
        row={'alpha':alpha,'n':n,'PD_before':before,'PD_after':L.PD_code(),
             'component_count':len(L.link_components),
             'connected_sum_pieces_PD':[x.PD_code() for x in pieces]}
        rows.append(row)
        assert len(pieces)==2 and [len(z.crossings) for z in pieces]==[5,5]
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Finite checks only; no universal isotopy proof','tangle':'rotate(1/2+1/3)','rows':rows},indent=2))
print('Eight checks gave two five-crossing connected summands; no general conclusion inferred.')
