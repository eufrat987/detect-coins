import math,numpy as np,cv2,os
import pickle
from imglib import imgfun

directories = [p for p in os.listdir('.') if os.path.isdir(p)
               and not p.endswith('_')]

for d in directories:
    data = [cv2.imread(d+'/'+f) for f in os.listdir(d) if f.endswith('jpg')]
    final = []
    for n,img in enumerate(data):
        print(d,n)
        res = imgfun(img)
        final.append([res,d])


    with open(d+'.pickle','wb') as f:
        pickle.dump(final,f)
