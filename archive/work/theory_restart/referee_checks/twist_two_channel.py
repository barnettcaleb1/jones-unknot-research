"""Three decisive initial values for a separately proved two-channel family.

No search. Uses the existing exact integer TL bracket implementation on the
specified halfword. Also checks the two tie values algebraically.
"""
import sys
import json
from pathlib import Path
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import flat_search as fs
import alex

def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items(): out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}

def shift(p,k,sign=1): return {e+k:sign*c for e,c in p.items()}
alpha={-3:1,-4:-1,-5:1}
beta={6:1,5:-1,2:-1,-4:1,-5:-1,-6:1}
def F(n): return add(shift(alpha,2*n),shift(beta,n,(-1 if n%2 else 1)))

out=[]
for n in (0,1,2):
    word='s.r1.x2.'+('y1.'*n)+'y0.r2.y0.y1.y0.y1.x2.u3.u1'
    half=alex.parse(word)
    assert alex.diagram(alex.symmetrize(half)) is not None
    y,x=fs.bracket_vector(half)
    u={}; fs.padd(u,y); fs.padd(u,fs.pdelta(x))
    u={e:c for e,c in u.items() if c}
    assert u=={0:1}
    assert all(e%4==0 for e in y)
    raw={e//4:c for e,c in y.items() if c}
    assert raw==F(n)
    val=sum(c*(-1 if e%2 else 1) for e,c in raw.items())
    der=sum(e*c*(-1 if (e-1)%2 else 1) for e,c in raw.items())
    assert (val,der)==(1,2*n-6)
    pref=shift(raw,2*n-6)
    out.append(dict(n=n,word=word,u=u,raw=raw,preferred=pref))

assert F(-1)=={1:1,4:1,5:-1}
assert F(9)=={3:-1,4:1,5:-1,11:1,13:1}
assert out[1]['preferred']=={-9:-1,-8:1,-6:-1,-5:1,-1:1,2:1,3:-1}
cert=dict(initial_values=out,ties={-1:F(-1),9:F(9)},
          alpha=alpha,beta=beta,
          scope='Three initial values plus two symbolic tie checks; all-n claim requires the skein proof.')
Path(__file__).with_suffix('.json').write_text(json.dumps(cert,indent=2)+'\n')
print('Exact initial values n=0,1,2 and both tie values verified; preferred n1 agrees with ce1.')
