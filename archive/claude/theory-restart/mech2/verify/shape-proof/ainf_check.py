#!/usr/bin/env python3
"""Check the A-infinity relations of my implementation of B^infty (F_2) on all composable basis sequences
of length n with powers <= K.  Also: list all non-zero mu_4, and check the reversal symmetry."""
import sys
from binf import *
from binf import _add

def ainf_defect(seq):
    """seq in source order; returns the F_2-sum of all terms mu(.., mu(..), ..)."""
    n = len(seq)
    tot = {}
    for s in range(2, n + 1):                 # mu_1 = 0
        for r in range(0, n - s + 1):
            t = n - r - s
            outer_n = r + 1 + t
            if outer_n < 2:
                continue
            inner = mu_src(seq[r:r + s])
            for b in inner:
                res = mu_src(seq[:r] + (b,) + seq[r + s:])
                for e in res:
                    _add(tot, e)
    return tot

def composable_seqs(n, K):
    bas = basis(K)
    def rec(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for a in bas:
            if not prefix or right(prefix[-1]) == left(a):
                prefix.append(a)
                yield from rec(prefix)
                prefix.pop()
    yield from rec([])

if __name__ == '__main__':
    # 1. all non-zero mu_4 on basis elements with powers <= 5 (path order printed)
    K = 5
    print('non-zero mu_4 on basis 4-tuples with powers <= %d, printed in SOURCE order mu_4(a_1,a_2,a_3,a_4):' % K)
    fam = {}
    cnt = 0
    for seq in composable_seqs(4, K):
        res = mu_src(seq)
        if res:
            cnt += 1
            assert len(res) == 1
            b = list(res)[0]
            pat = tuple((a[0], 'k' if a[1] > 1 else 1) for a in seq)
            fam.setdefault(tuple(a[0] + ('' if a[1] == 1 else '^k') for a in seq), []).append((seq, b))
    for pat, lst in sorted(fam.items()):
        ex = lst[-1]
        print('   pattern', pat, ': %d tuples, e.g. mu_4(%s) = %s' % (len(lst), ', '.join(name(a) for a in ex[0]), name(ex[1])))
    print('   total', cnt)
    # 2. reversal symmetry: mu on reversed argument order with the two S's swapped by the anti-automorphism
    def anti(a):   # anti-automorphism of B: reverse arrows; (kind,k,src,tgt) -> (kind,k,tgt,src)
        return (a[0], a[1], a[3], a[2])
    for n in (4, 6, 8):
        bad = 0; tot = 0
        for dseq in disk_sequences(n):
            rev = tuple(anti(a) for a in reversed(dseq))
            tot += 1
            if rev not in disk_sequences(n):
                bad += 1
        print('E_%d closed under (reverse order + reverse arrows): %s (%d sequences)' % (n, bad == 0, tot))
    # 3. A-infinity relations
    for n, K in ((3, 4), (5, 4), (7, 3)):
        bad = 0; tot = 0; nz = 0
        for seq in composable_seqs(n, K):
            tot += 1
            d = ainf_defect(seq)
            if d:
                bad += 1
                if bad <= 5:
                    print('   DEFECT', [name(a) for a in seq], d)
        print('A-infinity relation, n = %d, powers <= %d: %d composable sequences, %d violations' % (n, K, tot, bad))
