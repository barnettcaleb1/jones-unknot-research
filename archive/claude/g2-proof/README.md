# Lane G2-proof (third chat, started 2026-11-03 ~1:00 pm)

Question: is the Jones/Temperley-Lieb representation W(5,1) of B_5 (equivalently Jones's genus-two
representation restricted to B_5) faithful?
- If NOT: Ito (Math. Z. 2015) plus the normal-intersection lemma give a nontrivial knot with V = 1, so the
  Jones unknot conjecture is false.
- If YES: that is the first open rung of the conjecture, one step above Bharathram-Birman-Brendle (Burau_4, 2026).

This lane works the proof side (transfer of the BBB argument), a Heegaard/handlebody angle on 3-bridge knots,
and the kernel side as theory. The Astra bridge chat owns collab/; nothing here edits that board.

Files (written by the workflow agents):
- read-bbb/bbb.md, read-status/status.md, read-model/model.md
- build-transfer/transfer.md, build-heegaard/heegaard.md, build-kernel/kernel.md
- REPORT.md (summary for Caleb), LETTER-astra.md (draft for the bridge chat to send)

## zrho/ (second workflow, started ~1:12 pm)
Kasahara 2001 Problem 6.2: is Z_rho = rho(I_2)/rho([M_2,I_2]) infinite? If it is finite, rho is unfaithful on the
Torelli group and the conjecture is false. Kasahara's truncations give order >= 10; "exactly 10 remains possible".
Working reformulation to test: via Morita's Casson core d and Mullins's formula, Z_rho is finite iff some Torelli
kernel element gives a Jones-trivial 3-bridge knot with nonzero signature.
Files: zrho/read-kasahara/, zrho/read-casson/, zrho/build-identity/identity.md, zrho/build-infinite/infinite.md,
zrho/build-finite/finite.md, zrho/ZRHO.md, zrho/LETTER-paragraph.md
