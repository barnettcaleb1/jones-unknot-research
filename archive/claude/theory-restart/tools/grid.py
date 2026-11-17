#!/usr/bin/env python3
"""Print the bullet-generators of BN~(T) in lattice coordinates (a,b): generator = rho + a D + b P, D=(1,2), P=(5,8) in (h,q).
h = a + 5b, q = 2a + 8b, delta = -b.  Rows: b (top = largest b = lowest delta); columns: a.  Entry = multiplicity; rho marked with *.
usage: grid.py FILE.jsonl NAME [NAME...]"""
import json,sys,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from gtilde import jset,valid
def ab(pts):
    q0,d0=pts[0]
    out=[]
    for q,d in pts:
        b=-(d-d0); a=(q-q0)//2-4*b
        out.append((a,b))
    return out
def show(name,khr):
    js=jset(khr)
    if js is None: print(name,'not standard'); return
    k,j,pts=js
    S=collections.Counter(ab(pts))
    A=[a for a,b in S]; B=[b for a,b in S]
    print('== %s  k=%d j=%d  dim N=%d'%(name,k,j,len(pts)))
    for b in range(max(B),min(B)-1,-1):
        row=''
        for a in range(min(A),max(A)+1):
            c=S.get((a,b),0)
            cell=('%d'%c if c<10 else '+') if c else '.'
            if (a,b)==(0,0): cell=cell+'*'
            else: cell=cell+' '
            row+=cell
        print('b=%3d  %s'%(b,row))
    print('       a from %d to %d'%(min(A),max(A)))
if __name__=='__main__':
    fn=sys.argv[1]; names=sys.argv[2:]
    for line in open(fn):
        try: r=json.loads(line)
        except: continue
        nm=(r.get('file') or r.get('knot') or r.get('word') or '')
        short=nm.split('/')[-1].replace('.kht','')
        if names and short not in names: continue
        khr=r.get('khr') or []
        if khr and valid(khr): show(short,khr)
