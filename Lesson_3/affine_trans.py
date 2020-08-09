import cv2
import math
import numpy as np

img_src = cv2.imread('picture/src.png')

size = tuple(np.array([img_src.shape[1], img_src.shape[0]]))

#原点(左上)を中心に45度回転させ、y軸正の方向に画像の高さの半分だけ並行移動する行列の作成
afn_mat = np.float32([[math.cos(-math.pi / 4), -math.sin(-math.pi / 4), 0],
                      [math.sin(-math.pi / 4),  math.cos(-math.pi / 4), img_src.shape[0] * 0.5]])

#変数(画像の写真,変換行列,flags:補間手法)
img_dst = cv2.warpAffine(img_src, afn_mat, size, flags = cv2.INTER_CUBIC)

cv2.imwrite('picture/affine.png', img_dst)

#cv2.warpAffineは写真の位置を移動させる処理


#別解
center = tuple(np.array([img_src.shape[1] * 0.5, img_src.shape[0] * 0.5]))
angle = 45.0
scale = 1.0
size = tuple(np.array([img_src.shape[1], img_src.shape[0]]))
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)

img_dst = cv2.warpAffine(img_src, rot_mat, size, flags = cv2.INTER_CUBIC)