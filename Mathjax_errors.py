import os
import subprocess
import json
import matplotlib.pyplot as plt

from datetime import datetime


print('starting at:  ', datetime.now())

def main():

    root = '/projects/temporary/automates/er/gaurav/'

    for yr in [14, 15, 16, 17, 18]:
        year = '20' + str(yr)
        logs_path = os.path.join(root, f'{year}/Logs/{year}_MathJax_MML_Log.log')

        (dict_token, dict_error, token_counter, error_counter) = Mjx_errors_and_not_working_tokens(logs_path)

        # dumping token/error dictionaries
        json.dump(dict_token, open(os.path.join(root, f'{year}/Logs/not_working_tokens_dictionary.txt'), 'w'))
        json.dump(dict_error, open(os.path.join(root, f'{year}/Logs/Mathjax_errors_dictionary.txt'),'w'))

    # ranking tokens/errors based on the total number of equations affected
    (sorted_token_counter, sorted_error_counter) = Ranking(token_counter, error_counter)

    # dumping counter dictionaries
    json.dump(token_counter, open(os.path.join(root, f'{year}/Logs/tokens_counter_dictionary.txt'),'w'))
    json.dump(error_counter, open(os.path.join(root, f'{year}/Logs/errors_counter_dictionary.txt'), 'w'))

    # finding histogram distribution of token/error counter dictionaries
    # It helps to get an idea of the errors/tokens that are affecting most of the eqns
    Distribution(sorted_token_counter, sorted_error_counter)


# finding 'not working' latex eqns and respective tokens
# These tokens can be find in the lines having 'is either not supported by
# MathJax or incorrectly written'

def Mjx_errors_and_not_working_tokens(log_file):

    # defining dictionary to store 'not working' eqns along with respective
    # tokens -- {latex_eqns:token} or errors -- {latyex_eqns:error}
    dict_token = {}
    dict_error = {}
    # defining a dictionary to keep record of the frequency of a token or error
    # {token/error: total number of equations it has affected}
    token_counter = {}
    error_counter = {}

    data = open(log_file ,'r').readlines()


    for line in data:

        # eqn_path: will tell us the equation path
        # sentence: will be in the form -- '<token> is either not supported by
        # MathJax or incorrectly written' or  '<error> is an error produced by MathJax webserver'
        (eqn_path, sentence) = line.split(':')[1], line.split(':')[-1]

        # PART 1 -- COLLECT ALL THE 'NOT WORKING' TOKENS
        if 'is either not supported by MathJax or incorrectly written' in sentence:

            #print('Part 1 --  ', line.split(':'))

            eqn_path = eqn_path.replace('latex_images', 'latex_equations')
            latex_eqn = open((eqn_path+'.txt'), 'r').readlines()[0]
            token = sentence.replace(' is either not supported by MathJax or incorrectly written', '').replace(' ', '')

            # if {latex_eqn:token} pair not in dict_token
            if latex_eqn not in dict_token.keys():
                if token not in dict_token.values():
                    dict_token[latex_eqn] = token
            else:
                dict_token[latex_eqn] = token

            # to record the frequency of the token
            if token in token_counter.keys():
                token_counter[token] +=1
            else:
                token_counter[token] = 1

        # PART 2 -- COLLECT ALL THE 'ERRORS' PRODUCED BY MATHJAX SERVER
        if 'is an error produced by MathJax webserver' in sentence:

            #print('Part 2 --  ', line.split(':'))

            eqn_path = eqn_path.replace('latex_images', 'latex_equations')
            latex_eqn = open((eqn_path+'.txt'), 'r').readlines()[0]
            error = sentence.replace(' is an error produced by MathJax webserver', '').replace(' ', '')

            # if {latex_eqn:token} pair not in dict_token
            if latex_eqn not in dict_error.keys():
                if error not in dict_error.values():
                    dict_error[latex_eqn] = error
            else:
                dict_error[latex_eqn] = error

            # to record the frequency of the token
            if error in error_counter.keys():
                error_counter[error] +=1
            else:
                error_counter[error] = 1

    return(dict_token, dict_error, token_counter, error_counter)


def Ranking(token_counter, error_counter):

    # sorting the dictionaries based in values
    sorted_token_counter = dict(sorted(token_counter.items(), key=lambda item: item[1]))
    sorted_error_counter = dict(sorted(error_counter.items(), key=lambda item: item[1]))

    return(sorted_token_counter, sorted_error_counter)

def Distribution(sorted_token_counter, sorted_error_counter):

    plt.figure(figsize=(15,5))
    plt.bar(list(sorted_token_counter.keys()), sorted_token_counter.values(), color='g')
    plt.show()


if __name__ == "__main__":
    main()

    print('stopping at:  ', datetime.now())
