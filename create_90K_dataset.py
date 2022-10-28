import os, random, shutil
from tokenize_mml import token_main
import multiprocessing
from multiprocessing import Pool, Lock, TimeoutError


random.seed(20)

omml = open("OMML-90K-dataset/OMML-90K.txt", "w")
olatex = open("OMML-90K-dataset/OLATEX-90K.txt", "w")

root = "/projects/temporary/automates/er/gaurav/complete_data"

# check the available_etrees
available_etrees = list()
count_50, count_100, count_150 = 0,0,0
count_200, count_250, count_300 = 0,0,0
count_gt300 = 0


years = [14,15,16,17,18]
months = ["01", "02", "03", "04",
                  "05", "06", "07", "08",
                            "09", "10", "11", "12"]

def write_eqn(mml, latex, imagepath, NEqn):
        #print(NEqn)
        if "\n" not in mml:
            mml=mml+"\n"
        omml.write(mml)

        if "\n" not in latex:
            latex=latex+"\n"
        olatex.write(latex)

        dst = f"OMML-90K-dataset/IMAGES-90K/{NEqn}.png"
        shutil.copyfile(imagepath, dst)

NEqn = 0
yr = str(random.sample(years, 1)[0])
month = random.sample(months, 1)[0]
p1 = os.path.join(root, f"20{yr}/{yr}{month}" )
etrees = os.path.join(p1, "etree")
etree_list = random.sample(os.listdir(etrees),10)

for folder in etree_list:
    if NEqn<=10000:
        p2 = os.path.join(etrees, folder)
        for tyf in os.listdir(p2):
            p3 = os.path.join(p2, tyf)
            for eqn in os.listdir(p3):
                eqn_num = eqn.split(".")[0]
                mmlpath = root + f"/20{yr}/{yr}{month}/Simplified_mml/{folder}/{tyf}/{eqn_num}.txt"
                latexpath = root + f"/20{yr}/{yr}{month}/latex_equations/{folder}/{tyf.split('_')[0]}_eqns/{eqn_num}.txt"

                imagepath = root + f"/20{yr}/{yr}{month}/latex_images/{folder}/{tyf.split('_')[0]}_eqns/{eqn_num}.png0001-1.png"
                if not os.path.exists(imagepath):
                    imagepath = root + f"/20{yr}/{yr}{month}/latex_images/{folder}/{tyf.split('_')[0]}_eqns/{eqn_num}.png"

                latex = open(latexpath).readlines()[0]
                mml = open(mmlpath).readlines()[0]

                if (len(latex)>10) and (len(mml.split())>5) and ("&#xA0" not in mml):
                    print(NEqn)
                    tok_mml, tok_len = token_main(mml)
                    if (tok_len < 50) and (count_50 <= 10000):
                        count_50+=1
                        write_eqn(mml, latex, imagepath, NEqn)
                        NEqn+=1
                    elif (tok_len>=50 and tok_len < 100) and (count_100 <= 35000):
                        count_100+=1
                        write_eqn(mml, latex, imagepath, NEqn)
                        NEqn+=1
                    elif (tok_len>=100 and tok_len < 150) and (count_150 <= 25000):
                        count_150+=1
                        write_eqn(mml, latex, imagepath, NEqn)
                        NEqn+=1
                    elif (tok_len>=150 and tok_len < 200) and (count_200 <= 12000):
                        count_200+=1
                        write_eqn(mml, latex, imagepath, NEqn)
                        NEqn+=1
                    elif (tok_len>=200 and tok_len < 250) and (count_250 <= 5000):
                        count_250+=1
                        write_eqn(mml, latex, imagepath, NEqn)
                        NEqn+=1
                    elif (tok_len>=250 and tok_len < 300) and (count_300 <= 2000):
                        count_300+=1
                        write_eqn(mml, latex, imagepath, NEqn)
                        NEqn+=1
                    elif (tok_len>=300) and (count_gt300 <= 1000):
                        count_gt300+=1
                        write_eqn(mml, latex, imagepath, NEqn)
                        NEqn+=1

    else:
        break
