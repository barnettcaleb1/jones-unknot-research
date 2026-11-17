from t_common import *
for name, half in [('3_1 (LHT) quotient', 'l1.y0.y0.y1.u2'), ('4_1 inversion 1 quotient', 'l1.y0.y0.x1.u2'), ('4_1 inversion 2 quotient', 'l1.x0.x0.y1.u2')]:
    w = quotient_word(half)
    print('word:', w)
    D = closure13(w)
    if D.ncomp != 2:
        print(name, ': closure has', D.ncomp, 'components; adding one twist pair'); continue
    analyse(D, name)
    print()
