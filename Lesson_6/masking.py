import cv2
import numpy as np

img_src = cv2.imread('picture/src.png', 1)

img_msk = cv2.imread('picture/msk.png', 1)

img_msk = cv2.cvtColor(img_msk, cv2.COLOR_BGR2GRAY)

img_dst = cv2.bitwise_and(img_src, img_src, mask = img_msk)

cv2.imwrite('picture/mask_src.png', img_dst)

#マスク画像はグレースケールにしないと実行できない