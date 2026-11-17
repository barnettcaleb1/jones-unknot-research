#!/usr/bin/env python3
"""Scan BN~ chain files for squares (compact components x -P-> . -D-> . <-P- . <-D- x) and look for
w-pairs {X, X+(1,0)} and v-w parallelograms {X, X+(1,0), X+(4,6), X+(5,6)} in (h,q) of the first corner."""
import sys,glob,re,collections,json
SQ='⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—'
LINE=re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S+)')
def squares_of(lines):
    sq=[]; other=0
    for l in lines:
        m=LINE.match(l)
        if not m: continue
        if m.group(4)==SQ: sq.append((int(m.group(1)),int(m.group(2))))
        else: other+=1
    return sq,other
def quads(sq):
    C=collections.Counter(sq); n=0; wp=0
    for (h,q),m in list(C.items()):
        if (h+1,q) in C: wp+=min(m,C[(h+1,q)])
    C2=collections.Counter(C); found=[]
    for (h,q) in sorted(C2):
        while C2[(h,q)]>0 and C2[(h+1,q)]>0 and C2[(h+4,q+6)]>0 and C2[(h+5,q+6)]>0:
            for k in ((h,q),(h+1,q),(h+4,q+6),(h+5,q+6)): C2[k]-=1
            found.append((h,q)); n+=1
    return wp,n,found
if __name__=='__main__':
    tot=collections.Counter()
    if sys.argv[1]=='files':
        seen=set()
        for f in glob.glob('/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/**/cxBNr-c2-qs',recursive=True):
            lines=open(f).read().splitlines()[1:]
            key=tuple(lines)
            if key in seen: continue
            seen.add(key)
            sq,other=squares_of(lines)
            wp,n,found=quads(sq)
            tot['tangles']+=1; tot['squares']+=len(sq); tot['w-pairs']+=wp; tot['quadruples']+=n
            if n: print('QUAD',f.split('out/')[1],len(sq),'squares',n,'quadruples at',found)
        print(dict(tot))
    else:
        for fn in sys.argv[1:]:
            for l in open(fn):
                r=json.loads(l)
                if 'dimN' not in r: continue
                sq,other=squares_of(r.get('bnchains',[]))
                wp,n,found=quads(sq)
                print(r['word'],'dimN',r['dimN'],'rank',r['hfk']['rank'],'drop',r['dimN']-r['hfk']['rank'],'squares',len(sq),'w-pairs',wp,'quadruples',n,found)
