import cv2
import numpy as np

img_src1 = cv2.imread('picture/src1.png', 1)
img_src2 = cv2.imread('picture/sky.png', 1)

img_dst = cv2.addWeighted(img_src1, 0.4, img_src2, 0.6, 0.0)

cv2.imwrite('picture/addweighted.png', img_dst)