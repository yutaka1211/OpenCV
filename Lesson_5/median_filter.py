import cv2
import numpy as np

img_src = cv2.imread('picture/src_noise.jpeg', -1)

#変数(入力画像,フィルタのサイズ)
img_dst = cv2.medianBlur(img_src, 9)

cv2.imwrite('picture/median_filter.png', img_dst)


#注目画像の周辺領域(この場合9*9)の画素値をソートしてメジアンをとり、そのメジアンを注目画像の画素値とするフィルタ
#これにより、ゴマが乗ったようなノイズを除去することができる

#ボケてあんま綺麗に消えなかった