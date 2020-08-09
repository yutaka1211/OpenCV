import cv2
import math
import numpy as np

img_src = cv2.imread('picture/bi-linear.png', -1)

size = tuple(np.array([img_src.shape[1], img_src.shape[0]]))

pts1 = np.float32([[220, 578], [240, 578], [240, 289], [220, 289]])
pts2 = np.float32([[220, 578], [240, 578], [200, 289], [260, 289]])

#変数(入力画像上の対応する四角形の頂点の座標,出力画像上の対応する四角形の頂点の座標)
psp_mat = cv2.getPerspectiveTransform(pts1, pts2)

img_dst = cv2.warpPerspective(img_src, psp_mat, size)

cv2.imwrite('picture/perspect.png', img_dst)
