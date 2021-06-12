import os, subprocess
os.chdir('/home/gauravs/Automates/temp/Learn_git')

tgt = open('tgt-test.txt', 'r').readlines()
pred = open('pred.txt', 'r').readlines()
#temp_tgt = open('temp-tgt.txt', 'w')
#temp_pred = open('temp-pred.txt', 'w')
scores = open('4-gram-scores.txt', 'w')
overall = open('overall.txt', 'w')

for t, p in zip(tgt, pred):
    temp_tgt = open('temp-tgt.txt', 'w')
    temp_pred = open('temp-pred.txt', 'w')
    temp_tgt.write(t)
    temp_pred.write(p)
    temp_tgt.close()
    temp_pred.close()
    metric = subprocess.check_output('perl multi-bleu.perl %s < %s'%('temp-tgt.txt', 'temp-pred.txt'), shell=True)
    gram = str(metric).split()[3].split('/')[-1]
    scores.write(str(gram) + '\n')
    temp = {}
    temp['4-gram-score'] = gram
    temp['tgt'] = t
    temp['pred'] = p
    overall.write(str(temp) + '\n')
