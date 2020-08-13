import cv2
import numpy as np
import matplotlib.pyplot as plt

img_src1 = cv2.imread('picture/src1.png', 1)
img_src2 = cv2.imread('picture/sky.png', 1)

img_g1 = cv2.cvtColor(img_src1, cv2.COLOR_BGR2GRAY)                         #グレー画像にする

img_mskg = cv2.Canny(img_g1, 20, 200)
element8 = np.array([[1,1,1], [1,1,1],[1,1,1]], np.uint8)
img_mskg = cv2.dilate(img_mskg, element8, iterations = 1)
img_mskg = cv2.erode(img_mskg, element8, iterations = 1)

img_mskg = cv2.Sobel(img_mskg, cv2.CV_32F, 1, 0)
img_mskg = cv2.convertScaleAbs(img_mskg)



img_msk = cv2.merge((img_mskg, img_mskg, img_mskg))

img_slm = cv2.bitwise_and(img_src1, img_msk)

cv2.imwrite('picture/img_slm_canny_after.png', img_slm)


#THRESH_BINARY_INVは閾値より大きかったら0、閾値以下の場合は画素値の最大値をとる
#cv2.thresholdの返り値ret(retval)は閾値を返す,大津の2値化を使う場合は自動的に閾値をアルゴリズムが計算し、その値を返す
#この画像だと綺麗にエッジ検出できなかったので、うまく切り取りできなかった