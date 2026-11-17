import sys, collections, time
from cube import Diagram, quotient_word, word_str, CONN_H
from indcx import reduced_betti, fold_reduce
from search_half import gen_words
maxc = int(sys.argv[1])
stats = collections.Counter(); ex = {}; sizes = collections.Counter()
t0 = time.time(); cnt = 0
for half in gen_words(maxc):
    try:
        q = quotient_word(half, True, 0); D = Diagram(q, 1)
    except ValueError: continue
    if D.components_through_crossings()[0]: continue
    cnt += 1
    for which in 'AB':
        L = D.lando(which)
        if L['conn'] != CONN_H: stats['nonH'] += 1; continue
        red, contr = fold_reduce(L['adj'])
        if contr: stats['contractible-fold'] += 1; continue
        sizes[len(red)] += 1
        b = reduced_betti(red, reduce=False)
        key = tuple(sorted(b.items()))
        stats[key] += 1
        if key not in ex: ex[key] = (word_str(half), which, len(red))
print('diagrams', cnt, 'time %.1f' % (time.time() - t0))
for k, v in sorted(stats.items(), key=lambda kv: -kv[1]): print(v, k, ex.get(k))
print('fold-reduced sizes:', sorted(sizes.items()))
