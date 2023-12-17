import math,numpy as np,cv2,os
import pickle,operator
from imglib import imgfun,dist

succ,allchoice=0,0

pickle_file = [f for f in os.listdir() if f.endswith('.pickle')
               and not f.startswith('test')]
neighbours = []

for p in pickle_file:
    with open(p,'rb')as f:
        neighbours.append(pickle.load(f))

with open('test.pickle','rb')as f:
    labels = pickle.load(f)

how_many_vote = input('how_many_vote:')


first_use = True

allimg = len(labels)


c=0

dec_count,nom_count={},{}

for imglabel in labels:
    img,label = imglabel

    vec1 = imgfun(img)

    res =[]
    vote = {}

    for n in neighbours:
        for pic in n:
            vec2,nom = pic
            res.append([dist(vec1,vec2),nom])
            vote[nom]= 0
            if dec_count.get(nom) is None:dec_count[nom]=0
            if nom_count.get(nom) is None:nom_count[nom]=0
            
    res = sorted(res, key=lambda x: x[0])

    for i in range(len(res)):
        if i > int(how_many_vote)-1:break
        vote[res[i][1]]+=1
            
    dec = max(vote.items(), key=operator.itemgetter(1))[0]
    if label==dec:
        succ+=1
        dec_count[label]+=1
    
    allchoice+=1
    nom_count[label]+=1

    print(c,'/',allimg,':',dec,label,vote);c+=1
    
print('accuracy:',succ/allchoice)

    
for cn in dec_count:
    if nom_count[cn]!=0:
        dec_count[cn]/=nom_count[cn]
    else: dec_count[cn]=None
    

with open('acc.txt','w') as file:
    file.write('summary:'+str(dec_count)+'\n')
    file.write('accuracy:'+str(succ/allchoice))

input('press enter...')
        
