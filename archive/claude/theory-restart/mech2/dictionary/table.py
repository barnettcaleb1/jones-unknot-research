#!/usr/bin/env python3
"""Table: N(K,h) (staircase, squares, rows) versus classical data of K (signature, s, Alexander polynomial) for the 138 inversions."""
import json, sys, os, re, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/dictionary')
import chains
from gtilde import jset, valid
ROOT='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138'
KN='/Users/calebbarnett/jones-lanes/theory-restart/mech2/dictionary/work/examples/kn'
def knot_data(folder):
    """s and Kh~ delta-distribution from cxCKh (knot mode)."""
    p=os.path.join(KN,folder,'cxCKh-c2-s')
    if not os.path.exists(p): return None
    s=None; kh=collections.Counter()
    for line in open(p):
        if line.startswith('%') or not line.strip(): continue
        c=chains.parse_chain(line.rstrip('\n'))
        if c is None: continue
        G=c['gens']
        if len(G)==1:
            s=G[0][2]; kh[(G[0][1],G[0][2])]+=1
        else:
            for g in G: kh[(g[1],g[2])]+=1
    dl=collections.Counter()
    for (h,q),m in kh.items(): dl[q//2-h]+=m
    # signature diagonal: sum (-1)^(delta-d0) dim = det >0 ; choose majority
    tot=sum(dl.values())
    best=max(dl,key=lambda d:dl[d])
    return dict(s=s,khdim=tot,dl=dict(dl),sigma=-2*best)
def analyse(name,folder,khr):
    js=jset(khr)
    if js is None: return None
    k,j,pts=js
    comps=chains.load(os.path.join(ROOT,'examples/si',folder,'cxBNr-c2-qs'))
    st=chains.structure(comps)
    g=st['gens']
    # rho: arc b-generator with absolute (h,q) = (8j+k, 24j+2k)
    tgt=(8*j+k,24*j+2*k)
    arc=st['arc']; idx=arc['idx']
    cand=[i for i in idx if (g[i][0],g[i][1])==tgt]
    ends=[idx[0],idx[-1]] if idx else []
    rho=None
    for i in ends:
        if (g[i][0],g[i][1])==tgt: rho=i
    if rho is None:
        return dict(name=name,err='rho not at an end: cand=%s ends=%s tgt=%s'%(cand,[(g[i][0],g[i][1]) for i in ends],tgt))
    x0=idx[0] if rho==idx[-1] else idx[-1]
    if len(idx)==1: x0=rho
    h0,q0,_=g[rho]
    def ab(i):
        dh=g[i][0]-h0; dq=g[i][1]-q0
        b=(2*dh-dq)//2; a=dh-5*b
        return (a,b)
    L=[ab(i) for i in range(len(g))]
    # arc path from rho to x0
    path=[L[i] for i in (idx if rho==idx[0] else idx[::-1])]
    # squares: cyclic comps with 4 b's
    squares=[]; odd=[]
    for ci,c in enumerate(comps):
        if not c['cyclic']: continue
        mem=[i for i in range(len(g)) if g[i][2]==ci]
        pts_=sorted(L[i] for i in mem)
        if len(pts_)==4 and pts_==[(pts_[0][0],pts_[0][1]),(pts_[0][0],pts_[0][1]+1),(pts_[0][0]+1,pts_[0][1]),(pts_[0][0]+1,pts_[0][1]+1)]:
            squares.append(pts_[0])
        else: odd.append(pts_)
    # staircase type
    steps=[(path[i+1][0]-path[i][0],path[i+1][1]-path[i][1]) for i in range(len(path)-1)]
    return dict(name=name,k=k,j=j,dim=len(g),arc=path,steps=steps,squares=sorted(squares),odd=odd,x0=L[x0],x0abs=(g[x0][0],g[x0][1]),
                other=st['other'],L=L,dDpow=[p for (_,_,p) in st['dD'] if p!=1],dPn=[p for (_,_,p) in st['dP'] if p!=2])
if __name__=='__main__':
    out=[]
    for line in open(os.path.join(ROOT,'k138.jsonl')):
        r=json.loads(line)
        name=r['file']; folder=name.replace('^','-')
        khr=r.get('khr') or []
        if not khr or not valid(khr):
            out.append(dict(name=name,err='invalid khr')); continue
        try:
            a=analyse(name,folder,khr)
        except Exception as e:
            a=dict(name=name,err=repr(e))
        if a is None: a=dict(name=name,err='jset none')
        kd=knot_data(folder)
        if kd: a.update(kd)
        out.append(a)
    json.dump(out,open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/dictionary/table.json','w'))
    errs=[a for a in out if 'err' in a]
    print('records',len(out),'errors',len(errs))
    for a in errs: print('  ',a['name'],a['err'])
