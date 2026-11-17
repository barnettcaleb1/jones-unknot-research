"""Referee's sample generators (independent of the builder's): own random half-word walk, fs.gen long words, Montesinos words."""
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, words
def own_walk(rnd, L, pax=0.25, pcap=0.15, maxw=4):
    n=1; w=[]
    for _ in range(L):
        r=rnd.random()
        if r<pcap and n<2*maxw+1:
            i=rnd.randint(1,n+1); w.append(rnd.choice('lr')+str(i)); n+=2
        elif r<pcap+0.12 and n>=3:
            i=rnd.randint(1,n-1); w.append('u'+str(i)); n-=2
        elif r<pcap+0.12+pax:
            w.append(rnd.choice('xy')+'0')
        elif n>=2:
            i=rnd.randint(1,n-1); w.append(rnd.choice('xy')+str(i))
        else:
            w.append(rnd.choice('xy')+'0')
    while n>1:
        if n>=3 and rnd.random()<0.5:
            i=rnd.randint(1,n-1); w.append(rnd.choice('xy')+str(i))
        i=rnd.randint(1,n-1); w.append('u'+str(i)); n-=2
    return 's.'+'.'.join(w)
def sample(rnd, kind):
    if kind=='walk': return own_walk(rnd, rnd.randint(10,22))
    if kind=='long': return fs.gen(rnd, rnd.randint(14,24))
    if kind=='mont':
        m=rnd.choice([-3,-2,-1,1,2,3]); k=rnd.choice([2,3])
        rows=[rnd.choice([-7,-5,-3,3,5,7]) for _ in range(k)]
        return words.mont(m,rows,tw=rnd.choice('xy'),ax=rnd.choice('xy'),off=rnd.choice('xy'))
def flip(word, idx):
    t=word.split('.')
    for i in idx: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
def sites(word, mode):
    t=word.split('.')
    if mode=='axis': return [i for i,a in enumerate(t) if a in ('x0','y0')]
    if mode=='off': return [i for i,a in enumerate(t) if a[0] in 'xy' and a[1:].isdigit() and a[1:]!='0']
    return [i for i,a in enumerate(t) if a[0] in 'xy' and a[1:].isdigit()]
