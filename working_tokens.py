# Parsing all the working tokens
import json
import os

root = '/projects/temporary/automates/er/gaurav'
token_set = []

def main():

    global root, token_set

    '''
    for yr in [14, 15, 16, 17, 18]:
        year = '20' + str(yr)

        for m in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            month = str(yr)+m
            MML_path = os.path.join(root, f'{year}/{month}/Mathjax_mml')
    '''
    year = '2014'
    month = '1401'
    for folder in os.listdir(MML_path):
        Macros_path = os.path.join(root, f'{year}/{month}/latex_equations/{folder}/Macros_paper.txt')
        DMO_path = os.path.join(root, f'{year}/{month}/latex_equations/{folder}/DeclareMathOperator_paper.txt')
        Macros = open(Macros_path, 'r').readlines()
        DMOs = open(DMOs_path, 'r').readlines()

        for tyf in ['Small_MML', 'Large_MML']:
            tyf_path = os.path.join(MML_path, f'{folder}/{tyf}')

            for eqn in os.listdir(tyf_path):
                parsing_token(year, month, folder, Macros, DMOs, tyf, eqn)

    json.dump(token_set, open(os.path.join(root, f'{year}/Logs/combine_logs/working_tokens_set.json')))

def parsing_token(year, month, folder, Macros, DMOs, tyf, eqn):

    global root, token_set


    eqn_path = os.path.join(root, f'{year}/{month}/latex_equations/{folder}/{tyf}/{eqn}')
    equation = open(eqn_path, 'r').readlines()[0]
    backslash_index = [i for i,c in enumerate(eqn) if c == '\\']

    for index in backslash_index:
        temp = equation[i:]
        token = temp[:temp.find(' ')+1]
        print('the token is:  ', token)
        token_set.append(token)


if __name__ == '__main__':
    main()
