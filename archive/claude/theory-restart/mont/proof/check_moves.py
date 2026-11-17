"""Spot checks for the PROOF lane (cheap, exact). Run from mont/ folder."""
import sys, random, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *
import flat_search as fs
def tw(m,a='y',b='x'): return ([(a if m>0 else b)+'1']*abs(m))
def jn(*parts):
    w=[]
    for p in parts:
        if isinstance(p,str): w+= [x for x in p.split('.') if x]
        else: w+=p
    return '.'.join(w)
def Rrev(B):
    """pi-rotation about a horizontal line: reverse word, caps<->cups, crossings unchanged"""
    out=[]
    for tok in reversed(B.split('.')):
        c,i=tok[0],tok[1:]
        if c in 'lr': out.append('u'+i)
        elif c=='u': out.append('r'+i)
        else: out.append(tok)
    return '.'.join(out)
def row(j,ch='y'):
    return '.'.join(['r1']*j+[ch+'0']+[ch+str(2*i) for i in range(1,j+1)]+['u1']*j)
rnd=random.Random(3)
bodies=[]
while len(bodies)<25:
    w=fs.gen(rnd,rnd.randint(4,11))
    if w is None: continue
    B=w[2:]
    if J('s.'+B) is None: continue
    bodies.append(B)
bodies += [row(1),row(2),row(3),row(1,'x'),row(2,'x')]
Ws=['', 'y1', 'x1.x1', 'y0', 'y0.x1', 'x0.y1.y1', 'y1.y0.x1.x0']
stats={}
def rec(k,ok): stats.setdefault(k,[0,0]); stats[k][0 if ok else 1]+=1
for B in bodies:
    for m in (-2,-1,0,1,2,3):
        # Claim C: necklace word == TH-2BR closure of l1.B.(y1)^m
        a=J(jn('s.r2',tw(m),B,'u1')); b=J(jn('s.l1',B,tw(m),'u2'))
        if a is not None and b is not None: rec('claimC',a==b)
    for W in Ws:
        # R-invariance of box states
        a=J(jn('s.l1',B,W,'u2')); b=J(jn('s.l1',Rrev(B),W,'u2'))
        if a is not None and b is not None: rec('R-invariance',a==b)
        # folding lemma: [l1.r2.(x1)^m.B.u1] = X^m [l1.B]
        for m in (-2,-1,1,2):
            a=J(jn('s.l1.r2',tw(m,'x','y'),B,'u1',W,'u2')); b=J(jn('s.l1',B,tw(m,'x','y'),W,'u2'))
            if a is not None and b is not None: rec('folding',a==b)
for j in range(0,4):
    for W in Ws:
        for ch,och in (('y','x'),('x','y')):
            a=J(jn('s.l1',row(j+1,ch),W,'u2')); b=J(jn('s.l1.r2',och+'1',row(j,ch),'u1',W,'u2'))
            if a is not None and b is not None: rec('row-recursion',a==b)
            # row vector X^j Y e1 against TH-2BR word l1.y0.(x1)^j
            lt=(ch+'0') if True else ''
            c=J(jn('s.l1',row(j,ch),W,'u2')); d=J(jn('s.l1',lt,[(och+'1')]*j,W,'u2'))
            if c is not None and d is not None: rec('row=Y-then-X^j',c==d)
# cap-slide relation r_k.y_{k+1} = r_{k+1}.x_k inside random contexts
for B in bodies[:10]:
    for W in Ws[:4]:
        a=J(jn('s.l1.r1.y2.u1',B,W,'u2')); b=J(jn('s.l1.r2.x1.u1',B,W,'u2'))
        if a is not None and b is not None: rec('capslide',a==b)
print(stats)
json.dump(bodies,open('/Users/calebbarnett/jones-lanes/theory-restart/mont/proof/check_bodies.json','w'))
