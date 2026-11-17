"""Cor 3.8 check: nested body B(w) (B(Y^a w')=y0^a.B(w'), B(X^b w')=r2.(x1)^b.B(w').u1) has vector rho(w)e1.
Compare J(s.r2.(y1)^m.B(w1)...B(wn).(y0)^e.u1) with norm(e1^T X^-m Y^e (rho(w1)e1 * ... )). Also the m=0 multiplicativity."""
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
from lp import *
rnd=random.Random(17)
def blocks(w):   # word over X,Y (and inverses x,y) -> list of (letter, exponent) blocks
    out=[]
    for ch in w:
        L,s=(ch.upper(), 1 if ch.isupper() else -1)
        if out and out[-1][0]==L: out[-1][1]+=s
        else: out.append([L,s])
    return [(L,e) for L,e in out if e]
def body(w):
    bl=blocks(w)
    def build(i):
        if i==len(bl): return []
        L,e=bl[i]
        if L=='Y': return [('y0' if e>0 else 'x0')]*abs(e)+build(i+1)
        return ['r2']+[('x1' if e>0 else 'y1')]*abs(e)+build(i+1)+['u1']
    return '.'.join(build(0))
def rword(L):
    return ''.join(rnd.choice('XxYy') for _ in range(L))
ok=bad=skip=0
for trial in range(120):
    n=rnd.choice([1,1,2,2,3]); ws=[rword(rnd.randint(1,5)) for _ in range(n)]
    m=rnd.randint(-3,3); e=rnd.randint(-2,2)
    bodies=[body(w) for w in ws]
    if any(b=='' for b in bodies): continue
    word='.'.join(['s','r2']+[('y1' if m>0 else 'x1')]*abs(m)+bodies+[('y0' if e>0 else 'x0')]*abs(e)+['u1'])
    Jw=J(word)
    if Jw is None: skip+=1; continue
    p=apply(ws[0])
    for w in ws[1:]: p=star(p,apply(w))
    p=apply('Y'*e if e>=0 else 'y'*(-e),p)
    F=normalize(close(-m,p))
    if F==Jw: ok+=1
    else: bad+=1; print('MISMATCH',word,ws,m,e)
print('nested-body necklaces: ok',ok,'bad',bad,'skip(not knot)',skip)
