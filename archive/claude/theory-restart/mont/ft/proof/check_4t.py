# 4T test: three small segments I_1, I_2, I_3 of k (sheets s_r), chords t_ab between I_a and I_b with label s_a + s_b.
# [t12, t13 + t23] = 0  <->  D1 - D2 + D3 - D4 = 0, D1 = (I1: e13 before e12), D2 = (I1: e12 before e13),
# D3 = (I2: e23 before e12), D4 = (I2: e12 before e23).  Background: random extra chords / on-axis sites / twists.
import random, itertools, abstract as ab
def build(order_segments, background, contents):
    """order_segments: list of slot names in the order they appear along k, e.g. ['I1','b','I2',...];
    background tokens at 'b' slots; contents: dict segment -> token list."""
    D=[]
    for sl in order_segments:
        if sl in contents: D+=contents[sl]
        else: D+=background[sl]
    return D
def qsign(D):  # product of (-1)^tau over chords: converts upstairs-sign normalisation to quotient-sign normalisation
    _,tau=ab.labels(D); s=1
    for v in tau.values(): s*=(-1)**v
    return s
rnd=random.Random(3); res={'w(J) eps=+1':[0,0],'w(J) eps^q=+1':[0,0],'W(Jhat) eps^q=+1':[0,0]}
for trial in range(150):
    nb=rnd.choice([0,1,2])                     # number of background slots
    slots=['I1','I2','I3']+['b%d'%k for k in range(nb+3)]
    rnd.shuffle(slots)
    # background: random tokens; chords in background have both ends in background slots
    back={s:[] for s in slots if s[0]=='b'}
    bkeys=list(back)
    nbc=rnd.choice([0,1]) if bkeys else 0
    for c in range(nbc):
        for _ in range(2): back[rnd.choice(bkeys)].append(('E',10+c))
    if bkeys and rnd.random()<0.5: back[rnd.choice(bkeys)].append(('O',20))
    for s in bkeys:
        if rnd.random()<0.5: back[s].append(('T',))
        rnd.shuffle(back[s])
    # sheets of the segments are realised by the twists between them (already random); compute D1..D4
    e12a,e12b,e13a,e13b,e23a,e23b=('E',0),('E',0),('E',1),('E',1),('E',1),('E',1)
    D1=build(slots,back,{'I1':[('E',1),('E',0)],'I2':[('E',0)],'I3':[('E',1)]})
    D2=build(slots,back,{'I1':[('E',0),('E',1)],'I2':[('E',0)],'I3':[('E',1)]})
    D3=build(slots,back,{'I1':[('E',0)],'I2':[('E',1),('E',0)],'I3':[('E',1)]})
    D4=build(slots,back,{'I1':[('E',0)],'I2':[('E',0),('E',1)],'I3':[('E',1)]})
    Ds=[D1,D2,D3,D4]
    v=[ab.w(D) for D in Ds]
    res['w(J) eps=+1'][0 if v[0]-v[1]+v[2]-v[3]==0 else 1]+=1
    vq=[qsign(D)*x for D,x in zip(Ds,v)]
    res['w(J) eps^q=+1'][0 if vq[0]-vq[1]+vq[2]-vq[3]==0 else 1]+=1
    offs=lambda D: sorted(set(t[1] for t in D if t[0]=='E')); ons=lambda D: sorted(set(t[1] for t in D if t[0]=='O'))
    vh=[qsign(D)*ab.W_hat(D,offs(D),ons(D)) for D in Ds]
    res['W(Jhat) eps^q=+1'][0 if vh[0]-vh[1]+vh[2]-vh[3]==0 else 1]+=1
print('4T [t12, t13+t23] = 0  (holds, fails):',res)
