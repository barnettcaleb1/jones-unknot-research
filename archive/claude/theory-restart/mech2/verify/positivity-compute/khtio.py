#!/usr/bin/env python3
"""Referee's own readers for kht++ output: BN~ chain files -> generators with (h,q,idempotent); Kh~ component lines;
quotient word from the '<name>-q.svg' level comments; and a runner for kht++ (time limit, stdin closed)."""
import re, os, subprocess, json, hashlib, time
KHT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
ANSI = re.compile(r'\x1b\[[0-9;]*[A-Za-z]')
HEAD = re.compile(r'^\s*(\d+)\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*)$')
B, C = '⬮', '⬯'

def parse_chain(body):
    """body: string of generators and arrows. Returns (list of symbols, list of arrows) where arrow k sits between
    generator k and generator k+1 (cyclically, if the chain ends with an arrow): (kind 'S'|'D', power or None, forward?)."""
    body = body.strip()
    gens = []; arrows = []
    cur = ''
    for ch in body:
        if ch in (B, C):
            if gens or cur:
                if not gens:
                    raise ValueError('chain starts with an arrow: %r' % body)
                arrows.append(cur)
            cur = ''
            gens.append(ch)
        else:
            cur += ch
    cyclic = False
    if cur.strip():
        arrows.append(cur); cyclic = True
    out = []
    for a in arrows:
        a = a.strip()
        fwd = '>' in a; bwd = '<' in a
        if fwd == bwd:
            raise ValueError('arrow direction unclear: %r' % a)
        kind = 'S' if '~' in a else ('D' if '—' in a else None)
        if kind is None:
            raise ValueError('arrow kind unclear: %r' % a)
        m = re.search(r'\^(\d+)', a)
        lab = re.search(r'[SD]', a)
        if lab and lab.group(0) != kind:
            raise ValueError('label/shape mismatch: %r' % a)
        power = int(m.group(1)) if m else None
        out.append((kind, power, fwd, bool(lab)))
    return gens, out, cyclic

def chain_generators(h0, q0, body):
    """bigradings of all generators of one chain. Arrow x -> y labelled S^k: h(y)=h(x)+1, q(y)=q(x)+k; D^k: q(y)=q(x)+2k.
    Unlabelled S between equal idempotents is S^2."""
    gens, arrows, cyclic = parse_chain(body)
    res = [(gens[0], h0, q0)]
    h, q = h0, q0
    n = len(gens)
    for k, (kind, power, fwd, lab) in enumerate(arrows):
        x = gens[k]; y = gens[(k + 1) % n]
        if kind == 'S':
            p = power if power is not None else (2 if x == y else 1)
            if (p % 2 == 0) != (x == y):
                raise ValueError('S power parity vs idempotents')
            dq = p
        else:
            p = power if power is not None else 1
            if x != y:
                raise ValueError('D between different idempotents')
            dq = 2 * p
        if fwd:
            h, q = h + 1, q + dq
        else:
            h, q = h - 1, q - dq
        if k + 1 < n:
            res.append((gens[k + 1], h, q))
        else:
            if (h, q) != (h0, q0):
                raise ValueError('cyclic chain does not close up: %r' % body)
    return res, cyclic

def read_bn(path):
    """returns list of chains: dict(gens=[(sym,h,q)], cyclic=bool)"""
    chains = []
    for line in open(path, encoding='utf-8').read().splitlines():
        line = ANSI.sub('', line)
        if line.startswith('%') or not line.strip():
            continue
        m = HEAD.match(line)
        if not m:
            raise ValueError('cannot parse line %r in %s' % (line, path))
        h0, q0 = int(m.group(2)), int(m.group(3))
        gens, cyclic = chain_generators(h0, q0, m.group(5))
        chains.append(dict(gens=gens, cyclic=cyclic))
    return chains

def b_generators(path):
    out = []
    for ch in read_bn(path):
        for (s, h, q) in ch['gens']:
            if s == B:
                out.append((h, q))
    return sorted(out)

KHLINE = re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*?)\s{3,}(r|s)(\d*)\(([^)]*)\)\s+q\^(-?[\d/]+)\s+δ[_|]\^(-?[\d/]+)\s*$')
def read_khr(path):
    comps = []
    for line in open(path, encoding='utf-8').read().splitlines():
        line = ANSI.sub('', line)
        if line.startswith('%') or not line.strip():
            continue
        m = KHLINE.match(line)
        if not m:
            raise ValueError('cannot parse Kh line %r' % line)
        def fr(s):
            if '/' in s:
                a, b = s.split('/'); return int(a) / int(b)
            return float(int(s))
        comps.append({'type': m.group(5), 'len': m.group(6), 'slope': m.group(7), 'q': fr(m.group(8)), 'delta': fr(m.group(9))})
    return comps

def svg_levels(path):
    """word recorded in the level comments of a kht++ svg picture (caps appear as 'l/r<i>')."""
    txt = open(path, encoding='utf-8').read()
    toks = re.findall(r'<!-- level (\d+) (\S+) -->', txt)
    out = []
    for lev, t in toks:
        if t.startswith('l/r'):
            out.append(('cap', int(t[3:])))
        else:
            out.append((t[0], int(t[1:])))
    return out

def run_kht(workdir, name, word, timeout=300, sub='examples/words', field='2'):
    """writes workdir/sub/name.kht and runs kht++ -c<field> -q -s under a time limit with stdin closed."""
    d = os.path.join(workdir, sub)
    os.makedirs(d, exist_ok=True)
    f = os.path.join(sub, name + '.kht')
    with open(os.path.join(workdir, f), 'w') as fo:
        fo.write('%% %s\n%s\n,1\n' % (word, word))
    t0 = time.time()
    rec = {'word': word, 'name': name}
    try:
        r = subprocess.run(['perl', '-e', 'alarm %d; exec @ARGV' % timeout, KHT, '-c' + field, '-q', '-s', f],
                           cwd=workdir, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           timeout=timeout + 30)
        rec['rc'] = r.returncode
        tail = ANSI.sub('', r.stdout.decode('utf-8', 'replace'))[-400:]
    except subprocess.TimeoutExpired:
        rec['rc'] = 'timeout'; tail = ''
    rec['time'] = round(time.time() - t0, 1)
    od = os.path.join(d, name)
    pb = os.path.join(od, 'cxBNr-c%s-qs' % field)
    pk = os.path.join(od, 'cxKhr-c%s-qs' % field)
    rec['bn_file'] = pb if os.path.exists(pb) else None
    rec['kh_file'] = pk if os.path.exists(pk) else None
    if rec['bn_file'] is None:
        rec['tail'] = tail
    return rec
