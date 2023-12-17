import math,numpy as np,cv2,os
import pickle
from imglib import imgfun,dist

pickle_file = [f for f in os.listdir() if f.endswith('.pickle')]
neighbours = []

for p in pickle_file:
    with open(p,'rb')as f:
        neighbours.append(pickle.load(f))

files = [f for f in os.listdir('.') if f.endswith('jpg')]


img = cv2.imread(files[0])

vec1 = imgfun(img)

res =[]
vote={}
min = 10000

for n in neighbours:
    for pic in n:
        vec2,nom = pic
        res.append([dist(vec1,vec2),nom])
        vote[nom]=0

res = sorted(res, key=lambda x: x[0])

how_many_vote = input('how_many_vote:')

for i in range(len(res)):
    if i > int(how_many_vote)-1:break
    vote[res[i][1]]+=1
        
print(vote)
input()



        
