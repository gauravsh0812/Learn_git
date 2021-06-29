import os, random

N = 320834
images = os.listdir('/projects/temporary/automates/er/gaurav/data_325K/images/')
src_train = open('/projects/temporary/automates/er/gaurav/data_325K/src-train.txt', 'w')
src_test = open('/projects/temporary/automates/er/gaurav/data_325K/src-test.txt', 'w')
src_val = open('/projects/temporary/automates/er/gaurav/data_325K/src-val.txt', 'w')
tgt_train = open('/projects/temporary/automates/er/gaurav/data_325K/tgt-train.txt', 'w')
tgt_test = open('/projects/temporary/automates/er/gaurav/data_325K/tgt-test.txt', 'w')
tgt_val = open('/projects/temporary/automates/er/gaurav/data_325K/tgt-val.txt', 'w')

train, test, val = [], [], []
for i in range(int(N*0.8)):
  image = random.choice(images)
  train.append(image)
  src_train.write(image + '\n')
  #{folder}_{TYF}_{file_name.split(".")[0]}.png
  folder, tyf, file_name = image.split('_')
  month, folder_num = folder.split('.')
  year = '20'+str(month[0:2])
  eqn_name = file_name.split('.')[0].txt
  path = '/projects/temporary/automates/er/gaurav/{year}/{month}/Simplified_MML/{folder}/{tyf}/{eqn_name}'
  eqn = open(path, 'r').readlines()[0]
  tgt_train.write(eqn + '\n')

for i in range(int(N*0.1)):
  image = random.choice(images)
  if image not in train:
    test.append(image)
    src_test.write(image + '\n')
    #{folder}_{TYF}_{file_name.split(".")[0]}.png
    folder, tyf, file_name = image.split('_')
    month, folder_num = folder.split('.')
    year = '20'+str(month[0:2])
    eqn_name = file_name.split('.')[0].txt
    path = '/projects/temporary/automates/er/gaurav/{year}/{month}/Simplified_MML/{folder}/{tyf}/{eqn_name}'
    eqn = open(path, 'r').readlines()[0]
    tgt_test.write(eqn + '\n')

for i in range(int(N*0.1)):
  image = random.choice(images)
  if image not in train and image not in test:
    val.append(image)
    src_val.write(image + '\n')
    #{folder}_{TYF}_{file_name.split(".")[0]}.png
    folder, tyf, file_name = image.split('_')
    month, folder_num = folder.split('.')
    year = '20'+str(month[0:2])
    eqn_name = file_name.split('.')[0].txt
    path = '/projects/temporary/automates/er/gaurav/{year}/{month}/Simplified_MML/{folder}/{tyf}/{eqn_name}'
    eqn = open(path, 'r').readlines()[0]
    tgt_val.write(eqn + '\n')
