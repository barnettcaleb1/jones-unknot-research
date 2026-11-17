from t_common import *
import khtrun, random, io, contextlib
exec(open('t_random.py').read().split('seen = 0')[0].split('random.seed')[0])
src = open('t_random.py').read(); exec(src[src.index('def random_word'):src.index('seen = 0')])
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
NT = int(sys.argv[2]) if len(sys.argv) > 2 else 12
words = [('q31', quotient_word('l1.y0.y0.y1.u2')), ('q41a', quotient_word('l1.y0.y0.x1.u2')), ('q41b', quotient_word('l1.x0.x0.y1.u2'))]
i = 0
while len(words) < 3 + NT:
    w = random_word(9)
    try: D = closure13(w)
    except AssertionError: continue
    if D.ncomp != 2 or D.comp[D.marks[0]] == D.comp[D.marks[1]] or sum(D.mixed) == 0: continue
    words.append(('rnd%d_%d' % (int(sys.argv[1]) if len(sys.argv) > 1 else 7, i), w)); i += 1
nok = 0
for name, w in words:
    D = closure13(w)
    C = Complex(D, deform=False)
    E1 = homology_bigraded(C)
    g = khtrun.run(name, w)
    if g is None:
        print(name, w, 'kht++ failed/timeout'); continue
    B = khtrun.bgens(g)
    # compare up to an overall shift
    def norm(cnt):
        m = min(cnt); return collections.Counter({(h - m[0], q - m[1]): v for (h, q), v in cnt.items()})
    same = norm(B) == norm(E1)
    nok += same
    sh = (min(E1)[0] - min(B)[0], min(E1)[1] - min(B)[1])
    print('%-10s %-45s dim N(kht++ b-gens) = %d, dim H(X1X2 C,d0) = %d, equal up to shift: %s (shift %s)' % (name, w, sum(B.values()), sum(E1.values()), same, sh))
    if not same:
        print('    kht++ :', fmt(B)); print('    mine  :', fmt(E1))
print('agree:', nok, 'of', len(words))
