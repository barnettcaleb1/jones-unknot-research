#!/usr/bin/env python3
"""
Referee's independent implementation of the A-infinity algebra B^infty of
Kotelskiy-Watson-Zibrowius (arXiv:2202.01460, Definition 4.2), over F_2.

Conventions (mine, fixed here):
  idempotents 'b' (= bullet, Q_0) and 'c' (= circle, Q_infty).
  A basis element is a tuple (kind, k, src, tgt): an ARROW from src to tgt,
     kind 'I' (idempotent, k = 0), 'D' (D^k, src = tgt), 'S' (S^k, tgt = src iff k even).
  mul(a2, a1) = a2 . a1 = "first a1, then a2"  (function-composition order, as in the source,
     where an element with left idempotent X and right idempotent Y is an arrow Y -> X).
  A "source-order" sequence (a_1, ..., a_n) is a sequence with tgt(a_{i+1}) = src(a_i), i.e. a_1 a_2 ... a_n is a
     composable product; as a path it is traversed a_n first, ..., a_1 last.
  A "path-order" sequence (p_1, ..., p_n) is traversed p_1 first; source order = reversed path order.
Everything below is written from the definition in the paper, not from the project's scripts.
"""
from itertools import product

B, C = 'b', 'c'
IDEMS = (B, C)

def other(X):
    return C if X == B else B

def I(X):
    return ('I', 0, X, X)

def D(k, X):
    assert k >= 1
    return ('D', k, X, X)

def S(k, X):
    """S^k starting at X (arrow from X)."""
    assert k >= 1
    return ('S', k, X, X if k % 2 == 0 else other(X))

def Sto(k, Y):
    """S^k ending at Y."""
    return ('S', k, Y if k % 2 == 0 else other(Y), Y)

def qdeg(a):
    """|a|: the amount by which an arrow labelled a raises q (|S| = 1, |D| = 2)."""
    return {'I': 0, 'D': 2 * a[1], 'S': a[1]}[a[0]]

def name(a):
    if a[0] == 'I':
        return '1'
    return a[0] + ('' if a[1] == 1 else '^%d' % a[1])

def mul(a2, a1):
    """a2 . a1 (first a1, then a2). Returns a basis element or None for zero / not composable."""
    if a1[3] != a2[2]:
        return None
    if a1[0] == 'I':
        return a2
    if a2[0] == 'I':
        return a1
    if a1[0] != a2[0]:
        return None              # D S = S D = 0
    return (a1[0], a1[1] + a2[1], a1[2], a2[3])

def basis(maxpow, with_idem=True):
    out = []
    for X in IDEMS:
        if with_idem:
            out.append(I(X))
        for k in range(1, maxpow + 1):
            out.append(D(k, X))
            out.append(S(k, X))
    return out

# ---------------------------------------------------------------------------------------------
# Disk sequences, in SOURCE order, literally as in Definition 4.2.
# Source notation XaY  <->  my arrow from Y to X, i.e. (kind, k, src=Y, tgt=X).
def src_elt(kind, k, left, right):
    return (kind, k, right, left)

def left(a):
    return a[3]

def right(a):
    return a[2]

def E4():
    o, s = C, B     # o = circle, s = bullet (solid)
    seqs = [
        (src_elt('S', 1, o, s), src_elt('D', 1, s, s), src_elt('S', 1, s, o), src_elt('D', 1, o, o)),
        (src_elt('D', 1, s, s), src_elt('S', 1, s, o), src_elt('D', 1, o, o), src_elt('S', 1, o, s)),
        (src_elt('S', 1, s, o), src_elt('D', 1, o, o), src_elt('S', 1, o, s), src_elt('D', 1, s, s)),
        (src_elt('D', 1, o, o), src_elt('S', 1, o, s), src_elt('D', 1, s, s), src_elt('S', 1, s, o)),
    ]
    return set(seqs)

