import cv2
import math
import numpy as np

cv2.namedWindow('src')
cv2.namedWindow('dst')
cap = cv2.VideoCapture(0)

while True:
    ret, img_src = cap.read()

    img_dst = cv2.flip(img_src, flipCode = 0)

    cv2.imshow('src', img_src)
    cv2.imshow('dst', img_dst)
    ch = cv2.waitKey(1)
    if ch == ord('q'):
        break

cv2.destroyAllWindows()