import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
from fullcube import full_homology
from badblocks import describe
def run(hw):
    half = parse_word(hw)
    word, lab, wr = quotient_word(half, with_twists=False)
    n = len(crossings_of(word))
    betti, sizes = full_homology(word)
    M, st = extreme_states(word, sign=1)
    m, st0 = extreme_states(word, sign=-1)
    pts = sorted(betti.items())
    qs = [q for (h, q), b in pts]
    top = [(h, q) for (h, q), b in pts if q == max(qs)]
    bot = [(h, q) for (h, q), b in pts if q == min(qs)]
    print('%-28s n=%d w=%d N=%s' % (hw, n, wr, pts))
    print('    top corner (%d,%d) nE=%d defect %s | %s' % (n, M, len(st), [(n - h, M - q) for h, q in top], describe(half, 1)[0]))
    print('    bot corner (0,%d) nE=%d defect %s | %s' % (m, len(st0), [(h, q - m) for h, q in bot], describe(half, 0)[0]))
for hw in sys.argv[1:]:
    run(hw)
