#参考来源：https://blog.csdn.net/nominior/article/details/82954961?depth_1-utm
#_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

import cv2
import numpy as np
 
basicSize = 4
grayLevelSize = 8
gap = 2
 
img = cv2.imread('test.jpeg', 1)
grayImg = cv2.imread('test.jpeg', 0)
imgHeight,imgWidth = 300,300
 
dstImg = np.zeros(img.shape, np.uint8)
 
for i in range(basicSize,imgHeight-basicSize,gap):
    for j in range(basicSize,imgWidth-basicSize,gap):
        # 灰度等级统计
        grayLevel = np.zeros(grayLevelSize,np.uint8)                # 存放各个灰度等级的个数
        graySum = [0,0,0]                                           # 用于最后高频灰度等级均值计算
        # 对小区域进行遍历统计
        for m in range(-basicSize,basicSize):
            for n in range(-basicSize,basicSize):
                pixlv = int(grayImg[i + m, j + n] / (256 / grayLevelSize))       # 判断像素等级
                grayLevel[pixlv] += 1                               # 计算对应灰度等级个数
        # 找出最高频灰度等级及其索引
        mostLevel = np.max(grayLevel)
        mostLevelIndex = np.argmax(grayLevel)
        # 计算最高频等级内的所有灰度值的均值
        for m in range(-basicSize,basicSize):
            for n in range(-basicSize,basicSize):
                if int(grayImg[i + m, j + n] / (256 / grayLevelSize)) == mostLevelIndex:
                    graySum += img[i+m,j+n]
        (b,g,r) = (int(graySum[0]/mostLevel),int(graySum[1]/mostLevel),int(graySum[2]/mostLevel))
        # 写入目标像素
        for m in range(gap):
            for n in range(gap):
                dstImg[i+m,j+n] = (b,g,r)
 
cv2.imshow('',dstImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
print('complete')
