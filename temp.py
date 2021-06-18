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
    while i<100:
        f = open(f'score-{i}-{i+5}.txt', 'r').readlines()
        json_data = []
        #temp_dict={}
        #for idx, v in enumerate(f):
        num = 1
        vindex=0
        while num<25:
            temp_dict={}
            v=f[vindex]
            if v != '{' and v!= '}':
                if 'tgt' in v:
                    temp_dict['eqn_num'] = num
                    temp_dict['src'] = v[5:]
                    flag = True
                    while flag:
                      t=1
                      v = f[vindex+t]
                      if 'pred' in v:
                          temp_dict['mml']=v[6:]
                          flag = False
                      else: t+=1

            vindex=vindex+t
            json_data.append(temp_dict)
        #print(json_data[0:5])

        new_json = []
        for j in json_data:
            if j != {}:
                if 'eqn_num' in j:



        i+=5
        json2js(json_data, f'JS/score-{i}-{i+5}.js')
