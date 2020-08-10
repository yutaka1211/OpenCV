import cv2
import numpy as np

img_src = cv2.imread('picture/value_adjust_moon.png', 1)

shift = 100

table = np.arange(256, dtype = np.uint8)

for i in range(0, 255):                                         #トーンカーブの式: I_dst=I_src + shift (I_src<0ならI_dst=0, I_src>255ならI_dst=255)
    j = i + shift
    if j < 0:
        table[i] = 0
    elif j > 255:
        table[i] = 255
    else:
        table[i] = j

img_dst = cv2.LUT(img_src, table)

cv2.imwrite('picture/value_adjust_moon.png', img_dst)
