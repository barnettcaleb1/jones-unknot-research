# Depth of [Phi0, s3 Phi0 s3^-1] in all four conventions, and of the mirror word (opposite orientation),
# using the shipped script's own helper functions (definitions only, lines before the checks).
src = open('$HOME/jones-adversarial-pass/bbb-gap-note/phi0_check.py', encoding='utf-8').read()
ns = {}
exec(src[:src.index('FAILS = []')], ns)
inv, comm, burau, depth, at, is_I = ns['inv'], ns['comm'], ns['burau'], ns['depth'], ns['at'], ns['is_I']
A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
X = [1, 2] * 6
b = comm(comm(A14, A24), A34)
Phi0 = comm(X, b)
C = comm(Phi0, [3] + Phi0 + [-3])
mirror = lambda w: [-a for a in w]
for conv in ('U', 'UT', 'R', 'RT'):
    print(conv, 'depth C =', depth(burau(C, 4, conv)), ' depth mirror(C) =', depth(burau(mirror(C), 4, conv)))
mmul = ns['mmul']
s3c = [3] + Phi0 + [-3]
for conv in ('U', 'UT', 'R', 'RT'):
    P, Q = burau(Phi0, 4, conv), burau(s3c, 4, conv)
    print(conv, 'images of Phi0 and s3 Phi0 s3^-1 commute:', mmul(P, Q) == mmul(Q, P))
