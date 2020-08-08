import math
import cv2
import numpy as np

file_src = 'picture/src.png'
file_dst1 = 'picture/rgb_change.png'
file_dst2 = 'picture/hsv.png'
file_dst3 = 'picture/grayscale.png'

img_src = cv2.imread(file_src, 1)

cv2.namedWindow('src')
cv2.namedWindow('rgb_change')
cv2.namedWindow('hsv')
cv2.namedWindow('grayscale')

img_bgr = cv2.split(img_src)                                    #複数色チャンネルの分割
img_dst1 = cv2.merge((img_bgr[2], img_bgr[0], img_bgr[1]))      #青->赤、緑->青、赤->緑へ変換
img_dst2 = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)             #RGBからHSVへ変換
img_dst3 = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)            #RGBからグレースケール画像へ変換

cv2.imshow('src', img_src)
cv2.imshow('rgb_change', img_dst1)
cv2.imshow('hsv', img_dst2)
cv2.imshow('grayscale', img_dst3)

cv2.imwrite(file_dst1, img_dst1)
cv2.imwrite(file_dst2, img_dst2)
cv2.imwrite(file_dst3, img_dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()