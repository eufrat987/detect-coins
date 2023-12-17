import math,numpy as np,glob,cv2,os
from PIL import ImageEnhance,Image

def dist(vec1,vec2):
    if len(vec1)!=len(vec2):
        print('err len')
        return
    d=0
    for i in range(len(vec1)):
        for j in range(len(vec1)):
           d+=(vec1[i][j]-vec2[i][j])**2
    return d**(1/2)

def cradn(coin,rmin,rmax):# <0,1>
    R = len(coin)/2
    rmin*=R;rmax*=R 
    res = np.zeros(np.shape(coin))
    for i in range(len(coin)):
        for j in range(len(coin[i])):
            if ((((i-R)**2)+((j-R)**2)<rmax**2)
                and (((i-R)**2)+((j-R)**2)>rmin**2)):
                res[i][j]=coin[i][j]
            else: res[i][j]=None
    return res

def colfun(image,col=1):
    image = Image.fromarray(image)
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(col)
    image = np.array(image)
    return image

def per(v,i):
    return np.nanpercentile(v,i)

def imgfun(img):

    img = colfun(img,2)

    male = cradn(img,0,1/3)
    srednie = cradn(img,1/3,2/3)
    duze = cradn(img,2/3,1)

    r,g,b=[],[],[]
    for i in np.arange(5,100,10):
        male_0,male_1,male_2 = per(male[:,:,0],i),per(male[:,:,1],i),per(male[:,:,2],i)
        srednie_0,srednie_1,srednie_2 = per(srednie[:,:,0],i),per(srednie[:,:,1],i),per(srednie[:,:,2],i)
        duze_0,duze_1,duze_2 = per(duze[:,:,0],i),per(duze[:,:,1],i),per(duze[:,:,2],i)
        tmp = male_0**2 + srednie_0**4 + duze_0**6
        r.append(tmp)
        tmp = male_1**2 + srednie_1**4 + duze_1**6
        g.append(tmp)
        tmp = male_2**2 + srednie_2**4 + duze_2**6
        b.append(tmp)

    vec1 = [r,g,b]
    return vec1
