"""Referee (PROOF lane) common helpers: an independent random-body generator and word utilities."""
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *

def tw(m, pos='y', neg='x', idx=1):
    """m crossings at position idx: m>0 -> pos letters, m<0 -> neg letters"""
    return [(pos if m>0 else neg)+str(idx)]*abs(m)

def jn(*parts):
    w=[]
    for p in parts:
        if isinstance(p,str): w+=[x for x in p.split('.') if x]
        else: w+=list(p)
    return '.'.join(w)

def Rrev(B):
    out=[]
    for tok in reversed(B.split('.')):
        c,i=tok[0],tok[1:]
        if c in 'lr': out.append('u'+i)
        elif c=='u': out.append('r'+i)
        else: out.append(tok)
    return '.'.join(out)

def random_body(rnd, L, kmax=5):
    """random half-diagram body: starts and ends with one strand, never closes a loop, only body positions.
    Track segments: pos -> seg id; seg -> list of open ends ('IN' or position markers)."""
    pos=[0]; seg_ends={0:['IN']}; nid=[1]; word=[]
    def k(): return len(pos)
    tries=0
    while len(word)<L and tries<10*L:
        tries+=1
        r=rnd.random()
        if r<0.45 and k()>=2:
            i=rnd.randint(1,k()-1); c=rnd.choice('xy')
            pos[i-1],pos[i]=pos[i],pos[i-1]; word.append(c+str(i))
        elif r<0.6:
            c=rnd.choice('xy'); word.append(c+'0')
        elif r<0.8 and k()<kmax:
            i=rnd.randint(1,k()+1); s=nid[0]; nid[0]+=1
            pos[i-1:i-1]=[s,s]; seg_ends[s]=[]; word.append(rnd.choice('lr')+str(i))
        elif k()>=3:
            i=rnd.randint(1,k()-1); p,q=pos[i-1],pos[i]
            if p==q: continue
            # merge q into p
            for j in range(len(pos)):
                if pos[j]==q: pos[j]=p
            seg_ends[p]=seg_ends[p]+seg_ends[q]; del seg_ends[q]
            del pos[i-1:i+1]; word.append('u'+str(i))
    # close up
    guard=0
    while k()>1 and guard<50:
        guard+=1
        cand=[i for i in range(1,k()) if pos[i-1]!=pos[i]]
        if cand:
            i=rnd.choice(cand); p,q=pos[i-1],pos[i]
            for j in range(len(pos)):
                if pos[j]==q: pos[j]=p
            del pos[i-1:i+1]; word.append('u'+str(i))
        else:
            i=rnd.randint(1,k()-1) if k()>=2 else None
            if i is None: break
            # swap strands to break a same-segment adjacency (k>=3 needed)
            if k()>=3:
                i=rnd.randint(1,k()-1); c=rnd.choice('xy'); pos[i-1],pos[i]=pos[i],pos[i-1]; word.append(c+str(i))
            else:
                return None
    if k()!=1 or not word: return None
    return '.'.join(word)

def gen_bodies(seed, n, Lmin=3, Lmax=10, kmax=5, need_knot=True):
    rnd=random.Random(seed); out=[]; seen=set(); guard=0
    while len(out)<n and guard<50*n:
        guard+=1
        B=random_body(rnd, rnd.randint(Lmin,Lmax), kmax)
        if B is None or B in seen: continue
        seen.add(B)
        if need_knot and J('s.'+B) is None: continue
        out.append(B)
    return out

def ratio_mono(p,q):
    """exact p/q for q a monomial"""
    assert len(q)==1
    (e,c),=q.items()
    out={}
    for f,d in p.items():
        if d%c: return None
        out[f-e]=d//c
    return out

def divexact(p,d):
    p=dict(p); q={}
    if not p: return {}
    lo=bot(p)-bot(d); dt=top(d); dc=d[dt]
    while p:
        e=top(p); c=p[e]; k=e-dt
        if k<lo or c%dc: return None
        q[k]=c//dc
        p=sub(p,mul(mono(k,c//dc),d))
    return clean(q)

def unit_equal(p,q):
    """p == +-t^k q ?  returns (sign,k) or None"""
    if not p and not q: return (1,0)
    if not p or not q or len(p)!=len(q): return None
    k=bot(p)-bot(q); s=p[bot(p)]//q[bot(q)] if q[bot(q)] else None
    if s not in (1,-1): return None
    return (s,k) if {e+k:s*c for e,c in q.items()}==p else None

def vec_unit_equal(v,w):
    """v == +-t^k w (common unit) ?"""
    for comp in (0,1):
        if v[comp] or w[comp]:
            u=unit_equal(v[comp],w[comp])
            if u is None: return None
            s,k=u
            ok=all({e+k:s*c for e,c in w[j].items()}==clean(v[j]) for j in (0,1))
            return (s,k) if ok else None
    return (1,0)

def reduce_word(B):
    out=[]
    for l in B.split('.'):
        if out and out[-1][1:]==l[1:] and out[-1][0]!=l[0] and l[0] in 'xy' and out[-1][0] in 'xy': out.pop()
        else: out.append(l)
    return '.'.join(out)

def gen_bodies_nontriv(seed, n, Lmin=5, Lmax=12, kmax=5, frac_trivial=0.0):
    rnd=random.Random(seed); out=[]; seen=set(); guard=0
    while len(out)<n and guard<400*n:
        guard+=1
        B=random_body(rnd, rnd.randint(Lmin,Lmax), kmax)
        if B is None: continue
        B=reduce_word(B)
        if not B or B in seen: continue
        seen.add(B)
        j=J('s.'+B)
        if j is None: continue
        if len(j)==1 and rnd.random()>frac_trivial: continue
        out.append(B)
    return out
