# Is lambda_- invariant under the type-B braid relation (an equivariant isotopy)?  Check J equality first.
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, chord, flat_search as fs
rnd=random.Random(5)
pats=[]
for a in 'xy':
    for b in 'xy':
        pats.append(('%s0.%s1.%s0.%s1'%(a,b,a,b),'%s1.%s0.%s1.%s0'%(b,a,b,a)))
stat={}
for trial in range(400):
    w=fs.gen(rnd,rnd.randint(6,12))
    if not w or lp.J(w) is None: continue
    toks=w.split('.')
    # insert after a random position where half-strand count >=2 : try positions, keep valid ones
    pos=rnd.randint(2,len(toks)-1)
    for L,R in pats:
        w1='.'.join(toks[:pos]+L.split('.')+toks[pos:]); w2='.'.join(toks[:pos]+R.split('.')+toks[pos:])
        J1=lp.J(w1); J2=lp.J(w2)
        if J1 is None or J2 is None: continue
        same=(J1==J2)
        l1=chord.lam_counts(w1)['lm']; l2=chord.lam_counts(w2)['lm']
        key=(L,same,l1==l2)
        stat[key]=stat.get(key,0)+1
for k,v in sorted(stat.items()): print(k,v)
