import os, shutil

path = '/home/gauravs/github/img2mml/img2mml_version1/data'
path_images = os.path.join(path, 'images')
xfer_images = '/home/gauravs/github/Learn_git/small_data/images'
path_mml = open(os.path.join(path, 'mml.txt')).readlines()
xfer_mml = open('/home/gauravs/github/Learn_git/small_data/mml.txt', 'w')

count=0
while count<=7:
    # xfering image
    shutil.copyfile(os.path.join(path_images, f'{count}.png'),os.path.join(xfer_images, f'{count}.png'))
    # xfering mml 
    xfer_mml.write(path_mml[count])
    # increament count
    count+=1

