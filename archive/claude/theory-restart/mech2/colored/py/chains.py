#!/usr/bin/env python3
"""Parse kht++ chain files (cxBNr-*). Returns components: list of dicts
{cyclic:bool, gens:[(sym,h,q)], arrows:[(i,j,type,power)]} with arrow i->j meaning generator i maps to generator j."""
import re,sys
ANSI=re.compile(r'\x1b\[[0-9;]*[A-Za-z]')
HEAD=re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*)$')
def parse_chain(h0,q0,chain):
    chain=chain.strip()
    # drop trailing label like 's4(∞) ...' if present (Khr files)
    chain=re.split(r'\s{3,}',chain)[0]
    toks=re.split(r'([⬮⬯])',chain)
    # toks: '', sym, arrow, sym, arrow, ..., sym, (arrow or '')
    syms=[]; arrs=[]
    i=1
    assert toks[0]=='' , toks[:3]
    while i<len(toks):
        syms.append(toks[i]); 
        arrs.append(toks[i+1] if i+1<len(toks) else '')
        i+=2
    n=len(syms)
    cyclic = arrs[-1]!=''
    def info(a,s1,s2):
        fwd = a.endswith('>')
        bwd = a.startswith('<')
        assert fwd!=bwd, a
        typ = 'S' if '~' in a else 'D'
        m=re.search(r'\^(\d+)',a)
        if m: p=int(m.group(1))
        else:
            p = 2 if (typ=='S' and s1==s2) else 1
        if typ=='S' and not m: assert (s1==s2) == (p==2)
        if typ=='D': assert s1==s2, (a,s1,s2)
        return fwd,typ,p
    gens=[None]*n
    gens[0]=(syms[0],h0,q0)
    arrows=[]
    for i in range(n-1 if not cyclic else n):
        j=(i+1)%n
        fwd,typ,p=info(arrs[i],syms[i],syms[j])
        dq = p if typ=='S' else 2*p
        h,q=gens[i][1],gens[i][2]
        if fwd: hj,qj=h+1,q+dq
        else: hj,qj=h-1,q-dq
        if j==0:
            assert (hj,qj)==(gens[0][1],gens[0][2]), ('cyclic mismatch',hj,qj,gens[0])
        else:
            gens[j]=(syms[j],hj,qj)
        arrows.append((i,j,typ,p) if fwd else (j,i,typ,p))
    return dict(cyclic=cyclic,gens=gens,arrows=arrows)
def parse_file(fn):
    comps=[]
    for l in open(fn).read().splitlines():
        l=ANSI.sub('',l)
        m=HEAD.match(l)
        if not m: continue
        comps.append(parse_chain(int(m.group(1)),int(m.group(2)),m.group(4)))
    return comps
def bgens(comp):
    return [(h,q) for s,h,q in comp['gens'] if s=='⬮']
def lattice(fn):
    """return (rho, arc_pts, squares, other) in lattice coords (a,b) rel. rho; squares = list of lower-left corners"""
    comps=parse_file(fn)
    arcs=[c for c in comps if not c['cyclic']]
    assert len(arcs)==1, len(arcs)
    arc=arcs[0]
    bs=bgens(arc)
    # rho = b-generator adjacent to the tail of c's : arc starts or ends with c-run
    syms=[g[0] for g in arc['gens']]
    if syms[0]=='⬯' or (syms[0]=='⬮' and syms[-1]=='⬮' and len(bs)==len(syms)):
        rho=bs[0]
    else:
        rho=bs[-1]
    if syms[0]=='⬮' and syms[-1]=='⬯': rho=bs[-1]
    def ab(h,q):
        h-=rho[0]; q-=rho[1]
        # h=a+5b, q=2a+8b -> b=(2h-q)/2... solve: q-2h = -2b
        b2=2*h-q
        assert b2%2==0
        b=b2//2
        a=h-5*b
        return (a,b)
    arcpts=[ab(h,q) for h,q in bs]
    squares=[]; other=[]
    for c in comps:
        if not c['cyclic']: continue
        pts=sorted(ab(h,q) for h,q in bgens(c))
        if len(pts)==4:
            a0,b0=pts[0]
            if pts==sorted([(a0,b0),(a0+1,b0),(a0,b0+1),(a0+1,b0+1)]):
                squares.append((a0,b0)); continue
        other.append(pts)
    return rho,arcpts,squares,other
if __name__=='__main__':
    for fn in sys.argv[1:]:
        rho,arc,sq,other=lattice(fn)
        print(fn.split('/')[-2],'rho(h,q)=',rho,'arc',arc,'squares',sorted(sq),'other',other)
