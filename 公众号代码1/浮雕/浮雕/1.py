#参考来源：https://blog.csdn.net/u010736662/article/details/89386003?depth_1-
#utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
import cv2
import numpy as np

def Filter_Fudiao(src_img):
    # filter=np.array([[-1,0,0],[0,0,0],[0,0,1]])
    filter = np.array([[-1, 0], [0, 1]])
    row=src_img.shape[0]
    col=src_img.shape[1]
    new_img=np.zeros([row,col],dtype=np.uint8)
    for i in range(row-1):
        for j in range(col-1):
            new_value = np.sum(src_img[i:i + 2, j:j + 2] * filter) + 128  # point multiply
            if new_value > 255:
                new_value = 255
            elif new_value < 0:
                new_value = 0
            else:
                pass
            new_img[i, j]=new_value
    return new_img

src_img_name='test.jpeg'
src_img=cv2.imread(src_img_name)
gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
new_img=Filter_Fudiao(gray_img)
cv2.imshow('src',src_img)
cv2.imshow('fudiao',new_img)
cv2.waitKey()
