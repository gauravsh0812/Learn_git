train= open('/projects/temporary/automates/er/gaurav/OpenNMT_im2markup/OpenNMT-older-version/1401_mml_data/tgt-train.txt', 'r').readlines()
test=open('/projects/temporary/automates/er/gaurav/OpenNMT_im2markup/OpenNMT-older-version/1401_mml_data/tgt-test.txt', 'r').readlines()
val=open('/projects/temporary/automates/er/gaurav/OpenNMT_im2markup/OpenNMT-older-version/1401_mml_data/tgt-val.txt',  'r').readlines()

train_new= open('/projects/temporary/automates/er/gaurav/OpenNMT_im2markup/OpenNMT-older-version/1401_mml_data/tgt-train-new.txt', 'w')
test_new=open('/projects/temporary/automates/er/gaurav/OpenNMT_im2markup/OpenNMT-older-version/1401_mml_data/tgt-test-new.txt', 'w')
val_new=open('/projects/temporary/automates/er/gaurav/OpenNMT_im2markup/OpenNMT-older-version/1401_mml_data/tgt-val-new.txt',  'w')

eliminate = ['mspace', 'mtable', 'mathvariant', 'class', 'mpadded',
            'symmetric', 'fence', 'rspace', 'lspace', 'mstyle',
            'stretchy','form', 'movablelimits', 'maxsize', 'minsize', 'linethickness']

keep = ['mo', 'mi', 'mfrac', 'mn', 'mfrac']

def count(eqn, e):
    c=0
    for word in eqn.split():
        if e in word:
            c+=1
    return c

for t in [train, test, val]:
    for eqn in t:
        for e in eliminate:
            if e in eqn:
                c=count(eqn, e)
                for _ in range(c):
                    idx = eqn.find(e)
                    # find the '<' just before the e
                    temp1 = eqn[:idx+1]
                    temp2 = eqn[idx+1:]
                    open_angle = [idx_open for idx_open, angle in enumerate(temp1) if angle == '<']
                    close_angle = [idx_close for idx_close, angle in enumerate(temp2) if angle == '>']
                    filtered = temp1[open_angle[-1]:]+temp2[:close_angle[0]+1]
                    for k in keep:
                        if k in filtered:
                              flag=True
                              keep_token = k
                    if flag == True:
                        eqn = temp1[:open_angle[-1]]+f' <{keep_token}> '+temp2[close_angle[0]+1:]
                    else:
                        eqn = temp1[:open_angle[-1]]+temp2[close_angle[0]+1:]
                    #print(eqn)

        if t == train: train_new.write(eqn)
        elif t == test: test_new.write(eqn)
        else: val_new.write(eqn)
        #print(eqn)
