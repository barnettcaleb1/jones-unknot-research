#!/usr/bin/env python3
import sys, re, collections, glob, os
root = '/Users/calebbarnett/jones-lanes/theory-restart'
files = []
for dp, dn, fn in os.walk(root):
    if '/verify/shape-proof' in dp:
        continue
    for f in fn:
        if f.startswith('cxBNr-'):
            files.append(os.path.join(dp, f))
toks = collections.Counter()
heads = collections.Counter()
for f in files:
    for line in open(f, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('%'):
            continue
        m = re.match(r'^\s*(\d+)\)\s*(.*?)([⬮⬯].*)$', line)
        if not m:
            heads['UNPARSED: ' + line[:60]] += 1
            continue
        heads[re.sub(r'-?\d+', 'N', m.group(2))] += 1
        body = m.group(3)
        for t in re.split('[⬮⬯]', body):
            toks[t] += 1
print(len(files), 'files')
for t, c in toks.most_common():
    print(repr(t), c)
print()
for t, c in heads.most_common(20):
    print(repr(t), c)
