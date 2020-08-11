import cv2
import numpy as np

img_src = cv2.imread('picture/src.png', 1)

img_dst = cv2.blur(img_src, (9,9))                          #blur:ぼかす

cv2.imwrite('picture/ave_ope_9*9.png', img_dst)

#視力が下がったみたいになる