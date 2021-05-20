import sys, os, re, shutil, argparse, logging
import PIL
from PIL import Image
import numpy as np
import subprocess, shlex
from threading import Timer
import  multiprocessing
from multiprocessing import Pool

TIMEOUT = 10

# replace \pmatrix with \begin{pmatrix}\end{pmatrix}
# replace \matrix with \begin{matrix}\end{matrix}
template = r"""
\documentclass[12pt]{article}
\pagestyle{empty}
\usepackage{amsmath}
\newcommand{\mymatrix}[1]{\begin{matrix}#1\end{matrix}}
\newcommand{\mypmatrix}[1]{\begin{pmatrix}#1\end{pmatrix}}
\begin{document}
\begin{displaymath}
%s
\end{displaymath}
\end{document}
"""

def crop_image(img, output_path, default_size=None):
    old_im = Image.open(img).convert('L')
    img_data = np.asarray(old_im, dtype=np.uint8) # height, width
    nnz_inds = np.where(img_data!=255)
    if len(nnz_inds[0]) == 0:
        if not default_size:
            old_im.save(output_path)
            return False
        else:
            assert len(default_size) == 2, default_size
            x_min,y_min,x_max,y_max = 0,0,default_size[0],default_size[1]
            old_im = old_im.crop((x_min, y_min, x_max+1, y_max+1))
            old_im.save(output_path)
            return False
    y_min = np.min(nnz_inds[0])
    y_max = np.max(nnz_inds[0])
    x_min = np.min(nnz_inds[1])
    x_max = np.max(nnz_inds[1])
    old_im = old_im.crop((x_min, y_min, x_max+1, y_max+1))
    old_im.save(output_path)
    return True

def pad_group_image(img, output_path, pad_size, buckets):
    PAD_TOP, PAD_LEFT, PAD_BOTTOM, PAD_RIGHT = pad_size
    old_im = Image.open(img)
    old_size = (old_im.size[0]+PAD_LEFT+PAD_RIGHT, old_im.size[1]+PAD_TOP+PAD_BOTTOM)
    j = -1
    for i in range(len(buckets)):
        if old_size[0]<=buckets[i][0] and old_size[1]<=buckets[i][1]:
            j = i
            break
    if j < 0:
        new_size = old_size
        new_im = Image.new("RGB", new_size, (255,255,255))
        new_im.paste(old_im, (PAD_LEFT,PAD_TOP))
        new_im.save(output_path)
        return False
    new_size = buckets[j]
    new_im = Image.new("RGB", new_size, (255,255,255))
    new_im.paste(old_im, (PAD_LEFT,PAD_TOP))
    new_im.save(output_path)
    return True

def downsample_image(img, output_path, ratio):
    assert ratio>=1, ratio
    if ratio == 1:
        return True
    old_im = Image.open(img)
    old_size = old_im.size
    new_size = (int(old_size[0]/ratio), int(old_size[1]/ratio))

    new_im = old_im.resize(new_size, PIL.Image.LANCZOS)
    new_im.save(output_path)
    return True

def run(cmd, timeout_sec):
    proc = subprocess.Popen(cmd, shell=True)
    kill_proc = lambda p: p.kill()
    timer = Timer(timeout_sec, kill_proc, [proc])
    try:
        timer.start()
        stdout,stderr = proc.communicate()
    finally:
        timer.cancel()

def main():

    tgt = open('/projects/temporary/automates/er/gaurav/tgt-test.txt').readlines()
    pred = open('/projects/temporary/automates/er/gaurav/pred.txt').readlines()

    pred_dir = '/projects/temporary/automates/er/gaurav/OpenNMT_im2markup/OpenNMT-older-version/images_for_edit_distance/images_pred'
    tgt_dir = '/projects/temporary/automates/er/gaurav/OpenNMT_im2markup/OpenNMT-older-version/images_for_edit_distance/images_gold'

    for fi, F in enumerate([tgt, pred]):
        for idx, l in enumerate(F):

            temp=[]
            folder = tgt_dir if fi == 0 else folder = pred_dir
            temp.append([folder, idx, l])

    print('temp done!')
    with Pool(multiprocessing.cpu_count()-10) as pool:
        result = pool.map(pooling, temp)

def pooling(args_array):

    print('in pooling!')
    folder, idx, l = args_array
    output_path=folder
    print(folder)

    l = l.strip()
    l = l.replace(r'\pmatrix', r'\mypmatrix')
    l = l.replace(r'\matrix', r'\mymatrix')
    # remove leading comments
    l = l.strip('%')
    if len(l) == 0:
        l = '\\hspace{1cm}'
    # \hspace {1 . 5 cm} -> \hspace {1.5cm}
    for space in ["hspace", "vspace"]:
        match = re.finditer(space + " {(.*?)}", l)
        if match:
            new_l = ""
            last = 0
            for m in match:
                new_l = new_l + l[last:m.start(1)] + m.group(1).replace(" ", "")
                last = m.end(1)
            new_l = new_l + l[last:]
            l = new_l

    try:
        tex_filename = idx+'.tex'
        log_filename = idx+'.log'
        aux_filename = idx+'.aux'
        with open(tex_filename, "w") as w:
            print((template%l), file=w)
        run("pdflatex -interaction=nonstopmode %s  >/dev/null"%tex_filename, TIMEOUT)
        os.remove(tex_filename)
        os.remove(log_filename)
        os.remove(aux_filename)
        pdf_filename = tex_filename[:-4]+'.pdf'
        png_filename = tex_filename[:-4]+'.png'


        os.system("convert -density 200 -quality 100 %s %s"%(pdf_filename, png_filename))
        os.remove(pdf_filename)
        if os.path.exists(png_filename):
            crop_image(png_filename, output_path)
            os.remove(png_filename)
    except: print('error with  ', idx)

main()
print('jobs done!')
