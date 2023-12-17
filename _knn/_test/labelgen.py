import math,numpy as np,cv2,os
import pickle

directories = [p for p in os.listdir('.') if os.path.isdir(p)
               and not p.endswith('_')]

final = []
for d in directories:
    data = [cv2.imread(d+'/'+f) for f in os.listdir(d) if f.endswith('jpg')]
    for n,img in enumerate(data):
        print(d,n)
        final.append([img,d])

with open('test.pickle','wb') as f:
    pickle.dump(final,f)
