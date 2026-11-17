import re, sys, difflib
def sents(path):
    txt = open(path, encoding='utf-8').read()
    out = []
    for ln, line in enumerate(txt.split('\n'), 1):
        # split on sentence ends followed by space and capital/backslash/$
        parts = re.split(r'(?<=[.?!])\s+(?=[A-Z\\$(])', line.strip())
        for p in parts:
            p = p.strip()
            if p:
                out.append((ln, p))
    return out
a = sents(sys.argv[1]); b = sents(sys.argv[2])
sa = [s for _, s in a]; sb = [s for _, s in b]
sm = difflib.SequenceMatcher(a=sa, b=sb, autojunk=False)
nchg = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        continue
    print('=' * 70)
    print(op, 'old lines', sorted(set(a[i][0] for i in range(i1, i2))), 'new lines', sorted(set(b[j][0] for j in range(j1, j2))))
    for i in range(i1, i2):
        print('  - [%d] %s' % (a[i][0], a[i][1][:400]))
    for j in range(j1, j2):
        print('  + [%d] %s' % (b[j][0], b[j][1][:400]))
        nchg += 1
print('new/changed sentences in new file:', nchg)
