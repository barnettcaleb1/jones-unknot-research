> Public archival edition, prepared 17 November 2026. Historical AI-generated research/review record; not external specialist review. Private instructions and correspondence discussion have been removed with markers, and local paths anonymized. Mathematical claims and verdicts remain historical and may be superseded by the current ledger. No research or computation was rerun for this edition.

RECOVERED FROM SESSION TRANSCRIPTS (assembler addendum to MANIFEST.md, 17 Nov 2026)

Why this folder exists: H1 (MANIFEST.md section 11), H2 (A3, B7) and H3 (C1) list four scratchpad items as lost
(no longer on any disk). The assembler checked whether their text survives in the tool-call inputs recorded in
Claude's session transcripts. It does. Five files could be recovered EXACTLY and are in this folder. The rest can
only be rebuilt as a RECONSTRUCTION and are listed at the end, not extracted.

Method
- Read-only parse of Claude's session transcripts for the bridge session 7610ac96 (main transcript and subagent
  transcripts). Only the file body of a Write tool call, or the body of a shell heredoc with a quoted tag (no shell
  expansion), was taken. No other transcript text was copied.
- Exactness rule: a file is included only if it had exactly one creation event and no later modification event in
  any transcript of that session (Write, Edit, sed -i, in-place Python patch, redirection, cp or mv). The bytes here
  are exactly what the tool wrote at the stated time.
- Nothing was rerun. No new computation. Research remains paused.
- Code is unaltered. Two files (validate_section7.py, size_and_facts.py) contain absolute scratchpad paths that
  include the home-folder username: normalise at export, as for copied/.
- Times: local (UTC-6), with UTC in brackets. <scratch> = the Claude session scratchpad root under /private/tmp/claude-501/.

Recovered files (path in this folder | original path | created | by | bytes | SHA-256)

1. scratchpad-7610ac96/burau/phi0.py
   Original: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/burau/phi0.py
   Created: 3 Nov 2026 15:19 local [21:19:56 UTC], bridge session main transcript, shell heredoc.
   Bytes 1851. SHA-256 e097b9117ad189d50b524129b2e1022e534df95a996088929375c6d93331f398
   What it is: Claude's first exact check that the unreduced Burau matrix of
   Phi0 = [(s1 s2)^6, [[A14,A24],A34]] (word length 112) is the identity at t = -1 and not at t = 2, 3, in B_4 and
   B_5 (exact Fractions, standard library).
   Referenced in: collab/THEORY-width-ladder.md line ~484; collab/ledger/parts/P2_theorylog.md line 171
   ("location not given").
   Note: a different script from ~/jones-lanes/g2-proof/bbb-gap/phi0_check.py (1384 bytes), which stays the recheck
   of record (H2 B7). BBB mathematical material is included under the project lead's public-release authorization; the earlier precautionary hold is resolved.

2. scratchpad-7610ac96/scripts/bracket_check.py
   Original: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/scripts/bracket_check.py
   Created: 2 Nov 2026 23:33 local [3 Nov 05:33:40 UTC], LATE-41 audit workflow wf_cc7c4f23-e77, agent
   a8cbe4ead6f1a1b1a, shell heredoc.
   Bytes 1645. SHA-256 a0e86b4d9cbae9c2cdc0ff9d25de3143661cfd0398d651e88c764032da0113da
   What it is: Kauffman bracket check for X = <1/3> + <-1/3>, the counterexample to Sikora v2 Proposition 10(1)
   as printed: computes [N(X)] and compares with [N(<0>)], computes [D(X)] and the square-knot bracket
   [D(<1/3>)][D(<-1/3>)], and the determinant at A = e^{i pi/4}. Standard library.
   Referenced in: collab/audits/LATE-41-audit.md line 179; collab/lit/raw/late41-audit-results.json.
   Note: H3 C1 said to present the check as hand-verifiable because the script was lost. With this file the check is
   script-backed again (script recovered, not rerun in this pass).

