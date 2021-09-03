# -*- coding: utf-8 -*-

import os
os.chdir('/projects/temporary/automates/er/gaurav/data_17M/xfer')

train= open('tgt-train-new-reduced.txt', 'r').readlines()
test=open('tgt-test-new-reduced.txt', 'r').readlines()
val=open('tgt-val-new-reduced.txt',  'r').readlines()
data = train+test+val

F = open('vocab_10M.txt',  'w')
tokens=[]
problem_idx=[]

def token_extraction(open_angle, close_angle):

    global F, tokens, problem_idx

    for i in range(len(open_angle)):
        try:
            token1 = eqn[open_angle[i]:close_angle[i]+1]
            if token1 not in tokens:
               tokens.append(token1)
               F.write(f'{idx} --> {token1}\n')
               if i<len(open_angle)-1:
                   token2 = eqn[close_angle[i]+1:open_angle[i+1]]
                   token2=token2.strip()
                   if token2 not in tokens:
                       tokens.append(token2)
                       F.write(f'{idx} --> {token2}\n')
        except:
            problem_idx.append(str(idx))
            pass

def rectifying(eqn):
    alpha = 0
    prob_idx=[]

    for idx, e in enumerate(eqn):
        if e == '<':
            alpha += 1
        if e == '>':
            alpha -= 1
        if alpha>1:
           prob_idx.append(idx)
           alpha=1

    new_eqn = ''
    initial=0
    n=0
    while n < len(prob_idx):
      temp_eqn = eqn[initial:prob_idx[n]]
      print(temp_eqn)
      last_open = [ind for ind, char in enumerate(temp_eqn) if char == '<'][-1]
      new_eqn+=temp_eqn[:last_open]
      initial=prob_idx[n]
      n+=1

    new_eqn+=eqn[prob_idx[n-1]:]

    new_open_angle = [idx_open for idx_open, angle in enumerate(new_eqn) if angle == '<']
    new_close_angle = [idx_close for idx_close, angle in enumerate(new_eqn) if angle == '>']

    token_extraction(new_open_angle, new_close_angle)

def final_vocab():
    F1=open('/projects/temporary/automates/er/gaurav/data_17M/xfer/vocab_10M.txt', 'r').readlines()
    F2 = open('/projects/temporary/automates/er/gaurav/data_17M/xfer/final_vocab.txt', 'w')
    for f in F1:
        idx, token =f.split(' --> ')
        if idx not in problem_idx:
            F2.write(token)

    # writing integres
    for intg in range(0, 10):
        F2.write(str(intg))
    # writing '.'
    F2.write('.')


if __name__ = '__main__':

    for idx, eqn in enumerate(data):
        open_angle = [idx_open for idx_open, angle in enumerate(eqn) if angle == '<']
        close_angle = [idx_close for idx_close, angle in enumerate(eqn) if angle == '>']

        if len(open_angle) == len(close_angle):
            token_extraction(open_angle, close_angle)
        elif: len(open_angle)>len(close_angle):
            rectifying(eqn)

    final_vocab()
