# Preprocessing the data

import os, subprocess, glob, PIL

etree_path = '/projects/temporary/automates/er/gaurav/2014/1401/etree'
latex_path = '/projects/temporary/automates/er/gaurav/2014/1401/latex_equations'
image_path = '/projects/temporary/automates/er/gaurav/2014/1401/latex_images'

tokens = []
image_size = []

for folder_path in glob.glob(os.path.join(etree_path, '*')):
    folder = os.path.basename(folder_path)
    for tyf_path in glob.glob(os.path.join(folder_path, '*')):
        tyf_temp =  os.path.basename(tyf_path)
        tyf = 'Large_eqns' if tyf_temp == 'Large_MML' else 'Small_eqns'
        for file_path in glob.glob(os.path.join(tyf_path, '*')):
            file_name = os.path.basename(file_path).split(".")[0]

            eqn_path = os.path.join(latex_path, f'{folder}\{tyf}\{filename}.txt')
            eqn = open(eqn_path, 'r').readlines()[0]
            tokens.append(len([char for char in eqn if char != ' ']))

            img_path = os.path.join(image_path, f'{folder}\{tyf}\{filename}.png0001-1.png')
            (w, h) = PIL.Image.open(image_name).size
            image_size.append((w,h))


# Distribution

token_dict, image_dict = {}, {}
t50,t51_100, t101_150, t151_200, t200g = 0*(5)
w_600le_h100le, w600_800_h100le, w800g_h100le, w_600le_h100g, w600_800_h100g, w800g_h100g=0*6
for t in tokens:
    if t<=50:t50+=1
    elif 50<t<=100:t51_100+=1
    elif 100<t<=150:t101_150+=1
    elif 150<t<=200:t151_200+=1
    else: t200g+=1
for i in image_size:
    w, h = i
    if w<=600:
        if h<=100: w_600le_h100le+=1
        else: w_600le_h100g+=1

    if 600<w<=800:
        if h<=100: w600_800_h100le+=1
        else: w600_800_h100g+=1
    if w>800:
        if h<=100: w800g_h100le+=1
        else: w800g_h100g+=1

token_dict['t<=50']=t50
token_dict['50<t<=100']=t51_100
token_dict['100<t<=150']=t101_150
token_dict['150<t<=200']=t151_200
token_dict['t>200']=t200g

image_dict['w<=600, h<=100']=w_600le_h100le
image_dict['w<=600, h>100']=w_600le_h100g
image_dict['600<w<=800, h<=100']=w600_800_h100le
image_dict['600<w<=800, h>100']=w600_800_h100g
image_dict['w>800, h<=100']=w800g_h100le
image_dict['w>800, h>100']=w800g_h100g

# Plotting
plt.figure(figsize=(10,8))
plt.bar(token_dict.keys(), token_dict.values(), color='g')
plt.savefig('/projects/temporary/automates/er/gaurav/token_dict.png')

plt.figure(figsize=(10,8))
plt.bar(image_dict.keys(), image_dict.values(), color='r')
plt.savefig('/projects/temporary/automates/er/gaurav/image_dict.png')
