import cv2
import numpy as np

img_src = cv2.imread('picture/src.png', 1)

k = 0.3

op = np.array([[-k,     -k,    -k],             #オペレータ
               [-k, 1 + 8 * k, -k],             #元画像+(元画像-平滑化画像)*k,ラプラシアンフィルタ:この処理->(元画像-平滑化画像)
               [-k,     -k,    -k]])            #kを大きくすると,輪郭が鮮明になる

#変数(入力画像,出力画像のbit深度(負の値だと、入力画像と同じ),オペレータ)
img_tmp = cv2.filter2D(img_src, -1, op)

img_dst = cv2.convertScaleAbs(img_tmp)

cv2.imwrite('picture/src_shap.png', img_dst)

