import math,numpy as np,cv2,os
import pickle
from imglib import imgfun

os.system('mode con: cols=30 lines=10')

directories = [p for p in os.listdir('.') if os.path.isdir(p)
               and not p.endswith('_')]

print(directories)

d = input('dir nr:')

d = directories[int(d)]

with open(d+'.pickle','rb') as f:
    final = pickle.load(f)

data = [cv2.imread(d+'/'+f) for f in os.listdir(d) if f.endswith('jpg')]

for n,img in enumerate(data):
    print(d,n,'/',len(data))
    res = imgfun(img)
    final.append([res,d])


with open(d+'.pickle','wb') as f:
    pickle.dump(final,f)
