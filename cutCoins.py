import math,numpy as np,cv2,os
import skimage.morphology as mp
from matplotlib import pyplot as plt
from PIL import ImageEnhance,Image

file = [f for f in os.listdir('.') if f.endswith('jpg')]

def prepare_img(image,sh=1,con=1,col=1):
    d = 512 / image.shape[1]
    dim = (512, int(image.shape[0] * d))
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image

def colfun(image,col=1,con=1,sh=1):
    image = Image.fromarray(image)
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(col)
    image = np.array(image)
    return image

def get_circles(image,v=1,minR=20,maxR=70,minD=40):
    
    image = colfun(image,col=v)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray=255-gray
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    
    gray=255-gray
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    blurred= mp.dilation(mp.erosion(blurred))
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=2.2, minDist=minD,	#po wycieciu obrazka minDist mozna zmniejszyc
                               param1=200, param2=100, minRadius=minR, maxRadius=maxR)
    return circles

def get_circles_1(image):
    circle1,circl =[],[]
    circle= get_circles(image,v=1);
    if circle is not None:
        circle1 = [circle[0][i] for i in range(len(circle[0]))] 
        
        for k in range(2,12,2):
            c = get_circles(image,v=k)
            if c is not None:
                zn = [False for i in range(len(c[0]))]
                for i in range(len(circle[0])):
                    for j in range(len(c[0])):
                        if math.sqrt((circle[0][i][0] - c[0][j][0])**2 + (circle[0][i][1] - c[0][j][1])**2) < circle[0][i][2]:    
                             zn[j] = True
                    
                for j in range(len(zn)):
                    if zn[j] == False:
                        circle1.append(c[0][j])
                        circle= np.array([circle1])
        circl = np.array([circle1])
    return circl

def get_coins_cimg(circles,image):
    coins = []
    cimg = image.copy()
    if len(circles)>0:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(cimg,(i[0],i[1]),int(i[2]*1.05),(0,255,0),2) #*1.1 usunąć ;ostatni szerokosc
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            x = i[0]; y = i[1]; r = i[2]
            rectX = (x - r); rectY = (y - r)
            cut = image[rectY:(rectY+2*r),rectX:(rectX+2*r)].copy()
            R = len(cut)/2
            for i in range(len(cut)):
                for j in range(len(cut[i])):
                    if ((i-R)**2)+((j-R)**2)>(R**2):cut[i][j]=[255,255,255];
            coins.append(cut)
    return coins,cimg

j=int(input('name start with:'))
for f in file:
    image = cv2.imread(f)
    image = prepare_img(image)
    circles = get_circles_1(image)
    coins,cimg = get_coins_cimg(circles,image)
    if len(coins)>0:
        for i in coins:
            print(j)
            if len(i)>0:
                cv2.imwrite(str(j)+'.jpg',i)
                j+=1

