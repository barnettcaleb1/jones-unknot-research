"""Constituent knot K_1 = A_1 u k of a theta-curve given by undoubled events (circle model, one splitR at v_top on A_l,
one mergeL/mergeR at v_bot).  A_1 = the axis edge through the top cap.  Returns the Jones polynomial (bracket-normalised,
as a key) of K_1: V != 1  =>  Theta nontrivial  =>  K nontrivial (unknot has a unique strong inversion, trivial quotient)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from kauffman import padd, pshift, pdelta, cap as kcap, cup as kcup
def reduced_diagram(events):
    lab=[]; out=[]   # labels of current undoubled strands; out = elementary events on kept strands
    def kp(i): return sum(1 for l in lab[:i] if l!='A2')
    for ev in events:
        typ=ev[0]
        if typ=='proj': continue
        i=ev[1]
        if typ=='capA':
            l='A1' if not any(x in ('A1','A2') for x in lab) and not lab else 'A?'
            # first capA = top cap (A1); a later capA would be an axis wiggle: label by context not supported
            assert l=='A1', 'only one axis cap supported'
            out.append(('cap',kp(i))); lab[i:i]=['A1','A1']
        elif typ=='capK':
            out.append(('cap',kp(i))); lab[i:i]=['k','k']
        elif typ=='cup':
            if lab[i]=='A2' and lab[i+1]=='A2': del lab[i:i+2]; continue
            assert 'A2' not in (lab[i],lab[i+1]), ('mixed cup',lab)
            out.append(('cup',kp(i))); del lab[i:i+2]
        elif typ in ('X','Y'):
            if 'A2' not in (lab[i],lab[i+1]): out.append((typ.lower(),kp(i)))
            lab[i],lab[i+1]=lab[i+1],lab[i]
        elif typ=='splitR':
            assert lab[i]=='A1'
            lab[i]='A2'; lab[i+1:i+1]=['k']     # A1 continues as k (position i+1 kept), A2 below at i (dropped)
        elif typ=='mergeL':
            assert lab[i]=='k' and lab[i+1]=='A1'
            out.append(('cup',kp(i))); lab[i:i+2]=['A2']
        elif typ=='mergeR':
            assert lab[i]=='A1' and lab[i+1]=='k'
            out.append(('cup',kp(i))); lab[i:i+2]=['A2']
        else: raise ValueError(ev)
    return out
def jones_key(events):
    el=reduced_diagram(events)
    state={():{0:1}}
    for c,i in el:
        new={}
        for m,p in state.items():
            if c=='cap': padd(new.setdefault(kcap(m,i),{}),p)
            elif c=='cup':
                m2,loop=kcup(m,i); padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=kcup(m,i); q=pdelta(p) if loop else p
                padd(new.setdefault(kcap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    p=dict(state.get((),{}))
    # divide by delta and return normalised key; unknot -> single monomial
    r={}
    while p:
        e=max(p); v=p[e]; r[e-2]=-v; padd(p,{e:-v,e-4:-v})
    return r
def trivial_constituent(events): return len(jones_key(events))==1
