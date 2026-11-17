#!/usr/bin/env python3
"""Referee's own kht++ runner and chain parser (independent of the author's chain.py/run.py).
usage: khtrun.py [-t SEC] WORD ...   WORD = string in Y,X,y,x (Y -> y0, y -> x0, X -> x1, x -> y1), half diagram s.l1.<...>.u2
Computes chi = sum over the b-generators (symbol U+2B2E) of BN~ of (-1)^h t^(q/2) directly from the printed chains and compares
with (1 0) rho(L_m)..rho(L_1) (1 0)^T up to a unit."""
import os, re, sys, subprocess, hashlib, json
from lp import *
K='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
W='/Users/calebbarnett/jones-lanes/theory-restart/mech2/verify/twobridge-proof/kht'
TOK={'Y':'y0','y':'x0','X':'x1','x':'y1'}
B='⬮'; C='⬯'
def halfdiagram(w): return 's.l1.'+'.'.join(TOK[L] for L in w)+'.u2' if w else 's.l1.u2'
def run(w,timeout=300,field='2'):
    name='r'+hashlib.md5((w+field).encode()).hexdigest()[:10]
    f='examples/mine/%s.kht'%name
    hd=halfdiagram(w)
    out=os.path.join(W,'examples/mine',name,'cxBNr-c%s-qs'%field)
    if not os.path.exists(out):
        open(os.path.join(W,f),'w').write('%% %s = %s\n%s\n,1\n'%(w,hd,hd))
        r=subprocess.run(['perl','-e','alarm %d; exec @ARGV'%timeout,K,'-c'+field,'-q','-s',f],cwd=W,capture_output=True,text=True,stdin=subprocess.DEVNULL)
        if not os.path.exists(out): return None,(r.stdout+r.stderr)[-400:]
    lines=[l for l in open(out,encoding='utf-8').read().splitlines() if l.strip() and not l.startswith('%')]
    return lines,None
ARROW=re.compile(r'(?P<fwd>(?:~~|——)?(?P<lab1>\(?-?\d*\.?[SD](?:\^\d+)?\)?)?(?:~>|—>))|(?P<bwd>(?:<~|<—)(?P<lab2>\(?-?\d*\.?[SD](?:\^\d+)?\)?)?(?:~~|——)?)')
def parse_chain(line):
    m=re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(.*)$',line)
    assert m, line
    h,q=int(m.group(1)),int(m.group(2)); body=m.group(4).strip()
    gens=[]; arrows=[]; pos=0
    while pos<len(body):
        ch=body[pos]
        if ch in (B,C): gens.append(ch); pos+=1; continue
        mm=ARROW.match(body,pos)
        assert mm, (body,pos,body[pos:pos+12])
        txt=mm.group(0)
        fwd=mm.group('fwd') is not None
        lab=mm.group('lab1') if fwd else mm.group('lab2')
        kind='S' if '~' in txt else 'D'
        if lab:
            assert (('S' in lab) == (kind=='S')) or True
            kind='S' if 'S' in lab else 'D'
            pw=re.search(r'\^(\d+)',lab); k=int(pw.group(1)) if pw else 1
        else: k=None
        arrows.append((fwd,kind,k)); pos=mm.end()
    cyclic=(len(arrows)==len(gens))
    n=len(gens); hq=[(h,q)]
    res=[]
    for i,(fwd,kind,k) in enumerate(arrows):
        x=gens[i]; y=gens[(i+1)%n]
        if k is None:
            if kind=='D': k=1
            else: k=1 if x!=y else 2
        # idempotent sanity: D^k keeps the idempotent, S^k changes it iff k odd
        if kind=='D': assert x==y,(line,i)
        else: assert (x!=y)==(k%2==1),(line,i)
        dq=2*k if kind=='D' else k
        ch,cq=hq[i]
        nxt=(ch+1,cq+dq) if fwd else (ch-1,cq-dq)
        if i+1<n: hq.append(nxt)
        else: assert nxt==hq[0], ('cyclic chain does not close up',line)
    return [(g,)+hq[i] for i,g in enumerate(gens)]
def chi_b(lines):
    J={}
    nb=0
    for l in lines:
        for g,h,q in parse_chain(l):
            if g==B:
                assert q%2==0; nb+=1
                J=add(J,mon(q//2,(-1)**(h%2)))
    return J,nb
def same_up_to_unit(p,q):
    if not p or not q: return p==q
    sh=min(p)-min(q); q1={e+sh:c for e,c in q.items()}
    return p==q1 or p=={e:-c for e,c in q1.items()}
if __name__=='__main__':
    args=sys.argv[1:]; timeout=300
    if args and args[0]=='-t': timeout=int(args[1]); args=args[2:]
    for w in args:
        w=re.sub(r'([YXyx])(\d+)',lambda m:m.group(1)*int(m.group(2)),w)
        lines,err=run(w,timeout)
        if lines is None: print(w,'NO OUTPUT',err); continue
        J,nb=chi_b(lines); Jm=Jword(w)
        print('%-14s %-40s dim N = %3d  chi_b = %s'%(w,halfdiagram(w),nb,dict(sorted(J.items()))))
        print('%-14s formula = %s   %s'%('',dict(sorted(Jm.items())),'MATCH up to unit' if same_up_to_unit(J,Jm) else ('MATCH with t->1/t ONLY' if same_up_to_unit(J,subs_inv(Jm)) else 'DIFFER')),flush=True)
