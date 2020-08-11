import cv2
import numpy as np

img_src = cv2.imread('picture/src.png', 1)

#変数(入力画像,オペレータのサイズ(形状は正方形),x方向の標準偏差)
img_dst1 = cv2.GaussianBlur(img_src, (11,11), 1)                 #ガウシアンオペレータ処理

#変数(入力画像,オペレータのサイズ(形状は正方形),色空間での標準偏差,距離空間での標準偏差)
img_dst2 = cv2.bilateralFilter(img_src, 11, 50, 100)

cv2.imwrite('picture/gaussian_ope.png', img_dst1)

cv2.imwrite('picture/bilateral_ope.png', img_dst2)


#ガウシアンはノイズが減って、モザイクがかかった
#バイラテラルはノイズが減って、絵の具で書いたようになった