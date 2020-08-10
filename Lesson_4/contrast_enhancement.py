import cv2
import numpy as np

img_src = cv2.imread('picture/sky.png', 1)

min = 50
max = 150

table = np.arange(256, dtype = np.uint8)
for i in range(0, 255):
    if i < min:
        table[i] = 0
    elif max < i and i < 255:
        table[i] = 255
    else:
        table[i] = 255 * (i - min) / (max - min)

img_dst = cv2.LUT(img_src, table)

cv2.imwrite('picture/contrast_enchance.png', img_dst)
