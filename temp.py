import os, multiprocessing, glob
from multiprocessing import Pool
from shutils import copyfile


def main():

  temp=[]
  root = '/projects/temporary/automates/er/gaurav/'

  for y in range(14, 19):
    year = '20'+str(y)
    year_path = os.path.join(root, year)
    for m in range(1, 13):
    mm = f"{m:02d}"
    month = str(y)+mm
    month_path = os.path.join(year_path, month)
    etree = os.path.join(month_path, 'etree')
    for folder_path in glob.glob(os.path.join(etree, '*')):
      folder = os.path.basename(folder_path)
      for tyf in glob.glob(os.path.join(folder_path, '*')):
        tyf_basename = os.path.basename(tyf)
        TYF = 'Large_eqns' if tyf_basename == 'Large_MML' else 'Small_eqns'
        for file_name_path in glob.glob(os.path.join(tyf, '*')):
          file_name = os.path.basename(file_name_path)
          file_name = file_name.split('.')[0]

          temp.append([root, year, month, folder, TYF, file_name])

  with Pool(multiprocessing.cpu_count()-10) as pool:
    result = pool.map(main_parallel, temp)

def main_parallel(args_arr):

  root, year, month, folder, TYF, file_name = args_arr
  try:
    file_name_png = file_name+'.png'
    image_path = os.path.join(root, f'{year}/{month}/latex_images/{folder}/{TYF}/{file_name_png}')
    final_name = f'{month}_{folder.split('.')[1]}_{TYF.spllit('_')[0]}_{file_name}.png'
    dst = os.path.join(root, f'data_17M/images/{final_name}')
    copyfile(image_path, dst)
  except:
    try:
      file_name_png = file_name+'png0001-1.png'
      image_path = os.path.join(root, f'{year}/{month}/latex_images/{folder}/{TYF}/{file_name_png}')
      final_name = f'{month}_{folder.split('.')[1]}_{TYF.spllit('_')[0]}_{file_name}.png'
      dst = os.path.join(root, f'data_17M/images/{final_name}')
      copyfile(image_path, dst)
    except:
      pass

main()
print('Jobs Done!')
