# Parsing all the working tokens
import json
import os, subprocess
import matplotlib.pyplot as plt
import multiprocessing
import argparse
import string

from datetime import datetime
from multiprocessing import Pool, Lock


# counters
#zero_token = 0
#one2three_tokens = 0
#four2five_tokens = 0
#six2ten_tokens = 0
#ten_or_more = 0

alphabet_Set = list(string.ascii_lowercase)+list(string.ascii_uppercase)

def main():

    for yr in [15, 16, 17, 18]:
        year = '20' + str(yr)
        subprocess.call(['mkdir', f'/projects/temporary/automates/er/gaurav/{year}/eqn_token_distribution'])

        for m in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            month = str(yr)+m
            print(month)
            subprocess.call(['mkdir', f'/projects/temporary/automates/er/gaurav/{year}/eqn_token_distribution/{month}'])

            latex_eqn_path = f'/projects/temporary/automates/er/gaurav/{year}/{month}/latex_equations'
            etree_path = f'/projects/temporary/automates/er/gaurav/{year}/{month}/etree'

            temp_args = []

            for folder in os.listdir(etree_path):
                subprocess.call(['mkdir', f'/projects/temporary/automates/er/gaurav/{year}/eqn_token_distribution/{month}/{folder}'])
                for tyf in ['Small_MML', 'Large_MML']:
                    tyf_path = os.path.join(etree_path, f'{folder}/{tyf}')

                    for text_file in os.listdir(tyf_path):
                        temp_args.append([year, month, folder, tyf, text_file, latex_eqn_path])

            with Pool(multiprocessing.cpu_count()-10) as pool:
                result = pool.map(count_token, temp_args)

    # creating bins -- distribution
    #bin_plot()

def count_token(args_list):
    
    global aplhabet_Set

    # unpacking args_list
    (year, month, folder, tyf, text_file, latex_eqn_path) = args_list
    
    #print(folder)

    tyf_le = 'Small_eqns' if tyf == 'Small_MML' else 'Large_eqns'
    if not os.path.exists(f'/projects/temporary/automates/er/gaurav/{year}/eqn_token_distribution/{month}/{folder}/{tyf_le}'):
        subprocess.call(['mkdir', f'/projects/temporary/automates/er/gaurav/{year}/eqn_token_distribution/{month}/{folder}/{tyf_le}'])

    file_name = text_file.split('.')[0]
    original_eqn_path = os.path.join(latex_eqn_path, f'{folder}/{tyf_le}/{file_name}.txt')
    equation = open(original_eqn_path, 'r').readlines()[0]

    # count total number of tokens
    char_list=[char for char in equation]
    temp_token_list = []
    i, begin, end, alpha = 0,0,0, False

    while i <len(char_list):

        if char_list[i] in "\\":
            begin =i
            alpha=True

        if alpha==True:
            if i!=len(char_list)-1:
                if char_list[i+1] not in alphabet_Set:
                    alpha=False
                    end=i
                    token = equation[begin:end+1]
                    #print(token)
                    if token not in temp_token_list:
                        temp_token_list.append(token)
        i+=1

    number_of_tokens = len(temp_token_list)

    json.dump(number_of_tokens, open(f'/projects/temporary/automates/er/gaurav/{year}/eqn_token_distribution/{month}/{folder}/{tyf_le}/{file_name}.json', 'w'))

    '''
    if number_of_tokens == 0:
        zero_token+=1
    elif 1 <= number_of_tokens <=3:
        one2three_tokens+=1
    elif 4<= number_of_tokens <=5:
        four2five_tokens+=1
    elif 6<= number_of_tokens <=10:
        six2ten_tokens+=1
    else: ten_or_more+=1
    '''
'''
def bin_plot():

    temp = {}
    temp['0'] = zero_token
    temp['1-3'] = one2three_tokens
    temp['4-5'] = four2five_tokens
    temp['6-10'] = six2ten_tokens
    temp['10+'] = ten_or_more

    # plot histogram
    plt.figure(figsize=(15,5))
    plt.bar(temp.keys(), temp.values(), width, color='g')
    plt.savefig('/projects/temporary/automates/er/gaurav/token_equation_distribution.png')
'''

if __name__ == '__main__':
    main()
