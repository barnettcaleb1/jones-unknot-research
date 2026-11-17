"""Referee's independent h=0 state sum (claim 6): explicit enumeration of states and explicit curve tracing.
Half-word -> planar graph on half-strand positions. Off-axis crossing: 'swap' (unflipped) or, at a flip site, vertical (coef eps)
/ horizontal (coef -eps). On-axis letter: winding marker on the strand at position 0: unflipped -> wound (1 marker); flip site ->
unwound (coef 3/2 eps) or wound (coef 1/2 eps). Loops weigh -1 (even #markers) or 3 (odd); the arc T->B weighs 1."""
import sys, itertools
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
def parse(word):
    w=word.split('.')
    assert w[0]=='s'
    return [(t[0],int(t[1:])) for t in w[1:]]
def resolve(word, choice):
    """choice: dict token_index(1-based in word.split('.')) -> resolution in {'V','H','U','W'}; returns list of curves, each
    curve = ('arc'|'loop', markers)"""
    toks=parse(word)
    nid=[0]
    def new():
        nid[0]+=1; return nid[0]
    T=new(); pos=[T]; joins=[]; marks={}
    # each segment id: a piece of strand between events; joins: (segA, endA, segB, endB)
    def mark(seg):
        marks[seg]=marks.get(seg,0)+1
    for k,(c,i) in enumerate(toks):
        tk=k+1
        if c in 'lr':
            a,b=new(),new(); pos[i-1:i-1]=[a,b]; joins.append((a,'top',b,'top'))
        elif c=='u':
            a,b=pos[i-1],pos[i]; joins.append((a,'bot',b,'bot')); del pos[i-1:i+1]
        elif i>=1:
            L,R=pos[i-1],pos[i]; bl,br=new(),new(); pos[i-1],pos[i]=bl,br
            r=choice.get(tk,'X')
            if r=='X':      # swap: L continues to br, R to bl
                joins.append((L,'bot',br,'top')); joins.append((R,'bot',bl,'top'))
            elif r=='V':    # vertical: L -> bl, R -> br
                joins.append((L,'bot',bl,'top')); joins.append((R,'bot',br,'top'))
            elif r=='H':    # horizontal: L-R joined below (cup), bl-br joined above (cap)
                joins.append((L,'bot',R,'bot')); joins.append((bl,'top',br,'top'))
            else: raise ValueError
        else:               # on-axis: strand at position 0 continues, possibly with a winding marker
            S=pos[0]; n=new(); pos[0]=n; joins.append((S,'bot',n,'top'))
            r=choice.get(tk,'W')
            if r=='W': mark(n)
    assert len(pos)==1, pos
    B=pos[0]
    nxt={}
    for a,ea,b,eb in joins: nxt[(a,ea)]=(b,eb); nxt[(b,eb)]=(a,ea)
    segs=set([T,B]); [segs.update([a,b]) for a,_,b,_ in joins]
    seen=set(); curves=[]
    # arc from T
    s,end=T,'bot'; mk=0
    while True:
        seen.add(s); mk+=marks.get(s,0)
        if s==B and end=='bot': break
        s2,e2=nxt[(s,end)]
        s=s2; end='bot' if e2=='top' else 'top'
    curves.append(('arc',mk))
    for s0 in sorted(segs):
        if s0 in seen: continue
        s,end=s0,'bot'; mk=0
        while s not in seen:
            seen.add(s); mk+=marks.get(s,0)
            s2,e2=nxt[(s,end)]
            s=s2; end='bot' if e2=='top' else 'top'
        curves.append(('loop',mk))
    return curves
def statesum(word, flipsites, odd=3, even=-1, axw=(Fr(3,2),Fr(1,2))):
    toks=word.split('.')
    sites=sorted(flipsites)
    opts=[]
    for tk in sites:
        a=toks[tk]; eps=1 if a[0]=='x' else -1
        if a[1:]=='0': opts.append([('U',eps*axw[0]),('W',eps*axw[1])])
        else: opts.append([('V',Fr(eps)),('H',Fr(-eps))])
    tot=Fr(0)
    for combo in itertools.product(*opts):
        ch={tk:r for tk,(r,_) in zip(sites,combo)}
        coef=Fr(1)
        for _,cf in combo: coef*=cf
        wgt=Fr(1)
        for kind,mk in resolve(word,ch):
            if kind=='loop': wgt*= (odd if mk%2 else even)
        tot+=coef*wgt
    return tot
