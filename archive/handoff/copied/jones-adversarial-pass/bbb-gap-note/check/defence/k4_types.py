# Which disk types occur for (i) random elements of K4 (random y-words), (ii) random y-words ending
# in a few specific letters?  Used to judge how discriminating the Lemma 6.3 test is.
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lp import *
from curves import *
from lemma63 import push_word, W, LEMMA63, rand_reduced
random.seed(11)
def types_for(words):
    T = {}; nbad = 0
    for w in words:
        R = analyse(push_word(w), 4)
        bad = False
        for d in R['disks']:
            key = (tuple(sorted(d['P'])), 'chg' if d['changing'] else 'pres')
            T[key] = T.get(key, 0) + 1
            if LEMMA63.get(d['P']) != key[1]: bad = True
        nbad += bad
    return nbad, len(words), dict(sorted(T.items(), key=lambda x: (len(x[0][0]), x)))
words = [rand_reduced(random.randint(1, 7)) for _ in range(200)]
print("random K4 elements (y-words of length 1-7): #violating Lemma 6.3 list, #tested, types:")
print(types_for(words))
for last in ([1], [-1], [2], [-2], [3], [-3]):
    ws = []
    while len(ws) < 60:
        w = rand_reduced(random.randint(1, 6))
        if w[-1] == last[0]: ws.append(w)
    nb, nt, T = types_for(ws)
    print("ending in y%+d:" % last[0], nb, "of", nt, "violate; types:", sorted(T))
