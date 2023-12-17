import math,numpy as np,glob,cv2,os
from PIL import ImageEnhance,Image

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def imgfun(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    tmimg = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,11,2)
    
    canimg = cv2.Canny(img,np.nanpercentile(img,25),np.nanpercentile(img,75))

    v1, v2, v3, v4 = [], [], [], []
    nc = 5
    c = [cradn(img,i/nc,(i+1)/nc) for i in range(nc)]
    for oimg in c:
        b,g,r = cv2.split(oimg)
        perSet = np.arange(5,100,10)
        pb = [np.nanpercentile(b,i)for i in perSet]
        pg = [np.nanpercentile(g,i)for i in perSet]
        pr = [np.nanpercentile(r,i)for i in perSet]
        for i in range(len(pb)-1):
            v1.append(pb[i+1]-pg[i])
            v2.append(pg[i+1]-pr[i])
            v3.append(pb[i+1]-pr[i])

    v4.append(len(img))
    
    v4.append(np.nanmean(canimg))
    v4.append(np.nanmean(tmimg))

    v4.append(np.nanmean(canimg))
    v4.append(np.nanmean(tmimg))
    
    vec1 = [v1,v2,v3,v4]
    return vec1
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def dist(vec1,vec2):
    if len(vec1)!=len(vec2):
        print('err len')
        return
    d=0
    for i in range(len(vec1)):
        for j in range(len(vec1[i])):
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

def colfun(image,col=1,con=1,sh=1,br=1):
    image = image.copy()
    image = Image.fromarray(image)

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(col)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(con)

    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(sh)
	
	
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(br)
	
    
    image = np.array(image)
    return image

def per(v,i):
    return np.nanpercentile(v,i)

