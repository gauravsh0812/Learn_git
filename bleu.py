import os, logging, subprocess, random, json

path = '/projects/temporary/automates/er/gaurav/replicate_im2markup/im2markup_100K/im2markup'
gold = os.path.join(path, '.tmp.gold.txt')
pred = os.path.join(path,'.tmp.pred.txt')
Fp_temp = os.path.join(path, 'p.txt')
Fg_temp = os.path.join(path, 'g.txt')

Fp = open(pred, 'r').readlines()
Fg = open(gold, 'r').readlines()
#ptemp = open(Fp_temp, 'w')
#gtemp = open(Fg_temp, 'w')

scores = []
err=0
for i in range(len(Fp)):
    try:
        if len(Fp[i].split()) !=0:
            ptemp = open(Fp_temp, 'w')
            gtemp = open(Fg_temp, 'w')
    
            predicted = Fp[i]
            tgt = Fg[i]
            ptemp.write(predicted)
            gtemp.write(tgt)
            ptemp.close()
            gtemp.close()
            
    
            score = subprocess.check_output('perl multi-bleu.perl %s < %s'%(Fg_temp, Fp_temp), shell=True)
            #print(score.split()[2])
            scores.append(score.split()[2])
            #print('========='*5)
    except: err+=1

print('total not working equations: ', err)
outfile=open(os.path.join(path, 'scores.json'), 'w')
json.dump(scores, outfile)

