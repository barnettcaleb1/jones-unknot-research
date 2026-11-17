"""ENGINE C2: direct evaluator of <Theta; 1,1,2> for a theta-curve given as a two-colour Morse word.
Undoubled strands carry colour 'a' (axis, colour 1) or 'k' (the arc k, colour 2 = doubled band with one f_2).
Events (positions are undoubled, left to right, top to bottom sweep):
  ('capA',i) / ('capK',i) : new arc creating positions i,i+1          ('cup',i): join i,i+1 (same colour)
  ('X',i) / ('Y',i)       : crossing of positions i,i+1 (x: over strand from top-left to bottom-right, as alex.py)
  ('splitR',i)            : vertex on axis strand i, k born at i+1      ('splitL',i): k born at i, axis moves to i+1
  ('mergeR',i)            : axis i + k i+1 -> axis i                    ('mergeL',i): k i + axis i+1 -> axis i
  ('proj',i)              : position of the single f_2 on the k strand at i (exactly one required)
J = normalise( <Theta>/<Theta_0> ), t = A^4 (calibrated against lp.J, see calib.py)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp
from kauffman import padd, pshift, pdelta, cap as kcap, cup as kcup

def expand(events, use_e):
    """undoubled events -> elementary events on doubled strands; use_e: replace proj by e (cup+cap)"""
    cols=[]; out=[]
    def dpos(i): return sum(2 if c=='k' else 1 for c in cols[:i])
    def mult(i): return 2 if cols[i]=='k' else 1
    nproj=0
    for ev in events:
        typ=ev[0]
        if typ in ('capA','capK'):
            i=ev[1]; d=dpos(i); c='a' if typ=='capA' else 'k'
            if c=='a': out.append(('cap',d))
            else: out+= [('cap',d),('cap',d+1)]
            cols[i:i]=[c,c]
        elif typ=='cup':
            i=ev[1]; assert cols[i]==cols[i+1], ('cup colours',ev,cols)
            d=dpos(i)
            if cols[i]=='a': out.append(('cup',d))
            else: out+= [('cup',d+1),('cup',d)]
            del cols[i:i+2]
        elif typ in ('X','Y'):
            i=ev[1]; s=dpos(i); p=mult(i); q=mult(i+1); c=typ.lower()
            for j in range(p-1,-1,-1):
                for k in range(q): out.append((c,s+j+k))
            cols[i],cols[i+1]=cols[i+1],cols[i]
        elif typ=='splitR':
            i=ev[1]; assert cols[i]=='a'; d=dpos(i); out.append(('cap',d)); cols[i+1:i+1]=['k']
        elif typ=='splitL':
            i=ev[1]; assert cols[i]=='a'; d=dpos(i); out.append(('cap',d+1)); cols[i:i]=['k']
        elif typ=='mergeR':
            i=ev[1]; assert cols[i]=='a' and cols[i+1]=='k'; d=dpos(i); out.append(('cup',d)); del cols[i+1]
        elif typ=='mergeL':
            i=ev[1]; assert cols[i]=='k' and cols[i+1]=='a'; d=dpos(i); out.append(('cup',d+1)); del cols[i]
        elif typ=='proj':
            i=ev[1]; assert cols[i]=='k'; nproj+=1
            if use_e:
                d=dpos(i); out+= [('cup',d),('cap',d)]
        else: raise ValueError(ev)
    assert not cols, ('unclosed',cols)
    assert nproj==1
    return out

def bracket(elem):
    state={():{0:1}}
    for c,i in elem:
        new={}
        for m,p in state.items():
            if c=='cap':
                padd(new.setdefault(kcap(m,i),{}),p)
            elif c=='cup':
                m2,loop=kcup(m,i)
                padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=kcup(m,i)
                q=pdelta(p) if loop else p
                padd(new.setdefault(kcap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    assert set(state)<= {()}, state.keys()
    return state.get((),{})

DELTA={2:-1,-2:-1}
def pmul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items():
            r[e+f]=r.get(e+f,0)+c*d
    return {e:c for e,c in r.items() if c}
def pdiv(p,d):
    """exact division of Laurent polys (A-exponents); None if not exact"""
    p=dict(p); q={}
    if not p: return {}
    dt=max(d); dc=d[dt]; lo=min(p)-min(d)
    while p:
        e=max(p); c=p[e]; k=e-dt
        if k<lo or c%dc: return None
        q[k]=c//dc
        for f,g in d.items():
            ee=k+f; nv=p.get(ee,0)-g*(c//dc)
            if nv: p[ee]=nv
            else: p.pop(ee,None)
    return q
THETA0_TIMES_DELTA=None
def theta_raw(events):
    """returns delta*<Theta> = delta<D> - <D_e>  (Laurent poly in A)"""
    D=bracket(expand(events,False)); De=bracket(expand(events,True))
    r=pmul(DELTA,D); padd(r,De,-1)
    return r
def planar_theta():
    return [('capA',0),('splitR',0),('proj',1),('mergeR',0),('cup',0)]
def J_events(events, tsign=1):
    global THETA0_TIMES_DELTA
    if THETA0_TIMES_DELTA is None: THETA0_TIMES_DELTA=theta_raw(planar_theta())
    r=theta_raw(events)
    q=pdiv(r,THETA0_TIMES_DELTA)
    if q is None: return None
    es=sorted(q); r0=es[0]%4
    if any((e-r0)%4 for e in es): return None
    J={tsign*(e-r0)//4:c for e,c in q.items()}
    return lp.normalize(J)

def from_halfword(w):
    """convert a kht++ half-word 's.<...>' into undoubled events (A_out rerouted on the far right)"""
    toks=[t for t in w.strip().split('.') if t]
    assert toks[0]=='s'
    ev=[('capA',0),('splitR',0),('proj',1)]
    for tok in toks[1:]:
        c,s=tok[0],int(tok[1:])
        if c in 'xy':
            if s==0: ev+= [(c.upper(),0),(c.upper(),0)]
            else: ev.append((c.upper(),s))
        elif c in 'lr': ev.append(('capK',s))
        elif c=='u': ev.append(('cup',s))
    ev+= [('mergeR',0),('cup',0)]
    return ev
