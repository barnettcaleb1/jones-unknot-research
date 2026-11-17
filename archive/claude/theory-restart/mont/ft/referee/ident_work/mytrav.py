"""Referee's own traversal of the quotient arc k of a half-word (independent of ident/chord.py).
Events along k from the top fixed point: (token index t (in the token list after 's'), kind 'w'|'c', d) with d = +1 if k
moves DOWN the Morse picture at that event, -1 if up.  Sign conventions (stated, chosen to compare with the builder):
 winding site: sigma = +1 for x0, -1 for y0;  crossing site: sigma = base(c)*d1*d2 with base(x) = -1, base(y) = +1
 (= alex.py writhe convention for the oriented arc).  delta(winding) = 'v' if d = +1 (k passes along A_in, which is
 oriented downward from the start vertex), '^' if d = -1.  label(chord) = parity of the number of winding events strictly
 between the two passes along k."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
def events(word):
    half=alex.parse(word)
    # piece graph: each piece is a vertical segment occupying one position between two events.
    nid=[0]
    def new():
        nid[0]+=1; return nid[0]
    # connections: piece -> list of (piece, event, how) ; we store directed 'down' links: from upper piece to lower piece
    nbr={}
    def link(up,down,ev):  # k can go from 'up' piece to 'down' piece moving down (or reverse moving up)
        nbr.setdefault(up,[]).append((down,ev,+1)); nbr.setdefault(down,[]).append((up,ev,-1))
    def turn(a,b):          # cap or cup: connects two pieces; direction flips
        nbr.setdefault(a,[]).append((b,None,0)); nbr.setdefault(b,[]).append((a,None,0))
    top=new(); pos=[top]
    for t,(c,s) in enumerate(half):
        if c in 'xy' and s==0:
            a=pos[0]; b=new(); link(a,b,(t,'w')); pos[0]=b
        elif c in 'xy':
            i=s-1
            if i+1>=len(pos): return None
            tl,tr=pos[i],pos[i+1]; bl,br=new(),new()
            link(tl,br,(t,'c')); link(tr,bl,(t,'c')); pos[i],pos[i+1]=bl,br
        elif c in 'lr':
            i=s-1
            if i>len(pos): return None
            a,b=new(),new(); turn(a,b); pos[i:i]=[a,b]
        elif c=='u':
            i=s-1
            if i+1>=len(pos): return None
            turn(pos[i],pos[i+1]); del pos[i:i+2]
    if len(pos)!=1: return None
    bottom=pos[0]
    # walk from top piece moving down
    seq=[]; cur=top; d=+1; prev_edge=None; steps=0
    while not (cur==bottom and d==+1 and prev_edge is not None and False):
        steps+=1
        if steps>100000: return None
        if cur==bottom and d==+1: break
        opts=[(b,ev,h) for (b,ev,h) in nbr.get(cur,[]) if (h==d) or (h==0)]
        # moving in direction d along piece cur: next connection is at the bottom end if d=+1 (links with h=+1 or a cup),
        # at the top end if d=-1 (links with h=-1 or a cap).  Disambiguate turns: a piece has exactly one connection at each end.
        ends=[]
        for (b,ev,h) in nbr.get(cur,[]):
            if h==d: ends.append((b,ev,h))
        turns=[(b,ev,h) for (b,ev,h) in nbr.get(cur,[]) if h==0]
        # a piece created by a cap has its turn at its TOP end; a piece ending in a cup has its turn at its BOTTOM end
        if ends:
            b,ev,h=ends[0]; seq.append((ev[0],ev[1],d)); cur=b
        else:
            # turn at the end we are moving toward
            cand=[x for x in turns if tag.get((cur,x[0]))==d]
            if len(cand)!=1: return None
            cur=cand[0][0]; d=-d
    return seq
tag={}
def events2(word):
    """robust version: pieces know which end each connection is at."""
    half=alex.parse(word)
    nid=[0]
    def new():
        nid[0]+=1; return nid[0]
    lower={}; upper={}   # piece -> (other piece, event or None, kind) at its lower / upper end
    top=new(); pos=[top]
    for t,(c,s) in enumerate(half):
        if c in 'xy' and s==0:
            a=pos[0]; b=new(); lower[a]=(b,(t,'w')); upper[b]=(a,(t,'w')); pos[0]=b
        elif c in 'xy':
            i=s-1
            if i+1>=len(pos): return None
            tl,tr=pos[i],pos[i+1]; bl,br=new(),new()
            lower[tl]=(br,(t,'c')); upper[br]=(tl,(t,'c')); lower[tr]=(bl,(t,'c')); upper[bl]=(tr,(t,'c'))
            pos[i],pos[i+1]=bl,br
        elif c in 'lr':
            i=s-1
            if i>len(pos): return None
            a,b=new(),new(); upper[a]=(b,'turn'); upper[b]=(a,'turn'); pos[i:i]=[a,b]
        elif c=='u':
            i=s-1
            if i+1>=len(pos): return None
            a,b=pos[i],pos[i+1]; lower[a]=(b,'turn'); lower[b]=(a,'turn'); del pos[i:i+2]
        else: return None
    if len(pos)!=1: return None
    bottom=pos[0]; seq=[]; cur=top; d=+1; steps=0
    while True:
        steps+=1
        if steps>10**6: return None
        if cur==bottom and d==+1: break
        nxt=lower.get(cur) if d==+1 else upper.get(cur)
        if nxt is None: return None
        b,ev=nxt
        if ev=='turn': cur=b; d=-d
        else: seq.append((ev[0],ev[1],d)); cur=b
    return seq
def site_data(word, seq=None):
    """for each crossing letter index: ('T',delta,sigma) or ('C',label,sigma)"""
    half=alex.parse(word)
    if seq is None: seq=events2(word)
    if seq is None: return None
    wc=[0]
    for (t,k,d) in seq: wc.append(wc[-1]+(1 if k=='w' else 0))
    passes={}
    for p,(t,k,d) in enumerate(seq): passes.setdefault(t,[]).append((p,d))
    out={}
    for t,ps in passes.items():
        c=half[t][0]
        if len(ps)==1:
            (p,d),=ps; out[t]=('T','v' if d==1 else '^', +1 if c=='x' else -1)
        else:
            (p,d1),(q,d2)=ps; lab=(wc[q]-wc[p+1])%2
            base=-1 if c=='x' else 1
            out[t]=('C','+' if lab==0 else '-', base*d1*d2)
    return out
