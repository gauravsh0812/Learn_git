import matplotlib.pyplot as plt
import os
os.chdir('/home/gauravs/Automates/temp/Learn_git')

f = open('4-gram-scores.txt', 'r').readlines()
temp = {}
i=0    
while i <100:
    c=0
    for l in f:
        l=l.replace('\n', '')
        #print(l)
        if i<float(l)<=i+5: c+=1
    temp[f'{i}_to_{i+5}'] = c
    i=i+5

print(temp)
plt.figure(figsize=(15,6))
plt.bar(range(len(temp)), list(temp.values()), align='center')
plt.xlabel('BLEU SCORE')
plt.ylabel('# OF EQNS')
plt.savefig('BLEU_distribution_1.png')
