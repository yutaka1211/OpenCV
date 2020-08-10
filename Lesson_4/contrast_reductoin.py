import cv2
import numpy as np

img_src = cv2.imread('picture/sky.png', 1)

min = 100
max = 200

table = np.arange(256, dtype = np.uint8)
for i in range(0, 255):
    table[i] = min + i * (max - min) / 255                          #トーンカーブの式: I_dst = MIN + I_src * (MAX - MIN) / 255

img_dst = cv2.LUT(img_src, table)

cv2.imwrite('picture/contrast_reduction_sky.png', img_dst)