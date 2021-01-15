#参考来源：https://blog.csdn.net/weixin_38582851/article/details/80494205?depth_1-utm_source=distribute
#.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-taskimport numpy as np
import cv2
from PIL import Image,ExifTags
import numpy as np
 
def calcMeanAndVariance(img):
    row=img.shape[0]
    col=img.shape[1]
    #channel=img.shape[2]
    total=row*col
    print (row,col,total)
    mean=np.zeros((3))
    variance=np.zeros((3))
    sum=np.zeros((3))
 
    for i in range(row):
        for j in range(col):
            sum[0]+=img[i][j][0]
            sum[1]+=img[i][j][1]
            sum[2]+=img[i][j][2]
 
    mean[0]=sum[0]/total
    mean[1]=sum[1]/total
    mean[2]=sum[2]/total
    sum=np.zeros((3))
    for i in range(row):
        for j in range(col):
            sum[0]=np.square(img[i][j][0]-mean[0])
            sum[1]=np.square(img[i][j][1]-mean[1])
            sum[2]=np.square(img[i][j][2]-mean[2])
 
    variance[0]=np.sqrt(sum[0]/total)
    variance[1]=np.sqrt(sum[1]/total)
    variance[2]=np.sqrt(sum[2]/total)
    print (mean,variance)
    return mean,variance
 
def cololTransit(img1,img2):
    image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)
    image2=cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)
    mean1,variance1=calcMeanAndVariance(image1)
    mean2,variance2=calcMeanAndVariance(image2)
    #print (mean1,variance1)
    radio=np.zeros((3))
 
    radio[0]=variance2[0]/variance1[0]
    radio[1]=variance2[1]/variance1[1]
    radio[2]=variance2[2]/variance1[2]
 
    print('test', radio)
 
    row=image1.shape[0]
    col=image1.shape[1]
    for i in range(row):
        for j in range(col):
            image1[i][j][0]=min(255,max(0,radio[0]*(image1[i][j][0]-mean1[0])+mean2[0]))
            image1[i][j][1]=min(255,max(0,radio[1]*(image1[i][j][1]-mean1[1])+mean2[1]))
            image1[i][j][2]=min(255,max(0,radio[2]*(image1[i][j][2]-mean1[2])+mean2[2]))
    image = cv2.cvtColor(image1, cv2.COLOR_BGR2LAB)
    return image
 
if __name__=='__main__':
    img1=cv2.imread('1.jpeg')
    img2=cv2.imread('2.jpeg')
    cv2.namedWindow('src')
    cv2.namedWindow('dst')
    #cv2.resizeWindow('src',500,500)
    #cv2.resizeWindow('dst',500,500)
    cv2.imshow('src',img1)
    cv2.imshow('dst',img2)
    cv2.waitKey()
    cv2.destroyAllWindows()
 
    img=cololTransit(img1,img2)
    cv2.namedWindow('result')
    cv2.imshow('result',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    #print (img)
