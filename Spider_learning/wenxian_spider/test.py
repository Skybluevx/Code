"""
    图像剪切，去除图像周围空白
"""
from PIL import Image


img = Image.open("bg_img.png")

width, height = img.size
height_num = []
width_num = []
for i in range(height):
    for m in range(width):
        a, z, x, c = img.getpixel((m, i))
        if x < 220:
            # print(i)
            height_num.append(i)
            break
for i in range(width):
    for o in range(height):
        a, z, x, c = img.getpixel((i, o))
        if x < 220:
            # print(i)
            width_num.append(i)
            break
print(height_num, width_num)
height_up_line = height_num[0] + 5
height_down_line = height_num[-1] - 5
width_left_line = width_num[0]
width_right_line = width_num[-1]
result = img.crop((width_left_line, height_up_line, width_right_line, height_down_line))
result.save("result.png")
# print(img.getpixel((125, 145)))


