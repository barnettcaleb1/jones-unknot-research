"""Independent polynomial-engine audit of both final survivors. Neither is valid."""
import contextlib,io,json,math,runpy,random
from pathlib import Path
out=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):engine=runpy.run_path('work/bio7/quiver_candidate.py')
lines=(out/'finalists.txt').read_text().strip().splitlines()
finalists=[]
for start in range(0,len(lines),8):
 header=lines[start].split();C=[list(map(int,row.split())) for row in lines[start+1:start+8]]
 H3=engine['colored'](C,2);H4=engine['colored'](C,3)
 E=engine['add']({0:1},engine['shift'](engine['habiro_factor'](4,2),3))
 residual=engine['add'](H4,{e:-v for e,v in E.items()})
 quotient,remainder=engine['divide'](residual,engine['habiro_factor'](4,3))
 derivatives=[sum(v*math.prod(range(e-k+1,e+1)) for e,v in H4.items()) for k in range(6)]
 assert derivatives==[1,0,0,0,4320,int(header[3])]
 assert remainder
 F={0:1}
 for n in (1,2,4,5):F=engine['mul'](F,{n:1,0:-1})
 assert H3==engine['add']({0:1},F)
 finalists.append({'warning':'Fails a necessary color-four Habiro condition; not a candidate knot series','C':C,'H3':H3,'H4':H4,'H4_derivatives':derivatives,'required_derivatives':[1,0,0,0,4320,86400],'exact_nonzero_Habiro_remainder':remainder})
# Independent check of the elementary H4 formula used in C++, versus the
# original general q-multinomial coefficient engine.
rng=random.Random(75643)
def direct_H4(C):
 P={};s=[(-1)**C[i][i] for i in range(7)]
 add=engine['add'];shift=engine['shift']
 for i in range(7):P=add(P,{3*C[i][i]:s[i]})
 for i in range(7):
  for j in range(7):
   if i!=j:P=add(P,shift({0:1,1:1,2:1},C[i][i]+2*C[i][j],s[j]))
 for i in range(7):
  for j in range(i+1,7):
   for k in range(j+1,7):P=add(P,shift({0:1,1:2,2:2,3:1},C[i][j]+C[i][k]+C[j][k],s[i]*s[j]*s[k]))
 return P
for t in range(20):
 C=[[0]*7 for _ in range(7)]
 for i in range(7):C[i][i]=int(i>=4)
 for i in range(7):
  for j in range(i+1,7):C[i][j]=C[j][i]=rng.randrange(12)
 assert direct_H4(C)==engine['colored'](C,3)
(out/'independent_audit.json').write_text(json.dumps({'formula_checks':20,'finalists':finalists},indent=2)+'\n')
print('Independent general coefficient engine verifies both failures and 20 direct-formula comparisons.')
