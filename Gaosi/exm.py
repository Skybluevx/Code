# import os              #import语句的作用是用来导入模块，可以出现在程序任何位置
import cv2 as cv  # 导入openCV库
import skimage  # 导入skimage模块.scikit-image是一个图像处理算法的集合。它是基于scipy的一款图像处理包，它将图片作为numpy数组进行处理，方便进行后续运算。
# 必须首先安装numpy,scipy,matplotlib
import numpy as np  # 导入numpy模块。numpy是python扩展程序库，支持数组和矩阵运算，针对数组运算提供大量数学函数库。


def boxBlur(img):
    # 使用5x5的滤波核进行平滑
    blur = cv.boxFilter(img, -1, (5, 5))
    return blur


def gaussianBlur(img):
    #     使用高斯核进行平滑
    blur = cv.GaussianBlur(img, (5, 5), 1.5)
    return blur


def main():
    # 2. 定义图片类img
    path = r"234.png"
    img = cv.imread(path)
    start_t = cv.getTickCount()
    # 5. 加噪声，绘图
    # 3
    # add gaussian noise

    gauss_noiseImg = skimage.util.random_noise(
        img, mode='gaussian')  # 添加10%的高斯噪声
    gauss_noiseImg = gauss_noiseImg
    salt_noiseImg = skimage.util.random_noise(img, mode='salt')  # 添加椒盐噪声

    lb_gauss = cv.medianBlur(gauss_noiseImg.astype('float32'), 1)  # 中值滤波

    lb_salt = cv.medianBlur(salt_noiseImg.astype('float32'), 1)  # 中值滤波
    print(gauss_noiseImg.dtype, "gaussian noisy image dtype")  # 输出一个注释
    print(gauss_noiseImg.shape, "gaussian noisy image shape")  # 输出一个注释

    print(salt_noiseImg.dtype, "salt noisy image dtype")  # 输出一个注释
    print(salt_noiseImg.shape, "salt noisy image shape")  # 输出一个注释

    cv.namedWindow("Original Image", cv.WINDOW_NORMAL)  # 输出原图片的标题
    cv.imshow('Original Image', img)  # 输出原图片

    # Gaussian noisy image
    cv.namedWindow(
        "Added Gaussian Noise Image",
        cv.WINDOW_NORMAL)  # 输出高斯噪声图片的标题
    cv.imshow('Added Gaussian Noise Image', gauss_noiseImg)  # 输出高斯噪声图片

    # Salt noisy image
    cv.namedWindow("Added Salt Noise Image", cv.WINDOW_NORMAL)  # 输出椒盐噪声图片的标题
    cv.imshow('Added Salt Noise Image', salt_noiseImg)  # 输出椒盐噪声图片

    # 滤波后的图像
    cv.namedWindow("lbguass Image", cv.WINDOW_NORMAL)  # 输出滤波后高斯噪声图片标题
    cv.imshow('lbguass Image', lb_gauss)  # 输出滤波后高斯噪声图片
    cv.namedWindow("lbsalt Image", cv.WINDOW_NORMAL)  # 输出滤波后椒盐噪声图片标题
    cv.imshow('lbsalt Image', lb_salt)  # 输出滤波后椒盐噪声图片

    #####################################################

    stop_t = ((cv.getTickCount() - start_t) /
              cv.getTickFrequency()) * 1000  # 运行时间

    print(stop_t, "ms")  # 输出时间并加上单位

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
