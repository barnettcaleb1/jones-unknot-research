"""Fixed exact certificate for the recursive deep strong-inversion family."""
import json, sys
from pathlib import Path
import sympy as S
h=S.symbols('h')
A=S.Matrix([[0,-4],[0,1]])
B=S.Matrix([[0,0],[-3,-6]])
C1=A*B-B*A
C2=A*C1-C1*A
assert C1==S.Matrix([[12,24],[-3,-12]])
assert C2==S.Matrix([[12,72],[-3,-12]])
assert A*C2-C2*A==C1
assert C1[0,0]==C2[0,0]==12
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp
inv=lambda w: ''.join(c.swapcase() for c in w[::-1])
convert={'X':'x1','x':'y1','Y':'y0','y':'x0'}
word='YY'
rows=[]
for r in (1,2):
    word='X'+word+'x'+inv(word)
    halfword='s.l1.'+'.'.join(convert[c] for c in word[::-1])+'.u2'
    matrix_entry=lp.apply(word)[0]
    actual=lp.J(halfword)
    assert actual==matrix_entry
    moments=[sum(c*(-1)**(e%2)*e**k for e,c in actual.items()) for k in range(r+2)]
    assert moments==[1]+[0]*r+[12*S.factorial(r+1)]
    rows.append(dict(r=r,matrix_word=word,halfword=halfword,J=actual,moments=moments))
result=dict(ad_cycle=[list(C1),list(C2)],fixed_diagrams=rows,
            proof='ad_A alternates C1,C2, each with entry11=12; gives every r>=1.')
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2,default=int)+'\n')
print('Exact ad-cycle and two fixed marked diagram calibrations passed; wrote',out)
