"""Two knots with equal Jones and unequal actual untwisted Whitehead-double Jones.
Demonstrates the polynomial information loss in the strong-inversion reduction.
"""
from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]/'braid_classification/packages'))
from spherogram import Link
import regina

def coeff(J):return {e:int(str(J[e])) for e in range(J.minExp(),J.maxExp()+1) if int(str(J[e]))}
rows=[]
for name in ['5_1','10_132']:
 L=Link(name)
 R=regina.Link.fromPD([tuple(v+1 for v in row)for row in L.PD_code()])
 v=coeff(R.jones())
 if rows and v!=rows[0]['Jones_x']:
  R.reflect();v=coeff(R.jones())
  assert v==rows[0]['Jones_x'],'Need different orientation/chirality convention'
 W=R.whiteheadDouble(True)
 W.simplify()
 j=coeff(W.jones())
 C=R.parallel(2)
 C.simplify()
 c=coeff(C.jones())
 row={'knot':name,'PD_1based':R.pdData(),'Jones_x':v,'Whitehead_PD_1based':W.pdData(),'Whitehead_Jones_x':j,'Seifert_parallel_PD_1based':C.pdData(),'Seifert_parallel_Jones_x':c}
 rows.append(row)
 print(name,'J=',v,'Wh size',W.size(),'Wh span',min(j),max(j),'cable span',min(c),max(c),flush=True)
assert rows[0]['Jones_x']==rows[1]['Jones_x']
assert rows[0]['Whitehead_Jones_x']!=rows[1]['Whitehead_Jones_x']
assert rows[0]['Seifert_parallel_Jones_x']!=rows[1]['Seifert_parallel_Jones_x']
(ROOT/'quotient_response_test.json').write_text(json.dumps(rows,indent=2))
print('PASSED equal ordinary Jones, unequal Whitehead and 2-parallel Jones')
