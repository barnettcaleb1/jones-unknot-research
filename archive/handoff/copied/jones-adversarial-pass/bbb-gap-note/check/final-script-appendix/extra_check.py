# Extra checks for the Prop 4(a) proof text and the 28-letter A_i4 word; written from scratch.
def inv(w): return [-x for x in w[::-1]]
def cm(x, y): return x + y + inv(x) + inv(y)
def red(w):
    st = []
    for c in w:
        if st and st[-1] == -c: st.pop()
        else: st.append(c)
    return st
def delete(w, n, d):
    pos, out = list(range(1, n + 1)), []
    for a in w:
        k = abs(a); l, r = pos[k-1], pos[k]
        if d not in (l, r):
            kk = k - 1 if pos.index(d) + 1 < k else k
            out.append(kk if a > 0 else -kk)
        pos[k-1], pos[k] = r, l
    return out
A = {1: [3, 2, 1, 1, -2, -3], 2: [3, 2, 2, -3], 3: [3, 3]}
# Which strand deletions kill which A_i4 (as words that freely reduce to empty)?
for d in (1, 2, 3, 4):
    print("delete strand", d, {i: ("killed" if red(delete(A[i], 4, d)) == [] else "survives: " + str(red(delete(A[i], 4, d)))) for i in A})
# [K4,K4] word in the A_i4 basis: a1,a2,a3 = A14,A24,A34; delta = a1 a2 a3
delta = [1, 2, 3]
b = cm(cm([1], [2]), [3])
w = red(cm(inv(delta) + inv(delta), b))
print("Phi0 = [delta^-2, b] in basis A_i4:", len(w), "letters;", w)
print("exponent sums:", {i: sum((1 if c == i else -1 if c == -i else 0) for c in w) for i in (1, 2, 3)})
