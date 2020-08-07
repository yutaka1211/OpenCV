import math
import cv2
import numpy as np

file_src = 'src.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 1)

cv2.namedWindow('src')
cv2.namedWindow('dst')

img_dst = cv2.flip(img_src, flipCode = 0)

cv2.imshow('stc', img_src)
cv2.imshow('dst', img_dst)

cv2.imwrite(file_dst, img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()