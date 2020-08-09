import cv2
import numpy as np

SIZE = 3

#入力画像の読み込み
img_src = cv2.imread('picture/src.png', -1)

#変数(入力画像、リサイズ後の大きさを(w,h)で指定、x方向の倍率、y方向の倍率、補間方法)
img_dst = cv2.resize(img_src, (img_src.shape[1]*SIZE, img_src.shape[0]*SIZE), interpolation = cv2.INTER_LINEAR)
img_dst1= cv2.resize(img_src, (img_src.shape[1]*SIZE, img_src.shape[0]*SIZE), interpolation = cv2.INTER_NEAREST)
img_dst2= cv2.resize(img_src, (img_src.shape[1]*SIZE, img_src.shape[0]*SIZE), interpolation = cv2.INTER_CUBIC)
img_dst3= cv2.resize(img_src, (img_src.shape[1]*SIZE, img_src.shape[0]*SIZE), interpolation = cv2.INTER_LANCZOS4)

cv2.imwrite('picture/bi-linear.png', img_dst)
cv2.imwrite('picture/nearest.png', img_dst1)
cv2.imwrite('picture/cubic.png', img_dst2)
cv2.imwrite('picture/lanczos4.png', img_dst3)


#shape[画像の高さ,　画像の横幅]が格納されている
#src,nearestとbi,cubic,lanczosはパソコンだと少し鮮明になった
#逆にsrcとnearestや、bi,cubic,lanczosに大きな違いは見られなかった
#スマホだとどれも変わらん