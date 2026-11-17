#!/bin/zsh
# finish e3_n24_s124: its certification was started by the first pipeline (orphaned when that shell was replaced at 07:29);
# wait for that cert_words process (PID 13437) to exit, then two-checker verification, then mark done.
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45
while kill -0 13437 2>/dev/null; do sleep 3; done
echo "$(date +%H:%M:%S) [n24] cert e3_n24_s124: $(tail -1 logs/cert_u4_e3_n24_s124.log)" >> logs/pipeline.log
grep -E "COUNTEREXAMPLE|non-unknot|LEMMA_Q|ERROR" logs/cert_u4_e3_n24_s124.log >> logs/pipeline_ALERTS.log
python3 code/verify_sample.py 1.0 124 4 cert/verify_u4_e3_n24_s124.json cert/u4_e3_n24_s124.jsonl.gz >> logs/pipeline.log 2>&1
echo "$(date +%H:%M:%S) [n24] verified e3_n24_s124" >> logs/pipeline.log
touch cert/.done_e3_n24_s124
