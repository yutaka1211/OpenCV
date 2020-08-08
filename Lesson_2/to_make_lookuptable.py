import math
import cv2
import numpy as np

file_src = 'picture/src.png'
file_dst = 'picture/g_correction.png'

img_src = cv2.imread(file_src, -1)

cv2.namedWindow('src')
cv2.namedWindow('g_correction')

#ルックアップテーブル作成
Y = np.ones((256, 1), dtype = 'uint8') * 0              #配列[256][1]の作成、データ型はuint8,*0は配列を0番目にするため
for i in range(256):
    Y[i][0] = 255 * pow(float(i)/255, 1.0 / 1.5)        #ガンマ変換:f(x)=255(x/255)^(1/r)よりr=1.5

#ルックアップテーブル変換
img_dst4 = cv2.LUT(img_src, Y)

cv2.imshow('src', img_src)
cv2.imshow('g_correction', img_dst4)

cv2.imwrite(file_dst, img_dst4)

cv2.waitKey(0)
cv2.destoryAllWindow()

#g_correctionは画像の輝度や色彩を補正する際に使う
#np.ones((2, 3))
#->array([[1., 1., 1.],
#         [1., 1., 1.]])
#配列を作成し、初期値を1で埋める
#dtypeでデータ型を決定できる(初期値はfloat64)
#float64:倍精度浮動小数点型(符号1, 指数11, 仮数52)
#uint8  :符号なし8ビット整数型