3. scratchpad-7610ac96/bbb-attack/REPORT.md
   Original: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/bbb-attack/REPORT.md
   Created: 3 Nov 2026 17:43 local [23:43:38 UTC], Gamma-check subagent a0cc1a23f713fd60a of the bridge session, Write.
   Bytes 4518. SHA-256 e2e12e965e709ca9cb7b6764b596a043590493921e1be16ee4f08d8fd6bf3251
   What it is: the agent's own work record of the explicit Gamma check for BBB Prop 6.7 (verdict UNDECIDED, closed
   under the 17:39 redirect): conventions validated term by term against BBB Section 7; the words Gamma_1, Phi0 and
   Phi = Gamma_1^-1 y1^31 Phi0 y1^-31 Gamma_1; exact facts (Burau of Phi0 and Phi identity at t = -1, not at t = 2;
   coefficient sums Phi0 1.26e7, Phi 1.55e11; iota(alpha, (beta*_3)Phi0) = 976,672 with disk census and
   M_Phi0(-1) = 0; smallest Brunnian cap candidate found); the Figure 7.4 exponent remark; the obstacle
   (iota of order 1e10 to 1e11 for the proper-product form, above the 1e6 stop rule).
   Referenced in: collab/msgs/20261103-174515-claude.md; collab/THEORY-width-ladder.md line ~572.
   Note: BBB mathematical material is included under the public-release authorization. Internal AI work; not external review.

4. scratchpad-7610ac96/bbb-attack/scripts/validate_section7.py
   Original: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/bbb-attack/scripts/validate_section7.py
   Created: 3 Nov 2026 16:54 local [22:54:59 UTC], same subagent, Write.
   Bytes 4616. SHA-256 4d7bfc6d846c1648206f11a17f04fc49c5b4d00c0a58a68f7a5b52924a151554
   What it is: checks the agent's pipeline against BBB Section 7 (Figs 7.1 to 7.4; the docstring quotes the paper's
   three Moody polynomials). It imports braidarc.py and reads traces/*.json, which are NOT exactly recoverable (see
   below), so this file is a record, not a runnable script. Contains a scratchpad path with the username.

5. scratchpad-7610ac96/bbb-attack/scripts/size_and_facts.py
   Original: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/bbb-attack/scripts/size_and_facts.py
   Created: 3 Nov 2026 17:39 local [23:39:45 UTC], same subagent, shell heredoc.
   Bytes 7059. SHA-256 7d7fe5eec4be0214ef29feb3ca3793e0949a9d9207b9a0c356c2ffb9d8a54786
   What it is: the exact partial facts within the stop rule quoted in REPORT.md (Burau coefficient sums as a size
   proxy, t = -1 and t = 2 checks for Phi0, Phi, Gamma_1 and the y_i, ranking of small Brunnian cap candidates, disk
   census and M_Phi0 for (beta*_3)Phi0). Imports braidarc.py (not exactly recoverable). Contains a scratchpad path
   with the username.

Not recovered (text survives only as creation text plus later in-place patches: a RECONSTRUCTION)
- frob5/frob5_check.py (FROB5 sieve, letter 20261103-102245-claude.md): Write at 3 Nov 10:15 and 10:16 local,
  then three in-place Python string patches 10:17 to 10:20 local, main transcript. Rebuilding the final file needs
  a replay of those patches.
- bbb-attack/scripts/braidarc.py (Write 16:47 local, then an Edit and in-place patches 16:48 to 16:49),
  trace_fig.py (possible patch 16:53), construct_gamma.py (sed -i 17:07), main_phi.py (possible patch 17:07),
  small_candidate.py (heredoc 17:42, then sed -i 17:42).
- Outputs: bbb-attack traces/*.json, results/*.json and logs, the frob5 sieve output and the bracket_check output
  were written by running scripts, not through tool inputs. At most parts appear in tool results. Not recovered.
Any future extraction requiring replay of patches must be labelled RECONSTRUCTION, not exact recovery. No conclusion of the program depends on
them: the FROB5 pilots were later rejected by exact certification, and the Gamma check closed UNDECIDED.
