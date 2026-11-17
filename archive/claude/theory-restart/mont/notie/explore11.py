from nt import *
from collections import Counter, defaultdict
from fractions import Fraction
seqs=normal_seqs(4,3)
def c2rat(p,end='top'):
    if end=='top': e=top(p); return Fraction(p.get(e-1,0),p[e])
    e=bot(p); return Fraction(p.get(e+1,0),p[e])
def state(s):
    st=None
    for i,m in enumerate(s):
        if i==0: st='R' if m>0 else 'S0'
        else:
            if m>0: st='R'
            elif m<=-2: st='S0'
            else: st='S0' if st=='R' else 'S'+str(int(st[1:])+1)
    return st
D=defaultdict(Counter)
for s in seqs:
    u=box(s); a,b=chan(u)
    key=(state(s), 'last', s[-1] if abs(s[-1])<=1 else ('+big' if s[-1]>0 else '-big'), 'prev', (s[-2] if len(s)>1 else None))
    D[(state(s),s[-1] if s[-1] in (1,-1) else ('>=2' if s[-1]>0 else '<=-2'))][(c2rat(a),c2rat(b))]+=1
for k in sorted(D,key=str):
    print(k, dict(D[k]))