def interpose(seq):
    """All sequences obtained from seq (source order) by one interposition (the four rules of Def. 4.2)."""
    out = set()
    n = len(seq)
    for i in range(n - 1):
        a, b = seq[i], seq[i + 1]
        # rule (..., D^k_X, X S^l, ...) -> (..., D^{k+1}_X, X S X', X' D X', X' S^{l+1}, ...)
        if a[0] == 'D' and b[0] == 'S' and right(a) == left(b):
            X = right(a); Xp = other(X)
            new = (src_elt('D', a[1] + 1, X, X), src_elt('S', 1, X, Xp), src_elt('D', 1, Xp, Xp),
                   src_elt('S', b[1] + 1, Xp, right(b)))
            out.add(seq[:i] + new + seq[i + 2:])
        # rule (..., S^k_X, X D^l, ...) -> (..., S^{k+1}_X', X' D X', X' S X, X D^{l+1}, ...)
        if a[0] == 'S' and b[0] == 'D' and right(a) == left(b):
            X = right(a); Xp = other(X)
            new = (src_elt('S', a[1] + 1, left(a), Xp), src_elt('D', 1, Xp, Xp), src_elt('S', 1, Xp, X),
                   src_elt('D', b[1] + 1, X, X))
            out.add(seq[:i] + new + seq[i + 2:])
    return out

def check_seq(seq):
    """sanity: consecutive entries composable in source order, cyclically closed, S parity right."""
    n = len(seq)
    for i in range(n):
        a, b = seq[i], seq[(i + 1) % n]
        assert right(a) == left(b), seq
    for a in seq:
        if a[0] == 'D':
            assert a[2] == a[3]
        else:
            assert (a[2] == a[3]) == (a[1] % 2 == 0), a

_E = {}
def disk_sequences(n, close_under_rotation=False):
    """E_n (n even >= 4), source order."""
    key = (n, close_under_rotation)
    if key in _E:
        return _E[key]
    if n == 4:
        res = E4()
    else:
        res = set()
        for seq in disk_sequences(n - 2, close_under_rotation):
            res |= interpose(seq)
    if close_under_rotation:
        res2 = set()
        for seq in res:
            for r in range(len(seq)):
                res2.add(seq[r:] + seq[:r])
        res = res2
    for seq in res:
        check_seq(seq)
    _E[key] = res
    return res

# ---------------------------------------------------------------------------------------------
# Higher products.  mu_src(args): args in SOURCE order (a_1, ..., a_n).  Returns a dict {basis element: 1} (F_2).
def _add(dct, b):
    if b in dct:
        del dct[b]
    else:
        dct[b] = 1

def factor_right(a, d):
    """solve a = d . b  (b first, then d), b a basis element or idempotent; return b or None."""
    if a[0] != d[0] or a[3] != d[3]:
        return None
    k = a[1] - d[1]
    if k < 0:
        return None
    if k == 0:
        return I(d[2]) if a == d else None
    b = (a[0], k, a[2], d[2])
    return b if mul(d, b) == a else None

def factor_left(a, d):
    """solve a = b . d  (d first, then b)."""
    if a[0] != d[0] or a[2] != d[2]:
        return None
    k = a[1] - d[1]
    if k < 0:
        return None
    if k == 0:
        return I(d[3]) if a == d else None
    b = (a[0], k, d[3], a[3])
    return b if mul(b, d) == a else None

def mu_src(args, rot=False):
    n = len(args)
    out = {}
    if n == 2:
        p = mul(args[0], args[1])
        if p is not None:
            _add(out, p)
        return out
    if n % 2 == 1 or n < 4:
        return out
    if any(a[0] == 'I' for a in args):
        return out
    for dseq in disk_sequences(n, rot):
        # (a_1, ..., a_{n-1}, a_n b) -> b
        if all(args[i] == dseq[i] for i in range(n - 1)):
            b = factor_right(args[n - 1], dseq[n - 1])       # a_n b : first b then a_n
            if b is not None:
                _add(out, b)
                if b[0] == 'I':
                    continue                                    # the two descriptions coincide for b = 1
        # (b a_1, a_2, ..., a_n) -> b
        if all(args[i] == dseq[i] for i in range(1, n)):
            b = factor_left(args[0], dseq[0])                   # b a_1 : first a_1 then b
            if b is not None and b[0] != 'I':
                _add(out, b)
    return out

def mu_path(path, rot=False):
    """path = labels in PATH order (first arrow first)."""
    return mu_src(tuple(reversed(path)), rot)

def composable_path(path):
    return all(path[i][3] == path[i + 1][2] for i in range(len(path) - 1))

if __name__ == '__main__':
    for n in (4, 6, 8, 10):
        E = disk_sequences(n)
        Er = disk_sequences(n, True)
        print('E_%d: %d sequences; closed under rotation: %s (rotation closure has %d)' % (n, len(E), E == Er, len(Er)))
    print('E_6 (source order):')
    for seq in sorted(disk_sequences(6)):
        print('   ', ' , '.join('%s%s%s' % (left(a), name(a), right(a)) for a in seq))
