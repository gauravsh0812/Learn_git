import os, PIL, multiprocessing
from PIL import Image
from multiprocessing import Lock, Pool

lock=Lock()

def main(src):

  global lock

  temp = []
  for idx, s in enumerate(src[:100]):
    month, f, t, name = s.split('_')
    year = '20'+str(month[0:2])
    folder = str(month)+'.'+str(f)
    tyf = str(t)+'_eqns'
    eqn_name = name.split('.')[0]+'.txt'
    s_temp=s.replace('\n','')
    img_path = f'/projects/temporary/automates/er/gaurav/data_17M/xfer/images/{s_temp}'

    temp.append([img_path, year, month, folder, tyf, eqn_name])

  print('temp done!')

  pool = Pool(multiprocessing.cpu_count()-10)
  with open('/projects/temporary/automates/er/gaurav/data_17M/xfer/tgt-train-MP.txt') as tgt:
    with open('/projects/temporary/automates/er/gaurav/data_17M/xfer/src-train-new-MP.txt') as src_new:
      for result in pool.imap(parallel, temp):
        if Flag:
          lock.acquire()
          tgt.write(eqn)
          src.write(img_path_)
          lock.release()


def parallel(args):

  img_path, year, month, folder, tyf, eqn_name = args
  Flag=False
  try:
    IMG = Image.open(img_path)
    final_path = f'/projects/temporary/automates/er/gaurav/{year}/{month}/latex_equations/{folder}/{tyf}/{eqn_name}'
    eqn = open(final_path, 'r').readlines()[0]
    Flag = True
    return eqn, img_path_, Flag

  except:
    return Flag
    pass

if __name__ == '__main__':
    src = open('/projects/temporary/automates/er/gaurav/data_17M/xfer/src-train.txt', 'r').readlines()
    main(src)
