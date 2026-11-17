from fractions import Fraction
from khparse import label_info
def jk_from_kh(khc):
    for comp in khc:
        li = label_info(comp['label'])
        if li and li['type'] == 'r':
            k = int(li['slope']); qr = li['q']
            j24 = qr - Fraction(k * (abs(k) + 2), abs(k) + 1)
            assert j24.denominator == 1 and j24.numerator % 24 == 0, (k, qr)
            return k, j24.numerator // 24
    raise ValueError
