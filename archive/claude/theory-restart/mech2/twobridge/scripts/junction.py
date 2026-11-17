#!/usr/bin/env python3
"""JUNCTION FORMULA (conjectural closed formula for all side-preserving two-bridge inversions).
   Reduce the word (letters Y,y,X,x) by:  Yy,yY,Xx,xX -> empty;  YxY -> X, xYx -> y, XyX -> Y, yXy -> x  (centre ignored);
   leading X,x dropped; leading 'Yx' -> 'y', leading 'yX' -> 'Y';  trailing Y,y dropped.
   Then  P = (1 0) prod (matrices) (1 0)^T  with M_Y, M_X, Mt_y, Mt_x and each sign change pair replaced by
       J+- = [[1,1+y],[y/x^4,y/x^4]]            (for 'Yx' or 'Xy')
       J-+ = [[1,x^3(1+y)/y],[x/y,x^4/y]]       (for 'xY' or 'yX').
   Compare with the multiset N from kht++ chain files, up to translation."""
import sys,os,glob,re,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import chain, run as R
from hull_formula import hull,edges
def mm(p,m): return collections.Counter({(a+m[0],b+m[1]):v for (a,b),v in p.items()})
def add(*ps):
    r=collections.Counter()
    for p in ps:
        for k,v in p.items(): r[k]+=v
    return r
def step(v,L):
    v1,v2=v
    if L=='Y': return v1, add(mm(v1,(1,-1)),mm(v2,(1,-1)))
    if L=='X': return add(v1,v2,mm(v2,(0,1))), mm(v2,(1,0))
    if L=='y': return v1, add(mm(v1,(-4,1)),mm(v2,(-1,1)))
    if L=='x': return add(v1,mm(v2,(3,-1)),mm(v2,(3,0))), mm(v2,(-1,0))
    if L=='+-': return add(v1,v2,mm(v2,(0,1))), add(mm(v1,(-4,1)),mm(v2,(-4,1)))
    if L=='-+': return add(v1,mm(v2,(3,-1)),mm(v2,(3,0))), add(mm(v1,(1,-1)),mm(v2,(4,-1)))
RULES=[('Yy',''),('yY',''),('Xx',''),('xX',''),('YxY','X'),('xYx','y'),('XyX','Y'),('yXy','x')]
def reduce(w):
    while True:
        old=w
        for a,b in RULES: w=w.replace(a,b)
        w=re.sub(r'^[Xx]+','',w)
        w=re.sub(r'[Yy]+$','',w)
        if w.startswith('Yx'): w='y'+w[2:]
        if w.startswith('yX'): w='Y'+w[2:]
        if w==old: return w
def tokens(w):
    out=[]; i=0
    while i<len(w):
        if i+1<len(w) and w[i].isupper()!=w[i+1].isupper():
            out.append('+-' if w[i].isupper() else '-+'); i+=2
        else: out.append(w[i]); i+=1
    return out
def junction_poly(w):
    v=(collections.Counter({(0,0):1}),collections.Counter())
    for tk in tokens(w): v=step(v,tk)
    return v[0]
def same_up_to_shift(A,B):
    if sum(A.values())!=sum(B.values()): return False
    a0=min(A); b0=min(B)
    s=(b0[0]-a0[0],b0[1]-a0[1])
    return collections.Counter({(a+s[0],b+s[1]):c for (a,b),c in A.items()})==B
if __name__=='__main__':
    base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/'
    tot=ok=0; fails=[]
    items=[]
    for f in sorted(glob.glob(base+'*.kht')):
        nm=os.path.basename(f)[:-4]
        word=open(f).read().split('\n')[1].strip()
        m=re.fullmatch(r's\.[lr]1\.((?:[xy][01]\.)*)u2',word)
        fn=base+nm+'/cxBNr-c2-qs'
        if not m or not os.path.exists(fn): continue
        seq=''.join({'y0':'Y','x0':'y','x1':'X','y1':'x'}[t] for t in m.group(1).split('.') if t)
        bn=[l for l in open(fn,encoding='utf-8').read().splitlines() if not l.startswith('%')]
        items.append((nm,seq,bn))
    import json
    C=json.load(open(R.CACHE))
    for key,rec in C.items():
        w=key.split('|')[0]
        body=w[len('s.l1.'):-len('.u2')].split('.')
        if any(t not in ('y0','x0','x1','y1') for t in body) or rec.get('bn') is None: continue
        items.append(('mine:'+w,''.join({'y0':'Y','x0':'y','x1':'X','y1':'x'}[t] for t in body),rec['bn']))
    for nm,seq,bn in items:
        an=R.analyse({'word':nm,'bn':bn}); d=collections.Counter(an['N'])
        w=reduce(seq)
        Pj=junction_poly(w) if w else collections.Counter({(0,0):1})
        tot+=1
        if same_up_to_shift(Pj,d): ok+=1
        else: fails.append((nm,seq,w,sum(Pj.values()),sum(d.values())))
    print('words:',tot,' junction formula = N exactly (up to translation):',ok)
    for x in fails[:25]: print('  FAIL',x)
