import cv2
import math
import numpy as np

cv2.namedWindow('src')
cv2.namedWindow('dst')
cap = cv2.VideoCapture(0)

while True:
    ret, img_src = cap.read()

    cv2.imshow('src', img_src)

    ch = cv2.waitKey(1)
    if ch == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()