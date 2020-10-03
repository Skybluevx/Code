import skimage
from skimage import io
import cv2 as cv


class Gaosi(object):

    def __init__(self):
        self.img = io.imread(r"./234.png")

    def main(self):
        # 添加高斯噪声
        # self.add_gaosi_noise()

        # 添加椒盐噪声
        # self.add_jy_noise()

        # 添加脉冲噪声
        self.add_mc_moise()

        # 采用不同尺寸的 boxFilter 对三张噪声图进行去噪
        self.reduce()

        # 用不同的 sigma 的高斯滤波对三张噪声图进行去噪
        self.sigma()

    def sigma(self):
        pass

    def reduce(self):
        pass

    def add_mc_moise(self):
        pass

    def add_jy_noise(self):
        noisy = skimage.util.random_noise(self.img, mode="salt")
        io.imsave("./salt_234.png", noisy)

    def add_gaosi_noise(self):
        noisy = skimage.util.random_noise(self.img, mode="gaussian", var=0.01)
        io.imsave("./gaosi_234.png", noisy)


if __name__ == '__main__':
    go = Gaosi()
    go.main()
