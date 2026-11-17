"""One fixed W3 marked-family calibration, not a word search."""
from pathlib import Path
import json
import sys
from fractions import Fraction
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp
import kauffman

def inverse(word):
    return ''.join(c.swapcase() for c in reversed(word))
word='YY'
for _ in range(3):
    word='X'+word+'x'+inverse(word)
letters={'X':'x1','x':'y1','Y':'y0','y':'x0'}
halfword='s.l1.'+'.'.join(letters[c] for c in reversed(word))+'.u2'
J=lp.J(halfword)
moments=[sum(c*(-1)**(e%2)*e**k for e,c in J.items()) for k in range(5)]
assert moments==[1,0,0,0,288]
B=kauffman.bracket(halfword)
residue=min(B)%4
assert all((e-residue)%4==0 for e in B)
V={-(e-residue)//4:c for e,c in B.items()}
sign=sum(V.values())
assert sign in (-1,1)
V={e:c*sign for e,c in V.items()}
shift=sum(e*c for e,c in V.items())
V={e-shift:c for e,c in V.items()}
d2=sum(c*e*(e-1) for e,c in V.items())
d3=sum(c*e*(e-1)*(e-2) for e,c in V.items())
a2=Fraction(-d2,6)
v3=Fraction(-d3-3*d2,36)
determinant=abs(sum(c*(-1)**(e%2) for e,c in V.items()))
assert a2==0 and v3==0 and determinant==217345
result={'matrix_word':word,'halfword':halfword,'J':J,'moments':moments,
        'covering_knot_Jones':V,'a2':str(a2),'v3':str(v3),'determinant':determinant}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('W3 fixed check passed: moments',moments,'determinant',determinant,'a2',a2,'v3',v3)
