#!/usr/bin/env python3
"""Parse kht++ cxBNr chain files into N(T) with its Lambda-structure.
Returns for each component: list of generators (sym,h,q) and list of arrows (i -> j, label, power).
N = b-generators (sym '⬮').  Moves between consecutive b-generators along a component:
  D^a : direct arrow of label D^a between b's      (h,q) += (1,2a)
  P_n : S (D S^2)^(n-1) D S through c-generators   (h,q) += (2n+1,4n)
"""
import re, sys, os, json, collections
from fractions import Fraction as Fr
GEN='⬮⬯'
HEAD=re.compile(r'^\s*(\d+)\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S+)')
def parse_arrow(tok,a,b):
    """tok between generator symbols a (left) and b (right). returns (direction, letter, power): direction +1 = left->right"""
    if tok.endswith('>'): d=+1
    elif tok.startswith('<'): d=-1
    else: raise ValueError('arrow? '+tok)
    m=re.search(r'([SDH])(?:\^(\d+))?',tok)
    if m:
        letter=m.group(1); power=int(m.group(2) or 1)
    else:
        if '—' in tok: letter,power='D',1
        elif '~' in tok: letter='S'; power=2 if a==b else 1
        else: raise ValueError('arrow? '+tok)
    return d,letter,power
def parse_chain(line):
    m=HEAD.match(line)
    if not m: return None
    h=int(m.group(2)); q=int(m.group(3)); chain=m.group(5)
    # split into generators and arrows
    gens=[]; arrows=[]; cur=''
    for ch in chain:
        if ch in GEN:
            if gens: arrows.append(cur)
            elif cur: raise ValueError('leading arrow')
            cur=''; gens.append(ch)
        else: cur+=ch
    cyclic=bool(cur)
    n=len(gens)
    G=[None]*n; G[0]=(gens[0],h,q)
    A=[]
    for i,tok in enumerate(arrows):
        d,letter,power=parse_arrow(tok,gens[i],gens[i+1])
        dq=power*(2 if letter in 'DH' else 1)
        s,hh,qq=G[i]
        if d>0: G[i+1]=(gens[i+1],hh+1,qq+dq); A.append((i,i+1,letter,power))
        else:   G[i+1]=(gens[i+1],hh-1,qq-dq); A.append((i+1,i,letter,power))
    if cyclic:
        d,letter,power=parse_arrow(cur,gens[-1],gens[0])
        dq=power*(2 if letter in 'DH' else 1)
        s,hh,qq=G[-1]
        if d>0:
            assert (hh+1,qq+dq)==(G[0][1],G[0][2]),('cyclic grading mismatch',line)
            A.append((n-1,0,letter,power))
        else:
            assert (hh-1,qq-dq)==(G[0][1],G[0][2]),('cyclic grading mismatch',line)
            A.append((0,n-1,letter,power))
    return dict(gens=G,arrows=A,cyclic=cyclic)
