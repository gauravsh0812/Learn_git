import os

def json2js(json_data, output_file, var_name='eqn_src'):

    with open(output_file, 'w') as fout:
        fout.write(f'{var_name} = [\n')
        for i, datum in enumerate(json_data):
            fout.write('  {\n')
            fout.write(f'    eqn_num: {repr(datum["eqn_num"])},\n')
            fout.write(f'    mml1: {repr(datum["mml1"])},\n')
            fout.write(f'    mml2: {repr(datum["mml2"])}\n')
            fout.write('  }')
            if i < len(json_data):
                fout.write(',')
            fout.write('\n')
        fout.write('];')



if __name__ == '__main__':

    dir = "1402.0091"

    # json_data --> array of the dictionaries in a format like {'src': ---latex eqn---, 'mml': MathML code}
    #json_data = []

    Bleu = '/projects/temporary/automates/er/gaurav/Bleu_dict.txt'
    gram = '/projects/temporary/automates/er/gaurav/gram_dict.txt'
    idx_eqn = '/projects/temporary/automates/er/gaurav/idx_eqn.txt'

    b=json.load(open(Bleu.'r'))
    idx = json.load(open(idx_eqn, 'r'))
    temp = []
    for i, v in enumerate(b['lt60']):
      pred, tgt = idx[v]
      temp_dict = {}
      temp_dict['eqn_num'] = int(eqn_num)
      temp_dict['mml1'] = tgt
      temp_dict['mml2'] = pred
      temp.append(temp_dict)

    if destination = '/projects/temporary/automates/er/gaurav/lt60.js'

    json2js(temp, destination)
    
