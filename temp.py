import os, glob, multiprocessing
from shutils import copyfile
from multiprocessing import Pool, Lock

lock=Lock()

def xfer(args):
  folder, TYF, filename  = args
  try:
    img_path_1 = f'/projects/temporary/automates/er/gaurav/2018/1808/latex_images/{folder}/{TYF}/{filename}.png'
    dst = '/projects/temporary/automates/er/gaurav/data_17M/xfer/images'
    copyfile(img_path_1, dst)

  except:
    try:
      img_path_2 = f'/projects/temporary/automates/er/gaurav/2018/1808/latex_images/{folder}/{TYF}/{filename}.png0001-1.png'
      dst = '/projects/temporary/automates/er/gaurav/data_17M/xfer/images'
      copyfile(img_path_2, dst)

    except:
      pass


path_1808 = '/projects/temporary/automates/er/gaurav/2018/1808/etree/*'

c=0
temp = []
for folder_path in glob.glob(path_1808):
  if c<200000:
    folder = os.path.basename(folder_path)
    for tyf in glob.glob(os.path.join(folder_path, '*')):
      TYF = os.path.basename(tyf).split('_')[0]+'_eqns'
      for filepath in glob.glob(os.path.join(tyf, '*')):
        filename = os.path.basename(filepath).split('.')[0]
        c+=1
        temp.append([folder, TYF, filename])
  else: break

print('temp done!')
print(temp[-1])

with Pool(multiprocessing.cpu_count()-5) as pool:
  pool.map(xfer, temp)
