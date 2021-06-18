# -*- coding: utf-8 -*-

import os

def json2js(json_data, output_file, var_name='eqn_src'):
    with open(output_file, 'w') as fout:
        fout.write(f'{var_name} = [\n')

        for i, datum in enumerate(json_data):
            #print(datum)

            fout.write('  {\n')
            fout.write(f'    eqn_num: {repr(datum["eqn_num"])},\n')
            fout.write(f'    src: {repr(datum["src"])},\n')
            fout.write(f'    mml: {repr(datum["mml"])}\n')
            fout.write('  }')
            if i < len(json_data):
                fout.write(',')
            fout.write('\n')
        fout.write('];')

if __name__ == '__main__':
    # json_data --> array of the dictionaries in a format like {'src': ---latex eqn---, 'mml': MathML code}
    os.chdir('/projects/temporary/automates/er/gaurav')
    i=60
    f = open(f'score-{i}-{i+5}.txt', 'r').readlines()
    n=1
    flag=False
    json_data=[]

    while n<25:
      for line in f:
        if not flag:
          if 'tgt' in line:
            src = line[5:]
            flag = True
        if flag:
          if 'pred' in line:
            mml = line[6:]
            flag=False

            temp={}
            temp['eqn_num'] = n
            temp['src'] = src
            temp['mml']=mml
            n+=1
            json_data.append(temp)

    json2js(json_data, f'JS/score-{i}-{i+5}.js')
