import cv2
import math
import numpy as np

img_src = cv2.imread('picture/moon.png', -1)                                #画像の読み込み
img_gry = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)                         #画像をグレースケールへ変更

img_dst = cv2.resize(img_gry, (img_gry.shape[1], img_gry.shape[0]))         #大きさを元画像の大きさに変更

img_dst = cv2.equalizeHist(img_dst)                                         #グレースケールの画像について均一化を行う

cv2.namedWindow('equ')

cv2.imshow('equ', img_dst)
cv2.imwrite('picture/moon_homo.png', img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#均一化はグレースケールの画像のみに対して実行可能