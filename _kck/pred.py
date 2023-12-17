import math,numpy as np,cv2,os
import pickle,operator
from imglib import imgfun,dist


pickle_file = [f for f in os.listdir() if f.endswith('.pickle')
                   and not f.startswith('test')]
neighbours = []

for p in pickle_file:
    with open(p,'rb')as f:
        neighbours.append(pickle.load(f))


def predict(img):
    vec1 = imgfun(img)
    
    res =[]
    vote={}

    for n in neighbours:
        for pic in n:
            vec2,nom = pic
            res.append([dist(vec1,vec2),nom])
            vote[nom]=0

    res = sorted(res, key=lambda x: x[0])

    how_many_vote = 13 #input('how_many_vote:')

    for i in range(len(res)):
        if i > int(how_many_vote)-1:break
        vote[res[i][1]]+=1
            
    print(vote)
    print(max(vote.items(), key=operator.itemgetter(1))[0])



        
