import cv2
import numpy as np

"""Sobelでのエッジ検出"""
img_src = cv2.imread('picture/moon.png', 1)

#変数(入力画像,出力画像のbit深度,xで微分した次数,yで微分した次数)
img_temp = cv2.Sobel(img_src, cv2.CV_32F, 1, 0)

img_dst = cv2.convertScaleAbs(img_temp)                 #入力配列の要素を、任意の線形変換によって8 bit符号なし整数に変換

cv2.imwrite('picture/moon_edge.png', img_dst)

#1回微分して、かつ周りの画素値に対しても平滑化を行うことで境界値を判断する
#この方法によりノイズにも対応


"""Laplacianでのエッジ検出"""

#変数(入力画像,出力画像のbit深度,オペレータのサイズ)
img_temp1 = cv2.Laplacian(img_src, cv2.CV_32F, 3)

img_dst1 = cv2.convertScaleAbs(img_temp1)

cv2.imwrite('picture/moon_edge_by_laplacian.png', img_dst1)

#2回微分して、境界値を画素値の正負によって判断する




"""Canny(キャニー)のエッジ検出アルゴリズム"""

#1) ガウシアンオペレータを適用し、エッジをぼかす
#2) Sobelオペレータを適用し画像を微分する
#3) 微分画像を細線化する
#4) 細線化した結果の連結性をあげるために、2つの閾値処理を用いた2値化をおこなう
