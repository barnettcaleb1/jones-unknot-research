# Equivariant one-term relation: if the upstairs lift of D has an isolated chord, or a pair {c,h(c)} crossing only each other,
# then w(D) = 0.  Also list the converse failures (W = 0 without such a reason), for information.
import itertools, abstract as ab
import math
def lift(D):
    """upstairs chords on the circle: quotient slot p -> angles +theta_p and -theta_p (theta_p in (0,pi), increasing along k).
    sheet of slot p = parity of O/T tokens before it; a point on sheet s at theta is placed at +theta (s=0) or -theta (s=1)."""
    L=len(D); th={p:math.pi*(p+1)/(L+1) for p in range(L)}
    sheet={}; s=0
    for p,tk in enumerate(D):
        sheet[p]=s
        if tk[0] in 'OT': s^=1
    pos,_=ab.labels(D)
    ups=[]  # list of (group id, (x,y)) angles in [0,2pi)
    ang=lambda p,s: th[p] if s==0 else 2*math.pi-th[p]
    for i,(a,b) in pos.items():
        ups.append((('E',i),(ang(a,sheet[a]),ang(b,sheet[b]))))
        ups.append((('E',i),(ang(a,1-sheet[a]),ang(b,1-sheet[b]))))
    for p,tk in enumerate(D):
        if tk[0]=='O': ups.append((('O',tk[1]),(th[p],2*math.pi-th[p])))
    return ups
def cross(c,d):
    a,b=sorted(c); x,y=sorted(d)
    return (a<x<b)!=(a<y<b)
def has_isolated(D):
    ups=lift(D)
    for k,(g,c) in enumerate(ups):
        others=[d for j,(h,d) in enumerate(ups) if j!=k]
        if not any(cross(c,d) for d in others): return True
    groups={}
    for g,c in ups: groups.setdefault(g,[]).append(c)
    for g,cs in groups.items():
        if len(cs)==2:
            others=[d for h,d in ups if h!=g]
            if not any(cross(c,d) for c in cs for d in others): return True
    return False
res={'iso->0':[0,0]}; zero_noniso=0; tot=0
for (no,nn) in [(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]:
    toks=[('E',i) for i in range(no) for _ in (0,1)]+[('O',j) for j in range(nn)]
    seen=set()
    for perm in set(itertools.permutations(toks)):
        for parity in itertools.product([0,1],repeat=len(perm)-1):
            D=[perm[0]]
            for gb,tk in zip(parity,perm[1:]):
                if gb: D.append(('T',))
                D.append(tk)
            key=ab.shape(D)
            if key in seen: continue
            seen.add(key); tot+=1
            val=ab.w(D)
            if has_isolated(D): res['iso->0'][0 if val==0 else 1]+=1
            elif val==0: zero_noniso+=1
print('types',tot,' isolated chord/pair => W=0 (holds, fails):',res['iso->0'],'  W=0 without isolated chord/pair:',zero_noniso)
