"""Equivariant chord diagram (quotient form) of a singular configuration: half-word + set of flip sites.
Traverse the half-diagram arc k from the top fixed point to the bottom one; events at flip sites:
  winding site (x0/y0): tangency element 'T' (the arc touches A_in), with its rank along A_in (= order in the word);
  crossing site (x_i/y_i, i>=1): chord between its two passes, label = parity of the number of ALL winding letters
  (singular or not) passed strictly between the two passes  (= lk(loop, A) mod 2; 0 = 'same side', 1 = 'opposite').
Canonical form up to reversal of the arc (reversal also reverses the A_in order).
Each tangency also carries delta = +1 ('v') if k passes it in the direction of A_in (both oriented from the start vertex), else -1 ('^').
Resolution signs: windings use the upstairs crossing sign (x0 -> +1, y0 -> -1, orientation independent);
crossings use the quotient crossing sign of the oriented arc k."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
def traverse(word):
    """returns list of passes along k: (letter index, kind) kind in {'w','c'}; or None"""
    half=alex.parse(word)
    # segments: each position holds a segment id; connections: adjacency list between (seg) via events
    nid=[0]
    def new():
        nid[0]+=1; return nid[0]
    adj={}   # seg -> list of (other seg, event)   event = (letter index, kind) or None
    def link(a,b,ev):
        adj.setdefault(a,[]).append((b,ev,1)); adj.setdefault(b,[]).append((a,ev,-1))
    start=new(); pos=[start]
    for t,(c,s) in enumerate(half):
        if c in 'xy' and s==0:
            a=pos[0]; b=new(); link(a,b,(t,'w')); pos[0]=b
        elif c in 'xy':
            i=s-1
            if i+1>=len(pos): return None
            a,b=pos[i],pos[i+1]; cc,d=new(),new()
            link(a,d,(t,'c')); link(b,cc,(t,'c'))     # strands cross: top-left -> bottom-right, top-right -> bottom-left
            pos[i],pos[i+1]=cc,d
        elif c in 'lr':
            i=s-1
            if i>len(pos): return None
            a,b=new(),new(); link(a,b,None); pos[i:i]=[a,b]
        elif c=='u':
            i=s-1
            if i+1>=len(pos): return None
            link(pos[i],pos[i+1],None); del pos[i:i+2]
    if len(pos)!=1: return None
    end=pos[0]
    # walk from start to end
    seq=[]; prev=None; cur=start; used=set()
    while cur!=end:
        nxt=[(b,ev,dr) for (b,ev,dr) in adj.get(cur,[]) if (min(cur,b),max(cur,b),ev) not in used]
        if len(nxt)!=1: return None
        b,ev,dr=nxt[0]; used.add((min(cur,b),max(cur,b),ev))
        if ev is not None: seq.append((ev[0],ev[1],dr))
        cur=b
    return seq
def diagram(word, sites):
    """sites: set of letter indices (in the half-word token list WITHOUT the leading 's'); returns canonical diagram"""
    seq3=traverse(word)
    if seq3 is None: return None
    seq=[(t,k) for t,k,d in seq3]
    wdir={t:d for t,k,d in seq3 if k=='w'}
    sites=set(sites)
    # winding count prefix
    wcount=[0]
    for (t,k) in seq: wcount.append(wcount[-1]+(1 if k=='w' else 0))
    passes={}
    for p,(t,k) in enumerate(seq): passes.setdefault(t,[]).append(p)
    elems=[]   # (position, token)
    wsites=sorted(t for t in sites if seq and any(t==tt and k=='w' for tt,k in seq))
    rankA={t:i for i,t in enumerate(sorted(t for t in sites if len(passes.get(t,[]))==1))}
    chords=[]
    for t in sites:
        ps=passes.get(t,[])
        if len(ps)==1: elems.append((ps[0],('T',rankA[t],wdir[t])))
        elif len(ps)==2:
            p,q=ps; lab=(wcount[q]-wcount[p+1])%2
            chords.append((p,q,lab))
        else: return None
    # encode: sequence of points along k
    pts=[]
    for p,tok in elems: pts.append((p,tok))
    for ci,(p,q,lab) in enumerate(chords): pts.append((p,('C',ci,lab))); pts.append((q,('C',ci,lab)))
    pts.sort()
    def encode(order, nT, rev):
        # relabel chords by first appearance; tangency by A-rank (reversed if rev)
        cmap={}; out=[]
        for p,tok in order:
            if tok[0]=='T':
                r=tok[1] if not rev else nT-1-tok[1]
                out.append(('T',r,tok[2]))
            else:
                ci=tok[1]
                if ci not in cmap: cmap[ci]=len(cmap)
                out.append(('C',cmap[ci],tok[2]))
        return tuple(out)
    nT=len(elems)
    e1=encode(pts,nT,False); e2=encode(list(reversed(pts)),nT,True)
    return min(e1,e2)
def dstr(d):
    s=[]
    for tok in d:
        if tok[0]=='T': s.append('T%d%s'%(tok[1],'v' if tok[2]==1 else '^'))
        else: s.append('%s%s'%('abcdefgh'[tok[1]],'+' if tok[2]==0 else '-'))
    return ''.join(s) if s else '()'

def site_signs(word, sites):
    """canonical resolution sign of each site: crossings: quotient crossing sign of k (oriented top->bottom fixed point);
    windings: sign of the k/A_in crossings with A_in oriented from the top to the bottom fixed point."""
    seq3=traverse(word)
    half=alex.parse(word)
    dirs={}
    for t,k,d in seq3: dirs.setdefault(t,[]).append(d)
    out={}
    for s in sites:
        c=half[s][0]; base=1 if c=='y' else -1
        dd=dirs[s]
        if len(dd)==1: out[s]=-base          # upstairs crossing sign of the on-axis crossing: x0 -> +1, y0 -> -1
        else: out[s]=base*dd[0]*dd[1]        # quotient crossing sign of k (oriented top -> bottom fixed point)
    return out

def lam_counts(word):
    """lambda_minus = sum of quotient crossing signs over k-k crossings with odd label (all crossing letters i>=1);
    lambda_plus = same over even label; w0 = sum over windings of the upstairs sign (x0:+1, y0:-1);
    w0d = sum over windings of sign*delta (delta = +1 if k passes the winding in the direction of A_in)."""
    seq3=traverse(word); half=alex.parse(word)
    wcount=[0]
    for (t,k,d) in seq3: wcount.append(wcount[-1]+(1 if k=='w' else 0))
    passes={}
    for p,(t,k,d) in enumerate(seq3): passes.setdefault(t,[]).append((p,d))
    lm=lp_=w0=w0d=0
    for t,ps in passes.items():
        c=half[t][0]; base=1 if c=='y' else -1
        if len(ps)==2:
            (p,d1),(q,d2)=ps; lab=(wcount[q]-wcount[p+1])%2
            s=base*d1*d2
            if lab: lm+=s
            else: lp_+=s
        else:
            (p,d),=ps; s=-base
            w0+=s; w0d+=s*d
    return dict(lm=lm,lp=lp_,w0=w0,w0d=w0d)

def order1_counts(word):
    """lm: sum of quotient signs of odd-label k-k crossings; wup/wdn: sums of upstairs signs (x0:+1,y0:-1) over windings
    traversed against / along A_in (delta '^' / 'v')."""
    seq3=traverse(word); half=alex.parse(word)
    wcount=[0]
    for (t,k,d) in seq3: wcount.append(wcount[-1]+(1 if k=='w' else 0))
    passes={}
    for p,(t,k,d) in enumerate(seq3): passes.setdefault(t,[]).append((p,d))
    lm=lp_=wup=wdn=0
    for t,ps in passes.items():
        c=half[t][0]; base=1 if c=='y' else -1
        if len(ps)==2:
            (p,d1),(q,d2)=ps; lab=(wcount[q]-wcount[p+1])%2
            if lab: lm+=base*d1*d2
            else: lp_+=base*d1*d2
        else:
            (p,d),=ps
            if d==1: wdn+=-base
            else: wup+=-base
    return dict(lm=lm,lp=lp_,wup=wup,wdn=wdn)
