import math,numpy as np,cv2,os
import skimage.morphology as mp
from matplotlib import pyplot as plt
from PIL import ImageEnhance,Image

directories = [p for p in os.listdir('.') if os.path.isdir(p)
               and not p.endswith('_')]

size = int(input('test size:'))

os.mkdir('train')
os.mkdir('test')

for d in directories:
    os.mkdir('train/'+d)
    os.mkdir('test/'+d)
    file = [f for f in os.listdir(d) if f.endswith('jpg')]
    for f in file:
        print(f)
        dig = int(f[:-4])
        if dig%size==0:os.rename(d+'/'+f,'test/'+d+'/'+f)
        else: os.rename(d+'/'+f,'train/'+d+'/'+f)
