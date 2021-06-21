import os, subprocess

os.chdir('/projects/temporary/automates/er/gaurav')
pred = open('pred.txt', 'r').readlines()
tgt = open('tgt-test.txt', 'r').readlines()

pred_gram = {}
tgt_gram = {}

for t,p in zip(tgt, pred):
  temp_pred = open('temp_pred', 'w')
  temp_tgt = open('temp_tgt', 'w')
  temp_pred.write(p)
  temp_tgt.write(t)
  temp_pred.close()
  temp_tgt.close()

  metric = subprocess.check_output('perl multi-bleu.perl %s < %s'%('temp_tgt.txt', 'temp_pred.txt'), shell=True)

  gram = float(metric.split()[4].split('/')[-1])
  tgt_gram[len(t.split())] = gram
  pred_gram[len(p.split())]=gram

import json
json.dump(pred_gram, open('pred_gram.txt', 'w'))
json.dump(tgt_gram, open('tgt_gram.txt', 'w'))
