import os, json
import matplotlib.pyplot as plt

path = '/projects/temporary/automates/er/gaurav/replicate_im2markup/im2markup_100K/im2markup/scores.json'

scores  = json.load(open(path, 'r'))

zero_to_ten=0
ten_to_twenty=0
twenty_to_thirty=0
thirty_to_fourty=0
fourty_to_fifty=0
fifty_to_sixty=0
sixty_to_seventy=0
seventy_to_eighty=0
eighty_to_ninety=0
ninety_to_hundred=0

i=0
for s in scores:
    i+=1
    s=s.replace(',', '')
    if 0<=float(s)<10:
        zero_to_ten+=1
    elif 10<=float(s)<20:
        ten_to_twenty+=1
    elif 20<=float(s)<30:
        twenty_to_thirty+=1
    elif 30<=float(s)<40:
        thirty_to_fourty+=1
    elif 40<=float(s)<50:
        fourty_to_fifty+=1
    elif 50<=float(s)<60:
        fifty_to_sixty+=1
    elif 60<=float(s)<70:
        sixty_to_seventy+=1
    elif 70<=float(s)<80:
        seventy_to_eighty+=1
    elif 80<=float(s)<90:
        eighty_to_ninety+=1
    else:
        ninety_to_hundred+=1

Dict={}
Dict['0-10']=zero_to_ten
Dict['10-20']=ten_to_twenty
Dict['20-30']=twenty_to_thirty
Dict['30-40']=thirty_to_fourty
Dict['40-50']=fourty_to_fifty
Dict['50-60']=fifty_to_sixty
Dict['60-70']=sixty_to_seventy
Dict['70-80']=seventy_to_eighty
Dict['80-90']=eighty_to_ninety
Dict['90-100']=ninety_to_hundred


plt.figure(figsize=(8,10))
plt.bar(list(Dict.keys()), Dict.values(), color='g')
plt.xlabel('BLEU scores')
plt.ylabel('#eqns')
plt.xticks(rotation=30)
plt.show()
plt.savefig('histogram.png')

print(i)
