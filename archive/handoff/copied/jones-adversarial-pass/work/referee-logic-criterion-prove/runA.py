import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
conjs = {'c': [], 'x': [3], 'y': [4, 3, 2, 3]}
G = gen_mats(conjs)
print('triple cxy, syllables with |e|<=4, up to 3 syllables:')
enumerate_words(G, 'cxy', 3, exps=(1, -1, 2, -2, 3, -3, 4, -4))
print('triple cxy, syllables |e|<=2, up to 5 syllables:')
enumerate_words(G, 'cxy', 5, exps=(1, -1, 2, -2))
