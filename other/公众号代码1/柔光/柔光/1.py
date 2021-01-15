#参考来源：https://blog.csdn.net/wsp_1138886114/article/details/82876153?depth_
#1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
import cv2
import numpy as np

def img_filter(img):                   #计算图像梯度（高反差像素）
    x=cv2.Sobel(img,cv2.CV_16S,1,0)
    y=cv2.Sobel(img,cv2.CV_16S,0,1)

    absx=cv2.convertScaleAbs(x)
    absy=cv2.convertScaleAbs(y)
    dist=cv2.addWeighted(absx,0.5,absy,0.5,0)
    return dist

def addImage(img1, img2,alpha):
    h, w, _ = img1.shape
    """
        函数要求两张图必须是同一个size
        alpha，beta，gamma可调
    """
    img2 = cv2.resize(img2, (w, h), interpolation=cv2.INTER_AREA)

    beta = 1 - alpha
    gamma = 0
    img_add = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    return img_add


if __name__ == '__main__':
    img1=cv2.imread('test.jpeg', cv2.IMREAD_COLOR)  # 以彩色图的形式读入
    dist_img = img_filter(img1)                        # 执行高通过滤
    for i in range(1,10):                              # 循环执行（不同的alpha）：显示叠加图，写入处理后的图像
        IMG_Add = addImage(img1,dist_img,i*0.1)        # alpha，beta，gamma可调
        cv2.imshow('img_add_'+ str(i), IMG_Add)
        cv2.imwrite('img_add_'+ str(i)+".png", IMG_Add)
        cv2.imshow("img1",img1)
        # cv2.waitKey()

