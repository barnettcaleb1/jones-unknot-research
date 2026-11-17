#!/usr/bin/env python3
"""Direct test of Lemma Q on half-diagram words, by Kauffman bracket only (no homology).
For a strongly invertible knot given by 's.<half diagram>', build the quotient tangle as kht++ does (Tangle::quotient, without the
framing twists) and compute its bracket vector  [T] = y [b] + x [c]  (b = Q_0 joins the special top end to b3, c joins it to b1).
T is flat (all K_n have trivial Jones polynomial)  <=>  y is a monomial (framing independent)  <=>  J is a unit.
Sanity: u = y + delta x must be a monomial (T(infinity) = unknot).
usage: flat_search.py SEED COUNT MAXLEN OUT.txt"""
import sys,random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex,kauffman
from kauffman import padd,pshift,pdelta
def quotient_word(half):
    w=[('r',1),('r',2)]
    for c,s in half:
        if c in 'xy':
            if s==0: w+=[(c,0),(c,1),(c,1),(c,0)]
            else: w+=[(c,2*s),(c,2*s-1),(c,2*s+1),(c,2*s)]
        elif c in 'lr': w+=[(c,2*s-1),(c,2*s)]
        elif c=='u': w+=[(c,2*s),(c,2*s-1)]
    w.append(('u',0))
    return w
# states: tuple m of length W+1; index 0 = the top end T, indices 1..W = current strands (position p -> index p+1); m[i] = partner
def cap(m,i):          # insert matched pair at strand positions i,i+1  (indices i+1,i+2)
    j=i+1
    m2=[(x+2 if x>=j else x) for x in m]
    m2[j:j]=[j+1,j]
    return tuple(m2)
def cup(m,i):
    j=i+1
    p,q=m[j],m[j+1]
    m=list(m); loop=False
    if p==j+1: loop=True
    else: m[p]=q; m[q]=p
    del m[j:j+2]
    m=[(x-2 if x>j+1 else x) for x in m]
    return tuple(m),loop
def bracket_vector(half):
    w=quotient_word(half)
    state={(1,0):{0:1}}      # top end T (index 0) matched with strand 0 (index 1)
    for c,i in w:
        new={}
        for m,p in state.items():
            W=len(m)-1
            if c in 'lr':
                if i>W: return None
                padd(new.setdefault(cap(m,i),{}),p)
            elif c=='u':
                if i+1>=W: return None
                m2,loop=cup(m,i)
                padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                if i+1>=W: return None
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=cup(m,i)
                q=pdelta(p) if loop else p
                padd(new.setdefault(cap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    # final: W = 3 ; b: T-b3 (index 0 with 3), 1-2 ; c: T-b1 (0 with 1), 2-3
    yb=state.get((3,2,1,0),{}); xc=state.get((1,0,3,2),{})
    if set(state)-{(3,2,1,0),(1,0,3,2)}: return None
    return yb,xc
def is_monomial(p): return len(p)==1
def reduced(word):
    out=[]
    for l in word:
        if out and out[-1][1:]==l[1:] and out[-1][0]!=l[0]: out.pop()
        else: out.append(l)
    return out
def gen(rnd,L):
    r=rnd.random()
    if r<0.5:
        w=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(L)])
        return 's.'+rnd.choice(['l1','r1'])+'.'+'.'.join(w)+'.'+rnd.choice(['u1','u2']) if w else None
    a=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(rnd.randint(1,max(1,L//2)))])
    b=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2,3,4])) for _ in range(rnd.randint(2,L//2+2))])
    c=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(rnd.randint(0,L//2))])
    if not a or not b: return None
    return 's.'+rnd.choice(['l1','r1'])+'.'+'.'.join(a)+'.'+rnd.choice(['l1','r1','l2','r2','l3','r3'])+'.'+'.'.join(b)+'.'+rnd.choice(['u1','u2','u3'])+('.'+'.'.join(c) if c else '')+'.'+rnd.choice(['u1','u2'])
def main():
    seed,count,maxlen,outp=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
    rnd=random.Random(seed); seen=set(); stats={'tried':0,'knots':0,'nontrivial':0,'flat':0,'unitfail':0,'extreme_not_pm1':0}
    fo=open(outp,'a')
    for it in range(count):
        w=gen(rnd,rnd.randint(4,maxlen))
        if not w or w in seen: continue
        seen.add(w); stats['tried']+=1
        half=alex.parse(w)
        full=alex.symmetrize(half)
        if full is None or alex.diagram(full) is None: continue
        stats['knots']+=1
        kb=kauffman.bracket(w)
        if kb is None or len(kb)==1: continue           # unknot by Jones (or failure)
        stats['nontrivial']+=1
        bv=bracket_vector(half)
        if bv is None: continue
        y,x=bv
        u={}; padd(u,y); padd(u,pdelta(x))
        if not is_monomial(u): stats['unitfail']+=1; fo.write('UNITFAIL\t%s\n'%w); continue
        if is_monomial(y):
            stats['flat']+=1; fo.write('FLAT\t%s\t%s\n'%(w,sorted(y.items())))
        else:
            hi=y[max(y)]; lo=y[min(y)]
            if abs(hi)!=1 or abs(lo)!=1:
                stats['extreme_not_pm1']+=1; fo.write('EXT\t%s\t%d\t%d\t%d\n'%(w,lo,hi,len(half)))
    fo.write('STATS\t%d\t%s\n'%(seed,stats)); fo.close(); print(seed,stats)
if __name__=='__main__': main()
