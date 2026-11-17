"""Exact V_K of the covering knot of a halfword (tools/kauffman.bracket, normalised exactly as mont/ft/ident3.VK), and
the crossing count of its symmetric diagram (alex.symmetrize + alex.diagram)."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import kauffman, alex
def VK(word):
    kb = kauffman.bracket(word)
    if not kb: return None
    kb = {e: c for e, c in kb.items() if c}
    es = sorted(kb); r = es[0] % 4
    if any((e - r) % 4 for e in es): return None
    V = {-(e - r) // 4: c for e, c in kb.items()}
    s = sum(V.values())
    if s not in (1, -1): return None
    V = {e: c * s for e, c in V.items()}
    d = sum(e * c for e, c in V.items())
    return {e - d: c for e, c in V.items()}
def ncross(word):
    full = alex.symmetrize(alex.parse(word))
    if full is None: return None
    cr = alex.diagram(full)
    return None if cr is None else len(cr)
