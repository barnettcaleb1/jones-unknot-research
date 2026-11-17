# Is the Lemma 6.3 test discriminating?  Compare with (i) Gamma_1 reversed, (ii) Phi' ending in y2
# (word criterion violated), (iii) mirror reading of Fig. 6.3 (word reversed).
import random, sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lp import *
from curves import *
from lemma63 import PUSH, push_word, W, LEMMA63, rand_reduced

def frac_bad(words, G):
    nb = 0; nt = 0; types = set()
    for Vy in words:
        R = analyse(push_word(Vy) + push_word(G), 4)
        bad = [d for d in R['disks'] if LEMMA63.get(d['P']) != ('chg' if d['changing'] else 'pres')]
        for d in bad: types.add((tuple(sorted(d['P'])), 'chg' if d['changing'] else 'pres'))
        nt += 1; nb += bool(bad)
    return nb, nt, sorted(types)

random.seed(3)
good = [w for w in (rand_reduced(random.randint(1, 5)) for _ in range(120)) if w[-1] != 2][:60]
endy2 = [w + [2] for w in (rand_reduced(random.randint(0, 4)) for _ in range(200)) if (not w or w[-1] != -2)][:60]
print("Gamma_1, Phi' not ending in y2 (criterion holds):", frac_bad(good, W)[:2])
print("Gamma_1, Phi' ending in y2 (criterion fails):     ", frac_bad(endy2, W))
Winv = finv(W)
good_inv = [w for w in good if fred(w + Winv) == w + Winv][:60]
print("Gamma_1^-1 instead of Gamma_1:                     ", frac_bad(good_inv, Winv))
Wrev = list(reversed(W))
good_rev = [w for w in good if fred(w + Wrev) == w + Wrev][:60]
print("reversed word (mirror reading) instead of Gamma_1: ", frac_bad(good_rev, Wrev))