def moves(comp):
    """sequence of b-generators along the component with the moves between consecutive ones.
    returns (blist [(idx,h,q)], movelist [(i_from,i_to,kind,n)] in terms of positions in blist, tail info)"""
    G=comp['gens']; n=len(G)
    bidx=[i for i,g in enumerate(G) if g[0]=='⬮']
    out=[]
    # arrows between consecutive chain positions: build map (min(i,j)) -> arrow for linear part
    amap={}
    for (i,j,l,p) in comp['arrows']:
        key=(min(i,j),max(i,j)) if not (comp['cyclic'] and {i,j}=={0,n-1} and n>2) else ('wrap',)
        amap[key]=(i,j,l,p)
    def seg(i0,i1,wrap=False):
        """arrows along the chain from position i0 to i1 (consecutive b's)"""
        seq=[]
        if not wrap:
            for t in range(i0,i1): seq.append(amap[(t,t+1)]+(t,))
        else:
            for t in range(i0,n-1): seq.append(amap[(t,t+1)]+(t,))
            seq.append(amap[('wrap',)]+(n-1,))
            for t in range(0,i1): seq.append(amap[(t,t+1)]+(t,))
        return seq
    def classify(seq):
        # all arrows must point the same way
        dirs=set()
        for (i,j,l,p,t) in seq:
            fwd = (i==t)  # arrow goes from position t to the next
            dirs.add(fwd)
        if len(dirs)!=1: return ('mixed',0,None)
        fwd=dirs.pop()
        labs=[(l,p) for (i,j,l,p,t) in seq]
        if not fwd: labs=labs[::-1]
        if len(labs)==1 and labs[0][0]=='D': return ('D',labs[0][1],fwd)
        # P_n = S (D S^2)^(n-1) D S
        if labs[0]==('S',1) and labs[-1]==('S',1) and len(labs)%2==1:
            mid=labs[1:-1]; ok=True; k=0
            # pattern D S2 D S2 ... D
            for t,(l,p) in enumerate(mid):
                if t%2==0:
                    if (l,p)!=('D',1): ok=False
                else:
                    if (l,p)!=('S',2): ok=False
            if ok and len(mid)%2==1: return ('P',(len(mid)+1)//2,fwd)
        return ('other',labs,fwd)
    mv=[]
    for a in range(len(bidx)-1):
        kind,nn,fwd=classify(seg(bidx[a],bidx[a+1]))
        mv.append((a,a+1,kind,nn,fwd))
    if comp['cyclic'] and len(bidx)>=1:
        kind,nn,fwd=classify(seg(bidx[-1],bidx[0],wrap=True))
        mv.append((len(bidx)-1,0,kind,nn,fwd))
    bl=[(i,G[i][1],G[i][2]) for i in bidx]
    # tails (non-cyclic): the c-runs before the first b and after the last b
    tails=None
    if not comp['cyclic']:
        head=bidx[0] if bidx else n; tail=n-1-(bidx[-1] if bidx else -1)
        tails=(head,tail)
    return bl,mv,tails
def load(path):
    comps=[]
    for line in open(path):
        if line.startswith('%') or not line.strip(): continue
        c=parse_chain(line.rstrip('\n'))
        if c: comps.append(c)
    return comps
def structure(comps):
    """Return dict with N generators [(h,q,comp,pos)], d_D arrows, d_P arrows, arc info"""
    gens=[]; dD=[]; dP=[]; other=[]; arc=None
    for ci,c in enumerate(comps):
        bl,mv,tails=moves(c)
        base=len(gens)
        for (i,h,q) in bl: gens.append((h,q,ci))
        for (a,b,kind,nn,fwd) in mv:
            src,dst=(base+a,base+b) if fwd else (base+b,base+a)
            if kind=='D': dD.append((src,dst,nn))
            elif kind=='P': dP.append((src,dst,nn))
            else: other.append((base+a,base+b,kind,nn))
        if not c['cyclic']:
            # rho = the b-generator adjacent to the longer c-tail (tail carrying slope k); if no tail, either end
            head,tail=tails
            if arc is not None: raise ValueError('two arcs')
            if len(bl)==0: arc=dict(comp=ci,nb=0,rho=None,x0=None,tails=tails,idx=[])
            else:
                if tail>=head: rho=base+len(bl)-1; x0=base
                else: rho=base; x0=base+len(bl)-1
                arc=dict(comp=ci,nb=len(bl),rho=rho,x0=x0,tails=tails,idx=list(range(base,base+len(bl))))
    return dict(gens=gens,dD=dD,dP=dP,other=other,arc=arc,ncomp=len(comps))
def lattice(st):
    """(a,b) coordinates relative to rho"""
    g=st['gens']; r=st['arc']['rho']
    h0,q0,_=g[r]
    out=[]
    for (h,q,ci) in g:
        dh=h-h0; dq=q-q0
        # h = a+5b, q = 2a+8b  ->  b = (2h - q)/2 , a = h - 5b
        assert (2*dh-dq)%2==0,(dh,dq)
        b=(2*dh-dq)//2; a=dh-5*b
        out.append((a,b))
    return out
if __name__=='__main__':
    for p in sys.argv[1:]:
        comps=load(p); st=structure(comps)
        L=lattice(st)
        print(p); print(' gens',len(st['gens']),'arc',st['arc']); print(' lattice',L)
        print(' dD',st['dD']); print(' dP',st['dP']); print(' other',st['other'])
