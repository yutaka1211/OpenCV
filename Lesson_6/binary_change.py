import cv2
import numpy as np

img_src = cv2.imread('picture/src.png', 1)
img_gry = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

thresh = 128

for i in range(img_src.shape[0]):
    for j in range(img_src.shape[1]):
        if img_gry[i,j] < thresh:
            img_gry[i,j] = 0
        else:
            img_gry[i,j] = 255

cv2.imwrite('picture/binary_src_myself.png', img_gry)

#グレースケールの画像のみ実行できる

#変数(入力画像,閾値,画素値の最大値,画素値の種類)
ret, img_dst = cv2.threshold(img_src, thresh, 255, cv2.THRESH_BINARY)

cv2.imwrite('picture/binary_src_cv2.png', img_dst)

"""画素値の種類
THRESH_BINARY_INV: 入力画像の過疎地が閾値より大きい場合は0,それ以外は画素値の最大値となる
THRESH_TRUNC:      入力画像の画素値が閾値より大きい場合は閾値、それ以外は変化せず
THRESH_TOZERO:     入力画像が閾値より大きい場合は変化せず、それ以外は0
THRESH_TOZERO_INV: 入力画像の画素値が閾値より大きい場合は0,それ以外は変化せず
"""