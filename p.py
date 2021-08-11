import os
from shutil import copyfile 
path = '/projects/temporary/automates/er/gaurav/2018/1806/latex_images'
folders = os.listdir(path)
os.chdir(path)
count=0
for folder in folders:
  if count<50000:
    for tyf in os.listdir(folder):
      for File in os.listdir(f'{folder}/{tyf}');
        img_path = f'{folder}/{tyf}/{File}'
        dst = f'/projects/temporary/automates/er/gaurav/data_17M/images/{File}'
        copyfile(img_path, dst)
        count+=1
  else: break



