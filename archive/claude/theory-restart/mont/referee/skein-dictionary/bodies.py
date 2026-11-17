"""Generate a diverse list of actual bodies (one axis string, one arc string, no closed component).
Writes bodies.json: list of [body_word, kind]."""
import sys, json, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex, flat_search as fs
def is_knot(B):
    full=alex.symmetrize(alex.parse('s.'+B))
    return full is not None and alex.diagram(full) is not None
def width_ok(B):
    w=1
    for tok in B.split('.'):
        c,s=tok[0],int(tok[1:])
        if c in 'lr':
            if s>w: return False
            w+=2
        elif c=='u':
            if s+1>w: return False   # rough
            w-=2
        else:
            if s>0 and s+1>w: return False
    return w==1
rnd=random.Random(20261117)
out=[]; seen=set()
def add(B,kind):
    if B in seen: return
    if not is_knot(B): return
    seen.add(B); out.append([B,kind])
gb=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
for B,_ in gb: add(B,'general_boxes.json')
add('y0.r2.y0.y1.y0.y1.x2.u1','T_n box (nest sec 3)')
# rational: integral boxes and 2-bridge bodies l1.W.u2
for k in range(1,5): add('.'.join(['y0']*k),'integral'); add('.'.join(['x0']*k),'integral')
tries=0
while sum(1 for _,k in out if k=='rational l1.W.u2')<45 and tries<5000:
    tries+=1
    W=fs.reduced([rnd.choice('xy')+str(rnd.choice([0,1])) for _ in range(rnd.randint(2,9))])
    if not W: continue
    add('l1.'+'.'.join(W)+'.u2','rational l1.W.u2')
# random non-rational (fs.gen shapes) -- fresh seed, not the general_boxes seed
tries=0
while sum(1 for _,k in out if k=='random fs.gen')<70 and tries<20000:
    tries+=1
    w=fs.gen(rnd,rnd.randint(5,16))
    if w is None: continue
    add(w[2:],'random fs.gen')
# deeper internal extrema: two nested caps
tries=0
def rw(maxpos,L):
    return fs.reduced([rnd.choice('xy')+str(rnd.choice(range(maxpos+1))) for _ in range(L)])
while sum(1 for _,k in out if k=='deep extrema')<30 and tries<20000:
    tries+=1
    a=rw(2,rnd.randint(1,4)); b=rw(4,rnd.randint(2,6)); c=rw(6,rnd.randint(1,5)); d=rw(2,rnd.randint(0,3))
    if not a or not b or not c: continue
    B=rnd.choice(['l1','r1'])+'.'+'.'.join(a)+'.'+rnd.choice(['l2','r2','l3','r3'])+'.'+'.'.join(b)+'.'+rnd.choice(['l3','r3','l4','r4','l5','r5'])+'.'+'.'.join(c)+'.'+rnd.choice(['u3','u4','u5'])+'.'+rnd.choice(['u1','u2','u3'])+('.'+'.'.join(d) if d else '')+'.'+rnd.choice(['u1','u2'])
    add(B,'deep extrema')
# nested necklace bodies r2.(y1)^m.B1...Bn.u1 (depth 2) and depth 3
base=[B for B,k in out]
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
tries=0
while sum(1 for _,k in out if k=='necklace depth2')<35 and tries<5000:
    tries+=1
    n=rnd.choice([1,2,2,3]); m=rnd.choice([-3,-2,-1,1,2,3])
    bs=[rnd.choice(base) for _ in range(n)]
    add('r2.'+tw(m)+'.'.join(bs)+'.u1','necklace depth2')
d2=[B for B,k in out if k=='necklace depth2']
tries=0
while sum(1 for _,k in out if k=='necklace depth3')<20 and tries<5000:
    tries+=1
    m=rnd.choice([-2,-1,1,2]); bs=[rnd.choice(d2)]+[rnd.choice(base) for _ in range(rnd.choice([0,1]))]
    rnd.shuffle(bs)
    add('r2.'+tw(m)+'.'.join(bs)+'.u1','necklace depth3')
json.dump(out,open('bodies.json','w'))
from collections import Counter
print(len(out),Counter(k for _,k in out))
