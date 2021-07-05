import os
os.chdir('/projects/temporary/automates/er/gaurav/data_325K')
train = open('tgt-train.txt', 'r').readlines()
test = open('tgt-test.txt', 'r').readlines()
val = open('tgt-val.txt', 'r').readlines()
data = train+test+val

F = open('vocab_325K.txt', 'w')
tokens=[]

for eqn in data:
    open_angle = [idx_open for idx_open, angle in enumerate(eqn) if angle == '<']
    close_angle = [idx_close for idx_close, angle in enumerate(eqn) if angle == '>']
    for i in range(len(open_angle)):
        token1 = eqn[open_angle[i]:close_angle[i]+1]
        if token1 not in tokens:
           tokens.append(token1)
           F.write(f'{token1}\n')
           if i<len(open_angle)-1:
               token2 = eqn[close_angle[i]+1:open_angle[i+1]]
               token2=token2.strip()
               if token2 not in tokens:
                   tokens.append(token2)
                   F.write(f'{token2}\n')
