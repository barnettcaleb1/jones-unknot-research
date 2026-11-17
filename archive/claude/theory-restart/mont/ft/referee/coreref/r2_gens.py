# Referee: other generators. (a) own random Morse half-words with up to WMAX half-strands; (b) Montesinos words (words.mont);
# (c) long two-bridge words s.l1.W.u2; (d) swap words with several caps/cups. Tests F1, moment congruences, Conjecture D.
import sys, random, collections, itertools
import rlib, lp
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import words
from rlib import Fr
def morse_word(rnd,steps,WMAX,axis=True):
    w=1; out=[]
    for _ in range(steps):
        opts=[]
        if w+2<=WMAX: opts+=['cap']*2
        if w>=3: opts+=['cup']*2
        opts+=['x']*5
        o=rnd.choice(opts)
        if o=='cap': i=rnd.randint(1,w+1); out.append(rnd.choice('lr')+str(i)); w+=2
        elif o=='cup': i=rnd.randint(1,w-1); out.append('u'+str(i)); w-=2
        else:
            lo=0 if axis else 1
            if w-1<lo: continue
            i=rnd.randint(lo,w-1); out.append(rnd.choice('xy')+str(i))
    while w>1:
        i=rnd.randint(1,w-1); out.append('u'+str(i)); w-=2
    return 's.'+'.'.join(out)
def test(w,st,fails,J=None):
    J=lp.J(w) if J is None else J
    if J is None: st['not knot']+=1; return
    V=rlib.VK(w)
    if V is None: st['VK None']+=1; return
    Jm1=rlib.psub(J,rlib.ONE)
    if not Jm1: st['J=1']+=1; st['J=1 & V!=1' if V!={0:1} else 'J=1 & V=1']+=1; return
    st['n']+=1
    if rlib.divmod_laurent(Jm1,rlib.D7) is None: st['F1 FAIL']+=1; fails.append(('F1',w))
    a2=rlib.a2V(V); M2=rlib.mom(J,2); M3=rlib.mom(J,3); M4=rlib.mom(J,4)
    if M2!=-24*a2: st['M2 FAIL']+=1; fails.append(('M2',w))
    if M3%36 or (M3//36-a2)%2: st['M3 FAIL']+=1; fails.append(('M3',w))
    if a2==0:
        st['core']+=1
        if M3%72 or (M4-16*M3)%288: st['core cong FAIL']+=1; fails.append(('core',w))
    f=rlib.psub(rlib.subst_neg(J),rlib.subst_pow(V,2))
    if f and rlib.divmod_laurent(f,rlib.MODD) is None:
        st['ConjD FAIL']+=1; fails.append(('D',w))
        for nm,cp in (('Phi5',rlib.C5),('Phi3',rlib.C3),('t+1',rlib.T1),('(t-1)^3',rlib.ppow(rlib.TM,3))):
            if rlib.divmod_laurent(f,cp) is None: st['D fails '+nm]+=1
    else: st['ConjD ok']+=1
mode=sys.argv[1]; st=collections.Counter(); fails=[]
if mode=='morse':
    rnd=random.Random(int(sys.argv[2])); seen=set()
    while st['n']<int(sys.argv[3]):
        w=morse_word(rnd,rnd.randint(6,int(sys.argv[4])),int(sys.argv[5]))
        if w in seen: continue
        seen.add(w); test(w,st,fails)
elif mode=='mont':
    rnd=random.Random(int(sys.argv[2])); seen=set()
    while st['n']<int(sys.argv[3]):
        m=rnd.choice([-3,-2,-1,1,2,3]); k=rnd.randint(2,4)
        rows=[rnd.choice([-1,1])*rnd.choice([3,5,7,9]) for _ in range(k)]
        ax=rnd.choice('xy'); off=rnd.choice('xy'); tw=rnd.choice('xy')
        try: w=words.mont(m,rows,tw=tw,ax=ax,off=off)
        except AssertionError: continue
        if w in seen: continue
        seen.add(w); test(w,st,fails)
elif mode=='2br':
    rnd=random.Random(int(sys.argv[2])); seen=set()
    while st['n']<int(sys.argv[3]):
        L=rnd.randint(8,int(sys.argv[4]))
        W=[rnd.choice(['y0','x0','x1','y1']) for _ in range(L)]
        if any(W[i][1:]==W[i+1][1:] and W[i][0]!=W[i+1][0] for i in range(L-1)): continue
        w='s.l1.'+'.'.join(W)+'.u2'
        if w in seen: continue
        seen.add(w); test(w,st,fails)
elif mode=='swap':
    rnd=random.Random(int(sys.argv[2])); seen=set()
    while st['n']<int(sys.argv[3]):
        w=morse_word(rnd,rnd.randint(6,int(sys.argv[4])),int(sys.argv[5]),axis=False)
        if w in seen: continue
        seen.add(w); test(w,st,fails)
print(mode,sys.argv[2:],dict(sorted(st.items()))); print('fails:',fails[:8])
