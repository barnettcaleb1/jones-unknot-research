#!/usr/bin/env python3
"""Parser for kht++ chain files (cxBNr-*).  Returns components = list of dicts:
   gens: list of (idem 'b'|'c', h, q);  arrows: list of (src_index, dst_index, type 'S'|'D', power);  cyclic: bool
   Conventions (lit/kht/REPORT.md 2.4): arrow x->y labelled S^k: h+1, q+k;  D^k: h+1, q+2k."""
import re,sys,collections
from fractions import Fraction as Fr
B='⬮'; C='⬯'
def parse_line(line):
    m=re.match(r'\s*(\d+)\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*\S*\^\s*(-?[\d/]+)\s*(.*)$',line)
    if not m: return None
    h0=int(m.group(2)); q0=int(m.group(3)); s=m.group(5).strip()
    # tokenise
    toks=[]; cur=''
    for ch in s:
        if ch in (B,C):
            if cur: toks.append(('a',cur)); cur=''
            toks.append(('g','b' if ch==B else 'c'))
        else: cur+=ch
    if cur.strip(): toks.append(('a',cur.strip()))
    gens=[t[1] for t in toks if t[0]=='g']
    n=len(gens)
    arrows=[]; gi=-1; cyclic=False
    for idx,(k,v) in enumerate(toks):
        if k=='g': gi+=1; continue
        left=gi; right=gi+1
        if right>=n: right=0; cyclic=True
        fwd=v.endswith('>'); bwd=v.startswith('<')
        assert fwd!=bwd, v
        typ='S' if '~' in v else 'D'
        pm=re.search(r'\^(\d+)',v)
        if pm: p=int(pm.group(1))
        elif typ=='S': p=1 if gens[left]!=gens[right] else 2
        else: p=1
        if 'S' in v and typ!='S': raise ValueError(v)
        if fwd: arrows.append((left,right,typ,p))
        else: arrows.append((right,left,typ,p))
    # gradings
    hq=[None]*n; hq[0]=(h0,q0)
    # arrows in order connect i and i+1
    for (s_,d_,typ,p) in arrows:
        dq=p if typ=='S' else 2*p
        if hq[s_] is not None and hq[d_] is None: hq[d_]=(hq[s_][0]+1,hq[s_][1]+dq)
        elif hq[d_] is not None and hq[s_] is None: hq[s_]=(hq[d_][0]-1,hq[d_][1]-dq)
        elif hq[s_] is not None and hq[d_] is not None:
            assert hq[d_]==(hq[s_][0]+1,hq[s_][1]+dq),('inconsistent',line)
    return dict(gens=[(g,)+hq[i] for i,g in enumerate(gens)],arrows=arrows,cyclic=cyclic)
def parse_file(fn):
    comps=[]
    for line in open(fn,encoding='utf-8'):
        if line.startswith('%'): continue
        c=parse_line(line)
        if c: comps.append(c)
    return comps
def bmoves(comp):
    """sequence of b-generators along the component and the moves between consecutive ones.
    move = (direction +1/-1 relative to traversal, word) where word is e.g. 'D','D2','P2' (S(DS2)^(n-1)DS), or raw label string."""
    gens=comp['gens']; n=len(gens)
    arr={}
    for (s,d,t,p) in comp['arrows']:
        arr[(s,d)]=(t,p)
    def step(i,j):
        if (i,j) in arr: return (+1,)+arr[(i,j)]
        if (j,i) in arr: return (-1,)+arr[(j,i)]
        return None
    bidx=[i for i,g in enumerate(gens) if g[0]=='b']
    moves=[]
    pairs=list(zip(bidx,bidx[1:]))
    if comp['cyclic'] and len(bidx)>=1: pairs.append((bidx[-1],bidx[0]+n))
    for (i,j) in pairs:
        steps=[step(k%n,(k+1)%n) for k in range(i,j)]
        dirs=set(s[0] for s in steps)
        lab=''.join(('%s%s'%(s[1],s[2] if s[2]>1 else '')) for s in (steps if steps[0][0]>0 else steps[::-1]))
        d=steps[0][0] if len(dirs)==1 else 0
        moves.append((d,lab))
    return [gens[i] for i in bidx],moves
def short(lab):
    if re.fullmatch(r'D\d*',lab): return lab
    m=re.fullmatch(r'SD((S2D)*)S',lab)
    if m: return 'P%d'%(1+len(m.group(1))//3)
    return '['+lab+']'
def tail(comp):
    """for an arc: the c-part at the ends (lists of labels before first b and after last b)"""
    gens=comp['gens']; n=len(gens)
    bidx=[i for i,g in enumerate(gens) if g[0]=='b']
    return bidx[0], n-1-bidx[-1]
if __name__=='__main__':
    for fn in sys.argv[1:]:
        comps=parse_file(fn)
        print(fn)
        for c in comps:
            bg,mv=bmoves(c)
            print('  ','cyclic' if c['cyclic'] else 'arc   ','nb=%d'%len(bg),'ends(c-lengths)=%s'%(tail(c),) if not c['cyclic'] else '',
                  ' '.join(('+' if d>0 else '-' if d<0 else '?')+short(l) for d,l in mv), ' first b at',bg[0][1:] if bg else None)
