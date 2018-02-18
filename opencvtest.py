import cv2
import numpy as np
import random
from math import *
# import an image
class image:
    def __init__(self,na):
        self.dir='/home/hui/Pictures/'
       # self.name=raw_input('please input the picture name')
        self.name=na
        self.mode=cv2.IMREAD_COLOR
        self.im=cv2.imread(self.dir+self.name,self.mode)

    def reconf(self):
        self.im = cv2.imread(self.dir + self.name, self.mode)

    def modechoose(self,modex):
        if modex=='color':
            self.mode=cv2.IMREAD_COLOR
        elif modex == 'gray':
            self.mode=cv2.IMREAD_GRAYSCALE
        elif modex== 'alpha':
            self.mode=cv2.IMREAD_UNCHANGED
        else:
            print('wrong mode')
        self.reconf()

    def routechange(self):
        self.dir=raw_input('input your new route')
        self.name=raw_input('input your new filename')
        self.reconf()

    def show(self):
        cv2.imshow('huihui',self.im)
        k=cv2.waitKey(0)&0xFF
        if k==27:   #wait for esc coming
            self.dele('all')

    def dele(self,modeb):
        if  modeb=='all':
            cv2.destroyAllWindows()
        if  modeb=='name':
            cv2.destroyWindow(raw_input("please input your window's name"))

    def saveas(self):
        cv2.imwrite(raw_input('input your new filename'),self.im)
    def getpixel(self,a,b,c):     #pixel is xiangshu  ni dong de~  a is x b is y  c is 0 1 2  B G R
        print self.im.item(a,b,c)
    def setpixel(self,e,f,g,h):         # e f g is like the a b c and h is the new pixel value
        self.im.itemset((e,f,g),h)
look=image('hsj.jpeg')
shino =image('shino.jpeg')
juhua=image('juhua.jpg')
juhua.show()
'''for a in range(0,5000)
x=random.randint(0,280)
y=random.randint(0,449)
for b in range(0,3):
value=random.randint(0,255)
look.setpixel(x,y,b,value)'''

'''look.show()
shino.show()'''
'''test=look.im[50:140,100:200]
cv2.imshow('hui',test)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()'''
rows,cols,channel=look.im.shape
row,col,channels=shino.im.shape
pix=[]
sbliye=[]
hezi=[]
R=[]
G=[]
B=[]
n=130
route='/home/hui/'
green='sbliyeG.txt'
blue='sbliyeB.txt'
red='sbliyeR.txt'
gg=open(route+green,'w')
bb=open(route+blue,'w')
rr=open(route+red,'w')
'''M=cv2.getRotationMatrix2D((220,240),0,0.6)
K = cv2.getRotationMatrix2D((300, 300), 0, 0.5)
dst=cv2.warpAffine(look.im,M,(cols,rows))
shino1=cv2.warpAffine(shino.im,K,(col,row))
cv2.imshow('hui',dst)
cv2.imshow('shino',shino1)
for times in range(0,n):
    M=cv2.getRotationMatrix2D((215,248),(times)*360.0/n,1)
    dsto=cv2.warpAffine(dst,M,(cols,rows))
    if times==129:
        cv2.imshow('hi',dsto)
    look.im=dst
    for led in range(1,33):
        for i in range(0,3):
            pix.append(dsto.item(215,248-5*led,i))
            shino1.itemset((300, 300-5*led, i),dsto.item(215,248-5*led,i) )
    K = cv2.getRotationMatrix2D((300, 300), 360.0 / n, 1)
    shino1 = cv2.warpAffine(shino1, K, (col, row))
cv2.imshow('huihui', shino1)'''
M=cv2.getRotationMatrix2D((220,240),0,0.6)
dst=cv2.warpAffine(juhua.im,M,(cols,rows))
def qm(x,y,nn):    #x is xiangsu x  y is xiangsu y
    xz=195
    yz=154
    x0=x
    y0=y
    a=pi/65
    A=np.matrix([[cos(nn*a),-sin(nn*a)],[sin(nn*a),cos(nn*a)]])
    X=np.matrix([x0,y0])
    X1=X*A
    xy=X1.tolist()
    x1=int(round(xy[0][0]))
    y1=int(round(xy[0][1]))
    x1=x1+xz
    y1=y1+yz
    return [x1,y1]
zuobiao=[]
for times in range(0,130):
    for nnn in range(0,32):
        aaa=qm(0,4*nnn+1,times)
        zuobiao.append(aaa)
        for i in range(0,3):
            pix.append(dst.item(aaa[0],aaa[1],i))
            shino.im.itemset((aaa[0],aaa[1],i),dst.item(aaa[0],aaa[1],i))
cv2.imshow('hui',dst)
shino.show()
lenth=n*32*3
for time in range(0,lenth):
    if pix[time]<128:
        sbliye.append('0')
    else :
        sbliye.append('1')
for ttt in range(0,n):
    for ledp in range(0,32):
        B.append(sbliye[(ttt+1)*96-(ledp+1)*3])
        G.append(sbliye[(ttt+1)*96-(ledp+1)*3+1])
        R.append(sbliye[(ttt+1)*96-(ledp+1)*3+2])
    b=''.join(B)
    g=''.join(G)
    r=''.join(R)
    B=[]
    G=[]
    R=[]
    BB=hex(int(b,2))
    GG=hex(int(g,2))
    RR=hex(int(r,2))

    if ttt==n-1:
        rr.write(RR+'\n')
        bb.write(BB+'\n')
        gg.write(GG+'\n')

    else :
        if (ttt+1)%4==0 and ttt!=0:
            rr.write(RR+',\n')
            bb.write(BB + ',\n')
            gg.write(GG + ',\n')
        else :
            rr.write(RR+'   ,')
            bb.write(BB+'   ,')
            gg.write(GG+'   ,')
            
rr.close()
bb.close()
gg.close()


k=cv2.waitKey(0)&0xFF
if k==27:
    cv2.destroyAllWindows()






