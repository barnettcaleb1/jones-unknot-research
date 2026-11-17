import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
def blocks(word, lab):
    cr = crossings_of(word)
    bl = []
    for n in cr:
        if not bl or bl[-1][0] != lab[n] or len(bl[-1][1]) == 4 or (lab[n][0]=='twist' and len(bl[-1][1])==2):
            bl.append((lab[n], []))
        bl[-1][1].append(n)
    return cr, bl
def fmt(word, lab, bits):
    cr, bl = blocks(word, lab)
    pos = {n: j for j, n in enumerate(cr)}
    out = []
    for (kind, idx), ns in bl:
        s = ''
        for n in ns:
            b = bits[pos[n]]
            is_e = (b == 1) == one_is_e(word[n][0])
            s += 'e' if is_e else '1'
        out.append('%s%s:%s' % (kind[0], word[ns[0]][0], s))
    return ' '.join(out)
if __name__ == '__main__':
    half, orient, sym = read_kht(sys.argv[1])
    tw = (len(sys.argv) > 2 and sys.argv[2] == 'tw')
    word, lab, wr = quotient_word(half, with_twists=tw)
    for sign in (+1, -1):
        M, st = extreme_states(word, sign=sign)
        print('sign', sign, 'M', M, 'n states', len(st))
        for (bits, ones, circ) in sorted(st, key=lambda t: -t[1])[:40]:
            print('  |s|=%d k=%d  %s' % (ones, circ, fmt(word, lab, bits)))
