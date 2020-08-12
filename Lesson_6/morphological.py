import cv2
import numpy as np

img_src = cv2.imread('picture/src.png', 1)

element8 = np.array([[1,1,1],[1,1,1],[1,1,1]], np.uint8)            #8近傍で処理を行う

#変数(入力画像,カーネル,補間)
img_dilate = cv2.dilate(img_src, element8, iterations = 1)
img_erode = cv2.erode(img_src, element8, iterations = 1)

cv2.imwrite('picture/dilate_src.png', img_dilate)
cv2.imwrite('picture/erode_src.png', img_erode)


"""
膨張処理:図形を外側に1画素広げる処理であり、微小な孔を防ぐことができる->対象物体が綺麗に白くなる
収縮処理:図形を内側に1画素狭める処理であり、独立点を防ぐことができる->周りが綺麗に黒くなる
"""