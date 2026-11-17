#!/usr/bin/env python3
"""Check Theorem A (J matrix formula) and Theorem B (non-monomial, extreme coefficients +-1) on all table entries whose
half-diagram is of the form s.[lr]1.(x0|y0|x1|y1)*.u2  (side-preserving two-bridge inversions)."""
import sys,os,glob,re,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import chain, run as R, jmatrix as JM
from jcheck import norm
base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/'
ok=0; bad=0; n=0; mixed=0
for f in sorted(glob.glob(base+'*.kht')):
    nm=os.path.basename(f)[:-4]
    word=open(f).read().split('\n')[1].strip()
    m=re.fullmatch(r's\.[lr]1\.((?:[xy][01]\.)*)u2',word)
    if not m: continue
    letters=[t for t in m.group(1).split('.') if t]
    fn=base+nm+'/cxBNr-c2-qs'
    if not os.path.exists(fn): continue
    # blocks: runs of y0/x0 (a, sign + for y0) then runs of x1/y1 (b, sign + for x1); allow sign changes inside by splitting
    seq=[]
    for t in letters:
        L={'y0':'Y','x0':'y','x1':'X','y1':'x'}[t]
        seq.append(L)
    v=(JM.ONE,JM.ZERO)
    for L in seq: v=JM.apply(JM.RHO[L],v)
    Jm=v[0]
    rec={'word':nm,'bn':[l for l in open(fn,encoding='utf-8').read().splitlines() if not l.startswith('%')]}
    an=R.analyse(rec); Jd=R.Jpoly(an)
    n+=1
    signs=set(L.isupper() for L in seq)
    if len(signs)==2: mixed+=1
    a=norm(Jd); b=norm(Jm)
    good=(a[0] in b) and len(Jm)>1 and abs(Jm[max(Jm)])==1 and abs(Jm[min(Jm)])==1
    if good: ok+=1
    else: bad+=1; print('MISMATCH',nm,word,Jd,dict(sorted(Jm.items())))
print('table entries of two-letter type:',n,'(mixed-sign words: %d)'%mixed,' Theorem A/B confirmed:',ok,' failures:',bad)
