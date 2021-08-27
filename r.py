f=open('/projects/temporary/automates/er/gaurav/data_17M/xfer/src-val.txt', 'r').readlines()
#ft = open('/projects/temporary/automates/er/gaurav/data_17M/xfer/tgt-train-new-MP.txt', 'r').readlines()
#print(len(f))
#print(len(ft))
'''
print('1803_07475_Small_eqn179.png' in f)

for idx, (i, j) in enumerate(zip(f, ft)):

    #if ft == '\n':
    print(idx)
    print(' ')
    print(i)
    print(' ')
    print(j)
    print('======'*5)

print(len(f))
print(len(ft))
'''
f_new=open('/projects/temporary/automates/er/gaurav/data_17M/xfer/src-val-short.txt', 'w')
#R = [137259, 227817, 2165445, 3503091, 3984775,4426019,4620168]
#R=[274274, 746868, 1009907]
R=[20364, 25351, 284632,  519031, 819003]
#c=0
for i, v in enumerate(f):
    '''
    if len(v.split('_')) !=4:
#        c+=1
        print(i)
        print(v)
        #R.append(i)
    '''
    if i not in R:
        f_new.write(v)
    
#print(c)
