"""run kht++ (time limit, stdin closed, in my own working folder) on a tangle word and return the b-generators (h,q) of BN~"""
import os, re, subprocess, collections
KHT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'khtwork')

def parse_chain(line):
    m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)', line)
    if not m: return None
    h, q, chain = int(m.group(1)), int(m.group(2)), m.group(4)
    toks = re.findall(r'[⬮⬯]|[^⬮⬯]+', chain)
    gens = [t for t in toks if t in '⬮⬯']; arrows = [t for t in toks if t not in '⬮⬯']
    out = [(gens[0], h, q)]
    def step(a, left, right):
        fwd = a.endswith('>'); assert fwd != a.startswith('<'), a
        mm = re.search(r'([SD])(?:\^(\d+))?', a)
        if mm: kind, p = mm.group(1), int(mm.group(2) or 1)
        else:
            kind = 'S' if '~' in a else 'D'; p = 2 if (kind == 'S' and left == right) else 1
        deg = p if kind == 'S' else 2 * p
        return (1, deg) if fwd else (-1, -deg)
    for i in range(len(gens) - 1):
        dh, dq = step(arrows[i], gens[i], gens[i + 1])
        out.append((gens[i + 1], out[-1][1] + dh, out[-1][2] + dq))
    if len(arrows) == len(gens):   # cyclic: check closing
        dh, dq = step(arrows[-1], gens[-1], gens[0])
        assert (out[-1][1] + dh, out[-1][2] + dq) == (h, q), 'cyclic chain does not close'
    return out

def run(name, word, top=',0', opts=('-c2',), timeout=300):
    d = os.path.join(WORK, 'examples', 'mine'); os.makedirs(d, exist_ok=True)
    fn = os.path.join(d, name + '.kht')
    with open(fn, 'w') as f: f.write('%% %s\n%s\n%s\n' % (name, word, top))
    cmd = ['perl', '-e', 'alarm %d; exec @ARGV' % timeout, KHT] + list(opts) + ['examples/mine/%s.kht' % name]
    with open(os.path.join(WORK, 'run_%s.log' % name), 'w') as log:
        r = subprocess.run(cmd, cwd=WORK, stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT)
    if r.returncode != 0: return None
    suffix = ''.join(o for o in opts)
    cand = [x for x in os.listdir(os.path.join(d, name)) if x.startswith('cxBNr')]
    if not cand: return None
    gens = []
    for line in open(os.path.join(d, name, cand[0]), encoding='utf-8'):
        c = parse_chain(line)
        if c: gens += c
    return gens

def bgens(gens):
    return collections.Counter((h, q) for s, h, q in gens if s == '⬮')
