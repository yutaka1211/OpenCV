import cv2
import numpy as np

img_src = cv2.imread('picture/moon.png', 1)

img_dst = 255 - img_src                     #ネガポジ反転

cv2.imwrite('picture/moon_negaposi_inversion.png', img_dst)