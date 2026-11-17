# If lambda_- were an invariant of (K,h), it would vanish on every half-word representing the unknot
# (the unknot has a unique strong inversion).  Test on random words whose K has V=1 and Delta=1 and few crossings.
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, chord, kauffman, diag, flat_search as fs
rnd=random.Random(11); stat={}; ex={}
for trial in range(4000):
    w=fs.gen(rnd,rnd.randint(4,9))
    if not w: continue
    J=lp.J(w)
    if J is None: continue
    kb=kauffman.bracket(w)
    if kb is None or len({e for e,c in kb.items() if c})!=1: continue
    if J!={0:1}: stat['J!=1 for V=1']=stat.get('J!=1 for V=1',0)+1; continue
    lc=chord.lam_counts(w)
    key=('lm',lc['lm'])
    stat[key]=stat.get(key,0)+1; ex.setdefault(key,w)
print(stat); print(ex)
