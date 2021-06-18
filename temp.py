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
    #os.chdir('/projects/temporary/automates/er/gaurav')
    f = open('/content/score-90-95.txt', 'r').readlines()
    tgt = []
    pred =[]
    for line in f:
      if line!=' ':
        if line!='{' and line!='}' and line!='}{':
          if 'tgt' in line:
            tgt.append(line[5:])
          if 'pred' in line:
            pred.append(line[6:])

    json_data = []
    for idx, (t, p) in enumerate(zip(tgt, pred)):
      temp = {}
      temp['eqn_num'] = idx
      temp['src']=t
      temp['mml']=p
      json_data.append(temp)
