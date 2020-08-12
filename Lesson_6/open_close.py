import cv2
import numpy as np

img_src = cv2.imread('picture/src.png', 1)

element8 = np.array([[1,1,1],[1,1,1],[1,1,1]], np.uint8)            #8近傍で処理を行う

img_open = cv2.morphologyEx(img_src, cv2.MORPH_OPEN, element8)

img_close = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, element8)

cv2.imwrite('picture/open_and_close_src.png', img_close)

#良い写真がなかったから、比較が難しい
#これはノイズ除去の手法である