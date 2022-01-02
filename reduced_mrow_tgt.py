import os, json
path = '/projects/temporary/automates/er/gaurav/data_17M/data_5M/xfer/'
os.chdir(path)
for FILE in ['tgt-train.txt', 'tgt-test.txt', 'tgt-val.txt']:
    f_reduced = open(f'{FILE.split(".")[0]}-reduced.txt', 'w')
    f_old=open(FILE, 'r').readlines()
    for eqn_ind,eqn in enumerate(f_old):
        if eqn_ind%1000000 == 0: print(f'{FILE}:{eqn_ind}')
        if '<mrow>' in eqn:
        #    print(eqn)
            f=''
            for F in eqn.split():
                f=f+F+' '
            idxs_open = []
            idxs_close = []
            for ind, i in enumerate(f.split()):
                if i == '<mrow>':
                    idxs_open.append(ind)
                if i == '</mrow>':
                    idxs_close.append(ind)
            for o,c in zip(idxs_open, idxs_close):
                if len(f.split()[o:c+1])==3:
                    to_replace = ''
                    replace_with = ''
                    for fs in f.split()[o:c+1]:
                        to_replace+=fs+' '
                    #print(to_replace)
                    #print(' ')
                    replace_with = f.split()[o:c+1][1]+' '
                    #print(replace_with)
                    #print(' ')
                    f=f.replace(to_replace, replace_with)
       #     print(' ')
       #     print(f)
       #     print('----------------'*5)
            f_reduced.write(f+'\n')
        else:
      #      print(eqn)
            f=''
            for F in eqn.split():
                f=f+F+' '
            f_reduced.write(f+'\n')
