"""Symbolic moments of the affine-exponent Jones equation, exact integers."""
import ren_jones_locus as r
from collections import defaultdict
import json
def plus(*ps):
    d=defaultdict(int)
    for p in ps:
        for e,c in p.items():d[e]+=c
    return {e:c for e,c in d.items() if c}
def mult(p,q):
    d=defaultdict(int)
    for e,c in p.items():
        for f,k in q.items():d[tuple(x+y for x,y in zip(e,f))]+=c*k
    return {e:c for e,c in d.items() if c}
def moment(poly,k):
    out={}
    for b,c in poly.items():
        linear={(0,0,0):b[3],(1,0,0):b[0],(0,1,0):b[1],(0,0,1):b[2]}
        power={(0,0,0):c}
        for _ in range(k):power=mult(power,linear)
        out=plus(out,power)
    return out
def show(p):
    return ' + '.join(str(c)+'*m^%s*l^%s*n^%s'%e for e,c in sorted(p.items())) or '0'
if __name__=='__main__':
    result={}
    for name,poly in [('G',r.poly),('Fa_A',r.fa)]:
        result[name]={}
        for k in range(5):
            p=moment(poly,k)
            result[name][str(k)]=[[*e,c]for e,c in sorted(p.items())]
            print(name,k,show(p))
    (r.ROOT/'ren_moments.json').write_text(json.dumps(result,indent=2))
