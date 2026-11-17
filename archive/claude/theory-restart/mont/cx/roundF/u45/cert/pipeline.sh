#!/bin/zsh
# u45 U4 pipeline: as each E3 rerun finishes (e3/out/<run>.json appears), extract its stored J = 1 words, certify them with the
# audited certifier copy (cert_words.py) and re-check EVERY certificate in a fresh process with both checkers
# (verify_sample.py at fraction 1.0).  NP = 3 while >= 10 reruns are still running, else 7.
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45
RUNS=(e3b_n40_s240 e3d_n40_s440 e3d_n30_s430 e3b_n30_s230 e3w3_n30_s330 e3b_n24_s224 e3w3_n24_s324 e3b_n20_s220 e3d_n20_s420 e3_n40_s140 e3b_n16_s216 e3w3_n18_s318 e3_n30_s130 e3b_n12_s212 e3w3_n14_s314 e3_n24_s124 e3_n20_s120 e3_n16_s116 e3_n12_s112)
k=100
while true; do
  all=1
  for r in $RUNS; do
    [[ -f cert/.done_$r ]] && continue
    all=0
    if [[ -f e3/out/$r.json ]]; then
      nrun=$(ps -Ao command | grep -E "e3_search.py|e3w3.py|e3d_alex.py" | grep -v grep | wc -l | tr -d ' ')
      if [[ $nrun -ge 10 ]]; then NP=3; else NP=7; fi
      echo "$(date +%H:%M:%S) start $r NP=$NP running=$nrun" >> logs/pipeline.log
      python3 e3/u4_words.py $r >> logs/pipeline.log 2>&1
      python3 code/cert_words.py cert/words_$r.json $NP cert/u4_$r > logs/cert_u4_$r.log 2>&1
      echo "$(date +%H:%M:%S) cert $r: $(tail -1 logs/cert_u4_$r.log)" >> logs/pipeline.log
      grep -E "COUNTEREXAMPLE|non-unknot|LEMMA_Q" logs/cert_u4_$r.log >> logs/pipeline_ALERTS.log
      k=$((k+1))
      python3 code/verify_sample.py 1.0 $k $NP cert/verify_u4_$r.json cert/u4_$r.jsonl.gz >> logs/pipeline.log 2>&1
      echo "$(date +%H:%M:%S) verified $r" >> logs/pipeline.log
      touch cert/.done_$r
    fi
  done
  [[ $all == 1 ]] && break
  sleep 15
done
echo "$(date +%H:%M:%S) PIPELINE DONE" >> logs/pipeline.log
