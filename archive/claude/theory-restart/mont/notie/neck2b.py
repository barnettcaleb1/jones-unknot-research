from neck2 import *
import random
rnd=random.Random(11)
pool=normal_seqs(3,3)
for _ in range(300):
    k=rnd.randint(4,7); s=[rnd.choice([m for m in range(-4,5) if m]) for _ in range(k)]
    if s[0]==-1: s[0]=-2
    pool.append(tuple(s))
for trial in range(20000):
    nb=rnd.choice([2,2,3,3,4,5])
    ss=[rnd.choice(pool) for _ in range(nb)]
    mu=rnd.choice([m for m in range(-6,7) if m]); N=rnd.randint(-4,6)
    kind,ratio=predict_top(mu,N,ss)
    if kind=='tie' or ratio!=1: continue
    ssm=[mirror_seq(s) for s in ss]
    kb,rb=predict_top(-mu,nb-N,ssm)
    Jv=neck(mu,N,[box(s) for s in ss])
    print(mu,N,ss,'bottom:',kb,rb,'span',span(Jv))
