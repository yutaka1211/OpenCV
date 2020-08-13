import cv2
import numpy as np
import matplotlib.pyplot as plt

img_src = cv2.imread('picture/with_gecko.JPG', 1)
img_bkg = cv2.imread('picture/without_gecko.JPG', 1)

#変数(変化後の画像、変化前の画像)
img_df = cv2.absdiff(img_src, img_bkg)                          #配列の差の絶対値を返す

ret, img_m = cv2.threshold(img_df, 90, 255, cv2.THRESH_BINARY)

cv2.imwrite('picture/gecko.png', img_m)

plt.imshow(img_m)
plt.colorbar()
plt.show()
