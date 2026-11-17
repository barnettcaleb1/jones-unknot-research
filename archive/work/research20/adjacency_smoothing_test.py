#!/usr/bin/env python3
"""Actual all-marked oriented smoothing of the audited Stoimenow K3 PD."""
import sys, json, itertools
from pathlib import Path
sys.path.insert(0,str(Path('work/braid_classification/packages').resolve()))
sys.path.insert(0,str(Path('work/cancellation19').resolve()))
from stoimenow_k3 import build
from spherogram import Link
import regina

pd=build().PD_code()
parent={x:x for c in pd for x in c}
def root(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]];x=parent[x]
    return x
for i in (33,35,37):
    c=pd[i]
    # Each marked negative crossing has incoming ports0,1. Hence the
    # oriented smoothing joins0 to3 and1 to2.
    for a,b in ((0,3),(1,2)):parent[root(c[a])]=root(c[b])
new=[[root(x) for x in c] for i,c in enumerate(pd)if i not in (33,35,37)]
S=Link(new)
assert len(S.link_components)==4

def record(T,expected_components):
    # sublink() silently discards isolated free circles; retain their count.
    missing=expected_components-len(T.link_components)-T.unlinked_unknot_components
    assert missing>=0
    initial=T.PD_code();initial_lk=T.linking_number()
    T.simplify(mode='global')
    free=T.unlinked_unknot_components+missing
    R=regina.Link.fromPD([tuple(x+1 for x in c)for c in T.PD_code()]) if T.crossings else regina.Link(free)
    if T.crossings:
        for _ in range(free):R.insertLink(regina.Link(1))
    j=R.jones()
    coeff={e:int(str(j[e]))for e in range(j.minExp(),j.maxExp()+1)if int(str(j[e]))}
    # Derivatives in logarithmic t-variable, so exponent in sqrt(t) /2.
    # Multiply the kth derivative by2^k to keep arithmetic integral.
    delta={-1:-1,1:-1}
    unlink={0:1}
    for _ in range(expected_components-1):
        q={}
        for e,a in unlink.items():
            for f,b in delta.items():q[e+f]=q.get(e+f,0)+a*b
        unlink={e:a for e,a in q.items()if a}
    moments=[sum(c*e**k for e,c in coeff.items())-sum(c*e**k for e,c in unlink.items())for k in range(8)]
    return {'initial_PD':initial,'simplified_PD':T.PD_code(),'free_unknots':free,'components':expected_components,'linking_number':initial_lk,'Jones_sqrt_t':str(j),'coefficients':coeff,'scaled_log_derivatives_of_unlink_defect':moments}

pairs={','.join(map(str,ids)):record(S.sublink(list(ids)),2)for ids in itertools.combinations(range(4),2)}
full=record(S.copy(),4)
out={'full':full,'pairs':pairs}
Path('work/research20/adjacency_smoothing_test.json').write_text(json.dumps(out,indent=2))
for ids,row in pairs.items():
    print(ids,len(row['simplified_PD']),row['free_unknots'],row['Jones_sqrt_t'],row['scaled_log_derivatives_of_unlink_defect'])
print('full',full['Jones_sqrt_t'],full['scaled_log_derivatives_of_unlink_defect'])
