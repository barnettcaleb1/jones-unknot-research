import sys, time, random
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont/cx/cert')
import diagram, wirtinger, tietze, refs, replay
# 1. checker's Wirtinger == certifier's Wirtinger, literally
ws = refs.random_halfwords(3, 300, minlen=4, maxlen=18, width2_frac=0.5, w2len=(1, 16))
same = 0
for w in ws:
    pd = diagram.pd_from_halfword(w)
    a = wirtinger.wirtinger(pd); b = replay.wirtinger_presentation(w)
    if (list(a[0]), [tuple(r) for r in a[1]]) == (list(b[0]), [tuple(r) for r in b[1]]): same += 1
    else: print('DIFF', w, a, b); break
print('identical Wirtinger presentations', same, 'of', len(ws))
# 2. canonical forms agree
rnd = random.Random(1); agree=0
for _ in range(3000):
    w = tuple(rnd.choice([1,-1,2,-2,3,-3]) for _ in range(rnd.randint(0,30)))
    if tietze.canon_word(w) == replay.canonical_cyclic(w): agree += 1
print('canonical cyclic words agree', agree, '/ 3000')
