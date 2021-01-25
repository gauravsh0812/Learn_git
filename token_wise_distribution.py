# Parsing all the working tokens
import json
import os
import matplotlib.pyplot as plt

# counters
zero_token = 0
one2three_tokens = 0
four2five_tokens = 0
six2ten_tokens = 0
ten_or_more = 0

def main():

    for yr in [14, 15, 16, 17, 18]:
        year = '20' + str(yr)

        for m in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            month = str(yr)+m

            latex_eqn_path = f'/projects/temporary/automates/er/gaurav/{year}/{month}/latex_equations'
            etree_path = f'/projects/temporary/automates/er/gaurav/{year}/{month}/etree'

            for folder in os.listdir(etree_path):
                for tyf in ['Small_MML', 'Large_MML']:
                    tyf_path = os.path.join(etree_path, f'{folder}/{tyf}')

                    for text_file in os.listdir(tyf_path):
                        # open the same file in latex_equations
                        tyf_le = 'Small_eqns' if tyf == 'Small_MML' else 'Large_eqn'
                        file_name = text_file.split('.')[0]
                        original_eqn_path = os.path.join(latex_eqn_path, f'{folder}/{tyf_le}/{file_name}.txt')
                        eqn = open(original_eqn_path, 'r').readlines()[0]
                        count_token(eqn)

    # creating bins -- distribution
    bin_plot()

def count_token(eqn):

    # count total number of tokens
    tokens_index = [i for i, char in enumerate(eqn) if char == '\\']
    number_of_tokens = len(tokens_index)

    if number_of_tokens == 0:
        zero_token+=1
    elif 1 <= number_of_tokens <=3:
        one2three_tokens+=1
    elif 4<= number_of_tokens <=5:
        four2five_tokens+=1
    elif 6<= number_of_tokens <=10:
        six2ten_tokens+=1
    else: ten_or_more+=1

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


if __name__ == '__main__':
    main()
