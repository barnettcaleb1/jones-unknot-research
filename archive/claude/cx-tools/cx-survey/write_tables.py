#!/usr/bin/env python3
"""write_tables.py -- render certificates.md and summary.md from results.json,
checks.json and rational_slots.json."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
R = json.loads((HERE / 'results.json').read_text())
CH = json.loads((HERE / 'checks.json').read_text())
RS = json.loads((HERE / 'rational_slots.json').read_text())

FUSION_OF = {'1L': 'unfused', '1S': 'unfused',
             '2L': 'seam_sigma2 (H2; configs 2L,2S)', '2S': 'seam_sigma2 (H2; configs 2L,2S)',
             '3': 'seam_band (c1 anchor; configs 3,3b,4L,4S,6)', '3b': 'seam_band (c1 anchor; configs 3,3b,4L,4S,6)',
             '4L': 'seam_band (c1 anchor; configs 3,3b,4L,4S,6)', '4S': 'seam_band (c1 anchor; configs 3,3b,4L,4S,6)',
             '6': 'seam_band (c1 anchor; configs 3,3b,4L,4S,6)',
             '5a': 'top_sigma2 (configs 5a,5aL)', '5aL': 'top_sigma2 (configs 5a,5aL)',
             '5b': 'bottom_sigma2 (configs 5b,5bL)', '5bL': 'bottom_sigma2 (configs 5b,5bL)',
             '5c': 'seam_sigma2inv (config 5c)'}

yn = lambda b: 'HOLDS' if b else 'fails'

# ------------------------------------------------------------ certificates.md
out = ['# Certificates: four-corner survey of EKT-type fusions', '',
       'Conventions: ' + R['conventions'], '',
       'Site states: I = IdentityBraid(2), e = ZeroTangle (cup over cap), m = m full twists (BraidTangle([+-1]*2|m|,2)); '
       'at a rotated (seam) site the same local states are rotated by 90 degrees. '
       'B_ab: a = state of site 1, b = state of site 2 (sites listed in the title order). '
       'All four corners come from ONE diagram with only the two boxes replaced (same outside framing), absolute bracket, no per-corner normalisation. '
       'PD codes are spherogram PD_code() of K(0,0) (0-based labels); site edges are the PD edge labels of the two strands inside each box.', '',
       'Realisations of the T / U site: "lit" = vertical 2-string box on the cable strands immediately next to the rotated IntegerTangle(+-3) '
       '(full twists inside the rotated T / U); "seed" = the box at the top of the EKT seed S inside T = omega(S) (resp. U = omega_bar(S)), '
       'omega(T) = ((T + 2) * 1) + 2 as in c1_nonunit_turnback.py; omega(I2) is isotopic rel boundary to IntegerTangle(3), omega_bar(I2) to IntegerTangle(-3).', '']

for key, c in R['configs'].items():
    an = c['analysis']; k = c['K00']; xc = c['crosscheck']
    out.append(f'## [{key}] {c["title"]}')
    if c.get('note'):
        out.append(f'_{c["note"]}_')
    out.append('')
    out.append(f'* Sites: site 1 = **{c["sites"][0]}**, site 2 = **{c["sites"][1]}**.')
    out.append(f'* Diagram: `{c["tangle_word"]}` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).')
    out.append(f'* K(0,0): {k["crossings"]} crossings, {k["components"]} component(s), writhe w0 = {k["writhe"]}.')
    out.append(f'* PD(K(0,0)) = `{json.dumps(k["pd"])}`')
    out.append(f'* Site edges in that PD: site 1 ({c["sites"][0]}) = {k["site_edges"][c["sites"][0]]}, site 2 ({c["sites"][1]}) = {k["site_edges"][c["sites"][1]]}.')
    out.append('')
    out.append('**(1) Four raw corner brackets (absolute, same framing):**')
    out.append('')
    out.append('| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |')
    out.append('|---|---|---|---|---|---|')
    for tag, st in (('00', '(I, I)'), ('10', '(e, I)'), ('01', '(I, e)'), ('11', '(e, e)')):
        ci = c['corners'][tag]
        out.append(f'| B{tag} | {st} | {ci["crossings"]} | {ci["components"]} | {ci["writhe"]} | `{ci["bracket_str"]}` |')
    out.append('')
    out.append('**(2) Identity polynomials (exact):**')
    out.append('')
    out.append(f'* u = (-A^3)^w0 = `{an["unit_u"]}`;  B00 - u*delta = `{an["poly_B00_minus_u_delta"]}`  -> unknot-seed equation **{yn(an["unknot_seed_eq"])}**')
    out.append(f'* delta*B10 - B11 = `{an["poly_dB10_minus_B11"]}`  -> **{yn(an["id_dB10_eq_B11"])}**  (c = 0)')
    out.append(f'* delta*B01 - B11 = `{an["poly_dB01_minus_B11"]}`  -> **{yn(an["id_dB01_eq_B11"])}**  (b = 0)')
    out.append(f'* (single-site flatness at K(0,0): delta*B00 = B10 {yn(an["flat_site1_at_I"])}; delta*B00 = B01 {yn(an["flat_site2_at_I"])})')
    out.append('')
    out.append('**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):')
    out.append('')
    if xc.get('handedness'):
        out.append(f'* handedness s = {tuple(xc["handedness"])}, writhe w(m,n) = w0 + 2*({xc["writhe_slopes"][0]}) m + 2*({xc["writhe_slopes"][1]}) n; sites {xc["site_orientation"]}; direct-bracket cross-check at {xc["grid"]}: **{xc["status"]}**')
    for cc in 'abcd':
        co = an['coeffs'][cc]
        out.append(f'* delta^3 * {cc} = `{co["delta3_times"]}`   [{co["exact"]}]')
    out.append('')
    out.append('**K(0,0):** V = `' + k['V_str'] + '`' + (f', det = {k["det"]}' if 'det' in k else '') +
               (f'; HFK total rank {k["check"].get("hfk_total_rank")}, genus {k["check"].get("hfk_genus")}; spherogram simplify -> {k["check"].get("simplified_crossings")} crossings; snappy identify {k["check"].get("identify")}; volume {k["check"].get("volume")}' if 'check' in k else ' (link)'))
    if xc.get('points'):
        out.append('')
        out.append('Grid points (direct computation): ' + '; '.join(
            f'K({p}): V = {v["V_str"]}' + (f', det {v["det"]}' if v.get('det') is not None else '') for p, v in xc['points'].items()))
    fus = FUSION_OF.get(key)
    if fus:
        rs = RS[fus]
        out.append('')
        out.append(f'**Rational-slot corners C** (fusion `{fus}`, see rational_slots.md): (E1) {yn(rs["E1_holds"])}, defect `{rs["E1_defect"]}`; (E2) {yn(rs["E2_holds"])}, defect `{rs["E2_defect"]}`.')
    if 'certificate_extras' in c:
        out.append('')
        out.append('**Both identities hold -> extras:** ' + json.dumps(c['certificate_extras']))
    out.append('')

out.append('## Supplementary checks (checks.json)')
out.append('')
out.append(f'* c1_nonunit_turnback.py reproduction: K(0,0) PD identical = {CH["c1_K00_pd_identical"]} ({CH["c1_K00_crossings"][0]} crossings); all four corner PDs/brackets identical = '
           + str(all(v["identical"] and v["pd_identical"] for v in CH["c1_corners"].values())) + '.')
out.append(f'* V_J = V(N(R(25,-9))) = `{CH["V_J"]}`, det {CH["det_J"]}; config 3 has B10 = {CH["B10_eq_unit_delta2_VJ"]} * delta^2 * V_J(t = A^-4) (c1 note eq. (6)).')
out.append('* Config 4S/3b Jones-unit line K(0,n) (U-seed site twisted, seam fused): ' + '; '.join(
    f'n={n}: V = {v["V_str"]}, HFK rank {v["check"].get("hfk_total_rank")}, simplify -> {v["check"].get("simplified_crossings")} crossings' for n, v in CH['config4S_K0n_line'].items()) + '.')
out.append(f'* K(0,0) with the crossing circle c_U of the U-seed site: {CH["config4S_U_ring"]["components"]} components, V = `{CH["config4S_U_ring"]["V_str"]}`, lk = {CH["config4S_U_ring"]["linking"]}, spherogram simplify -> {CH["config4S_U_ring"]["simplified_crossings"]} crossings with {CH["config4S_U_ring"]["simplified_free"]} free unknots (split 2-component unlink: c_U bounds a disk missing K, the site is nugatory).')
out.append(f'* Anchor with the crossing circle of the T-seed site: {CH["config3_T_ring"]["geometry"]}; with the seam site\'s crossing circle: {CH["config3_seam_ring"]["geometry"]} (both hyperbolic: neither circle is nugatory).')
out.append('* Config 4L, seam twisted with the U-lit site turned back: ' + '; '.join(
    f'm={m}: V = {v["V_str"]}, HFK rank {v["check"].get("hfk_total_rank")}' for m, v in CH['config4L_seam_twist_with_Ue'].items()) + ' (all have the V and HFK of the trefoil: consistent with the seam twists being removable by isotopy once the U cable is turned back; evidence, not a proof).')
(HERE / 'certificates.md').write_text('\n'.join(out) + '\n')

# ------------------------------------------------------------ summary.md
s = ['# Summary table', '',
     'B-corner identities per configuration (absolute bracket; "site 1 / site 2" as in the title). '
     'c=0 means delta*B10 = B11 (site 2 flat when site 1 = e); b=0 means delta*B01 = B11 (site 1 flat when site 2 = e). '
     'Also shown: single-site flatness at K(0,0) (delta*B00 = B10: site 1 flat when site 2 = I; delta*B00 = B01: site 2 flat when site 1 = I).', '',
     '| cfg | fusion | site 1 | site 2 | K(0,0) | B00 = u delta | c = 0 | b = 0 | dB00=B10 | dB00=B01 | sites | xcheck |',
     '|---|---|---|---|---|---|---|---|---|---|---|---|']
for key, c in R['configs'].items():
    an = c['analysis']; k = c['K00']; xc = c['crosscheck']
    if k['components'] == 1:
        ch = k.get('check', {})
        idn = ch.get('identify') or []
        kname = (idn[1] if len(idn) > 1 else (idn[0] if idn else ('unknot' if ch.get('hfk_total_rank') == 1 else f'HFK rank {ch.get("hfk_total_rank")}')))
        k00 = f'knot {k["crossings"]} cr, {kname}, det {k.get("det")}'
    else:
        k00 = f'{k["components"]}-comp link, {k["crossings"]} cr'
    fus = FUSION_OF.get(key, '').split(' ')[0]
    s.append(f'| {key} | {fus} | {c["sites"][0]}{"" if key in ("3","3b","4L","4S","6","1L","1S","2L","2S","5a","5b","5c","5aL","5bL") else ""} | {c["sites"][1]} | {k00} | {yn(an["unknot_seed_eq"])} | {yn(an["id_dB10_eq_B11"])} | {yn(an["id_dB01_eq_B11"])} | {yn(an["flat_site1_at_I"])} | {yn(an["flat_site2_at_I"])} | {"/".join(o[:4] for o in xc.get("site_orientation", []))} | {"ok" if xc.get("all_match") else "FAIL"} |')
s += ['', 'Site realisation: L = literal box next to IntegerTangle(+-3) (not EKT-flat even on the link); S = seed box inside omega / omega_bar (EKT-flat on the link). '
      'Configs 3, 3b, 4L, 4S, 6 use the c1 seam-band fusion (ZeroTangle at the seam); 2, 5a, 5b use a sigma2 crossing; 5c sigma2^-1.', '',
      '## Link calibration (config 1, one site at a time on the unfused link)', '',
      '| site | delta*B_I - B_e | flat | V(1)/V(2)/V(-1) vs V(0) |', '|---|---|---|---|']
for name, v in R['config1_link_single_site'].items():
    s.append(f'| {name} | `{v["poly_delta_BI_minus_Be"]}` | {yn(v["bracket_identity_delta_BI_eq_Be"])} | {v["V_vs_I"]["1"]} / {v["V_vs_I"]["2"]} / {v["V_vs_I"]["-1"]} |')
s += ['', '## Rational-slot tensors (holder\'s C corners; reduced brackets, same framing)', '',
      '| fusion | C_00 (comps) | C_0inf (comps) | C_inf0 (comps) | C_infinf (comps) | E1 | E2 defect |', '|---|---|---|---|---|---|---|']
for fus, rs in RS.items():
    cc = rs['corners']
    s.append(f'| {fus} | `{cc["00"]["reduced"]}` ({cc["00"]["components"]}) | `{cc["0inf"]["reduced"]}` ({cc["0inf"]["components"]}) | `{cc["inf0"]["reduced"]}` ({cc["inf0"]["components"]}) | `{cc["infinf"]["reduced"]}` ({cc["infinf"]["components"]}) | {yn(rs["E1_holds"])} | `{rs["E2_defect"]}` |')
s.append('')
s.append('Unfused shell: C/delta equals the target [[d^6-7d^4+15d^2-8, d],[d, 1]] exactly (components 4,3,3,2 = pattern (3,2,2,1) plus one).')
(HERE / 'summary.md').write_text('\n'.join(s) + '\n')
print('wrote certificates.md and summary.md')
