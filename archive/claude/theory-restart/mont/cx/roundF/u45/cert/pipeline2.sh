#!/bin/zsh
# u45 U4 pipeline v2 (07:30): lock-aware (mkdir cert/.lock_<run> is atomic), so two instances can run side by side.
# usage: pipeline2.sh NP fwd|rev     For each finished rerun: extract stored J = 1 words (u4_words.py waits for a complete
# JSON), certify (cert_words.py, audited copy), re-check EVERY certificate in a fresh process with both checkers.
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45
NP=$1
RUNS=(e3b_n40_s240 e3d_n40_s440 e3d_n30_s430 e3b_n30_s230 e3w3_n30_s330 e3w3_n24_s324 e3d_n20_s420 e3_n40_s140 e3_n30_s130 e3_n24_s124 e3_n20_s120 e3_n16_s116 e3_n12_s112)
[[ $2 == rev ]] && RUNS=(${(Oa)RUNS})
k=$(( $2 == rev ? 300 : 200 ))
for r in $RUNS; do
  [[ -f cert/.done_$r ]] && continue
  mkdir cert/.lock_$r 2>/dev/null || continue
  echo "$(date +%H:%M:%S) [$2] start $r NP=$NP" >> logs/pipeline.log
  python3 e3/u4_words.py $r >> logs/pipeline.log 2>&1 || { echo "$(date +%H:%M:%S) [$2] EXTRACT FAILED $r" >> logs/pipeline.log; continue; }
  python3 code/cert_words.py cert/words_$r.json $NP cert/u4_$r > logs/cert_u4_$r.log 2>&1
  echo "$(date +%H:%M:%S) [$2] cert $r: $(tail -1 logs/cert_u4_$r.log)" >> logs/pipeline.log
  grep -E "COUNTEREXAMPLE|non-unknot|LEMMA_Q|ERROR" logs/cert_u4_$r.log >> logs/pipeline_ALERTS.log
  k=$((k+1))
  python3 code/verify_sample.py 1.0 $k $NP cert/verify_u4_$r.json cert/u4_$r.jsonl.gz >> logs/pipeline.log 2>&1
  echo "$(date +%H:%M:%S) [$2] verified $r" >> logs/pipeline.log
  touch cert/.done_$r
done
echo "$(date +%H:%M:%S) [$2] PIPELINE2 DONE" >> logs/pipeline.log
