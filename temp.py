import os, random, subprocess
path = '/projects/temporary/automates/er/gaurav'
os.chdir(path)
pred = open('pred.txt', 'r').readlines()
tgt = open('tgt-test.txt', 'r').readlines()

bleu_dict = {}
gram_dict ={}
idx_eqn ={}
idx=[]
n=0
b60, b6080, b80 = 0,0,0

while n < 20:
  r = random.randint(0, len(pred))
  if r not in idx:
    idx.append(r)
    pred_temp = open('temp_pred.txt', 'w')
    tgt_temp = open('temp_tgt.txt', 'w')
    pred_temp.write(pred[r])
    tgt_temp.write(tgt[r])
    pred_temp.close()
    tgt_temp.close()

    metric = subprocess.check_output()
    Bleu = float(metric.split()[2].replace(',', ''))
    gram_bleu = float(metric.split()[3].split('/')[-1])
    if Bleu < 60:
      bleu_dict['lt60'].append(r)
      b60+=1
    elif 60<= Bleu <80:
      bleu_dict['gte60_lt80'].append(r)
      b6080+=1
    else:
      bleu_dict['gte80'].append(r)
      b80+=1


    if gram_bleu < 60:
      gram_dict['lt60'].append(r)
    elif 60<= gram_bleu <80:
      gram_dict['gte60_lt80'].append(r)
    else: gram_dict['gte80'].append(r)

    idx_eqn[r] = f'[{pred[r]}, {tgt[r]}]'

    n=min(b60, b6080, b80)

import json
json.dump(bleu_dict, open('Bleu_dict.txt', 'w'))
json.dump(gram_dict, open('gram_dict.txt', 'w'))
json.dump(idx_eqn, open('idx_eqn.txt', 'w'))
