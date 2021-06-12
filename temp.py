pred = open('/home/gauravs/Automates/temp/Learn_git/pred.txt', 'r+').readlines()
tgt = open('/home/gauravs/Automates/temp/Learn_git/tgt-test.txt', 'r+').readlines()

for i, e in enumerate(pred):
    if '<math> <mstyle> </math>\n\n' in pred:
        pred = pred.remove(i) 
        tgt = tgt.remove(i)
    
