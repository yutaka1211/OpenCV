import cv2
import numpy as np

img_src1 = cv2.imread('picture/src1_msk.png', 1)
img_src1 = cv2.cvtColor(img_src1, cv2.COLOR_BGR2GRAY)

rows = img_src1.shape[0]
cols = img_src1.shape[1]

x_min = cols
x_max = 0
y_min = rows
y_max = 0

for y in range(rows):
    for x in range(cols):
        if img_src1[y,x] == 255:                    #白の幅を探している
            if x < x_min:
                x_min = x
            elif x > x_max:
                x_max = x
            if y < y_min:
                y_min = y
            elif y> y_max:
                y_max = y

aspectratio = float(y_max - y_min) / float(x_max - x_min)

print(aspectratio)


#縦長のブロブほど値が大きくなる
#1.03くらいになったがノイズが乗っているので正しい値ではなさそう
#収縮処理したが、うまく消えなかった