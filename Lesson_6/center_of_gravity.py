import cv2
import numpy as np
import matplotlib.pyplot as plt

img_src = cv2.imread('picture/src1_msk.png', cv2.IMREAD_GRAYSCALE)

#変数(入力画像,true:画素値が0ではないピクセルを全て1,false:不均一な密度のまま)
m = cv2.moments(img_src)                            #グレースケールの画像を元にモーメント計算をする
area = m['m00']
x_g = int(m['m10'] / m['m00'])
y_g = int(m['m01'] / m['m00'])

#変数(入力画像,円の中心座標,円の半径,円の色,円の太さ,円の種類)
cv2.circle(img_src, (x_g, y_g), 4, 100, 2, 4)       #円の描画
plt.imshow(img_src)
plt.colorbar()
plt.show()