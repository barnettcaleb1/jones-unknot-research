"""Exact all-parameter determinant certificate using reduced Burau at t=-1."""
from pathlib import Path
import json

def mm(a,b):return [[sum(a[i][k]*b[k][j]for k in range(2))for j in range(2)]for i in range(2)]
def inv(a):assert a[0][0]*a[1][1]-a[0][1]*a[1][0]==1;return[[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]
def U(x):return[[1,x],[0,1]]
def L(x):return[[1,0],[-x,1]]
def comm(a,b):return mm(mm(mm(a,b),inv(a)),inv(b))
def determinant(n):
 b=mm(comm(U(2*n),comm(L(2*(n-1)),U(2*(n-2)))),mm(U(1),L(1)))
 return abs(2-b[0][0]-b[1][1])
def formula(n):return abs(1+8*n*(n-1)*(n-2)*(8*(n-1)**2*(n-2)+6*n-8))
for n in range(-100,101):assert determinant(n)==formula(n)
raw=json.loads(Path(__file__).with_name('coupled_sampling.json').read_text())
for r in raw:assert determinant(r['n'])==r['determinant']
Path(__file__).with_suffix('.json').write_text(json.dumps({'integer_matrix_checks':201,'independent_Jones_determinant_checks':len(raw),'formula':'abs(1+8*n*(n-1)*(n-2)*(8*(n-1)^2*(n-2)+6*n-8))','nontrivial_for_every_n_ge':3},indent=2)+'\n')
print('201 matrix checks and',len(raw),'independent full Jones checks passed.')
