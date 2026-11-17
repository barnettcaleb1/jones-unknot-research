"""Point-reflection symmetric theta-curves: W_top + f(W_top), f = rotation by pi in the plane + crossing switch
(= the 3-d point reflection through the centre of the middle level; orientation-reversing, swaps v_top <-> v_bot,
A_1 <-> A_2, reverses k; fixed points: the centre (on k) and a point off Theta)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import theta
def levels(events):
    cols=[]; L=[list(cols)]
    for ev in events:
        typ=ev[0]
        if typ in ('capA','capK'):
            i=ev[1]; c='a' if typ=='capA' else 'k'; cols[i:i]=[c,c]
        elif typ=='cup': i=ev[1]; del cols[i:i+2]
        elif typ in ('X','Y'): i=ev[1]; cols[i],cols[i+1]=cols[i+1],cols[i]
        elif typ=='splitR': cols[ev[1]+1:ev[1]+1]=['k']
        elif typ=='splitL': cols[ev[1]:ev[1]]=['k']
        elif typ=='mergeR': del cols[ev[1]+1]
        elif typ=='mergeL': del cols[ev[1]]
        L.append(list(cols))
    return L
def fimage(events):
    """f-image (reversed order) of an event list starting at the empty level"""
    L=levels(events); out=[]
    for j in range(len(events)-1,-1,-1):
        ev=events[j]; typ=ev[0]; before=L[j]; after=L[j+1]; N=len(before)
        if typ=='proj': continue
        i=ev[1]
        if typ in ('capA','capK'): out.append(('cup',N-i))
        elif typ=='cup': out.append(('capA' if before[i]=='a' else 'capK', N-2-i))
        elif typ=='X': out.append(('Y',N-2-i))
        elif typ=='Y': out.append(('X',N-2-i))
        elif typ=='splitR': out.append(('mergeL',N-1-i))
        elif typ=='splitL': out.append(('mergeR',N-1-i))
        elif typ=='mergeR': out.append(('splitL',N-2-i))
        elif typ=='mergeL': out.append(('splitR',N-2-i))
    return out
def symmetric(top):
    mid=levels(top)[-1]
    assert mid==mid[::-1], ('middle level not palindromic',mid)
    return top+fimage(top)
def body(word, off=0):
    """half-word body letters acting with the axis at undoubled position off (k strand at off+1)"""
    ev=[]
    for tok in [t for t in word.split('.') if t]:
        c,s=tok[0],int(tok[1:])
        if c in 'xy':
            if s==0: ev+= [(c.upper(),off),(c.upper(),off)]
            else: ev.append((c.upper(),off+s))
        elif c in 'lr': ev.append(('capK',off+s))
        elif c=='u': ev.append(('cup',off+s))
    return ev
def Sneck_top(m, B):
    tw=[('Y',1)]*m if m>=0 else [('X',1)]*(-m)
    return [('capA',0),('splitR',0),('proj',1),('capK',2)]+tw+body(B,0)
