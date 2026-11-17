"""Sister evaluation: colour edge A_1 (axis edge through the top cap) by 2 and A_2, k by 1.  J' = normalised
<Theta; A_1=2, A_2=1, k=1>/<Theta_0>.  Theta trivial => J' = 1.  Events in the circle model (one capA at top, splitR at v_top
on A_l, mergeL or mergeR at v_bot, bottom cup of A_2)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import theta, lp
def expand_A1(events, use_e):
    lab=[]; out=[]; done_proj=False
    def dpos(i): return sum(2 if l=='A1' else 1 for l in lab[:i])
    def mult(i): return 2 if lab[i]=='A1' else 1
    for ev in events:
        typ=ev[0]
        if typ=='proj': continue
        i=ev[1]
        if typ=='capA':
            d=dpos(i)
            if not lab:   # top cap: A1, doubled
                out+=[('cap',d),('cap',d+1)]; lab[i:i]=['A1','A1']
                if use_e: out+=[('cup',d),('cap',d)]    # e on the left A1 strand pair right after the cap
            else: raise ValueError('second axis cap')
        elif typ=='capK':
            out.append(('cap',dpos(i))); lab[i:i]=['k','k']
        elif typ=='cup':
            d=dpos(i)
            if lab[i]=='A1': out+=[('cup',d+1),('cup',d)]
            else: out.append(('cup',d))
            del lab[i:i+2]
        elif typ in ('X','Y'):
            s=dpos(i); p=mult(i); q=mult(i+1); c=typ.lower()
            for j in range(p-1,-1,-1):
                for k in range(q): out.append((c,s+j+k))
            lab[i],lab[i+1]=lab[i+1],lab[i]
        elif typ=='splitR':     # A1 (doubled) above -> A2 (single, left) + k (single, right): no elementary event
            assert lab[i]=='A1'; lab[i:i+1]=['A2','k']
        elif typ=='mergeL':
            assert lab[i]=='k'
            if lab[i+1]=='A1':   # k (single) + A1 (doubled) -> A2 (single): cup k with inner A1 strand
                d=dpos(i); out.append(('cup',d)); lab[i:i+2]=['A2']
            else:                # k + A2 (single) -> A1 (doubled): strands continue
                assert lab[i+1]=='A2'; lab[i:i+2]=['A1']
        elif typ=='mergeR':
            assert lab[i+1]=='k'
            if lab[i]=='A1':     # A1 (doubled) + k (single) -> A2: cup inner A1 strand (d+1) with k (d+2)
                d=dpos(i); out.append(('cup',d+1)); lab[i:i+2]=['A2']
            else:                # A2 + k -> A1 (doubled): strands continue
                assert lab[i]=='A2'; lab[i:i+2]=['A1']
        else: raise ValueError(ev)
    assert not lab
    return out
def Jsister(events):
    if theta.THETA0_TIMES_DELTA is None: theta.THETA0_TIMES_DELTA=theta.theta_raw(theta.planar_theta())
    D=theta.bracket(expand_A1(events,False)); De=theta.bracket(expand_A1(events,True))
    r=theta.pmul(theta.DELTA,D); 
    from kauffman import padd
    padd(r,De,-1)
    # normalise by the planar theta in the SAME colouring
    P=[('capA',0),('splitR',0),('proj',1),('mergeR',0),('cup',0)]
    D0=theta.bracket(expand_A1(P,False)); D0e=theta.bracket(expand_A1(P,True))
    r0=theta.pmul(theta.DELTA,D0); padd(r0,D0e,-1)
    q=theta.pdiv(r,r0)
    if q is None: return None
    return q
def sister_is_unit(events):
    q=Jsister(events)
    return q is not None and len(q)==1
