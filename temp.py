from shutil import copyfile
import os, glob, random, json

N=325000

root = 'projects/temporary/automates/er/gaurav'

data_dir = []

for _ in range(N):
  y = random.randint(14, 18)
  year = '20'+str(y)
  for _ in range(int(N/5)):
    m = random.randint(1, 12)
    month = '14'+str(m)
    month_path = os.path.join(root, f'{year}/{month}')
    etree_path = os.path.join(month_path, 'etree')
    folder = random.choice(os.listdir(etree_path))      # directory name
    for tyf in glob.glob(os.path.join(etree_path, f'{folder}/*')):
      TYF = os.basename(tyf)  # TYF
      for file_name in os.listdir(tyf):
        data_dir.append([year, month, folder, TYF, file_name])

json.dump(data_dir, open(os.path.join(root, 'data_dir'), 'w'))

for d in data_dir:
  year, month, folder, TYF, file_name = d
  image = f'/projects/temporary/automates/er/gaurav/{year}/{month}/{folder}/{TYF}/{file_name.split('.')[0]}.png'
  new_name = f'{folder}_{TYF}_{file_name.split('.')[0]}.png'
  copyfile(image, f'/projects/temporary/automates/er/gaurav/data_325K/images/{new_name}')
